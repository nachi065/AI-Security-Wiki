---
title: "AI Coding Assistant and Coding Agent Security Standard"
author: Nachiket Sathaye
parent: "Domain Standards"
nav_order: 2
description: "Controls for AI coding assistants and coding agents: inventory, approved models and accounts, context scope, command and file-system guardrails, scoped credentials, MCP servers and plugins, rules files, hooks, provenance of AI-made changes, and the checks that run before commit, in CI and at merge."
document_type: AI Security Wiki Reference
version: 2.0
last_reviewed: 2026-10-23
---

# AI Coding Assistant and Coding Agent Security Standard

> **Purpose:** Set controls for AI coding assistants and coding agents, and for the developer pipeline that receives the code they write.

> **Audience:** Developers, DevSecOps, application security, platform engineering, security engineering, AI product developers, audit.

> **How to use:** Use the scope table to decide which tools are in scope, then apply the control requirements and the pipeline gates. Each row names the wiki control it implements and the test case that proves it. The [Developer Pipeline Checks](../24_Builder_Track/04_Developer_Pipeline_Checks.md) page has a working reference for the checks before commit and in CI.

## Scope

| Kind of tool | What it can do | Main exposure |
|---|---|---|
| Completion and chat assistants in the IDE | Read the open files and workspace context; suggest code a developer accepts | Source code and secrets sent to a provider; insecure or licensed code accepted without review |
| Coding agents (IDE agent modes and command-line agents) | Read the repository, run shell commands, edit many files, call tools and MCP servers, commit | Everything above, plus actions taken with the developer's privileges, often faster than a person reviews them |
| Background and pipeline agents (cloud coding agents, review bots, fix bots) | Work on a branch, open or update pull requests, comment on reviews | Pipeline credentials, changes merged without a human reviewer, prompt injection from issues and pull requests |
| Extensions, plugins, MCP servers, rules files and agent settings | Extend or steer all of the above | Supply chain compromise, hidden instructions, settings that switch guardrails off |

A tool can move between rows: an assistant gains an agent mode in an update. Classify by what the tool can do in your environment, not by its name.

## Primary Risks

- Source code exposure.
- Credential and secret leakage, including secrets the agent reads from configuration files and writes into code or logs.
- Infrastructure information disclosure.
- AI-generated insecure code, and code that matches licensed public code.
- Packages that do not exist or were registered by an attacker under a name an assistant suggests.
- Unauthorized AI coding assistant, extension, plugin or MCP server installation.
- Destructive or out-of-scope commands run by an agent with the developer's privileges.
- Over-broad credentials given to agents: personal access tokens, cloud administrator profiles.
- Instructions hidden in repository files, comments, issues, dependency metadata or assistant rules files that steer an agent.
- Agent settings, hooks or rules files changed so that guardrails stop working.
- AI-made changes merged without anyone knowing an assistant or agent made them.

## Control Requirements

| Requirement | Control ID | Description | Evidence | Prove it with |
|---|---|---|---|---|
| IDE and Agent Discovery | [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004), [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) | Identify approved and unapproved AI coding tools, extensions, command-line agents and the MCP servers they are configured to use. | IDE and endpoint inventory, MCP configuration inventory | [TC-L05-004](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-004), [TC-L05-031](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-031), [TC-L06-037](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-037) |
| Approved Models and Accounts | [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004) | Allow only approved providers, models and corporate accounts; block personal accounts for corporate code. | Allow-list, account policy, block events | [TC-L08-042](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-042), [TC-L05-032](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-032) |
| Source Code Protection | [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004) | Detect submission of proprietary source code to AI assistants; exclude sensitive paths from the context an assistant or agent can read. | Detection logs, context exclusion settings, test evidence | [TC-L04-031](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-031), [TC-L05-033](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-033) |
| Secret Detection | [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004) | Detect API keys, tokens, credentials, certificates and connection strings in prompts, in agent writes and in commits. | Secret detection alerts, hook and CI results | [TC-L08-007](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-007), [TC-L14-006](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-006) |
| Prompt Inspection | [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002) | Inspect developer prompts where technically feasible. | Prompt logs or policy events | [TC-L04-031](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-031) |
| Command and File-System Guardrails | [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027) | Agents work inside the workspace. Destructive commands, network commands and writes outside the workspace need approval or are denied. Untrusted repositories are opened in a disposable container or virtual machine. | Agent permission settings, denial and approval logs | [TC-L06-036](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-036) |
| Scoped Agent Credentials | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) | Agents get short-lived tokens limited to the repository and the actions the task needs, never a developer's personal access token or a cloud administrator profile. | Token issuance records, scope listing | [TC-L09-026](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-026) |
| MCP Servers, Plugins and Extensions | [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) | Allow-list MCP servers, agent plugins and IDE extensions; pin versions; review updates and tool descriptions before approval. | Allow-list, review records, pinned versions | [TC-L06-037](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-037), [TC-L16-026](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-026) |
| Repository Content as Untrusted Input | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-026](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-026) | Treat READMEs, comments, issues, dependency metadata and assistant rules files as untrusted. Changes to rules files and agent settings need code-owner review. | Code-owner rules, review records, injection test results | [TC-L07-041](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-041) |
| Managed Agent Settings and Hooks | [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) | Organisation-managed settings fix the permission mode, the deny rules and the hooks; neither the developer nor the agent can switch them off in a governed workspace. Hooks that block are tested with a planted fake secret. | Managed settings file, hook test result | [TC-L06-036](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-036) |
| Generated Code Review | [AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033), [AI-CTRL-046](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-046) | Generated code goes through static analysis and human review; matches to licensed public code are flagged. | SAST results, review records, licence match reports | [TC-L05-034](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-034), [TC-L05-035](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-035) |
| Dependency Verification | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) | A package an assistant suggests must exist, come from an approved registry, and not be newly registered or typosquatted before it is added. | Dependency scan, registry allow-list | [TC-L05-019](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-019), [TC-L16-004](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-004) |
| Provenance of AI-Made Changes | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) | Every commit or pull request records whether an assistant or agent made it, in a form review rules and metrics can read. | Commit trailers or labels, review rules that use them | [TC-L14-021](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-021) |
| Review and Fix Bot Permissions | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016), [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030) | Pipeline agents cannot approve or merge their own changes and get only the permissions their task needs. | Bot permission listing, branch protection settings | [TC-L14-022](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-022) |
| Policy Enforcement | [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) | Monitor, warn, redact, block or investigate risky submissions. | Policy screenshots, alert logs | [TC-L04-032](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-032) |
| Auditability | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) | Attribute activity to user, device, IDE, agent and AI assistant, including the commands an agent ran. | Exportable audit records, agent session logs | [TC-L09-025](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-025) |
| SIEM Integration | [AI-CTRL-009](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009) | Forward events to SOC monitoring. | SIEM event ID, parser mapping | [TC-L17-009](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-009) |

## Pipeline Gates for AI-Assisted Code

The same checks run in four places. Only the last two cannot be skipped by the person or the agent making the change, so they are the controls; the first two make failures cheap.

| Stage | Checks | Automated | Blocks | Can be bypassed by the author |
|---|---|---|---|---|
| In the agent, before a write or command | Secrets in content to be written; commands against the deny rules | Yes | The action | Only if agent settings are not managed |
| Before commit (git hooks) | Secrets and personal data in logs in added lines; the provenance trailer | Yes | The commit | Yes (`--no-verify`, or a clone without hooks) |
| Continuous integration on every pull request | The same checks over every commit; static analysis; dependency verification; secret scanning with a maintained scanner | Yes | The merge, when the check is required | No, if branch protection requires the check |
| Merge | Human review, with a second reviewer for agent-made changes to sensitive paths; no self-approval by bots | Partly | The merge | No |

The release stages after merge (build, test, release, deploy, operate) are in the [CI/CD release stages](../08_Governance/18_AI_Operating_Defaults.md#cicd-release-stages-for-ai-applications) table. [Developer Pipeline Checks](../24_Builder_Track/04_Developer_Pipeline_Checks.md) has working code and tests for the first three stages.

## Developer AI Coding Rules

Developers must not submit:

- Production credentials.
- API keys, tokens or certificates.
- Complete proprietary source files.
- Internal application logic not approved for external processing.
- Infrastructure-as-code templates containing sensitive infrastructure details.
- Customer, employee or regulated data.
- Security configurations, firewall rules, detection logic or privileged workflow details.

All AI-generated code must be reviewed through secure coding, peer review and DevSecOps processes before use.

When using a coding agent, developers must also:

- Run it with the organisation's managed settings, and not switch to a mode that approves every action without review on a machine that holds production credentials.
- Open repositories they do not trust only in a disposable container or virtual machine.
- Give it a task-scoped token, not their own long-lived credentials.
- Read the diff before committing, and mark the commit as agent-made.

## PoC Tests

1. Submit proprietary source code to AI coding assistant.
2. Attempt to share API keys or tokens.
3. Upload infrastructure-as-code template.
4. Install unapproved AI extension.
5. Request generation of privileged system code.
6. Ask a coding agent to delete files outside the workspace and to call an unknown host ([TC-L06-036](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-036)).
7. Plant an instruction in a rules file and a code comment and check whether the agent follows it ([TC-L07-041](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-041)).
8. Ask an agent to save a file containing a fake key, then commit a fake key with `--no-verify`; the agent hook and CI must each block it.
9. Add an unapproved MCP server to an agent's configuration and check it is detected ([TC-L06-037](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-037)).

## Related Frameworks

- [NIST SSDF Crosswalk](../23_Framework_Crosswalks/20_NIST_SSDF_Crosswalk.md): the secure development practices of NIST SP 800-218 and the generative AI profile SP 800-218A, mapped to this standard and the control library.
- [OWASP MCP Top 10 Crosswalk](../23_Framework_Crosswalks/19_OWASP_MCP_Top_10_Crosswalk.md) for MCP servers used by coding agents.

## Version History

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-05 | Version first published in this repository: IDE assistants, data submitted to them, and five tests. |
| 2.0 | 2026-10-23 | Scope extended to coding agents, pipeline agents, plugins, MCP servers and rules files; new requirements for guardrails, credentials, managed settings, dependency verification and provenance; pipeline gates; test case for each requirement. |
