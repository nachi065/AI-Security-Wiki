---
title: "Japan Regulatory Crosswalk"
author: Nachiket Sathaye
parent: "Japan AI Compliance"
nav_order: 3
description: "Japanese instruments mapped one per row to AI security controls, with verification status. Also available as a CSV file."
document_type: AI Security Wiki Reference
version: 1.0
---

# Japan Regulatory Crosswalk

> **Verification required.** Claims on this page about Japanese law were compiled on 7 October 2026 from secondary web sources and from memory of the law. No primary legal text was read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

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
| JP1 | AI Promotion Act | Binding law | Law; 4 Jun 2025 | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | Reported | Any duties on businesses; investigation or publication powers |  |
| JP2 | AI Basic Plan | Context | Cabinet decision; adopted 14 Jul 2026, replacing the 23 Dec 2025 plan | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | Reported | Content |  |
| JP3 | Guidelines for AI Business (MIC and METI), version 1.2 (31 Mar 2026) | Guidance | Non-binding | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012); [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037); [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039); [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | Reported | Official text; English is provisional |  |
| JP4 | Act on the Protection of Personal Information (APPI) | Binding law | Binding | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013); [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007); [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Recalled | AI points from the PPC |  |
| JP5 | Copyright Act Art. 30-4 (information analysis exception) | Binding law | Binding | [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029) | Recalled | Current interpretation and limits |  |
| JP6 | Sector rules (financial, medical devices, others) | Binding in scope | Binding | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014); [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | Unverified | Per sector |  |
