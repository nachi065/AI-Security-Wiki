---
title: "Japan AI Regulatory Hub"
author: Nachiket Sathaye
parent: "Japan AI Compliance"
nav_order: 1
description: "Japanese AI-relevant law and guidance mapped to AI security controls: the AI Promotion Act, AI Basic Plan, Guidelines for AI Business, APPI and copyright law."
document_type: AI Security Wiki Reference
version: 1.0
---

# Japan AI Regulatory Hub

> **Verification required.** Claims on this page about Japanese law were compiled on 7 October 2026 from secondary web sources and from memory of the law. No primary legal text was read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

This page maps Japanese laws, guidance and standards that bear on AI to the wiki's controls.

## 1. Regional model

Japan puts soft law first. Obligations on private firms come mainly from existing laws (privacy, copyright, consumer and sector rules). The AI Promotion Act sets principles and national coordination. The guidelines are voluntary, and they are the reference that buyers use [Reported].

## 2. Instrument register

| # | Instrument | Type / status | Key points | Wiki controls | Tag | To verify |
|---|---|---|---|---|---|---|
| JP1 | AI Promotion Act | Law; 4 Jun 2025 | Basic principles, AI Basic Plan, AI Strategic Headquarters; favours promotion over restriction | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | [Reported] | Any duties on businesses; investigation or publication powers |
| JP2 | AI Basic Plan | Cabinet decision; adopted 14 Jul 2026, replacing the plan of 23 Dec 2025 | National policy priorities; not binding on firms | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | [Reported] | Content |
| JP3 | Guidelines for AI Business (MIC and METI), version 1.2 (31 Mar 2026) | Non-binding | Voluntary risk reduction across the AI lifecycle for developers, providers and users | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-041](../11_GCC_AI_Compliance/06_Proposed_Control_Fairness_Bias_Explainability.md) (proposed) | [Reported] | Official text; the English version is provisional |
| JP4 | Act on the Protection of Personal Information (APPI) | Binding | Personal data use, purpose limits, cross-border rules | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [Recalled] | AI points from the PPC |
| JP5 | Copyright Act Art. 30-4 (information analysis exception) | Binding | Permits certain uses for AI training, with limits | [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029) | [Recalled] | Current interpretation and limits |
| JP6 | Sector rules (financial, medical devices, others) | Binding | Existing rules apply to AI | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | [Unverified] | Per sector |

## 3. Categories, tiers and roles

| Category / role | What it means |
|---|---|
| AI developer | Builds or fine-tunes AI |
| AI provider | Offers AI systems or services |
| AI business user | Uses AI in business |
| Non-business user / third party | Affected persons |
| No statutory tiers | The guidelines work by role and have no risk classes |

## 4. Timeline

| Date | Event | Tag |
|---|---|---|
| 4 Jun 2025 | AI Promotion Act | [Reported] |
| 23 Dec 2025 | First AI Basic Plan | [Reported] |
| 31 Mar 2026 | Guidelines version 1.2 | [Reported] |
| 14 Jul 2026 | Revised AI Basic Plan | [Reported] |

## 5. Mapping of common wiki controls

| Wiki control | Regional hook |
|---|---|
| [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) Policy | Guidelines for AI Business self-assessment ([JP-T1](JP-T1_AI_Guidelines_for_Business_Self_Assessment.md)) |
| [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) Privacy | APPI |
| [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029) Training data | Art. 30-4 analysis ([JP-T2](JP-T2_Training_Data_Copyright_Record.md)) |
| [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) Risk | Guideline risk reduction across the lifecycle |
| [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) Content safety | Guideline safety and transparency points |
| [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) Vendor | Split of responsibility between developer, provider and user |

## 6. Where the wiki covers this

The topics raised on this page are covered by the following controls, test cases and templates.

| Topic | Covered by |
|---|---|
| Responsibility by role (developer, provider, user) | [JP-T1](JP-T1_AI_Guidelines_for_Business_Self_Assessment.md); [TC-L03-020](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-020), [TC-L02-004](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-004) |
| Copyright analysis of training data | [JP-T2](JP-T2_Training_Data_Copyright_Record.md); [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029); [TC-L03-028](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-028) |
| APPI duties | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013); [TC-L03-001](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-001), [TC-L03-012](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-012) |

## 7. Conflicts and cautions

- Naming or investigative powers under the Act are not confirmed.
- The guideline version and the status of its English translation need checking.
- The APPI points on AI were not verified.

## 8. Verification checklist

- [ ] AI Promotion Act text and enforcement provisions
- [ ] AI Basic Plan content
- [ ] Guidelines version 1.2, Japanese text
- [ ] PPC guidance on AI
- [ ] Current limits of Copyright Act Art. 30-4
- [ ] Add the primary URL and retrieval date beside every confirmed row

## 9. Sources

All sources are secondary unless marked as a regulator or government page. Each fetched page was summarised by a tool and was not read line by line. A source marked "not read" appeared only as a title or snippet in search results, so do not treat it as support for any claim.

| Source | Status | Rows it relates to |
|---|---|---|
| [Vorp Labs: Japan AI Promotion Act, Basic Plan and business guidance (Jul 2026)](https://vorplabs.com/ai-regulatory-updates/japan/2026-07/ai-promotion-act-basic-plan-business-guidance) | Fetched and summarised | JP1, JP2, JP3 |
| [Timewell: Japan AI Promotion Act and business guidelines v1.2](https://timewell.jp/en/columns/japan-ai-promotion-act-business-guidelines-v1-2) | Not read | JP3 cross-check |
| [Mondaq: Overview of Japan's AI governance](https://www.mondaq.com/new-technology/1686510/overview-of-japans-ai-governance-what-global-companies-need-to-know) | Not read | JP4, JP5 cross-check |
| [IBA: Japan's emerging framework for responsible AI](https://prod-bo.ibanet.org/japan-emerging-framework-ai-legislation-guidelines) | Not read | Cross-check |

No primary legal text (statute, regulation or circular) was read for any row. Confirm each row against the primary source, and add its URL and retrieval date in the [Japan Regulatory Crosswalk](03_Regulatory_Crosswalk.md).
