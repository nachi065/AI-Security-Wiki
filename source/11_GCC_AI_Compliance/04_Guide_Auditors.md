---
title: "Guide for Auditors of AI Systems in the GCC"
author: Nachiket Sathaye
parent: "GCC AI Compliance"
nav_order: 4
description: "For auditors of AI systems in the GCC: setting criteria, scoping, test steps by control family, sampling, common findings and report wording."
document_type: AI Security Wiki Reference
version: 1.0
---

# Guide for Auditors of AI Systems in the GCC

> **Verification required.** Regional claims on this page were compiled from secondary sources on 7 October 2026. No primary legal text was read, and each claim is tagged [Reported], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

For internal audit, external assurance providers and anyone preparing for a regulator review. Regional claims carry the tags used in the [GCC AI Regulatory Hub](01_GCC_AI_Regulatory_Hub.md).

## 1. Set the audit basis honestly

Define the criteria before testing. A GCC AI audit usually combines:

| Criteria source | Examples | Caution |
|---|---|---|
| Binding law | UAE PDPL, DIFC Reg 10, Saudi PDPL, Qatar PDPPL | Read the primary text. This wiki does not reproduce it. |
| Sector regulator | CBUAE note, QCB guideline | Binding status differs; confirm |
| National baseline | NCA, Dubai AI Security Policy, NCSA | Some are voluntary or in consultation |
| Internal policy | Client AI policy | Always in scope |
| Framework | Wiki controls, ISO/IEC 42001, NIST AI RMF | Not a legal standard |

State in the engagement letter which criteria are in scope and which are reference only. Do not report "non-compliant with law X" on evidence of a secondary summary.

## 2. Scoping steps

1. Obtain the AI inventory ([T09](T09_AI_System_Inventory.md)). If none exists, that is finding one.
2. Tier systems ([T01](T01_AI_Use_Case_Intake_and_Risk_Tiering.md)). Sample all high-impact systems, and a risk-weighted sample of others.
3. Identify jurisdictions per system: users, data subjects, hosting, vendor.
4. Identify regulators and any notification or approval duties ([T11](T11_Regulator_Engagement_Log.md)).
5. Agree evidence period and sampling method.

## 3. Control families and test steps

| Family | Wiki controls | Key test | Evidence |
|---|---|---|---|
| Governance | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | Roles named; board reporting; policy approved and current | Policy, minutes, RACI |
| Inventory | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | Inventory completeness test: trace 5 known systems into register and 5 register items into reality | Register, discovery output |
| Privacy and regulatory | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) | Lawful basis recorded; impact assessment done before launch | [T02](T02_AI_Impact_Assessment.md) records |
| Residency | [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007) | Attestation matches actual configuration | Cloud config export, [T04](T04_Data_Residency_Attestation.md) |
| Vendor | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | Due diligence done before contract; sub-processors listed | [T03](T03_Vendor_Due_Diligence_GCC_Addendum.md), contract |
| Oversight | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) | Human approval exists and is evidenced; kill switch test within period | Review logs, test record |
| Content safety and reliability | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | Test results current; Arabic included | Test reports |
| Fairness | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | Bias test current; thresholds approved | [T10](T10_Bias_Testing_Record.md) |
| Incident | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Playbook; exercise; notice workflow includes regulators | [T05](T05_AI_Incident_and_Breach_Notification_Workflow.md), exercise log |
| Audit evidence | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | Evidence retained and retrievable | Evidence register |

Use [T08](T08_Audit_Checklist.md) for a line-by-line checklist and the [Evidence Register](08_Evidence_Register.md) to track requests.

## 4. Sampling guidance

| Population | Suggested sample | Note |
|---|---|---|
| High-impact AI systems | All | Small population |
| Medium | Risk-based, minimum 25 percent or 5, whichever is larger | A suggested default, not a standard |
| Decisions for explanation test | 10 per system | Trace to input, output, explanation, review |
| Incidents | All in period | Check notice timing |

These thresholds are practitioner defaults, not a regulatory requirement. Document your own rationale.

## 5. Techniques

- Re-performance: re-run a bias or accuracy test on a fixed dataset and compare to reported results.
- Configuration inspection: inspect hosting region, logging, retention, model version.
- Walkthrough: follow one decision end to end including human review.
- Interview: owner, engineer, privacy lead, vendor manager.
- Document inspection: approvals dated before go-live.
- Kill-switch observation: witness the test.

## 6. Common findings

- Inventory incomplete (shadow AI, embedded vendor AI).
- Impact assessment done after launch.
- Residency attestation not matched to configuration (backups or logs elsewhere).
- Human review exists on paper but reviewers approve everything in seconds.
- Bias test performed once, no thresholds.
- English-only testing for Arabic-speaking users.
- Vendor sub-processors unknown.
- No named regulator contact or notification path.

## 7. Rating and wording

Suggested scale: Effective / Partially effective / Ineffective / Not tested. Word findings as: criteria, condition, cause, effect, recommendation.

Template sentence for secondary-source criteria: "The assessed system was evaluated against [criteria] as summarised in the client's regulatory register dated [date]. The register has not been verified against primary legal text."

## 8. Report checklist

- Scope, period, criteria and their verification status
- Systems and sample
- Limitations (secondary sources, no legal opinion)
- Findings with evidence references
- Management responses with dates
- Follow-up plan

## 9. Independence and handling

Keep evidence containing personal data under the same rules as production. Do not copy personal data into external AI tools during the audit.
