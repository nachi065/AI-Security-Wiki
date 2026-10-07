---
title: "Guide for Auditors of AI Systems Under EU Rules"
author: Nachiket Sathaye
parent: "EU AI Compliance"
nav_order: 4
description: "For auditors of AI systems under EU rules: setting criteria, scoping, tests by control family, sampling, common findings and report wording."
document_type: AI Security Wiki Reference
version: 1.0
---

# Guide for Auditors of AI Systems Under EU Rules

> **Verification required.** EU claims on this page were compiled on 7 October 2026 from secondary sources and from memory of the legal text. The Official Journal text was not read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text on EUR-Lex before relying on any of them. This is not legal advice.

For internal audit, external assurance and readiness reviewers. EU claims carry the tags used in the [EU AI Regulatory Hub](01_EU_AI_Regulatory_Hub.md). A readiness audit is not a conformity assessment by a notified body.

## 1. Set the audit criteria honestly

| Criteria | Examples | Caution |
|---|---|---|
| Binding law | AI Act, GDPR, NIS2, DORA, CRA | Read the Official Journal text; it was not read for this section |
| Guidance | Commission guidelines, EDPB opinions | Some are drafts only [Reported] |
| Standards | EN 18286:2026 (OJ citation pending) and drafts [Reported]; ISO/IEC 42001 | A standard gives a presumption of conformity only after OJ citation |
| Internal policy | Client AI policy | Always in scope |

State in the engagement letter which criteria are law and which are reference. Because the high-risk dates have moved [Reported], also state the assessment date logic: "tested against requirements as if applicable" or "tested against requirements currently applicable".

## 2. Scoping

1. Obtain the inventory ([T09](T09_AI_System_Inventory.md)). If none exists, report that.
2. Check the classification and role decisions ([T01](T01_AI_System_Classification.md)) for each system. Retest a sample independently. The common failure is classifying a system into a lower tier than it belongs in.
3. Identify the jurisdictions and competent authorities ([T11](T11_Authority_and_Standards_Engagement_Log.md)).
4. Pick the sample: all high-risk systems and all systems close to a prohibited practice, plus a risk-weighted selection of the others.
5. Confirm the evidence period.

## 3. Control families and tests

| Family | Wiki controls | Test | Evidence |
|---|---|---|---|
| Governance | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | Policy, roles, board reporting, AI literacy | Policy, minutes, [T07](T07_AI_Literacy_Programme_Record.md) |
| Classification | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | Each system has a role and a tier with reasoning; Art. 6(3) cases documented | [T01](T01_AI_System_Classification.md) |
| Prohibited practices | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | Screening against Art. 5 is documented | [T01](T01_AI_System_Classification.md) |
| Risk management | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | Lifecycle risk process; residual risk accepted by a named owner | Risk records |
| Data governance | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | Provenance, bias examination, special category necessity | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md) |
| Technical documentation | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | Annex IV content complete and current | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md) |
| Logging | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | Logs reconstruct a decision; retention set | Log samples |
| Human oversight | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) | Oversight design; reviewers trained; overrides evidenced; kill switch tested | Review logs |
| Accuracy and cyber | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | Declared metrics tested; adversarial testing | Test reports |
| Transparency | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | Disclosures, marking and notices work ([T06](T06_Transparency_Notice.md)) | Screenshots, tests |
| Privacy | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) | DPIA, lawful basis, rights, transfers ([T02](T02_Impact_Assessment_FRIA_DPIA.md), [T04](T04_Data_Location_and_Transfer_Record.md)) | Records |
| Supplier | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | Due diligence, contract, sub-processors ([T03](T03_Supplier_Due_Diligence_EU_Addendum.md)) | Records |
| Incident | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Playbook with AI Act, GDPR, NIS2 and DORA paths; exercise ([T05](T05_AI_Incident_and_Breach_Reporting_Workflow.md)) | Records |
| Post-market | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Monitoring plan and results | Reports |
| Deployer duties | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | Use per instructions; log retention; worker information | [T02](T02_Impact_Assessment_FRIA_DPIA.md), [T08](T08_Audit_Checklist.md) |

Use [T08](T08_Audit_Checklist.md) for line-by-line testing and the [EU Evidence Register](08_Evidence_Register.md) to track requests.

## 4. Sampling

These are suggested defaults and have no regulatory status.

- All high-risk systems.
- Of the lower tiers, at least 25 percent or five systems, whichever is greater.
- Ten decisions per high-risk system, to trace explanation and oversight.
- All incidents in the period.

## 5. Techniques

- Re-performance of bias and accuracy tests.
- Configuration inspection: hosting region, retention, model version.
- Walkthrough of one decision from end to end.
- Interviews.
- Document inspection, for example that approval predates go-live.
- Log reconstruction test: pick a decision and rebuild its inputs and model version from the logs.

## 6. Common findings

- High-risk systems classified as minimal without documented reasoning.
- An organisation treated as a deployer only, although it fine-tunes the model.
- Technical file started after launch.
- Logs missing the model version or the input reference.
- Oversight reviewers who approve without time to review.
- No FRIA where the deployer category needs one [Recalled; Art. 27 scope to verify].
- AI literacy limited to a slide deck with no role-based content.
- Transfers to non-EU AI APIs that were never assessed.
- Sub-processors unknown.

## 7. Rating and wording

Rate each test Effective, Partially effective, Ineffective or Not tested. Write each finding as criteria, condition, cause, effect and recommendation.

Limitation sentence: "Criteria were taken from the client's regulatory register dated [date], compiled from secondary sources and not verified against the Official Journal. This report is not a legal opinion or a conformity assessment."

## 8. Report checklist

- Scope, period, criteria and their verification status
- Systems and sample
- Limitations
- Findings with references
- Management responses with dates
- Follow-up

## 9. Handling

Keep evidence that contains personal data under production controls. Do not paste it into external AI tools.
