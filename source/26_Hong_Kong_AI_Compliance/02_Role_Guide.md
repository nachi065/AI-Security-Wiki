---
title: "Hong Kong: Role Guide"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Hong Kong AI Compliance"
nav_order: 2
description: "What Hong Kong's AI guidance asks of practitioners, product companies, auditors and implementors: the HKMA ART principles, the SFC generative AI circular and the PDPO."
document_type: AI Security Wiki Reference
version: 1.0
---

# Hong Kong: Role Guide

> **Verification required.** The HKMA guidance of 15 October 2026 was read on 25 October 2026. Points about the SFC circular, PCPD guidance and the PDPO come from secondary sources or memory; see the tags in the [Hong Kong AI Regulatory Hub](01_Hong_Kong_AI_Regulatory_Hub.md). This is not legal advice.

Use the [Hong Kong AI Regulatory Hub](01_Hong_Kong_AI_Regulatory_Hub.md) for instrument detail, and [HK-T1](HK-T1_HKMA_ART_Principles_Self_Assessment.md) for a self-assessment.

## AI practitioners

For engineers, data scientists and security staff.

- Build a kill switch or equivalent into any material or higher-risk use case, and test it ([AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025)).
- Do not rely only on model instructions or filters for security: the HKMA guidance expects layered controls against data poisoning and prompt injection.
- Keep records that let an auditor trace a material output back to its sources, model version, configuration, inputs and, for generative AI, prompts.
- Set thresholds for when an output is withheld, sent for review or barred from triggering an action.
- Mask or pseudonymise personal data where you can.

## Product companies

For vendors, SaaS providers and platforms selling to Hong Kong banks and licensed corporations.

- Expect contract terms that bar you from training on the customer's personal or confidential data without authorisation, give audit rights, and require notice of material changes and incidents.
- Expect questions on concentration, substitutability and exit, and on how the customer can suspend your service.
- Give the information a customer needs to explain your system's purpose, limits and the basis of material outcomes.

## Auditors

For internal, external and assurance auditors.

- For banks, use the nine HKMA principles as the criteria ([HK-T1](HK-T1_HKMA_ART_Principles_Self_Assessment.md)). The guidance has no deadline, so state the date your opinion is measured against.
- Sample use cases from the inventory and confirm each has an owner, a materiality rating and the approvals that rating requires.
- For material use cases, check for independent validation, a tested kill switch, fallback arrangements and outcome tracing records.
- Check that the board approved an AI strategy and risk appetite.

## Implementors

For programme leads, GRC teams, CISOs and DPOs.

- Start with the inventory: define what counts as AI use, record third-party and embedded AI, and restrict anything not listed.
- Set up the materiality and risk assessment so that it decides the depth of review, then map the life cycle controls to it.
- Put the AI strategy and risk appetite to the board.
- Align customer disclosures: tell customers about AI use and its risks before the service is provided, and keep existing opt-out arrangements.
- For licensed corporations, check whether a planned generative AI use is high-risk under the SFC circular and whether it needs notice to the SFC.

## Shared evidence list

- Board-approved AI strategy and risk appetite
- Inventory of approved AI use cases with owners and risk ratings
- Materiality assessments and approvals
- Validation and adversarial test reports
- Kill-switch register and test records
- Vendor contracts and due diligence
- Customer AI-use notices and redress records

## Report limitation sentence for auditors

"Criteria were taken from the HKMA Supervisory Guidance for Responsible Adoption of Artificial Intelligence of 15 October 2026 and from a regulatory register dated 25 October 2026 that is partly compiled from secondary sources. This report is not a legal opinion."
