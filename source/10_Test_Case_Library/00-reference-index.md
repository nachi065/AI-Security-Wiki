---
title: "Reference Index"
parent: "Test Case Library"
nav_order: 1
---

# Reference Index

17-layer AI lifecycle model | 7 use-case domains | 470 test cases in 6 batches

*Status: draft for review. Case counts, domain assignments and mappings are proposals until approved.*

[Back to library overview](index.md)

## 1. Purpose and scope

This index is the master reference for the test case library. It organises the library by the 17 layers of the AI lifecycle (primary axis) and tags each test case with one or more buyer-facing use-case domains (secondary axis). The layer files contain the full test cases; this index controls numbering, counts, field definitions and coverage.

**Safety boundary:** all test cases use synthetic, non-functional or clearly marked test data only. No real customer, employee, financial, health or credential data is to be used or substituted during execution.

## 2. Numbering convention

Test case IDs take the form `TC-L##-###` where `L##` is the lifecycle layer and `###` is the sequence within that layer, for example `TC-L08-014`. IDs are unique across the library and stable once issued, so they can be referenced from a test case execution register, a PoC results tracker and a vendor comparison matrix.

Each case carries a **Legacy ID** field. Where a case supersedes an item from an earlier Domain A and B library (`TC-A-###`, `TC-B-###`) the old ID is recorded so existing references remain traceable. Mapping of the remaining legacy domains (C to O) has not been done.

## 3. Layer index

| Layer | Name | Primary test focus | Cases | Batch |
|---|---|---|---|---|
| L01 | [Business & Use Cases](L01-business-and-use-cases.md) | use-case registry, risk-tiering, business-owner attribution | 20 | 6 |
| L02 | [Governance & Risk Mgmt](L02-governance-and-risk-mgmt.md) | policy-to-control mapping, risk register, exceptions workflow | 25 | 6 |
| L03 | [Legal, Privacy & Compliance](L03-legal-privacy-and-compliance.md) | UAE/GCC residency, PDPL-type obligations, evidence export, DPIA support | 30 | 6 |
| L04 | [Human Interaction Layer](L04-human-interaction-layer.md) | browser/workforce AI, user coaching, approval prompts, multimodal input | 30 | 1 |
| L05 | [AI Applications](L05-ai-applications.md) | discovery, app-level runtime protection, output handling | 30 | 1 |
| L06 | [Agent Orchestration Layer](L06-agent-orchestration-layer.md) | agent and MCP discovery, tool governance, delegation chains, kill switch | 35 | 3 |
| L07 | [Prompt & Context Layer](L07-prompt-and-context-layer.md) | prompt injection (direct/indirect), jailbreak, context and memory poisoning | 40 | 2 |
| L08 | [AI Gateway & Security Controls](L08-ai-gateway-and-security-controls.md) | inline policy, DLP, guardrails, bypass resistance, latency | 40 | 1 |
| L09 | [Identity & Access Mgmt](L09-identity-and-access-mgmt.md) | user and agent (non-human) identity, scoped tokens, RBAC | 25 | 3 |
| L10 | [Data Layer](L10-data-layer.md) | sensitive-data classification, DLP, lineage, tenant isolation | 30 | 2 |
| L11 | [Knowledge & Retrieval Layer](L11-knowledge-and-retrieval-layer.md) | RAG poisoning, vector-store access control, retrieval leakage | 25 | 4 |
| L12 | [Model Layer](L12-model-layer.md) | model theft, extraction, adversarial inputs, model scanning | 25 | 4 |
| L13 | [Training & Fine-Tuning Layer](L13-training-and-fine-tuning-layer.md) | data poisoning, dataset provenance, fine-tune integrity | 20 | 4 |
| L14 | [MLOps / LLMOps Layer](L14-mlops-llmops-layer.md) | pipeline and registry security, CI/CD gates, artifact signing | 20 | 4 |
| L15 | [Infrastructure Layer](L15-infrastructure-layer.md) | GPU/cluster hardening, secrets, network segmentation, sovereignty of control plane | 20 | 5 |
| L16 | [Supply Chain & Third Party](L16-supply-chain-and-third-party.md) | AI-BOM, model and package provenance, third-party SaaS AI risk | 25 | 4 |
| L17 | [Monitoring, Detection & Response](L17-monitoring-detection-and-response.md) | telemetry, SIEM/SOAR integration, AI incident response, forensics | 30 | 5 |
| | **Total** | | **470** | |

## 4. Batch plan

| Batch | Layers | Theme | Cases |
|---|---|---|---|
| 1 | L04, L05, L08 | Workforce, app and gateway | 100 |
| 2 | L07, L10 | Injection, jailbreak and data | 70 |
| 3 | L06, L09 | Agents, MCP and identity | 60 |
| 4 | L11, L12, L13, L14, L16 | Model, data and supply chain | 115 |
| 5 | L15, L17 | Infrastructure and SOC | 50 |
| 6 | L01, L02, L03 | Governance, legal and UAE | 75 |

Layers L01 to L03 were written last because their cases depend on the control and evidence terminology settled in the technical layers.

## 5. Use-case domain tags

| Tag | Use-case domain |
|---|---|
| D1 | Workforce / Browser AI Governance |
| D2 | Developer / IDE AI Security |
| D3 | Custom AI Application Runtime Security |
| D4 | Model Security / AI Supply Chain |
| D5 | Agentic AI / MCP / Tool Governance |
| D6 | Data Protection / DLP / Investigation |
| D7 | Sovereignty / Compliance / UAE Requirements |

### Candidate additional domains (pending approval, not in use)

- D8 AI Red Teaming and Continuous Testing
- D9 Agent and Non-Human Identity Governance
- D10 Browser and Computer-Use Agents
- D11 Multimodal and Voice Input Security
- D12 AI Incident Response and Forensics
- D13 AI Cost and Abuse Controls

These reflect areas that vendors increasingly sell. Their market relevance has not been independently verified. Cases touching these themes are tagged to the closest existing domain.

## 6. Layer-to-domain coverage matrix (draft)

● = primary home for the domain's cases; ○ = secondary coverage.

| Layer | D1 | D2 | D3 | D4 | D5 | D6 | D7 |
|---|---|---|---|---|---|---|---|
| L01 | ○ |  | ○ |  |  |  | ○ |
| L02 | ○ |  |  | ○ |  |  | ● |
| L03 |  |  |  |  |  | ○ | ● |
| L04 | ● |  |  |  |  | ○ |  |
| L05 |  | ○ | ● |  |  |  |  |
| L06 |  |  |  |  | ● |  |  |
| L07 |  |  | ● |  | ○ |  |  |
| L08 | ○ |  | ● |  |  | ● |  |
| L09 | ○ |  |  |  | ● |  |  |
| L10 |  |  |  |  |  | ● |  |
| L11 |  |  | ○ |  |  | ● |  |
| L12 |  |  |  | ● |  |  |  |
| L13 |  |  |  | ● |  |  |  |
| L14 |  | ○ |  | ● |  |  |  |
| L15 |  |  |  | ○ |  |  | ● |
| L16 |  | ○ |  | ● |  |  |  |
| L17 | ○ |  | ○ |  | ○ | ● | ○ |

D2 (Developer / IDE AI Security) has no primary layer, so its cases are cross-layer tags drawn from L05, L08, L14 and L16.

## 7. Field dictionary

| Field | Definition |
|---|---|
| **Lifecycle Layer** | L01 to L17, the primary classification. |
| **Use-Case Domain(s)** | One or more of D1 to D7 (and approved additions). |
| **Test Method** | Technical = executed live in the PoC lab. Evidence = verified by configuration, export, workflow or document inspection. Attestation = vendor written declaration, scored lower than demonstrated evidence. |
| **Vendor Applicability** | Architecture classes for which the case is meaningful: E = endpoint or browser agent, G = inline gateway, proxy or SASE, A = application SDK or API-level control, P = posture, API-integrated or AI-SPM, R = red-team or testing tool, W = governance, risk and compliance workflow capability (used mainly in Batch 6). Out-of-scope architecture is scored N/A, not 0. |
| **Legacy ID** | Superseded TC-A or TC-B reference, if any. |
| **Control Theme, Applicable Requirement, Framework Crosswalk (Batch 6 only)** | Batch 6 is framework-neutral. Each case carries a control theme, a blank Applicable Requirement field that the assessor completes before testing (framework, clause, requirement text and numeric parameters), and a blank crosswalk row for ISO/IEC 27001 ISMS, DPDP, NESA, PDPL and other frameworks. No clause numbers or legal deadlines are asserted in the library. |
| **Risk Addressed / Business Scenario / Technical Scenario** | Why the case matters, what the stakeholder needs, and how the test is staged. The earlier Objective field restated the title and has been folded into Business Scenario. |
| **Preconditions / Test Data / Procedure** | Environment, synthetic inputs and numbered steps. Preconditions combine a layer-level baseline with any case-specific setup. |
| **Edge Cases / Variants (optional)** | Additional conditions to run if time allows, or to probe a vendor claim further. Present only where a case has meaningful variants. |
| **Expected Detection / Prevention / Alert-Log / Dashboard / Integration** | What the platform must detect, enforce, record, display and hand to other tools. |
| **Forensic Evidence / Compliance Evidence** | Artefacts for incident reconstruction and audit. |
| **MITRE ATLAS / OWASP LLM / NIST AI RMF** | Reference mappings, varied by case type. All identifiers must be verified against the current published versions before use in an RFP. A mapping of N/A means no direct technique applies. |
| **Risk Severity** | Critical, High, Medium or Low, used for weighted scoring. |
| **Scoring Criteria** | 0 = not demonstrated; 3 = partially met or evidence incomplete; 5 = fully met with complete evidence; N/A = architecture out of scope. |
| **Pass / Fail Criteria** | Pass requires Expected Detection (and Prevention where stated) within SLA with evidence captured from the live PoC. Fail is any miss, SLA breach, missing attribution or reliance on vendor demo data. |

## 8. Known limitations

- Reference identifiers (MITRE ATLAS, OWASP LLM, NIST AI RMF) come from working knowledge and must be checked against current releases before use in an RFP.
- Pass thresholds such as detection percentages, counts and times are starting values, to be tuned to your risk appetite and vendor SLAs.
- Legacy IDs for earlier Domains C to O are not mapped.
- Depth is uneven: some cases (notably in L04, L05, L12 and L14) are lighter than others and benefit from further detail.
- The governance and legal layers (L01 to L03) are framework-neutral. See the [Framework Adoption Guide](framework-adoption-guide.md).
