---
title: "India AI Regulatory Hub"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "India AI Compliance"
nav_order: 1
description: "Indian AI-relevant law mapped to AI security controls: the DPDP Act and Rules, MeitY AI guidelines, RBI, SEBI and IRDAI expectations, and CERT-In reporting."
document_type: AI Security Wiki Reference
version: 1.0
last_reviewed: 2026-10-20
---

# India AI Regulatory Hub

> **Verification status.** On 16 October 2026 the rows tagged [Verified] (IN1, IN2, IN4, IN5, IN6, IN10), on 20 October 2026 rows IN12, IN3 and IN9, on 25 October 2026 the text of the RBI draft (IN6), and on 27 October 2026 row IN11, were checked against primary documents; the crosswalk gives each source and what was and was not read. Everything else was compiled on 7 October 2026 from secondary sources or memory and is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any claim. This is not legal advice.

This page maps Indian laws, guidance and standards that bear on AI to the wiki's controls.

## 1. Regional model

There are four layers [Recalled]:

1. Data protection law: the DPDP Act 2023 and the DPDP Rules 2025, which are phased.
2. National AI governance guidelines, which are non-binding.
3. Sector regulators for banks, securities and insurance. Most of their output is non-binding guidance; some of it is directive.
4. Cyber incident rules (CERT-In).

Apply the strictest layer that fits. If personal data is involved, the DPDP Act applies whatever the AI label.

## 2. Instrument register

| # | Instrument | Type / status | Key points | Wiki controls | Tag | To verify |
|---|---|---|---|---|---|---|
| IN1 | Digital Personal Data Protection Act 2023 | Binding law (Act 22 of 2023, listed as 11 Aug 2023); being implemented | Notice (s.5), consent (s.6), duties of the data fiduciary including breach intimation (s.8, breach intimation s.8(6)), children's data (s.9), significant data fiduciaries (s.10), cross-border transfer (s.16), Data Protection Board (s.18). Schedule: up to INR 250 crore for failing to take reasonable security safeguards (s.8(5)) and up to INR 200 crore for failing to notify a breach (s.8(6)) | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [Verified] | Whether the penalty applies per contravention; wording of each section |
| IN2 | DPDP Rules 2025 | Notified as G.S.R. 846(E) dated 13 Nov 2025; phased | Rules 1, 2 and 17 to 21 in force on publication; Rule 4 (consent managers) one year after publication, about 13 Nov 2026; Rules 3, 5 to 16, 22 and 23 eighteen months after publication, about 13 May 2027. PIB announced the Rules on 14 Nov 2025. Reports that the phase-in may be shortened were not confirmed | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [Verified] | Breach intimation time limit in Rule 7 (English text not read); any shortening of the phase-in |
| IN3 | Data Protection Board of India | Established in law; Chairperson and four Member posts advertised on 6 May 2026; no appointment stated in Parliament on 12 Aug 2026 | Applications invited by MeitY notice of 6 May 2026 (one Chairperson, four Members); advertised in Employment News on 6 Jun 2026; no appointment reported; complaint mechanism unavailable | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [Verified] from the [MeitY notice](https://www.meity.gov.in/static/uploads/2026/05/cd481c027470b420b4cb85fb40a91c53.pdf) and the [Lok Sabha answer of 12 Aug 2026](https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AU3960_GyWSTk.pdf), read 20 Oct 2026 | Whether any appointment has been made since 12 Aug 2026 (one secondary source says appointments were made on 6 Jun 2026; the primary sources read do not support this) |
| IN4 | India AI Governance Guidelines (MeitY) | Non-binding; the document is undated; release reported as 5 Nov 2025 | Seven sutras: Trust is the Foundation; People First; Accountability; Fairness and Equity; Innovation over Restraint; Understandable by Design; Safety, Resilience and Sustainability. Six pillars: Infrastructure, Capacity Building, Policy and Regulation, Risk Mitigation, Accountability, Institutions. Proposes an AI Governance Group and a Technology and Policy Expert Committee; describes the AI Safety Institute as established. States that a separate AI law is not needed at this stage | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [Verified] | Release date (the document itself is undated) |
| IN5 | RBI FREE-AI Committee report | Committee report published by the RBI on 13 Aug 2025; not a binding direction | Seven sutras and 26 recommendations under six pillars (infrastructure, policy, capacity, governance, protection, assurance) | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [Verified] | The text of each recommendation; whether the RBI has adopted any of them as directions |
| IN6 | RBI draft Guidance on Model Risk Management | Draft issued 24 Jun 2026; comments to 24 Jul 2026 | Draft Guidance on Regulatory Principles for Model Risk Management. Applies to banks, NBFCs, asset reconstruction companies, credit information companies and other listed regulated entity types, and to all models they use including third-party models and models using AI or machine learning. The board oversees the model risk framework and approves model risk tiering (para 11). For AI models, the draft expects robust human oversight, including "override, suspension, or deactivation mechanisms, including kill-switch arrangements" (para 60(ii)), fallback mechanisms such as manual intervention (para 43), and an option for customers to switch to human assistance (para 59(iii)). No effective date is given | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025), [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045) | [Verified] | Final status: still a draft when read on 25 Oct 2026 |
| IN7 | SEBI regulations on AI and ML tools used by regulated entities | Amendments to the Intermediaries Regulations 2008 and the Securities Contracts (Regulation) (Stock Exchanges and Clearing Corporations) Regulations 2018; reported as notified 6 Feb 2025 | Regulated entities are solely responsible for the privacy, security and integrity of data, for the output of the AI and ML tools they use, and for legal compliance. The primary document read was the SEBI Board memorandum of Dec 2024, which proposed this; the notification itself was not read | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [Reported] | SEBI's notified text and gazette date; any later SEBI AI guidance |
| IN8 | IRDAI: AI-cybersecurity readiness directive (May 2026); AI working group (Jun 2026) | Not confirmed | A document titled IRDAI Information and Cybersecurity Guidelines, 2026 is listed on the IRDAI site. It could not be read, so whether an AI-specific directive of May 2026 exists is not confirmed | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | [Unverified] | Whether any IRDAI instrument addresses AI, and its text |
| IN9 | IT Rules amendments on synthetic content labelling | Notified as G.S.R. 120(E) dated 10 Feb 2026 (amending the IT Rules 2021); in force from 20 Feb 2026 (reported) | Intermediaries that offer tools to create synthetic content must label it prominently and embed provenance metadata with a unique identifier (Rule 3(3)); significant social media intermediaries must obtain and check user declarations (Rule 4(1A)); takedown deadlines are shorter, for example 3 hours after a court order or an authorised officer's intimation (Rule 3(1)(d)) | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [Verified] G.S.R. number, date and rule numbers, from [MeitY's consolidated text](https://www.meity.gov.in/static/uploads/2026/02/550681ab908f8afb135b0ad42816a1c9.pdf), read 20 Oct 2026; the commencement date was not shown | Commencement date (not shown in the text read); the Gazette copy itself |
| IN10 | CERT-In incident reporting directions (2022) and AI guidance | Binding directions of 28 Apr 2022 (No. 20(3)/2022-CERT-In) under section 70B(6) of the IT Act | Listed cyber incidents must be reported to CERT-In within 6 hours; the directions took effect 60 days after issue; the list of reportable incidents includes attacks or suspicious activity related to AI and ML systems. On 10 Jun 2026 CERT-In issued Guidelines regarding AI-Accelerated Vulnerability Protection and Response Requirements for OEMs and Technology Providers (V1.0); they describe themselves as compliance guidelines / recommendations and use advisory wording | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035), [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005) | [Verified]; the [10 Jun 2026 AI-accelerated vulnerability guidelines](https://www.cert-in.org.in/PDF/OEM_and_Technology_Providers_Guidelines.pdf) read 27 Oct 2026 | Legal status of the 10 Jun 2026 guidelines (advisory wording; they cite the 2022 directions for 6-hour reporting); other CERT-In AI advisories |
| IN11 | IT Act 2000 and SPDI Rules | Binding law; DPDP Act s.44(2) omits IT Act s.43A and s.87(2)(ob), commencing 18 months after G.S.R. 843(E) of 13 Nov 2025 (about 13 May 2027); the rest of the IT Act continues | Reasonable security practices for sensitive data | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | [Verified] s.44(2) and its commencement, from the [DPDP Act](https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf) and [G.S.R. 843(E)](https://www.meity.gov.in/static/uploads/2025/11/c56ceae6c383460ca69577428d36828b.pdf), read 27 Oct 2026 | Whether the SPDI Rules 2011 lapse when s.43A is omitted (an inference; not stated in the texts read); any change to the 18-month phase-in |
| IN12 | IndiaAI Mission | Programme (Mar 2024; INR 10,372 crore) | Compute, datasets, skilling. Listed for context; it creates no obligation | None | [Verified] date and outlay, from the [PIB release of 7 Mar 2024](https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2012355) (Rs 10,371.92 crore), read 20 Oct 2026 | n/a |
| IN13 | SEBI guidelines on responsible use of AI and ML in securities markets | Proposed. Consultation paper of 20 Jun 2025 ([SEBI listing](https://www.sebi.gov.in/reports-and-statistics/reports/jun-2025/consultation-paper-on-guidelines-for-responsible-usage-of-ai-ml-in-indian-securities-markets_94687.html), read 27 Oct 2026) [Verified]; on 10 Oct 2026 the SEBI chairman said the guidelines would be issued shortly [Reported] | The consultation paper reportedly proposed principles of accountability, transparency, safety and reliability, model governance, records of development, testing and monitoring, and disclosure of AI and ML use. The chairman's remarks of 10 Oct 2026 describe a tiered approach built on clear accountability, data controls, kill switches and human oversight, aligned with the IOSCO supervisory toolkit for AI. Nothing has been issued, so none of this binds yet, and whether a kill switch will be mandatory for every firm is not known | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025), [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | [Reported] | The consultation paper text; the final guidelines when issued |

## 3. Categories, tiers and roles

| Category / role | What it means |
|---|---|
| Data fiduciary | Decides the purposes and means of processing; the main duty holder |
| Data processor | Processes on behalf of a fiduciary; contractual duties |
| Significant data fiduciary | Designated by the government; extra duties such as audits and impact assessment [Recalled] |
| Regulated entity (RBI, SEBI, IRDAI) | Sector AI and model-risk expectations |
| Intermediary / platform | Content rules, including synthetic labelling if notified |

## 4. Timeline

| Date | Event | Tag |
|---|---|---|
| 28 Apr 2022 | CERT-In directions (6-hour reporting) | [Verified] |
| 6 Feb 2025 | SEBI amendments on AI and ML tools (as reported) | [Reported] |
| 20 Jun 2025 | SEBI consultation paper on responsible use of AI and ML | [Verified] |
| 13 Aug 2025 | RBI FREE-AI report | [Verified] |
| 5 Nov 2025 | MeitY AI Governance Guidelines released (date reported; the document is undated) | [Reported] |
| 13 Nov 2025 | DPDP Rules notified (G.S.R. 846(E); PIB announcement 14 Nov) | [Verified] |
| 10 Feb 2026 | IT Rules amendment on synthetic content notified (G.S.R. 120(E)); in force 20 Feb 2026 (as reported) | [Verified] notification; commencement [Reported] |
| May 2026 | IRDAI AI-cybersecurity readiness directive | [Unverified] |
| 24 Jun 2026 | RBI draft Model Risk Management guidance, including kill-switch arrangements for AI models | [Verified] |
| 10 Oct 2026 | SEBI chairman says AI and ML guidelines, including kill switches and human oversight, will be issued shortly | [Reported] |
| About 13 Nov 2026 | Consent manager rule (Rule 4) in force, one year after publication | [Verified] |
| About 13 May 2027 | Core DPDP obligations (Rules 3, 5 to 16, 22, 23), eighteen months after publication; on the same schedule DPDP Act s.44(2) omits IT Act s.43A (G.S.R. 843(E)) | [Verified] |

## 5. Mapping of common wiki controls

| Wiki control | Regional hook |
|---|---|
| [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) Privacy and regulatory | DPDP Act and Rules; notice and consent record ([IN-T1](IN-T1_DPDP_AI_Processing_Record_and_Notice.md)) |
| [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007) Data sovereignty | DPDP cross-border provisions; sector localisation rules [Unverified] |
| [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) Inventory and tiering | RBI FREE-AI; RBI model risk draft |
| [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) Vendor | RBI and SEBI outsourcing expectations; fiduciary-processor contract |
| [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) Human approval | MeitY accountability and human centricity; RBI recommendations |
| [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) Incident response | DPDP breach duties; CERT-In reporting ([IN-T2](IN-T2_Breach_and_Incident_Workflow.md)) |
| [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) Content safety | Synthetic labelling rules, if notified |
| [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) Fairness | MeitY fairness principle; RBI FREE-AI |

## 6. Where the wiki covers this

The topics raised on this page are covered by the following controls, test cases and templates.

| Topic | Covered by |
|---|---|
| DPDP Act and Rules mapped to controls | Section 5 above and the [India Regulatory Crosswalk](03_Regulatory_Crosswalk.md); the [Framework Adoption Guide](../10_Test_Case_Library/framework-adoption-guide.md) has an India DPDP column |
| Consent artefacts and withdrawal | [IN-T1](IN-T1_DPDP_AI_Processing_Record_and_Notice.md); [TC-L03-004](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-004) |
| Reporting to CERT-In and the Data Protection Board | [IN-T2](IN-T2_Breach_and_Incident_Workflow.md); [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035); [TC-L03-019](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-019) |
| RBI, SEBI and IRDAI expectations | [IN-T3](IN-T3_Regulated_Entity_AI_Readiness.md); [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041); [TC-L03-031](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-031); [Sector Overlays](../04_Domain_Standards/10B_Sector_Overlays.md) |
| Synthetic-content labelling | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039); [TC-L03-003](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-003); labelling record [CN-T2](../16_China_AI_Compliance/CN-T2_Content_Labelling_Implementation_Record.md); [TC-L03-035](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-035) |

## 7. Conflicts and cautions

- Sources differ on the DPDP Rules dates: 13 or 14 November 2025, and 13 or 14 May 2027.
- The government may shorten the phase-in. Check before planning.
- The synthetic content labelling rules are described both as proposed and as amended. MeitY's consolidated text (read 20 October 2026) shows them in the IT Rules as amended by G.S.R. 120(E) of 10 February 2026. A separate draft Second Amendment Rules 2026 (March 2026) on MeitY's site does not touch synthetic content.
- One source says the Board was not operational as of August 2026, so the enforcement route is uncertain. The Lok Sabha answer of 12 August 2026 (read 20 October 2026) names no appointment. Another secondary source says appointments were made on 6 June 2026; no primary source seen supports that.
- The penalty and section detail comes from a single vendor blog.

## 8. Verification checklist

- [ ] DPDP Act section numbers for notice, consent, breach, children, significant data fiduciary and cross-border transfer
- [ ] Rules phase dates and any change
- [ ] Board constitution
- [ ] MeitY guidelines text and institutions
- [ ] The 26 RBI FREE-AI recommendations
- [ ] RBI model risk guidance, final version
- [ ] List of SEBI circulars
- [ ] SEBI AI and ML guidelines (IN13), once issued
- [ ] IRDAI directive
- [ ] Status of the IT Rules on synthetic content
- [ ] CERT-In directions text
- [ ] Add the primary URL and retrieval date beside every confirmed row

## 9. Sources

All sources are secondary unless marked as a regulator or government page. Each fetched page was summarised by a tool and was not read line by line. A source marked "not read" appeared only as a title or snippet in search results, so do not treat it as support for any claim.

| Source | Status | Rows it relates to |
|---|---|---|
| [IAPP: India releases DPDPA rules, AI governance guidelines](https://iapp.org/news/a/notes-from-the-asia-pacific-region-india-releases-dpdpa-rules-ai-governance-guidelines) | Fetched and summarised | IN2, IN4 (Rules timing, MeitY guidelines, seven principles) |
| [AIRiskAware: India AI governance, DPDP, RBI, SEBI (2026)](https://airiskaware.com/insights/india-ai-governance-dpdp-2026) | Fetched and summarised (vendor blog; treat as secondary) | IN1, IN3, IN5, IN6, IN7, IN8, IN12 |
| [Global Law Experts: AI governance India 2026](https://globallawexperts.com/ai-governance-india/) | Fetched and summarised (the fetch returned metadata only) | IN2 phase dates; IN9, that the rules exist |
| [Lexology: India AI governance model and copyright](https://www.lexology.com/library/detail.aspx?g=ffc0c58c-3727-4472-9914-5fa6a33ffffd) | Not read | Further reading |
| [India AI Rulebook: guidelines and 7 sutras](https://indiaairulebook.com/learn/ai-policy/india-ai-governance-guidelines-2025) | Not read | IN4 cross-check |
| [TechJack Solutions: DPDPA and AI](https://techjacksolutions.com/ai-governance-india/dpdpa-ai/) | Not read | IN1, IN2 cross-check |

No primary legal text (statute, regulation or circular) was read for any row. Confirm each row against the primary source, and add its URL and retrieval date in the [India Regulatory Crosswalk](03_Regulatory_Crosswalk.md).
