---
title: "AI System Security Risk Review Checklist Template (.xlsx)"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Templates"
nav_order: 13
description: "A downloadable Excel checklist for reviewing the security risk of one AI system across its lifecycle: 150 review questions in nine categories, with an impact register, a risk register, threat and vulnerability lists and severity criteria."
document_type: AI Security Wiki Template
version: 1.0
---

# AI System Security Risk Review Checklist Template (.xlsx)

**[Download the AI System Security Risk Review Checklist Template (.xlsx)](AI_System_Security_Risk_Review_Checklist.xlsx)**

> **Purpose:** Review the security risk of one AI system with a question for each part of its lifecycle, from algorithm design and training to deployment, monitoring, audit, incident response and harm to people. Record each potential event's impact and risk, the threats and vulnerabilities behind it, the approved controls and the KRIs you watch.

> **Audience:** Security architects, risk and GRC teams, AI product owners, and internal audit.

> **Before you rely on it:** The severity criteria and risk appetite wording are examples for your governing body to adapt and approve. The registers cite ISO/IEC 42001, 42005, 23894, the 5259 series and 27701 as the basis of the method; check each standard's current edition.

## What is in the workbook

| Sheet | What it holds |
|---|---|
| README and License | How to use the workbook, colour legend, sources, licence, credit and disclaimer |
| Review Checklist | 150 review questions with an ID (AISSR-00001 onward), category, subcategory and IT area. Reserved yellow rows at the end of each subcategory are for your own questions |
| Impact Register | One row per potential event for one AI system: impact on the organisation, individuals, society, legal and regulatory conformity, and business continuity; IT area, lifecycle stage, impact area, likelihood, impact level, approved controls, KRIs, verifiability and maintainability |
| Risk Register | The same events with the threats and vulnerabilities involved, the risk level, approved controls and KRIs |
| Threat List and Vulnerability List | Threats and vulnerabilities to choose from, including AI-specific ones for bias, robustness, data quality and AI posing as a human |
| Ref Tables | The dropdown lists, the lifecycle stages, the impact areas and the High, Medium and Low severity criteria |

The nine question categories are Algorithm Design and Architecture; Model Training Security; Model Evaluation and Validation; Model Deployment Security; Access and Usage Controls; Post-Deployment Monitoring and Maintenance; Security Reviews and Audits; Incident Response and Recovery; and Harm to People, Organisations and the Ecosystem.

## How to use it

1. **Review Checklist.** Filter by category or IT area and answer each question for the system. Add your own questions in the reserved rows.
2. **Impact Register.** For each potential event, describe the impact in each of the five areas, choose the IT area, lifecycle stage and impact area, and rate likelihood and impact as High, Medium or Low using the criteria on Ref Tables.
3. **Risk Register.** For the same events, pick the threats and vulnerabilities, rate the risk, and record the approved controls and the KRIs you monitor.
4. **Treat and track.** Carry the risks into the [AI Risk Register Template](01_AI_Risk_Register_Template.md) for scoring, treatment and review dates.

## The severity criteria

An event is **High** when its losses exceed the organisation's risk appetite, its effect on society, the environment, ethics or health lasts longer than six months, or it leads to service or contract breaches outside the organisation's control. **Medium** covers losses within appetite but with a long-term effect, and effects lasting three to six months. **Low** covers losses within appetite with a short-term effect, and effects lasting less than three months. Replace these with your own thresholds.

## How it relates to the other templates

| Template | Use it for |
|---|---|
| [AI Risk Review Template](../02_Risk_Management/02E_AI_Risk_Review_Template.md) | A short intake review with twelve questions |
| This checklist | A full lifecycle review of one system, with its impact and risk record |
| [AI Security Assurance Baseline](14_AI_Security_Assurance_Baseline_Template.md) | Requirements to send to a vendor or system owner, with evidence |
| [AI Impact Assessment Template](09_AI_Impact_Assessment_Template.md) | The narrative impact assessment on people that the law or ISO/IEC 42005 may require |

## Licence and credit

Written by Nachiket Sathaye and Ankush Jain (version V01, 2024) and published in the wiki in October 2026, with organisation names removed, the dropdowns rebuilt and the standard editions corrected. The workbook is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), like the rest of the wiki. Suggested credit: "AI System Security Risk Review Checklist" by Nachiket Sathaye and Ankush Jain, AI Security Wiki, licensed under CC BY-SA 4.0. If you share an adapted version, say what you changed and release it under the same licence. Standard names belong to their owners and are cited for reference only.
