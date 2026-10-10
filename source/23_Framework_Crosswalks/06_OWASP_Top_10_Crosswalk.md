---
title: "OWASP Top 10 Crosswalk"
author: Nachiket Sathaye
parent: "Framework Crosswalks"
nav_order: 6
description: "Each item in the OWASP Top 10 for LLM Applications 2025 and the OWASP Top 10 for Agentic Applications with the wiki control objectives and test cases that cover it."
document_type: AI Security Wiki Reference
version: 1.0
---

# OWASP Top 10 Crosswalk

> **Purpose:** Let a team that uses the OWASP lists to name AI application risks find the wiki control objectives that treat each item and the test cases that exercise them.

> **Audience:** Application security, AI red teams, product developers, vendor evaluation teams.

> **Using the two together:** Use the OWASP lists to name and rank the risks of an LLM application or an agent. Use this wiki for the control objectives, evidence and test cases for each item.

## About the lists and this page

The OWASP GenAI Security Project publishes two lists that the wiki cites: the Top 10 for LLM Applications, 2025 edition (`LLM01:2025` to `LLM10:2025`), and the Top 10 for Agentic Applications (`ASI01` to `ASI10`). The editions used are the ones named in the [control library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#framework-identifiers).

The tables are generated each time the site is built. They are read from the OWASP field of each control and from the OWASP mapping field of each test case. To change a mapping, edit the control or the test case; this page follows on the next build.

> **Verify before use.** OWASP revises its lists and renumbers items between editions. Check identifiers and titles against the current published lists before quoting them. The mappings are the wiki's own judgment and have not been reviewed by OWASP.

## How to read the tables

- **Wiki controls** are the control objectives whose record cites the item.
- **Test cases under those controls** counts the distinct test cases that test at least one of those controls.
- **Test cases that cite it** counts the test cases whose own record names the item. Most test cases name items from the LLM list only. The agent-to-agent cases also name ASI07, so it is the one agentic item with a count in this column.

## Items to wiki controls

<!-- framework-crosswalk: owasp -->

## Attribution

The OWASP Top 10 for LLM Applications and the OWASP Top 10 for Agentic Applications are published by the OWASP GenAI Security Project. This page cites item identifiers and titles only. Check the project's licence before reusing its text.

## Related pages

- [MITRE ATLAS Crosswalk](07_MITRE_ATLAS_Crosswalk.md)
- [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md)
- [Test Case Library](../10_Test_Case_Library/index.md)
