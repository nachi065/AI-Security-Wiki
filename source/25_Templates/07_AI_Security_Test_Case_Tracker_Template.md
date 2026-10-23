---
title: "AI Security Test Case Tracker Template (.xlsx)"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Templates"
nav_order: 7
description: "A downloadable Excel tracker for AI security testing: the wiki's quick-start PoC scenarios and every case in the Test Case Library, with columns to select, run, score and evidence each one, and coverage by control and by register risk."
document_type: AI Security Wiki Template
version: 1.1
---

# AI Security Test Case Tracker Template (.xlsx)

**[Download the AI Security Test Case Tracker Template (.xlsx)](AI_Security_Test_Case_Tracker.xlsx)**

> **Purpose:** Plan, run and record AI security tests: the 20 quick-start PoC scenarios and all {{n:tests}} cases in the [Test Case Library](../10_Test_Case_Library/index.md) across {{n:layers}} layers and {{n:domains}} domains, with coverage by control and by register risk.

> **Audience:** Security testers, red teams, PoC evaluators and control owners.

> **Before you rely on it:** Use synthetic, non-functional or clearly marked test data only, and do not run these tests against production systems. The cases are a snapshot copied from the wiki on 22 October 2026; the Wiki Link column opens each case so you can check it for later changes.

## What is in the workbook

| Sheet | What it holds | Built from |
|---|---|---|
| README and License | How to use the workbook, colour legend, sources, licence, credit and disclaimer | Written for the workbook |
| Summary | Results by layer and the open checks | Calculated from the other sheets |
| Test Plan | Product, environment, testers, dates, the scoring scale and the safety boundary | [AI Security PoC Test Case Library](../06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md) |
| Quick-Start PoC | The 20 PoC scenarios with tracking columns | [AI Security PoC Test Case Library](../06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md) |
| Test Cases | The {{n:tests}} cases with procedure, expected result and evidence, every shared field filled in (preconditions, pass and fail criteria, scoring, expected log, audit and compliance evidence, reviewer notes) so each row stands on its own, the case's validation level, and columns to select, run and score each one | [Test Case Library](../10_Test_Case_Library/index.md), [Standard Fields](../10_Test_Case_Library/standard-fields.md) |
| Control Coverage and Risk Coverage | Cases, runs and results for each control and each register risk | [Risk, Control and Test Traceability](../02_Risk_Management/02G_Risk_Control_Test_Traceability.md), [AI Risk to Control Mapping](../02_Risk_Management/02D_AI_Risk_to_Control_Mapping.md) |

## How to use it

1. **Test Plan.** Record the product, environment, testers and dates.
2. **Quick-Start PoC.** Run the 20 scenarios first.
3. **Test Cases.** Filter to the layers, domains or controls in scope, set Selected to Yes, then run and score each case.
4. **Fix gaps.** Clear every Score Check message: add an evidence reference, record a finding for a 0 or 3, and cap vendor-evidence scores at 3.
5. **Coverage.** Use Control Coverage and Risk Coverage to see what has been tested and what failed.
6. **Summary.** Report results by layer and the open checks.

## How the scoring works

Scores use the wiki scale of 5, 3, 0 or N/A. Evidence from vendor documentation or demo data, rather than the live PoC, scores no higher than 3, and the Score Check column flags any score that breaks that rule.

## Licence and credit

The workbook is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), like the rest of the wiki. Suggested credit: "AI Security Test Case Tracker" by Nachiket Sathaye and Ankush Jain, AI Security Wiki, licensed under CC BY-SA 4.0. If you share an adapted version, say what you changed and release it under the same licence. Framework names, identifiers and short titles belong to their owners and are cited for mapping only.
