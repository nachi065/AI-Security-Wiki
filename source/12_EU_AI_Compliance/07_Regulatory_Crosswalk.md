---
title: "EU Regulatory Crosswalk"
author: Nachiket Sathaye
parent: "EU AI Compliance"
nav_order: 7
description: "EU instruments mapped one per row to AI security controls and control themes, with verification status. Also available as a CSV file."
document_type: AI Security Wiki Reference
version: 1.0
---

# EU Regulatory Crosswalk

> **Verification required.** EU claims on this page were compiled on 7 October 2026 from secondary sources and from memory of the legal text. The Official Journal text was not read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text on EUR-Lex before relying on any of them. This is not legal advice.

One row per instrument in the [EU AI Regulatory Hub](01_EU_AI_Regulatory_Hub.md), with the AI Act also split into five parts (E1a to E1e). Each row gives the wiki controls that relate to the instrument, the control themes from the [Framework Adoption Guide](../10_Test_Case_Library/framework-adoption-guide.md) and the verification status. The last column is empty until a row has been confirmed against the primary text; record the primary URL and the date you retrieved it there.

The same data is available as a CSV file for GRC tooling: [crosswalk.csv](data/crosswalk.csv).

**Legal force** sorts each row under one of seven labels, so that law is not mistaken for guidance or for a voluntary framework. The label is this wiki's reading of the sources and carries the same verification caveat as the rest of the row.

| Label | Meaning |
|---|---|
| Binding law | Enacted law or regulation that applies generally in the jurisdiction, including provisions that start on a later date. |
| Binding in scope | Binding only on a sector, a free zone, a state or province, or public bodies. |
| Guidance | Published by a government or regulator, and not binding in itself. |
| Voluntary | A standard, code or framework that an organization chooses to adopt. |
| Proposed | A bill, draft or consultation, or a proposal that lapsed. It is not law. |
| Context | A policy, authority, programme or summary row that sets no rule. |
| Unclear | The sources used do not settle whether it binds. |

| ID | Instrument | Legal force | Type / status | Wiki controls | Control themes | Verification tag | To verify | Primary URL and retrieval date |
|---|---|---|---|---|---|---|---|---|
| E1 | AI Act (Regulation (EU) 2024/1689) as amended by the Digital Omnibus | Binding law | Binding; phased | All | GOV; RSK; POL; INV; OVS; AUD; CHG; INC | Reported; Recalled | Omnibus number; amended articles |  |
| E1a | AI Act Art. 5 prohibited practices | Binding law | Applies from 2 Feb 2025 | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012); [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | GOV; POL | Reported | Current list incl. new prohibition from 2 Dec 2026 |  |
| E1b | AI Act Art. 4 AI literacy | Binding law | Applies from 2 Feb 2025 | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | TRN | Reported | Wording after omnibus |  |
| E1c | AI Act high-risk (Arts. 9 to 17, 26, 27, 43 to 49, 72, 73) | Binding law | Annex III 2 Dec 2027; Annex I 2 Aug 2028 (reported) | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037); [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013); [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038); [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008); [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023); [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034); [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039); [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | RSK; PRV; OVS; AUD; INC; CHG | Reported; Recalled | Dates; article text |  |
| E1d | AI Act Art. 50 transparency | Binding law | From 2 Aug 2026 with Art. 50(2) grace to 2 Dec 2026 (sources differ) | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | OVS | Conflict | Exact application date |  |
| E1e | AI Act GPAI (Arts. 51 to 55) | Binding law | Applies since 2 Aug 2025; enforcement from 2 Aug 2026 | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014); [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028); [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029) | VND; POL | Reported | Text; guidelines |  |
| E2 | GDPR | Binding law | Binding | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013); [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007); [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017); [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | PRV; XBT; RET; INC | Recalled | Articles; national law |  |
| E3 | EDPB opinion on AI models and personal data | Guidance | Guidance | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | PRV | Recalled | Title and content |  |
| E4 | Digital Omnibus (data/GDPR) | Proposed | Proposal; not before 2027 | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | PRV | Reported | Status |  |
| E5 | NIS2 | Binding law | Binding via national law | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005); [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | INC; VND; BCP | Recalled | National transposition |  |
| E6 | DORA | Binding in scope | Binding for financial entities | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014); [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | VND; INC; BCP | Reported | Technical standards |  |
| E7 | Cyber Resilience Act | Binding law | Reporting from 11 Sep 2026; full 11 Dec 2027 | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005); [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) | INC; AUD | Reported | Dates |  |
| E8 | Product Liability Directive (new) | Binding law | Directive | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | RSK | Unverified | Transposition date |  |
| E9 | Data Act | Binding law | Regulation | [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007); [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | XBT; VND | Recalled | Application date |  |
| E10 | Digital Services Act | Binding law | Regulation | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | OVS | Recalled | Scope for AI |  |
| E11 | Copyright TDM opt-out | Binding law | Directive | [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029) | POL | Recalled | National law |  |
| E12 | Commission guidelines: prohibited practices | Guidance | Guidance | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | POL | Recalled | Date and content |  |
| E13 | Commission guidelines: GPAI | Guidance | Guidance (10 Jul 2025) | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | VND | Reported | Content |  |
| E14 | Commission draft guidelines: high-risk classification | Proposed | Draft 19 May 2026; consultation closed 23 Jul 2026 | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | INV | Reported | Final adoption |  |
| E15 | GPAI Code of Practice | Voluntary | Voluntary | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | VND | Reported | Signatory list |  |
| E16 | Code of Practice on marking and labelling AI content | Voluntary | Voluntary; final 10 Jun 2026 | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | OVS | Reported | Adequacy assessment |  |
| E17 | CEN-CENELEC JTC 21 standards (EN 18286:2026; prEN 18228, 18229, 18282, 18284) | Voluntary | EN 18286 approved 12 Jul 2026, OJ citation pending; others draft | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012); [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037); [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005); [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | GOV; RSK; AUD | Reported | Numbers; status |  |
| E18 | ISO/IEC 42001 | Voluntary | Voluntary standard | All | GOV; AUD | Recalled | Not harmonised |  |

The EU instruments behind AI-CTRL-041 and AI-CTRL-042 are listed on the [EU drivers page](06_Proposed_Control_Fundamental_Rights_Impact_Assessment.md).
