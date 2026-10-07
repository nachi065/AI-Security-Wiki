---
title: "South Korea AI Regulatory Hub"
author: Nachiket Sathaye
parent: "South Korea AI Compliance"
nav_order: 1
description: "South Korea's AI Basic Act mapped to AI security controls: generative AI labelling, high-impact and high-performance AI duties, and the domestic representative rule."
document_type: AI Security Wiki Reference
version: 1.0
---

# South Korea AI Regulatory Hub

> **Verification required.** Claims on this page about South Korean law were compiled on 7 October 2026 from secondary web sources and from memory of the law. No primary legal text was read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

This page maps South Korean laws, guidance and standards that bear on AI to the wiki's controls.

## 1. Regional model

There is one horizontal statute, the AI Basic Act, administered by the Ministry of Science and ICT (MSIT). The Personal Information Protection Act applies beside it [Recalled]. The Act has three categories: generative AI, high-impact AI and high-performance AI. The fines are small, and the transparency and domestic representative duties still have to be met [Reported].

## 2. Instrument register

| # | Instrument | Type / status | Key points | Wiki controls | Tag | To verify |
|---|---|---|---|---|---|---|
| KR1 | AI Basic Act | Binding; effective 22 Jan 2026 | Applies to AI developers and to businesses that use AI in products and services; extraterritorial | Whole library | [Reported] | Article numbers; enforcement decree |
| KR2 | Generative AI duties | Binding | Notice that outputs are AI-generated; labelling of generative output; a visible or audible watermark unless the content is clearly fictional (for example animation) | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [Reported] | Format rules |
| KR3 | High-impact AI duties | Binding | Sectors reported: healthcare, energy, transportation, hiring, biometric analysis. Duties: impact assessment on fundamental rights, explainability where feasible, human oversight, user protection plan, documentation | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-041](../11_GCC_AI_Compliance/06_Proposed_Control_Fairness_Bias_Explainability.md) (proposed) | [Conflict] | One source says only Level-4 autonomous vehicles currently trigger it |
| KR4 | High-performance AI (training at 10^26 FLOP or more) | Binding | Lifecycle risk management and user protection | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005) | [Reported] | Notification routes |
| KR5 | Domestic representative | Binding | Required above KRW 1 trillion in revenue, KRW 10 billion in AI service revenue, or 1 million daily users in Korea | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | [Reported] | Thresholds and form |
| KR6 | Fines and grace period | Fines up to about KRW 30 million (about USD 21,000) | One-year grace period; investigations suspended for at least a year, barring severe rights violations | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | [Reported] | Enforcement decree |
| KR7 | Personal Information Protection Act (PIPA) and PIPC guidance | Binding | Personal data duties; AI guidance unverified | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [Recalled] | AI guidance |
| KR8 | AI Basic Act Support Center | Government support | Legal and technical guidance | None | [Reported] | Contact |

## 3. Categories, tiers and roles

| Category / role | What it means |
|---|---|
| Generative AI | Notice and labelling |
| High-impact AI | Impact assessment, oversight, explainability, documentation |
| High-performance AI | Lifecycle risk management for frontier models |
| Foreign provider above the thresholds | Domestic representative |
| Other AI | General duties |

## 4. Timeline

| Date | Event | Tag |
|---|---|---|
| 22 Jan 2026 | AI Basic Act takes effect | [Reported] |
| About Jan 2027 | One-year grace period ends | [Reported] |

## 5. Mapping of common wiki controls

| Wiki control | Regional hook |
|---|---|
| [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) Content safety | Generative AI notice and watermark ([KR-T2](KR-T2_Generative_AI_Labelling_and_Notice.md)) |
| [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) Risk assessment | Impact assessment for high-impact AI ([KR-T1](KR-T1_High_Impact_AI_Determination.md)) |
| [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) Human approval | Human oversight for high-impact AI |
| [AI-CTRL-041](../11_GCC_AI_Compliance/06_Proposed_Control_Fairness_Bias_Explainability.md) Fairness (proposed) | Explainability and rights impact |
| [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) Policy | Domestic representative ([KR-T3](KR-T3_Domestic_Representative_Check.md)) |
| [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) Privacy | PIPA |

## 6. Gaps to close in the wiki

- The rest of the wiki names no Korean instrument.
- No test case covers generative AI labelling.
- The wiki has no step for determining high-impact AI other than [KR-T1](KR-T1_High_Impact_AI_Determination.md).
- The wiki has no domestic representative check other than [KR-T3](KR-T3_Domestic_Representative_Check.md).

## 7. Conflicts and cautions

- The scope of high-impact AI is in conflict. Most sources give a list of sectors; a single source claims that only Level-4 autonomous vehicles qualify now.
- The fine amounts are approximate figures from news and law-firm notes.
- The enforcement decree and the guidelines were not read.

## 8. Verification checklist

- [ ] AI Basic Act text and article numbers
- [ ] Enforcement decree
- [ ] High-impact criteria and current scope
- [ ] Labelling formats
- [ ] Representative thresholds
- [ ] Grace-period terms
- [ ] PIPC AI guidance
- [ ] Add the primary URL and retrieval date beside every confirmed row

## 9. Sources

All sources are secondary unless marked as a regulator or government page. Each fetched page was summarised by a tool and was not read line by line. A source marked "not read" appeared only as a title or snippet in search results, so do not treat it as support for any claim.

| Source | Status | Rows it relates to |
|---|---|---|
| [Cooley: South Korea's AI Basic Act overview](https://www.cooley.com/news/insight/2026/2026-01-27-south-koreas-ai-basic-act-overview-and-key-takeaways) | Fetched and summarised | KR1, KR2, KR3, KR4, KR5 |
| [KoreaTechDesk: AI Basic Act enforcement and startups](https://www.koreatechdesk.com/korea-ai-basic-act-enforcement-startups-governance) | Fetched and summarised | KR3 (the single-source claim), KR6, KR8 |
| [Presencis: AI Basic Act timeline](https://cdn.presencis.com/regulations/kor-ai-basic/timeline/) | Not read | Timeline cross-check |
| [trade.gov: South Korea AI Basic Act](https://www.trade.gov/market-intelligence/south-korea-ai-basic-act) | Not read (government page) | Read it before relying on the thresholds |
| [eWeek: Foreign AI firms face 2026 compliance window](https://www.eweek.com/news/ai-compliance-window-apac-south-korea/) | Not read | KR5 cross-check |

No primary legal text (statute, regulation or circular) was read for any row. Confirm each row against the primary source, and add its URL and retrieval date in the [South Korea Regulatory Crosswalk](03_Regulatory_Crosswalk.md).
