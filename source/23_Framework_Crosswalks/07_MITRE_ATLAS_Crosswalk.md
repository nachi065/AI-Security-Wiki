---
title: "MITRE ATLAS Crosswalk"
author: Nachiket Sathaye
parent: "Framework Crosswalks"
nav_order: 7
description: "MITRE ATLAS techniques and mitigations cited in the wiki, each with the control objectives that address it and the test cases that exercise it."
document_type: AI Security Wiki Reference
version: 1.0
---

# MITRE ATLAS Crosswalk

> **Purpose:** Let a red team or detection team that works from MITRE ATLAS find the wiki control objectives that address a technique and the test cases that exercise it.

> **Audience:** AI red teams, threat intelligence, detection engineering, security architecture.

> **Using the two together:** Use ATLAS to describe adversary behaviour against AI systems. Use this wiki for the control objectives that counter each technique and the test cases that show whether a product does.

## About ATLAS and this page

MITRE ATLAS is a knowledge base of adversary tactics and techniques against AI systems, with a list of mitigations. Techniques are numbered `AML.T####` and mitigations `AML.M####`. The version used is the one named in the [control library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#framework-identifiers).

This page lists only the techniques and mitigations that the wiki cites. ATLAS holds more than these, so a technique missing from the table has not been mapped; it has not been judged out of scope.

The tables are generated each time the site is built. They are read from the MITRE ATLAS fields of each control and from the MITRE ATLAS Mapping field of each test case. To change a mapping, edit the control or the test case; this page follows on the next build.

> **Verify before use.** ATLAS is updated often and renames techniques. Check every identifier and name against the current ATLAS release before quoting it. The mappings are the wiki's own judgment and have not been reviewed by MITRE.

## How to read the tables

- **Wiki controls** are the control objectives whose record cites the technique or mitigation. "None" means that only test cases cite it.
- **Test cases under those controls** counts the distinct test cases that test at least one of those controls.
- **Test cases that cite it** counts the test cases whose own record names the technique. A sub-technique such as `AML.T0051.001` is counted under its technique.

## Techniques and mitigations to wiki controls

<!-- framework-crosswalk: mitre-atlas -->

## Attribution

MITRE ATLAS is published by The MITRE Corporation. This page cites technique and mitigation identifiers and names only and does not reproduce ATLAS descriptions.

## Related pages

- [OWASP Top 10 Crosswalk](06_OWASP_Top_10_Crosswalk.md)
- [AI Red Team Playbook](../06_Testing_and_Assurance/15C_AI_Red_Team_Playbook.md)
- [Test Case Library](../10_Test_Case_Library/index.md)
