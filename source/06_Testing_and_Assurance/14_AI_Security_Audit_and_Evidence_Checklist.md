---
title: "AI Security Audit and Evidence Checklist"
author: Nachiket Sathaye
parent: "Testing and Assurance"
nav_order: 2
document_type: AI Security Wiki Reference
version: 1.0
---

# AI Security Audit and Evidence Checklist

> **Purpose:** Define audit evidence required to verify AI security controls across every family of the control library, from discovery and DLP to agents, models, supply chain and incident response.

> **Audience:** Audit teams, governance teams, control owners, security engineering.

| Control Area | Control IDs | Evidence Required | Evidence Owner |
|---|---|---|---|
| AI Discovery | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) | AI inventory, usage dashboard, user/device reports | Security Engineering |
| Prompt Inspection | [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002) | Prompt detection logs, policy actions, sampled test results | AI Security Team |
| File Upload Protection | [AI-CTRL-003](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-003) | Upload block/warn logs, classification policy, screenshots | DLP Team |
| IDE Governance | [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004) | IDE assistant inventory, source code/secret detection events | DevSecOps |
| Runtime Protection | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-020](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-020), [AI-CTRL-021](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-021), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | Prompt injection test reports, runtime logs, guardrail evidence, grounding and content safety results | AppSec |
| Agent Governance | [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006), [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025), [AI-CTRL-026](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-026), [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027) | Agent inventory, tool access logs, approval logs | AI Platform Team |
| Sovereignty | [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007) | Residency, retention, training exclusion and admin access evidence | GRC / Legal |
| SOC Integration | [AI-CTRL-009](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009) | SIEM events, parser mapping, alert correlation and runbook | SOC |
| Policy Enforcement | [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) | Policy configuration, action logs by type, exception register, bypass test results | AI Security Team |
| Auditability | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) | Exportable audit records, log schema, retention policy, sample reconstruction | Security Engineering |
| Governance, Risk and Use-Case Registry | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | Use-case registry, intake approvals, risk tiering, policy-to-control mapping, risk register, exception register | AI Governance Lead |
| Privacy and Vendor Assurance | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | Impact assessments, data subject request tests, vendor assessments, contract clauses | Privacy Office / Procurement |
| Identity and Access | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015), [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) | Identity registry, sponsor records, permission maps, recertification and drift reports | IAM Team |
| Data and Retrieval | [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-018](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-018), [AI-CTRL-019](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-019) | Masking rules, tenant isolation tests, retrieval permission tests, ingestion provenance | Data Owner / Application Owner |
| Model, Training and Pipeline | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029), [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030) | Model access list, dataset provenance, artifact signing, release gate results | ML Engineering / MLOps |
| Supply Chain, Infrastructure and Resilience | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031), [AI-CTRL-032](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-032), [AI-CTRL-040](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-040) | AI-BOM, approved source list, scan reports, segmentation and secrets configuration, fail-mode and failover test results | DevSecOps / Platform Engineering |
| Security Review and Adversarial Testing | [AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) | Threat models, approvals, red team reports, regression suite results, agreed thresholds | Security Architecture / AI Red Team |
| Control Assurance | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | Control effectiveness results, evidence packs with collection dates, owner attestations, findings log | GRC / Internal Audit |
| Fairness and Explainability | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | Bias test results, threshold approvals, explanation records, human-review log | AI Governance Lead / Model Risk |
| Impact Assessment | [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042) | Completed assessments, data protection officer advice, approvals dated before go-live, review dates | Data Protection Officer / AI Governance Lead |
| Authority Engagement | [AI-CTRL-043](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-043) | Authority register, filing and registration records, contact log | Legal / Compliance |
| AI Literacy | [AI-CTRL-044](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-044) | Role and needs matrix, completion records, effectiveness checks | AI Governance Lead / HR |
| Incident Response and Forensics | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Playbooks, exercise records, preserved-state checklist, provider escalation path | SOC / Incident Response |
| Cost and Abuse | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) | Cost attribution reports, budget and quota configuration, anomaly alerts | FinOps / AI Platform Team |

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
