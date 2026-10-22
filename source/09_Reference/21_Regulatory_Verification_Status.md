---
title: "Regulatory Verification Status"
author: Nachiket Sathaye
parent: "Reference"
nav_order: 4
description: "How far the wiki's regulatory claims have been checked against primary legal texts: verification counts for every regional crosswalk, the order in which regions are verified, and an obligation-level tracker that starts with the EU AI Act."
document_type: AI Security Wiki Reference
version: 1.0
---

# Regulatory Verification Status

> **Purpose:** Show, in one place, how much of the wiki's regulatory content has been checked against the primary legal text, and track that checking obligation by obligation rather than law by law.

> **Audience:** Anyone relying on a regional section for a client or a compliance decision; contributors who verify legal content.

> **Verify before use:** A claim tagged [Verified] was read in the primary source on the date shown beside it. Every other tag means the claim still needs checking before anyone relies on it. Laws change; a [Verified] row can go out of date. This page is not legal advice.

## What the tags mean

| Tag | Meaning |
|---|---|
| [Verified] | Read in the primary source (the law, the official journal, or the issuing body's own page); source and retrieval date recorded beside the row. |
| [Reported] | Taken from a reliable secondary source, such as the issuing body's press release or a law firm briefing, but the primary text was not read. |
| [Recalled] | Written from memory of the source, without a source to hand. |
| [Unverified] | Not checked at all. |
| [Conflict] | Primary sources disagree; both are cited. |

## Status by region

Counted from the Verification tag column of each section's Regulatory Crosswalk every time the site is built. "Partly verified" is a row that carries [Verified] for some parts and another tag for the rest.

<!-- verification-status -->

A crosswalk row usually covers a whole law or a group of articles. A row tagged [Verified] means the facts on that row (title, status, dates) were checked; it does not mean every obligation in the law has been read. That is why the tracker below works at the level of single obligations.

## Order of verification

Verification effort goes first where it matters most to the people using the wiki. The order below is a working assumption based on the regions this wiki covers most deeply (the GCC and EU sections are the largest, and many test cases carry UAE framework crosswalk fields). Change it to match the jurisdictions you or your clients operate in.

1. **GCC, starting with the UAE**: the largest crosswalk, and one of the least verified.
2. **EU**: the AI Act obligations that apply to deployers and to high-risk systems.
3. **UK and US**: the instruments that create duties today, before guidance and proposals.
4. **India**.
5. **All other regions.**

Within a region, verify in this order: obligations that are already in force; obligations with a deadline in the next 12 months; obligations that carry penalties; then guidance and proposals.

## Obligation-level tracker

One row per obligation: who it applies to, what it requires, the article, when it applies, and whether that single obligation has been read in the primary text. When an obligation is read, update its row with the date and the exact article reference, and update the tag on the crosswalk row it belongs to if that changes.

### EU AI Act: obligations under crosswalk row E1c (high-risk systems) and related rows

The crosswalk rows E1, E1a, E1b, E1c and E1d of the [EU Regulatory Crosswalk](../12_EU_AI_Compliance/07_Regulatory_Crosswalk.md) are tagged [Verified] for their dates and status, read in Regulation (EU) 2024/1689 and the amending Regulation (EU) 2026/1744 on 10 October 2026. Row E1c bundles more than twenty articles into one row. The table below splits it.

On 22 October 2026 an attempt to read the individual articles on EUR-Lex for this tracker returned only the recitals, not the articles. So no obligation below has yet been checked one by one. The article titles in the second column are recalled and must be checked against the text; the application dates are those already verified at row level.

| # | Obligation | Applies to | Article (recalled) | Applies from (row level, verified) | Obligation-level check |
|---|---|---|---|---|---|
| EU-O1 | Establish and maintain a risk management system for the high-risk system | Providers | Art. 9 | Annex III systems 2 Dec 2027; Annex I systems 2 Aug 2028 | Not yet read |
| EU-O2 | Data and data governance for training, validation and testing data | Providers | Art. 10 | As EU-O1 | Not yet read |
| EU-O3 | Technical documentation | Providers | Art. 11 | As EU-O1 | Not yet read |
| EU-O4 | Record-keeping: automatic logging capability | Providers | Art. 12 | As EU-O1 | Not yet read |
| EU-O5 | Transparency and information to deployers (instructions for use) | Providers | Art. 13 | As EU-O1 | Not yet read |
| EU-O6 | Human oversight designed into the system | Providers | Art. 14 | As EU-O1 | Not yet read |
| EU-O7 | Accuracy, robustness and cybersecurity | Providers | Art. 15 | As EU-O1 | Not yet read |
| EU-O8 | Provider obligations, including a quality management system | Providers | Arts. 16 and 17 | As EU-O1 | Not yet read |
| EU-O9 | Deployer obligations: use according to instructions, assign human oversight, monitor operation, keep logs, inform workers and affected persons where required | Deployers | Art. 26 | As EU-O1 | Not yet read. The log retention period for deployers must be read here before the [log retention baseline](../08_Governance/18_AI_Operating_Defaults.md#log-retention-baseline) is relied on in the EU. |
| EU-O10 | Fundamental rights impact assessment for certain deployers before first use | Certain deployers | Art. 27 | As EU-O1 | Not yet read. Check whether the omnibus amended this article. |
| EU-O11 | Conformity assessment, declaration of conformity, CE marking and registration | Providers (registration also for certain deployers) | Arts. 43 to 49 | As EU-O1 | Not yet read |
| EU-O12 | Post-market monitoring | Providers | Art. 72 | As EU-O1 | Not yet read |
| EU-O13 | Reporting of serious incidents, with time limits | Providers | Art. 73 | As EU-O1 | Not yet read. The time limits must be read here before an incident playbook relies on them. |
| EU-O14 | AI literacy | Providers and deployers | Art. 4 (row E1b) | 2 Feb 2025; reworded by the omnibus | Row verified 10 Oct 2026; amended wording not yet quoted in the wiki |
| EU-O15 | Prohibited practices | Everyone placing on the market or using | Art. 5 (row E1a) | 2 Feb 2025; new points (ba) and (bb) from 2 Dec 2026 | Row verified 10 Oct 2026; the full list is still marked to verify on the crosswalk |
| EU-O16 | Transparency for certain AI systems (interaction, synthetic content, deepfakes) | Providers and deployers | Art. 50 (row E1d) | 2 Aug 2026; 2 Dec 2026 for Art. 50(2) for systems already on the market | Row partly verified; general date reported |

### Template for other regions

Copy this table into the tracker for the next region in the order above.

| # | Obligation | Applies to | Instrument and provision | In force or applies from | Penalty or consequence | Obligation-level check (date, source URL) | Crosswalk row |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## How to verify a row

1. Open the primary source: the official journal, the legislation portal or the issuing body's own page. A news article, a law firm briefing or an AI-generated summary is not a primary source.
2. Read the provision itself, not a summary of it.
3. Record the exact provision, the date you read it and the URL, and quote the key words where they decide the obligation (for example a deadline).
4. Update the tag on the crosswalk row, and note in the [Update Notes](19_Update_Notes.md) what changed.
5. If two primary sources disagree, tag the row [Conflict] and cite both.

The weekly crosswalk check recorded in the Update Notes is where rows move from one tag to another. This tracker adds the obligation-level detail for the regions at the top of the order.
