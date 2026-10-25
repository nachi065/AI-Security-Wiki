---
title: "GCC AI Regulatory Hub"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "GCC AI Compliance"
nav_order: 1
description: "UAE, Saudi, Qatar, Bahrain and Oman AI-relevant laws, policies and security baselines mapped to AI security controls, with verification status."
document_type: AI Security Wiki Reference
version: 1.0
last_reviewed: 2026-10-26
---

# GCC AI Regulatory Hub

> **Verification required.** Regional claims on this page were compiled from secondary sources on 7 October 2026. On 10 October 2026 four rows (S2, S3, S4 and B1), on 16 October 2026 row U1, on 19 October 2026 rows U2 and S8, and on 26 October 2026 rows U4, B2, U5 and U9 were checked against the issuing body's own documents and are tagged [Verified]. Most other government sites refused automated retrieval, so every other claim is still tagged [Reported], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

This page maps UAE and GCC laws, policies and baselines that bear on AI to the wiki's controls. Clause and article numbers are left blank unless a source showed them.

## 1. How the region is structured

No GCC state has an enacted horizontal AI statute comparable to the EU AI Act **[Reported]**. Duties arrive through four layers. Apply the strictest layer that applies to you.

| Layer | What it contains | Binding? | Typical question it answers |
|---|---|---|---|
| 1. Data protection law | UAE PDPL, DIFC and ADGM regimes, Saudi PDPL, Qatar PDPPL, Bahrain PDPL, Oman PDPL | Yes | May we use this personal data in this model, and what rights do people have? |
| 2. National AI ethics and policy | UAE Charter, UAE AI Ethics, SDAIA ethics and adoption frameworks, MCIT ethical AI, Bahrain policy, Oman policy | Mostly no (some scoped to government; Bahrain and Oman reported as binding in scope) | What does "responsible" mean here? What will a government buyer ask for? |
| 3. Sector regulator guidance | CBUAE, QCB, CBB, SAMA (not researched) | Varies; QCB reported as binding for licensees | What must a bank or insurer do before using AI? |
| 4. Cybersecurity baselines | Dubai AI Security Policy, NCA ECC/CCC, NCSA AI guidelines, UAE information assurance | Varies | What security controls must the AI system and its hosting meet? |

**Rule of thumb:** if personal data is involved, layer 1 applies regardless of any AI risk label. If you serve a regulated financial entity or government, layers 3 and 4 will show up in the contract.

## 2. United Arab Emirates

| # | Instrument | Type / status | Key points reported | Wiki controls | Verify |
|---|---|---|---|---|---|
| U1 | Federal Decree-Law 45/2021 (PDPL) | Binding | Lawful basis, purpose limitation, data subject rights, impact assessment, transfer rules, breach notification. Federal Decree-Law No. 45 of 2021, issued 20 September 2021, 31 articles: breach reporting Art. 9, impact assessment Art. 21, cross-border transfer Arts. 22 and 23. Executive Regulation status not checked. | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Executive Regulation status; whether later amendments exist [Verified] (text read on 16 Oct 2026; re-read on 19 Oct 2026, no change) |
| U2 | Federal Decree-Law 34/2021 (cybercrime) | Binding | Misuse, unauthorised access, deepfake-type scenarios | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [Verified] title, number, 20 Sep 2021 issue date and binding status ([UAE legislation portal](https://uaelegislation.gov.ae/en/legislations/1526/download), read 19 Oct 2026). AI and deepfakes are not named in the text; Art. 54 covers e-robots used to spread false data |
| U3 | UAE Charter for the Development and Use of AI | Non-binding; 12 principles (safety, transparency, human oversight among them) | Cited in procurement and policy | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [Conflict] publication month: the [UAE legislation portal](https://uaelegislation.gov.ae/en/policy/details/the-uae-charter-for-the-development-and-use-of-artificial-intelligence) gives an issue date of 10 Jun 2024 and the [Charter document](https://ai.gov.ae/wp-content/uploads/2024/07/UAEAI-Methaq-EN2-3.pdf) cover says July 2024 (both read 19 Oct 2026). The count of 12 principles was not checked |
| U4 | UAE AI Ethics: Principles and Guidelines, plus self-assessment | Voluntary; 8 principles | Self-assessment evidence used in tenders | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [Verified] non-binding status and the 8 principles, from [AI Ethics: Principles and Guidelines (Dec 2022)](https://assets.u.ae/api/public/content/893c940c21c4403ea8df7faad66a889e?v=b2f9c1a1) and the AI Office's [self-assessment page](https://ai.gov.ae/aiethics-self-assessment/) (read 26 Oct 2026). Use of the self-assessment in tenders was not checked |
| U5 | Artificial Intelligence and Data Authority (some sources call it the Federal Authority for AI and Data) | Approval announced 14 June 2026; brings together the AI Office, the TDRA Digital Government Sector and the UAE Data Office; reports to the Cabinet | Single national body for data, AI and digital government. The Cabinet announcement does not mention data protection | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [Verified] name, date and mandate, from the [UAE Cabinet announcement](https://uaecabinet.ae/en/news/mohammed-bin-rashid-approves-establishing-artificial-intelligence-and-data-authority) (read 26 Oct 2026). No founding law or decree is named |
| U6 | DIFC Data Protection Law and Regulation 10 | Binding in DIFC | Autonomous and semi-autonomous systems processing personal data. Reported concepts: human-defined purposes, an Autonomous Systems Officer (ASO) role, certification. The DIFC now lists a Regulation 10 accreditation and certification framework with approved certification bodies. A June 2026 consultation (comments by 18 July 2026) proposes a new Regulation 11 on recognising accreditation and certification frameworks and wider ASO duties; it is not yet enacted | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | [Conflict] enforcement date (Sept 2023 vs Jan 2026). The [DIFC Regulation 10 page](https://www.difc.com/business/registrars-and-commissioners/commissioner-of-data-protection/regulation-10) (read 26 Oct 2026) says the regulations were enacted on 1 Sep 2023 and gives no separate enforcement date; no DIFC source read gives Jan 2026. The ASO role is in the Commissioner's [guidance on Regulation 10](https://assets.difc.com/v1/media/edge/images/dubaiintern0078-difcexperie96c5-production-3253/media/project/difcexperiences/difc/difcwebsite/documents/registrars-and-commissioners/guidance-and-handbooks/lawful-processing/dp_regulation_10.pdf), which is not law; the [consultation paper](https://assets.difc.com/v1/media/edge/images/dubaiintern0078-difcexperie96c5-production-3253/media/project/difcexperiences/difc/difcwebsite/documents/laws--regulations/consultation-paper.pdf) is a draft |
| U7 | ADGM Data Protection Regulations | Binding in ADGM | Free-zone regime | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007) | [Reported] from [ADGM briefing slides](https://assets.adgm.com/download/assets/ADGM+Data+Protection+Regulations+2021+Updated.pdf/146aa34858b011efb99a36e29b0f3a63), read 19 Oct 2026: enacted 11 Feb 2021; applies to controllers and processors established in ADGM. The regulations text was not read |
| U8 | Dubai AI Security Policy (Dubai Electronic Security Center) | Policy, Sept 2024 | Security standards for AI incl. generative AI. Closest in scope to this wiki | Whole library | Obtain text; map clause by clause |
| U9 | CBUAE Guidance Note on responsible AI/ML adoption | Supervisory guidance for licensed financial institutions, including insurance providers. The Rulebook shows it issued on 11 Feb 2026; the CBUAE announced it on 23 Feb 2026 | See 2.1 | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) | [Verified] title, scope, guidance status and the expectations in 2.1, from the [note on the CBUAE Rulebook](https://rulebook.centralbank.ae/en/rulebook/guidance-note-consumer-protection-and-responsible-adoption-and-use-artificial-intelligence) (read 26 Oct 2026; the Rulebook date "11/2/2026" is read as 11 Feb 2026). The [CBUAE press release](https://www.centralbank.ae/media/mykn5fue/cbuae-issues-guidance-note-to-protect-consumers-and-ensure-responsible-use-of-artificial-intelligence-in-the-financial-sector-en.pdf) (read 19 Oct 2026) is dated 23 Feb 2026 |
| U10 | Abu Dhabi AI and Advanced Technology Council (Law 3/2024) | Governance body | Jurisdiction context | None | [Reported] |
| U11 | UAE information assurance (NESA/IA) | Baseline referenced by the wiki | No clause mapping in wiki | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-009](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009), [AI-CTRL-032](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-032) | [Unverified] custodian and version |
| U12 | Dubai AI Seal | Tiered certification; reported as needed for Dubai government AI contracting | Procurement gate | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [Unverified] single source |

### 2.1 CBUAE Guidance Note expectations to wiki controls

The expectations below were checked against the note's text on the [CBUAE Rulebook](https://rulebook.centralbank.ae/en/rulebook/guidance-note-consumer-protection-and-responsible-adoption-and-use-artificial-intelligence) on 26 October 2026; the section of the note is given in brackets. The inventory fields (name, purpose, risk rating) were not checked.

| Expectation (section of the note) | Covered by |
|---|---|
| Accountability for AI systems and outcomes (2) | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037); [TC-L01-003](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-003), [TC-L01-020](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-020) |
| Inventory of all AI models and systems developed or deployed (2) | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011); [T09](T09_AI_System_Inventory.md) |
| Bias testing once a year or each time a model is upgraded (3) | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041); [T10](T10_Bias_Testing_Record.md) |
| Consider opt-out rights; alternatives for customers who do not want an AI decision (4, 7) | [TC-L03-008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008) |
| Customers can ask for human review or an explanation of AI decisions (7) | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023); [TC-L03-008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008) |
| Clear and immediate ability, with human intervention, to stop using an AI model (6) | [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) |
| Due diligence on third-party AI providers (9) | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014); [T03](T03_Vendor_Due_Diligence_GCC_Addendum.md) |
| Disclosures in both Arabic and English (4) | [TC-L03-003](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-003), [TC-L03-030](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-030); [T06](T06_Bilingual_AI_Use_Notice.md) |

## 3. Saudi Arabia

| # | Instrument | Type / status | Key points reported | Wiki controls | Verify |
|---|---|---|---|---|---|
| S1 | PDPL | Binding; penalties reported up to SAR 5M | Active enforcement reported | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) | [Conflict] in force Sept 2023 vs enforced Sept 2024 |
| S2 | SDAIA AI Ethics Principles | Non-binding. SDAIA publishes "AI Ethics Principles", document SDAIA-P114E, version 1, dated May 2025; its page links to it as a draft. It lists the NIST AI RMF among its references and describes registration as optional | Cited by SDAIA-aligned buyers | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [Verified] document number, version and date. The v2.0 text reported for Sept 2023 and the count of seven principles were not checked |
| S3 | SDAIA Generative AI Guidelines | Two guidelines, one for government staff and one for the public. The government edition's cover is dated 2025 and tells government entities to follow the AI Ethics Principles | GenAI use rules | [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002), [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010), [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | [Verified] that both exist. The Jan 2024 date was not seen |
| S4 | SDAIA AI Adoption Framework | A guiding reference for government and private entities; cover dated 2025 | Maturity model | [Maturity Model and Roadmap](../00_Foundations/11-Maturity-Model-and-Roadmap.md) | [Verified] that it exists and is guidance. The four maturity levels and the Sept 2024 date were not seen |
| S5 | SDAIA National AI Risk Management Framework (SDAIA-P145) | Reported published April 2026; likelihood-impact matrix, proportional application; Arabic text authoritative | Basis for [T12](T12_Risk_Register_4x4.md) | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md) | [Conflict] date (April vs July 2026). Not listed on the SDAIA regulations page on 10 October 2026 |
| S6 | NCA ECC and CCC | Binding for government and critical infrastructure | Cyber and cloud baselines | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-032](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-032) | [Reported] |
| S7 | NCA NCNICC-1:2025 | Reported as applying to non-critical private sector from Jan 2026 | Cyber baseline | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-032](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-032) | [Unverified] |
| S8 | NCA AI Cybersecurity Guidelines | Consultation reported closed 5 Aug 2026; four domains: governance, defence, resilience, third-party risk; generative and agentic AI | Final text expected | Whole library | [Verified] consultation, 5 Aug 2026 deadline and four domains, from the [NCA announcement](https://nca.gov.sa/en/news/ai-cybersecurity-guidelines/), read 19 Oct 2026; the [consultations page](https://nca.gov.sa/en/public-consultations/ai-cybersecurity-guidelines/) lists it as Closed. No final text yet |
| S9 | Copyright text-and-data-mining exception | Reported effective 12 Aug 2026 | Training-data IP | [TC-L03-028](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-028) | [Reported] |
| S10 | NDMO, CST, SAMA localisation/sector rules | Overlays | Residency and sector | [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007) | [Unverified] |

## 4. Qatar

| # | Instrument | Status | Wiki controls | Verify |
|---|---|---|---|---|
| Q1 | Law 13/2016 (PDPPL) | Binding | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) | [Reported] |
| Q2 | NCSA Guidelines for Secure Adoption and Usage of AI (2024) | Voluntary, reported hardening into audit baselines | Whole library | [Reported] |
| Q3 | MCIT Principles and Guidelines for Ethical AI | Non-binding | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [Conflict] year 2024 vs 2025 |
| Q4 | QCB AI Guideline (4 Sept 2024) | Reported binding for QCB licensees; approval gate for high-risk AI; gating of fully autonomous systems | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033) | [Reported] strongest claim in region; confirm |

## 5. Bahrain

| # | Instrument | Status | Wiki controls | Verify |
|---|---|---|---|---|
| B1 | Law 30/2018 (PDPL) | Binding. Published by the Personal Data Protection Authority as Law No. (30) of 2018 with Respect to Personal Data Protection Law | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | [Verified] title, re-read 19 Oct 2026 with no amendment listed; articles not checked |
| B2 | General Policy for the Use of AI (v1.0, May 2025) | Binding on all government entities from its approval by the Ministerial Committee for ICT on 20 May 2025; some provisions say "should" rather than "must" | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | [Verified] version 1.0, approval on 20 May 2025 and scope, from the [iGA policy document](https://iga.gov.bh/Media/Publications/National%20Digital%20Policies/General%20Policy%20for%20the%20Use%20of%20AI.pdf) (read 26 Oct 2026) |
| B3 | Draft AI law (38 articles) | Not enacted as of July 2026 per sources; criminal penalties proposed | Watchlist | [Reported] re-check |
| B4 | CBB digital financial advice directives | Sector | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | [Reported] |

## 6. Oman

| # | Instrument | Status | Wiki controls | Verify |
|---|---|---|---|---|
| O1 | National AI Policy (in force 9 April 2025, MTCIT) | Reported mandatory within scope: governance standards, regular assessments, documentation, compliance reports on request | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [Reported] |
| O2 | PDPL amendments (automated processing, retention) | Reported issued by Royal Decree 68/2026 of 3 Sep 2026 and published in Official Gazette 1664 on 6 Sep 2026, in force the day after publication. Reported changes: new definitions of health data, controller and automated processing; Articles 2, 3, 7, 10, 14, 15, 22, 25 and 27 replaced; Articles 5bis and 10bis added | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | [Reported] from an English translation and news reports; the Official Gazette text was not read |

## 7. Kuwait

Kuwait has not been researched for this page.

## 8. International bridges

| Standard | Why it helps in the GCC | Note |
|---|---|---|
| ISO/IEC 42001 | AI management system; SDAIA itself is reported as certified; useful evidence for buyers | [Reported] SDAIA certification |
| NIST AI RMF | SDAIA ethics principles reference it | Use for GOVERN/MAP/MEASURE/MANAGE mapping |
| ISO/IEC 27001 | Common base for NCA, NESA and Dubai security expectations | Gap analysis still needed |

## 9. What each regional layer asks for, in practical terms

| Practical ask | Where it most often comes from | Template or page |
|---|---|---|
| AI inventory with risk rating | CBUAE, Oman policy, SDAIA risk framework | [T09](T09_AI_System_Inventory.md), [T01](T01_AI_Use_Case_Intake_and_Risk_Tiering.md) |
| Impact assessment before deployment | PDPL regimes, DIFC Reg 10, SDAIA risk framework | [T02](T02_AI_Impact_Assessment.md) |
| Human oversight and ability to stop | CBUAE, QCB, UAE Charter, DIFC Reg 10 | [T01](T01_AI_Use_Case_Intake_and_Risk_Tiering.md), [Guide for Implementors](05_Guide_Implementors.md) |
| Bias testing | CBUAE, ethics frameworks | [T10](T10_Bias_Testing_Record.md), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) |
| Vendor due diligence | CBUAE, NCA, NCSA | [T03](T03_Vendor_Due_Diligence_GCC_Addendum.md) |
| Data location and transfer proof | PDPLs, NCA, sector rules | [T04](T04_Data_Residency_Attestation.md) |
| Arabic and English notice | CBUAE, government buyers | [T06](T06_Bilingual_AI_Use_Notice.md) |
| Incident and breach notice | PDPLs, sector regulators, NCA | [T05](T05_AI_Incident_and_Breach_Notification_Workflow.md) |
| Ethics self-assessment | UAE and SDAIA ethics | [T07](T07_Ethics_Self_Assessment_Worksheet.md) |
| Regulator contact record | All | [T11](T11_Regulator_Engagement_Log.md) |

## 10. Where the wiki covers this

The topics raised on this page are covered by the following controls, test cases and templates.

| Topic | Covered by |
|---|---|
| Instruments mapped to controls and test cases | [Regulatory Crosswalk](07_Regulatory_Crosswalk.md), which gives the control themes for each instrument; the case index by control theme in the [Framework Adoption Guide](../10_Test_Case_Library/framework-adoption-guide.md) |
| Fairness, bias testing and explainability | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041); [T10](T10_Bias_Testing_Record.md); [TC-L03-008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008), [TC-L03-029](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-029); [TC-L03-031](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-031), [TC-L03-032](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-032) |
| Engagement with regulators and ethics bodies | [T11](T11_Regulator_Engagement_Log.md); [TC-L02-020](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-020), [TC-L03-026](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-026); [AI-CTRL-043](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-043); [TC-L03-039](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-039) |
| Banking, insurance and government expectations | Section 2.1 for the CBUAE note; [T03](T03_Vendor_Due_Diligence_GCC_Addendum.md), [T08](T08_Audit_Checklist.md); [TC-L03-021](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-021); [Sector Overlays](../04_Domain_Standards/10B_Sector_Overlays.md) |
| Arabic and English | [T06](T06_Bilingual_AI_Use_Notice.md); section 4 of the [Guide for AI Practitioners](02_Guide_AI_Practitioners.md); [TC-L03-030](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-030); [TC-L03-033](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-033) |

## 11. Verification checklist

- [ ] U1 article numbers and Executive Regulation status
- [ ] U3/U4 publication dates and principle counts
- [ ] U5 official announcement
- [ ] U6 enforcement date; ASO and certification provisions; consultation paper
- [ ] U8 policy text
- [ ] U9 CBUAE Rulebook entry
- [ ] U11 custodian and version
- [ ] S1 in-force vs enforcement dates
- [ ] S5 SDAIA publication date
- [ ] S7, S8 status
- [ ] Q2, Q4 binding status
- [ ] B2, O1 binding scope
- [ ] Kuwait research
- [ ] Add primary URL and retrieval date beside every confirmed row

## 12. Source note

Secondary sources used: Modulos documentation pages on the CBUAE note, UAE PDPL, UAE AI Ethics and SDAIA-P145; law-firm and news trackers on DIFC Reg 10, the UAE Charter, SDAIA ethics, QCB and NCSA. Rows S2, S3, S4 and B1 were checked on 10 October 2026 against documents on the SDAIA site and the Bahrain Personal Data Protection Authority site. The UAE legislation portal and several other government sites refused automated retrieval, so no other row has been verified against a primary source. Later checks: row U1 on 16 October 2026, and rows U2, U9 and S8 on 19 October 2026, against the UAE legislation portal, the CBUAE site and the NCA site.
