---
title: "Japan Regulatory Crosswalk"
author: Nachiket Sathaye
parent: "Japan AI Compliance"
nav_order: 3
description: "Japanese instruments mapped one per row to AI security controls, with verification status. Also available as a CSV file."
document_type: AI Security Wiki Reference
version: 1.0
last_reviewed: 2026-10-22
---

# Japan Regulatory Crosswalk

> **Verification required.** Claims on this page about Japanese law were compiled on 7 October 2026 from secondary web sources and from memory of the law. On 22 October 2026, rows JP1 to JP4 were checked against the primary text on the issuing bodies' own sites (the Cabinet Office, METI and the Personal Information Protection Commission) and are tagged [Verified]. Every other claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

One row per instrument in the [Japan AI Regulatory Hub](01_Japan_AI_Regulatory_Hub.md), with the wiki controls that relate to it and its verification status. The last column is empty until a row has been confirmed against the primary text; record the primary URL and the date you retrieved it there.

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

| ID | Instrument | Legal force | Type / status | Wiki controls | Verification tag | To verify | Primary URL and retrieval date |
|---|---|---|---|---|---|---|---|
| JP1 | AI Promotion Act (Act No. 53 of 2025) | Binding law | Law; promulgated 4 Jun 2025, fully in force 1 Sep 2025. Businesses must cooperate with state measures; no penalties | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | Verified | Article text on e-Gov (could not be read automatically); whether there is a power to publish names | [Cabinet Office: AI Act page](https://www8.cao.go.jp/cstp/ai/ai_act/ai_act.html); [Cabinet Office: AI Act overview (PDF)](https://www8.cao.go.jp/cstp/ai/ai_hou_gaiyou.pdf), retrieved 22 Oct 2026 (the government gathers information, analyses cases and gives guidance and advice to businesses; the AI Strategy Headquarters adopted a guideline under Art. 13 on 19 Dec 2025) |
| JP2 | AI Basic Plan | Context | Cabinet decision; adopted 14 Jul 2026, replacing the 23 Dec 2025 plan | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | Verified | Content (the plan text was not read) | [Cabinet Office: AI Basic Plan page](https://www8.cao.go.jp/cstp/ai/ai_plan/ai_plan.html); [Cabinet Office: AI policy top page](https://www8.cao.go.jp/cstp/ai/index.html), retrieved 22 Oct 2026 (the 14 Jul 2026 plan is listed as current (Phase II); the 23 Dec 2025 plan is listed under past plans) |
| JP3 | Guidelines for AI Business (MIC and METI), version 1.2 (31 Mar 2026) | Guidance | Non-binding | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012); [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037); [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039); [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | Verified | Nothing outstanding | [METI: AI Guidelines for Business version 1.2 page](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/20260331_report.html); [METI: AI Guidelines for Business version 1.2 (PDF)](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20260331_1.pdf), retrieved 22 Oct 2026 (the text calls itself non-binding soft law; METI labels the English version a tentative translation) |
| JP4 | Act on the Protection of Personal Information (APPI) | Binding law | Binding; amended by the 2026 APPI amendment law (passed 10 Jul 2026, promulgated 17 Jul 2026, in force within two years): consent exception for statistics including AI development, surcharges, rules for children under 16 | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013); [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007); [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Verified | Amendment law text and comparison table; PPC cabinet orders and rules (being drafted) | [PPC: 2026 amendment page](https://www.ppc.go.jp/personalinfo/legal/r8kaiseihogohou); [PPC: outline of the amendment law (PDF)](https://www.ppc.go.jp/files/pdf/260717_kaiseihounitsuite.pdf); [PPC: press release, 7 Apr 2026](https://www.ppc.go.jp/news/press/2026/260407/); [PPC: caution on generative AI services, 2 Jun 2023](https://www.ppc.go.jp/files/pdf/230602_alert_generative_AI_service.pdf), retrieved 22 Oct 2026 (Cabinet decision and submission to the Diet 7 Apr 2026) |
| JP5 | Copyright Act Art. 30-4 (information analysis exception) | Binding law | Binding | [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029) | Recalled | Current interpretation and limits |  |
| JP6 | Sector rules (financial, medical devices, others) | Binding in scope | Binding | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014); [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | Unverified | Per sector |  |
