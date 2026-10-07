---
title: "EU AI Regulatory Hub"
author: Nachiket Sathaye
parent: "EU AI Compliance"
nav_order: 1
description: "EU AI Act timeline, risk tiers, roles and high-risk obligations, with GDPR, NIS2, DORA, CRA and standards mapped to AI security controls."
document_type: AI Security Wiki Reference
version: 1.0
---

# EU AI Regulatory Hub

> **Verification required.** EU claims on this page were compiled on 7 October 2026 from secondary sources and from memory of the legal text. The Official Journal text was not read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text on EUR-Lex before relying on any of them. This is not legal advice.

This page maps EU laws, guidance and standards that bear on AI to the wiki's controls. In the instrument register, the Wiki coverage column says how far the wiki's current controls and test cases address the instrument. "Not covered" means no wiki page maps to it yet.

## 1. How EU duties stack

| Layer | Instruments | Question it answers |
|---|---|---|
| Horizontal AI law | AI Act (Regulation (EU) 2024/1689), as amended by the Digital Omnibus on AI [Reported] | Is it prohibited, high-risk, transparency-only or minimal? Which role are we in? |
| Data protection | GDPR, ePrivacy, EDPB guidance | Lawful basis, rights, DPIA, transfers, automated decisions |
| Security and resilience | NIS2, DORA (finance), Cyber Resilience Act (products with digital elements) | Cyber risk management and reporting |
| Product and liability | Sector product law (medical devices, machinery and others), Product Liability Directive | Conformity and compensation |
| Data and platform law | Data Act, Digital Services Act | Data access, platform duties |
| Standards | CEN-CENELEC JTC 21 standards; ISO/IEC 42001; NIST AI RMF as a bridge | How to show conformity |

An AI system can fall inside several layers at once. For each topic, apply the strictest duty that applies.

## 2. AI Act timeline

Verify every date against the Official Journal.

| Date | What | Status |
|---|---|---|
| 1 Aug 2024 | Entry into force | [Recalled] |
| 2 Feb 2025 | Prohibited practices (Art. 5) and AI literacy (Art. 4) apply | [Reported] |
| 2 Aug 2025 | General-purpose AI (GPAI) obligations apply (Arts. 51 to 55); penalties regime due from Member States | [Reported] |
| 2 Aug 2026 | Commission and AI Office enforcement powers over GPAI; national market surveillance enforcement; transparency (Art. 50) application | [Reported] |
| 2 Dec 2026 | Art. 50(2) marking grace ends for generative systems already on the market before 2 Aug 2026; new prohibition on generating non-consensual intimate imagery and CSAM | [Reported]; [Conflict] on exact scope, see 2.2 |
| 2 Aug 2027 | Grace period ends for GPAI models placed on the market before 2 Aug 2025 | [Reported] |
| 2 Dec 2027 | High-risk AI, Annex III use cases (previously 2 Aug 2026) | [Reported] |
| 2 Aug 2028 | High-risk AI embedded in Annex I regulated products (previously 2 Aug 2027) | [Reported] |

### 2.1 Omnibus status: sources conflict

- One firm reports a provisional agreement that awaits formal adoption.
- Another reports Parliament approval on 16 June 2026 (423 votes to 57, with 174 abstentions), Council adoption on 29 June, signature on 8 July and entry into force on 27 July 2026, as Regulation (EU) 2026/1744.
- A third says publication was "expected July 2026".

The later reports are more likely to be correct, but treat the status as [Conflict] until you have seen the Official Journal entry. Confirm the regulation number and whether the changes below are in force. The wiki's [Governance, Standards and Regulation](../00_Foundations/09-Governance-Standards-and-Regulation.md) page reports the same regulation number and the same high-risk dates, also from secondary sources.

### 2.2 Reported omnibus changes

| Change | Detail | Tag |
|---|---|---|
| High-risk delay | Annex III to 2 Dec 2027; Annex I to 2 Aug 2028 | [Reported] |
| Art. 50(2) marking | Grace to 2 Dec 2026 for systems already on the market; systems placed after 2 Aug 2026 comply on placement. One source says all transparency duties stay at 2 Aug 2026, another says the watermarking deadline moved | [Conflict] |
| New prohibition | Systems generating non-consensual intimate imagery or CSAM, with a safe harbour where effective safeguards exist; from 2 Dec 2026 | [Reported] |
| AI literacy (Art. 4) | Date reportedly unchanged (2 Feb 2025). Whether the obligation was softened is not confirmed | [Unverified] |
| Special category data for bias detection | "Strictly necessary" standard retained | [Reported] |
| Registration | Systems self-assessed as non-high-risk under Art. 6(3) still need EU database registration | [Reported] |
| SME relief | Extended to small mid-caps | [Reported] |
| Machinery and Annex I | Machinery reported as fully exempt; other sectors conditional, pending 2027 implementing acts | [Reported], single source |

## 3. AI Act core concepts

### 3.1 Risk tiers

Tagged [Recalled] unless noted.

| Tier | What | Main duties | Wiki controls and templates |
|---|---|---|---|
| Prohibited (Art. 5) | Manipulation, exploitation of vulnerabilities, social scoring, certain biometric and emotion-recognition uses, and others | Do not place on the market or use | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) |
| High-risk (Art. 6, Annex I and III) | Annex III areas: biometrics, critical infrastructure, education, employment, essential services (including credit and insurance), law enforcement, migration, justice and democratic processes [Reported list] | Risk management, data governance, technical documentation, logging, transparency, human oversight, accuracy, robustness, cybersecurity, QMS, conformity assessment, CE marking, registration, post-market monitoring | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) |
| Limited / transparency (Art. 50) | Chatbots, synthetic content, deepfakes, emotion recognition or biometric categorisation | Disclose AI interaction, mark synthetic output, label deepfakes | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [T06](T06_Transparency_Notice.md) |
| Minimal | Everything else | Voluntary codes | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) |
| GPAI models (Arts. 51 to 55) | Foundation and general-purpose models | Documentation, copyright policy, training-content summary; more for systemic-risk models | [T12](T12_GPAI_Model_Checklist.md) |

### 3.2 Roles

The roles are provider, deployer, importer, distributor, authorised representative and product manufacturer [Recalled]. A deployer or distributor can become a provider by putting its name on a high-risk system, making a substantial modification, or changing the intended purpose to a high-risk one (Art. 25). The role decides the duties, so classify first with [T01](T01_AI_System_Classification.md).

### 3.3 Obligation map for high-risk systems

Article numbers are [Recalled].

| Article | Topic | Applies to | Wiki control | Template |
|---|---|---|---|---|
| 9 | Risk management system | Provider | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | [T01](T01_AI_System_Classification.md), [T02](T02_Impact_Assessment_FRIA_DPIA.md) |
| 10 | Data and data governance (including bias examination) | Provider | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-041](../11_GCC_AI_Compliance/06_Proposed_Control_Fairness_Bias_Explainability.md) (proposed) | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md) |
| 11 and Annex IV | Technical documentation | Provider | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md) |
| 12 | Record-keeping and logs | Provider | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md) |
| 13 | Transparency and instructions for deployers | Provider | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md) |
| 14 | Human oversight | Provider (design), deployer (use) | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md), role guides |
| 15 | Accuracy, robustness, cybersecurity | Provider | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md) |
| 16, 17 | Provider obligations, quality management system | Provider | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md) |
| 25 | Value chain responsibilities | All | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | [T03](T03_Supplier_Due_Diligence_EU_Addendum.md) |
| 26 | Deployer obligations (use per instructions, oversight, input data, monitoring, log retention, inform workers) | Deployer | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [T02](T02_Impact_Assessment_FRIA_DPIA.md), [T08](T08_Audit_Checklist.md) |
| 27 | Fundamental rights impact assessment | Certain deployers (public bodies and some private entities, for example for credit scoring and life or health insurance) | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-042](06_Proposed_Control_Fundamental_Rights_Impact_Assessment.md) (proposed) | [T02](T02_Impact_Assessment_FRIA_DPIA.md) |
| 43, 47, 48 | Conformity assessment, declaration of conformity, CE marking | Provider | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md) |
| 49 | Registration in the EU database | Provider (and some deployers) | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md) |
| 72 | Post-market monitoring | Provider | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [T05](T05_AI_Incident_and_Breach_Reporting_Workflow.md) |
| 73 | Serious incident reporting | Provider | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [T05](T05_AI_Incident_and_Breach_Reporting_Workflow.md) |
| 86 | Right to explanation of an individual decision | Affected person | [AI-CTRL-041](../11_GCC_AI_Compliance/06_Proposed_Control_Fairness_Bias_Explainability.md) (proposed) | [T06](T06_Transparency_Notice.md) |

### 3.4 Penalties

The figures are [Recalled]. One secondary source repeats the high-risk figure.

| Breach | Maximum |
|---|---|
| Prohibited practices | EUR 35M or 7% of worldwide turnover, whichever is higher |
| Most other obligations, including high-risk and GPAI | EUR 15M or 3% |
| Incorrect information to authorities | EUR 7.5M or 1% |

For SMEs the lower of the two figures applies [Recalled]. Verify.

## 4. Register of related EU instruments

| # | Instrument | Relevance to AI | Key points | Wiki controls and templates | Wiki coverage | Tag |
|---|---|---|---|---|---|---|
| E1 | AI Act | Core | See sections 2 and 3 | Whole library | Partial: timeline and Article 15 summarised in [Foundations page 9](../00_Foundations/09-Governance-Standards-and-Regulation.md); no article-level mapping | [Reported], [Recalled] |
| E2 | GDPR | Any personal data in training, prompts or outputs | Lawful basis, purpose limitation, minimisation, rights, Art. 22 automated decisions, DPIA (Art. 35), transfers (Ch. V), breach notice within 72 hours (Art. 33), fines up to EUR 20M or 4% | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Partial | [Recalled] |
| E3 | EDPB guidance on AI models and personal data | How to treat models trained on personal data; legitimate interest tests | Opinion 28/2024 exists | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | Not covered | [Recalled]; confirm title and content |
| E4 | Digital Omnibus on data (GDPR changes) | Would allow legitimate interest for AI training, redefine pseudonymised data and add Art. 9(2)(k) | Early stage as of Sept 2026; adoption not expected before 2027 | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | Watchlist | [Reported], single source |
| E5 | NIS2 Directive | Cyber risk management and reporting for essential and important entities | Early warning in 24 hours, notification in 72 hours, final report in one month | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Not covered | [Recalled] timings; transposition varies by Member State |
| E6 | DORA | Financial sector ICT risk, incident reporting, third-party risk | Applicable since Jan 2025; ICT third-party register | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Not covered | [Reported] date |
| E7 | Cyber Resilience Act | Products with digital elements, including software with AI | Vulnerability reporting from 11 Sept 2026; full application 11 Dec 2027 | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) | Not covered | [Reported], single source |
| E8 | Product Liability Directive (new) | Software and AI as products; defect liability | Transposition deadline not confirmed | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | Not covered | [Unverified] |
| E9 | Data Act | Access to and portability of connected-product data; cloud switching | Application from Sept 2025 | [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | Not covered | [Recalled]; verify |
| E10 | Digital Services Act | Platforms, recommender systems, systemic risks | Risk assessment for very large platforms | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | Not covered | [Recalled] |
| E11 | Copyright Directive text-and-data-mining opt-out | Training data | Rights holders can reserve their rights; a GPAI copyright policy is needed | [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029) | Partial | [Recalled] |
| E12 | Commission guidelines: prohibited practices | Interpret Art. 5 | Published Feb 2025 | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | Not covered | [Recalled] |
| E13 | Commission guidelines: GPAI | Scope and obligations of GPAI providers | Published 10 July 2025 | [T12](T12_GPAI_Model_Checklist.md) | Not covered | [Reported] |
| E14 | Commission draft guidelines: high-risk classification (Art. 6) | Classification and the Art. 6(3) filter | Draft released 19 May 2026; consultation closed 23 July 2026; not final | [T01](T01_AI_System_Classification.md) | Not covered | [Reported] |
| E15 | GPAI Code of Practice (July 2025) | Route to show GPAI compliance | Reported signatories: OpenAI, Anthropic, Microsoft, Google, Mistral AI; xAI in part (safety chapter); Meta declined | [T12](T12_GPAI_Model_Checklist.md) | Not covered | [Reported], one source |
| E16 | Code of Practice on marking and labelling AI-generated content | Voluntary route to Art. 50 | Final version published 10 June 2026; multi-layer machine-readable marking; detection; deepfake labels | [T06](T06_Transparency_Notice.md) | Not covered | [Reported] |
| E17 | Harmonised standards, CEN-CENELEC JTC 21 | Presumption of conformity once cited in the OJ | EN 18286:2026 (QMS) reported approved 12 July 2026, OJ citation pending. Drafts: prEN 18228 (risk management), 18282 (cybersecurity), 18284 (dataset quality), 18229 parts 1 and 2 (trustworthiness: logging, transparency, human oversight) | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | Not covered | [Reported], single source; verify numbers |
| E18 | ISO/IEC 42001 | AI management system; likely to map to the AI Act QMS, but it is not a harmonised standard | Certification can support evidence | Whole library | Mapped control by control in the control library | [Recalled] |

## 5. Known gaps in the wiki

| Gap | Proposed fix |
|---|---|
| No role-based (provider or deployer) view of obligations | Add the [T01](T01_AI_System_Classification.md) classification step to intake, and a role column to the control library |
| High-risk obligations are not mapped article by article | Use the table in section 3.3 once it is verified |
| No control for a fundamental rights impact assessment | [AI-CTRL-042](06_Proposed_Control_Fundamental_Rights_Impact_Assessment.md) (proposed) |
| No fairness, bias or explainability control | [AI-CTRL-041](../11_GCC_AI_Compliance/06_Proposed_Control_Fairness_Bias_Explainability.md) (proposed in the GCC section) |
| General-purpose AI model obligations are absent | [T12](T12_GPAI_Model_Checklist.md) and a GPAI sub-section |
| Few test cases for Art. 50 transparency | Add test cases based on [T06](T06_Transparency_Notice.md) |
| No control specific to AI literacy; [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) covers user training in general | Add to the training family; [T07](T07_AI_Literacy_Programme_Record.md) |
| No named authority engagement (AI Office, national authorities, data protection authorities) | [T11](T11_Authority_and_Standards_Engagement_Log.md) |

## 6. Verification checklist

- [ ] Omnibus regulation number, entry into force and final text
- [ ] Which articles the omnibus amended (4, 6, 10, 49, 50 and others)
- [ ] Annex III list and Annex IV content
- [ ] Penalty ceilings and the SME rule
- [ ] Art. 27 FRIA scope
- [ ] Art. 73 reporting timelines
- [ ] Final Art. 6 guidelines
- [ ] Standards status and OJ citation
- [ ] National competent authority and market surveillance designations, per Member State
- [ ] GDPR article numbers; EDPB Opinion 28/2024
- [ ] NIS2 transposition in your Member States; CRA dates
- [ ] Add the primary URL and retrieval date beside every confirmed row

## 7. Source note

Secondary sources used: law-firm and vendor notes on the AI Omnibus (Addleshaw Goddard, Usercentrics, VerifyWise, Secure Privacy, Data Protection Report), the Kennedys timeline, a Cloud Security Alliance research note on GPAI enforcement, Jones Day on the marking code, Osborne Clarke on the draft Art. 6 guidelines, Modulos documentation on harmonised standards, Heuking on the data omnibus, and an Advisori note on NIS2, DORA and the CRA. The Advisori note was written before the omnibus, so its AI Act dates were not used. No row above has been verified against a primary source.
