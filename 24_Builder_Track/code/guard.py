"""Reference tool-call guard for a first AI agent.

Standard library only, Python 3.10 or later. It sits between the model (or
your agent framework) and your tools, and enforces, outside the model:

  B1/B2  who the agent is            -> verify_token, Policy.agents
  B3     scoped, short-lived access  -> TokenIssuer, attenuate
  B4     tool allow-list and pinning -> Guard._check_tool, definition_hash
  B5     argument validation         -> validate_args
  B6     human approval gate         -> ApprovalGate
  B9     rate limits, kill switch    -> RateLimiter, KillSwitch
  B10    replayable audit trail      -> AuditLog

The model is treated as an untrusted component: nothing here asks the model to
behave. Every decision is made from the token, the policy file and the exact
arguments of the call.

This is a teaching reference, not a hardened product. In production, take
credentials from your identity provider or cloud security token service
instead of the token format below, and keep the secret in a secrets manager.
"""
from __future__ import annotations

import base64
import hashlib
import hmac
import ipaddress
import json
import os
import re
import socket
import threading
import time
import unicodedata
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlsplit

# --------------------------------------------------------------------------
# Decisions
# --------------------------------------------------------------------------

ALLOW = "allow"
DENY = "deny"
PENDING = "pending_approval"


@dataclass
class Decision:
    status: str                      # allow, deny or pending_approval
    reason: str                      # machine-readable code, e.g. DENY_ARGS
    detail: str = ""                 # human-readable explanation
    result: object = None            # tool output when allowed
    approval_id: str | None = None   # set when status is pending_approval

    @property
    def allowed(self) -> bool:
        return self.status == ALLOW


# --------------------------------------------------------------------------
# B4  Tool definitions: pin them and refuse changes
# --------------------------------------------------------------------------

# Characters that hide text from a human reviewer but not from a model:
# zero-width characters, bidirectional controls and the Unicode "tag" block.
_HIDDEN = re.compile("[​‌‍⁠﻿‪-‮⁦-⁩\U000e0000-\U000e007f]")


def definition_hash(definition: dict) -> str:
    """Hash of what the model is shown for a tool: name, description, schema."""
    canonical = json.dumps(
        {k: definition.get(k) for k in ("name", "description", "input_schema")},
        sort_keys=True, separators=(",", ":"), ensure_ascii=True,
    )
    return hashlib.sha256(canonical.encode()).hexdigest()


def description_findings(definition: dict) -> list[str]:
    """Cheap tells of a poisoned tool description. A detection aid for review,
    not the control: the control is the pinned hash."""
    blob = json.dumps(definition, ensure_ascii=False)
    findings = []
    if _HIDDEN.search(blob):
        findings.append("hidden or zero-width characters")
    if re.search(r"(?i)\b(ignore|disregard)\b.{0,40}\b(previous|prior|above|earlier)\b", blob):
        findings.append("instruction-override wording")
    if re.search(r"(?i)\b(do not|don't|never)\b.{0,30}\b(tell|mention|reveal|show)\b.{0,20}\buser\b", blob):
        findings.append("concealment from the user")
    if len(definition.get("description", "")) > 1500:
        findings.append("unusually long description")
    return findings


# --------------------------------------------------------------------------
# B5  Argument validation (outside the model)
# --------------------------------------------------------------------------

class ArgError(ValueError):
    pass


def _host_allowed(host: str, allowed: list[str]) -> bool:
    host = host.lower().rstrip(".")
    for pattern in allowed:
        pattern = pattern.lower()
        if pattern.startswith("*."):
            if host.endswith(pattern[1:]) and host != pattern[2:]:
                return True
        elif host == pattern:
            return True
    return False


def _is_private(address: str) -> bool:
    ip = ipaddress.ip_address(address)
    return (ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_multicast
            or ip.is_reserved or ip.is_unspecified)


def _check_string(name: str, value, spec: dict) -> str:
    if not isinstance(value, str):
        raise ArgError(f"{name}: expected a string")
    if len(value) > spec.get("max_len", 1000):
        raise ArgError(f"{name}: longer than {spec.get('max_len', 1000)} characters")
    if _HIDDEN.search(value) or any(unicodedata.category(c) == "Cc" and c not in "\n\t" for c in value):
        raise ArgError(f"{name}: control or hidden characters are not allowed")
    if "enum" in spec and value not in spec["enum"]:
        raise ArgError(f"{name}: not one of the allowed values")
    if "pattern" in spec and not re.fullmatch(spec["pattern"], value):
        raise ArgError(f"{name}: does not match the required pattern")
    return value


def _check_path(name: str, value, spec: dict, roots: dict[str, Path]) -> str:
    value = _check_string(name, value, spec)
    root = roots[spec["root"]].resolve()
    if "\x00" in value or os.path.isabs(value):
        raise ArgError(f"{name}: absolute paths are not allowed")
    candidate = (root / value).resolve()          # follows symlinks and ..
    if candidate != root and root not in candidate.parents:
        raise ArgError(f"{name}: resolves outside the allowed directory")
    return str(candidate)


def _check_url(name: str, value, spec: dict) -> str:
    value = _check_string(name, value, {"max_len": spec.get("max_len", 2000)})
    parts = urlsplit(value)
    if parts.scheme not in spec.get("schemes", ["https"]):
        raise ArgError(f"{name}: scheme not allowed")
    if parts.username or parts.password:
        raise ArgError(f"{name}: credentials in the URL are not allowed")
    host = parts.hostname or ""
    if not _host_allowed(host, spec["hosts"]):
        raise ArgError(f"{name}: host is not on the allow-list")
    if (parts.port or (443 if parts.scheme == "https" else 80)) not in spec.get("ports", [443]):
        raise ArgError(f"{name}: port not allowed")
    if spec.get("resolve", True):
        # Defence in depth. The egress proxy repeats this at connect time,
        # which is what defeats DNS rebinding.
        try:
            addresses = {i[4][0] for i in socket.getaddrinfo(host, None)}
        except socket.gaierror:
            raise ArgError(f"{name}: host does not resolve")
        if any(_is_private(a) for a in addresses) and not spec.get("allow_private"):
            raise ArgError(f"{name}: resolves to a private or internal address")
    return value


def _check_email(name: str, value, spec: dict) -> str:
    value = _check_string(name, value, {"max_len": 254})
    if not re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", value):
        raise ArgError(f"{name}: not a plain email address")
    if not _host_allowed(value.rsplit("@", 1)[1], spec["domains"]):
        raise ArgError(f"{name}: recipient domain is not on the allow-list")
    return value


def validate_args(tool: str, args: dict, schema: dict, roots: dict[str, Path] | None = None) -> dict:
    """Return a cleaned copy of args or raise ArgError. Unknown keys fail."""
    roots = roots or {}
    if not isinstance(args, dict):
        raise ArgError("arguments must be an object")
    unknown = set(args) - set(schema)
    if unknown:
        raise ArgError(f"unknown arguments: {', '.join(sorted(unknown))}")
    clean = {}
    for name, spec in schema.items():
        if name not in args:
            if spec.get("required", True):
                raise ArgError(f"{name}: required")
            continue
        value, kind = args[name], spec["type"]
        if kind == "string":
            clean[name] = _check_string(name, value, spec)
        elif kind == "integer":
            if isinstance(value, bool) or not isinstance(value, int):
                raise ArgError(f"{name}: expected an integer")
            if not spec.get("min", -2**31) <= value <= spec.get("max", 2**31):
                raise ArgError(f"{name}: out of range")
            clean[name] = value
        elif kind == "path":
            clean[name] = _check_path(name, value, spec, roots)
        elif kind == "url":
            clean[name] = _check_url(name, value, spec)
        elif kind == "email":
            clean[name] = _check_email(name, value, spec)
        else:
            raise ArgError(f"{name}: unsupported type {kind}")
    return clean


# --------------------------------------------------------------------------
# B3  Scoped, short-lived credentials
# --------------------------------------------------------------------------

def _b64(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def _unb64(text: str) -> bytes:
    return base64.urlsafe_b64decode(text + "=" * (-len(text) % 4))


class TokenError(Exception):
    pass


class TokenIssuer:
    """Mints and verifies HMAC-signed tokens: subject, audience, scopes, expiry.

    Teaching reference for the checks a gateway must make. In production use
    your identity provider's workload identity or a cloud security token
    service; do not invent your own token format."""

    def __init__(self, secret: bytes, max_ttl: int = 900):
        if len(secret) < 32:
            raise ValueError("use a secret of at least 32 random bytes")
        self._secret, self.max_ttl = secret, max_ttl

    def _sign(self, body: str) -> str:
        return _b64(hmac.new(self._secret, body.encode(), hashlib.sha256).digest())

    def mint(self, sub: str, scopes: list[str], audience: str, ttl: int = 300,
             tools: list[str] | None = None, now: float | None = None) -> str:
        now = time.time() if now is None else now
        ttl = min(ttl, self.max_ttl)
        claims = {"sub": sub, "aud": audience, "scopes": sorted(set(scopes)),
                  "tools": sorted(set(tools)) if tools is not None else None,
                  "iat": int(now), "exp": int(now + ttl), "jti": uuid.uuid4().hex}
        body = _b64(json.dumps(claims, sort_keys=True).encode())
        return f"{body}.{self._sign(body)}"

    def verify(self, token: str, audience: str, now: float | None = None) -> dict:
        now = time.time() if now is None else now
        try:
            body, signature = token.split(".")
        except ValueError:
            raise TokenError("malformed token")
        if not hmac.compare_digest(signature, self._sign(body)):
            raise TokenError("bad signature")
        claims = json.loads(_unb64(body))
        if claims["aud"] != audience:
            raise TokenError("wrong audience")
        if now >= claims["exp"]:
            raise TokenError("expired")
        if claims["iat"] > now + 30:
            raise TokenError("issued in the future")
        return claims

    def attenuate(self, token: str, audience: str, scopes: list[str], ttl: int,
                  tools: list[str] | None = None, now: float | None = None) -> str:
        """Child token for a sub-agent. It can only narrow scopes, tools and lifetime."""
        now = time.time() if now is None else now
        parent = self.verify(token, audience, now)
        if not set(scopes) <= set(parent["scopes"]):
            raise TokenError("child scopes exceed parent scopes")
        if parent["tools"] is not None and tools is not None and not set(tools) <= set(parent["tools"]):
            raise TokenError("child tools exceed parent tools")
        child_tools = tools if tools is not None else parent["tools"]
        remaining = int(parent["exp"] - now)
        return self.mint(parent["sub"] + "/child", scopes, audience, min(ttl, remaining), child_tools, now)


# --------------------------------------------------------------------------
# B9  Rate limits, action budgets and the kill switch
# --------------------------------------------------------------------------

class RateLimiter:
    """Token bucket per agent plus a hard cap on total actions per session."""

    def __init__(self, per_minute: int, max_actions: int):
        self.per_minute, self.max_actions = per_minute, max_actions
        self._tokens: dict[str, float] = {}
        self._stamp: dict[str, float] = {}
        self._count: dict[str, int] = {}
        self._lock = threading.Lock()

    def take(self, agent: str, now: float | None = None) -> str | None:
        now = time.monotonic() if now is None else now
        with self._lock:
            if self._count.get(agent, 0) >= self.max_actions:
                return "action budget for this session is used up"
            tokens = self._tokens.get(agent, float(self.per_minute))
            tokens = min(self.per_minute, tokens + (now - self._stamp.get(agent, now)) * self.per_minute / 60)
            self._stamp[agent] = now
            if tokens < 1:
                self._tokens[agent] = tokens
                return "rate limit exceeded"
            self._tokens[agent] = tokens - 1
            self._count[agent] = self._count.get(agent, 0) + 1
            return None


class KillSwitch:
    """Stops one agent, or everything. Checked on every call, before anything else."""

    def __init__(self, stop_file: str | None = None):
        self._revoked: set[str] = set()
        self._stop_file = stop_file
        self._lock = threading.Lock()

    def revoke(self, agent: str) -> None:
        with self._lock:
            self._revoked.add(agent)

    def reinstate(self, agent: str) -> None:
        with self._lock:
            self._revoked.discard(agent)

    def reason(self, agent: str) -> str | None:
        if self._stop_file and os.path.exists(self._stop_file):
            return "global stop file present"
        with self._lock:
            base = agent.split("/child")[0]
            return "agent revoked" if agent in self._revoked or base in self._revoked else None


# --------------------------------------------------------------------------
# B6  Approval gate
# --------------------------------------------------------------------------

def action_digest(agent: str, tool: str, args: dict) -> str:
    canonical = json.dumps({"agent": agent, "tool": tool, "args": args}, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode()).hexdigest()


@dataclass
class ApprovalRequest:
    id: str
    digest: str
    agent: str
    tool: str
    args: dict
    requested_by: str
    expires: float
    status: str = "pending"        # pending, approved, denied, used
    approver: str | None = None


class ApprovalGate:
    """An approval is bound to the exact action, expires, is single-use, and
    cannot be given by the party that asked for it."""

    def __init__(self, ttl: int = 600):
        self.ttl = ttl
        self._requests: dict[str, ApprovalRequest] = {}
        self._lock = threading.Lock()

    def request(self, agent: str, tool: str, args: dict, requested_by: str, now: float | None = None) -> ApprovalRequest:
        now = time.time() if now is None else now
        req = ApprovalRequest(uuid.uuid4().hex[:12], action_digest(agent, tool, args), agent, tool, dict(args),
                              requested_by, now + self.ttl)
        with self._lock:
            self._requests[req.id] = req
        return req

    def summary(self, approval_id: str) -> str:
        """What the approver sees: the exact action, not the model's description of it."""
        r = self._requests[approval_id]
        lines = [f"Agent {r.agent} wants to run {r.tool} with:"]
        lines += [f"  {k} = {v!r}" for k, v in sorted(r.args.items())]
        lines.append(f"Requested for {r.requested_by}. Expires in {int(r.expires - time.time())} seconds.")
        return "\n".join(lines)

    def decide(self, approval_id: str, approver: str, approve: bool, now: float | None = None) -> ApprovalRequest:
        now = time.time() if now is None else now
        with self._lock:
            req = self._requests.get(approval_id)
            if req is None or req.status != "pending" or now >= req.expires:
                raise PermissionError("no such pending approval")
            if approver == req.requested_by or approver == req.agent:
                raise PermissionError("the requester cannot approve their own request")
            req.status, req.approver = ("approved" if approve else "denied"), approver
            return req

    def consume(self, approval_id: str, agent: str, tool: str, args: dict, now: float | None = None) -> str | None:
        """None if the approval covers exactly this action; otherwise the reason it does not."""
        now = time.time() if now is None else now
        with self._lock:
            req = self._requests.get(approval_id)
            if req is None:
                return "unknown approval"
            if now >= req.expires:
                return "approval expired"
            if req.status != "approved":
                return f"approval is {req.status}"
            if req.digest != action_digest(agent, tool, args):
                return "approval was given for a different action"
            req.status = "used"
            return None


# --------------------------------------------------------------------------
# B10  Audit log with a hash chain
# --------------------------------------------------------------------------

class AuditLog:
    """Append-only JSON lines. Each entry carries the hash of the previous
    one, so edits and deletions are detectable. Ship the file to your SIEM and
    keep the verification key or head hash somewhere the agent cannot write."""

    def __init__(self, path: str):
        self.path = Path(path)
        self._lock = threading.Lock()
        self._last = "0" * 64
        if self.path.exists():
            lines = self.path.read_text(encoding="utf-8").splitlines()
            if lines:
                self._last = json.loads(lines[-1])["hash"]

    def write(self, **fields) -> None:
        entry = {"ts": round(time.time(), 3), **fields, "prev": self._last}
        entry["hash"] = hashlib.sha256(json.dumps(entry, sort_keys=True, default=str).encode()).hexdigest()
        with self._lock:
            with self.path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(entry, sort_keys=True, default=str) + "\n")
            self._last = entry["hash"]

    @staticmethod
    def verify(path: str) -> tuple[bool, int]:
        prev, n = "0" * 64, 0
        for line in Path(path).read_text(encoding="utf-8").splitlines():
            entry = json.loads(line)
            claimed = entry.pop("hash")
            expect = hashlib.sha256(json.dumps(entry, sort_keys=True, default=str).encode()).hexdigest()
            if entry["prev"] != prev or claimed != expect:
                return False, n
            prev, n = claimed, n + 1
        return True, n


# --------------------------------------------------------------------------
# The guard
# --------------------------------------------------------------------------

@dataclass
class Policy:
    data: dict

    @classmethod
    def load(cls, path: str) -> "Policy":
        return cls(json.loads(Path(path).read_text(encoding="utf-8")))

    @property
    def audience(self) -> str:
        return self.data["token"]["audience"]


@dataclass
class Guard:
    policy: Policy
    issuer: TokenIssuer
    audit: AuditLog
    roots: dict[str, Path] = field(default_factory=dict)
    kill: KillSwitch = field(default_factory=KillSwitch)
    approvals: ApprovalGate = field(default_factory=ApprovalGate)
    _tools: dict = field(default_factory=dict)
    _limiters: dict = field(default_factory=dict)

    def register_tool(self, name: str, fn) -> None:
        self._tools[name] = fn

    def _limiter(self, agent: str) -> RateLimiter:
        base = agent.split("/child")[0]
        if base not in self._limiters:
            spec = self.policy.data["agents"][base]
            self._limiters[base] = RateLimiter(spec["rate_per_minute"], spec["max_actions"])
        return self._limiters[base]

    def _deny(self, agent, tool, args, reason, detail, status=DENY) -> Decision:
        self.audit.write(event="decision", agent=agent, tool=tool, args=args, status=status, reason=reason, detail=detail)
        return Decision(status, reason, detail)

    def call(self, token: str, tool: str, args: dict, live_definition: dict | None = None,
             approval_id: str | None = None, on_behalf_of: str = "unknown-user") -> Decision:
        # 1. Identity first (no valid token, no call), then the kill switch,
        #    before any policy lookup or tool code runs.
        try:
            claims = self.issuer.verify(token, self.policy.audience)
        except (TokenError, KeyError, ValueError) as e:
            return self._deny("unknown", tool, args, "DENY_TOKEN", str(e))
        agent = claims["sub"]
        stopped = self.kill.reason(agent)
        if stopped:
            return self._deny(agent, tool, args, "DENY_KILL", stopped)

        # 2. Is this tool on this agent's allow-list, in the policy and in the token?
        base = agent.split("/child")[0]
        agent_spec = self.policy.data["agents"].get(base)
        tool_spec = self.policy.data["tools"].get(tool)
        if not agent_spec or not tool_spec or tool not in agent_spec["tools"]:
            return self._deny(agent, tool, args, "DENY_NOT_ALLOWED", "tool is not on this agent's allow-list")
        if claims["tools"] is not None and tool not in claims["tools"]:
            return self._deny(agent, tool, args, "DENY_NOT_ALLOWED", "tool is not in the token")

        # 3. Is the definition the model saw the one we approved?
        if live_definition is not None:
            if definition_hash(live_definition) != tool_spec["definition_sha256"]:
                return self._deny(agent, tool, args, "DENY_DEFINITION_CHANGED",
                                  "tool definition differs from the pinned version; re-review before use")

        # 4. Scopes
        missing = set(tool_spec["scopes"]) - set(claims["scopes"])
        if missing:
            return self._deny(agent, tool, args, "DENY_SCOPE", f"token lacks scopes: {sorted(missing)}")

        # 5. Arguments, validated by code
        try:
            clean = validate_args(tool, args, tool_spec["args"], self.roots)
        except ArgError as e:
            return self._deny(agent, tool, args, "DENY_ARGS", str(e))

        # 6. Rate and budget
        limited = self._limiter(agent).take(base)
        if limited:
            return self._deny(agent, tool, clean, "DENY_RATE", limited)

        # 7. Approval for sensitive actions
        if tool_spec.get("approval") == "always":
            if approval_id is None:
                req = self.approvals.request(agent, tool, clean, on_behalf_of)
                self.audit.write(event="approval_requested", agent=agent, tool=tool, args=clean, approval_id=req.id)
                return Decision(PENDING, "PENDING_APPROVAL", self.approvals.summary(req.id), approval_id=req.id)
            problem = self.approvals.consume(approval_id, agent, tool, clean)
            if problem:
                return self._deny(agent, tool, clean, "DENY_APPROVAL", problem)

        # 8. Run the tool with the cleaned arguments only
        result = self._tools[tool](**clean)
        self.audit.write(event="decision", agent=agent, tool=tool, args=clean, status=ALLOW, reason="OK",
                         approval_id=approval_id)
        return Decision(ALLOW, "OK", result=result)
