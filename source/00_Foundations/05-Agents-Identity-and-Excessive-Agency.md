---
title: "5. Agents, Identity and Excessive Agency"
description: "Agentic AI risk: the OWASP Agentic Top 10, advisory output with enforced authority, non-human identity, tool design, approval gates and memory."
author: Nachiket Sathaye
parent: "Foundations"
nav_order: 5
document_type: Practitioner Research Paper
---

# 5. Agents, Identity and Excessive Agency

## 5.1 Why agents change the risk

A model that only returns text can mislead. An agent, which plans, remembers, calls tools and iterates, can *act*. That converts a model error or a successful injection into an operational event: an email sent, a record changed, code merged, a cloud resource created. The OWASP Top 10 for Agentic Applications (published 9 December 2025 by the OWASP GenAI Security Project) describes the risks of systems that "plan, hold memory, call tools, and take actions across other systems with delegated authority" [12]. **[Reported]**

| ID | Risk (as listed in [12]) |
|---|---|
| ASI01 | Agent Goal Hijack |
| ASI02 | Tool Misuse & Exploitation |
| ASI03 | Identity & Privilege Abuse |
| ASI04 | Agentic Supply Chain Vulnerabilities |
| ASI05 | Unexpected Code Execution (RCE) |
| ASI06 | Memory & Context Poisoning |
| ASI07 | Insecure Inter-Agent Communication |
| ASI08 | Cascading Failures |
| ASI09 | Human-Agent Trust Exploitation |
| ASI10 | Rogue Agents |

*Names taken from a secondary summary of the OWASP document; confirm exact wording against the primary source before quoting.*

The Q1 2026 OWASP GenAI Exploit Round-up reports that agentic incidents featured excessive autonomy, unsafe confirmation flows and identity misuse, and that many AI incidents arose from architectural and trust-boundary flaws rather than discrete code vulnerabilities (which creates a gap with CVE-based tracking) [13]. **[Reported]** *This is a summary of an eight-incident report over a limited period; do not generalise from it to prevalence.*

## 5.2 Design principle: advisory output, enforced authority

> Make model output advisory unless an independently enforced policy authorises the action. [Analysis]

Practically, this means the agent proposes and a deterministic layer disposes:

```
Model proposes action  →  Policy engine checks: who is the principal?
                                                  is this tool allowed for this task?
                                                  are parameters within limits?
                                                  does this need human approval?
                       →  Execute  /  Deny  /  Escalate to human
                       →  Log decision with full context
```

## 5.3 Non-human identity and least privilege

Agents need identities. The common failure is to run them under a developer's token, a shared service account or a broad API key. [Analysis]

| Practice | Rationale |
|---|---|
| **One identity per agent (and ideally per task or session)** | Attribution and revocation without side effects |
| **Short-lived, scoped credentials** | Limits value of a stolen or leaked token |
| **Act on behalf of the user, not above them** | Prevents the agent from becoming a privilege-escalation path (confused-deputy problem) |
| **Separate read and write capabilities** | Most tasks do not need write access |
| **No secrets in prompts, memory or logs** | Prompts and context are not a secure store; they can be leaked (LLM07) [11] |
| **Explicit delegation records** | Who authorised what, for how long, for which scope |
| **Kill switch** | Ability to revoke credentials and halt execution quickly |

## 5.4 Tools

Each tool is an interface to an external system and should be treated like any other API exposed to an untrusted caller:

- Allow-list tools per task; do not expose the full catalogue by default.
- Validate parameters against schemas and business limits outside the model.
- Prefer narrow, purpose-built tools to general ones (a "send invoice reminder" tool rather than "send arbitrary email"; a read-only query tool rather than raw SQL).
- Treat tool *descriptions* and tool *results* as untrusted text that can carry injected instructions.
- Sandbox code execution; deny network and filesystem access by default.
- Vet third-party tool servers and plugins as supply-chain components (see [Page 6](06-Supply-Chain-and-Infrastructure.md)).

## 5.5 Approval gates

Human-in-the-loop is a control only if the human can make an informed decision and the gate cannot be bypassed.

- Gate on **impact**, not on frequency: irreversible, external, financial, privilege-changing or bulk actions.
- Show the reviewer the **actual action and parameters**, not only the model's description of it. The Round-up cites "unsafe confirmation flows" as a pattern [13].
- Watch for **approval fatigue**. Too many low-value prompts train people to approve everything. [Analysis]
- Define **autonomy limits** per agent: maximum transaction value, maximum duration, maximum number of actions per run.

## 5.6 Memory and multi-agent systems

- **Persistent memory** is a new write path for attackers: poisoned memory can influence future sessions (ASI06) [12]. Provide integrity controls, expiry, and the ability to inspect and purge.
- **Agent-to-agent messages** should carry no implicit trust. Authenticate agents, scope what each can request of another, and avoid designs where a low-trust agent can instruct a high-trust one (ASI07, ASI08) [12].
- **Cascading failure**: a wrong output from one agent can be consumed as fact by the next. Place validation between stages.

## 5.7 Agent worksheet

For each agent, record: available tools; permissions; data sources; action types; approval requirements; memory stores; external communications; maximum transaction value; maximum autonomous duration; emergency shutdown mechanism. (Template in [Appendices](Appendices.md).)
