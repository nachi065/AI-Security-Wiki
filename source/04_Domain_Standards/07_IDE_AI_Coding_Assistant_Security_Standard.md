---
title: "IDE AI Coding Assistant Security Standard"
author: Nachiket Sathaye
parent: "Domain Standards"
nav_order: 2
document_type: AI Security Wiki Reference
version: 1.0
---

# IDE AI Coding Assistant Security Standard

> **Purpose:** Set controls for AI coding assistants and AI-enabled developer environments.

> **Audience:** Developers, DevSecOps, application security, security engineering, AI product developers, audit.

## Primary Risks

- Source code exposure.
- Credential and secret leakage.
- Infrastructure information disclosure.
- AI-generated insecure code.
- Unauthorized AI coding assistant installation.

## Control Requirements

| Requirement | Control ID | Description | Evidence |
|---|---|---|---|
| IDE Discovery | [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004), [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) | Identify approved and unapproved AI coding tools and extensions. | IDE inventory, endpoint reports |
| Source Code Protection | [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004) | Detect submission of proprietary source code to AI assistants. | Detection logs, test evidence |
| Secret Detection | [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004) | Detect API keys, tokens, credentials, certificates and connection strings. | Secret detection alerts |
| Prompt Inspection | [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002) | Inspect developer prompts where technically feasible. | Prompt logs or policy events |
| Policy Enforcement | [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) | Monitor, warn, redact, block or investigate risky submissions. | Policy screenshots, alert logs |
| Auditability | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) | Attribute activity to user, device, IDE and AI assistant. | Exportable audit records |
| SIEM Integration | [AI-CTRL-009](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009) | Forward events to SOC monitoring. | SIEM event ID, parser mapping |

## Developer AI Coding Rules

Developers must not submit:

- Production credentials.
- API keys, tokens or certificates.
- Complete proprietary source files.
- Internal application logic not approved for external processing.
- Infrastructure-as-code templates containing sensitive infrastructure details.
- Customer, employee or regulated data.
- Security configurations, firewall rules, detection logic or privileged workflow details.

All AI-generated code must be reviewed through secure coding, peer review and DevSecOps processes before use.

## PoC Tests

1. Submit proprietary source code to AI coding assistant.
2. Attempt to share API keys or tokens.
3. Upload infrastructure-as-code template.
4. Install unapproved AI extension.
5. Request generation of privileged system code.
