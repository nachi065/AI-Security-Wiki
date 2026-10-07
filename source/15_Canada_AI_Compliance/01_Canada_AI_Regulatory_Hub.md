---
title: "Canada AI Regulatory Hub"
author: Nachiket Sathaye
parent: "Canada AI Compliance"
nav_order: 1
description: "Canadian AI-relevant law mapped to AI security controls: PIPEDA, Quebec Law 25, the federal automated decision directive, OSFI E-23 and pending bills."
document_type: AI Security Wiki Reference
version: 1.0
---

# Canada AI Regulatory Hub

> **Verification required.** Claims on this page about Canadian law were compiled on 7 October 2026 from secondary web sources and from memory of the law. No primary legal text was read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

This page maps Canadian laws, guidance and standards that bear on AI to the wiki's controls.

## 1. Regional model

There are four layers [Reported]:

1. Privacy law, federal and provincial.
2. The Treasury Board Directive on Automated Decision-Making, for federal institutions and their vendors.
3. OSFI Guideline E-23, for federally regulated financial institutions.
4. A voluntary code on generative AI.

One source says to remove any "January 1, 2027 Canadian AI Act" entry from calendars [Reported].

## 2. Instrument register

| # | Instrument | Type / status | Key points | Wiki controls | Tag | To verify |
|---|---|---|---|---|---|---|
| CA1 | Artificial Intelligence and Data Act (Bill C-27) | Lapsed 6 Jan 2025; not resurrected as drafted | No federal AI statute | None | [Reported] | New bills |
| CA2 | PIPEDA | Binding federal privacy law | Purpose limitation when data is repurposed for training; consent | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [Reported] | OPC guidance |
| CA3 | Quebec Law 25 | Binding | Notice of automated decisions, explanation on request, human review | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-041](../11_GCC_AI_Compliance/06_Proposed_Control_Fairness_Bias_Explainability.md) (proposed) | [Reported] | Section numbers |
| CA4 | Treasury Board Directive on Automated Decision-Making; Algorithmic Impact Assessment (AIA) | Binding for federal institutions; flows down to vendors | Impact assessment, and controls set by impact level | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [Reported] | Current version |
| CA5 | Voluntary Code of Conduct on generative AI (ISED) | Voluntary | Safety, accountability, transparency, fairness, human oversight, validity | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [Reported] | Signatories |
| CA6 | OSFI Guideline E-23 | Guidance for federally regulated financial institutions | AI and ML model risk management | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [Unverified] | Final effective date |
| CA7 | Bills C-34 (digital safety, including AI chatbots) and C-36 (privacy reform) | Bills | Possible near-term obligations | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | [Unverified] | Bill numbers and status; single source |
| CA8 | Provincial public-sector AI rules (for example Ontario) | Varies | Duties for public bodies | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | [Unverified] | Details |

## 3. Categories, tiers and roles

| Category / role | What it means |
|---|---|
| Federal institution or its vendor | The Directive applies through procurement |
| Private-sector organisation | PIPEDA and provincial privacy laws |
| Federally regulated financial institution | OSFI model risk expectations |
| Quebec operations | Law 25 automated decision duties |
| No statutory AI tiers | Use the AIA impact levels as a reference |

## 4. Timeline

| Date | Event | Tag |
|---|---|---|
| 6 Jan 2025 | AIDA lapses | [Reported] |

## 5. Mapping of common wiki controls

| Wiki control | Regional hook |
|---|---|
| [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) Privacy | PIPEDA and Law 25 ([CA-T2](CA-T2_Quebec_Law_25_ADM_Record.md)) |
| [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) Inventory | OSFI E-23 inventory ([CA-T3](CA-T3_OSFI_E23_Inventory_Addendum.md)) |
| [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) Risk | AIA impact levels ([CA-T1](CA-T1_Algorithmic_Impact_Assessment_Worksheet.md)) |
| [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) Human approval | Law 25 human review |
| [AI-CTRL-041](../11_GCC_AI_Compliance/06_Proposed_Control_Fairness_Bias_Explainability.md) Fairness (proposed) | Human rights law and the AIA |
| [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) Content safety | Voluntary code |

## 6. Where the wiki covers this

The topics raised on this page are covered by the following controls, test cases and templates.

| Topic | Covered by |
|---|---|
| Quebec Law 25 automated decisions | [CA-T2](CA-T2_Quebec_Law_25_ADM_Record.md); [TC-L01-011](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-011), [TC-L03-008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008), [TC-L03-029](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-029) |
| Algorithmic impact assessment | [CA-T1](CA-T1_Algorithmic_Impact_Assessment_Worksheet.md); [TC-L03-010](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-010), [TC-L03-011](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-011) |
| OSFI model risk and inventory | [CA-T3](CA-T3_OSFI_E23_Inventory_Addendum.md); [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011); [TC-L01-001](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-001), [TC-L02-013](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-013) |
| PIPEDA purpose limits on training data | [TC-L03-015](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-015) |

## 7. Conflicts and cautions

- The bill numbers C-34 and C-36 come from a single source.
- The effective date of OSFI E-23 is not confirmed.
- The federal bills may have changed since the sources were written.

## 8. Verification checklist

- [ ] Current federal bills
- [ ] Law 25 text
- [ ] Directive version and AIA questionnaire
- [ ] OSFI E-23 final text and date
- [ ] OPC guidance on AI
- [ ] Add the primary URL and retrieval date beside every confirmed row

## 9. Sources

All sources are secondary unless marked as a regulator or government page. Each fetched page was summarised by a tool and was not read line by line. A source marked "not read" appeared only as a title or snippet in search results, so do not treat it as support for any claim.

| Source | Status | Rows it relates to |
|---|---|---|
| [Compliance Hub wiki: Canada AI regulation 2026](https://compliancehub.wiki/canada-ai-regulation-2026-no-ai-act-what-actually-applies/) | Fetched and summarised (the single source for CA1 to CA7) | CA1 to CA7 |
| [BLG: A turning point for AI in Canada in 2026](https://blg.com/en/insights/2026/03/a-turning-point-for-ai-in-canada-in-2026) | Not read; the fetch was refused | Intended to confirm the bills and OSFI rows |

No primary legal text (statute, regulation or circular) was read for any row. Confirm each row against the primary source, and add its URL and retrieval date in the [Canada Regulatory Crosswalk](03_Regulatory_Crosswalk.md).
