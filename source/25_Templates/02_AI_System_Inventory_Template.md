---
title: "AI System Inventory Template (.xlsx)"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Templates"
nav_order: 2
description: "A downloadable Excel workbook for keeping an inventory of every AI system, model, agent and AI feature in use, with owner, tier, data, supplier, regulatory scope, assurance evidence and review checks."
document_type: AI Security Wiki Template
version: 1.0
---

# AI System Inventory Template (.xlsx)

**[Download the AI System Inventory Template (.xlsx)](AI_System_Inventory.xlsx)**

> **Purpose:** Keep one record of every AI system, model, agent and AI feature in use, with its owner, tier, data, supplier, regulatory scope and assurance evidence. The inventory is the evidence for control AI-CTRL-011 (AI Use-Case Registry and Risk Tiering) in the [Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md).

> **Audience:** AI governance, GRC, security architecture, privacy and AI product owners.

> **Before you rely on it:** The review intervals and due-soon window on the Settings sheet are workbook defaults (orange cells), not values from a standard. The regulatory columns follow the wiki's GCC and EU templates, which say their regional claims come from secondary sources and must be checked. Rows 6 and 7 are the fictional examples from those pages: overwrite or delete them.

## What is in the workbook

| Sheet | What it holds | Built from |
|---|---|---|
| README and License | How to use the workbook, colour legend, sources, licence, credit and disclaimer | Written for the workbook |
| Dashboard | Counts by tier, status, autonomy, asset type, EU AI Act tier and review state | Calculated from the inventory |
| AI System Inventory | 53 columns in six sections and 300 rows with dropdowns, a Record Check column and a Review Alert column | [GCC T09 AI Model and System Inventory](../11_GCC_AI_Compliance/T09_AI_System_Inventory.md), [EU T09 AI System Inventory](../12_EU_AI_Compliance/T09_AI_System_Inventory.md), [GCC T01 Intake and Risk Tiering](../11_GCC_AI_Compliance/T01_AI_Use_Case_Intake_and_Risk_Tiering.md) |
| Discovery Sweeps | A log of searches for AI that is not yet in the inventory | [AI Risk Treatment Plan](../02_Risk_Management/02C_AI_Risk_Treatment_Plan.md) (phase 1, discovery) |
| Guidelines | What each column means and its wiki source, plus the maintenance rules | The T09 pages |
| Settings and Lists | Review interval for each tier, tier requirements and the dropdown values | Workbook defaults and the T01 and T09 pages |

## How to use it

1. **Settings.** Agree the review interval for each tier and record who approved it.
2. **Discover.** Run a discovery sweep and log it on Discovery Sweeps.
3. **Record.** Add one row per AI system. Yellow cells are inputs and many have dropdowns.
4. **Fix gaps.** Clear every Record Check message. It flags blank required fields, missing evidence for High tier systems, likely under-tiering, missing vendor reviews and missing transfer mechanisms.
5. **Review.** Keep Last Review Date current. Review Alert shows what is overdue.
6. **Report.** Use the Dashboard for the inventory report.

## Where it fits

Use the [AI Use-Case Risk Triage Template (.xlsx)](03_AI_Use_Case_Risk_Triage_Template.md) to set each system's tier, then assess each High and Medium system on the [AI Risk Register Template (.xlsx)](01_AI_Risk_Register_Template.md) and enter the risk IDs in the Register Risk IDs column.

## From the Builder Track

An agent built with the [Builder Track](../24_Builder_Track/01_Secure_Your_First_Agent.md#b1-register-the-agent-and-name-an-owner) already has most of a row: its `policy.json` entry names the owner, the tools it can call and its limits. Copy those into this inventory and record the date its kill switch was last tested.

## Licence and credit

The workbook is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), like the rest of the wiki. Suggested credit: "AI System Inventory" by Nachiket Sathaye and Ankush Jain, AI Security Wiki, licensed under CC BY-SA 4.0. If you share an adapted version, say what you changed and release it under the same licence. Framework names, identifiers and short titles belong to their owners and are cited for mapping only.
