---
title: "T01 AI Use-Case Intake and Risk Tiering"
author: Nachiket Sathaye
parent: "GCC AI Compliance"
nav_order: 9
description: "Fill-in form to register an AI use case and score it into a Low, Medium or High risk tier before build or purchase."
document_type: AI Security Wiki Reference
version: 1.0
---

# T01 AI Use-Case Intake and Risk Tiering

> **Verification required.** This is a working template, not a regulator-approved form. Where it names a regional instrument, the claim comes from secondary sources and is a pointer to check, not a confirmed legal requirement. This is not legal advice.

<!-- -->

> **How to use:** This is a blank form. Copy it and fill in the empty cells and blanks for your system. To copy it, follow the "Suggest an edit to this page" link in the footer to reach its Markdown source.

Wiki controls: [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) (registry and tiering), [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037). Complete before build or purchase.

## A. Basics

| Field | Entry |
|---|---|
| Use-case ID | |
| Name | |
| Business owner | |
| Technical owner | |
| Date submitted | |
| Build / buy / embedded in vendor product | |
| Vendor and product (if any) | |
| Intended users | Staff / customers / public |
| Countries of users and data subjects | |
| Regulated entity or sector (bank, insurer, health, government, other) | |

## B. Purpose and function

| Field | Entry |
|---|---|
| Problem and intended benefit | |
| What does the AI do? (classify, predict, generate, recommend, act) | |
| Does it make or support decisions about people? | Yes / No |
| Is a human required to approve outputs? | Yes / No / Sometimes |
| Can it take actions in other systems (agentic)? | Yes / No; list tools |

## C. Data

| Field | Entry |
|---|---|
| Personal data used (types) | |
| Special or sensitive categories (health, religion, biometrics, children, etc.) | |
| Source and lawful basis (record legal view) | |
| Customer data used to train or fine-tune? | |
| Hosting country and provider | |
| Cross-border transfer? | |
| Retention period for prompts, outputs, logs | |

## D. Tiering questions (score 0 to 3 each)

| # | Question | Score |
|---|---|---|
| 1 | Effect on a person's legal rights, finances, employment, health or access to services | |
| 2 | Degree of automation (3 = no human review) | |
| 3 | Scale (users or decisions per month) | |
| 4 | Sensitivity of data | |
| 5 | Reversibility of harm (3 = irreversible) | |
| 6 | Regulatory exposure (regulated entity, government customer) | |
| 7 | Autonomy and tool access | |
| 8 | Vendor opacity and third-party dependence | |

## E. Tier

| Total | Tier | Minimum requirements |
|---|---|---|
| 0 to 5 | Low | Register; policy acknowledgement |
| 6 to 11 | Medium | Register; impact assessment (short [T02](T02_AI_Impact_Assessment.md)); vendor addendum if external |
| 12 to 24 | High | Full [T02](T02_AI_Impact_Assessment.md); bias test [T10](T10_Bias_Testing_Record.md); human oversight and kill switch test; residency attestation [T04](T04_Data_Residency_Attestation.md); approval by governance lead |

Set a **mandatory High** override if the system decides on credit, insurance, employment, eligibility, or uses sensitive categories. These thresholds are suggested defaults, not regulatory values. Adjust and record the approval.

## F. Approvals

| Role | Name | Decision | Date |
|---|---|---|---|
| Business owner | | | |
| Privacy / DPO | | | |
| Security | | | |
| AI governance lead | | | |
| Legal (if High) | | | |

## G. Triggers for re-tiering

New data type, new country, new model or vendor, new decision type, material incident, regulator change.
