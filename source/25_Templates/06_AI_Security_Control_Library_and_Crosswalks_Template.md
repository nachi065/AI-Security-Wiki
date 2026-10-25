---
title: "AI Security Control Library and Crosswalks Template (.xlsx)"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Templates"
nav_order: 6
description: "A downloadable Excel workbook of the wiki's AI security controls with every library field, ready to track implementation and testing, cross-referenced to every item of the wiki's framework crosswalks and to the register risks."
document_type: AI Security Wiki Template
version: 1.2
---

# AI Security Control Library and Crosswalks Template (.xlsx)

**[Download the AI Security Control Library and Crosswalks Template (.xlsx)](AI_Security_Control_Library_and_Crosswalks.xlsx)**

> **Purpose:** Track the implementation and testing of the {{n:controls}} controls in the [Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md), and see what each framework item and register risk they cover. The workbook holds 890 items across 47 frameworks, standards, ethics instruments and regional regulations.

> **Audience:** Security architecture, GRC, control owners and audit.

> **Before you rely on it:** Every link between a framework item and a control is the wiki's own mapping, not the framework owner's. Where a crosswalk maps an item to risks only, the controls are derived through the AI Risk to Control Mapping and labelled "Derived via mapped risks". The Baseline and Advanced tiers are the author's judgement, not a requirement of any framework. Test intervals (orange cells) are read from each control's review frequency; set your own where the frequency is event-driven.

## What is in the workbook

| Sheet | What it holds | Built from |
|---|---|---|
| README and License | How to use the workbook, colour legend, sources, licence, credit and disclaimer | Written for the workbook |
| Dashboard | Implementation and testing status by tier and family, and overdue testing | Calculated from the library |
| Control Library | The {{n:controls}} controls with every library field (including assurance stage and deployment model), plus columns for applicability, status, owner, evidence location and testing | [Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md), [Control Tiers](../03_Control_Library/06_Control_Tiers.md) |
| Coverage | How much of each of the 47 framework columns your implemented controls cover | [Framework Crosswalks](../23_Framework_Crosswalks/index.md) |
| Framework Crosswalk | 910 framework items with their controls and whether those are implemented | [Framework Crosswalks](../23_Framework_Crosswalks/index.md) and the regional crosswalks |
| Framework Matrix | One row per control across all 47 frameworks | Framework Crosswalks |
| Risk to Control | Which register risks are fully, partly or not covered by implemented controls | [AI Risk to Control Mapping](../02_Risk_Management/02D_AI_Risk_to_Control_Mapping.md) |

## How to use it

1. **Control Library.** Mark each control applicable or not, and set its implementation status, named owner, evidence location and last test.
2. **Coverage.** See how much of each framework your implemented controls cover.
3. **Framework Crosswalk.** Filter by framework to see each item, its controls and whether they are implemented.
4. **Framework Matrix.** Read one control across all frameworks, for example to answer an auditor's mapping question.
5. **Risk to Control.** See which register risks are covered.
6. **Dashboard.** Report status by tier and family, and testing that is overdue.

## Licence and credit

The workbook is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), like the rest of the wiki. Suggested credit: "AI Security Control Library and Crosswalks" by Nachiket Sathaye and Ankush Jain, AI Security Wiki, licensed under CC BY-SA 4.0. If you share an adapted version, say what you changed and release it under the same licence. The AI Risk Map v1.3 crosswalk items, and the risks AI-R29 to AI-R46 they map to, are adapted from the AI Risk Map v1.3 by Evan Wheeler, RiskFramework.org, licensed under CC BY-SA 4.0. Framework names, identifiers and short titles belong to their owners and are cited for mapping only.
