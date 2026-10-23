---
title: "SOC 2 Crosswalk"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Framework Crosswalks"
nav_order: 11
description: "The SOC 2 Trust Services Criteria with the wiki control objectives and test cases that cite them, for service organizations that put AI systems in the scope of a SOC 2 report."
document_type: AI Security Wiki Reference
version: 1.0
---

# SOC 2 Crosswalk

> **Purpose:** Let a service organization that puts AI systems in the scope of a SOC 2 examination find the wiki control objectives, evidence and test cases that support each criterion.

> **Audience:** Compliance leads at AI product and SaaS companies, service auditors, vendor risk teams that read SOC 2 reports.

> **Using the two together:** Use SOC 2 for the independent report your customers ask for. Use this wiki to decide which controls to describe for the AI parts of the system, and what evidence the auditor can test.

## About SOC 2 and this page

A SOC 2 report is an examination by an independent auditor of a service organization's controls, measured against the Trust Services Criteria published by the AICPA. The criteria in use are the 2017 set with points of focus revised in 2022. A Type I report covers the design of controls at a date. A Type II report also covers how they operated over a period, so "SOC 2 Type II" names a kind of report and the criteria behind it are the same.

There are five categories. Security is required in every report and is covered by the common criteria, CC1 to CC9. Availability (A1), confidentiality (C1), processing integrity (PI1) and privacy (P1 to P8) are added when the report's scope includes them. This page lists 61 criteria across the five.

The tables are generated each time the site is built. They are read from the SOC 2 field of each control in the [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md). To change a mapping, edit the control; this page follows on the next build.

> **Verify before use.** Criteria numbers were written from memory and were not checked against the AICPA publication for this page. The label beside each number is this wiki's own short description, because the criteria text belongs to the AICPA. The mapping is this wiki's own judgment and has not been reviewed by the AICPA or a service auditor. Agree the controls and criteria in your report with your auditor.

## How to read the tables

- **Wiki controls** are the control objectives whose record cites the criterion.
- **Test cases under those controls** counts the distinct test cases that test at least one of those controls.
- A criterion with no name and "None" in the next column is not cited by any wiki control.

## Criteria to wiki controls

<!-- framework-crosswalk: soc-2 -->

## Reading a vendor's SOC 2 report for AI

A SOC 2 report covers the system its description names. An AI feature added after the examination period, or a model provider used as a subservice organization and carved out of the report, is outside it. [TC-L16-009](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-009) tests whether a vendor's assurance evidence reaches the AI service you are buying, and [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) sets the assessment it belongs to.

The criteria do not address fairness, human oversight or intellectual property, so the wiki controls for those cite no criterion.

## Attribution

The Trust Services Criteria are published and copyrighted by the AICPA. This page cites criteria numbers only and does not reproduce the criteria or their points of focus.

## Related pages

- [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md)
- [ISO/IEC 27001 Crosswalk](08_ISO_IEC_27001_Crosswalk.md)
- [AI Security Vendor Evaluation Master Framework](../05_Vendor_Evaluation/11_AI_Security_Vendor_Evaluation_Master_Framework.md)
- [AI Security Audit and Evidence Checklist](../06_Testing_and_Assurance/14_AI_Security_Audit_and_Evidence_Checklist.md)
