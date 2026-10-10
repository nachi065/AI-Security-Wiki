---
title: "US Regulatory Crosswalk"
author: Nachiket Sathaye
parent: "US AI Compliance"
nav_order: 3
description: "US federal and state instruments mapped one per row to AI security controls, with verification status. Also available as a CSV file."
document_type: AI Security Wiki Reference
version: 1.0
---

# US Regulatory Crosswalk

> **Verification required.** Claims on this page about US law were compiled on 7 October 2026 from secondary web sources and from memory of the law. No primary legal text was read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

One row per instrument in the [US AI Regulatory Hub](01_US_AI_Regulatory_Hub.md), with the wiki controls that relate to it and its verification status. The last column is empty until a row has been confirmed against the primary text; record the primary URL and the date you retrieved it there.

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
| US1 | Federal AI legislation | Context | None comprehensive | None | Reported | New bills |  |
| US2 | Executive Order 14365 (Dec 2025) | Context | Executive policy | None | Reported | Later litigation |  |
| US3 | Executive Order 14409 (2 Jun 2026) and 5 Jun national-security memo | Context | Executive policy | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005) | Reported | Text and numbers |  |
| US4 | NIST AI Risk Management Framework 1.0 | Voluntary | Voluntary | All | Reported | Colorado text after rewrite |  |
| US5 | Colorado: SB 24-205 repealed and reenacted by SB 26-189 (signed 14 May 2026) | Binding in scope | State law | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013); [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037); [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | Conflict | Older trackers still show 30 Jun 2026 |  |
| US6 | California: SB 53 frontier AI transparency; AB 2013 training data transparency | Binding in scope | State law; 1 Jan 2026 | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011); [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038); [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029) | Reported | Thresholds; text |  |
| US7 | California AI Transparency Act (SB 942 as amended) | Binding in scope | State law; operative 2 Aug 2026 (reported) | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | Reported | Bill number; scope |  |
| US8 | California CCPA regulations on ADMT, risk assessments and cybersecurity audits | Binding in scope | Binding regulation; approved by the Office of Administrative Law 22 Sep 2025, effective 1 Jan 2026 (CPPA page) | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013); [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023); [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037); [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | Reported | Approval and effective date come from the CPPA page; other details from law-firm summaries. Read the approved text for definitions, exceptions and thresholds |  |
| US9 | Texas TRAIGA (HB 149) | Binding in scope | State law; 1 Jan 2026 | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012); [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | Reported | Obligations list; enforcement |  |
| US10 | Illinois HB 3773 | Binding in scope | State law; 1 Jan 2026 | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041); [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | Reported | Scope |  |
| US11 | NYC Local Law 144; NY RAISE Act; Utah SB 149 | Binding in scope | Local and state | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041); [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | Reported | Dates |  |
| US12 | FTC Act s.5; EEOC and anti-discrimination law; ECOA adverse action; HIPAA; FDA for medical AI; bank model risk guidance (SR 26-2 and OCC Bulletin 2026-13, which replaced SR 11-7 on 17 Apr 2026) | Binding law | Existing federal law | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012); [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037); [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | Recalled | Current enforcement and guidance |  |
| US13 | State legislative volume | Context | Context | None | Reported | Figures |  |
