---
title: "Builder Track"
author: Nachiket Sathaye
coauthors: Ankush Jain
description: "Start here if you are building with AI: ten controls for a first agent, agent architecture patterns, privacy duties in code, developer pipeline checks, and a vendor-neutral toolkit (AI code checker, MCP server, evidence export, instructions for every coding assistant), all with working code and tests that run in CI."
nav_order: 14
has_children: true
---

# Builder Track

The rest of this wiki tells you what to govern, what to control and what to test. This section tells you how to build a first tool-using agent so that it passes those tests. It is short on purpose, and the code runs.

> **Audience:** AI product developers, application security engineers and platform engineers who are building or reviewing their first agent.

## Where to start

[Secure Your First Agent: Ten Controls With Code](01_Secure_Your_First_Agent.md) takes you through ten controls in build order. Each has the control it implements, the risk it addresses, a short explanation, and working configuration or code. It ends with the wiki test cases you should run against your own build.

[Agent Architecture Patterns](02_Agent_Architecture_Patterns.md) is the design layer behind those controls: the lethal trifecta and the Agents Rule of Two, six patterns that contain prompt injection, identity standards for agents and MCP, tracing, and an architect's review checklist.

[Privacy Duties in Code](03_Privacy_Duties_in_Code.md) turns the duties of India's DPDP Act into code: consent per purpose and notice version, access, correction, erasure, grievance and nomination, retention with advance notice, children's data, and logs without personal data.

[Developer Pipeline Checks](04_Developer_Pipeline_Checks.md) runs the same checks in three places (git hooks, a coding agent's hook and CI): secrets, personal data written to logs, and a trailer that records whether an assistant or agent made each change.

[Builder Toolkit](05_Builder_Toolkit.md) brings the wiki into the developer's loop whichever assistant, editor, operating system or CI service you use: a checker for AI-specific risks in code and agent configuration (with SARIF output), a read-only MCP server that any MCP client can use to look up controls, risks and test cases, an export that turns the agent's audit log into rows for the audit and test templates, and one set of rules written as the instruction file of each coding assistant.

| If you are... | Start with | Then use |
|---|---|---|
| Building a tool-using agent | [Secure Your First Agent](01_Secure_Your_First_Agent.md) | [AI System Inventory](../25_Templates/02_AI_System_Inventory_Template.md) to register it, [Test Case Tracker](../25_Templates/07_AI_Security_Test_Case_Tracker_Template.md) to record the tests |
| Designing or reviewing an agent architecture | [Agent Architecture Patterns](02_Agent_Architecture_Patterns.md) | [AI Use-Case Risk Triage](../25_Templates/03_AI_Use_Case_Risk_Triage_Template.md) |
| Handling personal data | [Privacy Duties in Code](03_Privacy_Duties_in_Code.md) | [AI Impact Assessment](../25_Templates/09_AI_Impact_Assessment_Template.md) |
| Setting up a repository or CI for AI-assisted work | [Developer Pipeline Checks](04_Developer_Pipeline_Checks.md) and the [Builder Toolkit](05_Builder_Toolkit.md) | [Audit and Evidence Checklist](../25_Templates/05_AI_Security_Audit_and_Evidence_Checklist_Template.md) for the results |
| Wiring the wiki into an assistant, agent or GRC tool | [Builder Toolkit](05_Builder_Toolkit.md) | The [CSV data files](../25_Templates/index.md#data-files-csv) |

## The code

Everything is in the [`code/`](code/) folder, uses only the Python standard library, and has tests that run in CI.

| File | What it is |
|---|---|
| [`guard.py`](code/guard.py) | The enforcement layer: identity, scoped tokens, tool allow-list and pinning, argument validation, approval gate, rate limits, kill switch, audit log |
| [`policy.json`](code/policy.json) and [`tool_definitions.json`](code/tool_definitions.json) | The agent registry, tool rules and reviewed tool definitions the guard reads |
| [`pin_definitions.py`](code/pin_definitions.py) | Writes the hash of each reviewed tool definition into the policy |
| [`sandbox.py`](code/sandbox.py) | Runs generated code with process limits and, where the kernel allows, no network |
| [`egress_proxy.py`](code/egress_proxy.py) | An allow-list forward proxy that checks hosts and resolved addresses |
| [`docker-sandbox.sh`](code/docker-sandbox.sh) and [`k8s-agent-pod.yaml`](code/k8s-agent-pod.yaml) | Container and Kubernetes settings for the real isolation boundary |
| [`agent_demo.py`](code/agent_demo.py) | A hijacked agent, played end to end with a scripted stand-in for the model |
| [`privacy.py`](code/privacy.py) and [`privacy_map.json`](code/privacy_map.json) | Consent ledger, rights desk, retention runner, children's gate and redacting logger, driven by one data map |
| [`pipeline_checks.py`](code/pipeline_checks.py) | Secret, personal-data-in-log and AI-Assistance trailer checks for git hooks, a coding agent's hook and CI |
| [`aiwiki_check.py`](code/aiwiki_check.py) and [`ai_rules.json`](code/ai_rules.json) | Checks code and agent configuration for AI-specific risks, with text, JSON or SARIF output |
| [`mcp_server.py`](code/mcp_server.py) | A read-only MCP server with wiki look-ups and the checks, for any MCP client |
| [`wiki_data.py`](code/wiki_data.py) | Offline look-ups and search over the wiki's CSV data files |
| [`evidence_export.py`](code/evidence_export.py) | Turns the guard's audit log and checker results into rows for the audit and test templates |
| [`gen_instructions.py`](code/gen_instructions.py) and [`agent_instructions.txt`](code/agent_instructions.txt) | Writes one set of rules as each coding assistant's instruction file |
| [`ci/`](code/ci/github-actions.yml) | GitHub Actions, GitLab CI and pre-commit examples |
| `test_*.py` | Tests for all of the above, including a check that the pages' code excerpts match the files. The [Builder Track tests workflow](https://github.com/nachi065/AI-Security-Wiki/blob/main/.github/workflows/builder-tests.yml) runs them on Python 3.10 and 3.13 for every change to this section, and runs the toolkit tests on Linux, macOS and Windows |

None of the code calls a model provider's API or depends on one assistant: the agent demo uses a scripted stand-in for the model, and the checks run from a terminal, git hooks, CI or any assistant that can run a command or call an MCP tool. The toolkit runs on Linux, macOS and Windows. The sandbox in [`sandbox.py`](code/sandbox.py) and the shell-based git hooks on the pipeline page need Linux or macOS.

## How this fits the rest of the wiki

- The ten controls are control objectives from the [Control Library](../03_Control_Library/index.md). Their evidence and audit tests are there. The [ten controls table](01_Secure_Your_First_Agent.md#the-ten-controls-at-a-glance) names the [register risks](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) each one treats.
- The [Agentic AI Security and Tool Governance](../04_Domain_Standards/09_Agentic_AI_Security_and_Tool_Governance.md) standard says what must be in place. This section shows one way to build it.
- The [Test Case Library](../10_Test_Case_Library/index.md) is how you prove it, and the [Payload Kit](../10_Test_Case_Library/payload-kit.md) uses this section's guard as one of its stand-in applications.
- The [Templates](../25_Templates/index.md) are where the results go, and the [CSV data files](../25_Templates/index.md#data-files-csv) are the same controls, risks and test cases in a form your tools and the [Builder Toolkit](05_Builder_Toolkit.md) can read.
- The [OWASP Top 10 Crosswalk](../23_Framework_Crosswalks/06_OWASP_Top_10_Crosswalk.md) and [OWASP MCP Top 10 Crosswalk](../23_Framework_Crosswalks/19_OWASP_MCP_Top_10_Crosswalk.md) map the OWASP risks the ten controls address.
- The [AI Coding Assistant and Coding Agent Security Standard](../04_Domain_Standards/07_IDE_AI_Coding_Assistant_Security_Standard.md) and the [NIST SSDF Crosswalk](../23_Framework_Crosswalks/20_NIST_SSDF_Crosswalk.md) put the pipeline checks in context.

## Evidence you can hand over

What a builder produces in this section, and where a risk owner or auditor records it.

| What you produce | Where it goes | Control it evidences |
|---|---|---|
| The agent's entry in `policy.json`: owner, tools, scopes and limits | A row in the [AI System Inventory](../25_Templates/02_AI_System_Inventory_Template.md) (Technical Owner, Can Take Actions in Other Systems, Tools, APIs or Agents It Can Call, Kill Switch Test Date) | [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006), [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) |
| The guard's hash-chained audit log | Rows from [`evidence_export.py`](code/evidence_export.py) in the [Audit and Evidence Checklist](../25_Templates/05_AI_Security_Audit_and_Evidence_Checklist_Template.md) | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) and the control behind each recorded decision |
| Results of the wiki test cases you ran against your build | The [Test Case Tracker](../25_Templates/07_AI_Security_Test_Case_Tracker_Template.md) | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) |
| CI runs of the pipeline checks and the AI checker (SARIF) | Evidence Ref in the [Audit and Evidence Checklist](../25_Templates/05_AI_Security_Audit_and_Evidence_Checklist_Template.md) | [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004), [AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033) |
| The privacy data map and consent records | The [AI Impact Assessment](../25_Templates/09_AI_Impact_Assessment_Template.md) | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) |
| A record of any incident or kill-switch use | The [AI Incident Report](../25_Templates/11_AI_Incident_Report_Template.md) | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) |

Evidence shows that something happened, not that a control works. The reviewer still decides the result.
