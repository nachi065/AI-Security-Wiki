---
title: "T09 AI Model and System Inventory"
author: Nachiket Sathaye
parent: "GCC AI Compliance"
nav_order: 17
description: "Column definitions, a CSV header row and maintenance rules for an inventory of AI models and systems."
document_type: AI Security Wiki Reference
version: 1.0
---

# T09 AI Model and System Inventory

> **Verification required.** This is a working template, not a regulator-approved form. Where it names a regional instrument, the claim comes from secondary sources and is a pointer to check, not a confirmed legal requirement. This is not legal advice.

Wiki control: [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011). The CBUAE note is reported to expect an inventory with name, purpose and risk rating [Reported]; the other fields are best practice. Keep as a table or copy the header row into a spreadsheet.

## Column definitions

| Column | Meaning |
|---|---|
| ID | Unique use-case ID (matches [T01](T01_AI_Use_Case_Intake_and_Risk_Tiering.md)) |
| Name | System or model name |
| Type | Built / bought / embedded in vendor product / open-source |
| Purpose | One line |
| Owner (business, technical) | Named people |
| Tier | Low / Medium / High ([T01](T01_AI_Use_Case_Intake_and_Risk_Tiering.md)) |
| Impact on individuals | None / Support / Decision |
| Autonomy | Advisory / Human approval / Autonomous |
| Model and version | Name, version, date |
| Vendor | Name; country |
| Data categories | Personal, sensitive, confidential, public |
| Hosting | Country and provider |
| Impact assessment date ([T02](T02_AI_Impact_Assessment.md)) | |
| Bias test date ([T10](T10_Bias_Testing_Record.md)) | |
| Kill switch tested | Date |
| Residency attestation ([T04](T04_Data_Residency_Attestation.md)) | Date |
| Vendor review ([T03](T03_Vendor_Due_Diligence_GCC_Addendum.md)) | Date |
| Notices ([T06](T06_Bilingual_AI_Use_Notice.md)) | Languages |
| Regulators / jurisdictions | |
| Status | Proposed / Pilot / Live / Retired |
| Next review | |

## Header row (CSV)
```
ID,Name,Type,Purpose,Business owner,Technical owner,Tier,Impact on individuals,Autonomy,Model and version,Vendor,Vendor country,Data categories,Hosting country,Impact assessment date,Bias test date,Kill switch tested,Residency attestation date,Vendor review date,Notice languages,Jurisdictions,Status,Next review
```

## Example row (illustrative, fictional)
```
AI-0007,Loan pre-screen,Bought,Rank loan applications,Head of Retail Credit,Data Science Lead,High,Decision,Human approval,ModelX v3.2,ExampleVendor,Ireland,Personal; financial,UAE,2026-05-12,2026-05-20,2026-06-01,2026-05-15,2026-04-30,Arabic; English,UAE mainland; CBUAE,Live,2027-05-12
```

## Maintenance rules

- Update within 10 working days of any new system, model change or retirement.
- Quarterly discovery sweep: procurement, SaaS logs, cloud accounts, expense claims.
- Sample test of completeness each audit cycle.
