---
title: "T10 Bias Testing Record"
author: Nachiket Sathaye
parent: "GCC AI Compliance"
nav_order: 18
description: "Record for a bias test: groups and attributes, data, metrics and thresholds, findings, an explainability check and the release decision."
document_type: AI Security Wiki Reference
version: 1.0
---

# T10 Bias Testing Record

> **Verification required.** This is a working template, not a regulator-approved form. Where it names a regional instrument, the claim comes from secondary sources and is a pointer to check, not a confirmed legal requirement. This is not legal advice.

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

## 7. Retention

Keep this record, data snapshot reference and code or notebook hash as audit evidence.
