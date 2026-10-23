---
title: "UK AI Regulatory Hub"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "UK AI Compliance"
nav_order: 1
description: "UK AI-relevant law mapped to AI security controls: UK GDPR, the Data (Use and Access) Act 2025, the five principles, ICO, FCA and PRA expectations."
document_type: AI Security Wiki Reference
version: 1.0
last_reviewed: 2026-10-20
---

# UK AI Regulatory Hub

> **Verification required.** Claims on this page about UK law were compiled on 7 October 2026 from secondary web sources and from memory of the law. Row UK13 (AI Management Essentials) was checked against the government's own documents on 15 October 2026, and rows UK1, UK9, UK10, UK3, UK6, UK8 and UK11 on 20 October 2026; those rows are tagged [Verified]; every other claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

This page maps UK laws, guidance and standards that bear on AI to the wiki's controls.

## 1. Regional model

There are four layers [Reported]:

1. Data protection: UK GDPR and the Data Protection Act 2018, as amended.
2. Five cross-sector principles, applied by existing regulators (the ICO, FCA, CMA, Ofcom and others).
3. Sector rules for financial services, online safety and competition.
4. Cyber guidance from the NCSC and DSIT.

The EU AI Act reaches UK firms that have EU customers or whose outputs affect people in the EU. See the [EU AI Regulatory Hub](../12_EU_AI_Compliance/01_EU_AI_Regulatory_Hub.md).

## 2. Instrument register

| # | Instrument | Type / status | Key points | Wiki controls | Tag | To verify |
|---|---|---|---|---|---|---|
| UK1 | UK approach: five principles (safety and robustness; transparency; fairness; accountability; contestability and redress) | Non-statutory; from the March 2023 White Paper | Applied by existing regulators | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [Verified] five principles and non-statutory basis, from the [White Paper](https://www.gov.uk/government/publications/ai-regulation-a-pro-innovation-approach/white-paper), read 20 Oct 2026 | Current government position; the source describes it "as of 2025" |
| UK2 | UK GDPR and Data Protection Act 2018 | Binding | Lawful basis, rights, DPIA, transfers, breach notice | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [Recalled] | Articles |
| UK3 | Data (Use and Access) Act 2025: new Arts 22A to 22D | Binding; section 80 in force 5 Feb 2026 (SI 2026/82, reg. 2(j)); not for decisions taken before that date (reg. 5) | Permits solely automated decisions with safeguards: meaningful information, human review and a right to contest. Meaningful human involvement must be real | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [Verified] substitution of Arts 22A to 22D and commencement, from [section 80](https://www.legislation.gov.uk/ukpga/2025/18/section/80/enacted) and [SI 2026/82](https://legislation.gov.uk/uksi/2026/82), read 20 Oct 2026. The key points were not re-read | ICO guidance |
| UK4 | ICO guidance on AI and data protection | Regulator guidance | Fairness, transparency, DPIA and explainability for AI | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [Recalled] | Current versions; any AI and biometrics strategy |
| UK5 | FCA approach (principles, Consumer Duty, SM&CR) | Regulatory framework | No AI-specific rulebook reported; existing rules apply | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | [Recalled] | Current FCA statements |
| UK6 | PRA SS1/23 model risk management | Supervisory statement for UK banks, building societies and PRA-designated investment firms with internal model approval for regulatory capital; first effective 17 May 2024; current version effective 23 Apr 2026 | Model inventory, validation, governance | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [Verified] scope and dates, from the [Bank of England page](https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss), read 20 Oct 2026 | What the April 2026 version changed |
| UK7 | CMA and Ofcom roles (competition; online safety) | Regulators | Competition work on foundation models; Online Safety Act for user-generated services | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [Reported] | Scope for AI services |
| UK8 | Copyright and AI training | No statutory text-and-data-mining exception for commercial AI training (s.29A CDPA covers non-commercial research only); the government report of 18 Mar 2026 dropped an exception with opt-out as its preferred option | Licensing, or defensible reliance on existing exceptions | [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029) | [Verified] from the [government report of 18 Mar 2026](https://www.gov.uk/government/publications/report-and-impact-assessment-on-copyright-and-artificial-intelligence/report-on-copyright-and-artificial-intelligence), read 20 Oct 2026 | Litigation; any later policy |
| UK9 | AI (Regulation) private member's bill | Not law | Would create an AI Authority and AI officers | None | [Verified] not law: [bill page](https://bills.parliament.uk/bills/3942) shows a Private Members' Bill, session 2024-26, HL Bill 76 as introduced 4 Mar 2025, no later stage, read 20 Oct 2026. The bill's content was not re-read | Parliamentary status |
| UK10 | NCSC and DSIT guidance on secure AI (guidelines for secure AI system development; AI cyber security code of practice) | Voluntary guidance | Secure design, development, deployment and operation | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) | [Verified] both exist and are voluntary: the [Code of Practice](https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice/code-of-practice-for-the-cyber-security-of-ai) (31 Jan 2025, 13 principles) cites the NCSC guidelines (Nov 2023); ETSI TS 104 223 builds on the code ([NCSC](https://www.ncsc.gov.uk/blog-post/new-etsi-standard-protects-ai-systems-from-evolving-cyber-threats)), read 20 Oct 2026 | Existence, titles, standard status |
| UK11 | Algorithmic Transparency Recording Standard (ATRS) | Public-sector standard; mandatory by policy for central government departments and in-scope arm's-length bodies; recommended for the wider public sector | Public bodies publish records of algorithmic tools | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | [Verified] scope, from the [mandatory scope and exemptions policy](https://www.gov.uk/government/publications/algorithmic-transparency-recording-standard-mandatory-scope-and-exemptions-policy/algorithmic-transparency-recording-standard-atrs-mandatory-scope-and-exemptions-policy), read 20 Oct 2026 | Whether it is mandatory for your body |
| UK12 | Equality Act 2010 | Binding | Discrimination by automated tools | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [Recalled] | Application to your use case |
| UK13 | AI Management Essentials (AIME) self-assessment tool (DSIT) | **Withdrawn draft.** Consultation draft 6 Nov 2024; the government response (dated December 2025, published 6 Feb 2026) says DSIT will not publish it | Ten-section self-assessment for organisations that develop or use AI: AI system record, AI policy, fairness, impact assessment, risk assessment, data management, bias mitigation, data protection, issue reporting, third-party communication. Not required in public procurement | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041), [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042) | [Verified] | DSIT's promised replacement guidance for SMEs |

## 3. Categories, tiers and roles

| Category / role | What it means |
|---|---|
| Controller / processor | UK GDPR roles |
| Solely automated decision | Now permitted under conditions, if the safeguards are in place [Reported] |
| Regulated firm (FCA, PRA) | Sector accountability and model risk |
| Public body | Transparency standard and public-law duties |
| No AI risk tiers | The UK has no statutory tiering; use your own ([GCC T01](../11_GCC_AI_Compliance/T01_AI_Use_Case_Intake_and_Risk_Tiering.md) or [EU T01](../12_EU_AI_Compliance/T01_AI_System_Classification.md)) |

## 4. Timeline

| Date | Event | Tag |
|---|---|---|
| Mar 2023 | White Paper sets the five principles (published 29 Mar 2023) | [Verified] |
| 2025 | Data (Use and Access) Act enacted | [Reported] |
| Mar 2025 | AI private member's bill reintroduced (HL Bill 76, 4 Mar 2025) | [Verified] |
| 6 Nov 2024 | AI Management Essentials (AIME) draft published for consultation (closed 29 Jan 2025) | [Verified] |
| 6 Feb 2026 | Government response: AIME will not be published or required in procurement | [Verified] |
| 5 Feb 2026 | Commencement of Arts 22A to 22D (section 80, SI 2026/82) | [Verified] |

## 5. Mapping of common wiki controls

| Wiki control | Regional hook |
|---|---|
| [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) Privacy | UK GDPR; automated decision safeguards in the Data (Use and Access) Act ([UK-T1](UK-T1_ADM_Safeguards_Record.md)) |
| [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) Human approval | Meaningful human involvement test |
| [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) Inventory | PRA SS1/23 for banks |
| [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) Vendor | FCA outsourcing and operational resilience [Recalled] |
| [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) Fairness | Equality Act; ICO fairness guidance |
| [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) Content safety | Online Safety Act, where applicable |
| [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029) Training data | Copyright licensing position |

## 6. Where the wiki covers this

The topics raised on this page are covered by the following controls, test cases and templates.

| Topic | Covered by |
|---|---|
| Automated decision safeguards after the 2025 change | [UK-T1](UK-T1_ADM_Safeguards_Record.md); [TC-L01-012](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-012), [TC-L03-008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008), [TC-L03-029](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-029); [TC-L03-036](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-036) |
| Financial-sector expectations (FCA, PRA) | [UK-T2](UK-T2_Regulated_Firm_AI_Checklist.md); [Sector Overlays](../04_Domain_Standards/10B_Sector_Overlays.md) |
| Public-sector transparency record | [UK-T3](UK-T3_Public_Sector_Transparency_Record.md); [TC-L03-003](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-003); [TC-L03-036](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-036) |
| Incident path (ICO within 72 hours, sector notices) | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035); [TC-L03-019](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-019); incident workflow [EU T05](../12_EU_AI_Compliance/T05_AI_Incident_and_Breach_Reporting_Workflow.md) |

## 7. Conflicts and cautions

- One source describes the position "as of 2025". Check for a government AI bill announcement in 2026.
- Arts 22A to 22D (section 80) commenced on 5 February 2026 under SI 2026/82 and do not apply to decisions taken before that date. Checked on legislation.gov.uk on 20 October 2026.
- The details of the NCSC and DSIT codes come from a single source or from memory.
- **AI Management Essentials (UK13) is withdrawn, not current.** Some third-party lists of AI governance frameworks, written before February 2026, still present AIME as a UK management standard. The government response says: "DSIT will not be publishing AIME and therefore will not be making it a requirement of the government procurement process." The reasons it gives are that the tool's scope was too broad for one instrument and that DSIT will instead write narrower guidance on foundational governance measures aimed at SMEs, and point organisations to other support. The ten sections of the 2024 draft are still a usable lightweight self-check, but do not describe AIME as a UK requirement or standard. Checked against the response PDF on 15 October 2026.

## 8. Verification checklist

- [x] Data (Use and Access) Act commencement regulations (SI 2026/82, checked 20 Oct 2026)
- [ ] ICO's current list of AI guidance
- [ ] FCA and PRA statements
- [x] Copyright position and any consultation response (report of 18 Mar 2026, checked 20 Oct 2026)
- [ ] Any government AI bill
- [ ] NCSC and DSIT secure AI documents
- [ ] Online Safety Act scope
- [ ] Add the primary URL and retrieval date beside every confirmed row

## 9. Sources

All sources are secondary unless marked as a regulator or government page. Each fetched page was summarised by a tool and was not read line by line. A source marked "not read" appeared only as a title or snippet in search results, so do not treat it as support for any claim.

| Source | Status | Rows it relates to |
|---|---|---|
| [DSIT: AI Management Essentials tool consultation page](https://www.gov.uk/government/consultations/ai-management-essentials-tool) | Government page; fetched 15 Oct 2026 | UK13 |
| [DSIT: AI Management Essentials tool, draft self-assessment (Nov 2024)](https://assets.publishing.service.gov.uk/media/672a5706094e4e60c466d19f/AI_Management_Essentials_tool_Self-Assessment.pdf) | Government document; fetched 15 Oct 2026 | UK13 |
| [DSIT: AI Management Essentials tool, government response](https://assets.publishing.service.gov.uk/media/6981d0758c1e89ed1e91bb55/AI_Management_Essentials_tool_government_response.pdf) | Government document; fetched 15 Oct 2026 | UK13 |
| [Bratby Law: UK AI regulation overview](https://bratby.law/uk-ai-regulation-overview/) | Fetched and summarised | UK1, UK3, UK4, UK5, UK7, UK8 |
| [GDPRLocal: UK AI regulation status and outlook](https://gdprlocal.com/uk-ai-act/) | Fetched and summarised (describes the status as of 2025) | UK1, UK9 |
| [RPC: UK AI regulation guide part 1](https://www.rpclegal.com/thinking/artificial-intelligence/ai-guide/part-1-uk-ai-regulation/) | Not read | Cross-check |
| [DSIT: A pro-innovation approach to AI regulation (White Paper)](https://www.gov.uk/government/publications/ai-regulation-a-pro-innovation-approach/white-paper) | Government page; fetched 20 Oct 2026 | UK1 |
| [UK Parliament: Artificial Intelligence (Regulation) Bill [HL]](https://bills.parliament.uk/bills/3942) | Parliament page; fetched 20 Oct 2026 | UK9 |
| [DSIT: Code of Practice for the Cyber Security of AI](https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice/code-of-practice-for-the-cyber-security-of-ai) | Government page; fetched 20 Oct 2026 | UK10 |
| [NCSC: New ETSI standard protects AI systems](https://www.ncsc.gov.uk/blog-post/new-etsi-standard-protects-ai-systems-from-evolving-cyber-threats) | Government page; fetched 20 Oct 2026 | UK10 |
| [legislation.gov.uk: Data (Use and Access) Act 2025, section 80](https://www.legislation.gov.uk/ukpga/2025/18/section/80/enacted) | Legislation; fetched 20 Oct 2026 | UK3 |
| [legislation.gov.uk: SI 2026/82](https://legislation.gov.uk/uksi/2026/82) | Legislation; fetched 20 Oct 2026 | UK3 |
| [DSIT and IPO: Report on Copyright and Artificial Intelligence](https://www.gov.uk/government/publications/report-and-impact-assessment-on-copyright-and-artificial-intelligence/report-on-copyright-and-artificial-intelligence) | Government page; fetched 20 Oct 2026 | UK8 |
| [GOV.UK: ATRS mandatory scope and exemptions policy](https://www.gov.uk/government/publications/algorithmic-transparency-recording-standard-mandatory-scope-and-exemptions-policy/algorithmic-transparency-recording-standard-atrs-mandatory-scope-and-exemptions-policy) | Government page; fetched 20 Oct 2026 | UK11 |
| [Scaffold Digital: UK AI regulation in 2026](https://www.scaffold.digital/news/uk-ai-regulation-in-2026-whats-in-force-whats-coming-and-what-your-business-should-do) | Not read | Cross-check |

Primary legislation was read for row UK3 only (section 80 and SI 2026/82, 20 October 2026); the other [Verified] rows rest on government or Parliament pages. Confirm each row against the primary source, and add its URL and retrieval date in the [UK Regulatory Crosswalk](03_Regulatory_Crosswalk.md).
