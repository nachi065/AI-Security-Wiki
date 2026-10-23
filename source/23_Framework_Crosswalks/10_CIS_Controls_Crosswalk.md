---
title: "CIS Controls Crosswalk"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Framework Crosswalks"
nav_order: 10
description: "The 18 CIS Critical Security Controls, version 8, with the wiki control objectives and test cases that cite them, and the wiki controls that have no CIS equivalent."
document_type: AI Security Wiki Reference
version: 1.0
---

# CIS Controls Crosswalk

> **Purpose:** Let a team that uses the CIS Critical Security Controls as its security baseline find the wiki control objectives and test cases that apply each control to AI systems.

> **Audience:** Security engineering, IT operations, GRC teams, auditors.

> **Using the two together:** Use the CIS Controls for the prioritised safeguards that every system needs. Use this wiki for the control objectives and tests that AI systems need on top of them.

## About the controls and this page

The CIS Critical Security Controls are published by the Center for Internet Security. Version 8 was released in May 2021 and has 18 controls, each divided into safeguards that are sorted into three implementation groups. Version 8.1, released in June 2024, keeps the same 18 controls.

The wiki maps at control level, for example `CIS 3` for Data Protection. Safeguards and implementation groups are not mapped.

The tables are generated each time the site is built. They are read from the CIS Controls field of each control in the [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md). To change a mapping, edit the control; this page follows on the next build.

> **Verify before use.** Control numbers and titles were written from memory of version 8 and were not checked against the published document for this page. The mapping is this wiki's own judgment and has not been reviewed by the Center for Internet Security. A wiki control citing a CIS Control means it supports that control for AI systems, not that it satisfies it.

## How to read the tables

- **Wiki controls** are the control objectives whose record cites the CIS Control.
- **Test cases under those controls** counts the distinct test cases that test at least one of those controls.
- A CIS Control with no name and "None" in the next column is not cited by any wiki control.

## CIS Controls to wiki controls

<!-- framework-crosswalk: cis-controls -->

## Where the wiki stops

The CIS Controls are technical safeguards and say little about governance. Eleven wiki controls therefore cite none of them, among them AI policy, risk assessment, impact assessment, human oversight, fairness testing and output reliability. The [summary table](index.md#all-mappings-by-control) shows "None" in the CIS column for each. A team whose only baseline is the CIS Controls should take those governance controls from this wiki, ISO/IEC 42001 or the NIST AI RMF.

## Attribution

The CIS Critical Security Controls are published by the Center for Internet Security under a Creative Commons licence. This page cites control numbers and titles only and does not reproduce the safeguards.

## Related pages

- [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md)
- [NIST CSF Crosswalk](09_NIST_CSF_Crosswalk.md)
- [ISO/IEC 27001 Crosswalk](08_ISO_IEC_27001_Crosswalk.md)
- [Existing Security Control Baseline](../03_Control_Library/04_Existing_Security_Control_Baseline.md)
