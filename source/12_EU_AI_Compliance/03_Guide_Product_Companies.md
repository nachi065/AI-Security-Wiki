---
title: "Guide for AI Product Companies Selling into the EU"
author: Nachiket Sathaye
parent: "EU AI Compliance"
nav_order: 3
description: "For AI vendors selling into the EU: whether the AI Act reaches you, product classification, buyer questions, a go-to-market checklist and contract points."
document_type: AI Security Wiki Reference
version: 1.0
---

# Guide for AI Product Companies Selling into the EU

> **Verification required.** EU claims on this page were compiled on 7 October 2026 from secondary sources and from memory of the legal text. The Official Journal text was not read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text on EUR-Lex before relying on any of them. This is not legal advice.

For providers, SaaS builders and platform vendors, including firms outside the EU. EU claims carry the tags used in the [EU AI Regulatory Hub](01_EU_AI_Regulatory_Hub.md).

## 1. Does the AI Act reach you?

The Act applies to providers that place AI systems on the EU market or put them into service. It also applies to non-EU providers where the system's output is used in the EU [Recalled]. Non-EU providers of high-risk systems generally need an authorised representative in the EU [Recalled]. Confirm with counsel.

## 2. Determine your product's position

| Question | If yes |
|---|---|
| Does it do something prohibited (Art. 5)? | Remove it. |
| Does it fall in an Annex III use case (employment, credit, education, biometrics, essential services and others)? | Probably high-risk. The date is reported as 2 Dec 2027 [Reported]. Check the Art. 6(3) filter and its documentation duty. |
| Is it a safety component of a regulated product (Annex I)? | High-risk through the product law; date reported as 2 Aug 2028 [Reported]. |
| Is it a chatbot, does it generate synthetic media, or does it detect emotion? | Art. 50 duties apply; check the date question in the [hub](01_EU_AI_Regulatory_Hub.md#22-reported-omnibus-changes). |
| Is it a general-purpose model that you provide? | Arts. 51 to 55; [T12](T12_GPAI_Model_Checklist.md). |
| None of the above | Minimal risk. GDPR and contract duties still apply. |

Use [T01](T01_AI_System_Classification.md) and record the reasoning. If you rely on Art. 6(3) to say that your Annex III system is not high-risk, you need a documented assessment and a database registration [Reported].

## 3. Buyer questions you will receive

| Question | Where the answer lives |
|---|---|
| What is your AI Act classification and role? | [T01](T01_AI_System_Classification.md) |
| Technical documentation, instructions for use, logs | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md) |
| Conformity assessment route, CE marking, declaration, registration | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md) |
| Where is data processed, and are there transfers? | [T04](T04_Data_Location_and_Transfer_Record.md) |
| Do you train on our data? | Contract, [T03](T03_Supplier_Due_Diligence_EU_Addendum.md) |
| Sub-processors and model suppliers | [T03](T03_Supplier_Due_Diligence_EU_Addendum.md) |
| Human oversight features | [T10](T10_Technical_Documentation_and_Conformity_Checklist.md), [Guide for AI Practitioners](02_Guide_AI_Practitioners.md) |
| Bias testing and explainability | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041), [T10](T10_Technical_Documentation_and_Conformity_Checklist.md) |
| Incident notice commitments | [T05](T05_AI_Incident_and_Breach_Reporting_Workflow.md) |
| Security certifications | ISO/IEC 27001 and any others you hold |
| Transparency features (AI disclosure, content marking) | [T06](T06_Transparency_Notice.md) |
| Information a deployer needs for its own FRIA or DPIA | [T02](T02_Impact_Assessment_FRIA_DPIA.md) |
| GPAI model information, if you build on one | [T12](T12_GPAI_Model_Checklist.md) |

## 4. Go-to-market checklist

1. Classify each product and each major feature ([T01](T01_AI_System_Classification.md)).
2. Set the timeline: prohibitions, literacy and GPAI duties apply now, transparency from 2026, high-risk from 2027 and 2028 [Reported].
3. Build the technical file early and keep it current ([T10](T10_Technical_Documentation_and_Conformity_Checklist.md)).
4. Decide hosting: EU regions, residency promises and transfer mechanism ([T04](T04_Data_Location_and_Transfer_Record.md)).
5. Nominate an authorised representative if you are outside the EU and your system is high-risk [Recalled].
6. Prepare the deployer pack: instructions for use, oversight guidance, log access, and input for the deployer's FRIA or DPIA.
7. Prepare incident contacts and customer notice SLAs ([T05](T05_AI_Incident_and_Breach_Reporting_Workflow.md)).
8. Watch standards and guidelines ([T11](T11_Authority_and_Standards_Engagement_Log.md)).

## 5. Value chain

If a customer rebrands your high-risk system or changes its purpose, the customer may become the provider [Recalled, Art. 25]. Give downstream parties the information they need, and agree in writing who does what. If you integrate a third-party model, you need its documentation (see the downstream part of [T12](T12_GPAI_Model_Checklist.md)).

## 6. Contract checklist

This is a list of points to cover. It does not give contract wording.

- Role statement for each party
- Intended purpose and prohibited uses
- Instructions for use and oversight duties
- Data processing terms, sub-processors, transfers
- Training-use limits on customer data
- Log access and retention
- Incident notice period
- Audit and authority cooperation
- Change notice for substantial modifications
- Liability allocation for AI errors; check the status of the Product Liability Directive [Unverified]
- Exit and data return

## 7. Answering questionnaires honestly

Do not claim conformity, a CE mark, ISO/IEC 42001 certification or "AI Act compliant" status without the document to show for it. For the high-risk dates, state your plan and do not present it as a status you already hold.

## 8. Verification

Each row on this page is a question to put to counsel.
