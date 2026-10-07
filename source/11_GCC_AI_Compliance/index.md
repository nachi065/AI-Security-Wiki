---
title: "GCC AI Compliance"
author: Nachiket Sathaye
description: "GCC AI compliance resources: regulatory hub for UAE, Saudi Arabia, Qatar, Bahrain and Oman, role guides, 12 fill-in templates and a control crosswalk."
nav_order: 11
has_children: true
---

# GCC AI Compliance

Resources for people who build, sell, audit or run AI systems in the Gulf Cooperation Council states. The pages map regional laws, policies and security baselines to the wiki's [control library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md) and [test cases](../10_Test_Case_Library/index.md). They cover the UAE, Saudi Arabia, Qatar, Bahrain and Oman. Kuwait has not been researched.

> **Verification required.** Everything in this section about laws, regulators, dates and expectations was compiled from secondary sources (vendor documentation, law-firm trackers and press) on 7 October 2026. No primary legal text was read, and sources disagree on several dates. Check the primary text before relying on any regional claim. This is not legal advice.

## What is in this section

| Part | Pages | What it holds |
|---|---|---|
| [GCC AI Regulatory Hub](01_GCC_AI_Regulatory_Hub.md) | 1 | 32 laws, policies, regulator notes and security baselines across five states, each mapped to wiki controls and tagged with its verification status. |
| Role guides | 4 | What to do and what to keep as evidence, for [practitioners](02_Guide_AI_Practitioners.md), [product companies](03_Guide_Product_Companies.md), [auditors](04_Guide_Auditors.md) and [implementors](05_Guide_Implementors.md). |
| Templates T01 to T12 | 12 | Fill-in documents: use-case intake, impact assessment, vendor addendum, residency attestation, incident workflow, bilingual notice, ethics worksheet, audit checklist, inventory, bias test record, regulator log and risk register. |
| [Proposed control](06_Proposed_Control_Fairness_Bias_Explainability.md) | 1 | AI-CTRL-041 on fairness, bias testing and explainability, which is not yet part of the control library. |
| [Regulatory Crosswalk](07_Regulatory_Crosswalk.md) and [Evidence Register](08_Evidence_Register.md) | 2 | The instrument-to-control map and a starter evidence list, each also downloadable as a CSV file. |

## How regional claims are tagged

| Tag | Meaning |
|---|---|
| **[Reported]** | Stated by secondary sources only. Verify before relying on it. |
| **[Conflict]** | Secondary sources disagree. Resolve from the primary text. |
| **[Unverified]** | Single source, or not researched. |

Clause and article numbers are left blank wherever they were not seen in a source.

The templates are working documents, not regulator-approved forms. Where a template cites a regional instrument, treat that as a pointer to check.

## Where to start

| If you are | Read | Then use |
|---|---|---|
| A data scientist, ML or security engineer | [Guide for AI Practitioners](02_Guide_AI_Practitioners.md) | [T01](T01_AI_Use_Case_Intake_and_Risk_Tiering.md), [T02](T02_AI_Impact_Assessment.md), [T10](T10_Bias_Testing_Record.md) |
| An AI vendor or SaaS builder selling into the GCC | [Guide for AI Product Companies](03_Guide_Product_Companies.md) | [T03](T03_Vendor_Due_Diligence_GCC_Addendum.md) (as the buyer will send it), [T04](T04_Data_Residency_Attestation.md), [T06](T06_Bilingual_AI_Use_Notice.md) |
| An internal or external auditor | [Guide for Auditors](04_Guide_Auditors.md) | [T08](T08_Audit_Checklist.md), [Evidence Register](08_Evidence_Register.md) |
| A programme lead, GRC lead or CISO | [Guide for Implementors](05_Guide_Implementors.md) | [GCC AI Regulatory Hub](01_GCC_AI_Regulatory_Hub.md), [T09](T09_AI_System_Inventory.md), [T12](T12_Risk_Register_4x4.md) |

## Using the templates

Templates T01 to T12 are fill-in documents. To reuse one, open the page, follow the "Suggest an edit to this page" link in the footer to reach its Markdown source on GitHub, and copy it into your own repository or document tool.

## Keeping this section current

When you confirm an instrument against its primary text, record the primary URL and the retrieval date beside it in the [Regulatory Crosswalk](07_Regulatory_Crosswalk.md). Several instruments listed here are described as new, in consultation or awaiting promulgation, so the whole hub should be re-checked every quarter.
