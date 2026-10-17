---
title: "AI Security Vendor Evaluation Scorecard (.xlsx)"
author: Nachiket Sathaye
parent: "Templates"
nav_order: 4
description: "A downloadable Excel scorecard to compare up to five AI security products on the wiki's eight evaluation domains, with weighted scores, flags, required vendor evidence, PoC notes, a recommendation and a GCC and EU supplier due-diligence questionnaire."
document_type: AI Security Wiki Template
version: 1.0
---

# AI Security Vendor Evaluation Scorecard (.xlsx)

**[Download the AI Security Vendor Evaluation Scorecard (.xlsx)](AI_Security_Vendor_Evaluation_Scorecard.xlsx)**

> **Purpose:** Compare up to five AI security products on the eight domains of the [AI Security Vendor Evaluation Master Framework](../05_Vendor_Evaluation/11_AI_Security_Vendor_Evaluation_Master_Framework.md), using the wiki's 0 to 5 scale, and record the evidence, PoC notes and recommendation behind the choice.

> **Audience:** Security architecture, procurement, vendor risk and evaluation teams.

> **Before you rely on it:** No vendor is named or pre-scored: every score must come from your own PoC or documented evidence. The wiki gives the scale and the checklist but no weights, so equal domain weights and the flag score of 2 are workbook defaults (orange cells on Settings). The due-diligence questions come from the wiki's GCC and EU T03 pages, which say their regional citations come from secondary sources and must be checked.

## What is in the workbook

| Sheet | What it holds | Built from |
|---|---|---|
| README and License | How to use the workbook, colour legend, sources, licence, credit and disclaimer | Written for the workbook |
| Summary | Scores, rank, flags, missing evidence and recommendation for each vendor | Calculated from the other sheets |
| Settings | Vendors, domain weights, region, flag score and the scoring scale | [AI Security Vendor Evaluation Master Framework](../05_Vendor_Evaluation/11_AI_Security_Vendor_Evaluation_Master_Framework.md) |
| Scoring | Domain scores with the evidence behind each, weighted score, rank and flagged domains | [AI Security Vendor Evaluation Master Framework](../05_Vendor_Evaluation/11_AI_Security_Vendor_Evaluation_Master_Framework.md) |
| Domain Checklist | What to evaluate, validate and evidence in each domain, and the evaluation workflow | [AI Security Vendor Evaluation Master Framework](../05_Vendor_Evaluation/11_AI_Security_Vendor_Evaluation_Master_Framework.md), [Vendor Evaluation and Audit Playbook](../07_Role_Based_Playbooks/15E_Vendor_Evaluation_and_Audit_Playbook.md) |
| Vendor Evidence | The wiki's required vendor evidence list, for each vendor | [AI Security Vendor Evaluation Master Framework](../05_Vendor_Evaluation/11_AI_Security_Vendor_Evaluation_Master_Framework.md) |
| Supplier Due Diligence | Questions merged from the GCC and EU addenda, a decision and contract clause checks | [GCC T03 Vendor Due-Diligence Addendum](../11_GCC_AI_Compliance/T03_Vendor_Due_Diligence_GCC_Addendum.md), [EU T03 Supplier Due-Diligence Addendum](../12_EU_AI_Compliance/T03_Supplier_Due_Diligence_EU_Addendum.md), AI-CTRL-014 |
| PoC and Recommendation | PoC decision notes and the final recommendation, one column per vendor | [AI Security PoC Test Case Library](../06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md) |

## How to use it

1. **Settings.** Name the vendors, agree the domain weights (0 removes a domain) and choose which regional questions apply.
2. **Domain Checklist.** Plan the PoC: what to validate and the evidence each domain needs.
3. **Scoring.** Score each vendor from 0 to 5 per domain, with the evidence behind each score.
4. **Vendor Evidence.** Record which required evidence items each vendor supplied.
5. **Supplier Due Diligence.** For the shortlisted supplier, answer the questionnaire and check the contract clauses. Copy the sheet for each supplier.
6. **Recommend.** Record the PoC notes and recommendation, and use the Summary for procurement and management.

## How the scoring works

Each domain is scored on the wiki scale, from 5 (strong capability demonstrated with evidence) to 0 (not available or not demonstrated). The weighted score uses only the domains you scored, and a domain is flagged when its score is at or below the flag score on Settings. In the wiki scale, 2 means a complementary control is likely required.

## Licence and credit

The workbook is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), like the rest of the wiki. Suggested credit: "AI Security Vendor Evaluation Scorecard" by Nachiket Sathaye, AI Security Wiki, licensed under CC BY-SA 4.0. If you share an adapted version, say what you changed and release it under the same licence. Framework names, identifiers and short titles belong to their owners and are cited for mapping only.
