---
title: "AI Security Market and Technology Landscape"
author: Nachiket Sathaye
parent: "Strategy and Market"
nav_order: 2
document_type: AI Security Wiki Reference
version: 2.0 Expanded Rewrite
---

# AI Security Market and Technology Landscape

**Purpose:** Expanded wiki reference for AI security governance, engineering, assurance and vendor evaluation.

**Audience:** Security leadership, enterprise architecture, procurement, governance, AI security researchers, AI product developers, red teamers and audit teams.

## 1. Purpose and Scope

This document provides a structured reference for understanding the AI security market, AI security technology categories, AI threat landscape, control taxonomy, stakeholder model, reference architectures, maturity model and future trends. It is intended to act as the strategy and market-intelligence foundation for the broader AI Security Wiki.

> **Design Intent:** Use this document as a parent knowledge domain. Detailed risk, control, PoC, vendor and audit documents should link back to this market and taxonomy reference.

## 2. Enterprise AI Adoption Landscape

AI adoption is no longer limited to standalone chatbots. Enterprise usage increasingly includes browser-based AI platforms, AI coding assistants, embedded SaaS AI, enterprise copilots, AI APIs, RAG applications, custom AI applications, autonomous agents and AI-enabled business workflows. This expands the security boundary from traditional application and data protection controls to prompt flows, model interactions, retrieval pipelines, tool invocation, agent permissions and AI supply chain dependencies.

| Market Wave | Description | Security Focus |
|---|---|---|
| Wave 1 — AI Usage Governance | Monitor or block public AI websites and unapproved AI tools. | Shadow AI, acceptable-use enforcement, user visibility |
| Wave 2 — AI Data Protection | Inspect prompts, uploads and sensitive data movement into AI services. | Prompt leakage, document upload, source code and secrets exposure |
| Wave 3 — AI Application Security | Secure custom AI apps, RAG, AI APIs and enterprise copilots. | Prompt injection, authorization gaps, output leakage, weak retrieval security |
| Wave 4 — Agentic AI Security | Control agents that can invoke tools, APIs and workflows. | Tool abuse, excessive privilege, action traceability, human approval |
| Wave 5 — AI Assurance | Validate AI systems before and after deployment. | AI red teaming, jailbreak testing, guardrail validation, continuous assessment |
| Wave 6 — Autonomous Enterprise AI | Govern multi-agent and autonomous business processes. | Agent mesh governance, delegated authority, business process manipulation |

## 3. AI Security Technology Taxonomy

AI security should be organized into technology categories that map to practical control objectives. The purpose of the taxonomy is to stop vendor-driven discussions from becoming disconnected from risk, control and evidence requirements.

| Category | Representative Capabilities | Primary Stakeholders |
|---|---|---|
| AI Discovery and Usage Governance | AI service discovery, user activity monitoring, shadow AI reporting, risk classification | Security Engineering, GRC, SOC |
| AI Data Protection / AI DLP | Prompt inspection, file upload inspection, response inspection, sensitive data detection | DLP, Data Protection, Compliance |
| AI Runtime Security | Prompt injection detection, runtime input/output inspection, RAG controls, AI API protection | AppSec, AI Platform, DevSecOps |
| AI Security Posture Management | AI asset inventory, AI application inventory, model inventory, configuration/posture analysis | Governance, Architecture, Risk Owners |
| AI Supply Chain Security | Model provenance, dataset governance, dependency scanning, plugin and MCP risk | DevSecOps, AI Researchers, AI Engineering |
| Agentic AI Security | Agent identity, tool/API governance, action logging, approval workflow, MCP visibility | AI Platform, IAM, SOC, Security Architecture |
| AI Red Teaming and Assurance | Jailbreak testing, prompt injection validation, guardrail testing, scenario-based evaluation | Red Team, AppSec, Assurance, Audit |
| Responsible AI and Trust Governance | Transparency, accountability, human oversight, traceability, risk management and governance | GRC, Legal, Compliance, AI Governance |

## 4. AI Security Threat Taxonomy

The AI threat taxonomy below should be used by security architects, red teamers and AI developers as a common language for AI threat modeling. It complements the enterprise risk register and the domain-specific standards.

| Threat Category | Description | Affected Areas | Control Themes |
|---|---|---|---|
| Prompt Injection | Malicious instructions attempt to override system or developer intent. | Custom AI apps, RAG, agents | Runtime inspection, input validation, guardrails, red team testing |
| Indirect Prompt Injection | Malicious instructions are embedded in retrieved content or external data. | RAG, email/document summarization, web-browsing agents | Content sanitization, retrieval controls, source trust validation |
| Jailbreak | User attempts to bypass safety or policy restrictions. | Chatbots, copilots, AI APIs | Guardrails, behavior testing, abuse monitoring |
| Data Leakage | Sensitive data is submitted to or generated by AI systems. | Browser AI, IDE AI, RAG, agents | Prompt/file/output inspection, DLP, classification-aware controls |
| RAG Manipulation | Retrieved content causes unauthorized disclosure or response manipulation. | Enterprise knowledge assistants, vector databases | Retrieval authorization, source logging, RAG red teaming |
| Training/Data Poisoning | Training or retrieval data is manipulated to influence model behavior. | Model training, datasets, knowledge bases | Dataset governance, provenance, integrity checks |
| Model Theft / Extraction | Adversary attempts to steal or reconstruct model behavior or weights. | Hosted AI services, custom models | Access control, rate limiting, monitoring, model governance |
| AI Supply Chain Compromise | Models, plugins, libraries, datasets or MCP servers are compromised. | AI development lifecycle | AI BOM, dependency scanning, vendor review, model registry |
| Agent Tool Abuse | Agent invokes tools beyond intent or authorization. | Agentic AI workflows | Tool allowlist, least privilege, approvals, action logs |
| Autonomous Action Risk | AI system performs business action without adequate oversight. | Agentic workflows, enterprise automation | Human approval, kill switch, policy enforcement, auditability |

## 5. AI Security Control Taxonomy

AI security controls must be grouped into families so that governance, engineering and audit teams understand ownership and testability.

| Control Family | Control Examples | Primary Owners |
|---|---|---|
| Identity and Access | User identity, service identity, agent identity, RBAC, least privilege | IAM, Security Architecture |
| Data Protection | Prompt inspection, upload inspection, response inspection, classification-aware enforcement | DLP, Data Protection |
| Application and Runtime Security | Input validation, prompt injection detection, output filtering, AI API security, RAG controls | AppSec, AI Platform |
| Agent Governance | Tool governance, API permissions, approval workflows, action traceability | AI Platform, IAM, SOC |
| Supply Chain and Model Governance | Model registry, dataset provenance, dependency scanning, plugin/MCP governance | DevSecOps, AI Engineering |
| Monitoring and Auditability | Prompt/response logging, source-document logging, SIEM integration, evidence export | SOC, Audit |
| Sovereignty and Third-Party Risk | Residency, retention, model training exclusion, admin access logging, vendor assurance | GRC, Legal, Procurement |

## 6. AI Security Stakeholder Model

| Stakeholder | Core Responsibility |
|---|---|
| AI Product Team | Define AI use case, data sources, business process and implementation design. |
| Security Engineering | Implement AI security controls and validate technical coverage. |
| Application Security / DevSecOps | Review custom AI applications, RAG, AI APIs and AI-assisted development. |
| SOC | Monitor AI events, investigate alerts and maintain response playbooks. |
| GRC / Compliance | Maintain AI risk, policy, control mapping and audit readiness. |
| Data Protection / Privacy | Validate data classification, personal data use, residency and retention. |
| IAM | Define user, service and agent identities and access boundaries. |
| Procurement / Legal | Validate vendor commitments, contractual terms, security documentation and processing locations. |
| Audit | Test control design and operating effectiveness using evidence. |

## 7. AI Security Reference Architecture Patterns

### Employee Browser AI Usage

```text
User → Browser → AI Security Control Layer → Public/Enterprise AI Service
```

Control focus: AI service discovery, prompt inspection, upload protection, policy enforcement and audit logging.

### AI Coding Assistant

```text
Developer → IDE → AI Security Control Layer → AI Coding Assistant / Code Model
```

Control focus: IDE visibility, source code protection, secret detection, developer attribution and DevSecOps integration.

### Custom RAG Application

```text
User → AI Application → Runtime Security Layer → Vector Database → Knowledge Sources
```

Control focus: prompt injection defense, retrieval authorization, source logging, output controls and API security.

### Agentic AI Workflow

```text
User / Trigger → AI Agent → Tool Governance Layer → Enterprise APIs / Workflows
```

Control focus: agent identity, tool allowlist, approval workflow, action logging, least privilege and kill switch.

### AI Supply Chain

```text
Developer → Model/Library/Dataset/Plugin Registry → CI/CD → AI Runtime
```

Control focus: model provenance, dependency review, AI BOM, scanning and release governance.

## 8. AI Security Maturity Model

| Maturity Level | Characteristics | Target Outcome |
|---|---|---|
| Level 1 — Ad Hoc | No consistent AI inventory, policy, monitoring or security review. | Unknown AI usage and unmanaged risk. |
| Level 2 — Discovered | Basic visibility into AI tools and usage patterns. | AI inventory and initial usage reporting. |
| Level 3 — Governed | Policies, intake process, DLP alignment and vendor review are established. | Controlled adoption and risk-based governance. |
| Level 4 — Protected | Runtime controls, IDE controls, RAG controls and agent governance are implemented. | Technical risk reduction and production readiness. |
| Level 5 — Optimized | Continuous monitoring, AI assurance, red teaming, metrics, audit automation and improvement. | Evidence-driven AI security program. |

## 9. AI Security Operating Model

The operating model should connect AI intake, architecture review, risk assessment, control implementation, testing, monitoring, exception handling and recurring governance reporting.

| Process Step | Description | Evidence |
|---|---|---|
| AI Intake | Business owner submits AI use case, data scope and vendor/platform details. | Intake form, data classification, use case description |
| Risk and Control Mapping | Security and GRC map use case to AI risks and controls. | Risk register entry, control mapping |
| Architecture and Data Review | Architecture, DLP, IAM, AppSec and privacy teams review technical design. | Architecture diagram, data flow, access model |
| Testing and Assurance | Run PoC, red team and audit evidence tests based on scope. | Test results, screenshots, logs |
| Approval / Conditional Approval | Approve, reject or approve with conditions. | Decision record, residual risk, exception log |
| Operational Monitoring | SOC and control owners monitor AI usage and alerts. | SIEM events, dashboards, incident records |
| Periodic Review | Review controls, vendors, exceptions and maturity metrics. | Review minutes, updated risk status |

## 10. AI Security and Governance Framework Mapping

The following frameworks should be used as references when designing the AI security program. They are not substitutes for local policy, technical architecture review or vendor due diligence.

| Framework | Primary Use in AI Security Program | Best-Fit Audience |
|---|---|---|
| NIST AI RMF | AI risk governance and risk management structure; includes Govern, Map, Measure and Manage concepts. | GRC, security leadership, AI governance |
| NIST Generative AI Profile | Generative AI risk management guidance aligned to AI RMF. | GenAI governance and AI risk teams |
| OWASP GenAI / LLM Top 10 | Application-focused risks for LLM and generative AI applications. | Developers, AppSec, red teams |
| MITRE ATLAS | Adversary tactics and techniques against AI-enabled systems. | Threat modeling, SOC, red team |
| ISO/IEC 42001 | AI Management System requirements for organizations developing, providing or using AI systems. | Governance, compliance, audit readiness |
| ISO/IEC 23894 | AI risk management guidance. | GRC and risk teams |
| EU AI Act | Risk-based regulatory model relevant for governance awareness. | Legal, compliance, vendor risk |
| UAE / Local Governance Requirements | Local privacy, data residency, critical infrastructure and sector requirements should be mapped separately. | GRC, legal, enterprise architecture |

## 11. AI Security Vendor Category Model

| Vendor Category | Purpose | Example Vendors / Platforms |
|---|---|---|
| AI Governance / Shadow AI | Discover and govern user AI usage. | Prompt Security, Lasso, Cyberhaven, Nightfall |
| AI Data Protection / AI DLP | Prevent sensitive data leakage through prompts, uploads and outputs. | Cyberhaven, Nightfall, Prompt Security |
| AI Runtime Security | Protect custom AI applications and AI APIs. | Prisma AIRS, HiddenLayer, Enkrypt AI |
| AI-SPM / AI Asset Governance | Inventory AI assets, agents, models and configurations. | Lasso, Prisma AIRS |
| Model and Supply Chain Security | Protect models, datasets, plugins and AI dependencies. | HiddenLayer, Prisma AIRS |
| AI Red Teaming and Assurance | Test AI systems, prompts, guardrails and jailbreak resilience. | Enkrypt AI and AI assurance platforms |
| Sovereign AI Governance | Support AI governance, sovereign architecture and strategic compliance. | Sovereign AI Security Labs and governance-focused providers |

## 12. Future AI Security Trends

| Trend | Why It Matters |
|---|---|
| MCP Security | Tool and data-source connectivity introduces new governance and attack-surface considerations. |
| Agent Identity | AI agents will require unique identity, access governance and accountability. |
| Agent Mesh and Multi-Agent Governance | Multiple collaborating agents will require relationship mapping, trust boundaries and action controls. |
| AI Assurance Platforms | Continuous AI testing, red teaming and guardrail validation will become part of production readiness. |
| Sovereign AI | Data residency, model governance and local control will become increasingly important for critical infrastructure. |
| AI Security Telemetry | SOC teams will need AI-specific logs: prompt, response, model, tool, data source and action context. |
| AI Supply Chain Controls | AI BOM, model provenance, dataset integrity and plugin governance will mature. |
| Policy-as-Code for AI | AI governance policies will increasingly be translated into technical controls and automated checks. |

## 13. Expanded AI Security Glossary

| Term | Meaning |
|---|---|
| LLM | Large Language Model; a model designed to process and generate language. |
| SLM | Small Language Model; a smaller model optimized for constrained or specialized use cases. |
| RAG | Retrieval-Augmented Generation; a pattern where the AI system retrieves external content to support responses. |
| Vector Database | A system used to store and retrieve embeddings or semantic representations. |
| Prompt Injection | A malicious instruction intended to manipulate the model or application behavior. |
| Indirect Prompt Injection | Prompt injection delivered through retrieved or external content. |
| Guardrails | Controls that constrain or monitor AI inputs, outputs and behavior. |
| AI BOM | AI Bill of Materials; inventory of models, datasets, libraries, plugins and dependencies. |
| Model Registry | Repository for tracking models, versions, metadata and governance status. |
| Agent | AI system capable of planning or acting through tools, APIs or workflows. |
| MCP | Model Context Protocol; protocol-like approach for connecting AI systems to tools and context sources. |
| Tool Calling | AI system invocation of tools, plugins, commands, APIs or workflows. |
| AI-SPM | AI Security Posture Management; discovery and governance of AI assets, configurations and risks. |
| AI Red Teaming | Adversarial testing to discover weaknesses in AI systems, prompts, guardrails and agents. |
| AI Assurance | Evidence-based validation that AI systems operate securely, reliably and according to policy. |

## 14. Strategic Guidance for the AI Security Wiki

- Keep this document as the parent strategy and taxonomy reference for the AI Security Wiki.

- Use risk and control documents as the operational source of truth for implementation and audit.

- Keep vendor profiles separate from control requirements to avoid vendor-first governance.

- Treat agentic AI, AI runtime security, AI supply chain security and AI assurance as emerging but high-priority domains.

- Use the maturity model to track progress from AI discovery to optimized continuous AI governance.

## 15. References Used for This Rewrite

| Source | URL | Use |
|---|---|---|
| Original Wiki File | 01_AI_Security_Market_and_Technology_Landscape.md | Internal generated wiki document provided by user. |
| NIST AI RMF | https://www.nist.gov/itl/ai-risk-management-framework | NIST describes AI RMF as voluntary guidance to manage AI risks and notes the Generative AI Profile and Critical Infrastructure profile concept note. |
| OWASP GenAI / LLM Top 10 | https://owasp.org/www-project-top-10-for-large-language-model-applications/ | OWASP describes its GenAI Security Project and LLM Top 10 as guidance for securing generative AI systems. |
| MITRE ATLAS | https://atlas.mitre.org/ | MITRE describes ATLAS as a living knowledge base of adversary tactics and techniques against AI-enabled systems. |
| ISO/IEC 42001 | https://www.iso.org/standard/42001 | ISO describes ISO/IEC 42001 as an AI management system standard for establishing, implementing, maintaining and improving an AIMS. |
