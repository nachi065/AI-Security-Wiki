---
title: "T10 Technical Documentation Index and Conformity Checklist"
author: Nachiket Sathaye
parent: "EU AI Compliance"
nav_order: 18
description: "Readiness index for high-risk AI providers: technical file sections, data governance, logging, human oversight, QMS and the conformity route."
document_type: AI Security Wiki Reference
version: 1.0
---

# T10 Technical Documentation Index and Conformity Checklist

> **Verification required.** This is a working template, not a regulator-approved form. Where it cites an article or a date, the citation comes from secondary sources or from memory of the legal text and is a pointer to check. This is not legal advice.

For providers of high-risk systems. Wiki control: [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038). The Annex IV headings below are given from memory of its structure [Recalled]. Replace them with the exact Annex IV list from the Official Journal. This is a readiness index and does not amount to a conformity assessment. Some product-sector rules and the omnibus may change who must do what.

System ID: ______ Version: ______ Owner: ______ Last updated: ______

## 1. Technical file index

| # | Section | Content to include | Location / link | Owner | Status |
|---|---|---|---|---|---|
| 1 | General description | Intended purpose, provider, version history, hardware and software context, forms of placing on the market, instructions for use | | | |
| 2 | Development process | Design choices, architecture, algorithms and key choices, data requirements, training methods, optimisation, human oversight measures, pre-determined changes | | | |
| 3 | Monitoring, functioning and control | Capabilities and limits, accuracy levels and expected errors for groups, foreseeable misuse and risks to health, safety and rights, oversight measures, input data specification | | | |
| 4 | Performance metrics | Why chosen, declared values | | | |
| 5 | Risk management system | Process, identified risks, mitigations, residual risk acceptance | | | |
| 6 | Lifecycle changes | Relevant changes by the provider | | | |
| 7 | Standards and specifications applied | Harmonised or other; where none, the solutions adopted | | | |
| 8 | Declaration of conformity | Copy | | | |
| 9 | Post-market monitoring plan | Plan and data collection | | | |

## 2. Data governance record

| Item | Entry |
|---|---|
| Training, validation and test datasets: origin, scope, characteristics | |
| Collection and preparation steps | |
| Assumptions made | |
| Suitability assessment, availability, quantity | |
| Bias examination and mitigation ([AI-CTRL-041](../11_GCC_AI_Compliance/06_Proposed_Control_Fairness_Bias_Explainability.md), proposed) | |
| Gaps and how they were addressed | |
| Special category data use and necessity record | |
| Copyright and licence position | |

## 3. Logging design

Wiki control: [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008).

| Item | Entry |
|---|---|
| Events logged | |
| Fields (time, input reference, model version, output, reviewer action) | |
| Retention | |
| Access control | |
| Ability to reconstruct a decision | |

## 4. Human oversight design (Art. 14 themes)

| Question | Answer |
|---|---|
| What can the overseer see and understand? | |
| How is automation bias addressed? | |
| Can they override, reverse or stop? | |
| Who is competent and trained? | |
| Is there a safe stop procedure? | |
| Evidence of use in practice | |

## 5. Accuracy, robustness, cybersecurity

| Item | Entry |
|---|---|
| Metrics and results | |
| Error handling | |
| Feedback-loop controls | |
| Resilience to poisoning, adversarial examples, model evasion and confidentiality attacks | |
| Test reports | |

## 6. Quality management system

Procedures to hold: design and verification, data management, risk management, post-market monitoring, incident reporting, communication with authorities, record keeping, resource management, accountability framework.

Standard followed: ______. EN 18286:2026 is reported as approved, with its OJ citation pending [Reported].

## 7. Conformity route

| Item | Entry |
|---|---|
| Route (internal control or notified body, per Annex and sector) | |
| Notified body (if any) and certificate | |
| Declaration of conformity date | |
| CE marking applied | |
| EU database registration reference | |
| Authorised representative (non-EU) | |
| Instructions for use delivered to deployers | |

## 8. Deployer pack contents

Intended purpose, accuracy and limits, oversight measures, input data guidance, log access, maintenance, expected lifetime, and how to run a FRIA or DPIA.

## 9. Sign-off

| Role | Name | Date |
|---|---|---|
| Provider representative | | |
| Independent reviewer | | |
