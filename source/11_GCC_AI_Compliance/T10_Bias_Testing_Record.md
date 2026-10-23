---
title: "T10 Bias Testing Record"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "GCC AI Compliance"
nav_order: 18
description: "Record for a bias test: groups and attributes, data, metrics and thresholds, findings, an explainability check and the release decision."
document_type: AI Security Wiki Reference
version: 1.0
---

# T10 Bias Testing Record

> **Verification required.** This is a working template, not a regulator-approved form. Where it names a regional instrument, the claim comes from secondary sources and is a pointer to check, not a confirmed legal requirement. This is not legal advice.

<!-- -->

> **How to use:** This is a blank form. Copy it and fill in the empty cells and blanks for your system. To copy it, follow the "Suggest an edit to this page" link in the footer to reach its Markdown source.

Supports proposed [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041). CBUAE is reported to expect annual bias testing or testing on material model change [Reported]. Methods and thresholds below are options for you to decide with legal and risk input; none is a regulatory requirement.

| Field | Entry |
|---|---|
| System / ID | |
| Model and version | |
| Test date | |
| Tester (independent of builder?) | |
| Trigger | Pre-release / annual / material change / incident |
| Decision tested | |

## 1. Groups and attributes

| Attribute | Source (recorded, inferred, proxy) | Legal view on use | Notes |
|---|---|---|---|
| Gender | | | |
| Nationality | | | |
| Age band | | | |
| Disability (if available) | | | |
| Language / dialect | | | |
| Other | | | |

If attributes are not recorded, document the proxy or synthetic approach and its limits. Using sensitive attributes for testing may itself need a lawful basis; ask the DPO.

## 2. Data

| Item | Entry |
|---|---|
| Test dataset source and size | |
| Representativeness vs production population | |
| Labels and ground truth quality | |
| Data protection handling | |

## 3. Metrics (choose and justify)

| Metric | Definition | Threshold set (by whom, date) | Result | Pass |
|---|---|---|---|---|
| Selection-rate ratio between groups | favourable outcome rate, group A vs B | | | |
| Error-rate gap | false positive / negative difference | | | |
| Calibration gap | predicted vs actual by group | | | |
| Quality gap by language | Arabic vs English task accuracy | | | |
| Other | | | | |

## 4. Findings and action

| # | Finding | Severity | Mitigation | Owner | Date | Retest |
|---|---|---|---|---|---|---|

## 5. Explainability check

Sample of 10 decisions: explanation produced? Understandable to affected person? Reviewer can challenge? Result:

## 6. Decision

Release / Release with conditions / Block. Approver and date:

## 7. Bias profile

Keep one versioned bias profile per system and update it at each test. The fields follow the structure that public sources describe for IEEE 7003-2024 (Algorithmic Bias Considerations); the clause numbers have not been checked against the published standard. See the [Trustworthy AI and Ethics Standards Crosswalk](../23_Framework_Crosswalks/16_Trustworthy_AI_Ethics_Crosswalk.md).

| Field | Entry |
|---|---|
| Profile version and date | |
| Intended differences in treatment, and why they are justified | |
| Unintended differences to detect, and the acceptability boundary for each | |
| Stakeholder groups and protected attributes considered, with the reason for each | |
| Representativeness of the test and validation data for those groups, and known imbalances | |
| Validation dataset selection rationale | |
| Validated application boundaries (populations, languages, settings and inputs the system was tested for) | |
| Risks accepted, and who accepted them | |
| Drift monitoring in operation (data, concept and outcome), and its trigger for retest | |

## 8. Retention

Keep this record, data snapshot reference and code or notebook hash as audit evidence.
