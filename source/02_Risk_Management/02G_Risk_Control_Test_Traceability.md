---
title: "Risk, Control and Test Traceability"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Risk Management"
nav_order: 7
description: "Every risk in the register traced to the control objectives that treat it and the test cases that exercise them, with the controls that have no test case yet."
document_type: AI Security Wiki Reference
version: 1.0
---

# Risk, Control and Test Traceability

> **Purpose:** Trace every risk in the register to the control objectives that treat it and to the test cases that exercise those controls, and list the controls that have no test case yet.

> **Audience:** Auditors, GRC, security engineering, vendor evaluation teams.

> **How to use:** Start from a risk to find what to implement and what to test. Start from a control to see which risks it treats and which test pages hold its cases.

The tables are generated each time the site is built. They are read from the [AI Risk to Control Mapping](02D_AI_Risk_to_Control_Mapping.md) and from the "Control(s) Tested" field of each case in the [Test Case Library](../10_Test_Case_Library/index.md). To change a link, edit the page that owns it; this page follows on the next build.

<!-- traceability-matrix -->

## Reading the case counts

A case count shows how much has been written for a control, not whether the control is tested well. Runtime and identity controls have many cases because each attack path needs its own; a governance control can be tested adequately by a few cases if together they exercise everything the control must achieve. Judge coverage by outcome and risk, not by count:

1. Take the control's **Implementation Expectation** and **Audit Test Procedure** from the [control library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md) and list the outcomes the control must achieve.
2. For each outcome, find the cases whose procedure actually exercises it, including cases filed under another control.
3. Where a case does exercise it, add the control to that case's Control(s) Tested field. Write a new case only for an outcome that no case exercises.
4. Weigh the gaps by the risks the control treats: an untested outcome on a control that treats a Critical risk matters more than one on a Low risk.

### Review of AI-CTRL-041 to AI-CTRL-046 (22 October 2026)

These six controls were the newest in the library and had between one and four cases each. The review below followed the four steps above. Cases marked *new* were written to close a gap; cases marked *tagged* already exercised the outcome and now name the control.

| Control | Outcomes the control must achieve | Cases that exercise them | Result |
|---|---|---|---|
| [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) Fairness, bias testing and explainability | Bias test before release and on change, with a release gate | [TC-L03-031](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-031), [TC-L03-032](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-032), [TC-L03-033](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-033) | Covered |
| | Explanation for each high-impact decision | [TC-L03-029](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-029) (tagged) | Covered |
| | Route to human review | [TC-L03-008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008) (tagged) | Covered |
| | Versioned bias profile and monitoring outside validated boundaries | [TC-L03-043](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-043) (new) | Gap closed |
| [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042) Rights and data protection impact assessment | Assessment approved before go-live, risks mapped to mitigations, officer's advice recorded | [TC-L03-034](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-034), [TC-L03-010](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-010) (tagged) | Covered |
| | Reassessment on material change | [TC-L03-011](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-011) (tagged), [TC-L03-034](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-034) | Covered |
| | Required content (misuse, regions, languages, benefits, consultation) and annual review without a change | [TC-L03-044](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-044) (new) | Gap closed |
| [AI-CTRL-043](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-043) Regulator and authority engagement | Authority register, filings, representatives and contact log | [TC-L03-039](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-039) | Covered |
| | Notification duties met to their deadlines | [TC-L03-019](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-019) (tagged), [TC-D12-016](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-016) (tagged) | Covered |
| | New guidance and pending rules tracked through to the affected systems | [TC-L02-020](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-020) (tagged) | Covered |
| [AI-CTRL-044](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-044) AI literacy and role-based competence | Training by role, reviewers trained before assignment, records | [TC-L03-038](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-038), [TC-L02-022](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-022) (tagged) | Covered |
| | Training shown to work | [TC-L03-045](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-045) (new) | Gap closed |
| [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045) Human oversight design and effectiveness | Design record by tier; evidence, authority and workload; effectiveness measured with seeded errors | [TC-L01-012](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-012), [TC-L03-040](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-040), [TC-L03-041](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-041) | Covered; no new case |
| [AI-CTRL-046](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-046) Intellectual property and copyright | Input and output policy; vendor terms; training data licences; release scans | [TC-L03-028](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-028), [TC-L03-042](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-042), [TC-L13-007](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-007), [TC-L05-035](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-035) | Covered; no new case |

All of these cases are at the Documented [validation level](../10_Test_Case_Library/index.md#validation-levels): covering an outcome on paper is not the same as having run the test.
