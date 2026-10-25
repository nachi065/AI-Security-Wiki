---
title: "Financial Regulator AI Comparison"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Domain Standards"
nav_order: 8
description: "MAS, RBI, SEBI, the EU AI Act, the FCA and the HKMA compared on eight themes for AI in financial services, with the strictest version of each and the wiki control that meets it."
document_type: AI Security Wiki Reference
version: 1.0
last_reviewed: 2026-10-25
---

# Financial Regulator AI Comparison

> **Verification required.** Compiled on 25 October 2026. Each cell carries the tag of its source row in the regional section it links to: **[Verified]** was checked against the regulator's own document, **[Reported]** comes from secondary sources and **[Recalled]** is from memory. Several of these instruments changed in October 2026 and more are expected, including SEBI's guidelines and the final RBI model risk guidance. This is not legal advice.

Financial firms that work in several markets often ask whether they need a separate AI programme for each regulator. On the eight themes below, most of these regulators ask for the same things, so one programme can be built to the strictest version of each. The last table names that version and the wiki control that meets it. Use the [Sector Overlays](10B_Sector_Overlays.md) for the wider list of financial-services expectations, including the CBUAE, APRA, OSFI and US model risk guidance.

## The six instruments

| Regulator | Instrument | Legal force | Timing | Detail |
|---|---|---|---|---|
| MAS (Singapore) | Guidelines on Artificial Intelligence Risk Management, 7 Oct 2026 | Guidance (supervisory expectations) | Sections 3 and 4 from 7 Oct 2027; Sections 5 and 6 by 7 Oct 2028 [Verified] | [Paragraph crosswalk](../19_Singapore_AI_Compliance/03_Regulatory_Crosswalk.md#mas-guidelines-on-ai-risk-management-paragraph-crosswalk) |
| RBI (India, banks and NBFCs) | FREE-AI Committee report, 13 Aug 2025; draft Guidance on Regulatory Principles for Model Risk Management, 24 Jun 2026 | FREE-AI: Guidance. Draft: Proposed | Draft has no effective date [Verified] | [India hub](../17_India_AI_Compliance/01_India_AI_Regulatory_Hub.md) rows IN5, IN6 |
| SEBI (India, securities markets) | AI and ML guidelines announced on 10 Oct 2026; consultation paper of 20 Jun 2025 | Proposed. Not issued | "Shortly" [Reported] | [India hub](../17_India_AI_Compliance/01_India_AI_Regulatory_Hub.md) row IN13 |
| EU | AI Act, Regulation (EU) 2024/1689, as amended by the Digital Omnibus on AI | Binding law | Annex III high-risk duties from 2 Dec 2027 [Verified] | [EU hub](../12_EU_AI_Compliance/01_EU_AI_Regulatory_Hub.md) |
| FCA (UK) | Existing rules: Principles, Consumer Duty, SM&CR; no AI-specific rules | Binding in scope (the existing rules) | Applies now [Reported] | [UK hub](../21_UK_AI_Compliance/01_UK_AI_Regulatory_Hub.md) row UK5 |
| HKMA (Hong Kong, banks) | Supervisory Guidance for Responsible Adoption of Artificial Intelligence, 15 Oct 2026 | Guidance (supervisory expectations) | No deadline; uplift "in a timely manner" [Verified] | [Principle crosswalk](../26_Hong_Kong_AI_Compliance/03_Regulatory_Crosswalk.md#hkma-guidance-on-responsible-ai-adoption-principle-crosswalk) |

## Eight themes compared

| Theme | MAS | RBI | SEBI | EU AI Act | FCA | HKMA |
|---|---|---|---|---|---|---|
| Board accountability | The board approves the AI risk governance approach and addresses AI in the risk appetite framework (paras 3.1 to 3.4) [Verified] | Draft: the board oversees the model risk framework and approves model risk tiering policy (para 11); the entity is accountable for the outcomes of all its models (para 8) [Verified] | Firms stay responsible for AI outcomes; "clear accountability" announced [Reported] | Duties fall on providers and deployers; no board-level duty in the Act [Recalled] | Senior manager accountability under SM&CR [Reported] | The board approves an AI strategy with the approach and risk appetite (principle 1) [Verified] |
| Risk-based tiering | Risk materiality of each use case on impact, complexity and reliance (paras 4.10 to 4.13) [Verified] | Draft: model risk tiering; high-risk models need board-level review of validation and committee approval (paras 11, 12, 18) [Verified] | A tiered approach announced [Reported] | Statutory tiers; credit scoring and life and health insurance pricing are high-risk under Annex III [Reported] | Proportionality under existing rules; no AI tiering [Reported] | Materiality and risk assessment sets the depth of review (principle 4) [Verified] |
| AI inventory | Inventory with key attributes, including AI in third-party services and shadow AI (paras 4.2 to 4.9) [Verified] | Not checked for this page | Not known | Registration of some high-risk systems in an EU database; no general inventory duty [Recalled] | No AI-specific duty; PRA SS1/23 model inventory for in-scope banks [Verified in the UK hub] | Inventory of approved use cases, including third-party and embedded AI; unlisted AI restricted (principle 3) [Verified] |
| Lifecycle controls | Data, fairness, testing, validation, monitoring, change and retirement (Section 5) [Verified] | Draft: validation and monitoring of all models, including third-party and AI models [Verified] | Records of development, testing and monitoring proposed in 2025 [Reported] | Risk management, data governance, logging, accuracy and robustness for high-risk systems [Reported] | Existing rules; PRA SS1/23 for in-scope banks [Verified in the UK hub] | End-to-end testing, independent validation for material cases, monitoring, records (principle 4) [Verified] |
| Human oversight | Assigned and competent overseers with authority to intervene (para 5.9) [Verified] | Draft: human-in-command arrangements, override, and periodic human review of outputs (paras 60 to 63) [Verified] | Human oversight announced [Reported] | Human oversight of high-risk systems (Art. 14) [Recalled] | No AI-specific rule; the Mills Review raised questions on SM&CR where AI acts [Reported] | In-the-loop, on-the-loop or in-command, with authority to override or stop (principle 2) [Verified] |
| Third-party AI | Test it in context, contractual visibility, concentration, right to audit (paras 5.10 to 5.11) [Verified] | Draft applies to third-party models, and the board oversees them (paras 9, 12) [Verified] | Firms solely responsible for the AI and ML tools they use (2025 amendments) [Reported] | Value-chain duties; DORA for ICT third parties [Reported] | Outsourcing and operational resilience rules [Recalled] | Due diligence, contracts barring training on data without authorisation, audit rights, exit and concentration (principle 5) [Verified] |
| Customer transparency | Consider the need to tell customers of AI use, its consequences and redress (paras 5.5 to 5.6) [Verified] | Draft: customers can ask to switch to a human (para 59(iii)) [Verified] | Disclosure of AI and ML use proposed in 2025 [Reported] | Transparency duties for certain AI (Art. 50); right to explanation of some decisions (Art. 86) [Recalled] | Consumer Duty outcomes, including consumer understanding [Recalled] | Tell consumers about AI use and its risks before the service; redress and human review (principle 9) [Verified] |
| Kill switch | Tested activation protocols for kill switches (para 5.3); consider kill switches or override for high-risk AI (para 5.23(b)) [Verified] | Draft: override, suspension or deactivation mechanisms, including kill-switch arrangements (para 60(ii)) [Verified] | Kill switches announced [Reported] | The overseer can stop a high-risk system through a "stop" button or similar (Art. 14(4)(e)) [Recalled] | Nothing AI-specific found | A kill switch or equivalent for material or higher-risk use cases (principle 4) [Verified] |

## Build once: the strictest version and the wiki control

This is the wiki's reading of which instrument asks the most on each theme. Building to that version should meet the others on that theme, but check each regulator's wording and scope.

| Theme | Strictest version found | Wiki control | Test case |
|---|---|---|---|
| Board accountability | HKMA and MAS: the board approves an AI strategy or governance approach and the AI risk appetite | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | [TC-L02-005](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-005) |
| Risk-based tiering | EU for systems in its scope (statutory high-risk list); MAS and HKMA for everything else (materiality on impact, complexity and reliance) | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | [TC-L01-005](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-005) |
| AI inventory | HKMA (only approved AI may run; third-party and embedded AI included) with the MAS attribute list | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) | [TC-L01-008](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-008) |
| Lifecycle controls | EU for high-risk systems (conformity before market); MAS Section 5 for breadth | [AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [TC-L01-015](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-015) |
| Human oversight | EU Art. 14 for high-risk systems; RBI draft and HKMA on override and testing that oversight works | [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | [TC-L01-012](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-012) |
| Third-party AI | HKMA (contract terms on training use, audit, exit) with MAS (testing in your own context) | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) | [TC-L03-021](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-021) |
| Customer transparency | HKMA (before the service, including risks) with EU Art. 50 and Art. 86 where they apply | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [TC-L03-029](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-029) |
| Kill switch | HKMA (built in for material or higher-risk use cases) and the RBI draft (including kill-switch arrangements); MAS for testing activation | [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025), [AI-CTRL-040](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-040) | [TC-L01-021](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-021) |

## What changed in October 2026

- MAS issued its final Guidelines on 7 October 2026 [Verified].
- The SEBI chairman said on 10 October 2026 that guidelines including kill switches and human oversight would be issued shortly [Reported]. Until they are issued, nothing in the SEBI column binds.
- The HKMA replaced its 2019 principles with the guidance of 15 October 2026, which expects an inventory and a kill switch or equivalent for higher-risk use cases [Verified]. Comparisons drawn before that date may show the HKMA as silent on both.
- SEBI is not the only regulator with a kill switch on the table: MAS, the RBI draft and the HKMA all address one.
