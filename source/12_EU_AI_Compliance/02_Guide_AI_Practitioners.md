---
title: "Guide for AI Practitioners Working Under EU Rules"
author: Nachiket Sathaye
parent: "EU AI Compliance"
nav_order: 2
description: "What EU rules ask of the people who build AI: role and tier, engineering requirements by AI Act article, a lifecycle checklist and evidence to keep."
document_type: AI Security Wiki Reference
version: 1.0
---

# Guide for AI Practitioners Working Under EU Rules

> **Verification required.** EU claims on this page were compiled on 7 October 2026 from secondary sources and from memory of the legal text. The Official Journal text was not read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text on EUR-Lex before relying on any of them. This is not legal advice.

For data scientists, ML and AI engineers, MLOps and security engineers. EU claims carry the tags used in the [EU AI Regulatory Hub](01_EU_AI_Regulatory_Hub.md).

## 1. Two questions to answer first

1. What is the system, and what is your role? You are a provider, a deployer or both ([T01](T01_AI_System_Classification.md)). If you build and sell the system, you are a provider. If you use a third party's system, you are a deployer. Fine-tuning, rebranding or changing the purpose can make you a provider [Recalled, Art. 25].
2. Does it process personal data? If it does, GDPR applies whatever the AI Act tier [Recalled].

## 2. What to build into the system

These requirements are duties for high-risk systems and good practice for the rest.

| Topic | Engineering requirement | AI Act article [Recalled] | Wiki control |
|---|---|---|---|
| Risk management | A continuous process across the lifecycle, with testing against defined metrics | 9 | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) |
| Data governance | Document provenance, representativeness, bias examination and gaps | 10 | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) |
| Technical documentation | Maintain the Annex IV content as you build, and do not leave it until after release | 11 | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) |
| Logging | Automatic event logs sufficient for traceability and post-market monitoring | 12 | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) |
| Transparency to deployers | Instructions for use: purpose, accuracy, limits, oversight measures | 13 | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) |
| Human oversight | Interfaces and measures that let a person understand, intervene and stop | 14 | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) |
| Accuracy, robustness, cybersecurity | Declared accuracy metrics; resilience to errors and to attacks, including data poisoning and adversarial inputs | 15 | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) |
| Quality management | Documented procedures for design, testing and change | 17 | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) |

The harmonised standards that will give a presumption of conformity are still maturing [Reported]: one QMS standard is approved and the others are in draft. Build to the requirements, and map to each standard once it is cited.

## 3. Lifecycle checklist

| Stage | Do this | Template |
|---|---|---|
| Idea | Classify (prohibited, high-risk, transparency, minimal) and determine your role | [T01](T01_AI_System_Classification.md) |
| Design | Choose the lawful basis; decide the oversight points; plan logging | [T02](T02_Impact_Assessment_FRIA_DPIA.md) |
| Data | Record source, licence, copyright opt-outs, personal data and bias checks | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md) |
| Build | Threat model; secure the pipeline; version data and models | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md) |
| Test | Accuracy, robustness, bias, security, red team; record thresholds | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md) |
| Release | Technical file complete; instructions for use written; notices published; registration if required | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md), [T06](T06_Transparency_Notice.md) |
| Operate | Monitor drift and incidents; keep logs for the required period | [T05](T05_AI_Incident_and_Breach_Reporting_Workflow.md) |
| Change | Decide whether the change is substantial; re-assess | [T01](T01_AI_System_Classification.md), [T09](T09_AI_System_Inventory.md) |
| Retire | Retain documentation as required; delete personal data per policy | [T09](T09_AI_System_Inventory.md) |

## 4. Personal data design points

- Training on personal data. You need a lawful basis for training and another for deployment. Legitimate interest is contested, and EDPB guidance exists [Recalled]. A proposal to make it explicit is still only a proposal [Reported].
- Automated decisions. GDPR Art. 22 limits solely automated decisions that have legal or similarly significant effects. AI Act Art. 86 adds a right to explanation for certain high-risk decisions [Recalled]. A human review and objection route is tested in [TC-L03-008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008).
- Special category data for bias testing. The AI Act allows it only where strictly necessary and with safeguards [Reported]. Record the necessity test.
- Transfers. Sending prompts to a non-EU model API is a transfer. See [T04](T04_Data_Location_and_Transfer_Record.md).
- Prompts and logs. Minimise, redact and set a retention period.

## 5. Generative and agentic systems

- Mark synthetic output in machine-readable form where Art. 50 applies, and use the voluntary marking code as a reference [Reported]. Verify which date applies to you ([hub section 2.2](01_EU_AI_Regulatory_Hub.md#22-reported-omnibus-changes)).
- Tell users that they are talking to AI.
- For agents, apply least privilege, per-tool approval, spend and action limits, and full action logs.
- If you provide or fine-tune a general-purpose model, see [T12](T12_GPAI_Model_Checklist.md).

## 6. Security

Map to ISO/IEC 27001-style controls first. NIS2 and DORA may impose reporting and supply-chain duties on your organisation or your customer [Recalled]. Watch the draft cybersecurity standard prEN 18282 [Reported].

## 7. Evidence to keep

Technical file, data sheets, test reports, bias results, oversight design, logs, change records, incident records and instructions for use. See the [EU Evidence Register](08_Evidence_Register.md).

## 8. Common mistakes

- Treating "just a pilot" as out of scope.
- Fine-tuning a vendor model without checking whether you became a provider.
- Writing the documentation after launch.
- Logs that cannot reconstruct a decision.
- Human oversight that exists only on paper, with reviewers who approve everything.
- Using special category data for bias tests without a necessity record.
- Sending EU personal data to a non-EU API without a transfer assessment.

## 9. Verification

Read the article text before relying on any citation on this page.
