---
title: "Hong Kong AI Compliance"
author: Nachiket Sathaye
coauthors: Ankush Jain
description: "Hong Kong AI compliance resources: regulatory hub covering the HKMA guidance on responsible AI adoption, SFC and PCPD guidance and the PDPO, a role guide, one template and a regulatory crosswalk."
nav_order: 11
group: "Regional AI Regulatory Hub"
has_children: true
---

# Hong Kong AI Compliance

Resources for people who build, sell, audit or run AI systems in Hong Kong, with a focus on banks and other financial firms. The pages map Hong Kong guidance and law to the wiki's [control library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md). The [GCC](../11_GCC_AI_Compliance/index.md) and [EU](../12_EU_AI_Compliance/index.md) sections cover their regions in more depth and hold the general templates.

> **Verification required.** This section was compiled on 25 October 2026. The HKMA Supervisory Guidance for Responsible Adoption of Artificial Intelligence (Annex A to the HKMA circular of 15 October 2026) and the government's announcement of the GenA.I. Sandbox++ were read from the regulators' own documents on that date, using a retrieval tool rather than line by line. Every other claim comes from secondary sources or memory and is tagged accordingly. The Insurance Authority's and the MPFA's own AI material was not researched. Check the primary text before relying on any claim. This is not legal advice.

## Hong Kong's position in one line

Hong Kong has no AI law. Financial regulators set expectations through supervisory guidance and circulars: for banks, the HKMA guidance of 15 October 2026 [Verified]; for licensed corporations, the SFC circular on generative AI language models of 12 November 2024 [Reported]. The Personal Data (Privacy) Ordinance applies to personal data used by AI [Recalled].

## What is in this section

| Page | For | What it holds |
|---|---|---|
| [Hong Kong AI Regulatory Hub](01_Hong_Kong_AI_Regulatory_Hub.md) | Everyone | Instrument register, timeline, categories and roles, mapping to wiki controls, wiki coverage, verification checklist and sources |
| [Hong Kong: Role Guide](02_Role_Guide.md) | Practitioners, product companies, auditors, implementors | One guide with a part for each role |
| [HK-T1](HK-T1_HKMA_ART_Principles_Self_Assessment.md) | Banks (authorized institutions) | Self-assessment against the nine principles of the HKMA guidance |
| [Hong Kong Regulatory Crosswalk](03_Regulatory_Crosswalk.md) | GRC tooling | Instrument-to-control map with verification status, and a principle-by-principle crosswalk of the HKMA guidance; both also as CSV files |

## How claims are tagged

| Tag | Meaning |
|---|---|
| **[Verified]** | The point stated was checked against the regulator's own document, on the date given. The document was read with a retrieval tool and not line by line, so confirm the wording before you cite it. |
| **[Reported]** | Stated by secondary web sources found on 25 October 2026 (law-firm notes, press and research notes). Not read in the primary text. |
| **[Recalled]** | Stated from memory of the law or guidance and not re-checked. Verify before citing it. |
| **[Conflict]** | Secondary sources disagree. Resolve from the primary text. |
| **[Unverified]** | Single source, marketing-grade source, or not researched. |

The template is a working document, not a regulator-approved form.

## Common templates to reuse

The GCC and EU sections contain working templates that are not tied to a region. Reuse them and adapt the regional lines.

| Need | Reuse | Adapt |
|---|---|---|
| System intake and tiering | [GCC T01](../11_GCC_AI_Compliance/T01_AI_Use_Case_Intake_and_Risk_Tiering.md) or [EU T01](../12_EU_AI_Compliance/T01_AI_System_Classification.md) | Use the HKMA materiality and risk assessment (principle 4) as the tiering basis |
| Inventory | [SG-T2](../19_Singapore_AI_Compliance/SG-T2_MAS_Style_Inventory_and_Materiality.md) or [GCC T09](../11_GCC_AI_Compliance/T09_AI_System_Inventory.md) | Add the attributes HKMA principle 3 lists: purpose, owner, provider, model, risk classification, status, dependencies and key controls |
| Supplier due diligence | [GCC T03](../11_GCC_AI_Compliance/T03_Vendor_Due_Diligence_GCC_Addendum.md) or [EU T03](../12_EU_AI_Compliance/T03_Supplier_Due_Diligence_EU_Addendum.md) | Add the contract terms in HKMA principle 5 |
| Incident workflow | [GCC T05](../11_GCC_AI_Compliance/T05_AI_Incident_and_Breach_Notification_Workflow.md) | Fill in the HKMA, SFC and PCPD routes |
| Bias testing record | [GCC T10](../11_GCC_AI_Compliance/T10_Bias_Testing_Record.md) | Use as it is |
| Risk register | [GCC T12](../11_GCC_AI_Compliance/T12_Risk_Register_4x4.md) | Use as it is |

## Keeping this section current

Re-check every quarter. Watch for the HKMA discussion paper on agentic AI governance that the HKMA announced on 15 October 2026, any SFC update to its 2024 circular, and AI guidance from the Insurance Authority and the MPFA.
