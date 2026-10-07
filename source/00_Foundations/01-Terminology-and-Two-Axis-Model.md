---
title: "1. Terminology and the Two-Axis Model"
description: "Security of AI, AI for security and AI security defined, with a two-axis object and mission model for placing any AI security question."
author: Nachiket Sathaye
parent: "Foundations"
nav_order: 1
document_type: Practitioner Research Paper
---

# 1. Terminology and the Two-Axis Model

## 1.1 The problem

Adoption of machine learning, foundation models and agents has turned AI from an isolated analytical tool into a general-purpose layer inside business systems. Security teams are now asked "are we secure with AI?" and the question hides at least four different ones:

- Can an attacker manipulate, steal, poison or disrupt our AI system?
- Can our AI-enabled business process cause or amplify a security failure, even if the model is behaving as designed?
- Can AI make attackers faster or cheaper against our conventional defences?
- Can AI make our defenders better, and what new risk does that introduce?

Using one phrase for all four leads to category errors. A hardened model does not make the surrounding business process safe. An AI-powered SOC product is not secure just because it improves analyst throughput. A vendor that sells "AI security" may be selling only one of the four.

## 1.2 Three meanings

| Term | Primary object of protection | Core question | Example controls |
|---|---|---|---|
| **Security of AI** | Models, data, pipelines, endpoints, prompts, agents, AI infrastructure | Can the AI system be manipulated, stolen, poisoned or disrupted? | Provenance, access control, adversarial testing, isolation |
| **AI for security** | Security operations (AI is the tool) | Can AI improve detection and response without creating new risk? | Human oversight, bounded autonomy, validation, audit logging |
| **AI security** (umbrella) | The AI-enabled enterprise and its ecosystem | Can AI create unacceptable security risk, amplify attacks, or improve our posture? | Governance, risk management, architecture, monitoring |

**Working definitions used in this paper**

- **Security of AI:** the protection of AI systems and their supporting lifecycle from malicious or accidental compromise.
- **AI security:** the coordinated management of confidentiality, integrity, availability, authenticity, robustness, privacy, controllability, safety and accountability risks arising from the design, development, deployment, operation and retirement of AI systems, and from the use or misuse of AI within the enterprise.

The terminology is a convention for this paper, not an industry standard. NIST's adversarial machine learning taxonomy, for example, is organised by attack class and lifecycle stage rather than by this vocabulary [1].

### A note on "safety"

Safety (preventing harmful outputs or behaviour regardless of an attacker) and security (resisting an adversary) overlap but are not the same. A model can refuse every harmful request in a benchmark and still leak data through a poisoned retrieval index. The early AI-safety literature framed many failure modes as accidents rather than attacks [27]; the security view adds an intelligent adversary who adapts to the defence. [Analysis]

## 1.3 Security properties

AI systems still need confidentiality, integrity and availability. They add properties that CIA does not capture well:

| Property | What it means for an AI system |
|---|---|
| Robustness | Behaviour holds under adversarial or unexpected input |
| Provenance | Origin and transformation history of data, models and prompts is known |
| Behavioural consistency | Behaviour does not change unexpectedly across versions, prompts or context |
| Controllability | The system can be stopped, constrained or rolled back |
| Accountability | Actions can be attributed and explained to a defensible standard |

These extend the CIA triad; they do not replace it. A model can be available yet unsafe, confidential yet manipulable, or accurate on a benchmark yet fragile under distribution shift. [Analysis]

## 1.4 The two-axis model

**Axis 1: object of protection.** What is being protected?

1. The AI asset (model, dataset, prompt, embedding index, tool definition, agent identity)
2. The AI-enabled application (the product or service that embeds the model)
3. The enterprise process (the decision or workflow the application supports)
4. The external ecosystem (customers, regulators, society, suppliers)

**Axis 2: security mission.** What outcome is required?

1. Prevent compromise
2. Detect manipulation
3. Contain impact
4. Recover safely
5. Govern the risk
6. Leverage AI for defence

Placing a problem in a cell of this matrix tells you who owns it and what evidence is needed.

| Object ↓ / Mission → | Prevent | Detect | Contain | Recover | Govern | Leverage for defence |
|---|---|---|---|---|---|---|
| **AI asset** | Artifact signing, access control, dataset validation | Drift and integrity monitoring, extraction-pattern detection | Model/endpoint isolation, kill switch | Roll back to last known-good model, re-train from clean data | Inventory, ownership, risk classification | AI-assisted anomaly detection on model telemetry |
| **AI-enabled application** | Input/output handling, least-privilege tools | Injection and misuse detection, tool-call logging | Per-session privilege limits, rate limits | Re-deploy from signed build, rotate credentials | Secure-development policy, release gates | AI-assisted code review of the app |
| **Enterprise process** | Approval gates on high-impact actions, segregation of duties | Business-logic anomaly detection | Transaction caps, manual fallback | Reversal procedures, reconciliation | Risk acceptance, control attestation | Fraud analytics, triage automation |
| **External ecosystem** | Supplier due diligence, contractual security terms | Threat intelligence on provider incidents | Provider failover, data-sharing limits | Customer notification, regulator engagement | Regulatory mapping, disclosure | Collaborative threat sharing |

*Table: cells contain illustrative examples, not an exhaustive control set. [Analysis]*

### Worked example: an autonomous coding agent

A coding agent that reads tickets, edits repositories and opens pull requests touches every row:

- **AI asset:** the model version and system prompt must be protected from tampering.
- **Application:** the agent runtime must treat repository content and ticket text as untrusted input.
- **Enterprise process:** merged code reaches production, so approval and review gates matter.
- **Ecosystem:** third-party packages the agent proposes become part of the supply chain.

A programme that only "secures the model" would address the first row and leave three open.

## 1.5 Lifecycle lens

Failure can originate at any of eight lifecycle stages: use-case selection; data acquisition and preparation; model selection or development; training and tuning; integration and testing; deployment; operation and monitoring; retirement and disposal. Weaknesses introduced upstream are hard to compensate for downstream. A deployment team cannot fully offset poisoned training data or an untrusted model artifact after the fact.

A fourth dimension, **authority** (who or what can act: human, model, service account, tool, agent), is added throughout this paper because it determines blast radius. A model that can only produce text has one class of impact. A model connected to email, repositories, cloud APIs or payment workflows can turn an error or an injected instruction into a real-world action. [Analysis]
