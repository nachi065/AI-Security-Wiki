---
title: "AI Security Audit and Evidence Checklist"
parent: "Testing and Assurance"
nav_order: 2
document_type: AI Security Wiki Reference
version: 1.0
---

# AI Security Audit and Evidence Checklist

> **Purpose:** Define audit evidence required to verify AI security controls across discovery, DLP, IDE, runtime, agentic AI, sovereignty and SOC integration.

> **Audience:** Audit teams, governance teams, control owners, security engineering.

> **How to use:** Use this page as a wiki reference. Update the evidence, owners, control status, and links as implementation maturity improves.

| Control Area | Evidence Required | Evidence Owner |
|---|---|---|
| AI Discovery | AI inventory, usage dashboard, user/device reports | Security Engineering |
| Prompt Inspection | Prompt detection logs, policy actions, sampled test results | AI Security Team |
| File Upload Protection | Upload block/warn logs, classification policy, screenshots | DLP Team |
| IDE Governance | IDE assistant inventory, source code/secret detection events | DevSecOps |
| Runtime Protection | Prompt injection test reports, runtime logs, guardrail evidence | AppSec |
| Agent Governance | Agent inventory, tool access logs, approval logs | AI Platform Team |
| Sovereignty | Residency, retention, training exclusion and admin access evidence | GRC / Legal |
| SOC Integration | SIEM events, parser mapping, alert correlation and runbook | SOC |

## Evidence Quality Criteria

Evidence should be:

- Exportable.
- Timestamped.
- Attributable to user/device/application where applicable.
- Linked to a policy or control ID.
- Retained according to approved retention requirements.
- Sufficient for incident reconstruction and audit sampling.

## Exception Register Fields

```markdown
Exception ID:
Control ID:
AI System / Vendor:
Reason for Exception:
Compensating Control:
Business Owner:
Risk Owner:
Approval Date:
Expiry Date:
Review Status:
```
