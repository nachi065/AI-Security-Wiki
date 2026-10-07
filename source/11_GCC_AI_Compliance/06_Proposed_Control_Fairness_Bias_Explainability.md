---
title: "Proposed Control: Fairness, Bias Testing and Explainability"
author: Nachiket Sathaye
parent: "GCC AI Compliance"
nav_order: 6
description: "Proposed AI-CTRL-041: test AI systems that make high-impact decisions for unfair bias, and keep explanations people can understand and challenge."
document_type: AI Security Wiki Reference
version: 1.0
---

# Proposed Control: Fairness, Bias Testing and Explainability

> **Status: proposed.** This control is not yet part of the [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md). None of the 40 existing controls covers fairness or bias testing. The nearest are [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) (Output Reliability and Content Safety) and the test cases [TC-L03-008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008) and [TC-L03-029](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-029). The regional drivers listed below come from secondary sources and are tagged [Reported]; check the primary text before relying on them. This is not legal advice.

| Field | Detail |
|---|---|
| Control ID | AI-CTRL-041 (proposed) |
| Name | Fairness, Bias Testing and Explainability |
| Family | Assurance and Testing |
| Control Objective | Test AI systems that make or support high-impact decisions for unfair bias, and keep explanations that a person can understand and a reviewer can challenge. |
| Implementation Expectation | 1. Define high-impact decisions. 2. Identify relevant groups with legal input. 3. Test before release, annually and on material model change. 4. Record method, data, thresholds, results and approvals. 5. Provide an explanation per high-impact decision and a route to human review. 6. Block or condition release on failed thresholds. |
| Evidence Required | Bias test plan and results ([T10](T10_Bias_Testing_Record.md)); threshold approvals; explanation records; human-review log; retest evidence. |
| Audit Test Procedure | Sample high-impact use cases. Confirm a current bias test exists. Re-perform one test. Trace one decision to explanation and review outcome. Confirm failed results led to action. |
| Control Owner | AI Governance Lead / Model Risk |
| Review Frequency | Annually and on material model change |
| Regional drivers | CBUAE Guidance Note (annual bias testing) [Reported]; UAE and SDAIA ethics principles (fairness) [Reported]; DIFC Reg 10 [Reported]; QCB guideline [Reported]. |
| NIST AI RMF | To be assigned by assessor (MEASURE function) |
| ISO/IEC 42001 | To be assigned by assessor |
| Related cases | [TC-L03-008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008), [TC-L03-029](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-029) |

The EU drivers for this control, and one further test for special category data, are on the [EU proposed control page](../12_EU_AI_Compliance/06_Proposed_Control_Fundamental_Rights_Impact_Assessment.md#eu-drivers-for-ai-ctrl-041).

## Proposed test cases

These tests have no case IDs yet. They would be numbered in the L03 series if the control is adopted.

| # | Test | Pass condition |
|---|---|---|
| 1 | Bias test exists for each high-impact system | Current test with named method and thresholds |
| 2 | Bias test re-run on material model change | Dated after change record |
| 3 | Arabic vs English quality parity | Documented gap within approved threshold |
| 4 | Explanation produced for adverse decision | Understandable explanation delivered |
| 5 | Human review can reverse outcome | Reversal path evidenced |
| 6 | Failed threshold blocks release | Release record shows block or condition |
| 7 | Group definition reviewed by legal | Legal sign-off on attributes and proxies |
| 8 | Test data handling lawful | DPO approval for use of sensitive attributes |
