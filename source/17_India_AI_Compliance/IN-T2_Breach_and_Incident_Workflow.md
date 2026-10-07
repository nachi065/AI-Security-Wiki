---
title: "IN-T2 India Breach and Incident Workflow"
author: Nachiket Sathaye
parent: "India AI Compliance"
nav_order: 5
description: "Authority matrix for CERT-In, the Data Protection Board and sector regulators, with a response workflow, message pack and record fields."
document_type: AI Security Wiki Reference
version: 1.0
---

# IN-T2 India Breach and Incident Workflow

> **Verification required.** This is a working template, not a regulator-approved form. Where it names an instrument or a date, the claim comes from secondary sources or from memory of the law and is a pointer to check. This is not legal advice.

<!-- -->

> **How to use:** This is a blank form. Copy it and fill in the empty cells and blanks for your system. To copy it, follow the "Suggest an edit to this page" link in the footer to reach its Markdown source.

Wiki control: [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035). The deadlines are [Recalled] or blank. Fill them in from the primary text.

## Authority matrix

| Authority | Trigger | Deadline | Channel | Source and date checked |
|---|---|---|---|---|
| CERT-In | Cyber incident within the scope of the directions | 6 hours, from memory [Recalled] | | |
| Data Protection Board | Personal data breach | Initial intimation and detailed report under the Rules; confirm the hours and days | | |
| Affected data principals | Personal data breach | Without delay under the Act; confirm | | |
| RBI / SEBI / IRDAI | Sector incident | Per the sector direction | | |
| Customers / contracts | Per contract | | | |

## Workflow

1. Detect and log.
2. Triage.
3. Contain, using the kill switch where needed ([AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025)).
4. Preserve evidence.
5. Assess duties.
6. Notify.
7. Remediate.
8. Review and record.

## Message pack

Board notice, individual notice, CERT-In report, sector notice and customer notice. Prepare them in English and in the relevant regional languages.

## Record fields

ID, dates, type, severity, systems, data and persons, root cause, regimes, notices, actions, lessons.
