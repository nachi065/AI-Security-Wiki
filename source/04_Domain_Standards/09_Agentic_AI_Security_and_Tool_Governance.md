---
title: "Agentic AI Security and Tool Governance"
author: Nachiket Sathaye
parent: "Domain Standards"
nav_order: 4
document_type: AI Security Wiki Reference
version: 1.0
---

# Agentic AI Security and Tool Governance

> **Purpose:** Define security requirements for AI agents that can perform actions, call tools, invoke APIs or trigger workflows.

> **Audience:** AI platform teams, automation teams, governance, security architecture, SOC, red teamers, audit teams.

> **How to use:** Use this page as a wiki reference. Update the evidence, owners, control status, and links as implementation maturity improves.


## Core Principle

No AI agent should be approved for enterprise use unless the following are explicitly defined:

- Agent owner.
- Agent identity.
- Authorized tools.
- Authorized APIs.
- Data access boundary.
- Human approval workflow.
- Action logging requirement.
- Kill switch or suspension process.
- SOC monitoring integration.

## Primary Agentic AI Risks

| Risk | Description | Required Control | OWASP Reference |
|---|---|---|---|
| Excessive Privileges | Agent has broader permissions than required. | Least privilege, access review | ASI03 Identity & Privilege Abuse |
| Unauthorized Tool Execution | Agent invokes scripts, APIs or workflows outside scope. | Tool allowlist, runtime enforcement | ASI02 Tool Misuse & Exploitation |
| Prompt Manipulation | Agent behavior altered by malicious instructions. | Prompt injection controls, input validation | ASI01 Agent Goal Hijack |
| Lack of Human Oversight | Sensitive actions occur without approval. | Approval workflow, escalation controls | LLM06 Excessive Agency; ASI09 Human-Agent Trust Exploitation |
| Agent-to-Agent Trust Abuse | Agents cascade actions or propagate privilege. | Trust boundaries, agent relationship mapping | ASI07 Insecure Inter-Agent Communication; ASI08 Cascading Failures |
| Memory and Context Poisoning | Poisoned persistent memory influences later sessions. | Memory integrity controls, expiry, ability to inspect and purge | ASI06 Memory & Context Poisoning |
| Unexpected Code Execution | Agent runs generated or injected code with access to network, files or secrets. | Sandboxed execution, no network or filesystem access by default | ASI05 Unexpected Code Execution (RCE) |
| Agentic Supply Chain Compromise | A third-party tool server, MCP server, plugin or agent framework is malicious or compromised. | Allowlist and vet tool servers, isolate them, monitor calls | ASI04 Agentic Supply Chain Vulnerabilities |

OWASP references are to the Top 10 for Agentic Applications (ASI) and the Top 10 for LLM Applications 2025 (LLM). Confirm the exact category wording against the OWASP documents before quoting it. The reasoning behind these controls, including approval-gate design and autonomy limits, is in [Agents, Identity and Excessive Agency](../00_Foundations/05-Agents-Identity-and-Excessive-Agency.md).

## Agent Control Objectives

| Control | Requirement | Evidence |
|---|---|---|
| Agent Discovery | Inventory deployed agents and owners. | Agent registry |
| Agent Identity | Unique identities for agents. | IAM record |
| Tool Governance | Identify and restrict tool access. | Tool matrix |
| API Governance | Govern API access and scopes. | API permission evidence |
| Least Privilege | Restrict permissions to use case. | Access review records |
| Human Approval | Require approval for sensitive actions. | Approval logs |
| Activity Monitoring | Monitor decisions, tool calls and workflows. | Activity logs |
| Audit Logging | Record prompts, decisions and actions. | Audit export |
| Risk Analytics | Detect abnormal agent behavior. | Alerts and analytics rules |
| SOC Integration | Export events to monitoring platforms. | SIEM events |

## PoC Scenarios

1. Agent attempts unauthorized application access.
2. Agent attempts execution using excessive privileges.
3. Prompt injection attack manipulates agent behavior.
4. Agent accesses unauthorized repository.
5. Agent performs business action without approval.
