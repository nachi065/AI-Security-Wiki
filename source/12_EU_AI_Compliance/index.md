---
title: "EU AI Compliance"
author: Nachiket Sathaye
description: "EU AI compliance resources: AI Act timeline and regulatory hub, role guides, 12 fill-in templates, control drivers and a crosswalk."
nav_order: 11
group: "Regional AI Regulatory Hub"
has_children: true
---

# EU AI Compliance

Resources for people who build, sell, deploy, audit or govern AI systems that touch the EU. The pages map the AI Act, GDPR and related EU laws, guidance and standards to the wiki's [control library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md) and [test cases](../10_Test_Case_Library/index.md). The [GCC AI Compliance](../11_GCC_AI_Compliance/index.md) section does the same for the Gulf states.

> **Verification required.** Everything in this section about laws, dates, article numbers and penalties was compiled on 7 October 2026 from two kinds of source. The first is secondary web sources (law-firm notes, vendor blogs and research notes), which disagree in places. The second is memory of the text of Regulation (EU) 2024/1689 and related laws. The Official Journal text was not read, and the Digital Omnibus may have amended some provisions. Check EUR-Lex before relying on any claim. This is not legal advice.

## What is in this section

| Part | Pages | What it holds |
|---|---|---|
| [EU AI Regulatory Hub](01_EU_AI_Regulatory_Hub.md) | 1 | The AI Act timeline, risk tiers, roles and high-risk obligations, plus 18 related instruments, each mapped to wiki controls and tagged with its verification status. |
| Role guides | 4 | What to do and what to keep as evidence, for [practitioners](02_Guide_AI_Practitioners.md), [product companies](03_Guide_Product_Companies.md), [auditors](04_Guide_Auditors.md) and [implementors](05_Guide_Implementors.md). |
| Templates T01 to T12 | 12 | Fill-in documents: system classification, impact assessment, supplier addendum, transfer record, incident workflow, transparency notice, literacy record, audit checklist, inventory, technical documentation index, authority log and general-purpose AI model checklist. |
| [EU drivers for AI-CTRL-041 and AI-CTRL-042](06_Proposed_Control_Fundamental_Rights_Impact_Assessment.md) | 1 | The EU instruments behind the controls on impact assessment and on fairness, with their templates and test cases. |
| [EU Regulatory Crosswalk](07_Regulatory_Crosswalk.md) and [EU Evidence Register](08_Evidence_Register.md) | 2 | The instrument-to-control map and a starter evidence list, each also downloadable as a CSV file. |

## How claims are tagged

| Tag | Meaning |
|---|---|
| **[Reported]** | Stated by secondary web sources. Verify before relying on it. |
| **[Recalled]** | Stated from memory of the legal text and not re-checked. Verify the article on EUR-Lex before citing it. |
| **[Conflict]** | Secondary sources disagree. Resolve from the primary text. |
| **[Unverified]** | Single source, or not researched. |

The templates are working documents, not regulator-approved forms. Where a template cites an article, treat that as a pointer to check.

## AI Act dates have moved

The AI Act's high-risk dates are reported to have moved under the "Digital Omnibus on AI" [Reported]: Annex III systems to 2 December 2027, and Annex I product-embedded systems to 2 August 2028. Sources conflict on whether the omnibus is already in force. One says it is Regulation (EU) 2026/1744, in force since 27 July 2026. Another describes a provisional agreement only. See [section 2 of the hub](01_EU_AI_Regulatory_Hub.md#2-ai-act-timeline).

## Where to start

| If you are | Read | Then use |
|---|---|---|
| A data scientist, ML or security engineer | [Guide for AI Practitioners](02_Guide_AI_Practitioners.md) | [T01](T01_AI_System_Classification.md), [T02](T02_Impact_Assessment_FRIA_DPIA.md), [T10](T10_Technical_Documentation_and_Conformity_Checklist.md) |
| A provider or SaaS vendor selling into the EU | [Guide for AI Product Companies](03_Guide_Product_Companies.md) | [T01](T01_AI_System_Classification.md), [T10](T10_Technical_Documentation_and_Conformity_Checklist.md), [T12](T12_GPAI_Model_Checklist.md), [T06](T06_Transparency_Notice.md) |
| An internal or external auditor | [Guide for Auditors](04_Guide_Auditors.md) | [T08](T08_Audit_Checklist.md), [EU Evidence Register](08_Evidence_Register.md) |
| A programme lead, GRC lead, CISO or DPO | [Guide for Implementors](05_Guide_Implementors.md) | [EU AI Regulatory Hub](01_EU_AI_Regulatory_Hub.md), [T09](T09_AI_System_Inventory.md), [T07](T07_AI_Literacy_Programme_Record.md) |

## Using the templates

Templates T01 to T12 are fill-in documents. To reuse one, open the page, follow the "Suggest an edit to this page" link in the footer to reach its Markdown source on GitHub, and copy it into your own repository or document tool.

## Keeping this section current

The AI Act timeline is still moving. Re-check the hub every month until the standards and guidelines settle. When you confirm an instrument against its primary text, record the primary URL and the retrieval date beside it in the [EU Regulatory Crosswalk](07_Regulatory_Crosswalk.md).
