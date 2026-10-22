---
title: "India AI Regulatory Hub"
author: Nachiket Sathaye
parent: "India AI Compliance"
nav_order: 1
description: "Indian AI-relevant law mapped to AI security controls: the DPDP Act and Rules, MeitY AI guidelines, RBI, SEBI and IRDAI expectations, and CERT-In reporting."
document_type: AI Security Wiki Reference
version: 1.0
last_reviewed: 2026-10-20
---

# India AI Regulatory Hub

> **Verification status.** On 16 October 2026 the rows tagged [Verified] (IN1, IN2, IN4, IN5, IN6, IN10), and on 20 October 2026 row IN12, were checked against primary documents; the crosswalk gives each source and what was and was not read. Everything else was compiled on 7 October 2026 from secondary sources or memory and is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any claim. This is not legal advice.

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
| IN3 | Data Protection Board of India | Established in law; not operational according to an Aug 2026 report | Nominations invited on 6 May and 6 June 2026; no appointments; complaint mechanism unavailable | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [Reported] | Current status (not re-checked on 16 Oct 2026) |
| IN4 | India AI Governance Guidelines (MeitY) | Non-binding; the document is undated; release reported as 5 Nov 2025 | Seven sutras: Trust is the Foundation; People First; Accountability; Fairness and Equity; Innovation over Restraint; Understandable by Design; Safety, Resilience and Sustainability. Six pillars: Infrastructure, Capacity Building, Policy and Regulation, Risk Mitigation, Accountability, Institutions. Proposes an AI Governance Group and a Technology and Policy Expert Committee; describes the AI Safety Institute as established. States that a separate AI law is not needed at this stage | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [Verified] | Release date (the document itself is undated) |
| IN5 | RBI FREE-AI Committee report | Committee report published by the RBI on 13 Aug 2025; not a binding direction | Seven sutras and 26 recommendations under six pillars (infrastructure, policy, capacity, governance, protection, assurance) | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [Verified] | The text of each recommendation; whether the RBI has adopted any of them as directions |
| IN6 | RBI draft Guidance on Model Risk Management | Draft issued 24 Jun 2026; comments to 24 Jul 2026 | Draft Guidance on Regulatory Principles for Model Risk Management. Applies to banks, NBFCs, asset reconstruction companies, credit information companies and other listed regulated entity types, and to all models they use including third-party models and models using AI or machine learning | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [Verified] | Final status (not re-checked on 16 Oct 2026) |
| IN7 | SEBI regulations on AI and ML tools used by regulated entities | Amendments to the Intermediaries Regulations 2008 and the Securities Contracts (Regulation) (Stock Exchanges and Clearing Corporations) Regulations 2018; reported as notified 6 Feb 2025 | Regulated entities are solely responsible for the privacy, security and integrity of data, for the output of the AI and ML tools they use, and for legal compliance. The primary document read was the SEBI Board memorandum of Dec 2024, which proposed this; the notification itself was not read | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [Reported] | SEBI's notified text and gazette date; any later SEBI AI guidance |
| IN8 | IRDAI: AI-cybersecurity readiness directive (May 2026); AI working group (Jun 2026) | Not confirmed | A document titled IRDAI Information and Cybersecurity Guidelines, 2026 is listed on the IRDAI site. It could not be read, so whether an AI-specific directive of May 2026 exists is not confirmed | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | [Unverified] | Whether any IRDAI instrument addresses AI, and its text |
| IN9 | IT Rules amendments on synthetic content labelling | Reported as notified 10 Feb 2026 and in force from 20 Feb 2026 (amendment rules to the IT Rules 2021) | Intermediaries that offer tools to create synthetic content must label it prominently and embed provenance metadata; significant social media intermediaries must obtain and check user declarations; takedown deadlines are shorter, for example 3 hours after a court order or an authorised officer's intimation | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [Reported] | Gazette text, G.S.R. number and exact scope (law-firm sources agree but the gazette was not read) |
| IN10 | CERT-In incident reporting directions (2022) and AI guidance | Binding directions of 28 Apr 2022 (No. 20(3)/2022-CERT-In) under section 70B(6) of the IT Act | Listed cyber incidents must be reported to CERT-In within 6 hours; the directions took effect 60 days after issue; the list of reportable incidents includes attacks or suspicious activity related to AI and ML systems | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035), [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005) | [Verified] | Whether CERT-In has issued separate AI-specific guidance |
| IN11 | IT Act 2000 and SPDI Rules | Existing law until the DPDP regime fully commences | Reasonable security practices for sensitive data | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | [Recalled] | Transition provisions |
| IN12 | IndiaAI Mission | Programme (Mar 2024; INR 10,372 crore) | Compute, datasets, skilling. Listed for context; it creates no obligation | None | [Verified] date and outlay, from the [PIB release of 7 Mar 2024](https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2012355) (Rs 10,371.92 crore), read 20 Oct 2026 | n/a |

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
| 13 Aug 2025 | RBI FREE-AI report | [Verified] |
| 5 Nov 2025 | MeitY AI Governance Guidelines released (date reported; the document is undated) | [Reported] |
| 13 Nov 2025 | DPDP Rules notified (G.S.R. 846(E); PIB announcement 14 Nov) | [Verified] |
| 10 Feb 2026 | IT Rules amendment on synthetic content, in force 20 Feb 2026 (as reported) | [Reported] |
| May 2026 | IRDAI AI-cybersecurity readiness directive | [Unverified] |
| 24 Jun 2026 | RBI draft Model Risk Management guidance | [Verified] |
| About 13 Nov 2026 | Consent manager rule (Rule 4) in force, one year after publication | [Verified] |
| About 13 May 2027 | Core DPDP obligations (Rules 3, 5 to 16, 22, 23), eighteen months after publication | [Verified] |

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
- The synthetic content labelling rules are described both as proposed and as amended.
- One source says the Board was not operational as of August 2026, so the enforcement route is uncertain.
- The penalty and section detail comes from a single vendor blog.

## 8. Verification checklist

- [ ] DPDP Act section numbers for notice, consent, breach, children, significant data fiduciary and cross-border transfer
- [ ] Rules phase dates and any change
- [ ] Board constitution
- [ ] MeitY guidelines text and institutions
- [ ] The 26 RBI FREE-AI recommendations
- [ ] RBI model risk guidance, final version
- [ ] List of SEBI circulars
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
