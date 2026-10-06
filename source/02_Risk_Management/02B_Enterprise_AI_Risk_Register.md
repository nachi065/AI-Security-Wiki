---
title: "Enterprise AI Risk Register"
author: Nachiket Sathaye
parent: "Risk Management"
nav_order: 2
document_type: AI Security Wiki Reference
version: 1.0
---

# Enterprise AI Risk Register

> **Purpose:** Provide a sample enterprise AI risk register covering AI usage, development, applications, agents, auditability and sovereignty, as a starting template.

> **Audience:** Governance, cyber risk, security architecture, audit, AI product owners.

> **How to use:** Use this page as a template. Re-score each risk using the AI Risk Methodology for your own environment, and add owners, evidence and treatment status.

> **Illustrative example:** The ratings and entries on this page are generic examples, not an assessment of any specific organization. Replace them with your own findings before relying on them.

| Risk ID | Risk Area | Example Likelihood | Example Impact | Example Residual Risk | Example Priority |
|---|---|---|---|---|---|
| AI-R01 | Critical Infrastructure Information Exposure | High | Critical | Critical | 1 |
| AI-R02 | Shadow AI and Ungoverned AI Usage | High | High | High | 2 |
| AI-R03 | Sensitive Data Leakage Through Prompts and Uploads | High | Critical | High | 3 |
| AI-R04 | IDE-Based Source Code and Credential Exposure | Medium-High | High | High | 4 |
| AI-R05 | Prompt Injection Against Custom AI Applications | Medium | Critical | High | 5 |
| AI-R06 | AI Output Leakage and Oversharing | Medium | High | High | 6 |
| AI-R07 | AI Agent and Tool-Calling Abuse | Medium | Critical | Critical | 7 |
| AI-R08 | AI Supply Chain and Model Integrity Risk | Medium | High | High | 8 |
| AI-R09 | Lack of AI Auditability and Forensic Visibility | High | High | High | 9 |
| AI-R10 | Data Sovereignty and Third-Party Processing Risk | Medium | Critical | High | 10 |

## Risk Narratives

### AI-R01 — Critical Infrastructure Information Exposure
Users may submit sensitive infrastructure, architecture, security, operational or business information into AI tools for summarization, translation, troubleshooting or code support. Required controls include prompt inspection, upload inspection, classification-aware policy enforcement, audit logging and SOC alerting.

### AI-R02 — Shadow AI and Ungoverned AI Usage
Unapproved AI use may occur through public AI sites, browser extensions, IDE plugins, SaaS features, APIs or desktop AI applications. Required controls include AI discovery, tool classification, allow/monitor/warn/block policy, endpoint visibility and reporting.

### AI-R03 — Sensitive Data Leakage Through Prompts and Uploads
AI interactions can contain confidential data, personal data, credentials, source code, logs and business documents. Required controls include sensitive data detection, redaction/masking/warning/blocking and evidence generation.

### AI-R04 — IDE-Based Source Code and Credential Exposure
AI coding assistants can expose source code, API keys, internal URLs, infrastructure-as-code and application logic. Required controls include IDE visibility, secret detection, source code protection and developer governance.

### AI-R05 — Prompt Injection Against Custom AI Applications
Custom AI applications, RAG systems and internal chatbots can be manipulated through direct or indirect prompt injection. Required controls include runtime inspection, RAG security validation, guardrails and output filtering.

### AI-R06 — AI Output Leakage and Oversharing
AI responses may aggregate or expose information beyond the intended context due to permission hygiene, weak retrieval controls or prompt manipulation. Required controls include output inspection, source-document logging and permission-aware response governance.

### AI-R07 — AI Agent and Tool-Calling Abuse
Agents can call tools, APIs and workflows. Risks include excessive privilege, unauthorized action, tool misuse, MCP compromise and insufficient traceability. Required controls include identity, least privilege, approvals, tool governance and action logging.

### AI-R08 — AI Supply Chain and Model Integrity Risk
AI applications rely on models, libraries, datasets, plugins, extensions and MCP servers. Required controls include AI asset inventory, model inventory, AI BOM, model scanning, plugin governance and vulnerability integration.

### AI-R09 — Lack of AI Auditability and Forensic Visibility
Investigations are weak if prompts, responses, uploads, retrieved documents, model calls, tool invocations and agent decisions cannot be reconstructed. Required controls include policy-based logging, audit export, SIEM integration and retention controls.

### AI-R10 — Data Sovereignty and Third-Party Processing Risk
AI platforms may process or retain prompts, uploads, metadata and logs in external locations. Required controls include data residency validation, training exclusion, retention configuration, administrative access logging and deployment model assessment.
