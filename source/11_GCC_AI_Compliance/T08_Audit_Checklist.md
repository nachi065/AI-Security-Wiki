---
title: "T08 AI Audit Checklist"
author: Nachiket Sathaye
parent: "GCC AI Compliance"
nav_order: 16
description: "Audit checklist of 34 tests across nine control families, from governance and inventory to incident response and evidence."
document_type: AI Security Wiki Reference
version: 1.0
---

# T08 AI Audit Checklist

> **Verification required.** This is a working template, not a regulator-approved form. Where it names a regional instrument, the claim comes from secondary sources and is a pointer to check, not a confirmed legal requirement. This is not legal advice.

Use with the [Evidence Register](08_Evidence_Register.md). Result: Effective (E), Partially effective (P), Ineffective (I), Not tested (N).

Audit: ______ System(s): ______ Period: ______ Auditor: ______ Criteria in scope (and their verification status): ______

## 1. Governance

| # | Test | Control | Result | Evidence ref | Note |
|---|---|---|---|---|---|
| 1.1 | AI policy approved, dated within review cycle | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | | | |
| 1.2 | Roles and accountability named incl. executive owner | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | | | |
| 1.3 | Board or executive reporting on AI risk in period | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | | | |
| 1.4 | Regulator and jurisdiction register current ([T11](T11_Regulator_Engagement_Log.md)) | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | | | |
| 1.5 | Ethics review or equivalent for high-impact systems | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | | | |

## 2. Inventory and tiering

| # | Test | Control | Result | Evidence ref | Note |
|---|---|---|---|---|---|
| 2.1 | Inventory exists with owner, purpose, tier, vendor, location | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | | | |
| 2.2 | Completeness: 5 discovered systems appear in register | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | | | |
| 2.3 | Tier decisions follow documented criteria ([T01](T01_AI_Use_Case_Intake_and_Risk_Tiering.md)) | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | | | |
| 2.4 | Vendor-embedded AI included | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | | | |

## 3. Privacy and regulatory

| # | Test | Control | Result | Evidence ref | Note |
|---|---|---|---|---|---|
| 3.1 | Lawful basis recorded for personal data use | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | | | |
| 3.2 | Impact assessment completed before go-live ([T02](T02_AI_Impact_Assessment.md)) | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | | | |
| 3.3 | Rights handling process tested | [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) | | | |
| 3.4 | Notices in Arabic and English where required ([T06](T06_Bilingual_AI_Use_Notice.md)) | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | | | |

## 4. Residency

| # | Test | Control | Result | Evidence ref | Note |
|---|---|---|---|---|---|
| 4.1 | Attestation ([T04](T04_Data_Residency_Attestation.md)) current and signed | [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007) | | | |
| 4.2 | Attestation matches cloud configuration (logs, backups, vector stores) | [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007) | | | |
| 4.3 | Transfers have a recorded legal view | [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | | | |

## 5. Vendors

| # | Test | Control | Result | Evidence ref | Note |
|---|---|---|---|---|---|
| 5.1 | Due diligence ([T03](T03_Vendor_Due_Diligence_GCC_Addendum.md)) before contract | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | | | |
| 5.2 | Contract has training-use restriction, sub-processor notice, incident SLA, audit rights | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | | | |
| 5.3 | Model-change notices handled | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | | | |

## 6. Oversight and safety

| # | Test | Control | Result | Evidence ref | Note |
|---|---|---|---|---|---|
| 6.1 | Human approval step exists for high-impact decisions | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | | | |
| 6.2 | Reviewer challenge evidenced (not rubber-stamp) | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | | | |
| 6.3 | Kill switch tested in period | [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) | | | |
| 6.4 | Accuracy, safety and robustness tests current, incl. Arabic | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | | | |
| 6.5 | Prompt-injection and exfiltration testing for generative or agentic systems | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | | | |

## 7. Fairness (AI-CTRL-041)

| # | Test | Control | Result | Evidence ref | Note |
|---|---|---|---|---|---|
| 7.1 | High-impact decisions defined | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | | | |
| 7.2 | Bias test current (pre-release, annual, on change) | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | | | |
| 7.3 | Re-performance of one test | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | | | |
| 7.4 | Explanation record traced for sample | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | | | |

## 8. Incident

| # | Test | Control | Result | Evidence ref | Note |
|---|---|---|---|---|---|
| 8.1 | Playbook includes AI incident types | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | | | |
| 8.2 | Notification matrix complete ([T05](T05_AI_Incident_and_Breach_Notification_Workflow.md)) | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | | | |
| 8.3 | Exercise held in period | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | | | |
| 8.4 | Incidents in period notified on time | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | | | |

## 9. Evidence and assurance

| # | Test | Control | Result | Evidence ref | Note |
|---|---|---|---|---|---|
| 9.1 | Evidence retained and retrievable | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | | | |
| 9.2 | Previous findings closed | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | | | |

## Summary

Total tests: ___ E: ___ P: ___ I: ___ N: ___

Top findings:

Limitations: criteria summarised from secondary sources; no legal opinion.
