---
title: "Evidence Register"
author: Nachiket Sathaye
parent: "GCC AI Compliance"
nav_order: 8
description: "Starter list of 27 evidence items an auditor would request for an AI system in the GCC, by control family. Also available as a CSV file."
document_type: AI Security Wiki Reference
version: 1.0
---

# Evidence Register

A starter list of the evidence an auditor would request for an AI system in the GCC, by control family. Use it with the [T08](T08_Audit_Checklist.md) audit checklist and fill in the last two columns as requests are made and answered.

The same data is available as a CSV file: [evidence_register.csv](data/evidence_register.csv).

| Ref | Family | Evidence item | Wiki control | Format | Requested date / owner | Received date / status |
|---|---|---|---|---|---|---|
| E01 | Governance | AI policy approved and dated | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | Policy document |  |  |
| E02 | Governance | Role and accountability matrix | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | RACI |  |  |
| E03 | Governance | Board or executive AI risk reports | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | Minutes, packs |  |  |
| E04 | Inventory | AI inventory ([T09](T09_AI_System_Inventory.md)) | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | Register export |  |  |
| E05 | Inventory | Discovery sweep output | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | Procurement / SaaS / cloud list |  |  |
| E06 | Inventory | Tiering records ([T01](T01_AI_Use_Case_Intake_and_Risk_Tiering.md)) | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | Completed forms |  |  |
| E07 | Privacy | Impact assessments ([T02](T02_AI_Impact_Assessment.md)) | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | Signed assessments |  |  |
| E08 | Privacy | Lawful basis record | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | DPO record |  |  |
| E09 | Privacy | Rights-request log and test | [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) | Log, test record |  |  |
| E10 | Privacy | Bilingual notices ([T06](T06_Bilingual_AI_Use_Notice.md)) | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | Screenshots, version history |  |  |
| E11 | Residency | Attestation ([T04](T04_Data_Residency_Attestation.md)) | [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007) | Signed form |  |  |
| E12 | Residency | Cloud region configuration export | [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007) | Config export |  |  |
| E13 | Vendor | Due diligence ([T03](T03_Vendor_Due_Diligence_GCC_Addendum.md)) | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | Completed addendum |  |  |
| E14 | Vendor | Contract clauses | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | Contract extract |  |  |
| E15 | Oversight | Human review log with overrides | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | Log extract |  |  |
| E16 | Oversight | Kill-switch test record | [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) | Test report |  |  |
| E17 | Safety | Accuracy, robustness, safety test reports (incl. Arabic) | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | Reports |  |  |
| E18 | Security | Prompt-injection / exfiltration test | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005); [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | Pen-test report |  |  |
| E19 | Fairness | Bias test records ([T10](T10_Bias_Testing_Record.md)) | [AI-CTRL-041](06_Proposed_Control_Fairness_Bias_Explainability.md) | Records, code hash |  |  |
| E20 | Fairness | Explanation records sample | [AI-CTRL-041](06_Proposed_Control_Fairness_Bias_Explainability.md) | Sample |  |  |
| E21 | Incident | Playbook and notification matrix ([T05](T05_AI_Incident_and_Breach_Notification_Workflow.md)) | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Documents |  |  |
| E22 | Incident | Tabletop exercise report | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Report |  |  |
| E23 | Incident | Incident register | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Register |  |  |
| E24 | Regulator | Authority register and contact log ([T11](T11_Regulator_Engagement_Log.md)) | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | [T11](T11_Regulator_Engagement_Log.md) |  |  |
| E25 | Risk | Risk register ([T12](T12_Risk_Register_4x4.md)) | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | Register |  |  |
| E26 | Assurance | Evidence retention rule | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | Policy |  |  |
| E27 | Assurance | Prior findings tracker | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | Tracker |  |  |
