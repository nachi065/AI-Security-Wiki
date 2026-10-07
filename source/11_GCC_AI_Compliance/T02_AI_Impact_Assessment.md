---
title: "T02 AI Impact Assessment"
author: Nachiket Sathaye
parent: "GCC AI Compliance"
nav_order: 10
description: "Fill-in AI impact assessment in the style of a DPIA, extended to cover fairness, explainability, human oversight and safety."
document_type: AI Security Wiki Reference
version: 1.0
---

# T02 AI Impact Assessment

> **Verification required.** This is a working template, not a regulator-approved form. Where it names a regional instrument, the claim comes from secondary sources and is a pointer to check, not a confirmed legal requirement. This is not legal advice.

A DPIA-style assessment extended for AI. Several GCC data protection regimes are reported to require an impact assessment for risky processing; confirm the trigger and format for your jurisdiction [Reported]. Wiki controls: [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041).

## 1. Summary

| Field | Entry |
|---|---|
| Use-case ID ([T01](T01_AI_Use_Case_Intake_and_Risk_Tiering.md)) | |
| Assessor | |
| Date | |
| Jurisdictions | |
| Assessment trigger | New / change / periodic |

## 2. Description of processing

- Purpose and legitimate aim:
- Data categories and subjects:
- Data flow (attach diagram) with countries:
- Recipients, vendors, sub-processors:
- Retention and deletion:
- Model: type, vendor, version, training data origin:

## 3. Lawful basis and necessity

| Question | Answer | Evidence |
|---|---|---|
| Lawful basis identified for each purpose? | | |
| Is consent used? If so, is it specific, informed and withdrawable? | | |
| Is each data element necessary? | | |
| Could the aim be met with less or anonymised data? | | |
| Is data reused for training? Basis? | | |

## 4. Data subject rights

| Right | How supported | Gap |
|---|---|---|
| Information / notice (Arabic and English, [T06](T06_Bilingual_AI_Use_Notice.md)) | | |
| Access | | |
| Correction | | |
| Deletion | | |
| Objection | | |
| Review of automated decision by a human | | |

## 5. Transfers and residency

Attach [T04](T04_Data_Residency_Attestation.md). State mechanism for each cross-border flow and legal view.

## 6. Risk register for individuals

| # | Risk to individuals | Likelihood (1-4) | Impact (1-4) | Score | Mitigation | Residual |
|---|---|---|---|---|---|---|
| 1 | Unfair outcome for a group | | | | [T10](T10_Bias_Testing_Record.md) test, threshold | |
| 2 | Wrong output relied on | | | | Human review, confidence display | |
| 3 | Unauthorised disclosure via prompts or outputs | | | | Redaction, access control | |
| 4 | Re-identification | | | | | |
| 5 | Lack of explanation | | | | Explanation record | |
| 6 | Harmful or culturally inappropriate content | | | | Safety tests in Arabic and English | |
| 7 | Loss of availability | | | | Fallback process | |

## 7. Fairness and explainability

- Affected groups considered:
- Bias test reference ([T10](T10_Bias_Testing_Record.md)):
- Explanation method and where the person sees it:

## 8. Oversight and safeguards

- Human oversight points:
- Who can stop the system and how (kill switch, [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025)):
- Monitoring and drift checks:
- Incident route ([T05](T05_AI_Incident_and_Breach_Notification_Workflow.md)):

## 9. Consultation

Views of DPO, security, legal, affected business unit, and (if appropriate) representatives of affected people. Regulator consultation required? Record decision ([T11](T11_Regulator_Engagement_Log.md)).

## 10. Decision

| Outcome | Approve / Approve with conditions / Reject |
|---|---|
| Conditions | |
| Approver and date | |
| Next review | |
