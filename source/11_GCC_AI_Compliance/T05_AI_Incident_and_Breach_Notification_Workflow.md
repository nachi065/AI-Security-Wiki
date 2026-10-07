---
title: "T05 AI Incident and Breach Notification Workflow"
author: Nachiket Sathaye
parent: "GCC AI Compliance"
nav_order: 13
description: "AI incident types, severity levels, a ten-step response workflow and a notification matrix to complete before an incident happens."
document_type: AI Security Wiki Reference
version: 1.0
---

# T05 AI Incident and Breach Notification Workflow

> **Verification required.** This is a working template, not a regulator-approved form. Where it names a regional instrument, the claim comes from secondary sources and is a pointer to check, not a confirmed legal requirement. This is not legal advice.

<!-- -->

> **How to use:** This is a blank form. Copy it and fill in the empty cells and blanks for your system. To copy it, follow the "Suggest an edit to this page" link in the footer to reach its Markdown source.

Wiki control: [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035). Notification deadlines and thresholds are not stated here because none was verified against a primary source for any GCC regime. Fill the "Deadline" column from the primary text or counsel before use.

## 1. AI incident types

| Code | Type | Example |
|---|---|---|
| I1 | Personal data breach | Prompt logs exposed; model leaks training data |
| I2 | Harmful or unsafe output | Wrong advice to a customer; offensive content |
| I3 | Unfair outcome | Bias found after harm |
| I4 | Security compromise | Prompt injection leads to action or exfiltration |
| I5 | Model failure or drift | Accuracy falls below threshold |
| I6 | Unauthorised AI use | Shadow AI with confidential data |
| I7 | Vendor incident | Supplier breach or silent model change |

## 2. Severity

| Level | Definition | Response |
|---|---|---|
| S1 | Harm to people or regulated data exposed | Immediate; executive and legal |
| S2 | Material service or compliance failure | Same day |
| S3 | Contained, no harm | Within agreed SLA |

## 3. Workflow

| Step | Action | Owner | Target time |
|---|---|---|---|
| 1 | Detect and log incident | Anyone / SOC | Immediately |
| 2 | Triage: type, severity, systems, data, countries | Incident lead | ______ |
| 3 | Contain: pause feature, trigger kill switch ([AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025)), revoke keys | Engineering | ______ |
| 4 | Preserve evidence: logs, prompts, model version, config | Security | ______ |
| 5 | Assess notification duties (table 4) | Privacy / Legal | ______ |
| 6 | Notify regulators and affected people where required | Legal / DPO | Per law |
| 7 | Notify customers (controller / regulated entity) per contract | Account owner | Per contract |
| 8 | Remediate and retest | Engineering | ______ |
| 9 | Post-incident review and control updates | AI governance lead | ______ |
| 10 | Record in incident register and [T11](T11_Regulator_Engagement_Log.md) | GRC | ______ |

## 4. Notification matrix (complete before an incident)

| Jurisdiction | Authority | Trigger | Deadline | Channel | Contact | Source checked and date |
|---|---|---|---|---|---|---|
| UAE mainland (PDPL) | [Reported] new Federal Authority for AI and Data; confirm | | | | | |
| DIFC | DIFC commissioner (confirm) | | | | | |
| ADGM | ADGM data protection office (confirm) | | | | | |
| Financial regulators (CBUAE, QCB, CBB, SAMA) | Sector regulator | | | | | |
| Saudi (PDPL) | SDAIA (confirm) | | | | | |
| Cybersecurity authority (NCA, NCSA, DESC) | | | | | | |
| Qatar (PDPPL) | | | | | | |
| Bahrain, Oman | | | | | | |
| Customers and contract counterparties | | | | | | |

## 5. Message pack

Prepare in Arabic and English: regulator notice, customer notice, affected-person notice, internal bulletin, holding statement. Have legal approve the wording.

## 6. Record per incident

ID, dates (detected, contained, notified), type, severity, systems, data and people affected, root cause, notices sent and to whom, actions, lessons.

## 7. Exercise

Run a tabletop at least annually with one prompt-injection scenario and one biased-output scenario. Record results as audit evidence ([AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038)).
