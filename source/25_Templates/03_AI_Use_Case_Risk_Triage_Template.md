---
title: "AI Use-Case Risk Triage Template (.xlsx)"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Templates"
nav_order: 3
description: "A downloadable Excel questionnaire for one AI use case: a prohibited-use screen, the wiki's triage questions, T01 tier scoring, the register risks that apply with their controls and evidence, and whether a full impact assessment is needed."
document_type: AI Security Wiki Template
version: 1.2
---

# AI Use-Case Risk Triage Template (.xlsx)

**[Download the AI Use-Case Risk Triage Template (.xlsx)](AI_Use_Case_Risk_Triage.xlsx)**

> **Purpose:** Triage one AI use case before it is built or bought: screen out prohibited uses, find which of the {{n:risks}} register risks apply, score its tier and decide whether a full impact assessment is needed. Built from the [AI Use-Case Risk Triage](../02_Risk_Management/02F_AI_Use_Case_Risk_Triage.md) page.

> **Audience:** AI product owners, risk management, GRC and AI governance committees.

> **Before you rely on it:** The wiki says its question-to-risk links are a starting design, not a validated instrument: check them against your own use cases before using the result as a gate. The tier bands and mandatory High overrides are the wiki's suggested defaults (orange cells), not regulatory values. The EU prohibited-practice list comes from the wiki's EU T01 page, which says its citations must be checked against the AI Act text and Commission guidelines. This is not legal advice.

## What is in the workbook

| Sheet | What it holds | Built from |
|---|---|---|
| README and License | How to use the workbook, colour legend, sources, licence, credit and disclaimer | Written for the workbook |
| Result | Tier, applicable risks, impact assessment trigger, next step, decision and approvals | Calculated from the other sheets |
| Use Case | Basics, purpose and data | [GCC T01 Intake and Risk Tiering](../11_GCC_AI_Compliance/T01_AI_Use_Case_Intake_and_Risk_Tiering.md) sections A to C |
| Stop Screen | A policy prohibition question and the EU AI Act Art. 5 practices | [EU T01 AI System Classification](../12_EU_AI_Compliance/T01_AI_System_Classification.md) |
| Risk Questions | The 43 triage questions A1 to E19, each linked to the register risks it switches on | [AI Use-Case Risk Triage](../02_Risk_Management/02F_AI_Use_Case_Risk_Triage.md) |
| Tiering | The eight scored T01 questions, tier bands and the two mandatory High overrides | [GCC T01 Intake and Risk Tiering](../11_GCC_AI_Compliance/T01_AI_Use_Case_Intake_and_Risk_Tiering.md) |
| Applicable Risks | All {{n:risks}} register risks, which questions switched each on, and the wiki controls and evidence | [Enterprise AI Risk Register](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI Risk to Control Mapping](../02_Risk_Management/02D_AI_Risk_to_Control_Mapping.md) |
| Triage Log and Worked Examples | A history of triage runs across use cases, and the wiki's three worked examples with how to calibrate | [AI Use-Case Risk Triage](../02_Risk_Management/02F_AI_Use_Case_Risk_Triage.md) |

## How to use it

1. **Use Case.** Describe the use case as it will run in production.
2. **Stop Screen.** Answer the policy question and, if the EU AI Act applies, the Art. 5 practices. Any Yes stops the use case.
3. **Risk Questions.** Answer all 36 questions Yes or No.
4. **Tiering.** Score the eight T01 questions from 0 to 3 and answer the two overrides.
5. **Applicable Risks.** Review which risks switched on and why, and take the controls and evidence listed against them.
6. **Result.** Read the tier, risks and next step, record the decision and approvals, then copy the calculated row into the Triage Log.

## When it asks for an impact assessment

The Result sheet asks for a full impact assessment on the wiki's own threshold: any Yes to C1, C3 or C4, or a Yes to both B2 and C2. ISO/IEC 42005:2025 clause 5.7 asks organizations to set their own threshold, so agree yours and record it. The [AI Impact Assessment Template (.docx)](09_AI_Impact_Assessment_Template.md) is the form to use next.

## Where it fits

Assess each applicable risk on the [AI Risk Register Template (.xlsx)](01_AI_Risk_Register_Template.md), and record the system on the [AI System Inventory Template (.xlsx)](02_AI_System_Inventory_Template.md).

## From the Builder Track

For an agent, the [Agent Architecture Patterns](../24_Builder_Track/02_Agent_Architecture_Patterns.md) review checklist and the lethal trifecta test help answer the triage questions about actions and data.

## Licence and credit

The workbook is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), like the rest of the wiki. Suggested credit: "AI Use-Case Risk Triage" by Nachiket Sathaye and Ankush Jain, AI Security Wiki, licensed under CC BY-SA 4.0. If you share an adapted version, say what you changed and release it under the same licence. The owner domains and risks AI-R29 to AI-R46 are adapted from the AI Risk Map v1.3 by Evan Wheeler (https://github.com/wheels344i-gte/ai-risk-map, RiskFramework.org), licensed under CC BY-SA 4.0. Framework names, identifiers and short titles belong to their owners and are cited for mapping only.
