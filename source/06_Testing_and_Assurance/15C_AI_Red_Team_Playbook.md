---
title: "AI Red Team Playbook"
author: Nachiket Sathaye
parent: "Testing and Assurance"
nav_order: 3
document_type: AI Security Wiki Reference
version: 1.0
---

# AI Red Team Playbook

> **Purpose:** Provide adversarial testing guidance for AI applications, RAG systems, AI agents and vendor PoC validation.

> **Audience:** AI red teamers, AppSec, security researchers, AI product teams, assurance teams.

## Red Team Scope Areas

- Prompt injection.
- Indirect prompt injection.
- Jailbreak attempts.
- RAG manipulation.
- Sensitive output leakage.
- Unauthorized retrieval.
- Agent tool misuse.
- Excessive privilege execution.
- Unsafe AI-generated code.
- Model or dependency abuse.

## Test Categories

| Category | Objective | Evidence |
|---|---|---|
| Prompt Injection | Validate resistance to instruction override. | Test transcript, detection log |
| Indirect Injection | Validate malicious retrieved content does not control the model. | Malicious document, response, alert |
| Output Leakage | Validate sensitive response suppression. | Prompt, response, policy action |
| RAG Security | Validate retrieval stays within authorization boundary. | Source logs, permission test |
| Agent Abuse | Validate agent cannot execute unauthorized tools/actions. | Tool call log, approval denial |
| Guardrail Evasion | Validate safety and policy bypass attempts are detected. | Test report, issue tracker |

## What to Measure

Measure whether the system leaks information or performs an unauthorized action, not only whether it refuses a request. Report results as rates over defined test sets, with the model version, configuration and date. Threat modeling steps and the limits of testing are covered in [Assurance: Testing, Monitoring and Response](../00_Foundations/08-Assurance-Testing-Monitoring-and-Response.md).

## Reporting Template

```markdown
Finding ID:
Severity:
AI System:
Attack Type:
Steps to Reproduce:
Observed Behavior:
Expected Behavior:
Impact:
Evidence:
Recommended Remediation:
Retest Result:
```
