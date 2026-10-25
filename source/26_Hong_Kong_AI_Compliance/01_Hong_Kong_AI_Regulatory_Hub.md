---
title: "Hong Kong AI Regulatory Hub"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Hong Kong AI Compliance"
nav_order: 1
description: "Hong Kong AI guidance and law mapped to AI security controls: the HKMA guidance on responsible AI adoption, the SFC generative AI circular, PCPD guidance, the PDPO and the GenA.I. Sandbox++."
document_type: AI Security Wiki Reference
version: 1.0
last_reviewed: 2026-10-25
---

# Hong Kong AI Regulatory Hub

> **Verification required.** This page was compiled on 25 October 2026. Rows HK1, HK2, HK3, HK8 and HK9 were checked that day against the HKMA's and the government's own documents and are tagged [Verified]. Every other claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

This page maps Hong Kong guidance and law that bear on AI to the wiki's controls.

## 1. Regional model

There are three layers:

1. The Personal Data (Privacy) Ordinance (PDPO), with non-binding PCPD guidance on AI [Recalled for the PDPO; Reported for the guidance].
2. Sector supervisory guidance: the HKMA for banks [Verified] and the SFC for licensed corporations [Reported]. The Insurance Authority and the MPFA were not researched.
3. Sandboxes run jointly by the financial regulators [Verified].

The HKMA guidance says institutions remain accountable for AI outputs and actions, and for outsourced AI [Verified].

## 2. Instrument register

| # | Instrument | Type / status | Key points | Wiki controls | Tag | To verify |
|---|---|---|---|---|---|---|
| HK1 | HKMA Supervisory Guidance for Responsible Adoption of Artificial Intelligence (Annex A to the HKMA circular of 15 Oct 2026; the "ART" framework) | Guidance. Supervisory expectations for authorized institutions, applied proportionately. No deadline: institutions should uplift policies, procedures and controls "in a timely manner" | Nine principles under Accountability, Resilience and Trust: (1) the board approves an AI strategy with the approach and risk appetite, and governance spans the three lines; (2) a named owner for each use case, and human-in-the-loop, on-the-loop or in-command oversight with authority to challenge, override or stop; (3) an up-to-date inventory of approved use cases including third-party and embedded AI, with unlisted AI restricted and shadow AI controlled; (4) materiality and risk assessment that sets the review depth, with independent validation and a kill switch or equivalent for material or higher-risk use cases, fallback and recovery, and auditable records; (5) data, third-party and cyber risk, including contracts that stop providers reusing data for training without authorisation; (6) resources and training; (7) accountability for outputs, including hallucination controls; (8) explainability; (9) fair treatment, redress and telling consumers about AI use and its risks before service | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045), [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [Verified] | The circular's reference number; the companion report on the second GenAI Sandbox cohort |
| HK2 | HKMA High-level Principles on Artificial Intelligence (1 Nov 2019) | Superseded by HK1 | Replaced by the guidance of 15 Oct 2026, which says it supersedes them | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | [Verified] | Whether the HKMA register still lists the 2019 circular as current (one secondary source says it did on 19 Oct 2026) |
| HK3 | HKMA circular: Consumer Protection in respect of Use of Generative Artificial Intelligence (19 Aug 2024) | Guidance | Advised human-in-the-loop oversight in the early stage of customer-facing generative AI. HK1 (footnote 3) now accepts that human-on-the-loop or human-in-command may suit some use cases, and says institutions may still follow this circular for customer-facing applications | [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [Verified] (as described in HK1) | The circular's own text |
| HK4 | HKMA consumer protection circular on big data analytics and AI (5 Nov 2019) | Guidance | Consumer protection expectations for AI-based products and services. HK1 says existing disclosure and opt-out expectations continue to apply | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [Reported] | Title, date and text |
| HK5 | SFC circular to licensed corporations on generative AI language models (12 Nov 2024) | Guidance; reported as effective immediately | Four core principles: senior management responsibilities; AI model risk management; cybersecurity and data risk management; third-party provider risk management. Investment recommendations, advice or research to clients are treated as high-risk by default. A licensed corporation reportedly must notify the SFC before using such models in high-risk use cases | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034), [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | [Reported] | The circular text, and whether the SFC has updated it |
| HK6 | PCPD Artificial Intelligence: Model Personal Data Protection Framework (11 Jun 2024) | Guidance; not law | Four areas: AI strategy and governance; risk assessment and human oversight; customisation of AI models and implementation and management of AI systems; communication and engagement with stakeholders. Aimed at organisations that buy, deploy and operate AI that handles personal data | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045) | [Reported] | The framework text |
| HK7 | Personal Data (Privacy) Ordinance (Cap. 486) | Binding law | Data protection principles apply to personal data used in AI. HK1 requires compliance with the PDPO in AI data governance | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) | [Recalled] | Provisions relevant to AI |
| HK8 | GenA.I. Sandbox++ (HKMA, SFC, Insurance Authority and MPFA, with Cyberport; announced 5 Mar 2026) | Programme | Extends the 2024 HKMA GenA.I. Sandbox to banking, securities, asset and wealth management, insurance, MPF and stored value facilities. Participants get supervisory guidance, technical support and computing at Cyberport | None | [Verified] | Cohort dates |
| HK9 | HKMA discussion paper on agentic AI governance | Proposed; announced on 15 Oct 2026 and not yet published | To explore a registry of material AI agents, intent-anchored accountability and mechanisms for effective intervention | [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) | [Verified] (announcement only) | Publication and content |

## 3. Categories, tiers and roles

| Category / role | What it means |
|---|---|
| Authorized institution (bank) | HK1 applies, in proportion to the institution's use of AI [Verified] |
| Licensed corporation (securities) | HK5 applies to the use of generative AI language models [Reported] |
| Material or higher-risk use case | Under HK1, needs senior management sign-off, independent validation, adversarial testing where appropriate, a kill switch or equivalent, and outcome tracing records [Verified] |
| High-risk use case (SFC) | Investment recommendations, advice or research using generative AI; stricter controls and notification [Reported] |
| Data user | PDPO duties for personal data [Recalled] |

## 4. Timeline

| Date | Event | Tag |
|---|---|---|
| 1 Nov 2019 | HKMA High-level Principles on AI | [Verified] |
| 5 Nov 2019 | HKMA consumer protection circular on big data analytics and AI | [Reported] |
| 11 Jun 2024 | PCPD Model Personal Data Protection Framework for AI | [Reported] |
| 19 Aug 2024 | HKMA circular on consumer protection and generative AI | [Verified] |
| 12 Nov 2024 | SFC circular on generative AI language models | [Reported] |
| 5 Mar 2026 | GenA.I. Sandbox++ announced by four financial regulators | [Verified] |
| 15 Oct 2026 | HKMA issues the Supervisory Guidance for Responsible Adoption of AI (the ART framework), superseding the 2019 principles; announces a discussion paper on agentic AI | [Verified] |

## 5. Mapping of common wiki controls

| Wiki control | Regional hook |
|---|---|
| [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) AI policy and roles | HK1 principle 1: board-approved AI strategy and risk appetite; HK5 senior management responsibilities |
| [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) Inventory and tiering | HK1 principle 3: inventory of approved use cases, unlisted AI restricted; principle 4: materiality and risk assessment |
| [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045) Human oversight | HK1 principle 2: in-the-loop, on-the-loop or in-command, with authority to override or stop |
| [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) Kill switch | HK1 principle 4: a kill switch or equivalent for material or higher-risk use cases |
| [AI-CTRL-040](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-040) Resilience | HK1 principle 4: fallback and recovery, including for third-party failures |
| [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) Third-party AI | HK1 principle 5: due diligence, contracts, concentration and exit risk; HK5 third-party provider risk |
| [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005) Runtime security | HK1 principle 5: layered controls against data poisoning and prompt injection, not only model instructions or filters |
| [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) Output reliability | HK1 principle 7: hallucination controls and thresholds for withholding outputs |
| [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) Fairness, explainability and disclosure | HK1 principles 8 and 9; HK3 and HK4 |
| [AI-CTRL-044](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-044) Competence | HK1 principle 6 |
| [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) Privacy | PDPO and the PCPD framework |

## 6. Where the wiki covers this

| Topic | Covered by |
|---|---|
| HKMA guidance, principle by principle | [Principle crosswalk](03_Regulatory_Crosswalk.md#hkma-guidance-on-responsible-ai-adoption-principle-crosswalk); [HK-T1](HK-T1_HKMA_ART_Principles_Self_Assessment.md) |
| Inventory and materiality | [SG-T2](../19_Singapore_AI_Compliance/SG-T2_MAS_Style_Inventory_and_Materiality.md), whose attributes are close to HK1 principle 3; [TC-L01-001](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-001), [TC-L01-008](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-008) |
| Kill switch for high-risk AI | [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025); [TC-L01-021](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-021) |
| Financial-sector comparison | [Financial Regulator AI Comparison](../04_Domain_Standards/10C_Financial_Regulator_AI_Comparison.md); [Sector Overlays](../04_Domain_Standards/10B_Sector_Overlays.md) |

## 7. Conflicts and cautions

- HK1 is supervisory guidance with no fixed deadline. Confirm with your own advisers how the HKMA will assess it.
- One secondary source says the HKMA register still listed the 2019 principles as current on 19 October 2026, although HK1 says it supersedes them.
- The SFC and PCPD rows rest on law-firm summaries only.

## 8. Verification checklist

- [x] HKMA guidance of 15 October 2026 (read 25 October 2026)
- [ ] HKMA circular reference number for HK1
- [ ] SFC circular of 12 November 2024: text and any update
- [ ] PCPD Model Personal Data Protection Framework: text
- [ ] PDPO provisions relevant to AI
- [ ] HKMA 2019 consumer protection circular: title and text
- [ ] Insurance Authority and MPFA AI guidance
- [ ] HKMA agentic AI discussion paper, when published

## 9. Sources

All sources are secondary unless marked as a regulator or government page. Each fetched page was summarised by a tool and was not read line by line.

| Source | Status | Rows it relates to |
|---|---|---|
| [HKMA: Supervisory Guidance for Responsible Adoption of Artificial Intelligence (Annex A)](https://brdr.hkma.gov.hk/eng/doc-ldg/docId/getPdf/20261015-2-EN/20261015-2-EN.pdf) | Regulator document, read 25 Oct 2026 | HK1, HK2, HK3, HK4 |
| [HKMA: press release on the ART Framework, 15 Oct 2026](https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261015-3/) | Regulator page, read 25 Oct 2026 | HK1, HK9 |
| [Hong Kong Government: GenA.I. Sandbox++ launch, 5 Mar 2026](https://www.info.gov.hk/gia/general/202603/05/P2026030500251.htm) | Government page, read 25 Oct 2026 | HK8 |
| [RegReportingDesk: HKMA ART Framework](https://regreportingdesk.com/hkma-art-framework-responsible-ai-guidance/) | Fetched and summarised | HK1, HK2, HK4 |
| [Clifford Chance: SFC circular on generative AI](https://cliffordchance.com/insights/resources/blogs/talking-tech/en/articles/2024/11/sfc-circular-to-licensed-corporations-on-use-of-generative-ai.html) | Fetched and summarised | HK5 |
| [Mayer Brown: PCPD Model Personal Data Protection Framework](https://www.mayerbrown.com/en/insights/publications/2024/06/hong-kong-pcpd-issues-model-personal-data-protection-ai-framework) | Fetched and summarised | HK6 |

Confirm each row against its primary source, and add its URL and retrieval date in the [Hong Kong Regulatory Crosswalk](03_Regulatory_Crosswalk.md).
