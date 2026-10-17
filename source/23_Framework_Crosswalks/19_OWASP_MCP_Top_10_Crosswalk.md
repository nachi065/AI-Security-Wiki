---
title: "OWASP MCP Top 10 Crosswalk"
author: Nachiket Sathaye
parent: "Framework Crosswalks"
nav_order: 19
description: "The ten items of the OWASP MCP Top 10 (beta) mapped to this wiki's risks and controls, with incidents that illustrate them."
document_type: AI Security Wiki Reference
version: 1.0
last_reviewed: 2026-10-17
---

# OWASP MCP Top 10 Crosswalk

> **Purpose:** Let a team that uses the OWASP MCP Top 10 find the matching risks and controls in this wiki for agents that connect to tools and data through the Model Context Protocol.

> **Audience:** AI platform engineers, application security, security architecture, red teams.

> **Using the two together:** Use the OWASP list to name MCP risks. Use this wiki for controls, evidence, tests, and the [Agent Architecture Patterns](../24_Builder_Track/02_Agent_Architecture_Patterns.md) that contain them.

## About the list and this page

The OWASP MCP Top 10 is an OWASP project on the security of the Model Context Protocol. The identifiers and titles below were read from the [project page](https://owasp.org/www-project-mcp-top-10/) on 17 October 2026, which describes the list as a beta in pilot testing. Titles may change before a final release, so check the project page before citing an item. This page cites identifiers and titles only. The mapping is this wiki's judgement and has not been reviewed by OWASP.

The wiki's other OWASP lists, for LLM applications and for agentic applications, are in the [OWASP Top 10 Crosswalk](06_OWASP_Top_10_Crosswalk.md).

**Match** is **Direct** when the wiki has a risk and controls for the item, and **Partial** when it covers only part, as the last column explains.

## MCP Top 10 to wiki risks and controls

| ID | Title | Wiki risks | Main wiki controls | Match | Notes |
|---|---|---|---|---|---|
| `MCP01:2025` | Token Mismanagement & Secret Exposure | [AI-R22](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015), [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) | Direct | Short-lived scoped tokens issued at call time; no secrets in configuration files or in the model's context. |
| `MCP02:2025` | Privilege Escalation via Scope Creep | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R23](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016), [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024) | Direct | Least-privilege scopes, periodic review of granted scopes, and step-up authorization for sensitive tools. |
| `MCP03:2025` | Tool Poisoning | [AI-R23](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R24](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024), [AI-CTRL-026](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-026) | Direct | Review tool descriptions before approval, pin their hashes and alert on change (Builder Track B4). |
| `MCP04:2025` | Software Supply Chain Attacks & Dependency Tampering | [AI-R23](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) | Direct | Allow-listed sources, version pinning and review of updates. See the postmark-mcp case. |
| `MCP05:2025` | Command Injection & Execution | [AI-R24](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R23](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-020](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-020), [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027) | Direct | Validate tool inputs, never build shell strings, and run servers sandboxed. See the mcp-remote case. |
| `MCP06:2025` | Prompt Injection via Contextual Payloads | [AI-R05](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R24](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022) | Direct | Treat tool output as untrusted and break the lethal trifecta. See the GitHub MCP case. |
| `MCP07:2025` | Insufficient Authentication & Authorization | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R46](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015), [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) | Direct | OAuth with audience-bound tokens and no token passthrough; per-tool authorization. |
| `MCP08:2025` | Lack of Audit and Telemetry | [AI-R09](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R45](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-009](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009) | Direct | Log every call with arguments, result and the agent and user identity. |
| `MCP09:2025` | Shadow MCP Servers | [AI-R02](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R23](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001), [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024) | Partial | AI discovery and tool governance apply, but no control or test case names MCP servers on developer machines specifically. |
| `MCP10:2025` | Context Injection & Over-Sharing | [AI-R06](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R21](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-018](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-018), [AI-CTRL-026](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-026) | Partial | Retrieval access control and memory isolation cover part of it. Isolation of shared context between sessions and tenants is not tested separately. |

Of the ten items, 8 are a direct match and 2 are partial.

## Incidents

The [AI Security Incident Casebook](../09_Reference/20_AI_Security_Incident_Casebook.md) has four MCP cases: the [GitHub MCP toxic agent flow](../09_Reference/20_AI_Security_Incident_Casebook.md#github-mcp-toxic-agent-flow), [postmark-mcp](../09_Reference/20_AI_Security_Incident_Casebook.md#postmark-mcp-malicious-mcp-server), [mcp-remote](../09_Reference/20_AI_Security_Incident_Casebook.md#mcp-remote-cve-2025-6514) and [MCP Inspector](../09_Reference/20_AI_Security_Incident_Casebook.md#mcp-inspector-cve-2025-49596).

## Attribution

The OWASP MCP Top 10 is published by the OWASP Foundation. This page cites item identifiers and titles only. Check the project's licence before reusing its text.

## Related pages

- [OWASP Top 10 Crosswalk](06_OWASP_Top_10_Crosswalk.md)
- [Agent Architecture Patterns](../24_Builder_Track/02_Agent_Architecture_Patterns.md)
- [Secure Your First Agent](../24_Builder_Track/01_Secure_Your_First_Agent.md)
- [AI Risk to Control Mapping](../02_Risk_Management/02D_AI_Risk_to_Control_Mapping.md)
