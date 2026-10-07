---
title: "Singapore: Role Guide"
author: Nachiket Sathaye
parent: "Singapore AI Compliance"
nav_order: 2
description: "What Singapore's AI frameworks ask of practitioners, product companies, auditors and implementors: agent bounding, MAS materiality, PDPA and CSA guidance."
document_type: AI Security Wiki Reference
version: 1.0
---

# Singapore: Role Guide

> **Verification required.** Claims on this page about Singapore law were compiled on 7 October 2026 from secondary web sources and from memory of the law. No primary legal text was read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

Use the [Singapore AI Regulatory Hub](01_Singapore_AI_Regulatory_Hub.md) for instrument detail, and the templates in this section.

## AI practitioners

For engineers, data scientists and security staff.

- For agents, bound the tools, data and scope of action, define approval checkpoints, and stage the deployment ([SG-T1](SG-T1_Agentic_AI_Risk_Bounding_Worksheet.md)).
- Keep test evidence in a form that can be used for AI Verify style reporting.
- Apply CSA threat mapping to prompts, tools and data flows.
- Minimise personal data in training and logs under the PDPA.
- Log agent actions to a standard that supports accountability.

## Product companies

For vendors, SaaS providers and platforms.

- Expect Singapore buyers, especially financial institutions, to request an inventory, a materiality assessment and third-party controls.
- Offer agent controls: scopes, approvals, kill switch, audit log.
- Say explicitly that the customer remains responsible for the agent's conduct, and give the customer the tools to carry that responsibility.
- Publish test summaries, and consider reporting aligned with AI Verify.
- Provide data location and sub-processor detail.

## Auditors

For internal, external and assurance auditors.

- The criteria are mostly voluntary, so define them in the engagement letter.
- For financial institutions, treat the MAS guidelines as the target even if the transition dates are not final, and state that basis.
- Test agent bounding by sampling permissions against the stated scope.
- Re-perform one test from the AI Verify style record.
- Check third-party AI arrangements.

## Implementors

For programme leads, GRC teams, CISOs and DPOs.

- Use the four agentic dimensions as the structure for agent governance.
- Build the MAS-style inventory and materiality assessment first ([SG-T2](SG-T2_MAS_Style_Inventory_and_Materiality.md)).
- Map controls to the CSA guidance for security.
- Align privacy notices and uses with PDPC guidance ([SG-T3](SG-T3_PDPA_AI_Use_Note.md)).
- Track the final MAS guidelines.

## Shared evidence list

- Agent risk assessment and approval records
- Inventory with materiality ratings
- Test reports
- Third-party AI due diligence
- PDPA basis records
- Security test reports

## Report limitation sentence for auditors

"Criteria were taken from a regulatory register dated 7 October 2026, compiled from secondary sources and not verified against primary legal text. This report is not a legal opinion."
