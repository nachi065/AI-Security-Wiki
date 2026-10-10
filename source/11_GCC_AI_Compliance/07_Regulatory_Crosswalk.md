---
title: "Regulatory Crosswalk"
author: Nachiket Sathaye
parent: "GCC AI Compliance"
nav_order: 7
description: "GCC instruments mapped one per row to AI security controls and control themes, with verification status. Also available as a CSV file."
document_type: AI Security Wiki Reference
version: 1.0
---

# Regulatory Crosswalk

> **Verification required.** Regional claims on this page were compiled from secondary sources on 7 October 2026. No primary legal text was read, and each claim is tagged [Reported], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

One row per instrument in the [GCC AI Regulatory Hub](01_GCC_AI_Regulatory_Hub.md), with the wiki controls that relate to it, the control themes from the [Framework Adoption Guide](../10_Test_Case_Library/framework-adoption-guide.md) and its verification status. The last column is empty until a row has been confirmed against the primary text; record the primary URL and the date you retrieved it there.

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

| ID | Jurisdiction | Instrument | Legal force | Type / status | Wiki controls | Control themes | Verification tag | To verify | Primary URL and retrieval date |
|---|---|---|---|---|---|---|---|---|---|
| U1 | UAE | Federal Decree-Law 45/2021 (PDPL) | Binding law | Binding | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013); [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007); [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017); [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | PRV; XBT; RET; INC | Reported | Executive Regulation status; article numbers |  |
| U2 | UAE | Federal Decree-Law 34/2021 (cybercrime) | Binding law | Binding | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005); [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028); [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | INC | Unverified | AI relevance |  |
| U3 | UAE | UAE Charter for Development and Use of AI | Guidance | Non-binding | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012); [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023); [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | GOV; POL; OVS; TRN | Conflict | Publication month |  |
| U4 | UAE | UAE AI Ethics Principles and Self-Assessment | Voluntary | Voluntary | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012); [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039); [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | POL; OVS | Reported | Principle names |  |
| U5 | UAE | Federal Authority for AI and Data | Context | Regulator (announced 14 Jun 2026) | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013); [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | GOV; AUD | Reported | Official mandate |  |
| U6 | UAE-DIFC | DIFC DP Law and Regulation 10 | Binding in scope | Binding in DIFC | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013); [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011); [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023); [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | PRV; OVS; RSK; CHG | Conflict | Enforcement date; ASO; certification |  |
| U7 | UAE-ADGM | ADGM Data Protection Regulations | Binding in scope | Binding in ADGM | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013); [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007) | PRV; XBT | Unverified | All |  |
| U8 | UAE-Dubai | Dubai AI Security Policy (DESC) | Unclear | Policy Sept 2024 | All | AUD; BCP; POL | Reported | Obtain text |  |
| U9 | UAE | CBUAE Guidance Note on AI/ML | Guidance | Supervisory guidance 23 Feb 2026 | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011); [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014); [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023); [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025); [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | GOV; INV; OVS; VND | Reported | Rulebook entry |  |
| U10 | UAE-AbuDhabi | AIATC Law 3/2024 | Context | Governance body |  |  | Reported | Scope |  |
| U11 | UAE | UAE information assurance (NESA/IA) | Unclear | Baseline | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005); [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008); [AI-CTRL-009](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009); [AI-CTRL-032](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-032) | AUD; BCP | Unverified | Custodian and version |  |
| U12 | UAE-Dubai | Dubai AI Seal | Unclear | Certification (procurement) | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012); [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | POL; AUD | Unverified | Single source |  |
| S1 | Saudi | PDPL | Binding law | Binding | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013); [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007); [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) | PRV; XBT; RET; INC | Conflict | In-force vs enforcement dates |  |
| S2 | Saudi | SDAIA AI Ethics Principles | Guidance | Non-binding | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012); [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039); [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | POL; OVS; TRN | Conflict | Version and date |  |
| S3 | Saudi | SDAIA Generative AI Guidelines | Guidance | Non-binding | [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002); [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010); [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | POL; OVS | Reported | Scope |  |
| S4 | Saudi | SDAIA AI Adoption Framework | Guidance | Non-binding |  | GOV | Reported | Levels |  |
| S5 | Saudi | SDAIA National AI Risk Mgmt Framework (SDAIA-P145) | Unclear | Published 2026 | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | RSK; INV; CHG | Conflict | Date April vs July 2026 |  |
| S6 | Saudi | NCA ECC and CCC | Binding in scope | Binding gov and CNI | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005); [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008); [AI-CTRL-032](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-032) | AUD; BCP; INC | Reported | Applicability |  |
| S7 | Saudi | NCA NCNICC-1:2025 | Unclear | Reported private sector from Jan 2026 | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005); [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008); [AI-CTRL-032](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-032) | AUD | Unverified | Applicability |  |
| S8 | Saudi | NCA AI Cybersecurity Guidelines | Proposed | Consultation closed 5 Aug 2026 | All | VND; AUD; BCP | Unverified | Final text |  |
| S9 | Saudi | Copyright TDM exception | Binding law | Reported eff. 12 Aug 2026 | [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029) | POL | Reported | Text |  |
| S10 | Saudi | NDMO/CST/SAMA localisation overlays | Unclear | Overlay | [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007) | XBT | Unverified | All |  |
| Q1 | Qatar | Law 13/2016 PDPPL | Binding law | Binding | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013); [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007); [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) | PRV; XBT; RET; INC | Reported | Articles |  |
| Q2 | Qatar | NCSA Guidelines for Secure Adoption and Usage of AI | Voluntary | Voluntary (reported) | All | VND; AUD; INC; BCP | Reported | Binding drift |  |
| Q3 | Qatar | MCIT Ethical AI Principles | Guidance | Non-binding | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012); [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039); [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | GOV; POL; OVS; TRN | Conflict | Year |  |
| Q4 | Qatar | QCB AI Guideline (4 Sep 2024) | Binding in scope | Reported binding for licensees | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011); [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023); [AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033); [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | GOV; RSK; INV; OVS; CHG | Reported | Binding status |  |
| B1 | Bahrain | Law 30/2018 PDPL | Binding law | Binding | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | PRV; XBT; RET; INC | Reported | Articles |  |
| B2 | Bahrain | General Policy for Use of AI (May 2025) | Binding in scope | Reported binding on government | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | GOV; POL; OVS | Reported | Scope |  |
| B3 | Bahrain | Draft AI law (38 articles) | Proposed | Not enacted per sources |  |  | Reported | Re-check |  |
| B4 | Bahrain | CBB digital financial advice directives | Unclear | Sector | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | VND | Reported | Scope |  |
| O1 | Oman | National AI Policy (9 Apr 2025) | Binding in scope | Reported mandatory within scope | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011); [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037); [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | GOV; RSK; INV; AUD; TRN; CHG | Reported | Scope |  |
| O2 | Oman | PDPL amendments | Proposed | Awaiting promulgation (reported) | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | PRV; RET | Reported | Re-check |  |
| K1 | Kuwait | None listed | Context |  |  |  | Unverified | Not researched |  |
