---
title: "ISO/IEC 27001 Crosswalk"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Framework Crosswalks"
nav_order: 8
description: "ISO/IEC 27001:2022 Annex A controls and management system clauses with the wiki control objectives and test cases that cite them, and the Annex A controls not yet cited."
document_type: AI Security Wiki Reference
version: 1.0
---

# ISO/IEC 27001 Crosswalk

> **Purpose:** Let a team that runs an information security management system under ISO/IEC 27001 find the wiki control objectives, evidence and test cases that extend each Annex A control to AI systems.

> **Audience:** ISMS owners, internal auditors, certification leads, GRC teams, security architects.

> **Using the two together:** Use ISO/IEC 27001 for the management system and its certification. Use this wiki for what each Annex A control has to cover once AI systems are in scope, and for the tests that show it.

## About the standard and this page

ISO/IEC 27001:2022 sets requirements for an information security management system. Its Annex A lists 93 controls in four themes: organizational (A.5.1 to A.5.37), people (A.6.1 to A.6.8), physical (A.7.1 to A.7.14) and technological (A.8.1 to A.8.34). Clauses 4 to 10 hold the management system requirements. The standard is sold by ISO and its text is copyrighted.

The standard has no AI-specific content. A wiki control cites an Annex A control when applying the wiki control to an AI system is one way to meet part of that Annex A control. For the AI management system standard, see the [ISO/IEC 42001 Crosswalk](05_ISO_IEC_42001_Crosswalk.md).

The tables are generated each time the site is built. They are read from the ISO/IEC 27001 field of each control in the [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md). To change a mapping, edit the control; this page follows on the next build.

> **Verify before use.** Control numbers and titles were written from memory of the 2022 edition and were not checked against a copy of the standard for this page. The mapping is this wiki's own judgment and has not been reviewed by ISO or a certification body. Check every number and title against your own copy before quoting it in a statement of applicability or an audit. A wiki control citing an Annex A control means it supports that control for AI systems, not that it satisfies it.

## How to read the tables

- **Wiki controls** are the control objectives whose record cites the Annex A control or clause.
- **Test cases under those controls** counts the distinct test cases that test at least one of those controls.
- An Annex A control with no name and "None" in the next column is not cited by any wiki control.

## Annex A and clauses to wiki controls

<!-- framework-crosswalk: iso-27001 -->

## Where the wiki stops

The wiki cites no physical control (A.7.1 to A.7.14). Data centre and office security for AI infrastructure is the same as for any other system, and the wiki adds nothing to it. Most people controls and the general controls for networks, endpoints, backup and malware are also left to the existing ISMS. The [Existing Security Control Baseline](../03_Control_Library/04_Existing_Security_Control_Baseline.md) is a template for assessing how far those general controls already address AI risks.

Four wiki controls cite no Annex A control: fairness and bias testing ([AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041)), output reliability ([AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039)), human oversight design ([AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045)) and risk assessment ([AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037)), which cites clauses 6.1.2 and 6.1.3 instead. An ISMS that takes AI into scope needs these from ISO/IEC 42001 or from this wiki.

## Attribution

ISO/IEC 27001:2022 is published by ISO and IEC. This page cites control numbers and titles only and does not reproduce the text of the standard.

## Related pages

- [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md)
- [ISO/IEC 42001 Crosswalk](05_ISO_IEC_42001_Crosswalk.md)
- [NIST CSF Crosswalk](09_NIST_CSF_Crosswalk.md)
- [Existing Security Control Baseline](../03_Control_Library/04_Existing_Security_Control_Baseline.md)
