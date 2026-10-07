---
title: "US: Role Guide"
author: Nachiket Sathaye
parent: "US AI Compliance"
nav_order: 2
description: "What US federal and state AI rules ask of practitioners, product companies, auditors and implementors, with a shared evidence list."
document_type: AI Security Wiki Reference
version: 1.0
---

# US: Role Guide

> **Verification required.** Claims on this page about US law were compiled on 7 October 2026 from secondary web sources and from memory of the law. No primary legal text was read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

Use the [US AI Regulatory Hub](01_US_AI_Regulatory_Hub.md) for instrument detail, and the templates in this section.

## AI practitioners

For engineers, data scientists and security staff.

- Identify which states your users and decisions touch, and build to the strictest ([US-T1](US-T1_State_Applicability_Matrix.md)).
- For employment and credit use cases, run disparate-impact style testing and keep the records ([US-T2](US-T2_Consequential_Decision_Impact_Assessment.md)).
- Where California law applies, implement provenance and disclosure features for generated content ([US-T3](US-T3_GenAI_Provenance_and_Transparency_Checklist.md)).
- Document against the NIST AI RMF. It may help as evidence of reasonable care.
- Make sure explanations and adverse-action reasons can be reconstructed from the logs.

## Product companies

For vendors, SaaS providers and platforms.

- Expect state-specific contract riders and questionnaires. Keep one control set with state overlays.
- Be accurate in claims about AI capability. Inaccurate claims carry FTC deception risk.
- If you develop large models, check the California frontier thresholds.
- Give deployers the documentation that state laws expect developers to provide.
- Do not market a product as "AI Act compliant" or "Colorado compliant" without confirming the current text.

## Auditors

For internal, external and assurance auditors.

- State whether each criterion is state law, federal enforcement risk or a NIST reference.
- Check the date logic. Some state duties start in 2027.
- Test notice, opt-out, appeal and human review for consequential decisions.
- Re-perform the bias or adverse-impact analysis on a sample.
- Record that federal preemption is not law.

## Implementors

For programme leads, GRC teams, CISOs and DPOs.

- Maintain a state-by-state applicability register ([US-T1](US-T1_State_Applicability_Matrix.md)) and review it every month.
- Use the NIST AI RMF as the spine, mapped to the wiki controls.
- Set up a litigation and enforcement watch that covers the DOJ task force and the state attorneys general.
- Assign owners for employment, credit and healthcare use cases.
- Prepare a single consumer notice and appeal process that satisfies the strictest state.

## Shared evidence list

- State applicability matrix
- NIST AI RMF mapping
- Impact or bias assessments
- Notices, opt-out and appeal logs
- Provenance and disclosure test results
- Vendor documentation
- Incident register

## Report limitation sentence for auditors

"Criteria were taken from a regulatory register dated 7 October 2026, compiled from secondary sources and not verified against primary legal text. This report is not a legal opinion."
