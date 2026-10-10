---
title: "7. Reference Architecture"
description: "Reference architecture for secure AI systems: layered trust boundaries, model gateway, policy enforcement point, tool gateway and telemetry."
author: Nachiket Sathaye
parent: "Foundations"
nav_order: 7
document_type: Practitioner Research Paper
---

# 7. Reference Architecture

## 7.1 Principles

1. **Layered trust boundaries.** Users interact with an application or orchestration layer; the orchestration layer mediates access to models and tools; models operate as untrusted reasoning components; data services enforce authorisation independently; sensitive actions pass through deterministic policy enforcement.
2. **Model-agnostic control plane.** Security policy should not depend on a specific model's behaviour. Models should be replaceable without redesigning the control layer, which also reduces lock-in.
3. **Zero trust applied to AI components.** No model, tool, retrieval source or agent is trusted merely because it sits inside the AI platform. Authenticate, authorise and evaluate every request in context. Minimise standing privilege; prevent a compromised prompt or model output from becoming an administrative command directly.
4. **Telemetry by design.** Capture identity, model version, prompt and retrieval provenance (where legally and operationally appropriate), tool invocations, policy decisions, outputs and downstream effects.

## 7.2 Layers

<img class="figure" src="images/secure-agentic-ai-system-architecture.jpg" width="1220" height="724" alt="Secure agentic AI system architecture. Users and upstream systems reach an application gateway, then the orchestration and agent runtime. The runtime calls model management (model gateway and model runtime), retrieval and data services, and a policy enforcement point. A policy decision point in the authorization control plane sets the rules for the enforcement point, and governance (inventory, risk and policy) sets the policy for the decision point. Authorized actions pass through the tool and agent gateway to enterprise systems and APIs. Orchestration, the model gateway, the policy enforcement point and the tool gateway send security telemetry to detection and response. An evaluation and red-team platform tests the orchestration layer.">

| Layer | Responsibility |
|---|---|
| Identity and access | Human and non-human identities; delegation; credential issuance |
| Application gateway | Authentication, rate limiting, input handling, abuse controls |
| Prompt and context management | Assemble system prompt, user input and retrieved content; label provenance |
| Model gateway | Route to approved models; redact sensitive data; log requests; enforce version pinning |
| Model runtime | Hosted API or self-managed inference, hardened and isolated |
| Retrieval and data services | Enforce entitlements on every query; record provenance |
| Tool and agent gateway | Expose only allow-listed, schema-validated tools with scoped credentials |
| Policy enforcement | Deterministic checks and approval workflow for sensitive actions |
| Policy decision | Evaluate each request against the policy that governance sets, return an allow, deny or approval-required decision to the enforcement point, and log the decision |
| Security telemetry | Structured logs feeding detection and audit |
| Evaluation and red-team platform | Pre-release and continuous testing against defined threat cases |
| Incident response | AI-specific playbooks, containment levers, forensics |
| Governance | Inventory, ownership, risk acceptance, evidence |

*[Analysis]. The layered pattern combines widely used enterprise practice; it is not a standard.*

## 7.3 Segmentation and isolation

- Separate environments for experimentation, training, evaluation and production, with controlled data flow between them.
- Isolate model runtimes from sensitive systems at the network level; allow only required egress.
- Run code-executing tools in sandboxes with no default network or secrets access.
- For multi-tenant systems, enforce tenant boundaries in the retrieval layer, memory and logs, not only at the UI.

## 7.4 Design checks

Before approving an architecture, ask:

- If the model produced the worst possible output at this step, what is the maximum damage?
- Which component enforces authorisation, and does it know who the *end user* is?
- What can the model reach that the user could not reach directly?
- Can we reconstruct, from logs, exactly what the system did and why?
- How do we stop it, and how fast?
