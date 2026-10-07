---
title: "T08 AI Audit Checklist (EU)"
author: Nachiket Sathaye
parent: "EU AI Compliance"
nav_order: 16
description: "Audit checklist of 52 tests across ten areas under EU rules, from governance and classification to provider and deployer duties and incidents."
document_type: AI Security Wiki Reference
version: 1.0
---

# T08 AI Audit Checklist (EU)

> **Verification required.** This is a working template, not a regulator-approved form. Where it cites an article or a date, the citation comes from secondary sources or from memory of the legal text and is a pointer to check. This is not legal advice.

<!-- -->

> **How to use:** This is a blank form. Copy it and fill in the empty cells and blanks for your system. To copy it, follow the "Suggest an edit to this page" link in the footer to reach its Markdown source.

Use with the [EU Evidence Register](08_Evidence_Register.md). Result: Effective (E), Partially effective (P), Ineffective (I), Not tested (N). Article references are [Recalled].

Audit: ______ System(s): ______ Period: ______ Auditor: ______ Criteria (and their verification status): ______ Basis: tested as if applicable / currently applicable

## 1. Governance and literacy

| # | Test | Control | Result | Evidence ref | Note |
|---|---|---|---|---|---|
| 1.1 | AI policy approved and current | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | | | |
| 1.2 | Roles and executive accountability named | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | | | |
| 1.3 | Board reporting in period | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | | | |
| 1.4 | AI literacy programme with records ([T07](T07_AI_Literacy_Programme_Record.md)) | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | | | |
| 1.5 | Authority register current ([T11](T11_Authority_and_Standards_Engagement_Log.md)) | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | | | |

## 2. Inventory and classification

| # | Test | Control | Result | Evidence ref | Note |
|---|---|---|---|---|---|
| 2.1 | Inventory complete with owner, role, tier ([T09](T09_AI_System_Inventory.md)) | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | | | |
| 2.2 | Completeness test: 5 discovered systems appear in register | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | | | |
| 2.3 | Independent re-classification of a sample agrees | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | | | |
| 2.4 | Prohibited screen recorded | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | | | |
| 2.5 | Art. 6(3) cases documented and registered | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | | | |
| 2.6 | Vendor-embedded AI included | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | | | |

## 3. Provider requirements (high-risk)

| # | Test | Control | Result | Evidence ref | Note |
|---|---|---|---|---|---|
| 3.1 | Risk management process across lifecycle | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | | | |
| 3.2 | Data governance and bias examination | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | | | |
| 3.3 | Technical documentation complete ([T10](T10_Technical_Documentation_and_Conformity_Checklist.md)) | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | | | |
| 3.4 | Logging reconstructs a decision | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | | | |
| 3.5 | Instructions for use adequate | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | | | |
| 3.6 | Human oversight design | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | | | |
| 3.7 | Accuracy, robustness, cybersecurity tested | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | | | |
| 3.8 | QMS in place | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | | | |
| 3.9 | Conformity route, declaration, CE marking, registration | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | | | |
| 3.10 | Post-market monitoring active | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | | | |

## 4. Deployer requirements

| # | Test | Control | Result | Evidence ref | Note |
|---|---|---|---|---|---|
| 4.1 | Used per instructions | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | | | |
| 4.2 | Oversight assigned to competent staff | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | | | |
| 4.3 | Input data relevance checked | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | | | |
| 4.4 | Logs retained for required period | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | | | |
| 4.5 | Workers informed | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | | | |
| 4.6 | FRIA done where required | [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042) | | | |
| 4.7 | Serious incidents reported to provider and authority | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | | | |

## 5. Privacy

| # | Test | Control | Result | Evidence ref | Note |
|---|---|---|---|---|---|
| 5.1 | Lawful basis recorded | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | | | |
| 5.2 | DPIA before go-live ([T02](T02_Impact_Assessment_FRIA_DPIA.md)) | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042) | | | |
| 5.3 | Rights handling tested | [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) | | | |
| 5.4 | Art. 22 safeguards for automated decisions | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | | | |
| 5.5 | Transfers assessed ([T04](T04_Data_Location_and_Transfer_Record.md)) | [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007) | | | |

## 6. Transparency

| # | Test | Control | Result | Evidence ref | Note |
|---|---|---|---|---|---|
| 6.1 | AI interaction disclosed | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | | | |
| 6.2 | Synthetic content marked and tested | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | | | |
| 6.3 | Deepfake labels | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | | | |
| 6.4 | Notice reviewed in required languages ([T06](T06_Transparency_Notice.md)) | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | | | |

## 7. Fairness

| # | Test | Control | Result | Evidence ref | Note |
|---|---|---|---|---|---|
| 7.1 | High-impact decisions defined | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | | | |
| 7.2 | Bias test current | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | | | |
| 7.3 | Special category necessity record | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | | | |
| 7.4 | Re-performance of one test | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | | | |
| 7.5 | Explanation traced for sample | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | | | |

## 8. Suppliers

| # | Test | Control | Result | Evidence ref | Note |
|---|---|---|---|---|---|
| 8.1 | Due diligence before contract ([T03](T03_Supplier_Due_Diligence_EU_Addendum.md)) | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | | | |
| 8.2 | Contract clauses present | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | | | |
| 8.3 | Supplier documentation available | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | | | |
| 8.4 | GPAI downstream information held ([T12](T12_GPAI_Model_Checklist.md)) | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | | | |

## 9. Incident

| # | Test | Control | Result | Evidence ref | Note |
|---|---|---|---|---|---|
| 9.1 | Multi-regime playbook ([T05](T05_AI_Incident_and_Breach_Reporting_Workflow.md)) | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | | | |
| 9.2 | Notification matrix complete | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | | | |
| 9.3 | Exercise in period | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | | | |
| 9.4 | Incidents notified on time | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | | | |

## 10. Evidence

| # | Test | Control | Result | Evidence ref | Note |
|---|---|---|---|---|---|
| 10.1 | Evidence retained and retrievable | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | | | |
| 10.2 | Prior findings closed | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | | | |

## Summary

Record the totals, the top findings and the limitations. State that the criteria were summarised from secondary sources and that the audit is not a conformity assessment or a legal opinion.
