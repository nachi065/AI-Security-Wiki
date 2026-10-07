---
title: "T12 AI Risk Register (4x4)"
author: Nachiket Sathaye
parent: "GCC AI Compliance"
nav_order: 20
description: "Likelihood and impact scales, rating bands and a register layout for AI risks, with two example rows."
document_type: AI Security Wiki Reference
version: 1.0
---

# T12 AI Risk Register (4x4)

> **Verification required.** This is a working template, not a regulator-approved form. Where it names a regional instrument, the claim comes from secondary sources and is a pointer to check, not a confirmed legal requirement. This is not legal advice.

Wiki control: [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037). SDAIA-P145 is reported to use a likelihood-impact matrix applied proportionally [Reported; publication date in conflict]. Its category names and scales were not seen, so this register is modelled on the generic idea only; map to the official scales once you have the text.

## Scales (adjust with your risk function)

| Score | Likelihood | Impact |
|---|---|---|
| 1 | Rare | Minor, no harm |
| 2 | Possible | Moderate, limited harm, reversible |
| 3 | Likely | Major, harm to individuals or regulatory breach |
| 4 | Almost certain | Severe, serious harm, legal or licence consequences |

## Rating

Score = Likelihood x Impact.

| Score | Rating | Action |
|---|---|---|
| 1 to 3 | Low | Accept, monitor |
| 4 to 8 | Medium | Mitigate, owner and date |
| 9 to 12 | High | Mitigate before release; governance lead approval |
| 13 to 16 | Critical | Do not release or stop; executive decision |

## Register

| Risk ID | System ID | Risk description | Category | Cause | Likelihood | Impact | Score | Rating | Existing controls | Planned actions | Owner | Due | Residual score | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Suggested categories

Fairness; Privacy; Security; Reliability; Safety and harmful content; Transparency; Third-party; Regulatory; Legal and IP; Operational resilience; Reputational.

## Example rows (illustrative)

| Risk ID | System ID | Risk description | Category | Cause | Likelihood | Impact | Score | Rating | Existing controls | Planned actions | Owner | Due | Residual score | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R-001 | AI-0007 | Loan pre-screen disadvantages a nationality group | Fairness | Skewed training data | 2 | 4 | 8 | Medium | Annual bias test | Quarterly test; threshold approval | Model risk lead | 2026-12-31 | 4 | Open |
| R-002 | AI-0012 | Customer prompts stored outside approved region | Privacy | Vendor default logging | 3 | 3 | 9 | High | None | Region pinning; [T04](T04_Data_Residency_Attestation.md) | CISO | 2026-11-15 | 3 | Open |
