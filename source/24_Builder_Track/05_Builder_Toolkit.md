---
title: "Builder Toolkit: Checks, MCP Server and Agent Instructions"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Builder Track"
nav_order: 5
description: "Vendor-neutral tools that bring the wiki into the developer's loop: an AI-specific code and configuration checker with SARIF output, a read-only MCP server for any MCP client, offline look-ups of controls, risks and test cases, an evidence export for the wiki's templates, and one set of instructions for every coding assistant."
document_type: AI Security Wiki Reference
version: 1.0
---

# Builder Toolkit: Checks, MCP Server and Agent Instructions

> **Purpose:** Put the wiki's controls, risks and test cases where code is written, in a form that works the same whichever assistant, agent, editor, operating system or CI service a team uses.

> **Audience:** AI product developers, application security engineers, DevSecOps and platform engineers. Governance teams can use the evidence export without running anything else.

> **How to use:** Copy the files from the [`code/`](code/) folder into a `tools/` folder in your repository. Run the checker, wire it into git hooks and CI, connect the MCP server to your assistant if it supports MCP, and write the instruction files into your repository. Each section below says how.

## The one idea

The checks are code, not prompts. Anything that must give the same answer every time (does this line pass model output to `eval`, is this MCP server pinned, which controls does AI-R23 map to) runs in a small Python program with tests. An assistant can call it and explain the result, but it does not decide the result. So Claude, ChatGPT, Gemini, Copilot, Cursor, any other assistant, or a person at a terminal all get the same findings, and CI enforces them whoever wrote the code.

Every tool uses only the Python standard library (3.10 or later), so there is nothing to install. The toolkit's tests run on Linux, macOS and Windows on every change ([Builder Track tests workflow](https://github.com/nachi065/AI-Security-Wiki/blob/main/.github/workflows/builder-tests.yml)).

## What is in the toolkit

| File | What it does | Wiki asset it connects to |
|---|---|---|
| [`aiwiki_check.py`](code/aiwiki_check.py) and [`ai_rules.json`](code/ai_rules.json) | Checks code and agent configuration for AI-specific risks. Text, JSON or SARIF 2.1.0 output, with exit codes for hooks and CI | [Control Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md), [Test Case Library](../10_Test_Case_Library/index.md) |
| [`mcp_server.py`](code/mcp_server.py) | A read-only MCP server: wiki look-ups and the checks, for any MCP client, over stdio or local HTTP | All of the above, plus the [risk register](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| [`wiki_data.py`](code/wiki_data.py) | Offline look-ups and search over the wiki's [CSV data files](../25_Templates/index.md#data-files-csv) | [Templates and data files](../25_Templates/index.md) |
| [`evidence_export.py`](code/evidence_export.py) | Turns the guard's audit log and checker results into rows for two Excel templates | [Audit and Evidence Checklist](../25_Templates/05_AI_Security_Audit_and_Evidence_Checklist_Template.md), [Test Case Tracker](../25_Templates/07_AI_Security_Test_Case_Tracker_Template.md) |
| [`gen_instructions.py`](code/gen_instructions.py) and [`agent_instructions.txt`](code/agent_instructions.txt) | Writes one set of AI security rules as the instruction file each coding assistant reads | [Secure Your First Agent](01_Secure_Your_First_Agent.md) |
| [`ci/`](code/ci/github-actions.yml) | Examples for [GitHub Actions](code/ci/github-actions.yml), [GitLab CI](code/ci/gitlab-ci.yml) and the [pre-commit framework](code/ci/pre-commit-config.yaml) | [Developer Pipeline Checks](04_Developer_Pipeline_Checks.md) |
| [`test_toolkit.py`](code/test_toolkit.py) | Tests for all of the above | |

## How it fits with ai-secure-by-design

Ankush Jain's [ai-secure-by-design](https://github.com/ankush1982/ai-secure-by-design) (v0.2, commit `70ef026`, 24 October 2026) is a platform-neutral engine for secure and private development: NIST SSDF, ISO/IEC 27001 and India's DPDP Act, with code scaffolds for consent, data principal rights, audit logging and human oversight. This toolkit does not repeat it. It adds what that engine leaves out: AI-specific rules (what happens to model output, how models and MCP servers are loaded) and look-ups into this wiki's controls, risks and test cases.

The two follow the same conventions, so they can run side by side in the same hooks and CI job:

| Convention | ai-secure-by-design | This toolkit |
|---|---|---|
| Rules as data, each with a stable ID | `rules/*.yaml`, `SBD-*` | `ai_rules.json`, `AIW-*` |
| Output | text, JSON, SARIF 2.1.0 | text, JSON, SARIF 2.1.0 |
| Exit codes | 0 clean, 1 findings at or above `--fail-on`, 2 error | the same |
| Gate only the lines a change adds | `--staged`, `--diff` | `--staged`, `--diff` |
| MCP server | read-only tools, stdio and HTTP | read-only tools, stdio and HTTP |
| Instruction files from one source | yes | yes |
| Runtime | Node.js 20 or later | Python 3.10 or later |

The comparison is from reading that repository's files on 29 October 2026; it may have changed since.

## The checker

```sh
python tools/aiwiki_check.py src/ config/              # files or folders
python tools/aiwiki_check.py --staged                  # only lines added in the staged change
python tools/aiwiki_check.py --diff origin/main        # only lines added since a base (CI)
python tools/aiwiki_check.py --stdin --filename app.py < new_content.py   # content an agent is about to write
python tools/aiwiki_check.py . --format sarif --output aiwiki.sarif --fail-on MEDIUM
```

Use `python3` where `python` is not on the path. Exit codes are 0 for no findings at or above `--fail-on` (default `HIGH`), 1 for findings, and 2 for a usage or runtime error. To accept one line after review, add a comment containing `aiwiki: ignore AIW-004` (or `aiwiki: ignore` for every rule) and record why.

| Rule | What it looks for | Severity | Controls | Prove the fix with |
|---|---|---|---|---|
| AIW-001 | Model output reaching `eval`, `exec` or a shell | High | [AI-CTRL-020](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-020), [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022), [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027) | [TC-L05-015](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-015), [TC-L06-025](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-025) |
| AIW-002 | Model output rendered as raw HTML | Medium | [AI-CTRL-020](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-020) | [TC-L05-014](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-014), [TC-L05-020](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-020) |
| AIW-003 | Model output formatted into a SQL statement | High | [AI-CTRL-020](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-020), [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022) | [TC-L05-015](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-015), [TC-L06-014](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-014) |
| AIW-004 | Model or data files loaded with `pickle`, `joblib`, `torch.load` without `weights_only=True`, or `allow_pickle=True` | High | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) | [TC-L12-002](../10_Test_Case_Library/L12-model-layer.md#tc-l12-002), [TC-L12-004](../10_Test_Case_Library/L12-model-layer.md#tc-l12-004), [TC-L16-005](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-005) |
| AIW-005 | `trust_remote_code=True` | High | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031), [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027) | [TC-L16-003](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-003), [TC-L16-004](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-004) |
| AIW-006 | Hub models downloaded without a pinned `revision` | Low | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) | [TC-L12-018](../10_Test_Case_Library/L12-model-layer.md#tc-l12-018), [TC-L16-001](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-001) |
| AIW-007 | MCP servers launched with `npx`, `uvx`, `pipx` or `docker` without a fixed version or image digest | Medium | [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) | [TC-L06-006](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-006), [TC-L06-008](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-008), [TC-L06-037](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-037) |
| AIW-008 | Remote MCP servers reached over `http://` | High | [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024), [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) | [TC-L06-010](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-010) |
| AIW-009 | MCP tools approved automatically (`autoApprove`, `alwaysAllow`, `trust`) | Medium | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024) | [TC-L06-015](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-015), [TC-L06-016](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-016) |
| AIW-010 | Coding agents started with approvals or the sandbox switched off in scripts and CI | Medium | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027), [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004) | [TC-L06-036](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-036) |

The MCP rules read JSON configuration files that hold an `mcpServers`, `servers` or `mcp.servers` object, which covers the layouts several clients use. AIW-010 matches flag and setting names taken from several vendors' coding agents. Both lists come from documentation as of mid-2026 and were not re-checked for this page, so check your own tools' current names and add any that are missing to `ai_rules.json`.

To add a rule, add an entry to `ai_rules.json` with a pattern, the controls it supports and the test cases that prove the fix. The tests check that every control, risk and test case a rule names exists in the wiki.

## The MCP server

The [Model Context Protocol](https://modelcontextprotocol.io/) is an open protocol that many assistants, agents and editors use to call tools. Any client that supports MCP can use this server; nothing in it is specific to one vendor.

| Tool | What it returns |
|---|---|
| `wiki_get` | One control, risk or test case, with related IDs and the URL of its wiki page |
| `wiki_search` | Controls, risks or test cases matching every word of a query |
| `wiki_controls_for_risk` | The controls the wiki maps to one register risk, and the evidence it expects |
| `wiki_tests_for_control` | The test cases that test one control |
| `check_ai_code` | The checker's findings for text an assistant is about to write |
| `check_secrets` | The [pipeline checks'](04_Developer_Pipeline_Checks.md) secret findings for the same text |

It also offers one prompt, `review-agent-design`, which asks the assistant to review a design against the ten controls in [Secure Your First Agent](01_Secure_Your_First_Agent.md) using the tools for IDs.

Every tool is read-only: none writes files, runs commands or reaches the network. Most local clients take a configuration entry of this shape (the outer key, such as `mcpServers` or `servers`, and the file it lives in differ by client, so check yours):

```json
{
  "mcpServers": {
    "ai-security-wiki": {
      "command": "python",
      "args": ["tools/mcp_server.py", "--data", "tools/data"]
    }
  }
}
```

`--data` points at a folder holding the wiki's [CSV files](../25_Templates/index.md#data-files-csv). Without it, the server looks for the `25_Templates/data` folder next to the Builder Track, which is where it is when you run it from a copy of this wiki.

**HTTP mode.** `python tools/mcp_server.py --http` serves the same tools at `http://127.0.0.1:8765/mcp`. It answers JSON over HTTP POST and does not open a server-sent event stream. It refuses to listen on any address other than loopback unless a bearer token is set (`--token`, or the `AIWIKI_MCP_TOKEN` environment variable), and it rejects requests whose `Host` or `Origin` header is not on its allow-list (`--allow-host`). Hosted assistants that can only reach remote servers need it published behind TLS and your own authentication; this reference does not provide that.

The server answers MCP protocol revisions 2025-06-18, 2025-03-26 and 2024-11-05. The tests drive it with JSON-RPC messages written from the specification, not with a vendor's client, so check it with your own client before relying on it.

## Look-ups from the command line

```sh
python tools/wiki_data.py control AI-CTRL-024
python tools/wiki_data.py risk AI-R23
python tools/wiki_data.py test TC-L06-008
python tools/wiki_data.py search "kill switch" --kind control
```

The answers come from the CSV files, which the wiki rebuilds from its pages on every build. The pages remain authoritative, and every answer includes the page's URL.

## Evidence for the templates

[`evidence_export.py`](code/evidence_export.py) reads the [guard's](01_Secure_Your_First_Agent.md#b10-log-every-decision-in-a-tamper-evident-trace) hash-chained audit log and any SARIF file, and writes two CSV files:

```sh
python tools/evidence_export.py --audit-log audit.jsonl --sarif aiwiki.sarif \
    --controls controls_evidence.csv --tests test_evidence.csv
```

- `--controls` has one row per control, using the column names of the Controls sheet in the [AI Security Audit and Evidence Checklist](../25_Templates/05_AI_Security_Audit_and_Evidence_Checklist_Template.md): Control ID, Control, Result, Evidence Ref, Evidence Collection Date and Auditor Notes.
- `--tests` has one row per test case, using the [Test Case Tracker's](../25_Templates/07_AI_Security_Test_Case_Tracker_Template.md) Date Run, Evidence Ref and Notes columns.

Each evidence reference includes the input file's SHA-256 prefix, so a reviewer can tell which file a row came from. The tool first checks the log's hash chain and says in the notes whether it holds; it exits with code 1 if a log has been edited. It records what was observed, not a verdict: a denied call shows that a control acted at least once, not that it is effective. Result and Score are left for the reviewer. The guard's decisions map to controls and test cases as in the [Prove it](01_Secure_Your_First_Agent.md#prove-it) table.

## One set of instructions for every assistant

[`agent_instructions.txt`](code/agent_instructions.txt) holds the rules a coding assistant should follow in a repository that builds AI features: treat model output as untrusted, enforce tool calls outside the model, ask before sensitive actions, sandbox generated code, pin models and MCP servers, run the checks before saving a file, and cite only wiki IDs it has looked up. [`gen_instructions.py`](code/gen_instructions.py) writes it into your repository as each assistant's own file:

```sh
python tools/gen_instructions.py --out .            # AGENTS.md, CLAUDE.md, GEMINI.md, Copilot and Cursor files
python tools/gen_instructions.py --out . --check    # in CI: fail if a file is missing or out of date
```

| File written | Read by |
|---|---|
| `AGENTS.md` | Several coding agents that follow the shared AGENTS.md convention |
| `CLAUDE.md` | Claude Code |
| `GEMINI.md` | Gemini CLI |
| `.github/copilot-instructions.md` | GitHub Copilot |
| `.cursor/rules/ai-security-wiki.mdc` | Cursor |

Which file each tool reads is from documentation as of mid-2026 and changes often; check each tool's current documentation. Existing files are never overwritten unless you pass `--force`, because they may hold your own instructions. Instructions guide an assistant; they do not enforce anything. The checks in git hooks and CI are the control.

## Wire it into hooks and CI

| Where | How | File |
|---|---|---|
| Any machine with git | The [pre-commit framework](https://pre-commit.com/) runs the checker on staged lines, plus the secret, personal-data and trailer checks | [`ci/pre-commit-config.yaml`](code/ci/pre-commit-config.yaml) |
| GitHub | Runs both sets of checks on the lines a pull request adds, and uploads SARIF so findings show in code scanning | [`ci/github-actions.yml`](code/ci/github-actions.yml) |
| GitLab | The same on merge requests, keeping the SARIF file as an artifact | [`ci/gitlab-ci.yml`](code/ci/gitlab-ci.yml) |
| Any other CI | Run `python tools/aiwiki_check.py --diff <base>` and fail the build on exit code 1 | |
| A coding agent's own hook | Pipe the content the agent is about to write into `aiwiki_check.py --stdin --filename <path>` and refuse the write on exit code 1 | |

Each agent passes data to its hooks in a different format, so this page does not ship an adapter per agent. Where the agent supports MCP, the `check_ai_code` tool does the same job. As [Developer Pipeline Checks](04_Developer_Pipeline_Checks.md#the-one-idea) explains, only the CI layer is a control; make the check required in branch protection.

## Run it

From the `code/` folder, with Python 3.10 or later:

```sh
python -m unittest -v test_toolkit      # the toolkit tests (any operating system)
python aiwiki_check.py .                 # the reference code is clean; the test fixtures are not
```

## Prove it

- Commit a line such as `exec(llm_output)` with the hooks installed, and again with `--no-verify`. The first must be blocked locally, the second in CI ([TC-L05-015](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-015)).
- Add an MCP server to your client's configuration as `npx -y some-server`. The checker must report AIW-007, and your tool inventory must record the pinned version you replace it with ([TC-L06-037](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-037)).
- Run the evidence export on a guard log, change one line of the log, and run it again. The second run must report the broken chain ([TC-L17-020](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-020)).

## Limits of this reference

> **Verify before use:** The rules are line-based pattern checks. They miss model output that passes through a variable with an unrelated name, and they can flag safe code; treat each finding as a prompt for a reviewer, and a clean result as no proof of safety. The MCP server has not been tested with any particular vendor's client. HTTP mode is for local use and has no TLS. Client configuration formats, instruction-file locations and agent flag names change often, and the ones on this page were not re-checked against each vendor's current documentation. The toolkit tests run on Linux, macOS and Windows; the rest of the Builder Track code needs Linux or macOS, because its sandbox uses Unix process limits.

## Related pages

- [Secure Your First Agent](01_Secure_Your_First_Agent.md) and [Agent Architecture Patterns](02_Agent_Architecture_Patterns.md)
- [Developer Pipeline Checks](04_Developer_Pipeline_Checks.md)
- [AI Coding Assistant and Coding Agent Security Standard](../04_Domain_Standards/07_IDE_AI_Coding_Assistant_Security_Standard.md)
- [OWASP MCP Top 10 Crosswalk](../23_Framework_Crosswalks/19_OWASP_MCP_Top_10_Crosswalk.md) and [NIST SSDF Crosswalk](../23_Framework_Crosswalks/20_NIST_SSDF_Crosswalk.md)
- [Templates and CSV data files](../25_Templates/index.md)
