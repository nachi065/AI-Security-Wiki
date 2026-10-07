---
title: "US AI Regulatory Hub"
author: Nachiket Sathaye
parent: "US AI Compliance"
nav_order: 1
description: "US AI-relevant law mapped to AI security controls: federal executive orders and enforcement, NIST AI RMF, and state laws in California, Colorado, Texas and Illinois."
document_type: AI Security Wiki Reference
version: 1.0
---

# US AI Regulatory Hub

> **Verification required.** Claims on this page about US law were compiled on 7 October 2026 from secondary web sources and from memory of the law. No primary legal text was read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

This page maps US laws, guidance and standards that bear on AI to the wiki's controls.

## 1. Regional model

There are four layers:

1. Federal executive policy, and agency enforcement under existing statutes by the FTC, EEOC, CFPB, FDA and the banking regulators [Recalled].
2. State AI and privacy laws (California, Texas, Colorado, Illinois, New York and others).
3. Sector rules for health, finance and employment.
4. The NIST AI RMF, a voluntary standard that some state laws recognise.

Apply the law of the strictest state you operate in.

## 2. Instrument register

| # | Instrument | Type / status | Key points | Wiki controls | Tag | To verify |
|---|---|---|---|---|---|---|
| US1 | Federal AI legislation | None comprehensive | In July 2025 the Senate voted 99 to 1 to strip a 10-year moratorium on state AI laws from the budget act; no preemption has been enacted | None | [Reported] | New bills |
| US2 | Executive Order 14365 (Dec 2025) | Executive policy | Declares a minimally burdensome national standard; sets up a DOJ AI Litigation Task Force (by 10 Jan 2026); orders a Commerce review of state laws. No complaints had been filed as of Mar 2026, and no court has struck down a state AI law | None | [Reported] | Later litigation |
| US3 | Executive Order 14409 (2 Jun 2026) and the national-security memo of 5 Jun | Executive policy | Voluntary pre-release review of frontier models (30 days); voluntary AI cyber clearinghouse; bans mandatory federal licensing | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005) | [Reported] | Text and numbers |
| US4 | NIST AI Risk Management Framework 1.0 | Voluntary | Govern, map, measure, manage. Colorado reportedly gives a rebuttable presumption to programmes aligned with it | Whole library | [Reported] | Colorado text after the rewrite |
| US5 | Colorado: SB 24-205, repealed and reenacted by SB 26-189 (signed 14 May 2026) | State law | Reframed around automated decision-making technology; the core developer and deployer duties moved to 1 Jan 2027 | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [Conflict] | Older trackers still show 30 Jun 2026 |
| US6 | California: SB 53 frontier AI transparency; AB 2013 training data transparency | State law; 1 Jan 2026 | SB 53 applies to developers above 10^26 FLOP and USD 500M in revenue; AB 2013 requires training data disclosure | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038), [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029) | [Reported] | Thresholds; text |
| US7 | California AI Transparency Act (SB 942 as amended) | State law; operative 2 Aug 2026 (reported) | Provenance, detection and disclosure duties; platform and hosting phases in 2027 | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [Reported] | Bill number; scope |
| US8 | California CCPA regulations on automated decision-making technology (ADMT), risk assessments and cybersecurity audits | Binding regulation; approved by the Office of Administrative Law on 22 Sep 2025, effective 1 Jan 2026 (CPPA page) | ADMT means technology that processes personal information and uses computation to replace or substantially replace human decision-making. Significant decisions cover financial or lending services, housing, education, employment and healthcare; advertising is excluded. Duties: pre-use notice, two or more opt-out methods (with limited exceptions), and access to ADMT logic and outcomes. Reviewers must be able to understand and alter outputs. ADMT compliance is due by 1 Jan 2027 for existing uses, and on adoption for later uses. Risk assessments: documentation by 31 Dec 2027 for ongoing activities that began before 2026; submission to the agency by 1 Apr 2028 for assessments from 2026 and 2027. Cybersecurity audits are staggered: 1 Apr 2028 (over USD 100M in revenue), 2029 (USD 50M to 100M), 2030 (under USD 50M) | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [Reported] | The approval and effective dates come from the CPPA page; the other details come from law-firm summaries. Read the approved text for definitions, exceptions and thresholds |
| US9 | Texas TRAIGA (HB 149) | State law; 1 Jan 2026 | Applies to developers and deployers that reach Texas residents; complaint mechanism due 1 Sep 2026 | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | [Reported] | Obligations list; enforcement |
| US10 | Illinois HB 3773 | State law; 1 Jan 2026 | Employer use of AI in employment decisions; a private right of action is reported | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | [Reported] | Scope |
| US11 | NYC Local Law 144; NY RAISE Act; Utah SB 149 | Local and state | Local Law 144 requires bias audits of hiring tools; the RAISE Act is targeted for 2027 and covers frontier developers; Utah requires disclosure | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [Reported] | Dates |
| US12 | FTC Act s.5; EEOC and anti-discrimination law; ECOA adverse action; HIPAA; FDA for medical AI; bank model risk (SR 11-7) | Existing federal law | Enforcement against deceptive AI claims and unfair outcomes; sector rules apply to AI | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [Recalled] | Current enforcement and guidance |
| US13 | State legislative volume | Context | 1,208 AI bills were introduced and 145 enacted across 38 states in 2025 | None | [Reported] | Figures |

## 3. Categories, tiers and roles

| Category / role | What it means |
|---|---|
| Developer | Builds or substantially modifies AI; state laws often put documentation duties here |
| Deployer | Uses AI for decisions; several states impose notice, assessment and appeal duties |
| High-risk or consequential decision (state definitions) | Employment, credit, housing, healthcare, education, legal services, insurance [Reported for Colorado] |
| Frontier developer | Very large models; transparency and incident duties in California, and proposed in New York |
| Regulated entity | Banks, insurers and health providers under sector rules |

## 4. Timeline

| Date | Event | Tag |
|---|---|---|
| Jul 2025 | Senate strips the preemption moratorium | [Reported] |
| 22 Sep 2025 | California ADMT, risk assessment and cybersecurity audit regulations approved | [Reported] |
| Dec 2025 | Executive Order 14365 | [Reported] |
| 1 Jan 2026 | California SB 53 and AB 2013, Texas TRAIGA and Illinois HB 3773 take effect | [Reported] |
| 14 May 2026 | Colorado SB 26-189 signed | [Reported] |
| 2 Jun 2026 | Executive Order 14409 | [Reported] |
| 2 Aug 2026 | California AI Transparency Act operative | [Reported] |
| 1 Sep 2026 | Texas complaint mechanism due | [Reported] |
| 1 Jan 2027 | Colorado core duties; California ADMT compliance date for existing uses | [Reported] |
| 2027 | NY RAISE Act targeted | [Reported] |
| 31 Dec 2027 and 1 Apr 2028 | California risk assessment documentation and submission | [Reported] |

## 5. Mapping of common wiki controls

| Wiki control | Regional hook |
|---|---|
| [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) Inventory and tiering | State definitions of consequential decisions ([US-T1](US-T1_State_Applicability_Matrix.md)) |
| [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) Privacy | State privacy laws and ADMT rules |
| [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) Risk assessment | NIST AI RMF; Colorado reasonable-care presumption |
| [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) Fairness | Employment, credit and civil rights law ([US-T2](US-T2_Consequential_Decision_Impact_Assessment.md)) |
| [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) Content safety and provenance | California AI Transparency Act ([US-T3](US-T3_GenAI_Provenance_and_Transparency_Checklist.md)) |
| [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) Audit evidence | Documentation to answer FTC or state attorney general inquiries |
| [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) Incident response | State breach laws [Recalled]; SB 53 incident reporting [Unverified] |

## 6. Where the wiki covers this

The topics raised on this page are covered by the following controls, test cases and templates.

| Topic | Covered by |
|---|---|
| State-by-state applicability | [US-T1](US-T1_State_Applicability_Matrix.md); [TC-L02-020](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-020), [TC-L03-030](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-030); [TC-L03-037](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-037) |
| Employment and credit discrimination | [US-T2](US-T2_Consequential_Decision_Impact_Assessment.md); [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041); [TC-L03-008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008), [TC-L03-029](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-029); [TC-L03-031](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-031), [TC-L03-032](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-032) |
| Provenance and disclosure under California law | [US-T3](US-T3_GenAI_Provenance_and_Transparency_Checklist.md); [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039); [TC-L03-003](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-003); [TC-L03-035](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-035) |
| NIST AI RMF as evidence of reasonable care | The [control library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md) cites NIST AI RMF subcategories for every control; [TC-L02-003](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-003) tests the multi-framework crosswalk |

## 7. Conflicts and cautions

- Colorado: SB 26-189 gives 1 January 2027, and older trackers show 30 June 2026. The newer report is more likely to be right, but confirm it.
- The approval and effective dates of the California CCPA regulations come from the CPPA page. The other details come from law-firm summaries and were not checked against the approved text.
- Federal preemption has been proposed and is not law. Do not drop state compliance on the strength of an executive order.
- Several effective dates come from tracker sites of mixed quality.

## 8. Verification checklist

- [ ] Colorado SB 26-189 text and rulemaking
- [ ] California SB 53, AB 2013 and AI Transparency Act text and dates
- [ ] Texas TRAIGA duties
- [ ] Illinois HB 3773 scope
- [ ] Approved text of the CCPA ADMT regulations (definitions, exceptions, thresholds)
- [ ] Text of Executive Orders 14365 and 14409
- [ ] Pending federal bills
- [ ] Current NYC Local Law 144 rules
- [ ] Sector guidance relevant to your clients
- [ ] Add the primary URL and retrieval date beside every confirmed row

## 9. Sources

All sources are secondary unless marked as a regulator or government page. Each fetched page was summarised by a tool and was not read line by line. A source marked "not read" appeared only as a title or snippet in search results, so do not treat it as support for any claim.

| Source | Status | Rows it relates to |
|---|---|---|
| [Cloud Security Alliance: US AI regulation, preemption and compliance](https://labs.cloudsecurityalliance.org/research/csa-research-note-us-ai-regulation-preemption-compliance-202/) | Fetched and summarised | US1, US2, US4, US6, US9, US10, US11, US13 |
| [Vorp Labs: July 2026 US AI regulatory update](https://vorplabs.com/ai-regulatory-updates/united-states/2026-07/federal-ai-orders-colorado-admt-reset) | Fetched and summarised | US3, US5, US7, US9 |
| [Layer3 Labs: AI law and compliance tracker](https://www.layer3labs.io/guides/ai-law-compliance-tracker) | Fetched and summarised (out of date on Colorado) | US3, US6, US11 cross-check |
| [California Privacy Protection Agency: CCPA updates](https://cppa.ca.gov/regulations/ccpa_updates.html) | Fetched and summarised (regulator page) | US8: approved 22 Sep 2025, effective 1 Jan 2026 |
| [MoFo: CCPA regulations on cybersecurity, risk assessments, ADMT](https://www.mofo.com/resources/insights/251007-ccpa-regulations-on-cybersecurity-risk-assessments) | Fetched and summarised | US8 definitions and dates |
| [Hunton: CPPA finalises CCPA regulations on ADMT](https://www.hunton.com/privacy-and-information-security-law/cppa-finalizes-ccpa-regulations-on-automated-decision-making-technology-risk-assessments-and-cybersecurity-audits) | Fetched and summarised | US8 compliance dates |
| [Carpe Datum: Colorado's AI reset (May 2026)](https://www.carpedatumlaw.com/2026/05/colorados-ai-reset-two-weeks-a-white-house-callout-and-a-pivot-away-from-the-eu-model/) | Not read; the fetch failed on redirects | US5 context |
| [Paul Hastings: Executive order challenging state AI laws](https://www.paulhastings.com/insights/client-alerts/president-trump-signs-executive-order-challenging-state-ai-laws) | Not read | US2 cross-check |
| [Clark Hill: Trump AI executive order and Colorado](https://www.clarkhill.com/news-events/news/what-does-trumps-ai-executive-order-mean-for-colorados-ai-act/) | Not read | US2, US5 cross-check |
| [Intellisee: Colorado AI Act repeal briefing](https://intellisee.com/intelligence/colorado-ai-act-sb-24-205-repeal-2026-compliance-briefing/) | Not read | US5 cross-check |
| [CASRAI: federal AI preemption fight](https://casrai.org/news/federal-ai-moratorium-state-preemption-fight-2026) | Not read | US1, US2 cross-check |

No primary legal text (statute, regulation or circular) was read for any row. Confirm each row against the primary source, and add its URL and retrieval date in the [US Regulatory Crosswalk](03_Regulatory_Crosswalk.md).
