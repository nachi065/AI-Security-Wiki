---
title: "India: Role Guide"
author: Nachiket Sathaye
parent: "India AI Compliance"
nav_order: 2
description: "What Indian rules ask of AI practitioners, product companies, auditors and implementors: DPDP consent and breach duties and sector regulator expectations."
document_type: AI Security Wiki Reference
version: 1.0
---

# India: Role Guide

> **Verification required.** Claims on this page about Indian law were compiled on 7 October 2026 from secondary web sources and from memory of the law. No primary legal text was read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

Use the [India AI Regulatory Hub](01_India_AI_Regulatory_Hub.md) for instrument detail, and the templates in this section.

## AI practitioners

For engineers, data scientists and security staff.

- Treat any personal data in training, prompts and logs as within DPDP scope, and keep consent and purpose records tied to datasets ([IN-T1](IN-T1_DPDP_AI_Processing_Record_and_Notice.md)).
- Design for withdrawal of consent and erasure, with lineage from the data to the model and its embeddings.
- Log enough to support a breach report to CERT-In within hours, and a report to the Board ([IN-T2](IN-T2_Breach_and_Incident_Workflow.md)).
- For finance clients, expect RBI-style model validation, explainability and fairness testing.
- Test Indian languages, code-mixing and transliteration, and record the quality gaps.

## Product companies

For vendors, SaaS providers and platforms.

- Decide your DPDP role for each customer (fiduciary or processor) and put it in the contract.
- Prepare answers on data location, sub-processors and the use of customer data for training.
- Banks, brokers and insurers will pass RBI, SEBI and IRDAI expectations down to you: inventory export, bias test summary, kill switch, audit rights.
- Offer notice and consent text in English and in scheduled languages, and confirm the language requirement in the Rules.
- Do not claim DPDP compliance for obligations that have not yet commenced. State your phased plan.

## Auditors

For internal, external and assurance auditors.

- State whether each criterion is binding (DPDP, sector directives) or a reference (MeitY guidelines, FREE-AI).
- Test consent artefacts: sample records, notice versions, withdrawal handling.
- Test the breach path from end to end, including its timing against CERT-In and DPDP duties.
- For regulated entities, check the AI inventory against RBI-style expectations ([IN-T3](IN-T3_Regulated_Entity_AI_Readiness.md)).
- Record the uncertainty over enforcement (the Board's status) as a limitation. It does not lower what the controls should achieve.

## Implementors

For programme leads, GRC teams, CISOs and DPOs.

- Build the DPDP programme first (notice, consent, rights, breach, retention), then layer the AI controls on it.
- Plan to the earlier May 2027 date, and watch for a shorter phase-in.
- Map the group AI policy to the MeitY principles and the sector expectations in one crosswalk.
- Appoint accountable owners for reporting to the Board, and for significant data fiduciary duties if you are designated.
- Run a tabletop exercise that covers both CERT-In and the Data Protection Board ([IN-T2](IN-T2_Breach_and_Incident_Workflow.md)).

## Shared evidence list

- Consent and notice records, with versions
- Data inventory and lineage to models
- Processor contracts
- Breach register and tabletop report
- AI inventory and tiering
- Bias and validation reports
- Kill-switch test
- Authority contact log

## Report limitation sentence for auditors

"Criteria were taken from a regulatory register dated 7 October 2026, compiled from secondary sources and not verified against primary legal text. This report is not a legal opinion."
