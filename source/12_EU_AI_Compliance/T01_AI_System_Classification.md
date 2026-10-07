---
title: "T01 AI System Classification (Role and Risk Tier)"
author: Nachiket Sathaye
parent: "EU AI Compliance"
nav_order: 9
description: "Fill-in form to classify an AI system under the EU AI Act: prohibited-practice screen, provider or deployer role, risk tier, GDPR flags and next steps."
document_type: AI Security Wiki Reference
version: 1.0
---

# T01 AI System Classification (Role and Risk Tier)

> **Verification required.** This is a working template, not a regulator-approved form. Where it cites an article or a date, the citation comes from secondary sources or from memory of the legal text and is a pointer to check. This is not legal advice.

Wiki controls: [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) (registry and tiering), [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037). Article references are [Recalled]; verify them. Complete this form before build, purchase or change.

## A. Basics

| Field | Entry |
|---|---|
| System ID | |
| Name and version | |
| Business owner / technical owner | |
| Build / buy / embedded in vendor product | |
| Vendor and product | |
| Intended purpose (precise wording) | |
| Users and affected persons | |
| Member States of use | |
| Is it used in the EU, or is its output used in the EU? | |

## B. Is it an AI system?

The AI Act definition: a machine-based system that operates with some autonomy and infers from its input how to generate outputs that can influence environments.

Answer and reasoning: ______

## C. Prohibited screen (Art. 5)

Check each practice. Any "Yes" stops the project pending legal review.

| Practice | Yes / No |
|---|---|
| Subliminal or manipulative techniques causing harm | |
| Exploiting vulnerabilities (age, disability, situation) | |
| Social scoring leading to detrimental treatment | |
| Predicting a criminal offence solely from profiling | |
| Untargeted scraping of facial images for databases | |
| Emotion recognition in the workplace or in education (except for medical or safety reasons) | |
| Biometric categorisation inferring sensitive attributes | |
| Real-time remote biometric identification in public for law enforcement | |
| Generates non-consensual intimate imagery or CSAM (reported new prohibition) | |

Confirm the current list in the text and in the Commission guidelines.

## D. Role

| Question | Answer |
|---|---|
| Do we develop it, or have it developed, and place it on the market or put it into service under our name? | Provider if yes |
| Do we use a third party's system under our authority? | Deployer if yes |
| Did we modify it substantially, change its intended purpose to a high-risk one, or put our name on a high-risk system? | Provider if yes (Art. 25) |
| Do we import it from outside the EU, or distribute it? | Importer / distributor |
| Is an authorised representative needed (non-EU provider)? | |

Role decision and reasoning: ______

## E. Risk tier

| Test | Answer |
|---|---|
| Is it a safety component of, or itself, a product under Annex I product law? | If yes: high-risk (date reported as Aug 2028) |
| Does it fall under an Annex III area (biometrics, critical infrastructure, education, employment, essential services including credit and insurance, law enforcement, migration, justice and democratic processes)? | If yes: presumed high-risk (date reported as Dec 2027) |
| Is the Art. 6(3) filter claimed (no material influence on the decision outcome)? | Needs a documented assessment and registration; not available where the system profiles individuals |
| Do transparency duties apply (Art. 50): chatbot, synthetic content, deepfake, emotion recognition, biometric categorisation? | |
| Is a general-purpose model provided? | Use [T12](T12_GPAI_Model_Checklist.md) |
| Otherwise | Minimal |

Final tier: Prohibited / High-risk / Transparency / GPAI / Minimal. Reasoning: ______

## F. GDPR flags

| Question | Answer |
|---|---|
| Personal data in training, input or output? | |
| Special category data? | |
| Solely automated decision with legal or similar effect (Art. 22)? | |
| DPIA required? | |
| FRIA required (deployer category)? | |
| International transfer? | |

## G. Other regimes

Is the organisation a NIS2 entity or a DORA entity? Is the system a CRA product? Does sector product law apply? Notes: ______

## H. Required next steps by tier

| Tier | Minimum |
|---|---|
| Minimal | Inventory entry, literacy, transparency check |
| Transparency | Notices and marking ([T06](T06_Transparency_Notice.md)) |
| High-risk provider | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md) technical file, [T02](T02_Impact_Assessment_FRIA_DPIA.md), [T05](T05_AI_Incident_and_Breach_Reporting_Workflow.md), registration, conformity route |
| High-risk deployer | Use per instructions, oversight, logs, [T02](T02_Impact_Assessment_FRIA_DPIA.md) (with FRIA if applicable), worker information |
| GPAI | [T12](T12_GPAI_Model_Checklist.md) |

## I. Approval

| Role | Name | Decision | Date |
|---|---|---|---|
| Business owner | | | |
| DPO | | | |
| Legal | | | |
| AI governance lead | | | |

## J. Triggers for re-classification

New purpose, new data type, new market, model change, vendor change, or a change in regulation or guidelines.
