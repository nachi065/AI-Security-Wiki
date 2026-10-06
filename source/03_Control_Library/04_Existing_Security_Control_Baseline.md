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

- AI prompt visibility.
- Prompt injection protection.
- AI runtime security.
- IDE-based AI governance.
- Agentic AI security.
- AI-specific auditability.
- AI Security Posture Management.
