---
title: "Test Case Library"
nav_order: 11
has_children: true
---

# AI Security Vendor Evaluation: Test Case Library

A lifecycle-based library of **487 test cases** for evaluating AI security products in a controlled proof of concept. Cases are organised by the **17 layers of the AI lifecycle** and tagged with seven buyer-facing use-case domains.

> **Status: draft for review.** Reference identifiers (MITRE ATLAS, OWASP LLM, NIST AI RMF) must be verified against current published versions, and numeric thresholds are starting values to tune to your risk appetite and vendor SLAs.

## Start here

- [Reference Index](00-reference-index.md): numbering, field definitions, applicability codes, domain tags, coverage matrix
- [Appendix: Lab Prerequisites](appendix-lab-prerequisites.md): the lab environment, tooling and fabricated data each layer needs
- [Framework Adoption Guide](framework-adoption-guide.md): how to use the governance and legal layers with ISO/IEC 27001, DPDP, NESA, PDPL or any other framework, plus a crosswalk template
- [AI Security PoC Test Case Library](../06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md): a 20-scenario quick-start set for a first PoC, mapped to the layers below

To find a specific case, type its ID (for example `TC-L08-014`) or a keyword into the search box at the top of any page. Each of the 487 cases is indexed individually.

## Layers

| Layer | Name | Primary test focus | Cases | Critical | High | Medium | Low |
|---|---|---|---|---|---|---|---|
| L01 | [Business & Use Cases](L01-business-and-use-cases.md) | use-case registry, risk-tiering, business-owner attribution | 20 | 6 | 8 | 5 | 1 |
| L02 | [Governance & Risk Mgmt](L02-governance-and-risk-mgmt.md) | policy-to-control mapping, risk register, exceptions workflow | 25 | 7 | 11 | 7 | 0 |
| L03 | [Legal, Privacy & Compliance](L03-legal-privacy-and-compliance.md) | UAE/GCC residency, PDPL-type obligations, evidence export, DPIA support | 30 | 11 | 16 | 3 | 0 |
| L04 | [Human Interaction Layer](L04-human-interaction-layer.md) | browser/workforce AI, user coaching, approval prompts, multimodal input | 32 | 6 | 16 | 10 | 0 |
| L05 | [AI Applications](L05-ai-applications.md) | discovery, app-level runtime protection, output handling | 35 | 8 | 19 | 8 | 0 |
| L06 | [Agent Orchestration Layer](L06-agent-orchestration-layer.md) | agent and MCP discovery, tool governance, delegation chains, kill switch | 37 | 17 | 17 | 3 | 0 |
| L07 | [Prompt & Context Layer](L07-prompt-and-context-layer.md) | prompt injection (direct/indirect), jailbreak, context and memory poisoning | 41 | 11 | 24 | 6 | 0 |
| L08 | [AI Gateway & Security Controls](L08-ai-gateway-and-security-controls.md) | inline policy, DLP, guardrails, bypass resistance, latency | 42 | 8 | 26 | 7 | 1 |
| L09 | [Identity & Access Mgmt](L09-identity-and-access-mgmt.md) | user and agent (non-human) identity, scoped tokens, RBAC | 26 | 9 | 14 | 3 | 0 |
| L10 | [Data Layer](L10-data-layer.md) | sensitive-data classification, DLP, lineage, tenant isolation | 30 | 9 | 14 | 7 | 0 |
| L11 | [Knowledge & Retrieval Layer](L11-knowledge-and-retrieval-layer.md) | RAG poisoning, vector-store access control, retrieval leakage | 25 | 6 | 10 | 9 | 0 |
| L12 | [Model Layer](L12-model-layer.md) | model theft, extraction, adversarial inputs, model scanning | 25 | 4 | 8 | 12 | 1 |
| L13 | [Training & Fine-Tuning Layer](L13-training-and-fine-tuning-layer.md) | data poisoning, dataset provenance, fine-tune integrity | 20 | 3 | 10 | 7 | 0 |
| L14 | [MLOps / LLMOps Layer](L14-mlops-llmops-layer.md) | pipeline and registry security, CI/CD gates, artifact signing | 22 | 4 | 12 | 6 | 0 |
| L15 | [Infrastructure Layer](L15-infrastructure-layer.md) | GPU/cluster hardening, secrets, network segmentation, sovereignty of control plane | 20 | 8 | 10 | 2 | 0 |
| L16 | [Supply Chain & Third Party](L16-supply-chain-and-third-party.md) | AI-BOM, model and package provenance, third-party SaaS AI risk | 26 | 4 | 13 | 9 | 0 |
| L17 | [Monitoring, Detection & Response](L17-monitoring-detection-and-response.md) | telemetry, SIEM/SOAR integration, AI incident response, forensics | 31 | 4 | 20 | 7 | 0 |
| | **Total** | | **487** | **125** | **248** | **111** | **3** |

## Coverage at a glance

Counts are taken from the case index of each layer.

| Test method | Cases | Meaning |
|---|---|---|
| Technical | 403 | Executed live in the PoC lab |
| Evidence | 72 | Verified by configuration, export, workflow or document inspection |
| Attestation | 12 | Vendor written declaration, scored lower than demonstrated evidence |

| Tag | Use-case domain | Cases tagged |
|---|---|---|
| D1 | Workforce / Browser AI Governance | 54 |
| D2 | Developer / IDE AI Security | 29 |
| D3 | Custom AI Application Runtime Security | 179 |
| D4 | Model Security / AI Supply Chain | 104 |
| D5 | Agentic AI / MCP / Tool Governance | 78 |
| D6 | Data Protection / DLP / Investigation | 102 |
| D7 | Sovereignty / Compliance / UAE Requirements | 143 |

A case can carry more than one domain tag, so the domain counts add up to more than 487. D2 covers the developer workflow end to end: IDE prompts, assistant extensions, coding agents, MCP configuration, repository policy, pipeline bots and SOC telemetry, with L05 as its primary layer.

## Coming next

> **Note:** Additional test cases are being written for the following domains. Until they are published, cases that touch these themes are tagged to the closest existing domain (D1 to D7).

- **Agent and non-human identity governance**, as a separate buyer concern from MCP tool governance.
- **Browser and computer-use agents**, which act on a user's behalf in web sessions. They are a different risk from a chat tab.
- **Multimodal and voice input**, covering images, documents and audio as injection and leakage channels.
- **AI incident response and forensics**, a lifecycle-wide need beyond L17 telemetry.
- **AI cost and abuse controls**, covering denial-of-wallet, quota abuse and runaway agents.

See the [Reference Index](00-reference-index.md) for the planned domain tags.

## Numbering and structure

Case IDs take the form `TC-L##-###`: the lifecycle layer and a sequence within it, for example `TC-L08-014`. IDs are unique across the library and stable once issued. Where a case is the detailed version of a quick-start scenario, the **Quick-Start Scenario** field links to it by ID, for example `AI-POC-ID-004`.

Each case records: lifecycle layer, use-case domains, test method (Technical, Evidence or Attestation), vendor applicability (E endpoint or browser agent, G inline gateway or proxy, A application or API-level control, P posture or AI-SPM, R red-team tool, W governance workflow), risk, scenarios, test data, numbered procedure, expected results, pass and fail criteria, scoring, evidence to capture, and reference mappings.

Layers L01 to L03 are framework-neutral. Their cases use an **Expected Result** field in place of Expected Detection, and add Control Theme, Applicable Requirement and Framework Crosswalk fields for the assessor to complete.

## Safety boundary

All test cases use synthetic, non-functional or clearly marked test data only. No real customer, employee, financial, health or credential data should be used or substituted during execution. Probe and simulation scripts are harmless lab tools. Never run them against production systems.

## How to use

1. Read the Reference Index and decide which layers and domains are in scope.
2. Build the lab prerequisites each layer calls for (mock providers, test cluster, lab SIEM, fabricated data).
3. Run each case, capture the evidence listed, and score 0, 3 or 5 (or N/A where the vendor architecture cannot perform the test by design).
4. For layers L01 to L03, complete the Applicable Requirement and Framework Crosswalk fields first.
