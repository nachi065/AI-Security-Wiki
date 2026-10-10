---
title: "NIST AI RMF Crosswalk"
author: Nachiket Sathaye
parent: "Framework Crosswalks"
nav_order: 3
description: "Every NIST AI RMF 1.0 subcategory with the wiki control objectives and test cases that cite it, and the subcategories no control cites yet."
document_type: AI Security Wiki Reference
version: 1.0
---

# NIST AI RMF Crosswalk

> **Purpose:** Let a team that organises its AI risk programme around the NIST AI Risk Management Framework find the wiki control objectives and test cases for each subcategory, and see which subcategories the wiki does not reach.

> **Audience:** GRC, risk and audit teams; security architecture; programme owners who report against the AI RMF.

> **Using the two together:** Use the AI RMF for the structure and language of the programme. Use this wiki for the control objectives, evidence, audit procedures and test cases behind each subcategory.

## About the framework and this page

The AI Risk Management Framework 1.0 (NIST AI 100-1) was published by the US National Institute of Standards and Technology in January 2023. Its Core has four functions, Govern, Map, Measure and Manage, divided into 19 categories and 72 subcategories. NIST publishes the Core at https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; the list of subcategory numbers used here was checked against that page on 10 October 2026.

The tables are generated each time the site is built. They are read from the NIST AI RMF field of each control in the [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md) and from the NIST AI RMF Mapping field of each test case. To change a mapping, edit the control or the test case; this page follows on the next build.

> **Verify before use.** A control citing a subcategory means the control helps to meet it, not that it meets it in full. The mappings are the wiki's own judgment and have not been reviewed by NIST. Read the subcategory text before relying on a mapping in an audit.

## How to read the tables

- **Wiki controls** are the control objectives whose record cites the subcategory.
- **Test cases under those controls** counts the distinct test cases that test at least one of those controls.
- **Test cases that cite it** counts the test cases whose own record names the subcategory. Cases in layers L01 to L03 name a function and not a subcategory, so they are not counted in this column.

## Subcategories to wiki controls

<!-- framework-crosswalk: nist-ai-rmf -->

## Attribution

NIST publications are works of the United States Government. This page cites subcategory numbers only and does not reproduce the text of the framework.

## Related pages

- [NIST AI 600-1 Generative AI Profile Crosswalk](04_NIST_AI_600_1_GenAI_Profile_Crosswalk.md)
- [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md)
- [Risk, Control and Test Traceability](../02_Risk_Management/02G_Risk_Control_Test_Traceability.md)
