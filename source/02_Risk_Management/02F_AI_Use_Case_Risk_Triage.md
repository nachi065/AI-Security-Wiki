---
title: "AI Use-Case Risk Triage"
author: Nachiket Sathaye
parent: "Risk Management"
nav_order: 6
description: "Yes/No questions that decide which risks in the register apply to an AI use case, to use alongside the T01 intake form that sets the tier."
document_type: AI Security Wiki Reference
version: 1.0
---

# AI Use-Case Risk Triage

> **Purpose:** Decide quickly which risks in the [Enterprise AI Risk Register](02B_Enterprise_AI_Risk_Register.md) apply to an AI use case, so the right controls and evidence are requested from the start.

> **Audience:** AI product owners, security architecture, GRC, vendor evaluation teams.

> **When to use:** At intake, and again whenever a review trigger in the [AI Risk Methodology](02A_AI_Risk_Methodology.md) occurs.

> **What this page does not do:** It does not set the risk tier. Use the scored questions and tier bands in [T01 AI Use-Case Intake and Risk Tiering](../11_GCC_AI_Compliance/T01_AI_Use_Case_Intake_and_Risk_Tiering.md) for that; this page only identifies which risks are in play. The question-to-risk links below are a starting design, not a validated instrument. Check them against your own use cases before using the result as a gate.

## How it works

1. Answer every question Yes or No for the use case as it will run in production.
2. Each **Yes** switches on the risks in the right-hand column. The union is the use case's applicable risk list.
3. Take the controls and evidence for each applicable risk from the [AI Risk to Control Mapping](02D_AI_Risk_to_Control_Mapping.md).
4. Score the use case with T01 to get its tier, and apply the tier's minimum requirements.

## A. Autonomy and actions

| # | Question | If Yes, apply risks |
|---|---|---|
| A1 | Can the AI call tools, APIs or systems, or change data? | AI-R07, AI-R24, AI-R22 |
| A2 | Can it take actions without a human approving each one? | AI-R07, AI-R19, AI-R18 |
| A3 | Does it keep persistent memory, notes or state across sessions? | AI-R21 |
| A4 | Does it interact with other agents, or use skills, plugins or MCP servers? | AI-R23, AI-R25 |
| A5 | Can it reach files, a shell, a browser session or code repositories? | AI-R22, AI-R04 |

## B. Data and hosting

| # | Question | If Yes, apply risks |
|---|---|---|
| B1 | Will it process confidential, restricted or regulated data? | AI-R01, AI-R03, AI-R06 |
| B2 | Will it process personal data? | AI-R03, AI-R28 |
| B3 | Is the model or service hosted by a third party? | AI-R10, AI-R16, AI-R13 |
| B4 | Could data be processed or stored outside the approved jurisdiction? | AI-R10 |
| B5 | Does it retrieve from internal knowledge sources or a vector store? | AI-R05, AI-R06, AI-R17 |
| B6 | Will it be fine-tuned or trained on enterprise data? | AI-R08, AI-R17 |

## C. Effect on people and the business

| # | Question | If Yes, apply risks |
|---|---|---|
| C1 | Will its output inform or make decisions about individuals (eligibility, pricing, hiring, access, service level)? | AI-R14, AI-R15, AI-R19, AI-R28 |
| C2 | Is it customer-facing or public-facing? | AI-R20, AI-R05, AI-R12 |
| C3 | Does it operate in, or affect, critical infrastructure or safety-relevant processes? | AI-R01, AI-R13, AI-R12 |
| C4 | Is the process regulated, so the AI step must meet the same supervisory standard as a human one? | AI-R28, AI-R15 |
| C5 | Will people act on its output without independent checking? | AI-R12, AI-R19 |

## D. Model and operations

| # | Question | If Yes, apply risks |
|---|---|---|
| D1 | Does the provider control updates to the underlying model (aliases, silent upgrades)? | AI-R16 |
| D2 | Could usage or cost grow quickly without a human noticing (automated traffic, loops)? | AI-R11 |
| D3 | Will it show or log reasoning steps, intermediate tool output or system instructions? | AI-R26 |
| D4 | Will it generate content or code that is published, shipped or sent externally? | AI-R27, AI-R20 |
| D5 | Is the business process dependent on it being available? | AI-R13 |
| D6 | Does it lack a registered purpose, or could it be reused for a purpose other than the approved one? | AI-R18, AI-R02 |
| D7 | Might its outputs or actions later need to be investigated or evidenced (an incident, a dispute, an audit)? | AI-R09, AI-R15 |

## Worked examples

These show how the answers combine. The answers are illustrative, not an assessment of any real system.

| Use case | Yes answers | Applicable risks |
|---|---|---|
| Internal meeting summariser (SaaS, staff use, no personal data of customers) | B1, B3, D1, D7 | AI-R01, AI-R03, AI-R06, AI-R09, AI-R10, AI-R13, AI-R15, AI-R16 |
| Customer-facing support assistant with retrieval over policy documents | B2, B3, B5, C2, D1, D4 | AI-R03, AI-R05, AI-R06, AI-R10, AI-R12, AI-R13, AI-R16, AI-R17, AI-R20, AI-R27, AI-R28 |
| Internal agent that can call finance APIs and prepare payments | A1, A2, A5, B1, B2, C5, D2, D7 | AI-R01, AI-R03, AI-R04, AI-R06, AI-R07, AI-R09, AI-R11, AI-R12, AI-R15, AI-R18, AI-R19, AI-R22, AI-R24, AI-R28 |

## Coverage

Every risk from AI-R01 to AI-R28 is switched on by at least one question. If you add a risk to the register, add or extend a question here so the new risk can be found at intake.

## Recording the result

Record for each use case: date, answers, applicable risk IDs, T01 score and tier, risk owner, and the decision on the next step. Run the triage again when any answer changes.

## Calibrating the questions

The links from questions to risks are judgments. To calibrate them, run the triage on a sample of real use cases that have already been through full assessment, and compare the applicable risks with the risks the assessment found. A risk found by the assessment but missed by triage means a question is missing or too narrow. A risk raised by triage and never confirmed across the sample means a question is too broad. Record the sample size and the changes made, and repeat after each major change to the register.

## Related pages

- [AI Risk Methodology](02A_AI_Risk_Methodology.md)
- [Enterprise AI Risk Register](02B_Enterprise_AI_Risk_Register.md)
- [AI Risk to Control Mapping](02D_AI_Risk_to_Control_Mapping.md)
- [T01 AI Use-Case Intake and Risk Tiering](../11_GCC_AI_Compliance/T01_AI_Use_Case_Intake_and_Risk_Tiering.md)
