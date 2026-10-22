---
title: "India Regulatory Crosswalk"
author: Nachiket Sathaye
parent: "India AI Compliance"
nav_order: 3
description: "Indian instruments mapped one per row to AI security controls, with verification status. Also available as a CSV file."
document_type: AI Security Wiki Reference
version: 1.0
last_reviewed: 2026-10-20
---

# India Regulatory Crosswalk

> **Verification required.** Claims on this page about Indian law were compiled on 7 October 2026 from secondary web sources and from memory of the law. Rows checked since then against primary documents (16 October 2026: IN1, IN2, IN4, IN5, IN6, IN10; 20 October 2026: IN12) are tagged [Verified] with the source in the last column. Every other claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

One row per instrument in the [India AI Regulatory Hub](01_India_AI_Regulatory_Hub.md), with the wiki controls that relate to it and its verification status. The last column is empty until a row has been confirmed against the primary text; record the primary URL and the date you retrieved it there.

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
| IN1 | Digital Personal Data Protection Act 2023 | Binding law | Binding law (Act 22 of 2023, listed as 11 Aug 2023); being implemented | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013); [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007); [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017); [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Verified | Whether the penalty applies per contravention; wording of each section | [Act text](https://www.indiacode.nic.in/bitstream/123456789/22037/2/a2023-22.pdf), retrieved 16 Oct 2026 |
| IN2 | DPDP Rules 2025 | Binding law | Notified as G.S.R. 846(E) dated 13 Nov 2025; phased | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013); [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007); [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Verified | Breach intimation time limit in Rule 7 (English text not read); any shortening of the phase-in | [Rules text (MeitY)](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf), retrieved 16 Oct 2026 |
| IN3 | Data Protection Board of India | Context | Established in law; not operational per Aug 2026 report | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013); [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Reported | Current status (not re-checked on 16 Oct 2026) |  |
| IN4 | India AI Governance Guidelines (MeitY) | Guidance | Non-binding; the document is undated; release reported as 5 Nov 2025 | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012); [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039); [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | Verified | Release date (the document itself is undated) | [Guidelines (PIB-hosted)](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc2025115685601.pdf), retrieved 16 Oct 2026 |
| IN5 | RBI FREE-AI Committee report | Guidance | Committee report published by the RBI on 13 Aug 2025; not a binding direction | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011); [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014); [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023); [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037); [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | Verified | The text of each recommendation; whether the RBI has adopted any of them as directions | [Report page (RBI)](https://rbi.org.in/SCRIPTS/PublicationReportDetails.aspx?ID=1306), retrieved 16 Oct 2026 |
| IN6 | RBI draft Guidance on Model Risk Management | Proposed | Draft issued 24 Jun 2026; comments to 24 Jul 2026 | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011); [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037); [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | Verified | Final status (not re-checked on 16 Oct 2026) | [Press release (RBI)](https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=63006), retrieved 16 Oct 2026 |
| IN7 | SEBI regulations on AI and ML tools used by regulated entities | Binding in scope | Amendments to the Intermediaries Regulations 2008 and the Securities Contracts (Regulation) (Stock Exchanges and Clearing Corporations) Regulations 2018; reported as notified 6 Feb 2025 | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011); [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014); [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | Reported | SEBI's notified text and gazette date; any later SEBI AI guidance | [Board memorandum (SEBI)](https://www.sebi.gov.in/sebi_data/meetingfiles/dec-2024/1735042007618_1.pdf), retrieved 16 Oct 2026 (proposal only) |
| IN8 | IRDAI: AI-cybersecurity readiness directive (May 2026); AI working group (Jun 2026) | Unclear | Not confirmed | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005); [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | Unverified | Whether any IRDAI instrument addresses AI, and its text |  |
| IN9 | IT Rules amendments on synthetic content labelling | Binding in scope | Reported as notified 10 Feb 2026 and in force from 20 Feb 2026 (amendment rules to the IT Rules 2021) | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | Reported | Gazette text, G.S.R. number and exact scope (law-firm sources agree but the gazette was not read) |  |
| IN10 | CERT-In incident reporting directions (2022) and AI guidance | Binding law | Binding directions of 28 Apr 2022 (No. 20(3)/2022-CERT-In) under section 70B(6) of the IT Act | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035); [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005) | Verified | Whether CERT-In has issued separate AI-specific guidance | [Directions (CERT-In)](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf), retrieved 16 Oct 2026 |
| IN11 | IT Act 2000 and SPDI Rules | Binding law | Existing law until DPDP fully commences | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005); [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | Recalled | Transition provisions |  |
| IN12 | IndiaAI Mission | Context | Programme (Mar 2024; INR 10,372 crore) | None | Verified | n/a | [Cabinet approval (PIB)](https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2012355), retrieved 20 Oct 2026 (release of 7 Mar 2024; outlay Rs 10,371.92 crore) |
