---
title: "UK: Role Guide"
author: Nachiket Sathaye
parent: "UK AI Compliance"
nav_order: 2
description: "What UK rules ask of AI practitioners, product companies, auditors and implementors: automated decision safeguards, equality law and sector regulators."
document_type: AI Security Wiki Reference
version: 1.0
---

# UK: Role Guide

> **Verification required.** Claims on this page about UK law were compiled on 7 October 2026 from secondary web sources and from memory of the law. No primary legal text was read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

Use the [UK AI Regulatory Hub](01_UK_AI_Regulatory_Hub.md) for instrument detail, and the templates in this section.

## AI practitioners

For engineers, data scientists and security staff.

- Solely automated decisions are now allowed with safeguards. Design the human review so that the reviewer has the authority, time and information to change the outcome.
- Build explanation and contest routes into the product ([UK-T1](UK-T1_ADM_Safeguards_Record.md)).
- Test for discrimination under the Equality Act as well as for statistical fairness.
- If you serve EU users, build to the EU AI Act requirements too.
- Check training-data licences, and do not rely on a copyright exception that was never enacted.

## Product companies

For vendors, SaaS providers and platforms.

- Expect UK buyers to ask about the DPIA, automated decision safeguards and alignment with ICO guidance.
- Financial customers will ask for model risk evidence in the style of PRA SS1/23.
- Provide the transparency fields that public bodies need for ATRS-style records ([UK-T3](UK-T3_Public_Sector_Transparency_Record.md)).
- State whether EU AI Act obligations apply to your product.
- Avoid claiming "UK AI compliance". There is no AI statute to comply with.

## Auditors

For internal, external and assurance auditors.

- Define the criteria. UK GDPR and the Data (Use and Access) Act are binding; the principles and ICO guidance are reference.
- Test that human involvement in automated decisions is meaningful: override rates, time on task, training.
- Check that the DPIA predates launch.
- For banks, test the inventory and validation against SS1/23 expectations.
- Record that no statutory AI tiering exists, so the tiering is the client's own.

## Implementors

For programme leads, GRC teams, CISOs and DPOs.

- Anchor the programme on UK GDPR and the sector regulators, and use the five principles as policy headings.
- Set up a register of automated decisions with their safeguards and contest route.
- Where you have EU exposure, align with the EU AI Act: one group standard plus a UK overlay.
- Plan for SM&CR accountability in regulated firms ([UK-T2](UK-T2_Regulated_Firm_AI_Checklist.md)).
- Track the Data (Use and Access) Act commencement and ICO guidance every month.

## Shared evidence list

- DPIA and automated decision safeguard records
- Human review logs with overrides
- Explanation and contest handling log
- Model inventory and validation (banks)
- Supplier due diligence
- Incident register with ICO notification decisions

## Report limitation sentence for auditors

"Criteria were taken from a regulatory register dated 7 October 2026, compiled from secondary sources and not verified against primary legal text. This report is not a legal opinion."
