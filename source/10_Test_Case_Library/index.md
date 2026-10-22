---
title: "Test Case Library"
author: Nachiket Sathaye
description: "{{n:tests}} AI security test cases for vendor evaluation and PoC across {{n:layers}} AI lifecycle layers and 6 emerging domains: prompt injection, DLP, agents, MCP, RAG."
nav_order: 11
has_children: true
---

# AI Security Vendor Evaluation: Test Case Library

A library of **{{n:tests}} test cases** for evaluating AI security products in a controlled proof of concept: **{{n:layer_tests}} cases organised by the {{n:layers}} layers of the AI lifecycle**, tagged with seven buyer-facing use-case domains, and **{{n:domain_tests}} cases in six emerging domains** that cut across the layers.

> **Status: draft for review.** Reference identifiers (MITRE ATLAS, OWASP LLM, NIST AI RMF) must be verified against current published versions, and numeric thresholds are starting values to tune to your risk appetite and vendor SLAs.

## Start here

- [Reference Index](00-reference-index.md): numbering, field definitions, applicability codes, domain tags, coverage matrix
- [Standard Fields](standard-fields.md): the wording that cases share (scoring, pass and fail criteria, reviewer notes, standard evidence, per-layer setup). A case shows a field only when it differs; the shared wording that applies is listed, closed, at the end of each case, so a copied case keeps it
- [Appendix: Lab Prerequisites](appendix-lab-prerequisites.md): the lab environment, tooling and fabricated data each layer needs
- [Framework Adoption Guide](framework-adoption-guide.md): how to use the governance and legal layers with ISO/IEC 27001, DPDP, NESA, PDPL or any other framework, plus a crosswalk template
- [Test Your Own Application](test-your-own-app.md): the same testing written for an owner who can change the code, with no product or provider language, an adapter template and a plain procedure for each case in the payload kit
- [Payload Kit](payload-kit.md): attack sets, legitimate requests and a runner for {{n:kit_cases}} Critical cases, with a baseline-versus-protected comparison you can point at your own application
- [AI Security PoC Test Case Library](../06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md): a 20-scenario quick-start set for a first PoC, mapped to the layers below
- [Regulatory Crosswalk](../11_GCC_AI_Compliance/07_Regulatory_Crosswalk.md): UAE and other GCC instruments mapped to controls and to the control themes used in layers L01 to L03
- [EU Regulatory Crosswalk](../12_EU_AI_Compliance/07_Regulatory_Crosswalk.md): the AI Act, GDPR and related EU instruments mapped to controls and to the same control themes

Every case names the control it tests, by ID, from the [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md).

To find a specific case, type its ID (for example `TC-L08-014`) or a keyword into the search box at the top of any page. Each of the {{n:tests}} cases is indexed individually.

## Validation levels

A published case says what to test. It is not evidence that any product passes it, and the size of this library says nothing about how well it protects a real system. Every case therefore shows a **Validation Level** in its table, so a reader can see how far the case itself has been proven.

| Level | Meaning | Cases now |
|---|---|---|
| Documented | The scenario, procedure and expected result are written out. No run against a real product is recorded. | {{n:documented}} |
| Executable | A runnable payload set exists in the [Payload Kit](payload-kit.md) and has been run against the kit's stand-in applications. Those stand-ins are a few regular expressions, not a model, so the result shows the kit works, not that any product is protected. | {{n:executable}} |
| Lab-validated | The case has been run against a named application or product version in a lab, and the result and evidence are recorded in the case's **Validated Against** row. | {{n:lab_validated}} |
| Independently reproduced | A second tester, independent of the first, reproduced a lab-validated result on the same or a later version, with their own evidence. | {{n:reproduced}} |

The Cases now column is counted when the site is built. Until a case reaches Lab-validated, treat it as untested against any real system, including yours. A case that does not state a level is Documented, or Executable if the kit has a payload file for it; the build fills the level in.

**To record a run against a real system,** add two rows to the case's table, below Control(s) Tested:

```
| **Validation Level** | Lab-validated |
| **Validated Against** | <application or product> <version>, <YYYY-MM-DD>, <PASS, FAIL or INCONCLUSIVE>, [evidence](<link to the report or run log>) |
```

The link check rejects any other level, and rejects a Lab-validated or Independently reproduced case whose Validated Against row has no date or no evidence link. Record failures as well as passes: a FAIL against a named version is still a validated result. Manual checks (inventory, configuration, evidence and attestation cases) are validated the same way, with the inspection record as the evidence.

## Layers

| Layer | Name | Primary test focus | Cases | Critical | High | Medium | Low |
|---|---|---|---|---|---|---|---|
| L01 | [Business & Use Cases](L01-business-and-use-cases.md) | use-case registry, risk-tiering, business-owner attribution | 20 | 6 | 8 | 5 | 1 |
| L02 | [Governance & Risk Mgmt](L02-governance-and-risk-mgmt.md) | policy-to-control mapping, risk register, exceptions workflow | 25 | 7 | 11 | 7 | 0 |
| L03 | [Legal, Privacy & Compliance](L03-legal-privacy-and-compliance.md) | UAE/GCC residency, PDPL-type obligations, evidence export, DPIA support, fairness, transparency, human oversight, intellectual property and authority engagement | 45 | 12 | 25 | 8 | 0 |
| L04 | [Human Interaction Layer](L04-human-interaction-layer.md) | browser/workforce AI, user coaching, approval prompts, multimodal input | 32 | 6 | 16 | 10 | 0 |
| L05 | [AI Applications](L05-ai-applications.md) | discovery, app-level runtime protection, output handling | 35 | 8 | 19 | 8 | 0 |
| L06 | [Agent Orchestration Layer](L06-agent-orchestration-layer.md) | agent and MCP discovery, tool governance, access grant approval, delegation chains, agent-to-agent trust, kill switch | 47 | 19 | 25 | 3 | 0 |
| L07 | [Prompt & Context Layer](L07-prompt-and-context-layer.md) | prompt injection (direct/indirect), jailbreak, context and memory poisoning, memory governance | 45 | 11 | 27 | 7 | 0 |
| L08 | [AI Gateway & Security Controls](L08-ai-gateway-and-security-controls.md) | inline policy, DLP, guardrails, guardrail policy ownership, bypass resistance, latency | 43 | 8 | 26 | 8 | 1 |
| L09 | [Identity & Access Mgmt](L09-identity-and-access-mgmt.md) | user and agent (non-human) identity, scoped tokens, RBAC | 26 | 9 | 14 | 3 | 0 |
| L10 | [Data Layer](L10-data-layer.md) | sensitive-data classification, DLP, lineage, tenant isolation, data quality | 33 | 9 | 16 | 8 | 0 |
| L11 | [Knowledge & Retrieval Layer](L11-knowledge-and-retrieval-layer.md) | RAG poisoning, vector-store access control, retrieval leakage, embedding and index governance | 28 | 6 | 12 | 10 | 0 |
| L12 | [Model Layer](L12-model-layer.md) | model theft, extraction, adversarial inputs, model scanning, identity for model access, model approval, predictive model drift and privacy attacks | 34 | 7 | 13 | 13 | 1 |
| L13 | [Training & Fine-Tuning Layer](L13-training-and-fine-tuning-layer.md) | data poisoning, dataset provenance, fine-tune integrity, training job identity | 26 | 4 | 14 | 8 | 0 |
| L14 | [MLOps / LLMOps Layer](L14-mlops-llmops-layer.md) | pipeline and registry security, CI/CD gates, artifact signing | 22 | 4 | 12 | 6 | 0 |
| L15 | [Infrastructure Layer](L15-infrastructure-layer.md) | GPU/cluster hardening, secrets, network segmentation, sovereignty of control plane | 20 | 8 | 10 | 2 | 0 |
| L16 | [Supply Chain & Third Party](L16-supply-chain-and-third-party.md) | AI-BOM, model and package provenance, third-party SaaS AI risk | 26 | 4 | 13 | 9 | 0 |
| L17 | [Monitoring, Detection & Response](L17-monitoring-detection-and-response.md) | telemetry, SIEM/SOAR integration, AI incident response, forensics, tracing platforms, quality failures | 33 | 4 | 21 | 8 | 0 |
| | **Total** | | **{{n:layer_tests}}** | **132** | **282** | **123** | **3** |

## Emerging domains

Six further domains cut across the layers and use their own ID series, `TC-D##-###`. Each case records the lifecycle layers it touches and links to the layer cases it builds on. The layer case tests the platform control; the domain case tests the buyer concern from the domain's own point of view.

| Domain | Name | Focus | Cases | Critical | High | Medium | Low |
|---|---|---|---|---|---|---|---|
| D08 | [AI Red Teaming and Continuous Testing](D08-ai-red-teaming-and-continuous-testing.md) | ground-truth accuracy, coverage, judging, reproducibility, CI/CD, safe execution | 25 | 6 | 16 | 3 | 0 |
| D09 | [Agent and Non-Human Identity Governance](D09-agent-and-non-human-identity-governance.md) | registry, sponsors, recertification, drift, delegation, revocation | 20 | 3 | 13 | 4 | 0 |
| D10 | [Browser and Computer-Use Agents](D10-browser-and-computer-use-agents.md) | isolation, credentials, action policy, injection via web content, approvals, kill switch | 23 | 9 | 11 | 3 | 0 |
| D11 | [Multimodal and Voice Input Security](D11-multimodal-and-voice-input-security.md) | images, documents, audio and video as injection and leakage channels, voice authentication, recording governance | 22 | 5 | 14 | 3 | 0 |
| D12 | [AI Incident Response and Forensics](D12-ai-incident-response-and-forensics.md) | taxonomy, state preservation, replay, scoping, containment, provider coordination, evidence handling | 22 | 9 | 11 | 2 | 0 |
| D13 | [AI Cost and Abuse Controls](D13-ai-cost-and-abuse-controls.md) | attribution, budgets, denial of wallet, key abuse, runaway agents, shadow spend, enforcement | 21 | 5 | 11 | 5 | 0 |
| | **Total** | | **{{n:domain_tests}}** | **37** | **76** | **20** | **0** |

## Coverage at a glance

Counts are taken from the case index of each layer and domain file. Test method covers all {{n:tests}} cases; the domain tags below apply to the {{n:layer_tests}} layer cases.

| Test method | Cases | Meaning |
|---|---|---|
| Technical | 554 | Executed live in the PoC lab |
| Evidence | 105 | Verified by configuration, export, workflow or document inspection |
| Attestation | 14 | Vendor written declaration, scored lower than demonstrated evidence |

| Tag | Use-case domain | Cases tagged |
|---|---|---|
| D1 | Workforce / Browser AI Governance | 56 |
| D2 | Developer / IDE AI Security | 29 |
| D3 | Custom AI Application Runtime Security | 197 |
| D4 | Model Security / AI Supply Chain | 122 |
| D5 | Agentic AI / MCP / Tool Governance | 89 |
| D6 | Data Protection / DLP / Investigation | 112 |
| D7 | Sovereignty / Compliance / UAE Requirements | 170 |

A case can carry more than one domain tag, so the domain counts add up to more than {{n:layer_tests}}. D2 covers the developer workflow end to end: IDE prompts, assistant extensions, coding agents, MCP configuration, repository policy, pipeline bots and SOC telemetry, with L05 as its primary layer.

## Numbering and structure

Layer case IDs take the form `TC-L##-###`: the lifecycle layer and a sequence within it, for example `TC-L08-014`. Emerging-domain case IDs take the form `TC-D##-###`, for example `TC-D10-007`. IDs are unique across the library and stable once issued. Where a case is the detailed version of a quick-start scenario, the **Quick-Start Scenario** field links to it by ID, for example `AI-POC-ID-004`.

Each case records: lifecycle layer, use-case domains, test method (Technical, Evidence or Attestation), vendor applicability (E endpoint or browser agent, G inline gateway or proxy, A application or API-level control, P posture or AI-SPM, R red-team tool, W governance workflow), risk, scenarios, test data, numbered procedure, expected results, pass and fail criteria, scoring, evidence to capture, and reference mappings.

Layers L01 to L03 are framework-neutral. Their cases use an **Expected Result** field in place of Expected Detection, and add Control Theme, Applicable Requirement and Framework Crosswalk fields for the assessor to complete.

## Safety boundary

All test cases use synthetic, non-functional or clearly marked test data only. No real customer, employee, financial, health or credential data should be used or substituted during execution. Probe and simulation scripts are harmless lab tools. Never run them against production systems.

## How to use

1. Read the Reference Index and decide which layers, use-case domains and emerging domains are in scope.
2. Build the lab prerequisites each layer calls for (mock providers, test cluster, lab SIEM, fabricated data).
3. Run each case, capture the evidence listed, and score 0, 3 or 5 (or N/A where the vendor architecture cannot perform the test by design).
4. For layers L01 to L03, complete the Applicable Requirement and Framework Crosswalk fields first.
