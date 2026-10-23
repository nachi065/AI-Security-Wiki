---
title: "NIST CSF Crosswalk"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Framework Crosswalks"
nav_order: 9
description: "The 22 categories of the NIST Cybersecurity Framework 2.0 with the wiki control objectives and test cases that cite them, and the categories not yet cited."
document_type: AI Security Wiki Reference
version: 1.0
---

# NIST CSF Crosswalk

> **Purpose:** Let a team that organises its security programme around the NIST Cybersecurity Framework find the wiki control objectives and test cases that apply each category to AI systems.

> **Audience:** Security programme owners, GRC teams, security architects, auditors.

> **Using the two together:** Use the CSF to organise and report on the whole security programme. Use this wiki for the AI-specific control objectives, evidence and tests that sit under each category.

## About the framework and this page

The NIST Cybersecurity Framework 2.0 was published by the US National Institute of Standards and Technology in February 2024. Its Core has six functions (Govern, Identify, Protect, Detect, Respond and Recover), 22 categories and 106 subcategories. It is voluntary and free to use.

The wiki maps at category level, for example `PR.DS` for Data Security. Subcategories are not mapped. For AI risk management as a discipline of its own, NIST publishes the AI RMF; see the [NIST AI RMF Crosswalk](03_NIST_AI_RMF_Crosswalk.md).

The tables are generated each time the site is built. They are read from the NIST CSF field of each control in the [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md). To change a mapping, edit the control; this page follows on the next build.

> **Verify before use.** Category identifiers and names were written from memory of CSF 2.0 and were not checked against the published Core for this page. The mapping is this wiki's own judgment and has not been reviewed by NIST. A wiki control citing a category means it supports that category for AI systems, not that it satisfies it.

## How to read the tables

- **Wiki controls** are the control objectives whose record cites the category.
- **Test cases under those controls** counts the distinct test cases that test at least one of those controls.
- A category with no name and "None" in the next column is not cited by any wiki control.

## Categories to wiki controls

<!-- framework-crosswalk: nist-csf -->

## Attribution

NIST publications are works of the United States Government. This page cites category identifiers and names from the CSF 2.0 Core and does not reproduce its subcategories or implementation examples.

## Related pages

- [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md)
- [NIST AI RMF Crosswalk](03_NIST_AI_RMF_Crosswalk.md)
- [ISO/IEC 27001 Crosswalk](08_ISO_IEC_27001_Crosswalk.md)
- [CIS Controls Crosswalk](10_CIS_Controls_Crosswalk.md)
