---
title: "Singapore AI Regulatory Hub"
author: Nachiket Sathaye
parent: "Singapore AI Compliance"
nav_order: 1
description: "Singapore AI frameworks and law mapped to AI security controls: IMDA governance frameworks including agentic AI, AI Verify, the PDPA, MAS and CSA guidance."
document_type: AI Security Wiki Reference
version: 1.0
---

# Singapore AI Regulatory Hub

> **Verification required.** Claims on this page about Singapore law were compiled on 7 October 2026 from secondary web sources and from memory of the law. No primary legal text was read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

This page maps Singapore laws, guidance and standards that bear on AI to the wiki's controls.

## 1. Regional model

There are four layers [Reported]:

1. The PDPA, and the PDPC advisory guidelines on AI recommendation and decision systems.
2. Voluntary governance frameworks: the Model AI Governance Framework, its generative and agentic versions, and AI Verify testing.
3. MAS guidelines for the financial sector.
4. CSA cybersecurity guidance for AI systems.

The voluntary frameworks still shape what buyers expect. Organisations remain legally responsible for the conduct of their AI agents.

## 2. Instrument register

| # | Instrument | Type / status | Key points | Wiki controls | Tag | To verify |
|---|---|---|---|---|---|---|
| SG1 | Model AI Governance Framework (2019; later editions) | Voluntary | Internal governance, risk management, operations, stakeholder communication | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [Recalled] | Current edition |
| SG2 | Model AI Governance Framework for Agentic AI (IMDA, 22 Jan 2026) | Voluntary | Four dimensions: risk assessment and bounding; human accountability; technical controls; end-user responsibility | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005) | [Reported] | Full text |
| SG3 | AI Verify testing framework and toolkit; Global AI Assurance Pilot (Feb 2025) | Voluntary testing and assurance | Technical tests and process checks against governance principles | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [Reported] | Principle list (11, from memory) |
| SG4 | PDPA and PDPC Advisory Guidelines on AI | Binding law; guidance | Use of personal data in AI recommendation and decision systems | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) | [Reported] | Guideline title and content; exceptions for research or business improvement |
| SG5 | MAS Guidelines on AI Risk Management | Proposed Nov 2025; final status not confirmed | For all financial institutions: governance, inventory, risk materiality assessment, lifecycle controls (data, fairness, transparency, oversight, testing, cyber), third-party AI, generative AI | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-041](../11_GCC_AI_Compliance/06_Proposed_Control_Fairness_Bias_Explainability.md) (proposed) | [Conflict] | Final issue date; transition period |
| SG6 | MAS FEAT principles and Veritas | Voluntary financial-sector principles | Fairness, ethics, accountability, transparency | [AI-CTRL-041](../11_GCC_AI_Compliance/06_Proposed_Control_Fairness_Bias_Explainability.md) (proposed) | [Recalled] | Current status |
| SG7 | CSA Guidelines and Companion Guide on Securing AI Systems (2024) and agentic addendum (17 Jun 2026) | Voluntary | Risk identification, lifecycle controls, threat mapping; an addendum for agentic AI. Consultation ran from 22 Oct to 31 Dec 2025 | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) | [Reported] | Text |
| SG8 | Cybersecurity Act (critical information infrastructure) | Binding | Obligations for owners of critical information infrastructure (CII) | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [Recalled] | Scope |

## 3. Categories, tiers and roles

| Category / role | What it means |
|---|---|
| Organisation | Remains legally responsible for AI and agent behaviour |
| Financial institution | MAS expectations apply to all financial institutions, if finalised as proposed |
| CII owner | Cybersecurity Act duties |
| Agentic AI deployer | Use the bounding and accountability dimensions |
| No statutory tiers | Use a materiality assessment ([SG-T2](SG-T2_MAS_Style_Inventory_and_Materiality.md)) |

## 4. Timeline

| Date | Event | Tag |
|---|---|---|
| 2019 | Model AI Governance Framework | [Recalled] |
| Feb 2025 | Global AI Assurance Pilot | [Reported] |
| Nov 2025 | MAS AI risk management guidelines proposed | [Reported] |
| 22 Jan 2026 | Agentic AI framework launched | [Reported] |
| 17 Jun 2026 | CSA agentic AI addendum | [Reported] |

## 5. Mapping of common wiki controls

| Wiki control | Regional hook |
|---|---|
| [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) Inventory and tiering | MAS inventory and materiality assessment ([SG-T2](SG-T2_MAS_Style_Inventory_and_Materiality.md)) |
| [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) Human approval | Human accountability checkpoints in the agentic framework ([SG-T1](SG-T1_Agentic_AI_Risk_Bounding_Worksheet.md)) |
| [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) Kill switch | Technical controls and graded deployment in the agentic framework |
| [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) Privacy | PDPA and PDPC AI guidelines ([SG-T3](SG-T3_PDPA_AI_Use_Note.md)) |
| [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005) Security | CSA guidance and addendum |
| [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) Audit evidence | AI Verify test records |
| [AI-CTRL-041](../11_GCC_AI_Compliance/06_Proposed_Control_Fairness_Bias_Explainability.md) Fairness (proposed) | MAS FEAT and AI risk guidelines |

## 6. Where the wiki covers this

The topics raised on this page are covered by the following controls, test cases and templates.

| Topic | Covered by |
|---|---|
| Agentic AI governance (IMDA framework) | [SG-T1](SG-T1_Agentic_AI_Risk_Bounding_Worksheet.md); [Agentic AI Security and Tool Governance](../04_Domain_Standards/09_Agentic_AI_Security_and_Tool_Governance.md); [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006), [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) |
| MAS-style inventory and materiality | [SG-T2](SG-T2_MAS_Style_Inventory_and_Materiality.md); [TC-L01-005](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-005), [TC-L01-009](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-009) |
| AI Verify test evidence | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038); [TC-L02-016](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-016) |
| AI use under the PDPA | [SG-T3](SG-T3_PDPA_AI_Use_Note.md); [TC-L03-002](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-002) |

## 7. Conflicts and cautions

- Sources describe the MAS guidelines as proposed. Confirm the final text and the transition period.
- The number of AI Verify principles is given from memory and was not verified.
- The voluntary frameworks are still enforced in practice, through tenders and sector supervision.

## 8. Verification checklist

- [ ] MAS final guidelines and effective date
- [ ] IMDA agentic framework text
- [ ] PDPC AI advisory guideline title and content
- [ ] AI Verify current principle list and toolkit
- [ ] CSA addendum text
- [ ] FEAT status
- [ ] Add the primary URL and retrieval date beside every confirmed row

## 9. Sources

All sources are secondary unless marked as a regulator or government page. Each fetched page was summarised by a tool and was not read line by line. A source marked "not read" appeared only as a title or snippet in search results, so do not treat it as support for any claim.

| Source | Status | Rows it relates to |
|---|---|---|
| [Bird & Bird: Singapore agentic AI governance framework](https://cm.twobirds.com/en/insights/2026/singapore/singapore-introduces-new-model-ai-governance-framework-for-agentic-ai) | Fetched and summarised | SG1, SG2, SG3 |
| [Simmons & Simmons: MAS guidelines on AI risk management](https://www.simmons-simmons.com/en/publications/cmm4lh7wv004utmikclcdujg7/mas-guidelines-on-artificial-intelligence-risk-management) | Fetched and summarised | SG5 |
| [Allen & Gledhill: CSA addendum on securing AI systems](https://www.allenandgledhill.com/sg/publication/articles/33420/csa-publishes-addendum-to-guidelines-and-companion-guide-on-securing-ai-systems) | Fetched and summarised | SG7 |
| [Allen & Gledhill: MAS consults on AI risk management guidelines](https://www.allenandgledhill.com/sg/publication/articles/31741/mas-consults-on-proposed-guidelines-for-artificial-intelligence-risk-management) | Not read | SG5 status |
| [Baker McKenzie: MAS consultation paper](https://connectontech.bakermckenzie.com/singapore-mas-publishes-consultation-paper-on-proposed-guidelines-on-ai-risk-management) | Not read | SG5 status |

No primary legal text (statute, regulation or circular) was read for any row. Confirm each row against the primary source, and add its URL and retrieval date in the [Singapore Regulatory Crosswalk](03_Regulatory_Crosswalk.md).
