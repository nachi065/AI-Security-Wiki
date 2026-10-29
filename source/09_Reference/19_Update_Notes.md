---
title: "Update Notes"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Reference"
nav_order: 2
description: "The full record of how the AI Security Wiki has changed: a note for each substantial update, with what was checked and what is still work in progress, and the complete version history since version 1.0."
document_type: AI Security Wiki Reference
version: 1.1
last_reviewed: 2026-10-29
---

# Update Notes

This page is the wiki's change record. It has two parts:

- **Update notes**, newest first: what changed in each substantial update, what was checked against sources, and what is still work in progress.
- **[Full version history](#full-version-history)**: every version since 1.0, newest first. The [home page](../index.md#20-version-history) shows only the three latest.

Entries are only ever added. Past entries are not rewritten or removed; when something in an earlier entry turns out to be wrong, the correction is recorded as a new entry that names the earlier one.

## 29 October 2026: the Builder Track on Windows

This entry follows the one below ("Builder Toolkit and Builder Track links"), which listed Windows support for the sandbox and the shell-based git hooks as not done.

### What changed

- **Sandbox.** On macOS, the sandbox now starts (it failed there before). On Windows, [`sandbox.py`](../24_Builder_Track/01_Secure_Your_First_Agent.md#b7-run-generated-code-in-a-sandbox) now places the child process in a Job Object (new file `winjob.py`, standard-library `ctypes`) that limits CPU time, memory and process count and kills everything the job started when it closes or times out. Its result has a new `limits` field that lists what the platform actually applied.
- **Git hooks.** The hook commands on [Developer Pipeline Checks](../24_Builder_Track/04_Developer_Pipeline_Checks.md#wire-it-in) use `python3` where it exists and `python` otherwise, and the page says to install them from Git Bash on Windows.
- **Text files.** The reference code and tests read and write files as UTF-8 instead of the platform's default encoding.
- **Container command.** `docker-sandbox.ps1` runs the same locked-down container command from PowerShell.
- **CI.** The Builder Track tests workflow runs every Builder Track test, not only the toolkit's, on Linux, macOS and Windows.

### What was checked and what is still open

- All Builder Track tests pass on Linux locally. The macOS and Windows results come from the CI run on the pull request.
- **macOS.** Running every test on macOS for the first time showed that the sandbox had never worked there: macOS refuses one of the Unix limits (the address-space limit, as far as the tests show), and the whole launch failed. The sandbox now applies each limit it can, runs without the ones the system refuses, and lists the applied ones in `limits`, as it does on Windows.
- Tests skip what a platform cannot do, with the reason: the memory limit where the system refuses it (macOS), the file-size limit on Windows, and network removal everywhere except Linux machines that allow `unshare --net`.
- On Windows the child process joins its Job Object just after it starts, so its first instructions run before the limits apply. The sandbox remains hygiene, not a security boundary, on every platform.
- `docker-sandbox.ps1` was not executed, like `docker-sandbox.sh`, because the tests need no container runtime.

## 29 October 2026: Builder Toolkit and Builder Track links

This entry follows the one below ("CSV data files and rebuilt workbooks"). It acts on a review of the Builder Track against the rest of the wiki and on Ankush Jain's [ai-secure-by-design](https://github.com/ankush1982/ai-secure-by-design) v0.2 (commit `70ef026`, 24 October 2026).

### What changed

- **[Builder Toolkit](../24_Builder_Track/05_Builder_Toolkit.md)**, a new Builder Track page with tools in the track's `code/` folder, all standard-library Python:
  - `aiwiki_check.py` with `ai_rules.json`: ten AI-specific rules (AIW-001 to AIW-010) for model output reaching `eval`, HTML or SQL, unsafe model loading, `trust_remote_code`, unpinned models and MCP servers, MCP over plain HTTP, auto-approved MCP tools and coding agents run with approvals off. Each rule names its controls, risks and test cases. Output is text, JSON or SARIF 2.1.0, with exit codes for hooks and CI and a mode that checks only the lines a change adds.
  - `mcp_server.py`: a read-only MCP server (stdio, and HTTP on loopback with token and Host and Origin checks) with six tools for wiki look-ups and the checks, and a design-review prompt.
  - `wiki_data.py`: offline look-ups and search over the CSV data files.
  - `evidence_export.py`: rows for the Audit and Evidence Checklist and the Test Case Tracker from the guard's audit log and SARIF results, after checking the log's hash chain.
  - `gen_instructions.py`: one set of rules written as `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, the Copilot instructions file and a Cursor rule.
  - GitHub Actions, GitLab CI and pre-commit examples.
- **Tests on three operating systems.** `test_toolkit.py` (32 tests) runs on Linux, macOS and Windows in the Builder Track tests workflow, which now also runs when the CSV data files change.
- **Links across the track.** The ten controls table on [Secure Your First Agent](../24_Builder_Track/01_Secure_Your_First_Agent.md#the-ten-controls-at-a-glance) gains a column of register risks and a link to the OWASP Top 10 Crosswalk. The track's pages link the inventory, triage, audit checklist, test tracker, impact assessment and incident report templates; the [section index](../24_Builder_Track/index.md) adds a where-to-start table and an evidence table; and those six template pages link back. The home page links the section index and the toolkit.

### What was checked and what is still open

- All Builder Track tests pass locally on Linux with Python 3.13 (122 tests, 1 skipped where the kernel does not allow `unshare`). The macOS and Windows results come from the CI run on the pull request.
- The checker reports nothing on the Builder Track's own reference code, on the Payload Kit or on the ai-secure-by-design repository. Its rules are line-based heuristics: they miss renamed variables and can flag safe code.
- The register risks in the ten controls table are the main ones the risk-to-control mapping links to each step's control, chosen by hand; the test suite checks only that every ID exists.
- **Not verified against vendor documentation:** MCP client configuration layouts, instruction-file locations for each assistant, the coding-agent flag names in AIW-010, and the MCP protocol revisions the server answers. The MCP server was tested with JSON-RPC messages written from the specification, not with any vendor's client.
- **Not done:** Windows support for the sandbox and the shell-based git hooks on the pipeline page; a hosted, TLS-protected MCP endpoint; per-agent hook adapters; dedicated pages for retrieval authorisation, model supply chain and detection and response.

## 29 October 2026: CSV data files and rebuilt workbooks

This entry follows the one below ("eight risks to close the AI Risk Map gaps").

### What changed

- **CSV data files.** The [Templates](../25_Templates/index.md#data-files-csv) section now offers five CSV files: the risk register, the risk-to-control mapping, the control objectives, the test cases and the AI Risk Map crosswalk. A new script, `export_data.py`, writes them from the Markdown pages on every build, so they cannot fall out of step with the pages. This follows the AI Risk Map's practice of publishing a flat CSV with stable IDs.
- **Workbooks rebuilt.** The [AI Risk Register](../25_Templates/01_AI_Risk_Register_Template.md) (version 1.3), [AI Use-Case Risk Triage](../25_Templates/03_AI_Use_Case_Risk_Triage_Template.md) (1.1), [Control Library and Crosswalks](../25_Templates/06_AI_Security_Control_Library_and_Crosswalks_Template.md) (1.4) and [Test Case Tracker](../25_Templates/07_AI_Security_Test_Case_Tracker_Template.md) (1.3) workbooks now include AI-R47 to AI-R54 and triage questions E13 to E19. Their licence sheets credit the AI Risk Map to Evan Wheeler (GitHub wheels344i-gte) and link https://github.com/wheels344i-gte/ai-risk-map.
- **Generator fixes.** The risk register generator no longer assumes 46 risks. The data extraction now finds the Owner Domains table by its heading (the new Considered and Not Added table had come first), and it now reads the Hong Kong regulatory crosswalk, which it had been skipping.

### What was checked and what is still open

- All four workbooks were recalculated with no formula errors. The register sheet holds AI-R01 to AI-R54 in rows 5 to 58, and rows 59 to 150 are free for new risks.
- The CSV files hold 54 risks, 46 controls and 674 test cases, the same counts the link check reports.
- The audit checklist, requirements traceability matrix and other workbooks were not rebuilt, because they do not list register risks.
- The CSV crosswalk maps the AI Risk Map's categories, not its factor IDs. Mapping each AIRM factor ID still needs the map's own CSV.

## 29 October 2026: eight risks to close the AI Risk Map gaps

This entry follows the one below ("rules for what goes on the risk register") and applies its four tests.

### What changed

- **Eight new risks.** The [Enterprise AI Risk Register](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) (version 1.4) adds AI-R47 Model Extraction and Inference Attacks, AI-R48 AI Incidents Not Recognised or Handled, AI-R49 Personal Data That Cannot Be Removed from Models, AI-R50 Training-Serving Skew and Unreproducible Models, AI-R51 Liability for Harm Caused by AI Decisions, AI-R52 Unmaintained Open-Source AI Components, AI-R53 Unlabelled AI-Generated Content and AI-R54 Agent Actions Others Cannot Identify as AI. Each is adapted from a category of the AI Risk Map by Evan Wheeler ([wheels344i-gte/ai-risk-map](https://github.com/wheels344i-gte/ai-risk-map)) that the register covered only in part.
- **Two risks widened instead of added.** AI-R29 now includes customers reaching the organization through their own agents, and AI-R31 includes shortages of GPUs, compute and power. Segregation of duties was considered and not added. All three decisions are recorded under Considered and Not Added.
- **Controls and triage.** The [AI Risk to Control Mapping](../02_Risk_Management/02D_AI_Risk_to_Control_Mapping.md) (1.3) maps each new risk to existing controls, so the [traceability page](../02_Risk_Management/02G_Risk_Control_Test_Traceability.md) links them to existing test cases. The [AI Use-Case Risk Triage](../02_Risk_Management/02F_AI_Use_Case_Risk_Triage.md) (1.2) adds questions E13 to E19.
- **Crosswalk.** The [AI Risk Map Crosswalk](../23_Framework_Crosswalks/18_AI_Risk_Map_Crosswalk.md) (1.2) now shows 42 direct and 13 partial matches, up from 31 and 24.

### What was checked and what is still open

- Five of the eight narratives name a second source as well as the map: NIST AI 100-2 (AI-R47), the EU AI Act Article 73 (AI-R48), the GDPR and EDPB Opinion 28/2024 (AI-R49), the new EU Product Liability Directive (AI-R51), and the EU AI Act Article 50 and China's labelling rules (AI-R53). These sources are cited from the wiki's own regional pages and crosswalks and were not re-read for this change. AI-R50, AI-R52 and AI-R54 say that only the map names them.
- No new test cases were written. The new risks are tested through the cases already filed under their controls. Whether those cases cover each risk well has not been reviewed.
- Ratings are illustrative, like the rest of the register. FINOS cross-references for the new risks are marked Not checked.

## 29 October 2026: rules for what goes on the risk register

A second comparison with the *AI Risk Map* by Evan Wheeler (RiskFramework.org), this time with its website, found that the map states why each factor is included and records what it left out, and that its factor IDs are never reused. The wiki had neither rule written down.

### What changed

- **What Belongs on the Register.** A new section of the [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md#what-belongs-on-the-register) (version 1.3) sets four tests for a new register risk: AI-specific, a distinct response, corroborated by at least two independent sources (or marked as the wiki's own framing), and treatable by at least one control. The tests are adapted from the map's inclusion gates and credited to it.
- **Considered and Not Added.** The [Enterprise AI Risk Register](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md#considered-and-not-added) (version 1.3) now records proposed risks that were left out, with the reason. It starts with the two scope decisions the methodology already made: attacks others carry out with AI, and general IT risks with no AI-specific change.
- **IDs are never reused.** The contributing guide now says AI-R, AI-CTRL and TC numbers are permanent and how to retire an item.
- **Credit for the AI Risk Map.** Every credit for the map (crosswalk, register, methodology, the three template pages and a new Third-party content section in the README) now names the author's GitHub account, wheels344i-gte, and links the map's repository, https://github.com/wheels344i-gte/ai-risk-map, as well as RiskFramework.org. The crosswalk gives the citation the author asks for.
- **AI Risk Map Crosswalk** (version 1.1). The page no longer says the map's website could not be reached. It records that the website was read on 29 October 2026 and still shows version 1.3, and that the map's workbook and CSV have not yet been compared with the page.

### What was checked and what is still open

- The website was read through a summarising web reader. The map's CSV, workbook and Markdown files could not be downloaded from the environment used, so the crosswalk is still by category, not by factor ID.
- The existing 46 register risks have not yet been re-tested against the four new tests. In particular, most narratives do not yet name their sources, which the corroboration test asks for.

## 25 October 2026: NIST SSDF crosswalk in the template workbooks

This entry closes the item left open in the entry below ("templates rebuilt for the regulator changes"), which said the NIST SSDF crosswalk was not yet a column in the risk register's framework matrix.

### What changed

- **SSDF column.** The [NIST SSDF and SP 800-218A Crosswalk](../23_Framework_Crosswalks/20_NIST_SSDF_Crosswalk.md) (added in 2.41) is now read by the template generators. Its 20 practices (PO, PS, PW and RV) appear as a column in the framework matrix and as rows in the Framework Crosswalk sheet of the [AI Risk Register](../25_Templates/01_AI_Risk_Register_Template.md) (version 1.2) and the [Control Library and Crosswalks](../25_Templates/06_AI_Security_Control_Library_and_Crosswalks_Template.md) (1.3) workbooks. Before this, the generators skipped the SSDF page, so the crosswalk was missing from the control library workbook as well as the risk register.
- **Counts corrected.** The control library workbook now lists 930 framework items (910 before) in 49 framework columns. The template page had said 47 columns, which was already one short after the Hong Kong column was added.
- **Risk links are via controls.** The SSDF crosswalk names controls, not risks, so the risk register links each practice to the risks its controls treat. The Framework Matrix marks that column "via controls".

### What was checked

- Both rebuilt workbooks were recalculated with no formula errors. In the risk register matrix, 24 of the 46 risks have at least one SSDF practice. In the control library matrix, 20 of the 46 controls do.
- The Requirements Traceability Matrix was not rebuilt: its framework columns come from each control's own fields, not from the crosswalks, so the SSDF change does not affect it.

## 25 October 2026: templates rebuilt for the regulator changes

This entry closes an item left open in the entry below ("financial regulators and the kill switch"), which said the Excel templates had not been rebuilt.

### What changed

- **Five workbooks rebuilt from wiki 2.44.** The [AI Risk Register](../25_Templates/01_AI_Risk_Register_Template.md) (version 1.1), [Audit and Evidence Checklist](../25_Templates/05_AI_Security_Audit_and_Evidence_Checklist_Template.md) (1.2), [Control Library and Crosswalks](../25_Templates/06_AI_Security_Control_Library_and_Crosswalks_Template.md) (1.2), [Test Case Tracker](../25_Templates/07_AI_Security_Test_Case_Tracker_Template.md) (1.2) and [Requirements Traceability Matrix](../25_Templates/12_AI_Security_Requirements_Traceability_Matrix_Template.md) (1.1) now show AI-CTRL-025 as AI Containment and Kill Switch with its wider text, the extended text of AI-CTRL-011, 012, 014 and 041, and test case TC-L01-021.
- **Hong Kong column.** The framework matrices and the traceability matrix have a Hong Kong regulation (incl. HKMA) column, and the crosswalk sheets carry the 18 Hong Kong items (nine instruments and nine HKMA principles). The control library workbook now lists 910 framework items.
- **Risk register catch-up.** The risk register had not been rebuilt since 17 October 2026, so this rebuild also brings in other wiki changes made since then. Its file properties now credit both authors.

### What was checked

- Every rebuilt workbook was recalculated with no formula errors, and its sheets match the previous version's sheet list.

### Still work in progress

- The NIST SSDF crosswalk (added in 2.41) is not yet a column in the risk register's framework matrix.

## 25 October 2026: financial regulators and the kill switch

A comparison of the wiki with a published chart of six financial regulators' AI expectations (MAS, RBI, SEBI, the EU AI Act, the FCA and the HKMA) found that the wiki had no Hong Kong coverage at all, and that its only kill-switch control applied to agents, while MAS, the HKMA and the RBI draft expect a way to suspend any high-risk AI. It also found that the chart understated MAS, the RBI and the HKMA on kill switches, and showed SEBI's guidelines as requirements before they were issued.

### What changed

- **Hong Kong section.** A new [Hong Kong AI Compliance](../26_Hong_Kong_AI_Compliance/index.md) section has a regulatory hub (nine instruments, HK1 to HK9), a role guide, the [HK-T1 HKMA ART Principles Self-Assessment](../26_Hong_Kong_AI_Compliance/HK-T1_HKMA_ART_Principles_Self_Assessment.md) and a [crosswalk](../26_Hong_Kong_AI_Compliance/03_Regulatory_Crosswalk.md) that maps the HKMA guidance principle by principle: seven direct and two partial. Both tables are also CSV files.
- **Financial regulator comparison.** A new [Financial Regulator AI Comparison](../04_Domain_Standards/10C_Financial_Regulator_AI_Comparison.md) sets the six regulators side by side on board accountability, risk tiering, inventory, lifecycle controls, human oversight, third-party AI, customer transparency and kill switch, with the strictest version of each and the wiki control that meets it.
- **Kill switch beyond agents.** [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) is renamed AI Containment and Kill Switch. It now asks for a named person, triggers, a fallback, re-approval before restart and a yearly test for every high-risk AI use case, including models that are not agents and third-party AI. New test case [TC-L01-021](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-021) tests it. It stays a Baseline control.
- **Other control text.** [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) restricts AI that is not in the registry; [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) asks for a board-approved AI strategy and risk appetite; [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) bars vendors by default from training on personal or confidential data without authorisation and adds audit, suspension and exit terms; [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) asks for a customer notice of AI use and its risks before the service.
- **India and UK.** IN6 now records the RBI draft's kill-switch, human oversight, fallback and board expectations. New row IN13 records SEBI's AI and ML guidelines as proposed. UK5 records the FCA's Mills Review and its reported position that it plans no AI-specific rules.
- **Sector Overlays.** The financial-services table adds the HKMA, the RBI draft and SEBI where they apply, and a row on telling customers that AI is used.

### What was checked

- The HKMA Supervisory Guidance for Responsible Adoption of Artificial Intelligence (Annex A to the circular of 15 October 2026), the HKMA press release of the same day and the government's GenA.I. Sandbox++ announcement of 5 March 2026 were read on 25 October 2026 [Verified].
- The RBI draft Guidance on Regulatory Principles for Model Risk Management was read on 25 October 2026: paras 8 to 12, 43 and 59 to 63, including "override, suspension, or deactivation mechanisms, including kill-switch arrangements" (para 60(ii)) [Verified]. It is still a draft and has no effective date.
- The MAS Guidelines' kill-switch text (paras 5.3 and 5.23(b), footnote 29) was re-read on 25 October 2026 [Verified].
- The FCA's Mills Review page was read on 25 October 2026 [Verified]. The FCA's statement that it plans no AI-specific rules was seen only in secondary sources [Reported].

### Still work in progress

- The SFC circular of 12 November 2024, the PCPD framework and the PDPO rest on secondary sources or memory. The Insurance Authority's and the MPFA's AI guidance was not researched.
- SEBI's guidelines have not been issued; IN13 will need updating when they are.
- Article 14(4)(e) of the EU AI Act is cited from memory on the comparison page.
- The Excel and Word templates under Templates were not rebuilt, so the Control Library and Test Case Tracker workbooks still show AI-CTRL-025's old title and do not include TC-L01-021.

## 24 October 2026: requirements traceability and review templates

The wiki lacked a requirements matrix: one row per testable requirement, scoped by assurance stage and deployment model, with columns for the vendor's answer and the assessor's review. No wiki page said which controls apply to SaaS, PaaS or IaaS delivery.

### What changed

- **Assurance stage and deployment model.** Every control in the [Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#assurance-stages-and-deployment-models) (version 2.5) now names the stage at which a reviewer first checks it and the deployment models it applies to. The link checker rejects a control without valid values. Both are starting values for a review to adjust.
- **Requirements traceability matrix.** A new [AI Security Requirements Traceability Matrix Template](../25_Templates/12_AI_Security_Requirements_Traceability_Matrix_Template.md) turns each sentence of a control's Implementation Expectation into one requirement, traced to the control, its risks, test cases and framework and regional crosswalks. It adds scoping, vendor and assessor columns, thirteen evidence types, a response check that treats a "Yes" with no detail as unanswered, and a live dashboard.
- **Workbooks rebuilt.** The [Control Library and Crosswalks](../25_Templates/06_AI_Security_Control_Library_and_Crosswalks_Template.md) and [Audit and Evidence Checklist](../25_Templates/05_AI_Security_Audit_and_Evidence_Checklist_Template.md) workbooks (version 1.1) carry the two new fields and were rebuilt from the current wiki. The audit workbook now reads control areas and evidence owners from the per-family tables of the [Audit and Evidence Checklist](../06_Testing_and_Assurance/14_AI_Security_Audit_and_Evidence_Checklist.md) page, so each control's area is now its family.

- **Two more templates.** The [AI System Security Risk Review Checklist](../25_Templates/13_AI_System_Security_Risk_Review_Checklist_Template.md) holds 150 review questions across the AI lifecycle, with impact and risk registers, threat and vulnerability lists and severity criteria. Organisation names were removed, its dropdowns rebuilt and the standard editions corrected. The [AI Security Assurance Baseline](../25_Templates/14_AI_Security_Assurance_Baseline_Template.md) holds 165 testable requirements in 14 domains, mapped to ISO/IEC 42001, NIST AI RMF, the EU AI Act and OWASP, with vendor and assessor columns and a dashboard. Its UAE and Dubai requirements and references moved to optional sheets so that the baseline applies anywhere.

### What was checked

- The baseline's dashboard and response check were recalculated with sample answers and gave the expected counts and flags. The checklist's dropdowns now read from its own Ref Tables sheet rather than an external workbook.
- The matrix dashboard's formulas were recalculated with sample answers (a Yes with no detail, an accepted row, a gap without an owner and an out-of-scope row) and gave the expected counts and flags. All three workbooks recalculate with no formula errors.
- The regulatory references in the matrix come from the wiki's crosswalks and keep their verification status. The UAE and Dubai instruments a Dubai Government review would cite (the DESC Information Security Regulation, the national AI security policy and the Dubai Data Law) were not added, because their text has not been read.

### Still work in progress

- About fifteen review topics have no or thin coverage in the control library, such as recovery time objectives, DDoS protection, key custody, model decommissioning and detection validation. They are listed for a later update.

## 23 October 2026: secure development and privacy in code

A comparison with [ai-secure-by-design](https://github.com/ankush1982/ai-secure-by-design), an open-source plugin for AI coding agents by the wiki's co-author Ankush Jain, found five gaps in the wiki. It never cited the NIST Secure Software Development Framework or its generative AI profile. Its standard for AI coding assistants was short and did not cover coding agents. It had no controls before commit. It described privacy duties as forms, not code. And the Builder Track tests were not run in CI. This update closes those gaps.

### What changed

- **NIST SSDF crosswalk.** A new [NIST SSDF and SP 800-218A Crosswalk](../23_Framework_Crosswalks/20_NIST_SSDF_Crosswalk.md) maps the 19 practices of SSDF 1.1, plus the new PW.3 practice of SP 800-218A, to the wiki's controls, pages, code and test cases: 17 direct and 3 partial. It records the PW.3 renumbering and the new PO.5.3 task.
- **Coding assistants and coding agents.** The [AI Coding Assistant and Coding Agent Security Standard](../04_Domain_Standards/07_IDE_AI_Coding_Assistant_Security_Standard.md) (version 2.0, same address) now covers completion assistants, coding agents, pipeline agents, and the extensions, plugins, MCP servers and rules files that steer them. New requirements cover approved models and accounts, command and file-system guardrails, scoped agent credentials, MCP servers and plugins, repository content as untrusted input, managed agent settings and hooks, generated code review, dependency verification, provenance of AI-made changes, and review bot permissions. Each requirement links to the existing test case that proves it. A pipeline gates table shows which checks run in the agent, before commit, in CI and at merge, and which of them the author can bypass.
- **Privacy duties in code.** A new Builder Track page, [Privacy Duties in Code](../24_Builder_Track/03_Privacy_Duties_in_Code.md), maps the duties of the DPDP Act (s.5, s.6, s.8(5) to s.8(10), s.9, s.11 to s.14, s.16) to tested reference code: a consent ledger keyed to the notice version, a rights desk, a retention runner with advance notice, a children's gate, and a logger that uses keyed pseudonyms. All of it is driven by one data map. The time limits from the DPDP Rules are settings, each with a verification tag.
- **Developer pipeline checks.** A new Builder Track page, [Developer Pipeline Checks](../24_Builder_Track/04_Developer_Pipeline_Checks.md), runs the same checks in git hooks, a coding agent's pre-write hook and CI. The checks look for secrets and for personal data written to logs, using the same data map, and require an `AI-Assistance` trailer that records whether a person, an assistant or an agent made each change. The trailer is this wiki's convention and supports [TC-L14-021](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-021).
- **Tests in CI.** A new workflow, `builder-tests.yml`, runs every Builder Track test on Python 3.10 and 3.13 for every pull request that changes the section. It runs with a read-only token and no secrets. The check that page excerpts match the code now covers every Builder Track page. Its first run caught a real bug in the [egress proxy](../24_Builder_Track/01_Secure_Your_First_Agent.md#b8-limit-egress-to-named-hosts). When a name resolved to several addresses, the proxy connected only to the first one. On a dual-stack host that lists an IPv6 address first, connections to a service listening only on IPv4 therefore failed. The proxy now checks every address and tries each in turn, and a new test covers the case.
- **Cards.** The Domain Standards, Framework Crosswalks, India and Builder Track cards on the home page describe the new content.

### What was checked

- The DPDP Act sections cited on the privacy page were read in the Act text published by MeitY on 23 October 2026 [Verified]. That reading confirmed two points. The Act has no "sensitive personal data" category. Section 7's legitimate uses include no general contract ground.
- The DPDP Rules numbers were also read on 23 October 2026, from the Hindi text only. The English text was not read. They are: at least 48 hours' notice before erasure (Rule 8(2)), a three-year retention for the classes in the Third Schedule (Rule 8(1)), and one year for logs (Rule 6). All three are tagged [Reported]. Two numbers are tagged [Unverified]: the ninety-day grievance limit (Rule 14(3)), because the extracted number was garbled, and the hours for the detailed breach report (Rule 7(2)(b)), because they were not legible.
- These items of SP 800-218 and SP 800-218A were read on the NIST publication pages and in the PDFs on 23 October 2026 [Verified]: the titles, dates and audiences, the four practice groups, the titles of PO.1 to PO.5 and PS.1, the new PW.3 practice, task PO.5.3, and the note that PO.1.3 was formerly PW.3.1. The PDFs were read only in part. The other practice titles are tagged [Reported] on the crosswalk.
- The Builder Track tests pass on Python 3.10, 3.11, 3.12 and 3.13 (90 tests, 1 skipped where the kernel does not allow a network namespace). The new git hook tests install the hooks in a throwaway repository and confirm that a secret or a missing trailer blocks the commit.
- The link and identifier check and the author check pass.

### Still work in progress

- The DPDP Rules numbers above need checking against the English text before anyone relies on them.
- The SSDF crosswalk maps at practice level. SP 800-218A adds recommendations at task level, and those are not yet mapped.
- No test case covers the right to nominate (s.14) or the deemed end of purpose after a period without contact (s.8(8)).
- The privacy code is written against India's DPDP Act. Other laws differ, for example in the GDPR's special categories and contract basis.

## 22 October 2026: weak points in proof, rating and operation

A review of the wiki found that it shows proof weakly (test cases could be read as validated protection, risk ratings were not calibrated, regulatory claims were only partly verified) and is hard to run as a programme (no charter, few default numbers, thin governance detail). This update addresses those points.

### What changed

- **Validation levels for test cases.** Every case now shows a Validation Level: Documented, Executable, Lab-validated or Independently reproduced ([Validation levels](../10_Test_Case_Library/index.md#validation-levels)). The build fills it in: a case with a payload file in the kit is Executable, every other case is Documented. A case can claim Lab-validated or Independently reproduced only with a Validated Against row that names the product and version, the date and an evidence link; the link check enforces this. No case is lab-validated: the payload kit has only been run against its own stand-in applications.
- **Self-contained test cases.** Each case now ends with a closed box listing the [Standard Fields](../10_Test_Case_Library/standard-fields.md) wording that applies to it, so a copied case keeps its pass and fail criteria, scoring and evidence rules. The [test case tracker workbook](../25_Templates/07_AI_Security_Test_Case_Tracker_Template.md) (version 1.1) fills those fields into every row and adds the validation level.
- **Risk scoring and calibration.** The [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md) (version 1.2) now has a jurisdiction-neutral scoring method (likelihood 1 to 4 times impact 1 to 4, with rating bands and acceptance authority, matching the risk register workbook), a prohibited-use stop before scoring, two overrides, an assessor calibration step and four worked examples that go from scenario to acceptance decision. The examples are invented and illustrative.
- **Governance.** The [AI Governance Operating Model](../08_Governance/16_AI_Governance_Operating_Model.md) (version 1.1) adds starting charters for the AI Governance Committee and an AI Security Review Board, a decision-rights table with one approver per decision, and a role-based training plan.
- **Test coverage of the newest controls.** AI-CTRL-041 to AI-CTRL-046 were reviewed by outcome, not by case count ([Reading the case counts](../02_Risk_Management/02G_Risk_Control_Test_Traceability.md#reading-the-case-counts)). Eight existing cases that already exercised one of their outcomes now name the control: TC-L03-008, TC-L03-029, TC-L03-010, TC-L03-011, TC-L03-019, TC-L02-020, TC-L02-022 and TC-D12-016. Three new cases close the gaps that were left: [TC-L03-043](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-043) (bias profile and monitoring outside validated boundaries), [TC-L03-044](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-044) (impact assessment content and periodic review) and [TC-L03-045](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-045) (AI literacy effectiveness). AI-CTRL-045 and AI-CTRL-046 were judged adequately covered and get no new case.
- **Operating defaults.** A new [AI Operating Defaults](../08_Governance/18_AI_Operating_Defaults.md) page gives illustrative exception limits, incident severity levels and response times, monitoring thresholds, a review and audit calendar (the control part is generated from the control library), CI/CD release stages showing which checks are automated and which block a release, and a log retention baseline. Every number on it is the wiki's own starting value, not taken from a standard or a law.
- **Predictive models.** A new standard, [Predictive Model Monitoring and Adversarial ML](../04_Domain_Standards/11_Predictive_Model_Monitoring_and_Adversarial_ML.md), covers input drift, concept drift, prediction drift, accuracy decay and fairness shift, and the predictive attack classes of NIST AI 100-2e2025. Two new cases test it: [TC-L12-033](../10_Test_Case_Library/L12-model-layer.md#tc-l12-033) (drift, performance decay and fairness shift monitoring) and [TC-L12-034](../10_Test_Case_Library/L12-model-layer.md#tc-l12-034) (membership inference and model inversion probes).
- **Regulatory verification.** A new [Regulatory Verification Status](21_Regulatory_Verification_Status.md) page counts the verification tags of every regional crosswalk at each build, sets an order for verification work, and starts an obligation-level tracker that splits the EU AI Act high-risk row into its obligations.
- **Templates.** Two new Word templates: the [AI Security Programme Charter](../25_Templates/10_AI_Security_Programme_Charter_Template.md), which brings the programme into one approvable document and links each section to the wiki page behind it, and the [AI Incident Report](../25_Templates/11_AI_Incident_Report_Template.md).
- **Build.** The committed search index had been built with a different markdown version and showed fill-in blanks on 18 template pages as broken text; it is rebuilt correctly.

### What was checked

- The link and identifier check passes, including the new validation-level rule, which was tested by adding an invalid level and an unsupported Lab-validated claim to a copy of the source and confirming that both were rejected.
- The hand-kept case counts (layer headers, the Tested By rows of the control library and the tables on the library index) were recalculated by script from the case tables, after confirming that the same script reproduced the earlier counts exactly.

### Still work in progress

- **No real-system validation yet.** No case has been run against a real model, agent framework or product. Publishing reproducible results against representative applications is still to do; until then every case is Documented or Executable.
- **EU obligations not yet read one by one.** On 22 October 2026 the article text of the EU AI Act could not be retrieved from EUR-Lex (only the recitals came back), so the obligation-level tracker lists the articles as recalled and no new [Verified] tag was added. The deployer log retention period (Art. 26) and the serious incident time limits (Art. 73) in particular must be read before they are relied on.
- **Order of verification is an assumption.** The tracker puts the GCC first, then the EU, the UK and US, and India. Change it to match the jurisdictions that matter to you.
- **Risk register workbook not rebuilt.** Its per-risk test case counts are a 17 October 2026 snapshot and do not include this update's new cases.
- **Operating defaults and thresholds are untested.** They are starting values to tune, not benchmarks.

## Week ending 24 October 2026: crosswalk verification

### What was checked

- **GCC (19 October 2026):** every row of the [GCC Regulatory Crosswalk](../11_GCC_AI_Compliance/07_Regulatory_Crosswalk.md) was checked for changes, and the rows not yet verified were checked against the issuing bodies' own pages where those pages could be read: the UAE legislation portal, the Central Bank of the UAE, the Saudi National Cybersecurity Authority (NCA) and the UAE AI Office.
- **India and UK (20 October 2026):** every row of the [India Regulatory Crosswalk](../17_India_AI_Compliance/03_Regulatory_Crosswalk.md) and the [UK Regulatory Crosswalk](../21_UK_AI_Compliance/03_Regulatory_Crosswalk.md) was checked for changes. Ten rows not yet verified were checked against MeitY, the Lok Sabha, the Press Information Bureau, legislation.gov.uk, GOV.UK, the UK Parliament bill pages, the Bank of England and the NCSC.
- **Singapore, US and South Korea (21 October 2026):** every row of the [Singapore](../19_Singapore_AI_Compliance/03_Regulatory_Crosswalk.md), [US](../22_US_AI_Compliance/03_Regulatory_Crosswalk.md) and [South Korea](../20_South_Korea_AI_Compliance/03_Regulatory_Crosswalk.md) crosswalks was checked for changes. Rows not yet verified were checked against IMDA, the AI Verify Foundation, the PDPC, the CSA and MAS; govinfo.gov, justice.gov, whitehouse.gov, nist.gov, nyc.gov and the Colorado, New York, Utah and Texas legislatures; and MSIT, PIPC and the Korea Legislation Research Institute's English translations of the AI Basic Act and its decree.
- **Australia, Brazil, Canada, China and Japan (22 October 2026):** every row of the [Australia](../13_Australia_AI_Compliance/03_Regulatory_Crosswalk.md), [Brazil](../14_Brazil_AI_Compliance/03_Regulatory_Crosswalk.md), [Canada](../15_Canada_AI_Compliance/03_Regulatory_Crosswalk.md), [China](../16_China_AI_Compliance/03_Regulatory_Crosswalk.md) and [Japan](../18_Japan_AI_Compliance/03_Regulatory_Crosswalk.md) crosswalks was checked for changes. This was the first check of these five regions against primary sources. Rows were checked against the Federal Register of Legislation, the OAIC, the Department of Industry, APRA, Treasury, the ACCC and the Parliament of NSW; the Brazilian Senate and Chamber, the Planalto legislation site and the ANPD; Justice Laws, LegisQuebec, ISED, OSFI, the Parliament of Canada and the Ontario legislature and government; the CAC, MIIT, the State Council policy library and the national standards system; and the Cabinet Office, METI, the Personal Information Protection Commission, the Agency for Cultural Affairs and the FSA.
- **Framework crosswalks (23 October 2026):** every MITRE ATLAS technique and mitigation identifier the wiki cites (88 in all, in the control library and the test cases) was compared with MITRE's own ATLAS data, release 2026.09 of 15 September 2026, the latest release in the [atlas-data repository](https://github.com/mitre-atlas/atlas-data) on 23 October 2026. The [Trustworthy AI and Ethics Standards Crosswalk](../23_Framework_Crosswalks/16_Trustworthy_AI_Ethics_Crosswalk.md) and the [International AI Instruments Crosswalk](../23_Framework_Crosswalks/17_International_AI_Instruments_Crosswalk.md) were due for a check this week but could not be checked (see below).
- **Weekly change watch (24 October 2026):** in every region, the rows still marked Proposed, pending, draft or under consultation were checked for news. Primary sources read: the European Commission's AI Act guideline pages, the Council of the EU, the Congresso Nacional page on [PL 2338/2023](../14_Brazil_AI_Compliance/03_Regulatory_Crosswalk.md), the Saudi NCA consultation page and the RBI draft on model risk. EUR-Lex was searched for new citations of AI Act harmonised standards, and the CEN-CENELEC AI page for news on JTC 21.

### What changed

- **GCC, now [Verified]:** U2 (UAE cybercrime law, Federal Decree-Law No. 34 of 2021) and S8 (NCA AI Cybersecurity Guidelines: a consultation draft, feedback closed 5 August 2026, no final text yet). U1 (UAE PDPL) was read again with no change.
- **GCC, U9 (CBUAE Guidance Note):** the CBUAE press release confirms the date (23 February 2026) and that it applies to licensed financial institutions. The row stays [Reported] because the note's own text has not been read.
- **GCC, U7 (ADGM Data Protection Regulations):** moved from [Unverified] to [Reported]. ADGM's own briefing slides give the enactment date (11 February 2021) and scope; the regulations text could not be retrieved.
- **GCC, B1 (Bahrain PDPL):** re-read on the Personal Data Protection Authority site; no amendment is listed.
- **GCC, O2 (Oman PDPL amendments):** an English translation of Royal Decree 68/2026 and news reports say the amendments were issued on 3 September 2026 and are in force. The row now reads Binding law, still tagged [Reported] because the Official Gazette text was not read.
- **GCC, U3 (UAE AI Charter):** the two primary sources give different dates, 10 June 2024 on the legislation portal and July 2024 on the document. Both are now cited and the row stays [Conflict].
- **India, now [Verified]:** IN12 (IndiaAI Mission: Cabinet approval of 7 March 2024, outlay Rs 10,371.92 crore).
- **India, IN3 (Data Protection Board):** MeitY invited applications for a Chairperson and four Members on 6 May 2026, and the government's answer in the Lok Sabha on 12 August 2026 names no appointment. The row now says this, tagged [Verified].
- **India, IN9 (IT Rules on synthetic content):** MeitY's consolidated text shows the rules were made by G.S.R. 120(E) of 10 February 2026 (labelling and provenance in Rule 3(3), user declarations in Rule 4(1A)). The 20 February 2026 start date is still as reported.
- **UK, now [Verified]:** UK1 (the five principles, non-statutory, March 2023 White Paper), UK9 (the AI (Regulation) private member's bill is not law; no stage after first reading is shown) and UK10 (the voluntary AI Cyber Security Code of Practice of 31 January 2025 and the NCSC guidelines it builds on).
- **UK, UK3 (automated decision-making):** the new Articles 22A to 22D came into force on 5 February 2026 under SI 2026/82 and do not apply to decisions taken before that date.
- **UK, UK6 (PRA SS1/23):** applies to banks, building societies and PRA-designated investment firms that have internal model approval for regulatory capital, not to all banks. The current version took effect on 23 April 2026.
- **UK, UK8 (copyright and AI):** the government's report of 18 March 2026 says a text and data mining exception with an opt-out is no longer its preferred option. The existing exception (s.29A CDPA) covers non-commercial research only.
- **UK, UK11 (Algorithmic Transparency Recording Standard):** mandatory by government policy, not by law, for central government departments and some arm's-length bodies; recommended for the rest of the public sector.
- **Singapore, now [Verified]:** SG4 (the PDPC advisory guidelines on AI recommendation and decision systems, 1 March 2024, and on generative AI, 20 July 2026) and SG7 (the CSA guidelines of October 2024 and the agentic AI addendum of 17 June 2026; consultation 22 October to 31 December 2025).
- **Singapore, SG1 (Model AI Governance Framework):** the second edition (21 January 2020) is confirmed. Its second area is the level of human involvement in AI-augmented decision-making, not risk management as the row said. The framework for generative AI (30 May 2024) is added. Now [Verified].
- **Singapore, SG2 (framework for agentic AI):** the date (22 January 2026) and the four dimensions are confirmed. IMDA updated the framework on 20 May 2026 with case studies and guidance on multi-agent systems. Now [Verified].
- **Singapore, SG3 (AI Verify):** the 11 principles, listed before from memory, and the pilot launch on 11 February 2025 are confirmed. Now [Verified]. SG6 now records that Veritas concluded its third phase on 26 June 2023.
- **US, now [Verified]:** US5 (Colorado SB 26-189: signed 14 May 2026, takes effect 1 January 2027; the 30 June 2026 date in older trackers was the date under SB 24-205, so the [Conflict] tag is resolved).
- **US, US2 (Executive Order 14365):** the order's text is confirmed. The row said no complaints had been filed; on 24 April 2026 the US Department of Justice intervened in a case against Colorado SB 24-205 citing the order. Now [Verified].
- **US, US3 (Executive Order 14409):** pre-release access is for up to 30 days, and the order disclaims, rather than bans, mandatory licensing. The memo of 5 June 2026 is NSPM-11 and does not set those measures. Now [Verified].
- **US, US4 (NIST AI RMF):** the framework details are confirmed, but the Colorado SB 26-189 text does not appear to keep the NIST-based presumption reported under SB 24-205. Now [Conflict].
- **US, US11:** the New York RAISE Act is enacted and takes effect on 1 January 2027 (it was described as targeted). Utah SB 149 was narrowed by SB 226 (2025) and the Utah chapter is repealed on 1 July 2027. Now [Verified].
- **South Korea, KR2 (generative AI labelling):** the row said a visible or audible watermark is needed unless content is clearly fictional. The decree allows a machine-readable mark with a text or voice notice; animation is an example where an invisible mark is enough, not an exemption.
- **South Korea, KR3 (high-impact AI):** the Act's list of sectors and duties is added. The impact assessment is a best-efforts duty. The claim that only Level-4 autonomous vehicles qualify was found only in news reports, so the tag moves from [Conflict] to [Reported].
- **South Korea, KR1, KR4 to KR7:** law and decree numbers, article references, a fourth criterion for the domestic representative, the fine ceiling (up to KRW 30 million, for three breaches), the grace period as ministry policy rather than law, and PIPC's AI guides are added. These rows stay [Reported] or [Recalled] because the Korean text on law.go.kr could not be read automatically.
- **South Korea, now [Verified]:** KR8, renamed the AI Basic Act Support Desk, from MSIT's own page.
- **Australia, now [Verified]:** AU2 (automated-decision transparency in APP 1.7 to 1.9 starts on 10 December 2026; the OAIC published its APP 1 guidance on 30 September 2026), AU3 (the OAIC sweep) and AU5 (AI Safety Institute, early 2026, $29.9 million).
- **Australia, AU6 and new row AU6a:** the NSW digital work systems bill is now law (Act No. 5 of 2026, assented 18 February 2026), so it moves to its own row, AU6a, as Binding in scope. Deepfake sexual material offences already exist under a 2024 Act; AU6 now covers only the further restrictions under consideration and Victoria.
- **Australia, AU3a, AU4, AU7 and AU8:** a breach of APP 1.7 joins the infringement-notice list from 10 December 2026 (AU3a, now [Verified]). The Guidance for AI Adoption dates from 21 October 2025 and replaces the Voluntary AI Safety Standard (AU4, now [Verified]). The Treasury review of AI and the Consumer Law is recorded (AU7). An amended CPS 230 started on 1 July 2026 and APRA wrote to industry on AI on 30 April 2026 (AU8, now [Reported]).
- **Brazil, now [Verified]:** BR1 (the AI bill PL 2338/2023 still waits for the rapporteur's opinion in the Chamber's special committee; nothing logged since 2 September 2026) and BR3 (the ANPD's AI sandbox, priority themes and duties towards minors under Decreto 12.880/2026).
- **Brazil, BR2 and BR4:** the ANPD became a special-regime agency under Lei 15.352/2026 (BR2). Decreto 13.135/2026 on customer service, in force on 2 November 2026, allows AI and automated service only with the option of a real-time human agent (BR4). Both stay [Recalled] because the LGPD and Consumer Code texts could not be read automatically.
- **Canada, now [Verified]:** CA2 (PIPEDA), CA3 (Quebec, s. 12.1 on automated decisions), CA5 (the voluntary code, 46 signatories), CA6 (OSFI E-23, effective 1 May 2027), CA7 (Bills C-34 and C-36, both at second reading) and CA8 (Ontario's Enhancing Digital Security and Trust Act and its AI directive; the label moves from Unclear to Binding in scope).
- **China, now [Verified]:** CN1 to CN4 (generative AI, algorithm recommendation, deep synthesis and labelling, with official titles and dates). CN5 is a trial measure in force on issue (20 March 2026). CN6 is final: CAC Order No. 21, in force 15 July 2026. CN8: the State Council's 2026 work plan commits to comprehensive AI legislation; no draft is published.
- **China, CN7:** the Cybersecurity Law amendment took effect on 1 January 2026. The row stays [Reported] because the Data Security Law was not read.
- **Japan, now [Verified]:** JP1 (AI Promotion Act, Act No. 53 of 2025, fully in force 1 September 2025; no penalties), JP2 (AI Basic Plan of 14 July 2026), JP3 (AI Guidelines for Business version 1.2) and JP4 (the APPI amendment law promulgated on 17 July 2026, in force within two years, with a consent exception for statistics including AI development).
- **Home page (22 October 2026):** a Source Repository line in the document box now links to the GitHub repository and its contributing guide, and version 2.39 records this week's merged changes.
- **MITRE ATLAS:** every identifier exists in release 2026.09, every name the wiki gives matches it, and none is deprecated. The [MITRE ATLAS Crosswalk](../23_Framework_Crosswalks/07_MITRE_ATLAS_Crosswalk.md) now has a review date. No mapping changed.
- **EU, E14 now [Verified]:** the Commission's draft guidelines on high-risk classification are dated 19 May 2026, and the Commission's page (updated 19 October 2026) still calls them a draft. The consultation was open until 23 July 2026. See the [EU Regulatory Crosswalk](../12_EU_AI_Compliance/07_Regulatory_Crosswalk.md).
- **EU, E4:** the Council agreed its negotiating mandate on the Digital Omnibus for data and the GDPR on 21 October 2026 [Verified]. Talks with Parliament start once Parliament adopts its own position. The row stays [Reported] because no adoption date is given; "not before 2027" still comes from secondary sources.
- **Home page (24 October 2026):** version 2.42 records this week's verification.

### Still work in progress

- GCC: Bahrain's AI law (B3) is still listed as a draft; news reports this year disagree on whether it has passed. The Saudi copyright text and data mining exception (S9) and the Saudi AI risk framework (S5) still have no primary source.
- The SDAIA site rejected automated requests on 19 October 2026, so the Saudi rows S1 to S4 were not re-checked this week.
- India: the SEBI AI rules (IN7) and the IRDAI items (IN8) still lack a primary source; the SEBI notification PDF and the IRDAI site could not be read automatically. The RBI model risk guidance (IN6) is still a draft. The IT Act transition (IN11) was not checked.
- UK: UK2, UK4, UK5, UK7 and UK12 were not checked this week.
- Singapore: SG8 (Cybersecurity Act) was not changed; its 2024 amendment is confirmed but the commencement date was not found. Some IMDA pages refused automated retrieval.
- US: the California legislature site could not be read automatically, so US6 (SB 53, AB 2013) and US7 (AI Transparency Act; a further amendment, SB 1000, is reported) are unchanged. The Illinois General Assembly site refused automated retrieval, so US10 is unchanged. No final HIPAA Security Rule was found (US17).
- South Korea: the Korean text on law.go.kr, the decree amendment of 20 July 2026 and the template [KR-T2](../20_South_Korea_AI_Compliance/KR-T2_Generative_AI_Labelling_and_Notice.md), which still has a column for a "clearly fictional" exemption, need follow-up.
- Australia: AU1 (the date of the National AI Plan) could not be confirmed because the Department of Industry's publication pages refuse automated retrieval. The consolidated Privacy Act PDF and the NSW legislation site could not be read.
- Brazil: the LGPD and Consumer Code pages on planalto.gov.br could not be read automatically, so BR2 and BR4 stay [Recalled].
- Canada: CA1 (AIDA) and CA4 (the Treasury Board directive) are unchanged. The LEGISinfo bill pages could not be read automatically and the Treasury Board site refused the request.
- China: CN9 was not checked. The NPC website could not be read, so the NPC Standing Committee work plan and the NPC copy of the Cybersecurity Law amendment were not checked.
- Japan: JP5 (copyright) and JP6 (sector rules) are unchanged. The guidance on AI and copyright of 15 March 2024 and the FSA's AI discussion paper (version 1.1, 3 March 2026) were read, but the e-Gov law texts could not be read automatically.
- The hub pages of Australia, Brazil, Canada, China and Japan have not yet been brought in line with these crosswalk changes.
- Framework crosswalks: on 23 October 2026 the retrieval tool could not read any outside web page (Council of Europe, IEEE, European Commission, UNESCO, the G7 Code text, OECD.AI, OWASP, NIST and CIS). The status of the Council of Europe Convention (signatories, ratifications, entry into force), the IEEE 7000-series statuses, and the OWASP, NIST AI RMF, ISO/IEC, NIST CSF, CIS Controls and SOC 2 identifiers in the control library were therefore not re-checked this week.
- EU: E17 still says the Official Journal citation of EN 18286 is pending. Commission Implementing Decision (EU) 2026/2274 of 12 October 2026 now references EN 18286:2026 (EUR-Lex gives 14 October 2026 as its entry into force), but the Annex of the Decision could not be read automatically, so the row was not changed. It will be corrected, and E18 annotated, on the next EU check.
- No change found for GCC S8 and B3, India IN6 or Brazil BR1. The US HIPAA Security Rule update (US17) was not checked against a primary source.

## 18 October 2026: Full version history moved here

### What is new

- The complete version history, from 1.0 to the latest version, now lives at the end of this page, newest first.
- [Section 20 of the home page](../index.md#20-version-history) shows only the three latest versions, with a link here.
- From now on this page is maintained as an append-only record, including the results of the regular verification runs on the regional and framework crosswalks.

### What was checked and what was not

- The rows were moved without changing their wording. The only new row is version 2.38, for this change.

## 17 October 2026: Eight more templates

### What is new

Eight templates were added to the [Templates](../25_Templates/index.md) section, each on its own page with a download link. Page names now end in the file type, (.xlsx) or (.docx).

- **[AI System Inventory Template (.xlsx)](../25_Templates/02_AI_System_Inventory_Template.md):** the GCC and EU inventory templates and T01 tiering in one sheet, with record checks, review alerts, a discovery sweep log and a dashboard.
- **[AI Use-Case Risk Triage Template (.xlsx)](../25_Templates/03_AI_Use_Case_Risk_Triage_Template.md):** a prohibited-use screen, the triage questions, T01 tier scoring, the register risks that apply and the impact assessment trigger.
- **[AI Security Vendor Evaluation Scorecard (.xlsx)](../25_Templates/04_AI_Security_Vendor_Evaluation_Scorecard.md):** up to five vendors on the eight evaluation domains, required vendor evidence, PoC notes and a GCC and EU supplier due-diligence questionnaire.
- **[AI Security Audit and Evidence Checklist Template (.xlsx)](../25_Templates/05_AI_Security_Audit_and_Evidence_Checklist_Template.md):** control tests, the GCC and EU audit checklists and evidence registers, a findings log, an exception register and ISO/IEC 42001 readiness.
- **[AI Security Control Library and Crosswalks Template (.xlsx)](../25_Templates/06_AI_Security_Control_Library_and_Crosswalks_Template.md):** the {{n:controls}} controls with tracking columns, every framework crosswalk item and coverage by framework and by risk.
- **[AI Security Test Case Tracker Template (.xlsx)](../25_Templates/07_AI_Security_Test_Case_Tracker_Template.md):** the quick-start PoC scenarios and all {{n:tests}} test cases, with scoring rules and coverage by control and by risk.
- **[AI Acceptable Use Policy Template (.docx)](../25_Templates/08_AI_Acceptable_Use_Policy_Template.md):** a policy draft with a policy-to-control mapping, a quick reference card and a user acknowledgement form.
- **[AI Impact Assessment Template (.docx)](../25_Templates/09_AI_Impact_Assessment_Template.md):** a combined data protection and fundamental rights impact assessment that adds benefits, misuse and interested parties from ISO/IEC 42005.

### What was checked and what was not

- The workbooks were recalculated with no formula errors, and the triage workbook gave the same result as the wiki for its three worked examples. The Word documents passed a schema check and were rendered to check their layout.
- Settings marked orange in the workbooks, and placeholders in the Word documents, are defaults or decisions for the organization, not values from a standard.
- The regional questions and citations come from the wiki's GCC and EU pages, which say they must be checked against the legal texts. The templates are not legal advice.

## 17 October 2026: Templates section and AI Risk Register Template

### What is new

- **[Templates](../25_Templates/index.md):** a new section, before Community Rules in the sidebar, for files you can download and fill in.
- **[AI Risk Register Template](../25_Templates/01_AI_Risk_Register_Template.md):** an Excel workbook with the {{n:risks}} register risks pre-filled, use-case triage, likelihood by impact scoring with editable settings, mapped controls and evidence, the framework and regional regulatory crosswalks, a dashboard, deadline alerts and record checks. It carries a License sheet and file metadata for CC BY-SA 4.0.

### What was checked and what was not

- The workbook's formulas were recalculated with no errors, and sample triage answers, dates and treatment decisions were entered to check the triage result, deadlines, appetite check and record checks.
- Its ratings are the register's generic examples and its settings (scales, bands, deadlines, appetite, acceptance authority) are defaults, not values from a standard.
- Where a crosswalk names only controls, framework items are linked to risks through those controls; these links are broader than a direct mapping and are marked in the workbook.

## 17 October 2026: Incidents, agent architecture patterns and the OWASP MCP Top 10

A review of the wiki against current agent and MCP security guidance found three gaps: the wiki named almost no real incidents, it said what to control in an agent but not how to arrange an agent so that a fooled model cannot leak data, and it did not cover the OWASP MCP Top 10.

### What is new

- **[AI Security Incident Casebook](20_AI_Security_Incident_Casebook.md):** nine cases (EchoLeak, the GitHub MCP toxic agent flow, postmark-mcp, mcp-remote, MCP Inspector, the Amazon Q Developer extension, the Replit database deletion, the Air Canada chatbot ruling and Mata v. Avianca), each mapped to register risks, controls and OWASP items, with the control that would have broken the chain.
- **[Agent Architecture Patterns](../24_Builder_Track/02_Agent_Architecture_Patterns.md):** the lethal trifecta and Meta's Agents Rule of Two, six design patterns for containing prompt injection (including Dual LLM, Plan-Then-Execute and CaMeL), identity standards for agents (RFC 8693, RFC 8707, DPoP, workload identity), the MCP specification's ban on token passthrough, tracing and shutdown, a twelve-question architect's review checklist and four exercises.
- **[OWASP MCP Top 10 Crosswalk](../23_Framework_Crosswalks/19_OWASP_MCP_Top_10_Crosswalk.md):** the ten items mapped to wiki risks and controls; 8 direct and 2 partial.
- **Triage question A6** in the [AI Use-Case Risk Triage](../02_Risk_Management/02F_AI_Use_Case_Risk_Triage.md) asks whether a session combines all three legs of the trifecta.

### What was checked and what was not

- Each incident was checked against the source linked beside it (the researcher's or vendor's write-up, a CVE advisory, a court decision or a report citing one) on 17 October 2026. Four of the nine sources are secondary reports (SOC Prime, TechRadar, the AI Incident Database and a law firm's case summary) rather than the original advisory or decision.
- The MCP Top 10 identifiers and titles were read from the OWASP project page, which calls the list a beta; titles may still change. One title differs from some summaries of the list: MCP06 is "Prompt Injection via Contextual Payloads".
- The trifecta, the Rule of Two, the six design patterns, CaMeL, the MCP specification requirements and the titles and purpose of RFC 8693, RFC 8707 and RFC 9449 were read from their primary sources.
- OpenTelemetry's generative AI conventions are named as an option, at the Development stability level. Their status was read from a secondary summary, because the OpenTelemetry pages moved to a new repository.
- No test cases were added for these pages yet.

### Second check, 17 October 2026

Every statement on these pages that came from the review's source material was checked again against its primary source. Corrections made: EchoLeak now describes the actual exfiltration path (reference-style Markdown and a Teams domain allowed by the content security policy) with a second source; the Air Canada and Mata v. Avianca cases give exact dates, courts and what the source says; the mcp-remote case gives its disclosure date; the RFC descriptions now match each RFC's stated purpose; and the OpenTelemetry link points to the conventions' new repository with their stability level. None of the statements was contradicted by its source; the fixes add missing detail, correct imprecise wording or replace a link that had moved.

## 17 October 2026: Risks from the AI Risk Map

The wiki's risk register was compared with the *AI Risk Map* v1.3 (2026) by Evan Wheeler, RiskFramework.org, a one-page map of 196 AI risk factors in 12 domains, grouped by who owns each risk. The map is licensed CC BY-SA 4.0, the same licence as the wiki, so its content could be adapted with credit. The comparison found the register strong on security, data and agent risks and thin on risks owned outside security.

### What is new

- **Eighteen register risks, AI-R29 to AI-R46**, adapted from the map: unrealised value, cost volatility, provider concentration and lock-in, model monoculture, deskilling, workforce change, energy and water use, output ownership and model licences, obligations triggered by modifying a model, legal hold, independent model validation, AI in financial reporting controls, AI-washing, emotional dependence, hallucinated package dependencies, safety training removed from self-hosted models, agent activity that looks like an attack, and insiders using agents to exceed their access. Each has controls and evidence in the [AI Risk to Control Mapping](../02_Risk_Management/02D_AI_Risk_to_Control_Mapping.md), and each names the map domain it came from.
- **Owner Domain column** on the [Enterprise AI Risk Register](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), using the map's twelve domains, with a suggested owner for each.
- **Methodology:** sections on risk factors versus scenarios, owner domains and when to quantify (for example with FAIR), and two new review triggers, in the [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md).
- **Triage:** section E of the [AI Use-Case Risk Triage](../02_Risk_Management/02F_AI_Use_Case_Risk_Triage.md) switches on the new risks.
- **[AI Risk Map Crosswalk](../23_Framework_Crosswalks/18_AI_Risk_Map_Crosswalk.md)**: the map's 55 categories mapped to register risks.
- The [NIST AI 600-1 Crosswalk](../23_Framework_Crosswalks/04_NIST_AI_600_1_GenAI_Profile_Crosswalk.md) now maps Environmental Impacts, homogenization and anthropomorphism to the new risks.

### What was checked and what was not

- The domain, category and risk factor wording was read from the one-page map PDF. The map's companion workbook, which gives the source of each factor, was not available, and the RiskFramework.org website could not be reached, so the map was not checked against either.
- The ratings of the new risks are illustrative, like the rest of the register. The FINOS cross-references for AI-R29 to AI-R46 have not been checked and are marked Not checked.
- The register entries paraphrase the map's factors rather than copy them. The mapping of map categories to wiki risks is this wiki's judgement.
- No test cases were added for the new risks yet.

## 16 October 2026: Control tiers and build-time counts

The 46 controls are split into 22 Baseline and 24 Advanced. The split is the author's judgement, not a framework requirement; the [Control Tiers](../03_Control_Library/06_Control_Tiers.md) page is generated from a Tier field in each control record, and the link check requires the ten Builder Track controls to be Baseline. Separately, totals such as the number of test cases, layers, controls and risks are now computed from the source at build time (`counts.py`) and written in pages as placeholders, so they cannot drift; the link check fails on a hand-typed total. Per-layer counts inside the test-method table in the Test Case Library index are still typed by hand.

## 16 October 2026: Regional verification and a freeze on new regions

India, the GCC and the EU were checked against primary texts where the texts could be fetched. India: the DPDP Act, the DPDP Rules (G.S.R. 846(E), phased commencement dates), the AI Governance Guidelines, the RBI FREE-AI report, the RBI draft model risk guidance and the CERT-In directions are now `[Verified]`; the IT Rules synthetic-content amendment and the SEBI amendments stay `[Reported]`; the IRDAI AI directive could not be confirmed and is `[Unverified]`. GCC: the UAE data protection law (article numbers) is `[Verified]`. The original EU AI Act Article 113 could not be retrieved, so those dates keep their earlier tags. Nothing outside these three sections was checked. New regions are frozen until the others are verified (see CONTRIBUTING.md).

## 16 October 2026: Builder Track

A review of the wiki found that it said well what to look for in an agent but gave builders little on how to secure one. The practitioner pages were short (the agentic standard is a single table) and there was no code anywhere in the wiki. The updates on this date work through that gap in order. This section covers the first.

### What is new

- **Standard Fields:** wording that repeated in most of the 668 test cases (scoring, pass and fail criteria, reviewer notes, standard evidence, and the lab setup for each layer) now lives once on the [Standard Fields](../10_Test_Case_Library/standard-fields.md) page, generated from `standard-fields.json`. A case shows a field only when it differs. This removes about 1.2 MB of repeated Markdown (about 42 percent of the case text) and 5,715 field entries; the cases now read as what is unique to each.
- **Payload Kit:** a new page, [Payload Kit](../10_Test_Case_Library/payload-kit.md), with a `kit/` folder of attack and legitimate-request sets for 36 of the 169 Critical test cases (all Critical cases in L06, L07 and L11 that a payload can test, plus selected L08, L09 and L10 cases) and a runner that compares an unprotected build with a protected one. Each covered case links to its payload file.
- **Test Your Own Application:** a new page, [Test Your Own Application](../10_Test_Case_Library/test-your-own-app.md), that restates the testing for an owner who can change the code. It drops the product and provider language, explains the setup, includes an adapter template, and gives a plain procedure for each of the 36 payload-kit cases.
- **Builder Track:** a new section with one page, [Secure Your First Agent: Ten Controls With Code](../24_Builder_Track/01_Secure_Your_First_Agent.md). It sets out ten controls in build order, each tied to an existing control objective, with working configuration and code for tool allow-lists, argument validation, scoped short-lived credentials, sandboxing, egress limits and approval gates.
- **Reference code:** the [`code/`](../24_Builder_Track/index.md#the-code) folder holds a guard, a sandbox wrapper, an allow-list egress proxy, container and Kubernetes settings, a policy file, and a demo in which a hijacked agent is stopped at every step. It uses only the Python standard library.

### What was checked

- For the Standard Fields change, every field of every case was rebuilt from its explicit text or the standard for its test method, kind of case or layer and compared with the original. All matched, so no wording was lost or altered. The link check now fails if a case repeats a standard word for word, and a deliberate repeat was used to confirm it does.
- The payload kit runner and stand-in applications have a test suite (38 tests). Eight deliberate breakages of the runner's judging were each caught. Against the stand-ins, the tool-governance cases pass and the cases that depend on what a model says fail, as expected; the resource-limit sandbox fails three of five probes.
- The Python code was run on Python 3.13 on Linux. The test suite passes, with one test skipped where the environment can already remove the network.
- To confirm that the tests protect something, twelve of the protective checks (path confinement, approval matching, self-approval, token signature, definition pinning, scope widening, private-address blocking, audit chain, child revocation, and the proxy's host, address and port checks) were switched off one at a time. The tests failed each time.
- A test checks that every code excerpt on the page appears word for word in the file it names.

### What is still work in progress

- The 36-case payload kit covers 36 of 169 Critical cases. The others are inventory, evidence, configuration or infrastructure checks, or need a browser, voice or training pipeline. It does not measure time, and its payloads were run only against a stand-in application, not against any real model or product.
- The Docker command and the Kubernetes manifest were not executed, because no container runtime was available. Their settings come from standard documented options and need to be checked against the versions you run.
- The reference code has not been through an independent security review.

## 15 October 2026: component ownership

This update compared the wiki's 17 layers with a nine-part list of AI application stack components: LLMs, agents, embeddings, RAG, AI security, MCP and tools, observability, vector databases and memory. Each part came with an ownership question, such as "who decides which models are approved for use?". The original source of that list was not verified. Every part already had a home in the 17 layers, but the wiki answered only two of the nine ownership questions in full. Agent memory had no owner at all, and observability covered security incidents but not quality failures.

### What is new

- **Component ownership:** the [AI Governance Operating Model](../08_Governance/16_AI_Governance_Operating_Model.md#component-ownership) now has a table that names the accountable role for each of the nine components, the roles to consult, and the test cases that check each decision. Two roles were added: AI Platform Owner and Agent Sponsor. The table is one workable allocation, not a requirement of any standard.
- **Agent memory:** four new cases, [TC-L07-042](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-042) to [TC-L07-045](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-045), cover a memory store inventory with owners, a policy on what may be remembered, user visibility and control, and memory in data subject access and erasure requests. [AI-CTRL-026](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-026) now asks for all four.
- **Embeddings and vector databases:** [TC-L11-026](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-026) to [TC-L11-028](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-028) cover approval of embedding models, content sent to external embedding providers, and approval and ownership of new indexes and collections.
- **Approval records:** [TC-L12-032](../10_Test_Case_Library/L12-model-layer.md#tc-l12-032) checks that each approved model has a decision record with a named approver, [TC-L08-043](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-043) that each guardrail policy has an owner and approved changes, and [TC-L06-047](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-047) that each tool or system grant to an agent is approved by the system owner and the agent's sponsor.
- **Observability:** [TC-L17-032](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-032) covers access, masking, retention and residency of AI tracing and evaluation tools, and [TC-L17-033](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-033) covers ownership and review of AI failures that are not security incidents.
- The library now holds 668 cases: 535 in the 17 layers and 133 in the six emerging domains.

### What was checked

The OWASP and NIST AI RMF mappings on the 12 new cases were checked on 15 October 2026. The OWASP identifiers and titles were checked against the OWASP GenAI Security Project's pages for the [Top 10 for LLM Applications 2025](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/). The NIST identifiers were checked against the subcategory text in [section 5 of the AI RMF 1.0 Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/). Every identifier exists, but several did not fit the case and were changed:

- GOVERN 1.1 covers legal and regulatory requirements, not roles or approvals. On the ownership and approval cases it was replaced with GOVERN 2.1 (roles and responsibilities), and on the policy cases with GOVERN 1.4 (transparent policies and procedures).
- MANAGE 2.3 (responding to previously unknown risks) was removed from TC-L06-047.
- LLM08:2025 Vector and Embedding Weaknesses does not cover sending content to third-party embedding providers. It was removed from TC-L11-027, and on TC-L11-026 it was replaced with LLM03:2025 Supply Chain, which covers vetting third-party models.
- TC-L07-044 now maps to LLM02:2025, which recommends transparency about how user data is used and a way to opt out. TC-L17-033 adds MANAGE 4.3 (incidents and errors communicated and tracked).

The same check was run on the 128 existing cases that cited GOVERN 1.1, which many of them used as a general governance tag. GOVERN 1.1 was kept on the 26 cases whose subject is a legal or regulatory requirement (data residency and sovereignty, privacy and data subject rights, biometric and recording consent, legal hold, licences and copyright, and regulatory incident reporting). On the other 102 cases it was replaced with the GOVERN subcategory that matches the case:

| Replacement | What it covers | Cases |
|---|---|---|
| GOVERN 1.4 | Policies, procedures and controls | 66 (policy enforcement, hardening, change control, policy as code) |
| GOVERN 6.1 | Third-party AI risk policies | 11 (vendor assessment, terms and assurance) |
| GOVERN 1.6 | AI system inventory | 5 |
| GOVERN 1.7 | Decommissioning AI systems | 4 |
| GOVERN 2.1 | Roles and responsibilities | 4 |
| GOVERN 4.3 | Testing, incident identification and information sharing | 4 |
| GOVERN 1.5 | Ongoing monitoring and periodic review | 3 (access recertification, false-positive review) |
| GOVERN 6.2 | Contingency for third-party failures | 3 |
| GOVERN 1.3 | Risk management effort set by risk tolerance | 2 (risk tiering) |

Each choice is a judgement about the closest fit, not a mapping published by NIST. The second identifier on each case (usually MANAGE 4.1 or MEASURE 2.10) was not reviewed. The four GOVERN 1.1 citations in the control library were checked and kept, because those controls cover data sovereignty, privacy and regulatory compliance, impact assessment, and regulator engagement.

### What is still work in progress

- The second NIST AI RMF identifier on older cases, often MANAGE 4.1, was not reviewed and may be a general tag in the same way.
- The thresholds in the new cases are starting values to tune, as for every case in the library.
- The layer-to-domain coverage matrix in the [Reference Index](../10_Test_Case_Library/00-reference-index.md) was not changed.

## 15 October 2026: AI governance frameworks

This update compared the wiki against a widely shared list of 30 AI governance frameworks and standards, and filled the gaps it found. Before it, the wiki mapped 10 of the 30 in depth, cited 2 without mapping them, and did not name the other 18.

### What is new

- **Four new crosswalk pages**, bringing the Framework Crosswalks section to 17 pages:
  - [NIST AI 100-2 Crosswalk](../23_Framework_Crosswalks/14_NIST_AI_100_2_Crosswalk.md): every NISTAML attack class identifier mapped to controls and test case layers.
  - [ISO/IEC AI Standards Crosswalk](../23_Framework_Crosswalks/15_ISO_IEC_AI_Standards_Crosswalk.md): ISO/IEC 38507, 42005, 42006, 23894, TR 24028, 5338, 23053, 22989 and the 5259 data quality series, clause by clause.
  - [Trustworthy AI and Ethics Standards Crosswalk](../23_Framework_Crosswalks/16_Trustworthy_AI_Ethics_Crosswalk.md): the EU Ethics Guidelines for Trustworthy AI, the UNESCO Recommendation on the Ethics of AI, and IEEE 7000, 7001, 7002, 7003 and 7010.
  - [International AI Instruments Crosswalk](../23_Framework_Crosswalks/17_International_AI_Instruments_Crosswalk.md): the Council of Europe Framework Convention on AI and the G7 Hiroshima Process Code of Conduct.
- **Board-level governance** (ISO/IEC 38507): the [AI Governance Operating Model](../08_Governance/16_AI_Governance_Operating_Model.md) now has a governing body, an accountable executive and a data owner for AI datasets, decisions reserved for the board, and board-level reporting.
- **Risk management** (ISO/IEC 23894): the [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md) now has a risk appetite statement, a communication and consultation step, more review triggers, and a table aligning each step of the ISO/IEC 23894 process with a wiki page.
- **Impact assessment** (ISO/IEC 42005): [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042) now asks for unintended uses and misuse, deployment regions and languages, data quality, and benefits as well as harms. The [AI Use-Case Risk Triage](../02_Risk_Management/02F_AI_Use_Case_Risk_Triage.md) now says which answers trigger a full impact assessment.
- **Certification readiness** (ISO/IEC 42006): the [AI Security Audit and Evidence Checklist](../06_Testing_and_Assurance/14_AI_Security_Audit_and_Evidence_Checklist.md) explains what an ISO/IEC 42001 certification audit will look for. The [Vendor Evaluation Master Framework](../05_Vendor_Evaluation/11_AI_Security_Vendor_Evaluation_Master_Framework.md) asks for the scope of a supplier's certificate.
- **Data quality** (ISO/IEC 5259): [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029) now requires a data quality profile with measured thresholds for each dataset, and [AI-CTRL-019](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-019) adds quality measures for retrieval corpora. Three new test cases, [TC-L10-031](../10_Test_Case_Library/L10-data-layer.md#tc-l10-031) to [TC-L10-033](../10_Test_Case_Library/L10-data-layer.md#tc-l10-033), test them. The library now holds 656 cases.
- **Bias** (IEEE 7003): [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) and the [GCC T10 Bias Testing Record](../11_GCC_AI_Compliance/T10_Bias_Testing_Record.md) now keep a versioned bias profile with the system's validated application boundaries.
- **Terminology** (ISO/IEC 22989): the [glossary](../09_Reference/18_AI_Security_Glossary_and_Taxonomy.md#standard-vocabulary) maps the standard's six AI stakeholder roles to the roles used in the wiki and the EU AI Act.
- **Advanced AI suppliers** (G7 Hiroshima Code): the [EU T12 GPAI Model Checklist](../12_EU_AI_Compliance/T12_GPAI_Model_Checklist.md) asks for a supplier's Hiroshima reporting framework report.

### Correction: NIST AI 100-2 in Foundations section 3.1

[Foundations section 3.1](../00_Foundations/03-Threat-Taxonomy.md#31-how-nist-classifies-attacks) misdescribed NIST AI 100-2e2025. It said that the report organises generative AI attacks into "evasion, poisoning, privacy and misuse" classes. In the published report, evasion, poisoning and privacy are the section headings of the **predictive** AI taxonomy. Both the predictive and the generative AI taxonomies classify attacks by the attacker's objective: availability (NISTAML.01), integrity (NISTAML.02), privacy (NISTAML.03), misuse (NISTAML.04, generative AI only) and supply chain (NISTAML.05). The section has been rewritten and was checked against the published PDF on 15 October 2026.

### UK AI Management Essentials (AIME) is withdrawn

Some lists of AI governance frameworks, including the one this update was checked against, present the UK's AI Management Essentials (AIME) as a current UK management standard. It is not. The UK Department for Science, Innovation and Technology (DSIT) published AIME as a draft self-assessment tool for consultation on 6 November 2024. Its government response, dated December 2025 and published on 6 February 2026, says that DSIT "will not be publishing AIME and therefore will not be making it a requirement of the government procurement process".

The response gives these reasons:

- Respondents found the tool's scope too broad to work as a single instrument.
- DSIT will instead write narrower guidance on foundational governance measures, aimed at small and medium-sized enterprises.
- DSIT will point organizations to other support, such as AI adoption hubs, rather than one tool.
- DSIT does not think it appropriate to link the guidance to specific legislation or standards.

The [UK AI Regulatory Hub](../21_UK_AI_Compliance/01_UK_AI_Regulatory_Hub.md) lists AIME as row UK13, a withdrawn draft, tagged [Verified] against the [government response](https://assets.publishing.service.gov.uk/media/6981d0758c1e89ed1e91bb55/AI_Management_Essentials_tool_government_response.pdf). The ten sections of the 2024 draft are still a reasonable lightweight self-check, but do not describe AIME as a UK requirement or standard.

### IEEE standards: based on available public data

IEEE standards are sold by IEEE, and their contents pages are not freely published. For IEEE 7000, 7001, 7002, 7003 and 7010, the wiki gives the title, year, status and scope as published on IEEE's own pages. Clause structures come from secondary public sources and, for IEEE 7001 and 7010, from papers by working group members that describe the draft standards. Each source is named on the [Trustworthy AI and Ethics Standards Crosswalk](../23_Framework_Crosswalks/16_Trustworthy_AI_Ethics_Crosswalk.md#ieee-7000-series-standards). Clause numbers have not been checked against the published standards.

### Verified in this update

These were checked on 15 October 2026 against the issuing body's own page or document, with a retrieval tool rather than line by line:

- ISO/IEC 38507, 42005, 42006, 23894, TR 24028, 5338, 23053, 22989 and 5259-1 to 5259-5: edition, title, clause numbers and clause headings, from publishers' pages and the free contents previews of standards stores.
- NIST AI 100-2e2025: section headings, attack classes and NISTAML identifiers, from the published PDF.
- EU Ethics Guidelines for Trustworthy AI: date and the seven requirements.
- UNESCO Recommendation: adoption date, values and principles from UNESCO's page; the eleven policy areas and their paragraph numbers from a copy of the full text.
- Council of Europe Framework Convention: article numbers and titles, Article 30(3) on entry into force, and the European Union's ratification on 15 May 2026.
- G7 Hiroshima Process Code of Conduct: the eleven actions, from the Code's text.
- UK AI Management Essentials: draft structure, consultation dates and the government response.

### Work in progress

These have not been fully verified. Treat them as provisional until a later update confirms them:

- **IEEE 7000, 7001, 7002, 7003 and 7010:** clause structures are from secondary public sources or describe drafts. IEEE 7002 has no public structure, so only its scope is given. The IEEE 7010 status page was found by search and not opened.
- **ISO/IEC standards:** only clause headings were read, not clause text, so every clause-to-control mapping is a judgment from the heading. The ISO page for ISO/IEC 23894 was not opened; its contents were checked in a store preview.
- **ISO/IEC 42006 audit time:** the factors that drive audit time (number of AI systems, high-risk uses, third-party AI) come from a secondary source.
- **Council of Europe Framework Convention:** the count of consents to be bound (only the EU as of 8 September 2026) comes from a secondary tracker, because the Treaty Office status page could not be read automatically. Whether each signatory has ratified has not been checked.
- **ALTAI:** the self-assessment web tool's address was found by search and not opened.
- **All mappings to wiki controls** on the four new crosswalk pages are this wiki's own judgment and have not been reviewed by the issuing bodies.
- **Not yet done:** recording NISTAML identifiers in each control and test case, so that the NIST AI 100-2 crosswalk can be generated at build time like the MITRE ATLAS one; adding the Council of Europe Convention to the regional hubs of its signatories; and a dedicated control for retiring AI systems (ISO/IEC 5338 clause 6.4.17).

## Full version history

Every version of the wiki, newest first. Rows are never edited after they are added.

| Version | Date | Author | Summary of Change |
|---|---|---|---|
| 2.52 | 2026-10-29 | Nachiket Sathaye | Home page "Latest update" now lists every update of the newest day, built by build.py from the Update Notes headings and the full version history, instead of a hand-written summary of the last change. |
| 2.51 | 2026-10-29 | Nachiket Sathaye | Builder Track runs on Windows: the sandbox uses a Windows Job Object for CPU, memory and process limits and reports which limits it applied, the git hooks fall back from python3 to python and run under Git for Windows, files are read and written as UTF-8, a PowerShell version of the container command, and every Builder Track test now runs in CI on Linux, macOS and Windows. |
| 2.50 | 2026-10-29 | Nachiket Sathaye | Builder Toolkit (Builder Track page 5): AI-specific code and configuration checker with ten rules and SARIF output, read-only MCP server, offline look-ups over the CSV data files, evidence export for the audit checklist and test tracker, instruction files for five coding assistants from one source, GitHub, GitLab and pre-commit examples, toolkit tests on Linux, macOS and Windows; Builder Track pages link register risks, templates, CSV files and the OWASP crosswalk, and six template pages link back. |
| 2.49 | 2026-10-29 | Nachiket Sathaye | CSV data files for the risk register, risk-to-control mapping, controls, test cases and AI Risk Map crosswalk, regenerated on every build; four workbooks rebuilt with AI-R47 to AI-R54 and the AI Risk Map credit linking its GitHub repository: AI Risk Register (version 1.3), AI Use-Case Risk Triage (1.1), Control Library and Crosswalks (1.4), Test Case Tracker (1.3). |
| 2.48 | 2026-10-29 | Nachiket Sathaye | Risk register 1.4: eight risks AI-R47 to AI-R54 (model extraction and inference, AI incidents, personal data inside models, training-serving skew, liability, unmaintained open-source components, unlabelled AI-generated content, agent actions others cannot identify), with control mappings and triage questions E13 to E19; AI-R29 and AI-R31 widened; the AI Risk Map Crosswalk now has 42 direct and 13 partial matches. |
| 2.47 | 2026-10-29 | Nachiket Sathaye | Risk register rules: the four tests a risk must pass to join the register (AI Risk Methodology 1.3), a Considered and Not Added list on the register (1.3), a rule in the contributing guide that risk, control and test case IDs are never reused, and the AI Risk Map Crosswalk (1.1) updated after reading the map's website, and every credit for the map now links its GitHub repository (wheels344i-gte/ai-risk-map). |
| 2.46 | 2026-10-25 | Nachiket Sathaye | NIST SSDF crosswalk added to the template workbooks: its 20 practices are now a column in the AI Risk Register (version 1.2) and Control Library and Crosswalks (1.3) framework matrices and rows in their Framework Crosswalk sheets. |
| 2.45 | 2026-10-25 | Nachiket Sathaye | Templates rebuilt from wiki 2.44: AI Risk Register (version 1.1), Audit and Evidence Checklist (1.2), Control Library and Crosswalks (1.2), Test Case Tracker (1.2) and Requirements Traceability Matrix (1.1) now carry AI-CTRL-025's new title and text, the extended control text, TC-L01-021 and a Hong Kong regulation column. |
| 2.44 | 2026-10-25 | Nachiket Sathaye | Financial regulators: new Hong Kong section (HKMA Supervisory Guidance for Responsible Adoption of AI of 15 October 2026, read in the HKMA text; SFC, PCPD, PDPO; HK-T1 self-assessment; principle crosswalk); new Financial Regulator AI Comparison page (MAS, RBI, SEBI, EU AI Act, FCA, HKMA on eight themes); AI-CTRL-025 renamed AI Containment and Kill Switch and widened to high-risk models, with new test case TC-L01-021; AI-CTRL-011, 012, 014 and 041 extended (unlisted AI restricted, board-approved AI strategy, no vendor training on data without authorisation, customer AI-use notice); India IN6 verified against the RBI draft text and new row IN13 for SEBI; UK5 updated for the FCA Mills Review. |
| 2.43 | 2026-10-24 | Nachiket Sathaye | Requirements traceability: every control now names the assurance stage at which it is first checked (Discovery, Design, Implementation, Platform or Production) and the deployment models it applies to (All, Cloud, or PaaS/IaaS/Self-hosted), enforced by the link checker; new AI Security Requirements Traceability Matrix template with one row per control requirement, vendor and assessor columns, a response check and a live dashboard; the Control Library and Audit Checklist workbooks carry the two new fields and were rebuilt from the current wiki; two templates by Nachiket Sathaye and Ankush Jain published: the AI System Security Risk Review Checklist (150 lifecycle review questions with impact and risk registers) and the AI Security Assurance Baseline (165 requirements in 14 domains, with an optional UAE and Dubai overlay). |
| 2.42 | 2026-10-24 | Nachiket Sathaye | Weekly crosswalk verification, second part (23 to 24 October 2026): MITRE ATLAS identifiers checked against ATLAS release 2026.09, with no change; weekly watch of proposed and pending rows in every region. EU E14 (draft guidelines on high-risk classification) confirmed against the Commission's pages and tagged [Verified]; EU E4 updated for the Council's negotiating mandate on the Digital Omnibus for data and the GDPR (21 October 2026). |
| 2.41 | 2026-10-23 | Nachiket Sathaye | Secure development and privacy in code, after a comparison with the ai-secure-by-design repository: new NIST SSDF and SP 800-218A crosswalk; the IDE coding assistant standard rewritten (version 2.0) to cover coding agents, pipeline agents, plugins, MCP servers and rules files, with pipeline gates and a test case per requirement; two new Builder Track pages with tested code, Privacy Duties in Code (DPDP consent, rights, retention, children's data, log redaction) and Developer Pipeline Checks (secrets, personal data in logs and an AI-Assistance trailer, run in git hooks, a coding agent's hook and CI); the Builder Track tests now run in CI. |
| 2.40 | 2026-10-22 | Nachiket Sathaye | Weak points addressed: validation level on every test case and a self-contained copy of the shared fields on each case and in the test tracker; scoring method and worked calibration examples in the risk methodology; committee charters, decision rights and a role-based training plan; outcome review of AI-CTRL-041 to 046 with three new cases; illustrative operating defaults; a predictive model monitoring and adversarial ML standard with two new cases; regulatory verification status and an obligation-level tracker; programme charter and incident report templates. |
| 2.39 | 2026-10-22 | Nachiket Sathaye | Weekly crosswalk verification (19 to 22 October 2026): the GCC, India, UK, Singapore, US, South Korea, Australia, Brazil, Canada, China and Japan crosswalks were checked against primary sources. Confirmed rows are tagged [Verified] with source and retrieval date, and out-of-date rows were corrected. The home page now links to the GitHub source repository. See the [note for the week ending 24 October 2026](#week-ending-24-october-2026-crosswalk-verification). |
| 2.38 | 2026-10-18 | Nachiket Sathaye | Update Notes now hold the full version history, newest first, and are only ever added to. This section of the home page shows the three latest versions. |
| 2.37 | 2026-10-17 | Nachiket Sathaye | Templates: added eight templates built from the wiki and licensed under CC BY-SA 4.0: AI System Inventory, AI Use-Case Risk Triage, AI Security Vendor Evaluation Scorecard, AI Security Audit and Evidence Checklist, AI Security Control Library and Crosswalks and AI Security Test Case Tracker (.xlsx), and AI Acceptable Use Policy and AI Impact Assessment (.docx). Template page names now show the file type. See the [Update Notes](../09_Reference/19_Update_Notes.md). |
| 2.36 | 2026-10-17 | Nachiket Sathaye | Added a Templates section with an AI Risk Register Template in Excel, built from the risk register, methodology, triage, control library and every framework and regional regulatory crosswalk, and licensed under CC BY-SA 4.0. Its ratings and settings are illustrative defaults. See the [Update Notes](../09_Reference/19_Update_Notes.md). |
| 2.35 | 2026-10-17 | Nachiket Sathaye | Added an AI Security Incident Casebook (nine incidents checked against their sources and mapped to risks and controls), an Agent Architecture Patterns page in the Builder Track (lethal trifecta, Agents Rule of Two, six prompt-injection design patterns, identity standards for agents and MCP, tracing, review checklist), an OWASP MCP Top 10 Crosswalk and triage question A6. See the [Update Notes](../09_Reference/19_Update_Notes.md). |
| 2.34 | 2026-10-17 | Nachiket Sathaye | Risk Management: added eighteen risks (AI-R29 to AI-R46) adapted from the AI Risk Map v1.3 by Evan Wheeler (RiskFramework.org, CC BY-SA 4.0), covering strategy and value, cost, provider concentration, workforce, energy use, licensing, legal hold, model validation, financial reporting, capability claims, emotional dependence and five security and agent risks. Added an Owner Domain column to the register, guidance on risk factors, ownership and quantification to the methodology, triage questions for the new risks and an AI Risk Map Crosswalk. See the [Update Notes](../09_Reference/19_Update_Notes.md). |
| 2.33 | 2026-10-16 | Nachiket Sathaye | Verified India, UAE and EU rows against primary texts where they could be fetched and added a Verified tag; froze new regions until the rest are checked. Split the controls into Baseline and Advanced tiers (new Tier field and a generated Control Tiers page). Counts that pages quote (cases, layers, controls, risks) are now filled in at build time. See the [Update Notes](../09_Reference/19_Update_Notes.md). |
| 2.32 | 2026-10-16 | Nachiket Sathaye | Moved wording that repeats across the test cases into one Standard Fields page. Cases show only the fields that differ from the standard. No wording was changed; the link check enforces the rule. See the [Update Notes](../09_Reference/19_Update_Notes.md). |
| 2.31 | 2026-10-16 | Nachiket Sathaye | Added the Payload Kit: runnable attack and legitimate-request sets, thresholds and a runner for 36 of the 169 Critical test cases, linked from each covered case, and a Test Your Own Application page for owners of the code. Tested against stand-in applications only. See the [Update Notes](../09_Reference/19_Update_Notes.md). |
| 2.30 | 2026-10-16 | Nachiket Sathaye | Added the Builder Track section: one page, "Secure Your First Agent: Ten Controls With Code", with ten controls in build order and working configuration and code for tool allow-lists, argument validation, scoped short-lived credentials, sandboxing, egress limits and approval gates. The `code/` folder holds a reference guard, sandbox and egress proxy, a runnable demo and a test suite. The Python code was run and tested; the container and Kubernetes settings were not executed. See the [Update Notes](../09_Reference/19_Update_Notes.md). |
| 2.29 | 2026-10-15 | Nachiket Sathaye | Governance operating model: added a component ownership table covering models, agents, embeddings, retrieval sources, guardrails, tool and MCP access, observability, vector databases and agent memory, and two roles (AI Platform Owner and Agent Sponsor). Added 12 test cases: agent memory governance (TC-L07-042 to TC-L07-045), embedding and index governance (TC-L11-026 to TC-L11-028), model approval records (TC-L12-032), guardrail policy ownership (TC-L08-043), tool access grant approval (TC-L06-047), and tracing platforms and quality failures (TC-L17-032 and TC-L17-033). Extended AI-CTRL-026 to cover memory inventory, write policy, user control and data subject requests. The library holds 668 cases. See the [Update Notes](../09_Reference/19_Update_Notes.md). |
| 2.28 | 2026-10-15 | Nachiket Sathaye | Framework Crosswalks: added four pages (NIST AI 100-2, ISO/IEC AI standards, trustworthy AI and ethics, and international AI instruments). Corrected Foundations section 3.1, which misdescribed the NIST AI 100-2 taxonomy. Marked the UK AI Management Essentials (AIME) as a withdrawn draft. Added governing body roles and ISO/IEC 38507 alignment to the governance operating model, ISO/IEC 23894 alignment to the risk methodology, ISO/IEC 42006 certification preparation to the audit checklist, and three data quality test cases (TC-L10-031 to TC-L10-033); the library holds 656 cases. The IEEE content is based on available public data, and unverified mappings are marked as work in progress. See the [Update Notes](../09_Reference/19_Update_Notes.md). |
| 2.27 | 2026-10-13 | Nachiket Sathaye | Framework Crosswalks: added six pages. Four are generated at build time from new fields in every control record (ISO/IEC 27001, NIST CSF, CIS Controls and SOC 2). The other two map the OECD AI Principles to wiki controls and compare eight privacy laws by theme. The section home page now has a table of every control's identifiers in every framework. Added NAIC, Colorado SB 21-169, FTC and HIPAA rows to the US section, and PCI DSS, insurance and health rows to the sector overlays. |
| 2.26 | 2026-10-10 | Nachiket Sathaye | Home, section 6: replaced the text flow of the AI security operating model with an image of the secure AI agent operating lifecycle. |
| 2.25 | 2026-10-10 | Nachiket Sathaye | Foundations, section 7.2: replaced the text diagram of the reference architecture with an image of the secure agentic AI system architecture, which shows the policy decision point and governance. Added a policy decision row to the layer table. |
| 2.24 | 2026-10-10 | Nachiket Sathaye | Singapore AI Compliance: updated from the MAS Guidelines on Artificial Intelligence Risk Management issued on 7 October 2026, which take effect on 7 October 2027. The crosswalk now maps the Guidelines paragraph by paragraph to wiki controls and test cases, and the SG-T2 template follows the final text. The sector overlays cite the Guidelines. |
| 2.23 | 2026-10-10 | Nachiket Sathaye | Added 21 test cases: nine on agent-to-agent communication (TC-L06-038 to TC-L06-046), six on identity for training jobs (TC-L13-021 to TC-L13-026) and six on identity for model serving and registries (TC-L12-026 to TC-L12-031). AI-CTRL-006 and AI-CTRL-015 now cite OWASP ASI07, AI-CTRL-016 maps to AI-R08, and three controls gained wording on agent-to-agent and workload identity. The library holds 653 cases. |
| 2.22 | 2026-10-10 | Nachiket Sathaye | Framework Crosswalks: added five pages. Four are generated at build time from the control library and the test cases (NIST AI RMF, ISO/IEC 42001, the OWASP Top 10 lists and MITRE ATLAS). The fifth maps the twelve generative AI risks in NIST AI 600-1 to the wiki's risks and controls. |
| 2.21 | 2026-10-10 | Nachiket Sathaye | GCC AI Compliance: checked four crosswalk rows (S2, S3, S4 and B1) against documents on the SDAIA and Bahrain Personal Data Protection Authority sites and tagged them [Verified]. SDAIA's current AI Ethics Principles document is SDAIA-P114E, version 1, May 2025. Most other government sites refused automated retrieval, so the remaining rows keep their tags. |
| 2.20 | 2026-10-10 | Nachiket Sathaye | EU AI Compliance: checked twelve crosswalk rows against the Official Journal or the issuing body's page and tagged them [Verified], with the primary URL and retrieval date. The Digital Omnibus on AI is confirmed as Regulation (EU) 2026/1744, in force since 27 July 2026, with the high-risk dates of 2 December 2027 and 2 August 2028. |
| 2.19 | 2026-10-10 | Nachiket Sathaye | Added three test cases (TC-L03-040 to TC-L03-042) for human oversight effectiveness and AI vendor terms, and pointed four existing cases at AI-CTRL-045 and AI-CTRL-046, so every control now has at least one test case. The library holds 632 cases. |
| 2.18 | 2026-10-10 | Nachiket Sathaye | Added a Risk, Control and Test Traceability page, generated at build time from the risk mapping and the test cases. Every page footer now shows the date the page last changed, and a page can record a review date with an optional `last_reviewed` line. |
| 2.17 | 2026-10-10 | Nachiket Sathaye | Added a Legal force column to the twelve regional crosswalks and their CSV files, so each instrument is labelled as binding law, binding in scope, guidance, voluntary, proposed, context or unclear. Added a link and identifier check for contributors, and rules for reusing the wiki to the Community Rules. |
| 2.16 | 2026-10-10 | Nachiket Sathaye | Changed the licence from CC BY 4.0 to CC BY-SA 4.0; earlier versions remain available under CC BY 4.0. Updated the US bank model risk references after SR 11-7 was replaced by SR 26-2 and OCC Bulletin 2026-13. |
| 2.15 | 2026-10-10 | Nachiket Sathaye | Added 15 risks to the register (AI-R14 to AI-R28), two controls (AI-CTRL-045 human oversight design and AI-CTRL-046 intellectual property), wording changes to six existing controls, FINOS AI Governance Framework columns in the risk to control mapping, a use-case risk triage page, a Framework Crosswalks section with the FINOS and AI BCF crosswalks, and a positioning statement on the home page. |
| 2.14 | 2026-10-07 | Nachiket Sathaye | Added four controls (AI-CTRL-041 to AI-CTRL-044: fairness, impact assessment, authority engagement, AI literacy), nine test cases (TC-L03-031 to TC-L03-039), a sector overlays page and a regional crosswalk by control theme. The regional sections now point to these controls and cases. |
| 2.13 | 2026-10-07 | Nachiket Sathaye | Added the US AI Compliance section: regulatory hub, role guide, templates and crosswalk. Its content comes from secondary sources and from memory of the law, and has not been verified against primary legal text. |
| 2.12 | 2026-10-07 | Nachiket Sathaye | Added the UK AI Compliance section: regulatory hub, role guide, templates and crosswalk. Its content comes from secondary sources and from memory of the law, and has not been verified against primary legal text. |
| 2.11 | 2026-10-07 | Nachiket Sathaye | Added the South Korea AI Compliance section: regulatory hub, role guide, templates and crosswalk. Its content comes from secondary sources and from memory of the law, and has not been verified against primary legal text. |
| 2.10 | 2026-10-07 | Nachiket Sathaye | Added the Singapore AI Compliance section: regulatory hub, role guide, templates and crosswalk. Its content comes from secondary sources and from memory of the law, and has not been verified against primary legal text. |
| 2.9 | 2026-10-07 | Nachiket Sathaye | Added the Japan AI Compliance section: regulatory hub, role guide, templates and crosswalk. Its content comes from secondary sources and from memory of the law, and has not been verified against primary legal text. |
| 2.8 | 2026-10-07 | Nachiket Sathaye | Added the India AI Compliance section: regulatory hub, role guide, templates and crosswalk. Its content comes from secondary sources and from memory of the law, and has not been verified against primary legal text. |
| 2.7 | 2026-10-07 | Nachiket Sathaye | Added the China AI Compliance section: regulatory hub, role guide, templates and crosswalk. Its content comes from secondary sources and from memory of the law, and has not been verified against primary legal text. |
| 2.6 | 2026-10-07 | Nachiket Sathaye | Added the Canada AI Compliance section: regulatory hub, role guide, templates and crosswalk. Its content comes from secondary sources and from memory of the law, and has not been verified against primary legal text. |
| 2.5 | 2026-10-07 | Nachiket Sathaye | Added the Brazil AI Compliance section: regulatory hub, role guide, templates and crosswalk. Its content comes from secondary sources and from memory of the law, and has not been verified against primary legal text. |
| 2.4 | 2026-10-07 | Nachiket Sathaye | Added the Australia AI Compliance section: regulatory hub, role guide, templates and crosswalk. Its content comes from secondary sources and from memory of the law, and has not been verified against primary legal text. |
| 2.3 | 2026-10-07 | Nachiket Sathaye | Added the EU AI Compliance section: regulatory hub, four role guides, twelve templates, proposed impact assessment control, crosswalk and evidence register. EU content comes from secondary sources and from memory of the legal text, and has not been verified against the Official Journal. |
| 2.2 | 2026-10-07 | Nachiket Sathaye | Added the GCC AI Compliance section: regulatory hub, four role guides, twelve templates, proposed fairness control, crosswalk and evidence register. Regional content is secondary-sourced and its verification is in progress. |
| 2.1 | 2026-10-07 | Nachiket Sathaye | Added the Foundations section (research paper: AI Security vs. Security of AI) and linked it from the purpose, navigation, framework mapping, roadmap, and metrics sections. |
| 2.0 | 2026-07-27 | Nachiket Sathaye | Expanded the home page with mission, strategic objectives, operating model, governance, standards hierarchy, framework mapping, maintenance rules, roadmap, metrics, and fuller navigation. |
| 1.0 | Initial release | Nachiket Sathaye | Initial wiki home page with purpose, audience, design principle, role navigation, lifecycle navigation, folder structure, and vendor-neutral operating rule. |
