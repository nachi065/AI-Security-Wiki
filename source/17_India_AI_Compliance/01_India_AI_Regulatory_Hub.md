---
title: "India AI Regulatory Hub"
author: Nachiket Sathaye
parent: "India AI Compliance"
nav_order: 1
description: "Indian AI-relevant law mapped to AI security controls: the DPDP Act and Rules, MeitY AI guidelines, RBI, SEBI and IRDAI expectations, and CERT-In reporting."
document_type: AI Security Wiki Reference
version: 1.0
---

# India AI Regulatory Hub

> **Verification required.** Claims on this page about Indian law were compiled on 7 October 2026 from secondary web sources and from memory of the law. No primary legal text was read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

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
| IN1 | Digital Personal Data Protection Act 2023 | Binding; being implemented | Consent and notice, purpose limits, rights, breach notice to the Board and to individuals, children's data, duties of significant data fiduciaries, cross-border rules. Maximum penalty reported as INR 250 crore per contravention | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [Reported] | Section numbers; penalty schedule |
| IN2 | DPDP Rules 2025 | Notified 13 Nov 2025 (gazette date reported as 14 Nov); phased | Consent managers from about Nov 2026; core obligations from about 13 or 14 May 2027; the government is reportedly considering shortening the phase-in to 12 months | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [Conflict] | Exact phase dates; any shortening |
| IN3 | Data Protection Board of India | Established in law; not operational according to an Aug 2026 report | Nominations invited on 6 May and 6 June 2026; no appointments; complaint mechanism unavailable | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [Reported] | Current status |
| IN4 | India AI Governance Guidelines (MeitY) | Non-binding; 5 Nov 2025 | Seven principles: trust, human centricity, responsible innovation, fairness, accountability, understandability, safety. Six pillars, including institutions and risk mitigation | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [Reported] | Institution names; text |
| IN5 | RBI FREE-AI Committee report | Non-binding; 13 Aug 2025 | Seven sutras and 26 recommendations on responsible AI in finance | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [Reported] | Recommendation list |
| IN6 | RBI draft Guidance on Model Risk Management | Draft 24 Jun 2026; comments to 24 Jul 2026 | Model risk expectations that reach AI models | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [Reported] | Final status |
| IN7 | SEBI circulars on AI use by market intermediaries | Sector rules | Disclosure and risk management for AI in trading, advice and compliance | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [Reported] | Circular numbers and scope |
| IN8 | IRDAI: AI-cybersecurity readiness directive (May 2026); AI working group (Jun 2026) | Sector directive and policy work | Comprehensive AI guidance pending | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | [Reported] | Directive text |
| IN9 | IT Rules amendments on synthetic content labelling | Proposed or amended; reception mixed | Platforms to label AI-generated synthetic content | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [Conflict] | Whether notified; effective date; scope |
| IN10 | CERT-In incident reporting directions (2022) and AI guidance | Binding directions; AI guidance unverified | Cyber incidents to be reported within 6 hours; the figure is given from memory | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035), [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005) | [Recalled] | Hour limit; whether AI guidance exists |
| IN11 | IT Act 2000 and SPDI Rules | Existing law until the DPDP regime fully commences | Reasonable security practices for sensitive data | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | [Recalled] | Transition provisions |
| IN12 | IndiaAI Mission | Programme (Mar 2024; INR 10,372 crore) | Compute, datasets, skilling. Listed for context; it creates no obligation | None | [Reported] | n/a |

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
| 13 Aug 2025 | RBI FREE-AI report | [Reported] |
| 5 Nov 2025 | MeitY AI Governance Guidelines released | [Reported] |
| 13 Nov 2025 | DPDP Rules notified | [Reported] |
| May 2026 | IRDAI AI-cybersecurity readiness directive | [Reported] |
| 24 Jun 2026 | RBI draft Model Risk Management guidance | [Reported] |
| About Nov 2026 | Consent manager framework | [Reported] |
| About 13 or 14 May 2027 | Core DPDP obligations | [Conflict] |

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
