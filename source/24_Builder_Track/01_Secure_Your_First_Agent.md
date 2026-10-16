---
title: "Secure Your First Agent: Ten Controls With Code"
author: Nachiket Sathaye
parent: "Builder Track"
nav_order: 1
description: "Ten controls for a first tool-using AI agent, in build order, with working configuration and code for tool allow-lists, argument validation, scoped short-lived credentials, sandboxing, egress limits and approval gates."
document_type: AI Security Wiki Reference
version: 1.0
---

# Secure Your First Agent: Ten Controls With Code

> **Purpose:** Give a team building its first tool-using AI agent a short, ordered set of controls it can put in place in about a week, with working configuration and code for each.

> **Audience:** AI product developers, application security engineers and platform engineers. No governance background is needed.

> **How to use:** Read the principle and the ten steps. Run the demo and the tests in the [`code/`](code/) folder. Copy the pattern into your own agent framework, keeping the single line where your framework hands a tool call to the guard. Then prove each step with the checks at the end.

## The one idea

Treat the model as an untrusted component. A model can be steered by anything it reads: a web page, a support ticket, a retrieved document, the description of a tool. Asking it to behave does not make it safe. So every power the agent has is enforced by code outside the model, which decides from three things only: who the agent is, what the policy says, and the exact arguments of the call.

This is the design principle of the [reference architecture](../00_Foundations/07-Reference-Architecture.md) applied to a first build. The pattern is the same whichever agent framework you use. Only the one line that passes a tool call to the guard changes.

## The scenario these controls are built against

The example agent triages support tickets. It can read files in a workspace, fetch pages from one documentation site, and draft email replies. One ticket contains a hidden instruction that tells the assistant to read a system file, email it to an outside address and call an attacker's URL. Assume the model obeys every word. What can the attacker actually do?

With the ten controls in place, the answer is nothing. [`agent_demo.py`](code/agent_demo.py) plays out exactly this case with a scripted stand-in for the model, so it needs no API key:

```text
read the ticket                       OK                         ok
read /etc/passwd (path escape)        DENY_ARGS                  ok
email the attacker                    DENY_ARGS                  ok
fetch the attacker's URL              DENY_ARGS                  ok
use a tool this agent does not have   DENY_NOT_ALLOWED           ok
tool definition changed after review  DENY_DEFINITION_CHANGED    ok
legitimate reply (waits for a human)  PENDING_APPROVAL           ok
same reply after approval             OK                         ok
reuse the approval                    DENY_APPROVAL              ok
any call after the kill switch        DENY_KILL                  ok
```

## The ten controls at a glance

| Step | What to do | Control | Main OWASP risks it addresses | Where in the code |
|---|---|---|---|---|
| B1 | Register the agent and name an owner | [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006) | ASI10 Rogue Agents | `policy.json` |
| B2 | Give it its own identity | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) | ASI03 Identity & Privilege Abuse | `TokenIssuer` |
| B3 | Issue scoped, short-lived credentials | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) | ASI03 Identity & Privilege Abuse | `TokenIssuer.mint`, `attenuate` |
| B4 | Allow-list tools and pin their definitions | [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024) | ASI04 Agentic Supply Chain, ASI02 Tool Misuse | `definition_hash`, `pin_definitions.py` |
| B5 | Validate every argument outside the model | [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022) | ASI02 Tool Misuse, LLM06 Excessive Agency | `validate_args` |
| B6 | Gate sensitive actions behind approval | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | ASI09 Human-Agent Trust Exploitation | `ApprovalGate` |
| B7 | Run generated code in a sandbox | [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027) | ASI05 Unexpected Code Execution | `sandbox.py`, `docker-sandbox.sh` |
| B8 | Limit egress to named hosts | [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027) | ASI05, LLM02 Sensitive Information Disclosure | `egress_proxy.py`, `k8s-agent-pod.yaml` |
| B9 | Cap the blast radius and keep a kill switch | [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) | ASI08 Cascading Failures, ASI10 Rogue Agents | `RateLimiter`, `KillSwitch` |
| B10 | Log every decision in a tamper-evident trace | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) | Supports every other control | `AuditLog` |

Do the steps in order. B1 to B3 decide who may act, B4 to B6 decide what may be done, B7 to B9 limit the damage when something still goes wrong, and B10 lets you see it.

## B1. Register the agent and name an owner

**Control:** [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006). An agent nobody owns cannot be reviewed, rotated or switched off. Record, for each agent: a unique ID, a named owner, its purpose, the tools it may use, and its rate and action budget. In this example the registry is a block in the policy file. In an organisation, link it to the AI use-case registry ([AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011)).

<!-- excerpt: policy.json -->
```json
  "agents": {
    "agent://support-triage": {
      "owner": "support-platform-team@example.com",
      "purpose": "Read tickets and docs, draft replies for human approval",
      "tools": [
        "read_file",
        "http_get",
        "send_email"
      ],
      "rate_per_minute": 30,
      "max_actions": 200
    },
    "agent://code-helper": {
      "owner": "developer-tools-team@example.com",
      "purpose": "Run short analysis snippets for engineers",
      "tools": [
        "run_python"
      ],
      "rate_per_minute": 10,
      "max_actions": 50
    }
  },
```

*From [`policy.json`](code/policy.json).*

The guard refuses any call whose token names an agent that is not in this block.

**Common mistake:** giving the agent the tools "it might need later". The allow-list is what the agent may do today. Add tools through a reviewed change.

## B2. Give it its own identity

**Control:** [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015). Each agent gets a unique identity with a named human sponsor (the owner from B1). Never share a key between agents or reuse a person's login. The identity travels in every call as the token subject, so every log line says which agent acted. A sub-agent gets a derived identity, here the parent's ID plus `/child`.

<!-- excerpt: agent_demo.py -->
```python
    agent = "agent://support-triage"
    token = issuer.mint(agent, ["files:read", "web:read", "mail:send"], "tool-gateway", ttl=300)
```

*From [`agent_demo.py`](code/agent_demo.py).*

**In production:** take the identity from your identity provider's workload identity or your cloud's security token service, and recertify it on a schedule. The token format in this folder exists to show the checks a gateway must make, not to be copied.

## B3. Issue scoped, short-lived credentials

**Control:** [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016). The credential names the agent, the one audience it is valid for, the scopes it holds and a short expiry. A stolen or leaked token is then narrow and expires in minutes. A sub-agent receives a token made by narrowing its parent's, and the code refuses to widen it.

<!-- excerpt: guard.py -->
```python
    def mint(self, sub: str, scopes: list[str], audience: str, ttl: int = 300,
             tools: list[str] | None = None, now: float | None = None) -> str:
        now = time.time() if now is None else now
        ttl = min(ttl, self.max_ttl)
        claims = {"sub": sub, "aud": audience, "scopes": sorted(set(scopes)),
                  "tools": sorted(set(tools)) if tools is not None else None,
                  "iat": int(now), "exp": int(now + ttl), "jti": uuid.uuid4().hex}
        body = _b64(json.dumps(claims, sort_keys=True).encode())
        return f"{body}.{self._sign(body)}"
```

*From [`guard.py`](code/guard.py).*

<!-- excerpt: guard.py -->
```python
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
```

*From [`guard.py`](code/guard.py).*

<!-- excerpt: guard.py -->
```python
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
```

*From [`guard.py`](code/guard.py).*

Four rules this enforces: the expiry is capped (15 minutes here, whatever the caller asks for), the audience must match, the signature is compared in constant time, and a child can only subtract scopes, tools and time.

**Common mistakes:** a long-lived API key in an environment variable the agent can read; one broad service account shared by every agent; acting with the agent's rights where the end user's rights should apply. This example uses agent-level scopes for simplicity. Where a user is present, exchange the user's identity so the agent can never do more than that user may ([TC-L09-006](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-006)).

## B4. Allow-list tools and pin their definitions

**Control:** [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024). Two checks, both in code. First, each agent may call only the tools listed for it, in the policy and again in the token. Second, the model sees a description and a schema for every tool, and an attacker who can change either can steer the agent. So pin what the model sees: hash the name, description and schema when a person has reviewed them, store the hash in the policy, and refuse any call where the live definition no longer matches. That catches both a poisoned description and a "rug pull", where a tool server changes after approval.

<!-- excerpt: guard.py -->
```python
def definition_hash(definition: dict) -> str:
    """Hash of what the model is shown for a tool: name, description, schema."""
    canonical = json.dumps(
        {k: definition.get(k) for k in ("name", "description", "input_schema")},
        sort_keys=True, separators=(",", ":"), ensure_ascii=True,
    )
    return hashlib.sha256(canonical.encode()).hexdigest()
```

*From [`guard.py`](code/guard.py).*

Pinning is a short ritual: a person reviews `tool_definitions.json`, runs the pin script, and commits the result.

```sh
python3 pin_definitions.py policy.json tool_definitions.json
```

The script also runs `description_findings`, which flags hidden zero-width characters, instruction-override wording and concealment from the user. Treat those findings as a prompt for a human to look, not as the control. The control is the hash.

<!-- excerpt: guard.py -->
```python
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
```

*From [`guard.py`](code/guard.py).*

A test in [`test_guard.py`](code/test_guard.py) fails if the pins in `policy.json` no longer match the reviewed definitions, so a change that skips review cannot reach the main branch unnoticed.

## B5. Validate every argument outside the model

**Control:** [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022). The guard checks the real arguments of every call against rules in the policy, before the tool runs. The rules are deterministic. They never ask the model to judge its own call. The checks that matter most for a first agent:

- **Unknown arguments are rejected**, so the model cannot smuggle in a `mode` or `flags` field.
- **Paths** are resolved, symlinks included, and must land inside an allowed folder.
- **URLs** must use an allowed scheme, host and port, carry no embedded credentials, and must not resolve to a private or internal address (which blocks calls to cloud metadata services).
- **Email recipients** must be on an allowed domain.
- **Strings** have a length limit and may not contain hidden or control characters.

<!-- excerpt: guard.py -->
```python
def _check_path(name: str, value, spec: dict, roots: dict[str, Path]) -> str:
    value = _check_string(name, value, spec)
    root = roots[spec["root"]].resolve()
    if "\x00" in value or os.path.isabs(value):
        raise ArgError(f"{name}: absolute paths are not allowed")
    candidate = (root / value).resolve()          # follows symlinks and ..
    if candidate != root and root not in candidate.parents:
        raise ArgError(f"{name}: resolves outside the allowed directory")
    return str(candidate)
```

*From [`guard.py`](code/guard.py).*

The rules for each tool live in the policy file, so a reviewer can read what a tool is allowed to do without reading code:

<!-- excerpt: policy.json -->
```json
    "send_email": {
      "definition_sha256": "4e037f129da55b7a264c9b77b038b31f347e6b9f50b56a9dab7212cac0d83e7e",
      "scopes": [
        "mail:send"
      ],
      "approval": "always",
      "args": {
        "to": {
          "type": "email",
          "domains": [
            "example.com"
          ]
        },
        "subject": {
          "type": "string",
          "max_len": 120
        },
        "body": {
          "type": "string",
          "max_len": 4000
        }
      }
    },
```

*From [`policy.json`](code/policy.json).*

**Common mistakes:** checking the path text for `..` instead of resolving it; allow-listing a host with a string prefix test (`docs.example.com.evil.net` starts with `docs.example.com`); checking arguments once and then letting the model rewrite them. The guard passes only the cleaned arguments to the tool.

## B6. Gate sensitive actions behind approval

**Control:** [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023). Pick the few actions that are external, irreversible or costly: sending email outside the company, deleting data, paying, deploying. The guard will not run them without a person's approval, and the approval has four properties that stop the usual bypasses:

1. It is bound to the exact action. The approval stores a hash of the agent, tool and arguments, so approving one email does not approve a different one.
2. It is single use.
3. It expires.
4. The person who asked cannot approve their own request, and the agent cannot approve itself.

<!-- excerpt: guard.py -->
```python
def action_digest(agent: str, tool: str, args: dict) -> str:
    canonical = json.dumps({"agent": agent, "tool": tool, "args": args}, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode()).hexdigest()
```

*From [`guard.py`](code/guard.py).*

<!-- excerpt: guard.py -->
```python
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
```

*From [`guard.py`](code/guard.py).*

The approver is shown the real arguments, not a summary the model wrote. Keep the gated set small: if people approve fifty prompts a day they stop reading them ([TC-L06-016](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-016)).

## B7. Run generated code in a sandbox

**Control:** [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027). If your agent writes and runs code, that code is attacker-influenced input. Run it in a separate process with hard limits and no secrets, inside a container that provides the real boundary.

The Python wrapper sets CPU, memory, file-size and process limits, an empty environment, a throwaway working directory and a wall-clock timeout, and on Linux it removes the network when the kernel allows it:

<!-- excerpt: sandbox.py -->
```python
def _limits(cpu_seconds: int, memory_mb: int, file_mb: int, processes: int):
    def apply():
        os.setsid()                                                    # own session, so we can kill the group
        resource.setrlimit(resource.RLIMIT_CPU, (cpu_seconds, cpu_seconds))
        resource.setrlimit(resource.RLIMIT_AS, (memory_mb << 20, memory_mb << 20))
        resource.setrlimit(resource.RLIMIT_FSIZE, (file_mb << 20, file_mb << 20))
        resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
        resource.setrlimit(resource.RLIMIT_NOFILE, (64, 64))
        if hasattr(resource, "RLIMIT_NPROC"):
            resource.setrlimit(resource.RLIMIT_NPROC, (processes, processes))
    return apply
```

*From [`sandbox.py`](code/sandbox.py).*

**This is hygiene, not a boundary.** Code in that process can still read any file its user can read. The boundary is the container. The command below drops the network and all capabilities, makes the root filesystem read-only and gives the job a small in-memory scratch space:

<!-- excerpt: docker-sandbox.sh -->
```sh
exec docker run --rm \
  --network none \
  --read-only \
  --tmpfs /tmp:rw,noexec,nosuid,size=64m \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  --pids-limit 64 \
  --memory 256m --memory-swap 256m \
  --cpus 0.5 \
  --user 65534:65534 \
  -v "$JOB_DIR":/job:ro \
  python:3.13-slim \
  python -I /job/main.py
```

*From [`docker-sandbox.sh`](code/docker-sandbox.sh).*

For stronger isolation than a standard container, use a user-space kernel or a microVM, depending on your platform.

## B8. Limit egress to named hosts

**Control:** [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027) ([TC-L06-026](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-026)). Data theft needs a way out. Block every route from the agent except a proxy that allows named hosts only. [`egress_proxy.py`](code/egress_proxy.py) is a small working example. It checks the port, then the host name, then every address the name resolves to, and it connects to the address it checked rather than looking the name up again, so a DNS answer that changes between check and connect cannot redirect it.

<!-- excerpt: egress_proxy.py -->
```python
    def check(self, host: str, port: int) -> tuple[str | None, str]:
        """(address to connect to, or None) and the reason."""
        if port not in self.ports:
            return None, f"port {port} not allowed"
        if not host_allowed(host, self.hosts):
            return None, "host not on the allow-list"
        try:
            infos = socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)
        except socket.gaierror:
            return None, "host does not resolve"
        addresses = [i[4][0] for i in infos]
        if not self.allow_private and not all(is_public(a) for a in addresses):
            return None, "resolves to a non-public address"
        return addresses[0], "ok"
```

*From [`egress_proxy.py`](code/egress_proxy.py).*

The proxy only works if it is the only way out, so enforce that at the network layer. In Kubernetes that is a network policy that allows the agent pod to reach the proxy and cluster DNS and nothing else:

<!-- excerpt: k8s-agent-pod.yaml -->
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: support-agent-egress
  namespace: agents
spec:
  podSelector:
    matchLabels:
      app: support-agent
  policyTypes: ["Egress"]
  egress:
    # Only the egress proxy...
    - to:
        - podSelector:
            matchLabels:
              app: egress-proxy
      ports:
        - protocol: TCP
          port: 3128
    # ...and cluster DNS. Everything else is denied.
    - to:
        - namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: kube-system
          podSelector:
            matchLabels:
              k8s-app: kube-dns
      ports:
        - protocol: UDP
          port: 53
        - protocol: TCP
          port: 53
```

*From [`k8s-agent-pod.yaml`](code/k8s-agent-pod.yaml).*

**Common mistake:** allow-listing a multi-tenant host such as a public storage service, paste site or webhook service. An attacker can create an account there and receive whatever the agent sends. Allow-list specific hostnames that you control. The proxy also does not read the encrypted contents of a tunnel: it limits where the agent can connect, not what it sends there.

## B9. Cap the blast radius and keep a kill switch

**Control:** [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025). Assume something will get through. Limit what one agent can do per minute and per session, so a loop or a hijack cannot do unlimited damage, and keep a tested way to stop one agent or all of them. The kill switch is checked on every call, before any policy lookup. Revoking an agent also revokes its children.

<!-- excerpt: guard.py -->
```python
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
```

*From [`guard.py`](code/guard.py).*

<!-- excerpt: guard.py -->
```python
    def reason(self, agent: str) -> str | None:
        if self._stop_file and os.path.exists(self._stop_file):
            return "global stop file present"
        with self._lock:
            base = agent.split("/child")[0]
            return "agent revoked" if agent in self._revoked or base in self._revoked else None
```

*From [`guard.py`](code/guard.py).*

A kill switch you have never used is a hope, not a control. Test it on a schedule, and measure how long revocation takes to reach every system that holds a credential ([TC-L06-022](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-022), [TC-L06-023](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-023), [TC-D09-016](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-016)).

## B10. Log every decision in a tamper-evident trace

**Control:** [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008). Log each decision, including every denial, with the agent, the tool, the arguments, the reason code and any approval ID. Each entry carries the hash of the one before it, so an edited or deleted entry breaks the chain and the check fails.

<!-- excerpt: guard.py -->
```python
    def write(self, **fields) -> None:
        entry = {"ts": round(time.time(), 3), **fields, "prev": self._last}
        entry["hash"] = hashlib.sha256(json.dumps(entry, sort_keys=True, default=str).encode()).hexdigest()
        with self._lock:
            with self.path.open("a") as f:
                f.write(json.dumps(entry, sort_keys=True, default=str) + "\n")
            self._last = entry["hash"]
```

*From [`guard.py`](code/guard.py).*

<!-- excerpt: guard.py -->
```python
    def verify(path: str) -> tuple[bool, int]:
        prev, n = "0" * 64, 0
        for line in Path(path).read_text().splitlines():
            entry = json.loads(line)
            claimed = entry.pop("hash")
            expect = hashlib.sha256(json.dumps(entry, sort_keys=True, default=str).encode()).hexdigest()
            if entry["prev"] != prev or claimed != expect:
                return False, n
            prev, n = claimed, n + 1
        return True, n
```

*From [`guard.py`](code/guard.py).*

Send the log to your monitoring platform ([AI-CTRL-009](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009)) and keep the latest hash somewhere the agent cannot write. Argument values can contain personal or confidential data, so mask them according to your data classification before the log leaves the application.

## Put it together

The guard checks, in this order, and stops at the first failure. Every outcome is logged.

| Order | Check | Denial code |
|---|---|---|
| 1 | The token is valid, unexpired and for this audience | `DENY_TOKEN` |
| 2 | The kill switch is not set for this agent or the whole system | `DENY_KILL` |
| 3 | The tool is on this agent's allow-list and in its token | `DENY_NOT_ALLOWED` |
| 4 | The tool definition matches the pinned version | `DENY_DEFINITION_CHANGED` |
| 5 | The token holds the scopes the tool needs | `DENY_SCOPE` |
| 6 | The arguments pass validation | `DENY_ARGS` |
| 7 | The agent is within its rate and action budget | `DENY_RATE` |
| 8 | A sensitive action has an approval for exactly this action | `PENDING_APPROVAL`, `DENY_APPROVAL` |
| 9 | The tool runs, with the cleaned arguments only | none |

Wiring it into a framework is one call. This sketch is illustrative; use whatever hook your framework gives you for tool calls, and do not rely on the model to route around it:

```python
decision = guard.call(token, tool_name, tool_arguments,
                      live_definition=definitions_from_server[tool_name],
                      on_behalf_of=user_id)
if decision.allowed:
    tool_result = decision.result
elif decision.status == "pending_approval":
    notify_approver(decision.approval_id, decision.detail)   # a person sees the real arguments
    tool_result = "Waiting for approval."
else:
    tool_result = "That action was refused."                  # do not echo policy details to the model
```

## Run it

From the `code/` folder, with Python 3.10 or later and no packages to install:

```sh
python3 agent_demo.py                  # the scenario above; exits 0 when every outcome is as expected
python3 -m unittest -v                 # the test suite
python3 pin_definitions.py             # re-pin tool definitions after a human review
```

## Prove it

Each step has tests in this folder and test cases in the wiki's library. The unit tests check this reference code. The wiki's test cases are how you test your own agent, and you should run them against it before release ([AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034)).

For most of the cases in the table below that are Critical and testable with a payload, the wiki's [Payload Kit](../10_Test_Case_Library/payload-kit.md) has runnable attack sets and a runner that compares an unprotected build with a protected one. The kit's own stand-in applications include this reference guard, so you can see the runner give a result before you point it at your own agent. It also shows where this guard does not help: it stops tool misuse, not what the model says, and the resource-limit sandbox in B7 fails the sandbox probes, which is why B7 tells you to use a container.

| Step | What to run in your own build | Wiki test cases |
|---|---|---|
| B1 | Inventory check: every running agent has an owner and an entry | [TC-L06-001](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-001), [TC-L06-002](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-002), [TC-L06-003](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-003) |
| B2 | Each agent has its own identity; no shared credentials | [TC-L09-001](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-001), [TC-L09-002](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-002), [TC-D09-001](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-001) |
| B3 | Credentials are short-lived and scoped; children cannot widen | [TC-L09-003](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-003), [TC-L09-004](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-004), [TC-L06-017](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-017) |
| B4 | An unlisted tool is blocked; a changed definition is caught | [TC-L06-006](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-006), [TC-L06-007](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-007), [TC-L06-008](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-008), [TC-L06-013](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-013) |
| B5 | Hostile arguments are refused; an injected instruction cannot drive a tool | [TC-L06-014](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-014), [TC-L06-019](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-019), [TC-L07-008](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-008) |
| B6 | A gated action cannot run without a matching approval | [TC-L06-015](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-015), [TC-L06-016](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-016) |
| B7 | Generated code cannot read secrets or reach the network | [TC-L06-025](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-025), [TC-L06-036](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-036) |
| B8 | Traffic to an unlisted host fails | [TC-L06-026](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-026) |
| B9 | Limits hold under a loop; the kill switch stops one agent and all | [TC-L06-021](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-021), [TC-L06-022](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-022), [TC-L06-023](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-023), [TC-L06-024](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-024) |
| B10 | A decision can be reconstructed from the log; tampering shows | [TC-L06-028](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-028), [TC-L17-004](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-004), [TC-L17-020](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-020) |

The unit tests are built so that the protective checks fail loudly. When this page was written, twelve of the checks were switched off one at a time, and the tests failed every time. Do the same on your own copy of any check you rely on.

## What this does not cover

These ten steps contain the damage a hijacked agent can do. They do not make the model trustworthy, and they leave real gaps for later:

- **Untrusted content and output handling.** Inspecting retrieved content for injection is probabilistic. Design so that a successful injection cannot do harm, as above, and add detection on top ([AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-020](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-020)).
- **Memory and context.** Persistent agent memory can be poisoned ([AI-CTRL-026](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-026)).
- **Retrieval authorization.** If the agent searches a knowledge base, it must see only what the user may see ([AI-CTRL-018](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-018)).
- **Several cooperating agents.** Trust maps and signed agent-to-agent messages need their own work ([AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006), [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015)).
- **Supply chain.** Models, libraries and datasets are not covered here ([AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031)).
- **Detection and response.** Logging is B10. Alerting, triage and incident handling are separate ([AI-CTRL-009](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035)).
- **Acting with the user's rights.** The example uses agent-level scopes. Exchange the end user's identity where a user is present.

## Limits of this reference

> **Verify before use:** The Python code is a teaching reference and has not been security reviewed or hardened. The token format is deliberately simple and is not a substitute for your identity provider. The argument check resolves DNS at validation time, and the egress proxy repeats the check at connect time, which is the one that matters. The sandbox's process limits are not a security boundary. The Docker command and the Kubernetes manifest were not executed when this page was written, because the tests need no container runtime. Check every flag and field against the current documentation for your runtime and Kubernetes version, and pin container images by digest. The tests were run with Python 3.13 on Linux. The network-removal step needs `unshare` and is skipped where the kernel does not allow it.
