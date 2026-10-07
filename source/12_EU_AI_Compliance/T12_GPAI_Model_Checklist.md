---
title: "T12 General-Purpose AI Model Checklist"
author: Nachiket Sathaye
parent: "EU AI Compliance"
nav_order: 20
description: "Checklist of AI Act duties for providers of general-purpose AI models, including systemic-risk models, and for teams that build on one."
document_type: AI Security Wiki Reference
version: 1.0
---

# T12 General-Purpose AI Model Checklist

> **Verification required.** This is a working template, not a regulator-approved form. Where it cites an article or a date, the citation comes from secondary sources or from memory of the legal text and is a pointer to check. This is not legal advice.

Wiki controls: [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029). Use part A if you provide a general-purpose AI (GPAI) model and part B if you build on one. The obligation list is [Recalled] from Arts. 51 to 55. Read the text and the Commission's GPAI guidelines of 10 July 2025 [Reported]. GPAI duties have applied since 2 Aug 2025, and the AI Office gained enforcement powers on 2 Aug 2026 [Reported]. Models that were on the market before 2 Aug 2025 reportedly have until 2 Aug 2027 [Reported].

## A. Provider checklist

| # | Obligation | Status | Evidence |
|---|---|---|---|
| A1 | Is it a GPAI model under the guidelines? Record the reasoning | | |
| A2 | Technical documentation for the AI Office and downstream providers | | |
| A3 | Information for downstream providers that integrate the model | | |
| A4 | Copyright compliance policy, including respect for text-and-data-mining opt-outs | | |
| A5 | Public summary of training content (using the template) | | |
| A6 | Authorised representative, if non-EU | | |
| A7 | Open-source exemption analysis (does it apply, and are systemic-risk models excluded) | | |
| A8 | Code of Practice: signed, partially signed, or an alternative demonstration (reported signatories include several large providers) | | |

### Systemic-risk models

| # | Obligation | Status | Evidence |
|---|---|---|---|
| S1 | Classification (reported presumption threshold: training compute above 10^25 floating-point operations) | | |
| S2 | Notify the Commission | | |
| S3 | Model evaluation, including adversarial testing | | |
| S4 | Assess and mitigate systemic risks | | |
| S5 | Serious incident tracking and reporting to the AI Office | | |
| S6 | Cybersecurity protection of the model and its infrastructure | | |

## B. Downstream checklist

For teams that integrate a GPAI model.

| # | Question | Answer | Evidence |
|---|---|---|---|
| B1 | Does the model provider supply documentation and intended-use information? | | |
| B2 | Does your use make you a provider of a high-risk or transparency-duty system? | | |
| B3 | Have you checked the supplier's Code of Practice status? | | |
| B4 | Do contracts cover model changes, deprecation and incident notice? | | |
| B5 | Have you tested the model in your use case (bias, safety, accuracy, language)? | | |
| B6 | Data flows and transfers ([T04](T04_Data_Location_and_Transfer_Record.md)) | | |
| B7 | Content marking and disclosure obligations ([T06](T06_Transparency_Notice.md)) | | |
| B8 | Fine-tuning: did you become a provider of a new model? Record the reasoning | | |

## C. Decisions

Owner: ______ Date: ______ Next review (on a model version change or a guideline update): ______
