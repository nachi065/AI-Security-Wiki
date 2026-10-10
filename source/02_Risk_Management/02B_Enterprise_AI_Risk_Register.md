---
title: "Enterprise AI Risk Register"
author: Nachiket Sathaye
parent: "Risk Management"
nav_order: 2
document_type: AI Security Wiki Reference
version: 1.1
---

# Enterprise AI Risk Register

> **Purpose:** Provide a sample enterprise AI risk register covering AI usage, development, applications, agents, auditability, sovereignty, cost, output reliability and resilience, as a starting template.

> **Audience:** Governance, cyber risk, security architecture, audit, AI product owners.

> **How to use:** Use this page as a template. Re-score each risk using the AI Risk Methodology for your own environment, and add owners, evidence and treatment status.

> **Scope of AI-R14 to AI-R28:** These fifteen entries were added in version 1.1 to make operational risks (bias, explainability, model change, drift, oversight, reputation) and agentic risks (memory poisoning, credential harvesting, plugin supply chain, tool chains, trust boundaries) first-class entries. The Example Priority column is not re-ranked across all 28 risks; re-rank it with the AI Risk Methodology. Each risk is cross-referenced to the FINOS AI Governance Framework in the [risk to control mapping](02D_AI_Risk_to_Control_Mapping.md).

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
| AI-R11 | AI Cost Abuse and Resource Exhaustion | Medium | High | High | 11 |
| AI-R12 | Unreliable or Harmful AI Output | Medium | High | High | 12 |
| AI-R13 | AI Service Disruption and Dependency Failure | Medium | High | Medium | 13 |
| AI-R14 | Biased or Discriminatory AI Outcomes | Medium | High | High | 14 |
| AI-R15 | Lack of Explainability and Decision Traceability | Medium | High | High | 15 |
| AI-R16 | Foundation Model Version Change and Non-Deterministic Behaviour | High | Medium | High | 16 |
| AI-R17 | Data Quality Degradation and Model Drift | Medium | High | High | 17 |
| AI-R18 | Model Overreach and Use Beyond Approved Purpose | Medium | High | High | 18 |
| AI-R19 | Insufficient or Ineffective Human Oversight | Medium | High | High | 19 |
| AI-R20 | Reputational Harm from AI Behaviour | Medium | High | Medium | 20 |
| AI-R21 | Agent Memory and State Persistence Poisoning | Medium | High | High | 21 |
| AI-R22 | Agent-Mediated Credential Discovery and Harvesting | Medium | Critical | High | 22 |
| AI-R23 | Skill, Plugin and MCP Server Supply Chain Compromise | Medium | Critical | High | 23 |
| AI-R24 | Tool Chain Manipulation and Injection | Medium | Critical | High | 24 |
| AI-R25 | Multi-Agent Trust Boundary Violation | Medium | High | High | 25 |
| AI-R26 | Reasoning Trace and Intermediate Output Exposure | Medium | Medium | Medium | 26 |
| AI-R27 | Intellectual Property and Copyright Infringement | Medium | High | High | 27 |
| AI-R28 | Regulatory Non-Compliance from Unsupervised AI Decisions | Medium | Critical | High | 28 |

## Risk Narratives

### AI-R01: Critical Infrastructure Information Exposure
Users may submit sensitive infrastructure, architecture, security, operational or business information into AI tools for summarization, translation, troubleshooting or code support. Required controls include prompt inspection, upload inspection, classification-aware policy enforcement, audit logging and SOC alerting.

### AI-R02: Shadow AI and Ungoverned AI Usage
Unapproved AI use may occur through public AI sites, browser extensions, IDE plugins, SaaS features, APIs or desktop AI applications. Required controls include AI discovery, tool classification, allow/monitor/warn/block policy, endpoint visibility and reporting.

### AI-R03: Sensitive Data Leakage Through Prompts and Uploads
AI interactions can contain confidential data, personal data, credentials, source code, logs and business documents. Required controls include sensitive data detection, redaction/masking/warning/blocking and evidence generation.

### AI-R04: IDE-Based Source Code and Credential Exposure
AI coding assistants can expose source code, API keys, internal URLs, infrastructure-as-code and application logic. Required controls include IDE visibility, secret detection, source code protection and developer governance.

### AI-R05: Prompt Injection Against Custom AI Applications
Custom AI applications, RAG systems and internal chatbots can be manipulated through direct or indirect prompt injection. Required controls include runtime inspection, RAG security validation, guardrails and output filtering.

### AI-R06: AI Output Leakage and Oversharing
AI responses may aggregate or expose information beyond the intended context due to permission hygiene, weak retrieval controls or prompt manipulation. Required controls include output inspection, source-document logging and permission-aware response governance.

### AI-R07: AI Agent and Tool-Calling Abuse
Agents can call tools, APIs and workflows. Risks include excessive privilege, unauthorized action, tool misuse, MCP compromise and insufficient traceability. Required controls include identity, least privilege, approvals, tool governance and action logging.

### AI-R08: AI Supply Chain and Model Integrity Risk
AI applications rely on models, libraries, datasets, plugins, extensions and MCP servers. Required controls include AI asset inventory, model inventory, AI BOM, model scanning, plugin governance and vulnerability integration.

### AI-R09: Lack of AI Auditability and Forensic Visibility
Investigations are weak if prompts, responses, uploads, retrieved documents, model calls, tool invocations and agent decisions cannot be reconstructed. Required controls include policy-based logging, audit export, SIEM integration and retention controls.

### AI-R10: Data Sovereignty and Third-Party Processing Risk
AI platforms may process or retain prompts, uploads, metadata and logs in external locations. Required controls include data residency validation, training exclusion, retention configuration, administrative access logging and deployment model assessment.

### AI-R11: AI Cost Abuse and Resource Exhaustion
AI usage is metered, so leaked keys, automated traffic against public endpoints, runaway agents and retry loops can exhaust budget or capacity within hours. Required controls include cost attribution, budgets and quotas with enforcement, rate limits, spend anomaly detection, key revocation and limits on agent loops.

### AI-R12: Unreliable or Harmful AI Output
AI systems can give confident wrong answers, invent sources, packages and links, drift outside their approved scope or produce harmful content, and people act on the result. Required controls include grounding in approved sources, citation verification, topic restriction, harmful content filtering and factuality evaluation.

### AI-R13: AI Service Disruption and Dependency Failure
Business processes come to depend on AI services, model providers and the security controls in front of them. Outages, provider changes, overload or a control that fails open can stop the process or silently remove protection. Required controls include defined fail modes, failover that keeps policy intact, fallback paths, tested backups, provider exit plans and detection of silent control failure.

### AI-R14: Biased or Discriminatory AI Outcomes
AI outputs or decisions can disadvantage people or groups because of skewed data, proxy variables or the way a prompt frames the task. Required controls include group-level fairness testing before release and in operation, review of proxy variables, documented thresholds and human review of adverse outcomes.

### AI-R15: Lack of Explainability and Decision Traceability
The basis for an AI-assisted decision may not be explainable to a customer, reviewer or regulator, and the decision may not be reconstructable later. Required controls include decision records that name the model version, prompt template and sources, explanation templates by audience and retention that matches the decision's life.

### AI-R16: Foundation Model Version Change and Non-Deterministic Behaviour
Providers update, replace or retire models, and the same input can give different outputs. Guardrails, prompts and safety evaluations that passed before can regress without any change on the customer side. Required controls include version pinning, tracking of provider notices, a regression suite on every change, tolerance limits for output variation and tested rollback.

### AI-R17: Data Quality Degradation and Model Drift
Source data, retrieval content or input patterns change over time, so output quality or safety falls without any code change. Required controls include quality baselines, freshness limits and named owners for each source, drift indicators with thresholds and a defined response when a threshold is crossed.

### AI-R18: Model Overreach and Use Beyond Approved Purpose
A system approved for a low-risk purpose may later be used for a higher-risk one, or its autonomy and data access may grow without a new assessment. Required controls include a purpose statement per use case, change triggers that force reassessment and monitoring of actual use against the approved purpose.

### AI-R19: Insufficient or Ineffective Human Oversight
A person may be nominally in the loop but unable or unwilling to review meaningfully, through automation bias, missing context, no authority to override or a volume that forces rubber-stamping. Required controls include oversight points set by risk tier, reviewer context, authority and training, and effectiveness measures such as override rates and sampled re-review.

### AI-R20: Reputational Harm from AI Behaviour
A public-facing or customer-facing AI system may say something offensive, misleading or off-brand, or make a commitment the organisation did not intend, and the output becomes public. Required controls include content filtering, topic restriction, adversarial testing before release and a public-incident response path.

### AI-R21: Agent Memory and State Persistence Poisoning
Malicious or wrong content written into an agent's long-term memory or saved state can influence later sessions or other users and survive restarts. Required controls include memory integrity checks, provenance for stored entries, purge and rollback procedures and isolation of memory between users.

### AI-R22: Agent-Mediated Credential Discovery and Harvesting
An agent with file, shell or environment access can find and use credentials it was never meant to hold, and an injected instruction can make it send them out. Required controls include keeping secrets out of agent-readable locations, short-lived scoped tokens issued at call time, canary credentials and separate identities for agents.

### AI-R23: Skill, Plugin and MCP Server Supply Chain Compromise
Agent skills, plugins and MCP servers run with the agent's authority, and a compromised or malicious one can act as the agent. This narrows AI-R08 to the agent extension surface. Required controls include an allowlist, review before approval, version pinning, integrity checks and removal procedures.

### AI-R24: Tool Chain Manipulation and Injection
An attacker can steer an agent through a sequence of individually permitted tool calls, or inject instructions through tool inputs and outputs, so the combined effect is one nobody authorised. Required controls include deterministic checks on call sequences, validation of tool inputs and outputs and runtime inspection.

### AI-R25: Multi-Agent Trust Boundary Violation
Agents that call or delegate to other agents can pass on instructions, data or authority across boundaries nobody intended, so one compromised agent affects the rest. Required controls include an agent trust map, identity for every agent, containment and isolation between agents and logging of inter-agent requests.

### AI-R26: Reasoning Trace and Intermediate Output Exposure
Reasoning steps, intermediate tool output and system instructions can expose sensitive data, internal logic or attack paths when they are shown to users or written to logs. Required controls include classifying these traces, deciding what is displayed and retained, and testing for leakage.

### AI-R27: Intellectual Property and Copyright Infringement
Staff may submit third-party copyrighted or licensed material to AI tools, and AI output or training data may infringe the rights of others or carry licence obligations into products and code. Required controls include a usage policy, review of vendor terms for output ownership and indemnity, provenance records for training data and scanning of released output where policy requires.

### AI-R28: Regulatory Non-Compliance from Unsupervised AI Decisions
A regulated process may use AI without the supervision, records or accountability the regulator expects of a human performing the same step. Required controls include an obligation register, impact assessment, decision records, human oversight appropriate to the tier and a named accountable owner.
