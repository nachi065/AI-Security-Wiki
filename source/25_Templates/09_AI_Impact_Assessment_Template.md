---
title: "AI Impact Assessment Template (.docx)"
author: Nachiket Sathaye
parent: "Templates"
nav_order: 9
description: "A downloadable Word template for a combined data protection and fundamental rights impact assessment of an AI system, built from the wiki's GCC and EU impact assessment forms, with benefits, misuse, fairness, oversight, consultation and decision sections."
document_type: AI Security Wiki Template
version: 1.0
---

# AI Impact Assessment Template (.docx)

**[Download the AI Impact Assessment Template (.docx)](AI_Impact_Assessment_Template.docx)**

> **Purpose:** Assess the impact of one AI system or use case on people before go-live, and reassess it on material change and at least annually, as control AI-CTRL-042 in the [Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md) asks.

> **Audience:** Privacy and data protection officers, AI product owners, risk management, legal and AI governance committees.

> **Before you rely on it:** This combined form is a convenience and does not replace any assessment the law requires, such as a GDPR Art. 35 DPIA or an EU AI Act Art. 27 FRIA. The wiki marks those citations as recalled or reported, so confirm which legal duties apply and consult your data protection officer. Sections marked [EU] or [GCC] come from the regional forms: delete the ones that do not apply. This is not legal advice.

## What is in the document

| Section | What it holds | Built from |
|---|---|---|
| Front matter | Cover, a how-to-use box with the triage triggers, and a table of contents | [AI Use-Case Risk Triage](../02_Risk_Management/02F_AI_Use_Case_Risk_Triage.md) |
| 1 to 2. Summary and description | Identifiers, trigger, tier, which assessments are required, and the system's purpose, uses, misuse, people affected, data and oversight | [GCC T02 AI Impact Assessment](../11_GCC_AI_Compliance/T02_AI_Impact_Assessment.md), [EU T02 Impact Assessment (FRIA and DPIA Combined)](../12_EU_AI_Compliance/T02_Impact_Assessment_FRIA_DPIA.md) |
| 3. Expected benefits | Benefits, who gains, how they are measured and the target | [ISO/IEC AI Standards Crosswalk](../23_Framework_Crosswalks/15_ISO_IEC_AI_Standards_Crosswalk.md) (ISO/IEC 42005) |
| 4 to 6. Lawful basis, rights and transfers | Necessity and proportionality, rights and transparency, and cross-border transfers | GCC and EU T02 |
| 7. Impacts on people | Scored risks to individuals with mitigations, and a fundamental rights analysis | GCC and EU T02, [Proposed Control: Fundamental Rights Impact Assessment](../12_EU_AI_Compliance/06_Proposed_Control_Fundamental_Rights_Impact_Assessment.md) |
| 8 to 10. Fairness, oversight and consultation | Bias testing and explanations, oversight and security, and the parties consulted | [Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md) (AI-CTRL-041, AI-CTRL-025), GCC and EU T02 |
| 11 to 12. Decision and review history | Outcome, conditions, approver, next review, reassessment triggers and version history | GCC and EU T02, AI-CTRL-042 |

## How to use it

1. **Decide if it is needed.** The [AI Use-Case Risk Triage](../02_Risk_Management/02F_AI_Use_Case_Risk_Triage.md) asks for a full impact assessment on any Yes to C1, C3 or C4, or a Yes to both B2 and C2. ISO/IEC 42005:2025 clause 5.7 asks you to set your own threshold.
2. **Describe.** Complete sections 1 and 2 with the people who run the system.
3. **Assess.** Record the benefits, then work through the lawful basis, rights, transfers, impacts and fairness sections.
4. **Consult.** Record the data protection officer's advice and the other parties' views in section 10.
5. **Decide.** Weigh the benefits against the residual impacts and record the decision before go-live.
6. **Review.** Reassess on the triggers in section 11 and at least annually, and add a row to the review history.

## What it adds to the regional forms

The wiki's ISO/IEC AI Standards Crosswalk notes that its impact assessment templates focus on harms, while ISO/IEC 42005 clause 6.8.2 asks for benefits as well. Section 3 closes that gap. The template also adds intended and unintended uses, misuse and interested parties, following the ISO/IEC 42005 rows of the same crosswalk.

## Licence and credit

The document is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), like the rest of the wiki. Suggested credit: "AI Impact Assessment Template" by Nachiket Sathaye, AI Security Wiki, licensed under CC BY-SA 4.0. If you share an adapted version, say what you changed and release it under the same licence. Framework names, identifiers and short titles belong to their owners and are cited for mapping only.
