---
title: "Guide for Implementors: Building an AI Governance Programme in the GCC"
author: Nachiket Sathaye
parent: "GCC AI Compliance"
nav_order: 5
description: "For programme leads, GRC teams and CISOs: a 90-day plan, RACI, early decisions, maturity steps and metrics for AI governance in the GCC."
document_type: AI Security Wiki Reference
version: 1.0
---

# Guide for Implementors: Building an AI Governance Programme in the GCC

> **Verification required.** Regional claims on this page were compiled from secondary sources on 7 October 2026. No primary legal text was read, and each claim is tagged [Reported], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

For programme leads, GRC teams, CISOs and vCISOs. Regional claims carry the tags used in the [GCC AI Regulatory Hub](01_GCC_AI_Regulatory_Hub.md).

## 1. Target outcome in 90 days

A working baseline: inventory, tiering, policy, impact assessment process, vendor addendum, incident workflow, named owners, and a regional register with verification status.

## 2. 90-day plan

| Days | Workstream | Output | Template |
|---|---|---|---|
| 0 to 15 | Discover | AI inventory v1, including vendor-embedded AI; list of jurisdictions and regulators | [T09](T09_AI_System_Inventory.md), [T11](T11_Regulator_Engagement_Log.md) |
| 0 to 15 | Mandate | Executive sponsor, steering group, charter | none |
| 15 to 45 | Classify | Tiering rules; high-impact list | [T01](T01_AI_Use_Case_Intake_and_Risk_Tiering.md), [T12](T12_Risk_Register_4x4.md) |
| 15 to 45 | Policy | AI policy, acceptable-use, GenAI rules | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) |
| 30 to 60 | Assess | Impact assessment procedure; first assessments on top 3 systems | [T02](T02_AI_Impact_Assessment.md) |
| 30 to 60 | Vendors | GCC addendum issued to AI vendors | [T03](T03_Vendor_Due_Diligence_GCC_Addendum.md) |
| 45 to 75 | Data | Residency attestation per system | [T04](T04_Data_Residency_Attestation.md) |
| 45 to 75 | Incident | Notice workflow; tabletop exercise | [T05](T05_AI_Incident_and_Breach_Notification_Workflow.md) |
| 60 to 90 | Fairness | Bias testing on high-impact systems | [T10](T10_Bias_Testing_Record.md) |
| 60 to 90 | Transparency | Bilingual notices | [T06](T06_Bilingual_AI_Use_Notice.md) |
| 75 to 90 | Assure | Internal audit pass; gap log; board report | [T08](T08_Audit_Checklist.md) |

## 3. RACI (starting point)

| Activity | Board / ExCo | AI governance lead | CISO | DPO / privacy | Legal | Business owner | Engineering |
|---|---|---|---|---|---|---|---|
| AI policy | A | R | C | C | C | I | I |
| Inventory | I | A | C | C | I | R | R |
| Tiering | I | A | C | C | C | R | C |
| Impact assessment | I | A | C | R | C | R | C |
| Vendor due diligence | I | C | R | C | C | A | I |
| Residency attestation | I | C | A | C | C | R | R |
| Incident notification | I | C | A | R | R | C | R |
| Bias testing | I | A | C | C | C | R | R |
| Regulator engagement | A | R | C | C | R | I | I |

R responsible, A accountable, C consulted, I informed. Adjust to your organisation.

## 4. Decisions you must make early

1. Which framework is the spine? The wiki's control library with ISO/IEC 42001 and NIST AI RMF mapping is a practical choice; SDAIA reportedly references both [Reported].
2. Single group standard or per-country overlays? Recommended: one group standard at the strictest common level, plus country overlays recorded in the [Regulatory Crosswalk](07_Regulatory_Crosswalk.md).
3. Who is accountable at board level? CBUAE expectations reportedly include board accountability [Reported]; assign it even if you are not a bank.
4. What is "high impact"? Write the definition. Include decisions on credit, insurance, employment, eligibility, health and safety, and anything affecting legal rights; confirm with counsel.
5. Where may data go? Approved hosting regions list.

## 5. Maturity steps

| Level | Looks like | Evidence |
|---|---|---|
| 1 Ad hoc | No inventory; teams use AI freely | none |
| 2 Defined | Policy, inventory, intake form | [T01](T01_AI_Use_Case_Intake_and_Risk_Tiering.md), [T09](T09_AI_System_Inventory.md) |
| 3 Managed | Assessments, vendor addendum, bias tests on high-impact | [T02](T02_AI_Impact_Assessment.md), [T03](T03_Vendor_Due_Diligence_GCC_Addendum.md), [T10](T10_Bias_Testing_Record.md) |
| 4 Measured | Metrics, internal audit, regulator log | [T08](T08_Audit_Checklist.md), [T11](T11_Regulator_Engagement_Log.md) |
| 5 Optimised | Continuous monitoring, certification | ISO/IEC 42001 certificate if pursued |

## 6. Metrics

- Percent of AI systems in the inventory with a tier and owner
- Percent of high-impact systems with a current impact assessment and bias test
- Vendors with signed addendum
- Mean time to classify an incident and issue notices
- Open audit findings past due
- Percent of systems with tested kill switch in last 12 months

## 7. Regulator engagement

Maintain [T11](T11_Regulator_Engagement_Log.md): who the regulator is, what duties exist (notifications, approvals, reporting), last contact. The UAE Federal Authority for AI and Data was reported on 14 June 2026; confirm its remit before listing it as a duty [Reported].

## 8. Pitfalls

- Starting with tools instead of an inventory.
- Treating the regional register as settled law.
- One-time assessments with no re-trigger on change.
- Ignoring vendor-embedded AI.
- No Arabic content in notices.

## 9. Escalation triggers

Define when a system is stopped: failed bias threshold, unapproved data location, unresolved high incident, regulator instruction. Link to kill switch ownership ([AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025)).
