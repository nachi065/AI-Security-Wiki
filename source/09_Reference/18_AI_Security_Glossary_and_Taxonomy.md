---
title: "AI Security Glossary and Taxonomy"
author: Nachiket Sathaye
parent: "Reference"
nav_order: 1
document_type: AI Security Wiki Reference
version: 1.0
---

# AI Security Glossary and Taxonomy

> **Purpose:** Provide common terminology for AI security governance, engineering, red teaming, assurance, vendor evaluation and audit.

> **Audience:** All wiki users.

| Term | Definition |
|---|---|
| AI Usage Governance | Controls that discover, monitor and govern how users interact with AI tools. |
| AI Data Protection | Controls that detect and prevent leakage of sensitive data through AI interactions. |
| AI Runtime Security | Controls that protect AI applications during operation. |
| AI-SPM | AI Security Posture Management; inventory, assess and govern AI assets and configurations. |
| AI Supply Chain Security | Protection of models, datasets, libraries, plugins, MCP servers and AI dependencies. |
| Agentic AI Security | Governance of AI agents that can use tools, APIs or workflows. |
| Prompt Injection | Attack that manipulates model instructions or application behavior through crafted input. |
| Indirect Prompt Injection | Prompt injection delivered through external or retrieved content. |
| RAG Security | Security of retrieval-augmented generation systems and their data sources. |
| Shadow AI | Use of AI tools without approval, governance or security visibility. |
| MCP | Model Context Protocol; an emerging mechanism for connecting AI systems to tools and data sources. |
| Tool Calling | AI system invocation of tools, APIs, commands, workflows or plugins. |
| AI Output Leakage | Sensitive information exposed through generated AI responses. |
| AI Red Teaming | Adversarial testing of AI systems to validate resilience and controls. |
| AI Security | The broader discipline of managing security risks associated with AI systems and AI use; the umbrella over security of AI and AI for security. |
| Security of AI | Protection of AI systems and their lifecycle from malicious or accidental compromise. |
| AI for Security | Use of AI to perform or augment defensive security functions. |
| Adversarial Machine Learning | Study and mitigation of attacks that exploit machine-learning behaviour. |
| Data Poisoning / Model Poisoning | Malicious manipulation of training data or model artifacts. |
| Excessive Agency | Unnecessary functionality, permissions or autonomy that enables harmful actions (OWASP LLM06). |
| Policy Enforcement Point | A deterministic component that authorizes or denies an action independently of the model. |
| Provenance | The origin and transformation history of an artifact or data item. |
| Robustness | Resilience under relevant perturbations and unexpected conditions. |
| Evaluation | Systematic measurement against defined criteria. |
| Model Drift | Changes in behaviour or performance over time, including those caused by data, model, configuration or environment. |
| LLM | Large Language Model; a model designed to process and generate language. |
| SLM | Small Language Model; a smaller model optimized for constrained or specialized use cases. |
| RAG | Retrieval-Augmented Generation; a pattern where the AI system retrieves external content to support responses. |
| Vector Database | A system used to store and retrieve embeddings or semantic representations. |
| Agent | AI system capable of planning or acting through tools, APIs or workflows. |
| Guardrails | Controls that constrain or monitor AI inputs, outputs and behavior. |
| AI BOM | AI Bill of Materials; inventory of models, datasets, libraries, plugins and dependencies. |
| Model Registry | Repository for tracking models, versions, metadata and governance status. |
| AI Assurance | Evidence-based validation that AI systems operate securely, reliably and according to policy. |

The distinction between AI security, security of AI and AI for security is explained in [Terminology and the Two-Axis Model](../00_Foundations/01-Terminology-and-Two-Axis-Model.md).

## Usage Guidance

Use this glossary to standardize language in risk reviews, control descriptions, architecture documents, vendor questionnaires and audit evidence.
