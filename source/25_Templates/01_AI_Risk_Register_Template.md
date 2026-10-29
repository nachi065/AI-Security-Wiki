---
title: "AI Risk Register Template (.xlsx)"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Templates"
nav_order: 1
description: "A downloadable Excel workbook for running an AI risk register: the wiki's risks pre-filled, use-case triage, likelihood and impact scoring, mapped controls and evidence, framework and regulatory crosswalks, a dashboard and tracking checks."
document_type: AI Security Wiki Template
version: 1.5
---

# AI Risk Register Template (.xlsx)

**[Download the AI Risk Register Template (.xlsx)](AI_Risk_Register_Template.xlsx)**

> **Purpose:** Give risk, security and governance teams a ready-to-use workbook for assessing, treating and tracking AI risks, built from the [Enterprise AI Risk Register](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) and the pages around it.

> **Audience:** Risk management, GRC, security architecture, audit and AI product owners.

> **Illustrative example:** Every likelihood and impact in the workbook is the wiki's generic example, not an assessment of any organization. The scales, rating bands, deadlines, review intervals, appetite and acceptance authority on the Settings sheet are workbook defaults, not values from a standard. Re-score every risk and have the governing body approve the settings before you rely on the results.

## What is in the workbook

| Sheet | What it holds | Built from |
|---|---|---|
| README and License | How to use the workbook, colour legend, sources, licence, credit and third-party notices | Written for the workbook |
| Dashboard | Counts by rating, status and treatment, a likelihood by impact heat map, risks by owner domain, overdue items and risks to escalate | Calculated from the register |
| AI Risk Register | The {{n:risks}} risks pre-filled with description, owner domain, triage questions, mapped controls, evidence and framework references, plus columns for scenario, scoring, treatment, target values, owners, dates, status and review | [Enterprise AI Risk Register](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI Risk to Control Mapping](../02_Risk_Management/02D_AI_Risk_to_Control_Mapping.md), [Risk, Control and Test Traceability](../02_Risk_Management/02G_Risk_Control_Test_Traceability.md) |
| Guidelines | What to enter in every register column, and an illustrative worked example | Written for the workbook |
| Triage | The use-case triage questions; answering them marks which register risks apply | [AI Use-Case Risk Triage](../02_Risk_Management/02F_AI_Use_Case_Risk_Triage.md) |
| Methodology and Settings | Rating method, treatment options, review triggers and ISO/IEC 23894 alignment; editable scales, bands and risk criteria | [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md), [AI Risk Treatment Plan](../02_Risk_Management/02C_AI_Risk_Treatment_Plan.md) |
| AI Risk Library and Control Library | Reference copies of the risks and the {{n:controls}} control objectives with objective, evidence, audit test, owner and framework fields | [Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md) |
| Framework Matrix and Framework Crosswalk | Every item of every framework crosswalk, linked to wiki controls and register risks | [Framework Crosswalks](../23_Framework_Crosswalks/index.md) |
| Regulatory Crosswalk | Laws and guidance from the regional sections, with the wiki's verification tags | The Regulatory Crosswalk page of each regional section |
| Control Gaps and Threat Library | A weakness for each control, and threats and techniques from OWASP, MITRE ATLAS and NIST AI 600-1, linked to register risks | Control library and crosswalks |

## How to use it

1. **Settings.** Agree the likelihood and impact scales, rating bands, mitigation deadlines, appetite and who may accept each rating.
2. **Triage.** For one use case, answer the Yes/No questions. The register's Triage Result column then shows which risks apply.
3. **Assess.** For each risk that applies, write the scenario for your system, record existing controls and their coverage, and score likelihood and impact (1 to 4).
4. **Treat.** Choose Mitigate, Avoid, Transfer or Accept, use the mapped controls and evidence, and set the target likelihood and impact.
5. **Track.** Assign owners and dates, keep the status current, and clear every message in the Record Check column.
6. **Report.** Use the Dashboard for the risk report and for risks to escalate to the AI Governance Committee.

## How the scoring works

The score is likelihood (1 to 4) multiplied by impact (1 to 4), from 1 to 16, and the rating (Low, Medium, High or Critical) is read from the bands on the Settings sheet. Impact is scored directly and its type is recorded in a separate column, so risks that are not about confidentiality, integrity or availability, such as cost, workforce or bias, can be rated on the same scale.

## How the framework links were made

Where a wiki crosswalk names register risks (FINOS risks, the AI Risk Map, NIST AI 600-1 and the OWASP MCP Top 10), the workbook uses that mapping. Where a crosswalk names only controls, the workbook links a framework item to the risks those controls treat. That second kind of link is broader than a direct mapping; the Framework Matrix marks each column "direct" or "via controls".

## Licence and credit

The workbook is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), like the rest of the wiki. Suggested credit: "AI Risk Register Workbook" by Nachiket Sathaye and Ankush Jain, AI Security Wiki, licensed under CC BY-SA 4.0. If you share an adapted version, say what you changed and release it under the same licence. The owner domains and risks AI-R29 to AI-R46 are adapted from the AI Risk Map v1.3 by Evan Wheeler (https://github.com/wheels344i-gte/ai-risk-map, RiskFramework.org), licensed under CC BY-SA 4.0. Framework names, identifiers and short titles belong to their owners and are cited for mapping only.
