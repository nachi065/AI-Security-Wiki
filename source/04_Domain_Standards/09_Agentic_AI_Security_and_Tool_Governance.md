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

| Risk | Description | Required Control | Control ID | OWASP Reference |
|---|---|---|---|---|
| Excessive Privileges | Agent has broader permissions than required. | Least privilege, access review | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) | ASI03 Identity & Privilege Abuse |
| Unauthorized Tool Execution | Agent invokes scripts, APIs or workflows outside scope. | Tool allowlist, runtime enforcement | [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022), [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024) | ASI02 Tool Misuse & Exploitation |
| Prompt Manipulation | Agent behavior altered by malicious instructions. | Prompt injection controls, input validation | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005) | ASI01 Agent Goal Hijack |
| Lack of Human Oversight | Sensitive actions occur without approval. | Approval workflow, escalation controls | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | LLM06 Excessive Agency; ASI09 Human-Agent Trust Exploitation |
| Agent-to-Agent Trust Abuse | Agents cascade actions or propagate privilege. | Trust boundaries, agent relationship mapping | [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) | ASI07 Insecure Inter-Agent Communication; ASI08 Cascading Failures |
| Memory and Context Poisoning | Poisoned persistent memory influences later sessions. | Memory integrity controls, expiry, ability to inspect and purge | [AI-CTRL-026](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-026) | ASI06 Memory & Context Poisoning |
| Unexpected Code Execution | Agent runs generated or injected code with access to network, files or secrets. | Sandboxed execution, no network or filesystem access by default | [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027) | ASI05 Unexpected Code Execution (RCE) |
| Agentic Supply Chain Compromise | A third-party tool server, MCP server, plugin or agent framework is malicious or compromised. | Allowlist and vet tool servers, isolate them, monitor calls | [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) | ASI04 Agentic Supply Chain Vulnerabilities |

OWASP references are to the Top 10 for Agentic Applications (ASI) and the Top 10 for LLM Applications 2025 (LLM). Confirm the exact category wording against the OWASP documents before quoting it. The reasoning behind these controls, including approval-gate design and autonomy limits, is in [Agents, Identity and Excessive Agency](../00_Foundations/05-Agents-Identity-and-Excessive-Agency.md).

## Agent Control Objectives

| Control | Control ID | Requirement | Evidence |
|---|---|---|---|
| Agent Discovery | [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006) | Inventory deployed agents and owners. | Agent registry |
| Agent Identity | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) | Unique identities for agents. | IAM record |
| Tool Governance | [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024) | Identify and restrict tool access. | Tool matrix |
| API Governance | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016), [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022) | Govern API access and scopes. | API permission evidence |
| Least Privilege | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) | Restrict permissions to use case. | Access review records |
| Human Approval | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | Require approval for sensitive actions. | Approval logs |
| Activity Monitoring | [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006) | Monitor decisions, tool calls and workflows. | Activity logs |
| Audit Logging | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) | Record prompts, decisions and actions. | Audit export |
| Risk Analytics | [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006), [AI-CTRL-009](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009) | Detect abnormal agent behavior. | Alerts and analytics rules |
| SOC Integration | [AI-CTRL-009](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009) | Export events to monitoring platforms. | SIEM events |

## PoC Scenarios

1. Agent attempts unauthorized application access.
2. Agent attempts execution using excessive privileges.
3. Prompt injection attack manipulates agent behavior.
4. Agent accesses unauthorized repository.
5. Agent performs business action without approval.
