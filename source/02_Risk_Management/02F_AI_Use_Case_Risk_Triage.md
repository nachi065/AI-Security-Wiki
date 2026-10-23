---
title: "AI Use-Case Risk Triage"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Risk Management"
nav_order: 6
description: "Yes/No questions that decide which risks in the register apply to an AI use case, to use alongside the T01 intake form that sets the tier."
document_type: AI Security Wiki Reference
version: 1.1
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
| A6 | In a single session, does it read untrusted content, reach private data, and have a way to send data out (email, web requests, posting, rendering remote links or images)? See the [lethal trifecta](../24_Builder_Track/02_Agent_Architecture_Patterns.md#the-lethal-trifecta-and-the-rule-of-two). | AI-R05, AI-R06, AI-R24 |

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

## E. Business, people, legal and supply chain

These questions were added in version 1.1 for risks AI-R29 to AI-R46, which were adapted from the AI Risk Map (see the credit on the [Enterprise AI Risk Register](02B_Enterprise_AI_Risk_Register.md#credit-ai-risk-map)).

| # | Question | If Yes, apply risks |
|---|---|---|
| E1 | Is the use case being funded or scaled at significant cost, or without a stated problem and success measure? | AI-R29, AI-R30 |
| E2 | Does the cost depend on a provider's pricing, or on usage that is hard to forecast? | AI-R30, AI-R35 |
| E3 | Does it depend on one model provider, a proprietary API or fine-tuning that would not transfer to another provider? | AI-R31 |
| E4 | Does it share a base model with other systems, or with the controls that check its output? | AI-R32 |
| E5 | Will it take over work that people do today, or change their roles? | AI-R33, AI-R34 |
| E6 | Will you fine-tune, rebrand or change the purpose of a third-party model, or self-host an open-weight model? | AI-R36, AI-R37, AI-R44 |
| E7 | Could its prompts, outputs or traces be needed in litigation, a regulatory inquiry or a dispute? | AI-R38 |
| E8 | Is it a model used in decisions that model risk management or financial reporting controls cover? | AI-R39, AI-R40 |
| E9 | Will the organization make external claims about its AI capability, or rely on a vendor's claim? | AI-R41 |
| E10 | Is it conversational, with a persona, or open to the public or to vulnerable users? | AI-R42 |
| E11 | Will it write code or install software dependencies? | AI-R43 |
| E12 | Can it act on behalf of users, with permissions broader than some of those users hold, or is its activity watched by security monitoring? | AI-R45, AI-R46 |

## When to run a full impact assessment

Any **Yes** to C1, C3 or C4, or a **Yes** to both B2 and C2, should trigger a full impact assessment under [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042) before go-live, in addition to the risk assessment. These are this wiki's thresholds for sensitive uses. ISO/IEC 42005:2025, clause 5.7, asks an organization to set its own thresholds for sensitive uses, restricted uses and impact scales, so adjust them to your own and record the version you use. Uses that your AI policy prohibits are stopped at intake and are not assessed.

## Worked examples

These show how the answers combine. The answers are illustrative, not an assessment of any real system. They were written before section E was added and show answers to sections A to D only.

| Use case | Yes answers | Applicable risks |
|---|---|---|
| Internal meeting summariser (SaaS, staff use, no personal data of customers) | B1, B3, D1, D7 | AI-R01, AI-R03, AI-R06, AI-R09, AI-R10, AI-R13, AI-R15, AI-R16 |
| Customer-facing support assistant with retrieval over policy documents | B2, B3, B5, C2, D1, D4 | AI-R03, AI-R05, AI-R06, AI-R10, AI-R12, AI-R13, AI-R16, AI-R17, AI-R20, AI-R27, AI-R28 |
| Internal agent that can call finance APIs and prepare payments | A1, A2, A5, B1, B2, C5, D2, D7 | AI-R01, AI-R03, AI-R04, AI-R06, AI-R07, AI-R09, AI-R11, AI-R12, AI-R15, AI-R18, AI-R19, AI-R22, AI-R24, AI-R28 |

## Coverage

Every risk in the register is switched on by at least one question. If you add a risk to the register, add or extend a question here so the new risk can be found at intake.

## Recording the result

Record for each use case: date, answers, applicable risk IDs, T01 score and tier, risk owner, and the decision on the next step. Run the triage again when any answer changes.

## Calibrating the questions

The links from questions to risks are judgments. To calibrate them, run the triage on a sample of real use cases that have already been through full assessment, and compare the applicable risks with the risks the assessment found. A risk found by the assessment but missed by triage means a question is missing or too narrow. A risk raised by triage and never confirmed across the sample means a question is too broad. Record the sample size and the changes made, and repeat after each major change to the register.

## Related pages

- [AI Risk Methodology](02A_AI_Risk_Methodology.md)
- [Enterprise AI Risk Register](02B_Enterprise_AI_Risk_Register.md)
- [AI Risk to Control Mapping](02D_AI_Risk_to_Control_Mapping.md)
- [T01 AI Use-Case Intake and Risk Tiering](../11_GCC_AI_Compliance/T01_AI_Use_Case_Intake_and_Risk_Tiering.md)
