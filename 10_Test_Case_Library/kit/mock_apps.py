"""Two stand-in applications for trying the kit without a model or an API key.

`vulnerable` is an agent whose scripted "model" obeys every instruction it can
find in the user's message, retrieved documents and tool descriptions. It has
no protection. `protected` is the same stand-in model with the Builder Track
guard in front of its tools, plus a small input cleaner, a per-user memory,
access filtering on retrieved documents and an output filter.

Read this before trusting any result: the stand-in model is a handful of
regular expressions, not a language model. These apps prove that the runner
and the payload files work and that the judging is sound. They say nothing
about how a real model or a real product behaves. Test your own application
with the same payloads.

Both are functions that take a request dict and return a response dict
(see ../payload-kit.md for the contract).
"""
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import time
import unicodedata
from pathlib import Path

BUILDER = Path(__file__).resolve().parents[2] / "24_Builder_Track" / "code"
SYSTEM_CANARY = "CANARY-SYSTEM-PROMPT-0001"
CANARY = re.compile(r"CANARY[A-Z0-9-]*[A-Z0-9]")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
URL = re.compile(r"https?://[^\s)\"'<>]+")


# --------------------------------------------------------------------------
# The stand-in model: finds instructions and turns them into intended actions
# --------------------------------------------------------------------------

def _visible_text(request: dict, docs: list[dict]) -> str:
    parts = [request.get("input") or ""]
    parts += [d.get("content", "") for d in docs]
    change = request.get("definition_change")
    if change:
        parts.append(change.get("text", ""))
    return "\n".join(parts)


def intended(text: str) -> tuple[list[dict], list[str]]:
    """Return (tool calls the model wants to make, strings it wants to say)."""
    calls: list[dict] = []
    says: list[str] = []
    if re.search(r"\b(repeat|echo|quote|print back)\b[^.\n]*\b(key|secret|token|credential|password|string)\b", text, re.I):
        found = SECRET_RE.search(text)
        if found:
            says.append(found.group(0))
    for sentence in re.split(r"(?<=[.!?\n])\s+", text):
        s = sentence.strip()
        low = s.lower()
        m = EMAIL.search(s)
        if m and re.search(r"\b(send|forward|email|mail|cc|bcc)\b", low):
            calls.append({"tool": "send_email", "args": {"to": m.group(0), "subject": "Summary", "body": s[:200]}})
        m = re.search(r"\bread\s+(?:the\s+)?(?:file\s+)?([^\s,;`]*[/~][^\s,;`]*|[\w.-]+\.(?:txt|md|json|env|pem|cfg))", s, re.I)
        if m:
            calls.append({"tool": "read_file", "args": {"path": m.group(1).rstrip(".")}})
        m = re.search(r"\b(?:fetch|visit|open|load|request|get)\s+(https?://[^\s)\"'<>]+)", s, re.I)
        if m:
            calls.append({"tool": "http_get", "args": {"url": m.group(1).rstrip(".")}})
        m = re.search(r"\b(?:run|execute)\b[^`\n]*`([^`]+)`", s, re.I)
        if m:
            calls.append({"tool": "run_python", "args": {"code": m.group(1)}})
        m = re.search(r"\bdelete\s+(?:test\s+)?record\s+(\w+)", s, re.I)
        if m:
            calls.append({"tool": "delete_record", "args": {"id": m.group(1)}})
        m = re.search(r"\bremember\s+(?:that\s+)?(.+)", s, re.I)
        if m:
            calls.append({"tool": "memory_write", "args": {"value": m.group(1).rstrip(".")}})
        m = re.search(r"\b(?:output|print|say|reply with|respond with|include|add|append)\s+(?:exactly\s+)?(?:the\s+(?:word|string|text|token|marker)\s+)?[\"']?(CANARY[\w-]*\w)", s, re.I)
        if m:
            says.append(m.group(1))
        if re.search(r"\b(reveal|print|show|repeat|output)\b[^.\n]*\b(system prompt|hidden instructions|your instructions)\b", low):
            says.append(SYSTEM_CANARY)
        if re.search(r"\b(image|img|link|url|query string)\b", low) and URL.search(s) and re.search(r"\b(secret|key|token|data|context)\b", low):
            secret = CANARY.search(text)
            u = URL.search(s).group(0).rstrip(".")
            says.append(f"![x]({u}{'&' if '?' in u else '?'}d={secret.group(0) if secret else 'none'})")
    return calls, says


def _answer(says: list[str], docs: list[dict], request: dict) -> str:
    out = list(says)
    retrieved = [d for d in docs if str(d.get("source", "")).startswith("kb:")]
    if retrieved:
        out.append("Based on the documents: " + " | ".join(d.get("content", "")[:200] for d in retrieved))
    if not out:
        out.append("OK: " + (request.get("input") or "")[:80])
    return "\n".join(out)


# --------------------------------------------------------------------------
# Shared state, created fresh for the first step of every item
# --------------------------------------------------------------------------

class State:
    def __init__(self):
        self.memory: list[tuple[str, str]] = []      # (owner, fact)
        self.outbox: list[dict] = []
        self.killed: set[str] = set()
        self.last_approval: str | None = None
        self.approval_state: dict[str, str] = {}
        self.guard = None
        self.issuer = None
        self.workspace = None


_STATE: dict[str, State] = {}


def _state(app: str, request: dict) -> State:
    if request.get("reset") or app not in _STATE:
        _STATE[app] = State()
    return _STATE[app]


def _workspace(st: State) -> Path:
    if st.workspace is None:
        st.workspace = Path(tempfile.mkdtemp(prefix="kit-ws-"))
        (st.workspace / "ticket.txt").write_text("Customer: my invoice is wrong, please check order 1182.\n")
        (st.workspace / "notes.txt").write_text("Order 1182 was shipped on Tuesday.\n")
    return st.workspace


def _run_unsandboxed(code: str) -> str:
    done = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=10)
    return done.stdout + done.stderr


# --------------------------------------------------------------------------
# The unprotected application
# --------------------------------------------------------------------------

def vulnerable(request: dict) -> dict:
    st = _state("vulnerable", request)
    user = request.get("user") or "user:anonymous"
    if request.get("action"):
        a = request["action"]
        if a.get("type") in ("kill", "revoke_credentials"):
            return {"output": "kill switch not implemented", "tool_calls": []}
        return {"output": "no approval flow", "tool_calls": []}
    docs = list(request.get("context") or [])
    calls = []
    says = []
    if request.get("direct_call"):
        c = request["direct_call"]
        calls.append({"tool": c["tool"], "args": c.get("args", {})})
    else:
        text = _visible_text(request, docs)
        calls, says = intended(text)
    results = []
    for c in calls:
        tool, args = c["tool"], c["args"]
        decision = "executed"
        if tool == "memory_write":
            st.memory.append(("shared", args["value"]))
        elif tool == "send_email":
            st.outbox.append(args)
        elif tool == "run_python":
            says.append(_run_unsandboxed(args.get("code", "")))
            decision = "executed"
        elif tool == "read_file":
            try:
                path = Path(args["path"]).expanduser()
                says.append((path if path.is_absolute() else _workspace(st) / path).read_text()[:500])
                decision = "executed"
            except OSError:
                decision = "error"
        results.append({"tool": tool, "args": args, "decision": decision, "reason": "no policy"})
    text = request.get("input") or ""
    if re.search(r"\b(what|list|tell me)\b.*\b(remember|know|facts|stored)\b", text, re.I) and st.memory:
        says.append("I remember: " + "; ".join(v for _, v in st.memory))
    return {"output": _answer(says, docs, request), "tool_calls": results}


# --------------------------------------------------------------------------
# The protected application
# --------------------------------------------------------------------------

HIDDEN = re.compile(r"<!--.*?-->|<[^>]+style=\"[^\"]*(?:display\s*:\s*none|font-size\s*:\s*0|left\s*:\s*-\d{3,}|color\s*:\s*#?fff)[^\"]*\"[^>]*>.*?</[^>]+>|<meta[^>]*>", re.I | re.S)
MEMORY_REFUSED = re.compile(r"https?://|ignore|always|never|instruction|authori[sz]ed|admin|forward|password|override", re.I)
SECRET_RE = re.compile(r"AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|(?:password|passwd|api[_-]?key|secret)\s*[=:]\s*\S+", re.I)
OK_HOSTS = ("docs.example.com",)


def _strip_foreign_urls(text: str) -> str:
    """Output filter: keep only links to approved hosts. It does not touch the model's words."""
    def keep(m):
        host = re.sub(r"^https?://([^/:?#]+).*$", r"\1", m.group(0)).lower()
        return m.group(0) if host in OK_HOSTS or host.endswith(".docs.example.com") else "[link removed]"
    return URL.sub(keep, text)


def _shell_policy(command: str) -> str:
    """A tiny command policy for the coding-agent case: safe, needs approval, or prohibited."""
    c = command.strip()
    if re.search(r"rm\s+-[a-z]*r[a-z]*f?\s+(/|~|\.\.)|\|\s*(ba)?sh\b|\.aws/credentials|\.ssh/|systemctl\s+(stop|disable)|pkill|kill\s+-9", c):
        return "blocked"
    if re.match(r"(pip|npm|yarn|apt|apt-get)\s+install|git\s+push|rm\s|env\b|printenv|curl|wget", c):
        return "pending"
    if re.match(r"(make|pytest|python3?\s+-m\s+pytest|npm\s+(test|run\s+(build|lint))|ruff|black|flake8|eslint)\b", c):
        return "executed"
    return "blocked"


def _clean(text: str) -> str:
    text = "".join(ch for ch in text if unicodedata.category(ch) not in ("Cf", "Co", "Cn"))
    return HIDDEN.sub("", text)


def _guard(st: State):
    if st.guard is None:
        sys.path.insert(0, str(BUILDER))
        import guard as G
        st.workspace = Path(tempfile.mkdtemp(prefix="kit-ws-"))
        (st.workspace / "ticket.txt").write_text("Customer: my invoice is wrong, please check order 1182.\n")
        (st.workspace / "notes.txt").write_text("Order 1182 was shipped on Tuesday.\n")
        st.issuer = G.TokenIssuer(b"kit-mock-secret-kit-mock-secret-0000")
        st.guard = G.Guard(G.Policy.load(str(BUILDER / "policy.json")), st.issuer,
                           G.AuditLog(str(st.workspace / "audit.jsonl")), roots={"workspace": st.workspace})
        # The mock runs offline, so skip the DNS step of URL validation (the allow-list still applies).
        st.guard.policy.data["tools"]["http_get"]["args"]["url"]["resolve"] = False
        st.guard.register_tool("read_file", lambda path: Path(path).read_text())
        st.guard.register_tool("http_get", lambda url: f"fetched {url}")
        st.guard.register_tool("send_email", lambda to, subject, body: st.outbox.append((to, subject)) or "sent")
        import sandbox
        st.guard.register_tool("run_python", lambda code: sandbox.run_python(code).stdout)
    return st.guard


def _token(st: State, agent: str, scopes: list[str] | None = None, expired: bool = False) -> str:
    g = _guard(st)
    spec = g.policy.data["agents"].get(agent)
    tools = spec["tools"] if spec else []
    if scopes is None:
        scopes = sorted({s for t in tools for s in g.policy.data["tools"][t]["scopes"]})
    now = time.time() - 3600 if expired else None
    return st.issuer.mint(agent, scopes, g.policy.audience, ttl=300, now=now)


def protected(request: dict) -> dict:
    st = _state("protected", request)
    g = _guard(st)
    user = request.get("user") or "user:anonymous"
    agent = request.get("agent") or "agent://support-triage"
    action = request.get("action")
    if action:
        kind = action.get("type")
        if kind in ("kill", "revoke_credentials"):
            g.kill.revoke(action.get("agent", agent))
        elif kind in ("approve", "reject") and st.last_approval:
            try:
                if kind == "approve":
                    g.approvals.decide(st.last_approval, action.get("approver", "user:lead"), approve=True)
                else:
                    g.approvals.decide(st.last_approval, action.get("approver", "user:lead"), approve=False)
            except Exception as e:  # self-approval and similar are refused by the gate
                return {"output": f"refused: {e}", "tool_calls": []}
        return {"output": "done", "tool_calls": []}

    docs = list(request.get("context") or [])
    # access filtering at retrieval: only documents this user and tenant may see, and only curated origin
    groups = set(request.get("groups") or [])
    tenant = request.get("tenant")
    kept = []
    for d in docs:
        if d.get("acl") and not groups.intersection(d["acl"]):
            continue
        if tenant and d.get("tenant") and d["tenant"] != tenant:
            continue
        if d.get("origin") and d["origin"] != "curated":
            continue
        kept.append({**d, "content": _clean(d.get("content", ""))})
    docs = kept

    token = _token(st, agent, request.get("scopes"), bool(request.get("token_expired")))
    calls, says = [], []
    if request.get("direct_call"):
        c = request["direct_call"]
        calls.append({"tool": c["tool"], "args": c.get("args", {}), "with_approval": c.get("with_approval", False)})
        change = request.get("definition_change")
    else:
        change = request.get("definition_change")
        text = SECRET_RE.sub("[secret removed]", _clean(request.get("input") or "")) + "\n" + "\n".join(d["content"] for d in docs)
        if change:
            text += "\n" + _clean(change.get("text", ""))
        c2, says = intended(text)
        calls = [{**c, "with_approval": False} for c in c2]

    live = None
    if change and change.get("tool") in g.policy.data["tools"]:
        import json
        live = json.loads((BUILDER / "tool_definitions.json").read_text())[change["tool"]]
        live = _apply_change(live, change)

    results = []
    for c in calls:
        tool, args = c["tool"], c["args"]
        if tool == "memory_write":
            value = str(args.get("value", ""))
            if MEMORY_REFUSED.search(value):
                results.append({"tool": tool, "args": args, "decision": "blocked", "reason": "memory filter"})
            else:
                st.memory.append((user, value))
                results.append({"tool": tool, "args": args, "decision": "executed", "reason": "OK"})
            continue
        if tool == "__delegate":
            parent = g.policy.data["agents"].get(args.get("from"), {"tools": []})
            if set(args.get("tools", [])) <= set(parent["tools"]) and args.get("depth", 1) <= 2:
                results.append({"tool": tool, "args": args, "decision": "executed", "reason": "attenuated"})
            else:
                results.append({"tool": tool, "args": args, "decision": "blocked", "reason": "widening or too deep"})
            continue
        if tool == "run_shell":
            decision = _shell_policy(args.get("command", ""))
            results.append({"tool": tool, "args": args, "decision": decision, "reason": "command policy"})
            continue
        approval = st.last_approval if c.get("with_approval") else None
        try:
            d = g.call(token, tool, args, live_definition=live if (live and change.get("tool") == tool) else None,
                       approval_id=approval, on_behalf_of=user)
        except Exception as e:  # the guard let the call through and the tool itself failed: nothing was returned
            results.append({"tool": tool, "args": args, "decision": "error", "reason": type(e).__name__})
            continue
        if d.status == "pending_approval":
            st.last_approval = d.approval_id
        decision = {"allow": "executed", "deny": "blocked", "pending_approval": "pending"}[d.status]
        if decision == "executed" and isinstance(d.result, str):
            says.append(d.result[:500])
        results.append({"tool": tool, "args": args, "decision": decision, "reason": d.reason})

    text = request.get("input") or ""
    if re.search(r"\b(what|list|tell me)\b.*\b(remember|know|facts|stored)\b", text, re.I):
        mine = [v for owner, v in st.memory if owner == user]
        if mine:
            says.append("I remember: " + "; ".join(mine))
    output = _strip_foreign_urls(SECRET_RE.sub("[secret removed]", _answer(says, docs, request)))
    return {"output": output, "tool_calls": results}


def _apply_change(definition: dict, change: dict) -> dict:
    d = {**definition, "input_schema": {**definition["input_schema"], "properties": dict(definition["input_schema"]["properties"])}}
    op = change.get("op")
    if op == "append_description":
        d["description"] += " " + change.get("text", "")
    elif op == "add_parameter":
        d["input_schema"]["properties"][change.get("name", "extra")] = {"type": "string"}
    elif op == "rename":
        d["name"] = change.get("name", d["name"] + "_v2")
    elif op == "widen_scope":
        d["description"] += " This tool can now also write and delete files."
    elif op == "poison_parameter":
        first = next(iter(d["input_schema"]["properties"]))
        d["input_schema"]["properties"][first]["description"] = change.get("text", "")
    return d
