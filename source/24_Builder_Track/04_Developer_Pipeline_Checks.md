---
title: "Developer Pipeline Checks for AI-Assisted Code"
author: Nachiket Sathaye
parent: "Builder Track"
nav_order: 4
description: "Working, tested checks that run in three places (git hooks on the developer's machine, a coding agent's pre-write hook, and CI): secrets, personal data written to logs, and a trailer that records how each change was made."
document_type: AI Security Wiki Reference
version: 1.0
last_reviewed: 2026-10-23
---

# Developer Pipeline Checks for AI-Assisted Code

> **Purpose:** Give a team that writes code with AI assistants and coding agents a small set of checks that run before a commit, inside the agent, and in CI, with a reference implementation that runs and has tests.

> **Audience:** Developers, DevSecOps and platform engineers. The [AI Coding Assistant and Coding Agent Security Standard](../04_Domain_Standards/07_IDE_AI_Coding_Assistant_Security_Standard.md) says what must be in place; this page shows one way to build the developer side of it.

> **How to use:** Run the tests in the [`code/`](code/) folder. Wire [`pipeline_checks.py`](code/pipeline_checks.py) in as git hooks, in your coding agent and in CI, as shown below. Then prove it with the test cases at the end.

## The one idea

Run the same checks in three places, and treat only the last one as the control.

| Where | What it is for | Can it be skipped? |
|---|---|---|
| Git hooks on the developer's machine | Cheap, fast feedback before a commit exists | Yes: `git commit --no-verify`, or a fresh clone without the hooks |
| The coding agent's hook before it writes a file or runs a command | Stops the agent writing a secret or a risky change, even when no human is watching each step | Yes, if the agent's settings can be changed by the user or the agent |
| CI on every pull request | The control: the same checks over every commit in the change, before merge | No, if branch protection requires the check |

AI assistants write code faster than people review it, and coding agents commit without a human typing each line. That makes the local layers more useful and does not make them sufficient. The CI layer is what the [CI/CD release stages](../08_Governance/18_AI_Operating_Defaults.md#cicd-release-stages-for-ai-applications) table means by the "Commit" stage.

## The checks

| Check | Why | Control | Prove it with |
|---|---|---|---|
| Secrets in added lines | Assistants copy keys from context into code, and agents read `.env` files | [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004), [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030) | [TC-L14-006](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-006), [TC-L14-002](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-002) |
| Personal data written to logs | Generated code often logs whole objects; the data map says which field names are personal | [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) | [TC-L10-007](../10_Test_Case_Library/L10-data-layer.md#tc-l10-007) |
| An `AI-Assistance` trailer on every commit | Review depth, metrics and incident analysis need to know which changes an assistant or agent made | [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) | [TC-L14-021](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-021) |

The personal-data check reads the same [data map](code/privacy_map.json) as the [privacy code](03_Privacy_Duties_in_Code.md), so a field classified once is checked everywhere.

## Secret patterns

The patterns are high-confidence formats only. They are Python regular expressions, so a pattern that starts with dashes, such as a private key header, is never mistaken for a command-line option. That mistake is easy to make in a shell hook, where `grep -P "$pattern"` with a leading dash fails and, with errors hidden, silently matches nothing. The tests check this case.

<!-- excerpt: pipeline_checks.py -->
```python
SECRET_PATTERNS = {
    "private key block": r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP |ENCRYPTED )?PRIVATE KEY-----",
    "AWS access key ID": r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b",
    "GitHub token": r"\bgh[pousr]_[A-Za-z0-9]{36,}\b",
```

This is a teaching reference. Also run a maintained secret scanner in CI, and treat a clean result as "nothing obvious", not "no secrets".

## The AI-Assistance trailer

Each commit message ends with one line that says how the change was made. This is this wiki's convention, not a standard. Use any wording your team prefers, as long as it is machine-readable and required.

<!-- excerpt: pipeline_checks.py -->
```python
TRAILER = re.compile(r"(?mi)^AI-Assistance:\s*(none|suggestions|agent)\s*$")
```

`suggestions` means a person accepted assistant suggestions; `agent` means a coding agent made the change. A team can then require a second reviewer for `agent` changes to sensitive paths, and count findings by value.

## Wire it in

**Git hooks.** Point git at a hooks folder kept in the repository, so every clone gets the same hooks:

```sh
mkdir -p .githooks
printf '#!/bin/sh\nexec python3 tools/pipeline_checks.py pre-commit\n' > .githooks/pre-commit
printf '#!/bin/sh\nexec python3 tools/pipeline_checks.py commit-msg "$1"\n' > .githooks/commit-msg
chmod +x .githooks/*
git config core.hooksPath .githooks
```

The tests in [`test_pipeline_checks.py`](code/test_pipeline_checks.py) install these two hooks in a throwaway repository and check that a secret or a missing trailer blocks the commit.

**The coding agent.** Many coding agents can run a command before they write a file or run a shell command, and refuse the action if the command fails. Send the content the agent is about to write to `pipeline_checks.py scan` on standard input; it exits with a non-zero status when it finds something. How the content reaches your hook, and which exit status blocks the action, differ between tools, so check your agent's hook documentation and test that a planted fake key is actually blocked. Keep the hook configuration in a file the agent cannot edit ([TC-L06-036](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-036)).

**CI.** Run the same checks over every commit in the pull request. The check needs the full history to find the base:

```yaml
- uses: actions/checkout@v4
  with:
    fetch-depth: 0
- run: python3 tools/pipeline_checks.py ci origin/${{ github.base_ref }}
```

Then make the check required in branch protection. Without that, the CI layer can be skipped like the others.

<!-- excerpt: pipeline_checks.py -->
```python
    elif mode == "ci":
        base = rest[0]
        findings = scan_diff(_git("diff", "--unified=0", "--no-color", f"{base}...HEAD"), fields)
        for sha in _git("rev-list", "--no-merges", f"{base}..HEAD").split():
            for f in check_trailer(_git("log", "-1", "--format=%B", sha)):
                findings.append(Finding(f.check, f"commit {sha[:12]}", f.detail))
```

## Run it

```sh
cd source/24_Builder_Track/code
python3 -m unittest -v test_pipeline_checks
```

The [Builder Track tests workflow](https://github.com/nachi065/AI-Security-Wiki/blob/main/.github/workflows/builder-tests.yml) runs these tests, and the rest of the Builder Track tests, on every change to this section.

## Prove it

- Commit a fake key with the hooks installed and with `--no-verify`. The first is blocked locally; the second must be blocked by CI ([TC-L14-002](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-002)).
- Ask the coding agent to save a file containing a fake key. The hook must refuse the write ([TC-L06-036](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-036)).
- Check that every merged commit in a sample of pull requests has the trailer, and that `agent` changes to sensitive paths had the extra review ([TC-L14-021](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-021)).

## Limits of this reference

- The secret patterns cover common formats only, and the personal-data check matches field names, not values. Both are prompts for a reviewer, not proof.
- The trailer records what the author declares. It does not detect undeclared AI use.
- It does not cover dependency scanning, package hallucination or code review of generated code. Those are in the [standard](../04_Domain_Standards/07_IDE_AI_Coding_Assistant_Security_Standard.md) and the release stages table.

## Related pages

- [AI Coding Assistant and Coding Agent Security Standard](../04_Domain_Standards/07_IDE_AI_Coding_Assistant_Security_Standard.md)
- [NIST SSDF Crosswalk](../23_Framework_Crosswalks/20_NIST_SSDF_Crosswalk.md)
- [Privacy Duties in Code](03_Privacy_Duties_in_Code.md)
- [Illustrative Operating Defaults: CI/CD release stages](../08_Governance/18_AI_Operating_Defaults.md#cicd-release-stages-for-ai-applications)
