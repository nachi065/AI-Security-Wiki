---
title: "T05 AI Incident and Breach Reporting Workflow (EU)"
author: Nachiket Sathaye
parent: "EU AI Compliance"
nav_order: 13
description: "AI incident types, a reporting matrix across GDPR, the AI Act, NIS2, DORA and the CRA, and a ten-step response workflow to complete in advance."
document_type: AI Security Wiki Reference
version: 1.0
---

# T05 AI Incident and Breach Reporting Workflow (EU)

> **Verification required.** This is a working template, not a regulator-approved form. Where it cites an article or a date, the citation comes from secondary sources or from memory of the legal text and is a pointer to check. This is not legal advice.

Wiki control: [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035). One incident can trigger several regimes at once. The timings below are [Recalled]. Confirm every deadline from the primary text and the national transposition before you use this workflow. Where a cell is blank, fill it from the source.

## 1. Incident types

| Code | Type | Example |
|---|---|---|
| I1 | Personal data breach | Prompt logs exposed |
| I2 | Serious incident under the AI Act (high-risk) | Death, serious harm to health, serious and irreversible disruption of critical infrastructure, serious infringement of fundamental rights, serious harm to property or the environment |
| I3 | Cybersecurity incident (NIS2 or DORA entity) | Compromise of the AI platform |
| I4 | Vulnerability in a product with digital elements (CRA) | Exploited flaw |
| I5 | Harmful or unfair output | Discriminatory decisions |
| I6 | GPAI systemic-risk incident | Provider reporting to the AI Office |
| I7 | Supplier incident | Silent model change, breach |

## 2. Regime matrix

Complete this matrix before an incident happens.

| Regime | Who reports | To whom | Trigger | Deadline | Source checked and date |
|---|---|---|---|---|---|
| GDPR breach | Controller; the processor notifies the controller | Supervisory authority; affected persons if the risk is high | Personal data breach with risk | 72 hours to the authority [Recalled] | |
| AI Act serious incident (Art. 73) | Provider of a high-risk system | Market surveillance authority of the Member State | Serious incident | 15 days in general; shorter for a widespread infringement or critical infrastructure; shorter for a death [Recalled] | |
| AI Act deployer duty | Deployer | Provider and authorities | Serious incident identified | Without undue delay [Recalled] | |
| GPAI systemic risk (Art. 55) | Provider | AI Office | Serious incident | | |
| NIS2 | Essential or important entity | CSIRT or competent authority | Significant incident | Early warning in 24 hours; notification in 72 hours; final report in one month [Recalled] | |
| DORA | Financial entity | Financial supervisor | Major ICT incident | Reported as an initial notice within hours; verify | |
| CRA | Manufacturer | CSIRT and ENISA | Actively exploited vulnerability or severe incident | Reporting applies from 11 Sept 2026 [Reported] | |
| Contracts | Supplier or customer | Counterparty | Per contract | Per contract | |

## 3. Workflow

| Step | Action | Owner | Target |
|---|---|---|---|
| 1 | Detect and log | Anyone / SOC | Immediately |
| 2 | Triage: type, severity, systems, data, Member States | Incident lead | |
| 3 | Contain: pause, kill switch ([AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025)), revoke keys | Engineering | |
| 4 | Preserve logs, prompts, model version, configuration | Security | |
| 5 | Assess duties across all regimes in section 2 | DPO / Legal | |
| 6 | Notify authorities within the deadlines | Legal / DPO | Per law |
| 7 | Notify customers, suppliers, affected persons | Account owner / DPO | Per law and contract |
| 8 | Remediate and retest | Engineering | |
| 9 | Update the risk assessment, technical file and post-market plan | AI governance lead | |
| 10 | Record the incident and update [T11](T11_Authority_and_Standards_Engagement_Log.md) | GRC | |

## 4. Severity

| Level | Definition |
|---|---|
| S1 | Harm to people or to regulated data |
| S2 | Material compliance or service failure |
| S3 | Contained |

## 5. Messages

Prepare these in the languages of the affected Member States: authority notice, customer notice, individual notice, internal bulletin and holding statement. Legal approves each one.

## 6. Record

ID, dates, type, severity, systems, persons and data, root cause, regimes triggered, notices (who and when), actions, lessons, file references.

## 7. Exercise

Run a tabletop exercise each year. Cover one multi-regime scenario (a personal data breach in a high-risk system) and one biased-output scenario. Keep the report as evidence.
