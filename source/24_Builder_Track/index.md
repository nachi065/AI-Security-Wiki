---
title: "Builder Track"
author: Nachiket Sathaye
description: "Start here if you are building with AI: ten controls for a first agent, privacy duties (consent, rights, retention, children's data) and developer pipeline checks, all with working code and tests that run in CI."
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
| `test_*.py` | Tests for all of the above, including a check that the pages' code excerpts match the files. The [Builder Track tests workflow](https://github.com/nachi065/AI-Security-Wiki/blob/main/.github/workflows/builder-tests.yml) runs them on Python 3.10 and 3.13 for every change to this section |

## How this fits the rest of the wiki

- The ten controls are control objectives from the [Control Library](../03_Control_Library/index.md). Their evidence and audit tests are there.
- The [Agentic AI Security and Tool Governance](../04_Domain_Standards/09_Agentic_AI_Security_and_Tool_Governance.md) standard says what must be in place. This section shows one way to build it.
- The [Test Case Library](../10_Test_Case_Library/index.md) is how you prove it.
- The [AI Coding Assistant and Coding Agent Security Standard](../04_Domain_Standards/07_IDE_AI_Coding_Assistant_Security_Standard.md) and the [NIST SSDF Crosswalk](../23_Framework_Crosswalks/20_NIST_SSDF_Crosswalk.md) put the pipeline checks in context.
