---
title: "Guide for Implementors: Building an EU AI Governance Programme"
author: Nachiket Sathaye
parent: "EU AI Compliance"
nav_order: 5
description: "For programme leads, GRC teams, CISOs and DPOs: what applies when, a 90-day plan, RACI, early decisions, maturity steps and metrics under EU rules."
document_type: AI Security Wiki Reference
version: 1.0
---

# Guide for Implementors: Building an EU AI Governance Programme

> **Verification required.** EU claims on this page were compiled on 7 October 2026 from secondary sources and from memory of the legal text. The Official Journal text was not read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text on EUR-Lex before relying on any of them. This is not legal advice.

For programme leads, GRC teams, CISOs, DPOs and virtual CISOs. EU claims carry the tags used in the [EU AI Regulatory Hub](01_EU_AI_Regulatory_Hub.md).

## 1. Target outcome in 90 days

An inventory with role and tier, a literacy programme, a policy, an impact assessment procedure, a supplier addendum, an incident workflow, named owners, and a register of dates and authorities.

## 2. What applies when

A planning view. All dates are [Reported].

| When | What |
|---|---|
| Now | Prohibitions, AI literacy, GPAI duties, transparency (check the date nuance) |
| Dec 2026 | Marking grace ends for existing generative systems; new prohibition on intimate-imagery generation |
| Dec 2027 | High-risk Annex III |
| Aug 2028 | High-risk Annex I products |

Do not wait for the late dates. Inventory, classification and documentation take months.

## 3. 90-day plan

| Days | Workstream | Output | Template |
|---|---|---|---|
| 0 to 15 | Discover | Inventory v1, including AI embedded in vendor products | [T09](T09_AI_System_Inventory.md) |
| 0 to 15 | Mandate | Sponsor, steering group, charter | none |
| 0 to 30 | Prohibited screen | All use cases checked against Art. 5 | [T01](T01_AI_System_Classification.md) |
| 15 to 45 | Classify | Role and tier per system | [T01](T01_AI_System_Classification.md) |
| 15 to 60 | Literacy | Role-based training and records | [T07](T07_AI_Literacy_Programme_Record.md) |
| 30 to 60 | Assess | DPIA and FRIA procedure; first assessments | [T02](T02_Impact_Assessment_FRIA_DPIA.md) |
| 30 to 60 | Suppliers | Addendum issued to AI suppliers | [T03](T03_Supplier_Due_Diligence_EU_Addendum.md) |
| 45 to 75 | Data | Transfer record per system | [T04](T04_Data_Location_and_Transfer_Record.md) |
| 45 to 75 | Incident | Multi-regime workflow; tabletop exercise | [T05](T05_AI_Incident_and_Breach_Reporting_Workflow.md) |
| 60 to 90 | Transparency | Notices and marking review | [T06](T06_Transparency_Notice.md) |
| 60 to 90 | Documentation | Technical file skeleton for each high-risk system | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md) |
| 75 to 90 | Assure | Internal audit pass; board report | [T08](T08_Audit_Checklist.md), [T11](T11_Authority_and_Standards_Engagement_Log.md) |

## 4. RACI (starting point)

| Activity | Board | AI gov lead | CISO | DPO | Legal | Business owner | Engineering |
|---|---|---|---|---|---|---|---|
| Policy | A | R | C | C | C | I | I |
| Inventory | I | A | C | C | I | R | R |
| Classification | I | A | C | C | R | R | C |
| DPIA and FRIA | I | A | C | R | C | R | C |
| Supplier due diligence | I | C | R | C | C | A | I |
| Technical documentation | I | A | C | C | I | C | R |
| Incident notification | I | C | A | R | R | C | R |
| Literacy | I | A | C | C | C | R | I |
| Authority engagement | A | R | C | C | R | I | I |

## 5. Decisions you must make early

1. The spine framework. Use the wiki controls mapped to the AI Act, with ISO/IEC 42001 as a certifiable bridge. ISO/IEC 42001 is not a harmonised standard [Recalled].
2. A provider or deployer posture for each system. Avoid becoming a provider by accident.
3. A definition of "high-impact" that works across GDPR Art. 22 and AI Act Annex III.
4. Approved hosting regions and a transfer position.
5. A joint DPIA and FRIA procedure ([T02](T02_Impact_Assessment_FRIA_DPIA.md)).
6. Who may sign technical documentation and declarations.

## 6. Maturity steps

| Level | Looks like | Evidence |
|---|---|---|
| 1 | Ad hoc | none |
| 2 | Inventory, policy, classification | [T01](T01_AI_System_Classification.md), [T09](T09_AI_System_Inventory.md) |
| 3 | Assessments, supplier controls, literacy | [T02](T02_Impact_Assessment_FRIA_DPIA.md), [T03](T03_Supplier_Due_Diligence_EU_Addendum.md), [T07](T07_AI_Literacy_Programme_Record.md) |
| 4 | Technical files, internal audit, authority log | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md), [T08](T08_Audit_Checklist.md), [T11](T11_Authority_and_Standards_Engagement_Log.md) |
| 5 | Continuous monitoring; certification where useful | ISO/IEC 42001 certificate, if pursued |

## 7. Metrics

- Percent of systems with a role and a tier
- High-risk systems with a complete technical file
- Staff who have completed role-based literacy training
- Suppliers with a signed addendum
- Time to classify an incident and send notices
- Systems with a tested kill switch
- Open audit findings that are overdue

## 8. Overlaps to integrate

NIS2, DORA and the CRA share risk management, reporting and supply-chain themes with the AI Act [Reported]. Build one incident process ([T05](T05_AI_Incident_and_Breach_Reporting_Workflow.md)) and one supplier process ([T03](T03_Supplier_Due_Diligence_EU_Addendum.md)) rather than four of each. One source claims this saves 30 to 40 percent of the effort. That figure rests on a single source and is not established [Unverified].

## 9. Pitfalls

- Waiting for the late dates.
- Classifying by marketing label.
- Ignoring AI embedded in vendor products.
- Running literacy training once and never again.
- Writing documentation after launch.
- Treating the voluntary marking code or the draft guidelines as final law.

## 10. Stop triggers

Stop or pause a system on a failed threshold, an unlawful data location, an unresolved serious incident, an authority instruction, or the discovery of a prohibited practice. Link each trigger to kill-switch ownership ([AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025)).
