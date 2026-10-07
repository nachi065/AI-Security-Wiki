---
title: "T09 AI System Inventory (EU)"
author: Nachiket Sathaye
parent: "EU AI Compliance"
nav_order: 17
description: "Column definitions, a CSV header row and maintenance rules for an inventory of AI systems that records AI Act role, risk tier and applicable date."
document_type: AI Security Wiki Reference
version: 1.0
---

# T09 AI System Inventory (EU)

> **Verification required.** This is a working template, not a regulator-approved form. Where it cites an article or a date, the citation comes from secondary sources or from memory of the legal text and is a pointer to check. This is not legal advice.

<!-- -->

> **How to use:** This is a blank form. Copy it and fill in the empty cells and blanks for your system. To copy it, follow the "Suggest an edit to this page" link in the footer to reach its Markdown source.

Wiki control: [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011). Keep the inventory as a table, or copy the header row into a spreadsheet.

## Column definitions

| Column | Meaning |
|---|---|
| ID | Matches [T01](T01_AI_System_Classification.md) |
| Name, version | |
| Type | Built / bought / embedded / open source |
| Purpose | Intended purpose, one line |
| Owners | Business and technical |
| AI Act role | Provider / deployer / importer / distributor / GPAI provider |
| Risk tier | Prohibited / High-risk / Transparency / GPAI / Minimal |
| Annex reference | Annex I or III area, or Art. 6(3) filter used |
| Applicable date | Per the [hub timeline](01_EU_AI_Regulatory_Hub.md#2-ai-act-timeline), as verified |
| Impact on persons | None / Support / Decision |
| Autonomy | Advisory / Human approval / Autonomous |
| Model and supplier | Name, version, country |
| Data categories | Personal, special, children, confidential |
| Hosting | Country, provider |
| Transfers outside EEA | Y/N, mechanism |
| DPIA / FRIA date ([T02](T02_Impact_Assessment_FRIA_DPIA.md)) | |
| Bias test date | |
| Technical file status ([T10](T10_Technical_Documentation_and_Conformity_Checklist.md)) | |
| Conformity / CE / registration | |
| Kill switch test date | |
| Notice languages ([T06](T06_Transparency_Notice.md)) | |
| NIS2 / DORA / CRA relevance | |
| Status | Proposed / Pilot / Live / Retired |
| Next review | |

## Header row (CSV)
```
ID,Name and version,Type,Purpose,Business owner,Technical owner,AI Act role,Risk tier,Annex reference,Applicable date,Impact on persons,Autonomy,Model and supplier,Supplier country,Data categories,Hosting country,Transfers outside EEA,DPIA FRIA date,Bias test date,Technical file status,Conformity status,Kill switch test date,Notice languages,Other regimes,Status,Next review
```

## Example row (illustrative, fictional)
```
AI-0012,CV screener v2,Bought,Rank job applicants,Head of HR,HR Systems Lead,Deployer,High-risk,Annex III employment,2027-12-02 (reported),Decision,Human approval,ScreenCo v2.1,Netherlands,Personal,Germany,No,2026-09-15,2026-09-20,Supplier file requested,Supplier declaration on file,2026-09-01,German; English,GDPR,Pilot,2027-03-15
```

## Maintenance rules

- Update within 10 working days of any new system, model change or retirement.
- Quarterly discovery sweep: procurement, SaaS logs, cloud accounts.
- Test completeness every audit cycle.
