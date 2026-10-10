---
title: "SG-T2 AI Inventory and Risk Materiality Assessment (Financial Institutions)"
author: Nachiket Sathaye
parent: "Singapore AI Compliance"
nav_order: 5
description: "AI inventory record and risk materiality assessment for financial institutions, following the MAS Guidelines on Artificial Intelligence Risk Management of 7 October 2026."
document_type: AI Security Wiki Reference
version: 1.1
---

# SG-T2 AI Inventory and Risk Materiality Assessment (Financial Institutions)

> **Verification required.** This is a working template, not a regulator-approved form. Paragraph numbers refer to the MAS Guidelines on Artificial Intelligence Risk Management of 7 October 2026, read on 10 October 2026. The scoring scale and the controls by rating are this wiki's suggestion and are not set by MAS. This is not legal advice.

<!-- -->

> **How to use:** This is a blank form. Copy it and fill in the empty cells and blanks for your system. To copy it, follow the "Suggest an edit to this page" link in the footer to reach its Markdown source.

Wiki controls: [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037). The paragraph-by-paragraph mapping of the Guidelines to wiki controls is in the [Singapore Regulatory Crosswalk](03_Regulatory_Crosswalk.md#mas-guidelines-on-ai-risk-management-paragraph-crosswalk).

## Step 1. Does the basic governance route apply?

Paragraph 2.3 lets an institution apply basic governance policies and procedures where poor performance or unavailability of the AI is unlikely to have a material adverse impact on the institution, its customers or other stakeholders. Paragraph 2.4 gives examples such as drafting emails or summarising documents for internal reference, with a person checking the output.

| Question | Answer |
|---|---|
| Could poor performance or unavailability have a material financial, operational, regulatory, legal or reputational impact on the institution? | |
| Could it have a material impact on customers or other stakeholders, including fairness, ethical conduct and consumer protection? | |
| Does a person review the output before it is used? | |
| Route chosen: basic governance (paragraph 2.5) or full assessment (the rest of this form) | |
| Date of the next review of this answer (paragraph 2.5(f)) | |

## Step 2. Inventory record

The attributes follow paragraph 4.7. Record the differences your policy allows between use cases, systems and models.

| Attribute | Entry |
|---|---|
| Use case, system or model ID | |
| Purpose and description | |
| Approved scope of use, including jurisdiction | |
| Model type | |
| Data used | |
| Dependencies, including other AI systems and models | |
| Life cycle status | |
| Assigned risk materiality rating | |
| Model review status | |
| Owner, developers and other key roles | |
| Links to essential documentation | |
| Third-party AI: provider, service and contract reference | |
| Links to other inventories (data assets, third-party or outsourcing register) | |

For an AI agent, add the attributes that paragraph 4.8 and its footnote suggest:

| Agent attribute | Entry |
|---|---|
| Agent identifier | |
| Tools and systems the agent can access | |
| Components | |
| Guardrails imposed | |

## Step 3. Risk materiality assessment

Paragraph 4.12 names three dimensions as the minimum. Score each from 1 to 3 using your own rubric, once before controls (inherent) and once after (residual), as paragraph 4.11 asks.

| Dimension | What to consider | Inherent | Residual | Reason |
|---|---|---|---|---|
| Impact | Consequences of failure, malfunction or poor performance for the institution (financial, operational, regulatory, reputational) and for customers and other stakeholders (fairness, ethics, consumer protection); the nature and sensitivity of the data processed | | | |
| Complexity | The AI technology used, how novel the application is, the data it uses and how explainable its outputs are; for third-party AI, how much visibility you have | | | |
| Reliance | How far the decision or output depends on the AI, the autonomy granted to it and the degree of human involvement or oversight | | | |

| Result | Entry |
|---|---|
| Inherent risk materiality: Low / Medium / High | |
| Residual risk materiality: Low / Medium / High | |
| Is the residual rating within risk appetite? (paragraph 4.11) | |
| Control function that approved the rating (paragraph 4.13) | |
| Date of the next review | |

## Step 4. Controls by rating

The Guidelines ask for controls in proportion to risk materiality and name specific expectations for high-risk use cases. The Low and Medium rows are this wiki's suggestion.

| Rating | Minimum controls |
|---|---|
| Low | Inventory record; data management, safety and cybersecurity controls applied in proportion (footnote 12) |
| Medium | Evaluation and testing against set thresholds; documented review by qualified people not involved in development (paragraph 5.20); monitoring; human oversight where outputs affect customers |
| High | Contingency plan with tested fallback (paragraph 5.3); formal independent validation before deployment (paragraph 5.19); regular re-validation by independent parties (paragraph 5.24); fairness assessment and higher transparency where customer outcomes are affected (paragraphs 5.6 to 5.8); a kill switch or override considered (paragraph 5.23(b)) |

## Step 5. Life cycle checklist

Tick each area that applies and record where the evidence is held. Section 5 of the Guidelines is to be met by 7 October 2028.

| Area | Paragraphs | Applies? | Evidence |
|---|---|---|---|
| Data management | 5.4 | | |
| Transparency and explainability | 5.5 to 5.6 | | |
| Fairness | 5.7 to 5.8 | | |
| Human oversight | 5.9 | | |
| Third-party AI management | 5.10 to 5.11 | | |
| Selection | 5.12 to 5.13 | | |
| Evaluation and testing | 5.14 to 5.15 | | |
| Technology and cybersecurity | 5.16 | | |
| Reproducibility and auditability | 5.17 | | |
| Pre-deployment review | 5.18 to 5.22 | | |
| Monitoring, incidents and re-validation | 5.23 to 5.24 | | |
| Change management and retirement | 5.25 to 5.26 | | |

Owner: ______ Date: ______ Review: ______
