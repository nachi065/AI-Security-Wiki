---
title: "US AI Compliance"
author: Nachiket Sathaye
description: "US AI compliance resources: regulatory hub covering federal orders, NIST AI RMF and state AI laws in California, Colorado, Texas and Illinois, a role guide and three templates."
nav_order: 11
group: "Regional AI Regulatory Hub"
has_children: true
---

# US AI Compliance

Resources for people who build, sell, audit or run AI systems in the United States. The pages map US laws, guidance and standards to the wiki's [control library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md). The [GCC](../11_GCC_AI_Compliance/index.md) and [EU](../12_EU_AI_Compliance/index.md) sections cover their regions in more depth and hold the general templates.

> **Verification required.** Everything in this section about US law was compiled on 7 October 2026 from secondary web sources and from memory of the law. No primary legal text was read. Article, clause and section numbers are left blank unless a source showed them; fill them in from the primary text. Check the primary text before relying on any claim. This is not legal advice.

## The US position in one line

The US has no comprehensive federal AI law. Duties come from federal enforcement of existing law, sector rules, and a fast-moving patchwork of state AI laws. Federal preemption has been attempted by executive action and has not been enacted [Reported].

## What is in this section

| Page | For | What it holds |
|---|---|---|
| [US AI Regulatory Hub](01_US_AI_Regulatory_Hub.md) | Everyone | Instrument register, timeline, categories and roles, mapping to wiki controls, gaps, verification checklist and sources |
| [US: Role Guide](02_Role_Guide.md) | Practitioners, product companies, auditors, implementors | One guide with a part for each role |
| [US-T1](US-T1_State_Applicability_Matrix.md) | All | State AI law applicability matrix |
| [US-T2](US-T2_Consequential_Decision_Impact_Assessment.md) | All | Consequential-decision and discrimination impact assessment |
| [US-T3](US-T3_GenAI_Provenance_and_Transparency_Checklist.md) | Providers of generative AI | Generative AI provenance and transparency checklist |
| [US Regulatory Crosswalk](03_Regulatory_Crosswalk.md) | GRC tooling | Instrument-to-control map with verification status, also as a CSV file |

## How claims are tagged

| Tag | Meaning |
|---|---|
| **[Reported]** | Stated by secondary web sources found on 7 October 2026 (law-firm notes, vendor blogs, research notes). Not read in the primary text. |
| **[Recalled]** | Stated from memory of the law or guidance and not re-checked. Verify before citing it. |
| **[Conflict]** | Secondary sources disagree. Resolve from the primary text. |
| **[Unverified]** | Single source, marketing-grade source, or not researched. |

The templates are working documents, not regulator-approved forms.

## Common templates to reuse

The GCC and EU sections contain working templates that are not tied to a region. Reuse them and adapt the regional lines.

| Need | Reuse | Adapt |
|---|---|---|
| System intake and tiering | [GCC T01](../11_GCC_AI_Compliance/T01_AI_Use_Case_Intake_and_Risk_Tiering.md) or [EU T01](../12_EU_AI_Compliance/T01_AI_System_Classification.md) | Replace the tier names with this region's categories (section 3 of the hub) |
| Inventory | [GCC T09](../11_GCC_AI_Compliance/T09_AI_System_Inventory.md) or [EU T09](../12_EU_AI_Compliance/T09_AI_System_Inventory.md) | Add the regional columns listed in this section's templates |
| Audit checklist | [GCC T08](../11_GCC_AI_Compliance/T08_Audit_Checklist.md) or [EU T08](../12_EU_AI_Compliance/T08_Audit_Checklist.md) | Replace the criteria with this region's instruments |
| Supplier due diligence | [GCC T03](../11_GCC_AI_Compliance/T03_Vendor_Due_Diligence_GCC_Addendum.md) or [EU T03](../12_EU_AI_Compliance/T03_Supplier_Due_Diligence_EU_Addendum.md) | Replace the regional questions |
| Incident workflow | [GCC T05](../11_GCC_AI_Compliance/T05_AI_Incident_and_Breach_Notification_Workflow.md) or [EU T05](../12_EU_AI_Compliance/T05_AI_Incident_and_Breach_Reporting_Workflow.md) | Fill in this region's authority matrix |
| Bias testing record | [GCC T10](../11_GCC_AI_Compliance/T10_Bias_Testing_Record.md) | Use as it is |
| Risk register | [GCC T12](../11_GCC_AI_Compliance/T12_Risk_Register_4x4.md) | Use as it is |

## Keeping this section current

Re-check every month. State effective dates, federal orders and litigation change quickly. Colorado's law was rewritten in May 2026.
