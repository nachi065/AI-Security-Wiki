---
title: "Guide for AI Practitioners in the GCC"
author: Nachiket Sathaye
parent: "GCC AI Compliance"
nav_order: 2
description: "What changes when you build AI in the GCC: lifecycle checklist, residency, human oversight, fairness, Arabic testing and the evidence to keep."
document_type: AI Security Wiki Reference
version: 1.0
---

# Guide for AI Practitioners in the GCC

> **Verification required.** Regional claims on this page were compiled from secondary sources on 7 October 2026. No primary legal text was read, and each claim is tagged [Reported], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

For data scientists, ML and AI engineers, MLOps and security engineers. Regional claims carry the tags used in the [GCC AI Regulatory Hub](01_GCC_AI_Regulatory_Hub.md).

## 1. What changes when you build in the GCC

1. Personal data law applies first. Every GCC state has a data protection law [Reported]. Training, fine-tuning, prompts, logs and embeddings can all be personal data.
2. There is no single AI law, but buyers behave as if there is one. Government and regulated-sector customers ask for ethics self-assessments, inventories, human oversight and vendor evidence [Reported].
3. Decide residency at design time. Where inference, logs, vector stores and backups sit must be known before the architecture is fixed.
4. Arabic needs the same testing as English. Cover quality, dialect handling, right-to-left output and bilingual notices.

## 2. Lifecycle checklist

| Stage | Do this | Wiki control | Template |
|---|---|---|---|
| Idea | Register the use case; assign a tier | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | [T01](T01_AI_Use_Case_Intake_and_Risk_Tiering.md) |
| Design | Choose hosting region; record data flows and lawful basis; decide human oversight points | [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | [T04](T04_Data_Residency_Attestation.md), [T02](T02_AI_Impact_Assessment.md) |
| Data | Minimise; document provenance and licence; check text-and-data-mining and copyright position for the country (Saudi exception reported from 12 Aug 2026, verify) | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029) | [T02](T02_AI_Impact_Assessment.md) |
| Build | Threat-model prompts, tools, retrieval; secure secrets; pin dependencies | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) | none |
| Test | Functional, security, safety, bias (high-impact), Arabic and English | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [T10](T10_Bias_Testing_Record.md) |
| Release | Approval by named owner; kill switch tested; notice published | [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | [T06](T06_Bilingual_AI_Use_Notice.md) |
| Operate | Monitor drift, abuse, cost; log decisions; handle rights requests | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [T05](T05_AI_Incident_and_Breach_Notification_Workflow.md) |
| Change | Re-test on material change; update inventory | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011); theme CHG | [T09](T09_AI_System_Inventory.md) |
| Retire | Delete or archive per retention rule; revoke access | Theme RET | [T09](T09_AI_System_Inventory.md) |

CHG and RET are control themes from the [Framework Adoption Guide](../10_Test_Case_Library/framework-adoption-guide.md).

## 3. Design points by topic

### 3.1 Residency and transfers

- Draw the data flow: user device, API gateway, model host, retrieval store, logs, telemetry, backup, support access.
- Mark each hop with country and legal entity. Third-country model APIs are a transfer.
- Prefer in-region hosting for personal and regulated data. In-region availability of your preferred model may be limited; record the trade-off in [T04](T04_Data_Residency_Attestation.md).
- Transfer rules differ by country and free zone. No article-level rules were verified for this guide; check each PDPL.

### 3.2 Prompts, logs and training reuse

- Decide whether prompts and outputs are used for training. Default to no for customer data.
- Redact before logging where possible. Set a retention period for prompt logs.
- Customers in regulated sectors often forbid provider training on their data; contract for it.

### 3.3 Human oversight

- For decisions with legal or similarly significant effect (credit, insurance, employment, eligibility), design a human review step and an objection route ([TC-L03-008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008)). A kill switch must be tested, not just present ([AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025)).
- Record who can override, how fast, and what is logged.

### 3.4 Fairness and explainability

- Define the protected or sensitive groups relevant to the country and use case with legal input. Nationality, gender, age, disability and religion are typical candidates; confirm locally.
- Test before release, annually and on material change (CBUAE expectation, reported). Use [T10](T10_Bias_Testing_Record.md).
- Keep a human-readable explanation per high-impact decision.

### 3.5 Generative and agentic AI

- Treat tool-calling agents as privileged identities. Least privilege, per-tool approval, spend and action limits.
- Prompt injection and data exfiltration tests belong in release gates. NCA and NCSA AI guidance are reported to target generative and agentic AI; final text status differs, verify.
- Content safety: test culturally and legally sensitive outputs for the target country (religion, politics, public order). Define blocked categories with legal input.

### 3.6 Security baseline

- Map to ISO/IEC 27001-style controls first; then to the national baseline your customer uses (NCA, Dubai AI Security Policy, NCSA) [Reported].

## 4. Arabic and bilingual testing

| Check | Pass condition |
|---|---|
| Arabic answer quality vs English on same task | Documented gap and acceptance |
| Dialect handling (Gulf, Levantine, Egyptian, MSA) | Test set per dialect expected from users |
| Mixed Arabic-English input | No failure or leakage of English-only guardrails |
| Right-to-left rendering and numerals | Correct display and parsing |
| Safety filters in Arabic | Same block rate as English on a matched set |
| Notice and consent text | Both languages present; Arabic reviewed by a native legal reader |

## 5. Evidence to keep

Use case record, data-flow diagram, hosting attestation, model card, test results (security, safety, bias), approval record, kill-switch test log, incident log, change log. See the [Evidence Register](08_Evidence_Register.md).

## 6. Common mistakes

- Treating "internal tool" as exempt from data protection.
- Sending personal data to an out-of-region API during testing.
- Testing only English.
- No named owner for model changes.
- Bias test run once and never repeated.
- Claiming ISO/IEC 42001 or a national seal without a certificate in hand.
