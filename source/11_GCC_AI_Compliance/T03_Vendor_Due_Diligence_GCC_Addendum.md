---
title: "T03 Vendor Due-Diligence GCC Addendum"
author: Nachiket Sathaye
parent: "GCC AI Compliance"
nav_order: 11
description: "Questions to add to a third-party security questionnaire for AI suppliers: data location, model governance, security, incidents and exit."
document_type: AI Security Wiki Reference
version: 1.0
---

# T03 Vendor Due-Diligence GCC Addendum

> **Verification required.** This is a working template, not a regulator-approved form. Where it names a regional instrument, the claim comes from secondary sources and is a pointer to check, not a confirmed legal requirement. This is not legal advice.

Add to the standard third-party security questionnaire. Wiki control: [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014). Regional drivers reported: CBUAE vendor diligence expectation, NCA third-party domain, NCSA AI guidance [Reported].

Vendor: ______  Product: ______  Date: ______  Reviewer: ______

Answer Yes / No / Partial. Attach evidence. "Partial" needs a dated plan.

## A. Identity and certification

| # | Question | Answer | Evidence |
|---|---|---|---|
| A1 | Legal entity, country of incorporation, parent | | |
| A2 | Information security certification held (name, scope, expiry) | | |
| A3 | AI management certification held, if claimed (name, scope, expiry) | | |
| A4 | Any local or national seal or registration claimed (name, issuer, date) | | |

## B. Data location and handling

| # | Question | Answer | Evidence |
|---|---|---|---|
| B1 | Country of inference, storage, logs, backups, support access | | |
| B2 | Any processing outside the customer's jurisdiction? List | | |
| B3 | Sub-processors and fourth parties (name, country, role) | | |
| B4 | Is customer data used to train or improve models? | | |
| B5 | Retention of prompts and outputs; deletion on request and at exit | | |
| B6 | Encryption at rest and in transit; key control | | |
| B7 | Can the customer pin processing to an approved region? | | |

## C. Model governance

| # | Question | Answer | Evidence |
|---|---|---|---|
| C1 | Model card or equivalent (intended use, limits) | | |
| C2 | Training data provenance and licence position | | |
| C3 | Bias testing: method, last date, results sharing | | |
| C4 | Arabic support: tested dialects and quality results | | |
| C5 | Material model changes: notice period and testing | | |
| C6 | Human oversight features and kill switch / tenant disable | | |
| C7 | Explainability features for decisions about people | | |
| C8 | Content safety controls and evidence | | |

## D. Security of the AI system

| # | Question | Answer | Evidence |
|---|---|---|---|
| D1 | Prompt-injection and data-exfiltration testing | | |
| D2 | Agent and tool permission model | | |
| D3 | Penetration test date and scope | | |
| D4 | Vulnerability management SLAs | | |
| D5 | Logging and customer access to logs | | |

## E. Incident and regulator matters

| # | Question | Answer | Evidence |
|---|---|---|---|
| E1 | Incident notice to customer within how many hours? | | |
| E2 | Support for customer's regulator notifications | | |
| E3 | Past regulatory action or material breach (last 3 years) | | |
| E4 | Regulator and audit access rights granted | | |

## F. Exit and continuity

| # | Question | Answer | Evidence |
|---|---|---|---|
| F1 | Data return format and deletion certificate | | |
| F2 | Service continuity and fallback | | |
| F3 | Subcontractor failure handling | | |

## G. Decision

| Risk rating | Low / Medium / High |
|---|---|
| Conditions | |
| Contract clauses required | training-use ban, residency commitment, sub-processor notice, incident SLA, audit access, model-change notice |
| Approver / date | |
| Next review | |
