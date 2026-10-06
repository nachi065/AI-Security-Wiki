---
title: "AI Risk to Control Mapping"
author: Nachiket Sathaye
parent: "Risk Management"
nav_order: 4
document_type: AI Security Wiki Reference
version: 1.0
---

# AI Risk to Control Mapping

> **Purpose:** Map AI risks to control objectives and evidence so teams can test and audit implementation consistently.

> **Audience:** Security engineering, audit, GRC, vendor evaluation teams.

> **How to use:** Use this page as a wiki reference. Update the evidence, owners, control status, and links as implementation maturity improves.

| Risk ID | Primary Controls | Evidence Required |
|---|---|---|
| AI-R01 | Prompt inspection; file upload protection; classification-aware enforcement | Prompt logs; upload block logs; data classification policy; SOC alerts |
| AI-R02 | AI discovery; application risk classification; policy enforcement | AI inventory; shadow AI reports; user activity dashboard |
| AI-R03 | Sensitive data detection; redaction; block/warn policy | DLP events; AI prompt detections; policy screenshots |
| AI-R04 | IDE discovery; source code protection; secret detection | IDE inventory; secret detection log; developer policy evidence |
| AI-R05 | Prompt injection detection; runtime inspection; RAG validation | Red team report; runtime logs; guardrail evidence |
| AI-R06 | Output inspection; retrieval governance; source-document logging | Response logs; retrieval logs; permission validation evidence |
| AI-R07 | Agent identity; tool governance; approvals; action logging | Agent registry; API/tool matrix; approval logs; SIEM events |
| AI-R08 | AI asset inventory; model inventory; plugin governance; dependency scanning | AI BOM; model registry; vulnerability reports |
| AI-R09 | Audit logging; SIEM integration; retention controls | Exportable audit records; SIEM event IDs; retention policy |
| AI-R10 | Residency; retention; training exclusion; admin access logging | Vendor documentation; DPA clauses; residency attestation; admin logs |

## Mapping Usage

Use this mapping during solution architecture review, vendor PoC scoring, audit evidence collection and recurring risk review. Each AI project should identify applicable risks and provide the mapped evidence before production approval.
