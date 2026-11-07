---
title: "OWASP Top 10 Crosswalk"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Framework Crosswalks"
nav_order: 6
description: "Each item in the OWASP Top 10 for LLM Applications 2026 and the OWASP Top 10 for Agentic Applications with the wiki control objectives and test cases that cover it."
document_type: AI Security Wiki Reference
version: 1.1
---

# OWASP Top 10 Crosswalk

> **Purpose:** Let a team that uses the OWASP lists to name AI application risks find the wiki control objectives that treat each item and the test cases that exercise them.

> **Audience:** Application security, AI red teams, product developers, vendor evaluation teams.

> **Using the two together:** Use the OWASP lists to name and rank the risks of an LLM application or an agent. Use this wiki for the control objectives, evidence and test cases for each item.

## About the lists and this page

The OWASP GenAI Security Project publishes two lists that the wiki cites: the Top 10 for LLM Applications, 2026 edition (`LLM01:2026` to `LLM10:2026`), and the Top 10 for Agentic Applications (`ASI01` to `ASI10`). The editions used are the ones named in the [control library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#framework-identifiers).

The tables are generated each time the site is built. They are read from the OWASP field of each control and from the OWASP mapping field of each test case. To change a mapping, edit the control or the test case; this page follows on the next build.

> **Verify before use.** OWASP revises its lists and renumbers items between editions. Check identifiers and titles against the current published lists before quoting them. The mappings are the wiki's own judgment and have not been reviewed by OWASP.

## Moving from the 2025 identifiers

The wiki cited the 2025 edition until 7 November 2026. The 2026 edition keeps all ten categories and adds none, so a 2025 identifier in an older report, RFP or test plan maps to exactly one 2026 identifier. Use this table to read the two against each other.

| 2025 | Category in the 2026 edition | 2026 |
|---|---|---|
| `LLM01:2025` | Prompt Injection | `LLM01:2026` |
| `LLM02:2025` | Sensitive Information Disclosure | `LLM02:2026` |
| `LLM03:2025` | Supply Chain | `LLM04:2026` |
| `LLM04:2025` | Data and Model Poisoning | `LLM05:2026` |
| `LLM05:2025` | Improper Output Handling | `LLM10:2026` |
| `LLM06:2025` | Excessive Agency | `LLM03:2026` |
| `LLM07:2025` System Prompt Leakage | Hidden Context Exposure | `LLM08:2026` |
| `LLM08:2025` | Vector and Embedding Weaknesses | `LLM09:2026` |
| `LLM09:2025` | Misinformation | `LLM07:2026` |
| `LLM10:2025` | Unbounded Consumption | `LLM06:2026` |

Two cautions when reading an older document against the new list. `LLM07:2025` System Prompt Leakage was renamed to Hidden Context Exposure and widened beyond the system prompt to the context supplied to a connected AI system, so a finding written against the old name may now sit inside a larger category. And four categories widened in scope without changing name, so the 2026 entry may cover more than the 2025 text a finding was written against: Prompt Injection now covers instructions hidden in an image or an audio track, Data and Model Poisoning absorbs fine-tuning subversion, Supply Chain covers a promoted model artifact that is not what it claims to be, and Improper Output Handling spans insecure code generated at scale by coding assistants.

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
