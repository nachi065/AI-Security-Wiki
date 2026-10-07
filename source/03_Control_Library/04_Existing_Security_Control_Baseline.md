---
title: "Existing Security Control Baseline"
author: Nachiket Sathaye
parent: "Control Library"
nav_order: 2
document_type: AI Security Wiki Reference
version: 1.0
---

# Existing Security Control Baseline

> **Purpose:** Show how a typical enterprise control set partially addresses AI-related risks, as a starting template for your own baseline assessment.

> **Audience:** Security engineering, architecture, audit, procurement, governance.

> **How to use:** Use this page as a template. Assess each control domain in your own environment and replace the example ratings and gaps with your results.

> **Illustrative example:** The ratings and entries on this page are generic examples, not an assessment of any specific organization. Replace them with your own findings before relying on them.

| Control Domain | Typical Coverage (Example) | Common AI-Specific Gap |
|---|---|---|
| Identity and Access Management | High | Prompt inspection and detailed agent governance not directly covered |
| Data Classification | High | Limited enforcement inside prompts, AI uploads, AI APIs and outputs |
| Data Loss Prevention | High | Coverage may vary for browsers, IDEs, APIs and unsanctioned AI channels |
| Endpoint Security | High | Limited prompt/content awareness and AI-specific telemetry |
| Cloud and SaaS Governance | High | Limited deep prompt and upload inspection |
| SOC and Monitoring | High | AI-specific context may be limited |
| Secure Software Development | High | AI coding assistant monitoring and AI-generated code controls require validation |
| AI Runtime Protection | Limited | Dedicated AI runtime protection may be required |
| Agent Governance | Limited | Dedicated identity, tool and action governance required before autonomous workflows |

## Baseline Principle

Existing enterprise controls remain the first line of defense. Dedicated AI security controls should not duplicate identity, DLP, endpoint, cloud governance or SOC capabilities unless they provide deeper AI-specific visibility, enforcement or forensic context.

## Gap Areas Commonly Prioritized

- AI prompt visibility ([AI-CTRL-002](03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002)).
- Prompt injection protection ([AI-CTRL-005](03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005)).
- AI runtime security ([AI-CTRL-005](03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-020](03_AI_Security_Control_Objectives_Library.md#ai-ctrl-020)).
- IDE-based AI governance ([AI-CTRL-004](03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004)).
- Agentic AI security ([AI-CTRL-006](03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006), [AI-CTRL-022](03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022) to [AI-CTRL-027](03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027)).
- AI-specific auditability ([AI-CTRL-008](03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008)).
- AI Security Posture Management ([AI-CTRL-001](03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001), [AI-CTRL-011](03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-031](03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031)).

The full set of controls is in the [AI Security Control Objectives Library](03_AI_Security_Control_Objectives_Library.md).
