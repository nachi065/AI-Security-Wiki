---
title: "GCC Drivers for AI-CTRL-041: Fairness, Bias Testing and Explainability"
author: Nachiket Sathaye
parent: "GCC AI Compliance"
nav_order: 6
description: "The GCC instruments behind AI-CTRL-041 on fairness, bias testing and explainability, with the template and test cases that support the control."
document_type: AI Security Wiki Reference
version: 1.1
---

# GCC Drivers for AI-CTRL-041: Fairness, Bias Testing and Explainability

> **How this relates.** [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) is part of the [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md). This page lists the GCC instruments that call for it. They come from secondary sources and are tagged [Reported]; check the primary text before relying on them. This is not legal advice.

| Field | Detail |
|---|---|
| Control | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) Fairness, Bias Testing and Explainability |
| GCC drivers | CBUAE Guidance Note (annual bias testing) [Reported]; UAE and SDAIA ethics principles (fairness) [Reported]; DIFC Reg 10 [Reported]; QCB guideline [Reported] |
| Template | [T10 Bias Testing Record](T10_Bias_Testing_Record.md) |
| Test cases | [TC-L03-031](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-031), [TC-L03-032](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-032), [TC-L03-033](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-033), [TC-L03-008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008), [TC-L03-029](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-029) |

## Test cases by topic

| Topic | Test case |
|---|---|
| A current bias test exists for each high-impact system, and a failed threshold blocks release | [TC-L03-031](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-031) |
| The bias test is re-run on material model change | [TC-L03-031](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-031) |
| Arabic and English quality parity | [TC-L03-033](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-033) |
| An explanation is produced for an adverse decision | [TC-L03-029](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-029) |
| Human review can reverse the outcome | [TC-L03-008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008) |
| Legal reviews the group definition, and the use of sensitive attributes in testing is lawful | [TC-L03-032](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-032) |

The EU instruments behind this control are on the [EU drivers page](../12_EU_AI_Compliance/06_Proposed_Control_Fundamental_Rights_Impact_Assessment.md#eu-drivers-for-ai-ctrl-041).
