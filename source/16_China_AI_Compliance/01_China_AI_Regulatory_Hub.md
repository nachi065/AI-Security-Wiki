---
title: "China AI Regulatory Hub"
author: Nachiket Sathaye
parent: "China AI Compliance"
nav_order: 1
description: "Chinese AI measures mapped to AI security controls: generative AI, algorithm recommendation, deep synthesis, content labelling, ethics review, and the PIPL and data laws."
document_type: AI Security Wiki Reference
version: 1.0
---

# China AI Regulatory Hub

> **Verification required.** Claims on this page about Chinese law were compiled on 7 October 2026 from secondary web sources and from memory of the law. No primary legal text was read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

This page maps Chinese laws, guidance and standards that bear on AI to the wiki's controls. It covers mainland China.

## 1. Regional model

There are four layers:

1. Foundation laws: the Cybersecurity Law (with a 2025 amendment that adds AI provisions), the Data Security Law (DSL) and the Personal Information Protection Law (PIPL).
2. Service-specific AI measures, administered mainly by the Cyberspace Administration of China (CAC).
3. Mandatory national standards such as GB 45438-2025.
4. Sector regulators (MIIT, SAMR, MPS).

Public-facing services face filing and assessment steps. Internal enterprise use faces fewer AI-specific measures, but the PIPL and the DSL still apply [Recalled].

## 2. Instrument register

| # | Instrument | Type / status | Key points | Wiki controls | Tag | To verify |
|---|---|---|---|---|---|---|
| CN1 | Interim Measures for the Management of Generative AI Services (2023) | Binding administrative measures | Training data governance, content review and complaint handling for publicly available services | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | [Reported] | Filing duties; thresholds |
| CN2 | Provisions on Algorithm Recommendation (2022) | Binding | Algorithm filing and security assessment for services with public opinion attributes; transparency; opt-out | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | [Reported] | Filing process |
| CN3 | Provisions on Deep Synthesis (2023) | Binding | Real-name verification, content management, identification of synthetic content | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [Reported] | Scope |
| CN4 | Measures for labelling AI-generated content; mandatory standard GB 45438-2025 | Binding; effective 1 Sep 2025 | Dual labelling: visible labels and metadata identifiers | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [Reported] | Exact measure title and obligations |
| CN5 | AI ethics review measures | Effective March 2026 | Two-tier review: internal ethics committees, plus external expert review for high-risk activities such as behavioural influence and public opinion models | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [Reported] | Official title; scope |
| CN6 | Rules for anthropomorphic (emotional companion) AI services | Effective July 2026 | AI disclosure, dependency safeguards, protection of minors, bans on encouraging self-harm or manipulation | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | [Reported] | Official title; scope |
| CN7 | Cybersecurity Law (2025 amendment with AI provisions); Data Security Law; PIPL | Binding | Network security, data classification, personal information duties, cross-border data rules | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [Reported] | Amendment effective date; transfer mechanisms |
| CN8 | Comprehensive AI law | In the 2026 legislative work plan; not enacted | The State Council plan calls for faster work on comprehensive AI legislation | None | [Reported] | Draft text |
| CN9 | Regulators: CAC, MIIT, SAMR, MPS | Authorities | The CAC is the principal AI regulator | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | [Reported] | Contact points |

## 3. Categories, tiers and roles

| Category / role | What it means |
|---|---|
| Service provider (public-facing) | Primary duty holder for filings, content review and labelling |
| Technical supporter / platform | Duties around deep synthesis and distribution |
| Internal enterprise use | Fewer AI-specific measures; the PIPL and the DSL apply [Recalled] |
| High-risk ethics review activities | Subject to two-tier review (CN5) |
| Anthropomorphic services | Separate rules from July 2026 |

## 4. Timeline

| Date | Event | Tag |
|---|---|---|
| 2022 | Algorithm recommendation provisions | [Reported] |
| 2023 | Generative AI and deep synthesis measures | [Reported] |
| 1 Sep 2025 | Content labelling measures and GB 45438-2025 | [Reported] |
| Mar 2026 | AI ethics review measures | [Reported] |
| Jul 2026 | Anthropomorphic AI rules | [Reported] |
| 2026 | Comprehensive AI law on the legislative plan | [Reported] |

## 5. Mapping of common wiki controls

| Wiki control | Regional hook |
|---|---|
| [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) Policy | Ethics review committee ([CN-T3](CN-T3_Ethics_Review_Committee_Record.md)) |
| [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) Content safety | Content review, labelling ([CN-T2](CN-T2_Content_Labelling_Implementation_Record.md)), anthropomorphic rules |
| [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) Privacy | PIPL; deep synthesis consent rules [Recalled] |
| [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007) Data sovereignty | DSL and cross-border data rules |
| [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) Inventory | Filing registers ([CN-T1](CN-T1_Filing_and_Registration_Readiness.md)) |
| [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005) Security | Cybersecurity Law and standards |
| [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) Incident response | Reporting duties under the Cybersecurity Law [Recalled] |

## 6. Where the wiki covers this

The topics raised on this page are covered by the following controls, test cases and templates.

| Topic | Covered by |
|---|---|
| Filing and registration readiness | [CN-T1](CN-T1_Filing_and_Registration_Readiness.md); [TC-L02-020](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-020), [TC-L03-026](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-026); [AI-CTRL-043](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-043); [TC-L03-039](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-039) |
| Labelling of AI-generated content | [CN-T2](CN-T2_Content_Labelling_Implementation_Record.md); [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039); [TC-L03-003](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-003); [TC-L03-035](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-035) |
| Ethics review committee | [CN-T3](CN-T3_Ethics_Review_Committee_Record.md); [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012); [TC-L02-005](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-005) tests the governance committee workflow and decision record |
| Data localisation and cross-border transfer | [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007); [TC-L03-012](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-012), [TC-L03-013](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-013), [TC-L03-014](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-014); transfer record [EU T04](../12_EU_AI_Compliance/T04_Data_Location_and_Transfer_Record.md) |

## 7. Conflicts and cautions

- The measure titles and some of the effective dates come from a single law-guide page.
- The filing thresholds and processes are given from memory and were not verified.
- Rules change quickly. A measure may have been replaced after the source was written.

## 8. Verification checklist

- [ ] Official titles and effective dates of CN4 to CN6
- [ ] Cybersecurity Law amendment text
- [ ] Filing and security assessment requirements by service type
- [ ] GB 45438-2025 technical requirements
- [ ] Cross-border data transfer rules
- [ ] Comprehensive AI law drafts
- [ ] Add the primary URL and retrieval date beside every confirmed row

## 9. Sources

All sources are secondary unless marked as a regulator or government page. Each fetched page was summarised by a tool and was not read line by line. A source marked "not read" appeared only as a title or snippet in search results, so do not treat it as support for any claim.

| Source | Status | Rows it relates to |
|---|---|---|
| [Legal 500: Topics and regulatory trends in China's AI governance](https://www.legal500.com/guides/hot-topic/topics-and-regulatory-trends-in-chinas-ai-governance/) | Fetched and summarised | CN1 to CN9 |
| [DLA Piper: Artificial intelligence in China](https://intelligence.dlapiper.com/artificial-intelligence?c=CN) | Not read | Cross-check |
| [Hogan Lovells AI hub: China](https://digital-client-solutions.hoganlovells.com/resources/ai-hub/jurisdiction/china) | Not read | Cross-check |
| [Han Kun publication (Sept 2026, PDF)](https://hankunlaw.com/upload/portal/20260911/33f09b56e7a5e07d6a817a4b1d927f56.pdf) | Not read | Latest measures; read it before relying on CN4 to CN6 |

No primary legal text (statute, regulation or circular) was read for any row. Confirm each row against the primary source, and add its URL and retrieval date in the [China Regulatory Crosswalk](03_Regulatory_Crosswalk.md).
