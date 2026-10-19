---
title: "Update Notes"
author: Nachiket Sathaye
parent: "Reference"
nav_order: 2
description: "The full record of how the AI Security Wiki has changed: a note for each substantial update, with what was checked and what is still work in progress, and the complete version history since version 1.0."
document_type: AI Security Wiki Reference
version: 1.1
last_reviewed: 2026-10-19
---

# Update Notes

This page is the wiki's change record. It has two parts:

- **Update notes**, newest first: what changed in each substantial update, what was checked against sources, and what is still work in progress.
- **[Full version history](#full-version-history)**: every version since 1.0, newest first. The [home page](../index.md#20-version-history) shows only the three latest.

Entries are only ever added. Past entries are not rewritten or removed; when something in an earlier entry turns out to be wrong, the correction is recorded as a new entry that names the earlier one.

## Week ending 24 October 2026: crosswalk verification

### What was checked

- **GCC (19 October 2026):** every row of the [GCC Regulatory Crosswalk](../11_GCC_AI_Compliance/07_Regulatory_Crosswalk.md) was checked for changes, and the rows not yet verified were checked against the issuing bodies' own pages where those pages could be read: the UAE legislation portal, the Central Bank of the UAE, the Saudi National Cybersecurity Authority (NCA) and the UAE AI Office.

### What changed

- **GCC, now [Verified]:** U2 (UAE cybercrime law, Federal Decree-Law No. 34 of 2021) and S8 (NCA AI Cybersecurity Guidelines: a consultation draft, feedback closed 5 August 2026, no final text yet). U1 (UAE PDPL) was read again with no change.
- **GCC, U9 (CBUAE Guidance Note):** the CBUAE press release confirms the date (23 February 2026) and that it applies to licensed financial institutions. The row stays [Reported] because the note's own text has not been read.
- **GCC, U7 (ADGM Data Protection Regulations):** moved from [Unverified] to [Reported]. ADGM's own briefing slides give the enactment date (11 February 2021) and scope; the regulations text could not be retrieved.
- **GCC, B1 (Bahrain PDPL):** re-read on the Personal Data Protection Authority site; no amendment is listed.
- **GCC, O2 (Oman PDPL amendments):** an English translation of Royal Decree 68/2026 and news reports say the amendments were issued on 3 September 2026 and are in force. The row now reads Binding law, still tagged [Reported] because the Official Gazette text was not read.
- **GCC, U3 (UAE AI Charter):** the two primary sources give different dates, 10 June 2024 on the legislation portal and July 2024 on the document. Both are now cited and the row stays [Conflict].

### Still work in progress

- GCC: Bahrain's AI law (B3) is still listed as a draft; news reports this year disagree on whether it has passed. The Saudi copyright text and data mining exception (S9) and the Saudi AI risk framework (S5) still have no primary source.
- The SDAIA site rejected automated requests on 19 October 2026, so the Saudi rows S1 to S4 were not re-checked this week.

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
