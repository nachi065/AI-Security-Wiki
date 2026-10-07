---
title: "2. The AI System Boundary and Assets"
description: "What sits inside an AI system boundary, the trust boundaries to draw, the assets to protect and why the model is treated as an untrusted component."
author: Nachiket Sathaye
parent: "Foundations"
nav_order: 2
document_type: Practitioner Research Paper
---

# 2. The AI System Boundary and Assets

## 2.1 What is inside the boundary

An AI-enabled system is more than a model endpoint. Drawing the boundary too tightly around "the model" is the most common scoping error in AI security assessments. [Analysis]

| Component | Examples | Why it matters for security |
|---|---|---|
| Data | Training sets, fine-tuning data, evaluation corpora, retrieval documents, user inputs | Can be poisoned, leaked, or used to infer private information |
| Model artifacts | Weights, adapters, tokenizers, configuration, model cards | Can be tampered with, stolen, or swapped |
| Instructions | System prompts, templates, guardrail policies | Define behaviour; leakage and tampering both matter |
| Retrieval layer | Vector stores, indices, connectors | Introduces external content and access-control questions |
| Orchestration | Frameworks, agent loops, memory stores, routing | Holds state and decides which tools run |
| Tools and integrations | APIs, databases, email, code execution, MCP-style tool servers | Convert model output into actions |
| Identities and credentials | Service accounts, API keys, delegated tokens | Define what the system is able to do |
| Infrastructure | GPUs, containers, orchestration, cloud accounts | Conventional attack surface, with AI-specific value |
| Humans | Operators, reviewers, end users | Can be manipulated by or over-trust AI output |

## 2.2 The root design problem: data and instructions share a channel

In conventional software the control plane (code) and data plane (inputs) are separate. A language model receives instructions and data in the same token stream, and nothing in the model architecture enforces the distinction. This is why text embedded in a web page, document or email can influence behaviour. Indirect prompt injection was demonstrated against LLM-integrated applications, including Bing Chat and GitHub Copilot, by Greshake et al. [23]. The earlier "ignore previous prompt" work by Perez and Ribeiro established goal hijacking and prompt leaking as attack classes against language models [22].

The practical consequence, and the central design principle of this paper, is:

> **Treat the model as an untrusted computational component. Its output may be useful but is never authoritative. Authority to access data, call tools or change state must be enforced by deterministic controls outside the model.** [Analysis]

This is not a claim that models are malicious. It is a claim that their behaviour under adversarial input cannot currently be guaranteed, so assurance has to sit in components whose behaviour can be.

## 2.3 Trust boundaries

Key boundaries to draw explicitly on any architecture diagram:

1. **User ↔ application.** Users can be malicious, or can be a channel for someone else's instructions.
2. **Application ↔ model provider.** Data leaves your control; model behaviour can change on the provider's schedule.
3. **Model ↔ retrieved content.** Retrieved documents are untrusted input, even when they come from internal sources.
4. **Model ↔ tools.** The point at which text becomes action. This is the most important boundary to police.
5. **Agent ↔ agent.** Messages from another agent inherit no trust by default.
6. **Platform ↔ tenant.** Relevant in shared GPU and managed-AI environments.

## 2.4 Model versus application

Many "AI vulnerabilities" are application vulnerabilities in disguise: an LLM output rendered unescaped in a browser, a tool endpoint without authorisation checks, a secret placed in a system prompt. OWASP classifies these separately (for example *Improper Output Handling*, LLM05:2025) from model-level risks [11]. Practical implication: a large share of risk can be reduced with conventional application security, applied carefully to the new data flows. The remainder (model manipulation, extraction, poisoning) needs AI-specific methods. [Analysis]

## 2.5 What must be protected

| Asset | Confidentiality concern | Integrity concern | Availability concern |
|---|---|---|---|
| Model weights | Theft of proprietary model | Backdoored or swapped weights | Loss or corruption of the only copy |
| Training / fine-tuning data | Exposure of sensitive records | Poisoning | Dataset unavailable for retraining |
| Embeddings / vector index | Reconstruction of source content; cross-user leakage | Injected or altered documents | Index corruption |
| System prompts and policies | Disclosure of logic and embedded secrets (OWASP LLM07) | Tampering to disable guardrails | Misconfiguration breaking service |
| Tool definitions and permissions | Disclosure of internal API surface | Malicious or altered tool descriptions | Tool outage cascading to the agent |
| Agent identities and credentials | Credential exposure | Impersonation, privilege escalation | Credential revocation breaking workflows |
| Inference endpoint | Prompt and output leakage | Output manipulation | Resource exhaustion (OWASP LLM10) |

*[Analysis], structured using OWASP LLM Top 10 2025 categories [11].*

## 2.6 Control principles for this layer

- Inventory each AI asset, dependency and trust boundary before choosing controls.
- Define the security property being protected and the business consequence of its failure.
- Assume model output can be manipulated, incorrect or incomplete unless independently validated.
- Separate model reasoning from authority to execute sensitive actions.
- Record provenance, version, owner and change history for material AI components.
