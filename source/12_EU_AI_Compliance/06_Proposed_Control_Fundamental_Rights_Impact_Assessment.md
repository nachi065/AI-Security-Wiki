---
title: "Proposed Control: Fundamental Rights and Data Protection Impact Assessment"
author: Nachiket Sathaye
parent: "EU AI Compliance"
nav_order: 6
description: "Proposed AI-CTRL-042: assess the impact on people's rights before deploying high-risk AI, plus the EU drivers for the proposed fairness control AI-CTRL-041."
document_type: AI Security Wiki Reference
version: 1.0
---

# Proposed Control: Fundamental Rights and Data Protection Impact Assessment

> **Status: proposed.** This control is not yet part of the [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md). [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) asks for a privacy impact assessment where an AI system processes personal data, and no existing control asks for a fundamental rights impact assessment. The EU drivers listed below are tagged [Recalled] or [Reported]; check the primary text before relying on them. This is not legal advice.

| Field | Detail |
|---|---|
| Control ID | AI-CTRL-042 (proposed) |
| Name | Fundamental Rights and Data Protection Impact Assessment |
| Family | Governance and Compliance |
| Control Objective | Assess the impact on individuals' rights before deploying AI that is high-risk or that processes personal data in a way that puts people at risk, and keep the assessment current. |
| Implementation Expectation | 1. Run a combined DPIA and FRIA ([T02](T02_Impact_Assessment_FRIA_DPIA.md)) before go-live for in-scope systems. 2. Record purpose, data, groups affected, risks, oversight, mitigation, consultation and decision. 3. Reassess on material change. |
| Evidence Required | Completed [T02](T02_Impact_Assessment_FRIA_DPIA.md); DPO advice; approval; review dates. |
| Audit Test Procedure | Sample systems. Confirm the assessment predates go-live. Check that each risk maps to a mitigation. Confirm that a change triggers reassessment. |
| Control Owner | DPO with AI Governance Lead |
| Review Frequency | Before deployment, at least annually, and on change |
| EU drivers | GDPR Art. 35 [Recalled]; AI Act Art. 27 FRIA for certain deployers [Recalled; scope to verify] |
| Related controls | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) |

## EU drivers for AI-CTRL-041

[AI-CTRL-041](../11_GCC_AI_Compliance/06_Proposed_Control_Fairness_Bias_Explainability.md) (Fairness, Bias Testing and Explainability) is proposed in the GCC section, and the same control serves EU use. The EU rules add the following to that card.

| Field | EU addition |
|---|---|
| Implementation Expectation | Where special category data is needed for bias testing, record the strict-necessity test and the safeguards. |
| Evidence Required | The necessity record. |
| EU drivers | AI Act data governance and bias examination (Art. 10) and the right to explanation (Art. 86) [Recalled]; GDPR Art. 22 [Recalled]; the strict-necessity standard for special category data, reported as retained by the omnibus [Reported]. |
| Related cases | [TC-L03-008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008), [TC-L03-029](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-029) |

## Proposed test cases

These tests have no case IDs yet. They would be numbered in the L03 series if the controls are adopted. For AI-CTRL-041, tests 1, 2, 4 and 5 on [its page](../11_GCC_AI_Compliance/06_Proposed_Control_Fairness_Bias_Explainability.md#proposed-test-cases) apply unchanged, and the EU drivers add the first test below.

| # | Control | Test | Pass condition |
|---|---|---|---|
| 1 | AI-CTRL-041 | Special category data used for bias testing | Necessity record and safeguards on file |
| 2 | AI-CTRL-042 | Assessment predates go-live | Dates verified |
| 3 | AI-CTRL-042 | DPO advice recorded | Advice on file |
| 4 | AI-CTRL-042 | Reassessment triggered by change | Change log links to the reassessment |
