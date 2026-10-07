---
title: "Guide for AI Product Companies Selling into the GCC"
author: Nachiket Sathaye
parent: "GCC AI Compliance"
nav_order: 3
description: "For AI vendors selling into the GCC: what buyers ask for, a market-entry checklist, the evidence pack to prepare and contract clauses to expect."
document_type: AI Security Wiki Reference
version: 1.0
---

# Guide for AI Product Companies Selling into the GCC

> **Verification required.** Regional claims on this page were compiled from secondary sources on 7 October 2026. No primary legal text was read, and each claim is tagged [Reported], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

For vendors, SaaS builders and platform providers. Regional claims carry the tags used in the [GCC AI Regulatory Hub](01_GCC_AI_Regulatory_Hub.md).

## 1. What GCC buyers usually ask for

Based on reported regulator expectations (CBUAE, QCB, NCA, Dubai AI Security Policy, government procurement), expect these in questionnaires and contracts. None is verified at clause level.

| Buyer ask | Why they ask | Your answer lives in |
|---|---|---|
| Where is data stored and processed? | Data protection, localisation, sector rules | [T04](T04_Data_Residency_Attestation.md) |
| Do you train on our data? | Confidentiality, IP, personal data | Contract + [T03](T03_Vendor_Due_Diligence_GCC_Addendum.md) |
| Can a human override or stop the system? | Oversight expectations; kill switch | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) |
| Do you test for bias and keep results? | CBUAE annual testing (reported) | [T10](T10_Bias_Testing_Record.md) |
| What third parties and sub-processors do you use? | Vendor due diligence | [T03](T03_Vendor_Due_Diligence_GCC_Addendum.md) |
| Incident and breach notice commitments? | Regulator deadlines | [T05](T05_AI_Incident_and_Breach_Notification_Workflow.md) |
| Arabic support and bilingual notices? | Disclosure expectations | [T06](T06_Bilingual_AI_Use_Notice.md) |
| Security certifications? | NCA, Dubai, NCSA baselines | ISO/IEC 27001, others you hold |
| Ethics self-assessment? | UAE/SDAIA ethics | [T07](T07_Ethics_Self_Assessment_Worksheet.md) |

## 2. Market-entry checklist

1. Pick your jurisdictions. UAE mainland, DIFC, ADGM, Saudi, Qatar, Bahrain, Oman each differ [Reported]. Do not assume one UAE regime.
2. Classify your customers. Financial institutions, government and critical infrastructure bring the heaviest requirements.
3. Decide hosting. In-region cloud, customer-tenant, or on-premise. Record what you can promise and what you cannot.
4. Prepare the evidence pack (section 4).
5. Local entity or partner questions. Procurement may require a local presence or certification; verify per tender. The Dubai AI Seal is reported as a gate for Dubai government AI contracting; single source, verify.
6. Contract baseline. Data protection terms, sub-processor list, audit rights, incident notice, training-use restriction, exit and deletion, liability for AI errors.

## 3. Product design points that sell

- In-region deployment option with clear architecture diagram.
- Customer-controlled retention and deletion.
- Human-in-the-loop modes for high-impact workflows.
- Model inventory export the buyer can paste into their own register ([T09](T09_AI_System_Inventory.md) fields).
- Bias and performance reports per customer or per release.
- Admin kill switch at tenant level.
- Arabic parity statement with published test results.
- Audit log export.

## 4. Evidence pack to prepare once and reuse

| Item | Source |
|---|---|
| Architecture and data-flow diagram with countries | [T04](T04_Data_Residency_Attestation.md) |
| Residency attestation (signed) | [T04](T04_Data_Residency_Attestation.md) |
| Sub-processor list with locations | [T03](T03_Vendor_Due_Diligence_GCC_Addendum.md) |
| Security certifications and last pen-test summary | your own |
| Model card and intended-use statement | your own |
| Bias test summary | [T10](T10_Bias_Testing_Record.md) |
| Incident response plan and notice timelines | [T05](T05_AI_Incident_and_Breach_Notification_Workflow.md) |
| Ethics self-assessment | [T07](T07_Ethics_Self_Assessment_Worksheet.md) |
| Bilingual notices | [T06](T06_Bilingual_AI_Use_Notice.md) |
| AI impact assessment template for customers | [T02](T02_AI_Impact_Assessment.md) |

## 5. Answering questionnaires honestly

- Say "not yet" rather than overstating certification. A false answer in a regulated tender is worse than a gap with a dated plan.
- Date every claim. Attach the document.
- Where a regional rule is unclear, say which instrument you assume and why.

## 6. Contract clauses to prepare (checklist, not wording)

- Purpose limitation and no training on customer data without consent
- Sub-processor approval and notification
- Data location commitment and transfer mechanism
- Breach and incident notice period (set to the stricter of the customer's regulator and the law that applies; verify the law)
- Audit and regulator access rights
- Model change notification for material changes
- Human oversight responsibilities split (provider vs customer)
- Exit, deletion and data return

## 7. Regulated customer notes

- Banks and insurers (UAE): expect the CBUAE expectations in section 2.1 of the [GCC AI Regulatory Hub](01_GCC_AI_Regulatory_Hub.md) flowed down to you [Reported].
- Qatar licensees: QCB guideline reported binding with approval for high-risk AI; expect approval evidence requests [Reported].
- Saudi customers: expect NCA-style controls and PDPL terms [Reported].
- Government (any): expect ethics frameworks, local hosting and sometimes certification.

## 8. Verification reminders

Put each reported requirement to the customer's compliance team or counsel as a question before you treat it as settled.
