---
title: "AI Risk Treatment Plan"
parent: "Risk Management"
nav_order: 3
document_type: AI Security Wiki Reference
version: 1.0
---

# AI Risk Treatment Plan

> **Purpose:** Define how AI risks are treated through phased visibility, controls, runtime protection, agent governance and continuous compliance.

> **Audience:** Risk owners, governance, security engineering, architecture review boards.

> **How to use:** Use this page as a wiki reference. Update the evidence, owners, control status, and links as implementation maturity improves.


## Treatment Strategy

| Phase | Objective | Key Activities | Outcome |
|---|---|---|---|
| Phase 1 — Visibility and Discovery | Understand AI usage and AI assets | Discover AI tools, users, endpoints, IDE plugins, SaaS AI, AI APIs and custom AI apps | AI inventory and usage baseline |
| Phase 2 — Data Protection and Enforcement | Reduce leakage through AI interactions | Enforce classification-aware prompt and upload controls; detect source code and credentials | Data leakage risk reduction |
| Phase 3 — Runtime Protection | Secure custom AI applications | Test prompt injection, RAG retrieval, output governance, AI API security | Production-ready AI application controls |
| Phase 4 — Agentic AI Governance | Prevent unauthorized AI-driven actions | Define agent identity, tool/API permissions, approval workflows, action logs | Controlled agentic AI adoption |
| Phase 5 — Continuous Governance | Maintain evidence and oversight | Periodic review, dashboard reporting, exception tracking, audit evidence | Sustainable AI governance maturity |

## Risk Treatment Options

| Option | When to Use | Required Evidence |
|---|---|---|
| Mitigate | Control can reduce likelihood or impact | Control configuration, test results, logs |
| Avoid | Risk exceeds tolerance or controls unavailable | Rejection decision, architectural notes |
| Transfer | Third party assumes contractual responsibility | Contract terms, SLA, audit rights |
| Accept | Residual risk is within tolerance | Risk acceptance record, owner approval, review date |

## Exception Handling

All exceptions must include business justification, affected AI platform, data classification, compensating controls, approval owner, expiry date and review cadence.
