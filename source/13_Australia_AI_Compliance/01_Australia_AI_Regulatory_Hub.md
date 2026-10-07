---
title: "Australia AI Regulatory Hub"
author: Nachiket Sathaye
parent: "Australia AI Compliance"
nav_order: 1
description: "Australian AI-relevant laws, reforms and guidance, including Privacy Act automated-decision transparency, mapped to AI security controls."
document_type: AI Security Wiki Reference
version: 1.0
---

# Australia AI Regulatory Hub

> **Verification required.** Claims on this page about Australian law were compiled on 7 October 2026 from secondary web sources and from memory of the law. No primary legal text was read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

This page maps Australian laws, guidance and standards that bear on AI to the wiki's controls.

## 1. Regional model

Duties arrive through four layers [Reported]:

1. The Privacy Act and the Australian Privacy Principles (APPs).
2. The Australian Consumer Law and other existing statutes.
3. Targeted AI-related reforms, such as deepfake offences and workplace safety in New South Wales.
4. Voluntary guidance from the National AI Centre, and an AI Safety Institute.

APRA prudential standards also apply to regulated financial entities [Recalled].

## 2. Instrument register

| # | Instrument | Type / status | Key points | Wiki controls | Tag | To verify |
|---|---|---|---|---|---|---|
| AU1 | National AI Plan (Dec 2025) | Policy | Infrastructure, adoption and skills; proportionate risk management through existing law | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | [Reported] | Text |
| AU2 | Privacy Act automated decision transparency (APP 1.7 to 1.9) | Binding; commences 10 Dec 2026 (OAIC statement, Allens) | The privacy policy must state three things: the kinds of personal information used in the computer programs; the kinds of decisions made solely by them; and the kinds of decisions where a program does something substantially and directly related to making the decision. The duty applies where the decision could reasonably be expected to significantly affect an individual's rights or interests and personal information is used. APP 1.9 lists examples, such as statutory benefits, contractual rights and access to significant services. The scope is broad and can cover simple rule-based tools. The OAIC published two fact sheets and a flowchart after receiving 90 submissions | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-041](../11_GCC_AI_Compliance/06_Proposed_Control_Fairness_Bias_Explainability.md) (proposed) | [Reported] | Confirmed by the OAIC and a law-firm note; read the Act text and the APP 1 guidelines for the exact wording |
| AU3 | OAIC privacy policy compliance sweep | Regulator action; began in the first week of Jan 2026 | About 60 entities across six sectors (real estate and rental agencies, pharmacies, licensed venues, car rental, car dealerships, pawnbrokers and second-hand dealers), chosen by size, location and risk profile. The sweep covers general privacy policy compliance. It was not aimed at AI, and the six sectors are not "high-risk AI sectors" | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [Reported] | OAIC outcomes; any AI-specific sweeps |
| AU3a | Privacy Act civil penalty tiers | Binding | Serious or repeated interference: the greater of AUD 50 million, three times the benefit obtained, or 30% of adjusted turnover (Spruson, on the 2022 amendment). A law-firm summary of the 2024 tiers gives a low tier of up to AUD 330,000 for corporations (AUD 66,000 for others) for policy or notification failures; infringement notices of up to AUD 66,000 for corporations and AUD 19,800 for others; and a mid tier of up to AUD 3.3 million for corporations and AUD 660,000 for others | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [Reported] | Confirm the tiers in the Act; which tier an APP 1.7 to 1.9 breach falls in is not confirmed |
| AU4 | Guidance for AI Adoption (National AI Centre) | Voluntary | Accountability, risk management, transparency, human control | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | [Reported] | Practices list |
| AU5 | AI Safety Institute (early 2026; AUD 29.9M) | Government body | Oversight frameworks for high-risk AI | None | [Reported] | Remit |
| AU6 | Deepfake criminal offences (forthcoming); NSW workplace AI safety bill; Victoria considering a similar measure | Proposed | Non-consensual intimate imagery; surveillance and discrimination in workplaces | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-041](../11_GCC_AI_Compliance/06_Proposed_Control_Fairness_Bias_Explainability.md) (proposed) | [Reported] | Status |
| AU7 | Australian Consumer Law | Binding | Misleading claims; consumer guarantees for AI-enabled products | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | [Reported] | Guidance |
| AU8 | APRA CPS 230 and CPS 234 | Binding for regulated entities | Operational risk and information security | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [Recalled] | Applicability to AI |

## 3. Categories, tiers and roles

| Category / role | What it means |
|---|---|
| APP entity | Covered by the Privacy Act |
| Deployer of automated decision-making (ADM) with significant effect | Transparency duty from Dec 2026 |
| Regulated financial entity | APRA standards |
| No statutory AI tiers | Use your own tiering |

## 4. Timeline

| Date | Event | Tag |
|---|---|---|
| Dec 2025 | National AI Plan | [Reported] |
| Early 2026 | AI Safety Institute | [Reported] |
| 10 Dec 2026 | ADM transparency applies | [Reported] |

## 5. Mapping of common wiki controls

| Wiki control | Regional hook |
|---|---|
| [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) Privacy | ADM transparency statement ([AU-T1](AU-T1_ADM_Transparency_Register.md)) |
| [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) Content safety | Deepfake rules |
| [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) Risk | Guidance for AI Adoption |
| [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) Vendor | APRA CPS 230 |
| [AI-CTRL-041](../11_GCC_AI_Compliance/06_Proposed_Control_Fairness_Bias_Explainability.md) Fairness (proposed) | Discrimination law and OAIC expectations |

## 6. Where the wiki covers this

The topics raised on this page are covered by the following controls, test cases and templates.

| Topic | Covered by |
|---|---|
| Automated decision transparency (APP 1.7 to 1.9) | [AU-T1](AU-T1_ADM_Transparency_Register.md); [TC-L01-011](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-011) identifies automated decisions; [TC-L03-003](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-003) tests notice and transparency |
| Explanation and human review of decisions | [TC-L03-008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008), [TC-L03-029](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-029) |
| Deepfakes and synthetic content | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039); the labelling record [CN-T2](../16_China_AI_Compliance/CN-T2_Content_Labelling_Implementation_Record.md) and the provenance checklist [US-T3](../22_US_AI_Compliance/US-T3_GenAI_Provenance_and_Transparency_Checklist.md) can be reused |
| APRA CPS 230 and CPS 234 | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035); [TC-L03-021](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-021); supplier addendum [GCC T03](../11_GCC_AI_Compliance/T03_Vendor_Due_Diligence_GCC_Addendum.md) or [EU T03](../12_EU_AI_Compliance/T03_Supplier_Due_Diligence_EU_Addendum.md) |
| Guidance for AI Adoption | [AU-T2](AU-T2_AI_Adoption_Self_Assessment.md); [TC-L02-001](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-001) |

## 7. Conflicts and cautions

- Three points were checked on 7 October 2026 against the OAIC page and law-firm notes. The 10 December 2026 commencement is confirmed by both. The 60-entity OAIC sweep took place, as a general privacy policy sweep of six sectors unrelated to AI. The ceiling of AUD 50 million, three times the benefit or 30% of turnover is the penalty for serious interference. It is not a penalty specific to APP 1.7 to 1.9.
- "AUD 66,000" appears in sources both as a low-tier figure for non-corporations and as an infringement notice maximum for corporations. Use the tier figures in row AU3a and read the Act.
- The tier that an APP 1.7 to 1.9 breach would fall in is not confirmed.
- The NSW and Victorian proposals may have changed.

## 8. Verification checklist

- [ ] Privacy Act amendment text and commencement (APP 1.7 to 1.9)
- [ ] Which civil penalty tier applies to APP 1 breaches
- [ ] OAIC fact sheets and flowchart
- [ ] Guidance for AI Adoption text
- [ ] Deepfake legislation status
- [ ] APRA position on AI
- [ ] Add the primary URL and retrieval date beside every confirmed row

## 9. Sources

All sources are secondary unless marked as a regulator page. Each fetched page was summarised by a tool and was not read line by line.

| Source | Status | What it supports |
|---|---|---|
| [OAIC: New resources on transparency for AI and automated decision-making](https://www.oaic.gov.au/news/media-centre/new-resources-on-transparency-for-use-of-ai-and-automated-decision-making) | Fetched and summarised (regulator page) | AU2 |
| [Allens: ADM transparency, APP 1 amendments (Jun 2026)](https://www.allens.com.au/insights-news/insights/2026/06/automated-decision-making-transparency-what-app-entities-need-to-know-about-the-app-1-amendments/) | Fetched and summarised | AU2 |
| [Clifford Chance: OAIC enforcement priorities in 2026](https://www.cliffordchance.com/insights/resources/blogs/regulatory-investigations-financial-crime-insights/2026/01/spotlight-on-data-protection-regulatory-risks-in-australia-oaics-enforcement-priorities-and-activities-in-2026.html) | Fetched and summarised | AU3, AU3a tiers |
| [Australian Security Magazine: OAIC privacy compliance sweep](https://australiansecuritymagazine.com.au/oaic-privacy-compliance-sweep/) | Fetched and summarised | AU3 (about 60 entities, six sectors) |
| [Spruson: privacy breach penalties passed into law (Nov 2022)](https://www.spruson.com/substantial-increases-to-australian-privacy-breach-penalties-passed-into-law/) | Fetched and summarised | AU3a maximum penalty |
| [Mondaq: TMT trends 2026, Australia](https://www.mondaq.com/australia/consumer-credit/1741662/tmt-trends-2026-digital-infrastructure-and-emerging-technology-regulation) | Fetched and summarised | AU1, AU4 to AU7 |
| [Blue Apache: December 2026 AI governance rules](https://www.blueapache.com/blog/seven-things-every-business-must-do-before-december-as-ai-governance-rules-kick-in) | Fetched and summarised (marketing-grade; its penalty and sweep claims were corrected) | AU5 only |
| [FTI Consulting: Australia penalties](https://www.fticonsulting.com/insights/articles/australia-serious-penalties-privacy-enforcement) | Fetch returned an index page; not used | None |

No primary legal text (statute, regulation or circular) was read for any row. Confirm each row against the primary source, and add its URL and retrieval date in the [Australia Regulatory Crosswalk](03_Regulatory_Crosswalk.md).
