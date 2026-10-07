---
title: "GCC AI Regulatory Hub"
author: Nachiket Sathaye
parent: "GCC AI Compliance"
nav_order: 1
description: "UAE, Saudi, Qatar, Bahrain and Oman AI-relevant laws, policies and security baselines mapped to AI security controls, with verification status."
document_type: AI Security Wiki Reference
version: 1.0
---

# GCC AI Regulatory Hub

> **Verification required.** Regional claims on this page were compiled from secondary sources on 7 October 2026. No primary legal text was read, and each claim is tagged [Reported], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

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
| U1 | Federal Decree-Law 45/2021 (PDPL) | Binding | Lawful basis, purpose limitation, data subject rights, impact assessment, transfer rules, breach notification. Reported as a 31-article law. Executive Regulation reported as pending. | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Article numbers; Executive Regulation status [Reported] |
| U2 | Federal Decree-Law 34/2021 (cybercrime) | Binding | Misuse, unauthorised access, deepfake-type scenarios | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [Unverified] AI relevance |
| U3 | UAE Charter for the Development and Use of AI | Non-binding; 12 principles (safety, transparency, human oversight among them) | Cited in procurement and policy | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [Conflict] publication month |
| U4 | UAE AI Ethics: Principles and Guidelines, plus self-assessment | Voluntary; 8 principles | Self-assessment evidence used in tenders | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-041](06_Proposed_Control_Fairness_Bias_Explainability.md) (proposed) | [Reported] |
| U5 | Federal Authority for Artificial Intelligence and Data | Announced 14 June 2026; consolidates AI Office, TDRA digital-government arm, Emirates Data Office | New central body for AI, data protection, digital government | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [Reported] Confirm mandate officially |
| U6 | DIFC Data Protection Law and Regulation 10 | Binding in DIFC | Autonomous and semi-autonomous systems processing personal data. Reported concepts: human-defined purposes, an Autonomous Systems Officer (ASO) role, certification. Consultation (from 18 June 2026) proposes AI accreditation and certification | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | [Conflict] enforcement date (Sept 2023 vs Jan 2026) |
| U7 | ADGM Data Protection Regulations | Binding in ADGM | Free-zone regime | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007) | [Unverified] |
| U8 | Dubai AI Security Policy (Dubai Electronic Security Center) | Policy, Sept 2024 | Security standards for AI incl. generative AI. Closest in scope to this wiki | Whole library | Obtain text; map clause by clause |
| U9 | CBUAE Guidance Note on responsible AI/ML adoption | Supervisory guidance, 23 Feb 2026, for licensed financial institutions | See 2.1 | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) | [Reported] |
| U10 | Abu Dhabi AI and Advanced Technology Council (Law 3/2024) | Governance body | Jurisdiction context | None | [Reported] |
| U11 | UAE information assurance (NESA/IA) | Baseline referenced by the wiki | No clause mapping in wiki | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-009](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009), [AI-CTRL-032](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-032) | [Unverified] custodian and version |
| U12 | Dubai AI Seal | Tiered certification; reported as needed for Dubai government AI contracting | Procurement gate | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [Unverified] single source |

### 2.1 CBUAE Guidance Note expectations to wiki controls

| Reported expectation | Covered by |
|---|---|
| Board accountability for AI | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037); [TC-L01-003](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-003), [TC-L01-020](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-020) |
| Complete AI model inventory (name, purpose, risk rating) | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011); [T09](T09_AI_System_Inventory.md) |
| Annual bias testing or on material change | [AI-CTRL-041](06_Proposed_Control_Fairness_Bias_Explainability.md) (proposed); [T10](T10_Bias_Testing_Record.md) |
| Consumer opt-out consideration for high-impact decisions | [TC-L03-008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008) |
| Human review of AI decisions | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023); [TC-L03-008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008) |
| Kill-switch capability | [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) |
| Third-party AI vendor due diligence | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014); [T03](T03_Vendor_Due_Diligence_GCC_Addendum.md) |
| Arabic and English disclosure | [TC-L03-003](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-003), [TC-L03-030](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-030); [T06](T06_Bilingual_AI_Use_Notice.md) |

## 3. Saudi Arabia

| # | Instrument | Type / status | Key points reported | Wiki controls | Verify |
|---|---|---|---|---|---|
| S1 | PDPL | Binding; penalties reported up to SAR 5M | Active enforcement reported | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) | [Conflict] in force Sept 2023 vs enforced Sept 2024 |
| S2 | SDAIA AI Ethics Principles | Non-binding; v2.0 reported Sept 2023; seven principles; references international standards incl. NIST AI RMF | Cited by SDAIA-aligned buyers | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [Conflict] version and update dates |
| S3 | SDAIA Generative AI Guidelines | Non-binding; Jan 2024; government focus | GenAI use rules | [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002), [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010), [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | [Reported] |
| S4 | SDAIA AI Adoption Framework | Non-binding; four maturity levels; Sept 2024 | Maturity model | [Maturity Model and Roadmap](../00_Foundations/11-Maturity-Model-and-Roadmap.md) | [Reported] |
| S5 | SDAIA National AI Risk Management Framework (SDAIA-P145) | Reported published April 2026; likelihood-impact matrix, proportional application; Arabic text authoritative | Basis for [T12](T12_Risk_Register_4x4.md) | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md) | [Conflict] date (April vs July 2026) |
| S6 | NCA ECC and CCC | Binding for government and critical infrastructure | Cyber and cloud baselines | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-032](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-032) | [Reported] |
| S7 | NCA NCNICC-1:2025 | Reported as applying to non-critical private sector from Jan 2026 | Cyber baseline | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-032](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-032) | [Unverified] |
| S8 | NCA AI Cybersecurity Guidelines | Consultation reported closed 5 Aug 2026; four domains: governance, defence, resilience, third-party risk; generative and agentic AI | Final text expected | Whole library | [Unverified] single source |
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
| B1 | Law 30/2018 (PDPL) | Binding | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | [Reported] |
| B2 | General Policy for the Use of AI (v1.0, May 2025) | Reported binding on government entities | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | [Reported] |
| B3 | Draft AI law (38 articles) | Not enacted as of July 2026 per sources; criminal penalties proposed | Watchlist | [Reported] re-check |
| B4 | CBB digital financial advice directives | Sector | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | [Reported] |

## 6. Oman

| # | Instrument | Status | Wiki controls | Verify |
|---|---|---|---|---|
| O1 | National AI Policy (in force 9 April 2025, MTCIT) | Reported mandatory within scope: governance standards, regular assessments, documentation, compliance reports on request | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [Reported] |
| O2 | PDPL amendments (automated processing, retention) | Reported cleared May 2026; awaiting royal promulgation | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | [Reported] re-check |

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
| Bias testing | CBUAE, ethics frameworks | [T10](T10_Bias_Testing_Record.md), [AI-CTRL-041](06_Proposed_Control_Fairness_Bias_Explainability.md) |
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
| Fairness, bias testing and explainability | [AI-CTRL-041](06_Proposed_Control_Fairness_Bias_Explainability.md) (proposed); [T10](T10_Bias_Testing_Record.md); [TC-L03-008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008), [TC-L03-029](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-029) |
| Engagement with regulators and ethics bodies | [T11](T11_Regulator_Engagement_Log.md); [TC-L02-020](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-020), [TC-L03-026](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-026) |
| Banking, insurance and government expectations | Section 2.1 for the CBUAE note; [T03](T03_Vendor_Due_Diligence_GCC_Addendum.md), [T08](T08_Audit_Checklist.md); [TC-L03-021](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-021) |
| Arabic and English | [T06](T06_Bilingual_AI_Use_Notice.md); section 4 of the [Guide for AI Practitioners](02_Guide_AI_Practitioners.md); [TC-L03-030](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-030) |

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

Secondary sources used: Modulos documentation pages on the CBUAE note, UAE PDPL, UAE AI Ethics and SDAIA-P145; law-firm and news trackers on DIFC Reg 10, the UAE Charter, SDAIA ethics, QCB and NCSA. No row above has been verified against a primary source.
