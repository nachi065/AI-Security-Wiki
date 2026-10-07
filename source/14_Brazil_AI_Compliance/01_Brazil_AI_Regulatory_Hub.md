---
title: "Brazil AI Regulatory Hub"
author: Nachiket Sathaye
parent: "Brazil AI Compliance"
nav_order: 1
description: "Brazilian AI-relevant law mapped to AI security controls: the LGPD, sector rules and the pending AI bill PL 2338/2023, with verification status."
document_type: AI Security Wiki Reference
version: 1.0
---

# Brazil AI Regulatory Hub

> **Verification required.** Claims on this page about Brazilian law were compiled on 7 October 2026 from secondary web sources and from memory of the law. No primary legal text was read, and each claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

This page maps Brazilian laws, guidance and standards that bear on AI to the wiki's controls.

## 1. Regional model

There are three layers:

1. The LGPD and the ANPD, the data protection authority [Recalled].
2. Consumer and sector law.
3. A pending AI bill with risk tiers, rights and supervision, which is not enforceable yet.

Use the bill for planning, and do not build your compliance to its text [Reported].

## 2. Instrument register

| # | Instrument | Type / status | Key points | Wiki controls | Tag | To verify |
|---|---|---|---|---|---|---|
| BR1 | PL 2338/2023 (AI bill) | Pending; Senate approved 10 Dec 2024; awaiting committee opinion in the Chamber as at 2 Sep 2026 | Topics reported: risk classification, fundamental rights, governance, civil liability, supervision, penalties. The specific tiers and fines were not verified | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-041](../11_GCC_AI_Compliance/06_Proposed_Control_Fairness_Bias_Explainability.md) (proposed) | [Reported] | Chamber text; amendments |
| BR2 | LGPD (Law 13.709/2018) | Binding | Lawful bases; rights, including review of automated decisions (Art. 20); breach notice | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [Recalled] | Article numbers; ANPD rules |
| BR3 | ANPD and sector regulators advancing AI regulation | Regulator activity | Guidance and sector rules in the absence of a statute | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | [Reported] | Specific instruments |
| BR4 | Consumer Defence Code and sector rules (finance, health) | Binding | Existing duties apply to AI products | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | [Recalled] | Applicability |

## 3. Categories, tiers and roles

| Category / role | What it means |
|---|---|
| Controller / operator | LGPD roles |
| Risk classes in the pending bill | Not yet law; use as a watchlist |
| Regulated sector entity | Sector regulator duties |

## 4. Timeline

| Date | Event | Tag |
|---|---|---|
| 10 Dec 2024 | Senate approves PL 2338/2023 | [Reported] |
| 2 Sep 2026 | Chamber record: awaiting committee opinion | [Reported] |

## 5. Mapping of common wiki controls

| Wiki control | Regional hook |
|---|---|
| [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) Privacy | LGPD automated decision review ([BR-T1](BR-T1_LGPD_Automated_Decision_Review_Record.md)) |
| [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) Inventory | Prepare a tier mapping for the bill ([BR-T2](BR-T2_PL2338_Readiness_Watchlist.md)) |
| [AI-CTRL-041](../11_GCC_AI_Compliance/06_Proposed_Control_Fairness_Bias_Explainability.md) Fairness (proposed) | LGPD non-discrimination principle [Recalled] |
| [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) Incident response | LGPD breach notification [Recalled] |

## 6. Gaps to close in the wiki

- The rest of the wiki names no Brazilian instrument.
- No test case names LGPD automated decision review.
- The wiki has no tier mapping to prepare for the bill, other than [BR-T2](BR-T2_PL2338_Readiness_Watchlist.md).

## 7. Conflicts and cautions

- The bill's penalty amounts and tier definitions were not verified.
- The bill's text may change in the Chamber.
- A contract that refers to "Brazil's AI law" refers to an obligation that does not exist yet.

## 8. Verification checklist

- [ ] Chamber progress
- [ ] Senate text
- [ ] LGPD article text
- [ ] ANPD AI regulation agenda
- [ ] Sector regulator instruments
- [ ] Add the primary URL and retrieval date beside every confirmed row

## 9. Sources

All sources are secondary unless marked as a regulator or government page. Each fetched page was summarised by a tool and was not read line by line. A source marked "not read" appeared only as a title or snippet in search results, so do not treat it as support for any claim.

| Source | Status | Rows it relates to |
|---|---|---|
| [CASRAI: Brazil AI bill PL 2338 status](https://casrai.org/guides/brazil-ai-bill-pl-2338-status) | Fetched and summarised (the source dates the Chamber record 2 Sep 2026) | BR1, BR2 |
| [Tozzini Freire: ANPD and sector regulators advance AI regulation](https://tozzinifreire.com.br/en/artigos/sem-marco-legal-anpd-e-setores-avancam-na-regulacao-da-ia) | Not read | BR3 |
| [Barbieri Advogados: PL 2338 vs EU AI Act](https://www.barbieriadvogados.com/brazil-ai-act/) | Not read | BR1 content |

No primary legal text (statute, regulation or circular) was read for any row. Confirm each row against the primary source, and add its URL and retrieval date in the [Brazil Regulatory Crosswalk](03_Regulatory_Crosswalk.md).
