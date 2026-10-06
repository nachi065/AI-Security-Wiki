---
title: "Appendix: Lab Prerequisites"
description: "Lab prerequisites for AI security PoC testing: the environment, mock services, tooling and synthetic data needed for each AI lifecycle layer."
parent: "Test Case Library"
nav_order: 3
---

# Appendix: Lab Prerequisites

This appendix compiles the setup each layer assumes, taken directly from the Preconditions field of its cases. It is a starting checklist, not an exhaustive build guide. Where a layer shows several variants, the first is the standard setup and the others are extra setup needed only by the listed cases.

[Back to library overview](index.md)

## L01 Business & Use Cases

**Standard setup (all cases):** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per this appendix; test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials.

- **Lab environment** (20 cases): Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

## L02 Governance & Risk Mgmt

**Standard setup (all cases):** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per this appendix; test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials.

- **Lab environment** (25 cases): Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

## L03 Legal, Privacy & Compliance

**Standard setup (all cases):** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per this appendix; test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials.

- **Lab environment** (30 cases): Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

## L04 Human Interaction Layer

**Standard setup (all cases):** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per this appendix; platform agent or integration installed for the channel under test.

- **Developer and IDE test bench** (2 cases): Managed test workstations with two IDE families and AI coding assistant extensions, a CLI coding agent, corporate and personal test accounts, fabricated repositories (general, restricted and infrastructure-as-code) on a lab source-control server, a mock extension marketplace, mock MCP servers and a mock URL endpoint that records requests; no real source code, tokens or keys.

## L05 AI Applications

**Standard setup (all cases):** Isolated PoC lab provisioned; test applications, test tenants and synthetic data seeded per this appendix; platform integration or SDK deployed on the applications under test.

- **Developer and IDE test bench** (5 cases): Managed test workstations with two IDE families and AI coding assistant extensions, a CLI coding agent, corporate and personal test accounts, fabricated repositories (general, restricted and infrastructure-as-code) on a lab source-control server, a mock extension marketplace, mock MCP servers and a mock URL endpoint that records requests; no real source code, tokens or keys.

## L06 Agent Orchestration Layer

**Standard setup (all cases):** Isolated PoC lab provisioned; lab agent framework, mock tools, mock MCP servers and test users seeded per this appendix; platform deployed in the documented mode for agent and tool traffic.

- **Lab environment** (29 cases): Lab agent framework with a controllable model or scripted agent, mock tools and mock MCP servers writing to a lab sink, canary strings registered in advance, and attack-success baseline measured with the platform disabled.
- **Additional setup** ([TC-L06-003](L06-agent-orchestration-layer.md#tc-l06-003)): Cross-reference L04 and L05 discovery cases.
- **Additional setup** ([TC-L06-004](L06-agent-orchestration-layer.md#tc-l06-004)): Low-code agent tenant available in the lab.
- **Additional setup** ([TC-L06-005](L06-agent-orchestration-layer.md#tc-l06-005)): Test MCP servers are benign and written for the lab.
- **Additional setup** ([TC-L06-010](L06-agent-orchestration-layer.md#tc-l06-010)): Lab servers configured with the four security modes.
- **Additional setup** ([TC-L06-025](L06-agent-orchestration-layer.md#tc-l06-025)): Probes use canary files and lab hosts only.
- **Additional setup** ([TC-L06-031](L06-agent-orchestration-layer.md#tc-l06-031)): Computer-use agent available in the lab.
- **Developer and IDE test bench** (2 cases): Managed test workstations with two IDE families and AI coding assistant extensions, a CLI coding agent, corporate and personal test accounts, fabricated repositories (general, restricted and infrastructure-as-code) on a lab source-control server, a mock extension marketplace, mock MCP servers and a mock URL endpoint that records requests; no real source code, tokens or keys.

## L07 Prompt & Context Layer

**Standard setup (all cases):** Isolated PoC lab provisioned; test application, mock model or lab-hosted model, mock tools and test users seeded per this appendix; platform deployed in the documented mode for the channel under test.

- **Lab environment** (25 cases): Test application backed by a lab-hosted or mock model; mock tools writing to a lab sink; canary strings registered in advance; attack-success baseline measured with the platform disabled so only payloads that actually work are counted.
- **Additional setup** ([TC-L07-014](L07-prompt-and-context-layer.md#tc-l07-014), [TC-L07-023](L07-prompt-and-context-layer.md#tc-l07-023)): Multimodal model available in the lab.
- **Additional setup** ([TC-L07-009](L07-prompt-and-context-layer.md#tc-l07-009)): Lab web server hosting the test pages; no external sites.
- **Additional setup** ([TC-L07-010](L07-prompt-and-context-layer.md#tc-l07-010)): Lab mailbox and document store populated before testing.
- **Additional setup** ([TC-L07-012](L07-prompt-and-context-layer.md#tc-l07-012)): Cross-reference L11 cases for vector store controls.
- **Additional setup** ([TC-L07-015](L07-prompt-and-context-layer.md#tc-l07-015)): Lab collaboration workspace with test users.
- **Additional setup** ([TC-L07-016](L07-prompt-and-context-layer.md#tc-l07-016)): Lab collector reachable only from the test application.
- **Additional setup** ([TC-L07-021](L07-prompt-and-context-layer.md#tc-l07-021)): Fuzzing tool licensed or open source and approved for the lab.
- **Additional setup** ([TC-L07-024](L07-prompt-and-context-layer.md#tc-l07-024)): Version numbers recorded for platform, policy and model.
- **Additional setup** ([TC-L07-028](L07-prompt-and-context-layer.md#tc-l07-028)): Assistant with a memory feature available.
- **Additional setup** ([TC-L07-029](L07-prompt-and-context-layer.md#tc-l07-029)): Two tenants configured in the lab.
- **Additional setup** ([TC-L07-034](L07-prompt-and-context-layer.md#tc-l07-034)): Prompt store or equivalent configured in the lab.
- **Additional setup** ([TC-L07-037](L07-prompt-and-context-layer.md#tc-l07-037)): Analysts independent of the vendor.
- **Additional setup** ([TC-L07-039](L07-prompt-and-context-layer.md#tc-l07-039)): Prompts stored in a test repository.
- **Additional setup** ([TC-L07-040](L07-prompt-and-context-layer.md#tc-l07-040)): Evaluator selects new techniques after the PoC begins.
- **Developer and IDE test bench** (1 case): Managed test workstations with two IDE families and AI coding assistant extensions, a CLI coding agent, corporate and personal test accounts, fabricated repositories (general, restricted and infrastructure-as-code) on a lab source-control server, a mock extension marketplace, mock MCP servers and a mock URL endpoint that records requests; no real source code, tokens or keys.

## L08 AI Gateway & Security Controls

**Standard setup (all cases):** Isolated PoC lab provisioned; gateway or agent deployed in the documented mode; test users and synthetic data seeded per this appendix; baseline traffic captured without the platform.

- **Additional setup** ([TC-L08-001](L08-ai-gateway-and-security-controls.md#tc-l08-001)): Lab egress logging enabled and baseline noise (OS updates, browser telemetry) filtered out so only platform traffic is analysed.
- **Additional setup** ([TC-L08-002](L08-ai-gateway-and-security-controls.md#tc-l08-002)): At least one app in the test set must be unknown to the vendor's catalogue at the start of the test.
- **Additional setup** ([TC-L08-003](L08-ai-gateway-and-security-controls.md#tc-l08-003)): IdP groups and MDM posture feeds connected to the platform before testing.
- **Additional setup** ([TC-L08-004](L08-ai-gateway-and-security-controls.md#tc-l08-004)): Mock AI provider or capture point available so provider-received content can be inspected.
- **Additional setup** ([TC-L08-005](L08-ai-gateway-and-security-controls.md#tc-l08-005)): Only numbers from published test ranges and fabricated formats are used.
- **Additional setup** ([TC-L08-006](L08-ai-gateway-and-security-controls.md#tc-l08-006)): Identifier formats built from publicly documented structure only; no real identifiers.
- **Additional setup** ([TC-L08-007](L08-ai-gateway-and-security-controls.md#tc-l08-007)): All secrets fabricated, non-functional and clearly marked.
- **Additional setup** ([TC-L08-008](L08-ai-gateway-and-security-controls.md#tc-l08-008)): Terms and documents are fictional.
- **Additional setup** ([TC-L08-010](L08-ai-gateway-and-security-controls.md#tc-l08-010)): Mock model able to echo and rewrite text.
- **Additional setup** ([TC-L08-011](L08-ai-gateway-and-security-controls.md#tc-l08-011)): Only synthetic data used.
- **Additional setup** ([TC-L08-012](L08-ai-gateway-and-security-controls.md#tc-l08-012)): Files built from fabricated content.
- **Additional setup** ([TC-L08-013](L08-ai-gateway-and-security-controls.md#tc-l08-013)): Images fabricated for the test.
- **Additional setup** ([TC-L08-015](L08-ai-gateway-and-security-controls.md#tc-l08-015)): Labelled data set agreed in advance and kept out of the vendor's hands.
- **Additional setup** ([TC-L08-016](L08-ai-gateway-and-security-controls.md#tc-l08-016)): Benign target requests only; no real harmful content.
- **Additional setup** ([TC-L08-018](L08-ai-gateway-and-security-controls.md#tc-l08-018)): Mock responses are mild, clearly labelled and contain no operational content.
- **Additional setup** ([TC-L08-019](L08-ai-gateway-and-security-controls.md#tc-l08-019)): Canary and hostname fabricated.
- **Additional setup** ([TC-L08-021](L08-ai-gateway-and-security-controls.md#tc-l08-021)): Earlier test results recorded for baseline.
- **Additional setup** ([TC-L08-022](L08-ai-gateway-and-security-controls.md#tc-l08-022)): Mock endpoint available that supports all five protocols.
- **Additional setup** ([TC-L08-025](L08-ai-gateway-and-security-controls.md#tc-l08-025)): Test accounts with documented privilege levels.
- **Additional setup** ([TC-L08-028](L08-ai-gateway-and-security-controls.md#tc-l08-028)): Mock providers for approved and unapproved endpoints.
- **Additional setup** ([TC-L08-029](L08-ai-gateway-and-security-controls.md#tc-l08-029)): Mock provider that accepts only the fabricated key.
- **Additional setup** ([TC-L08-032](L08-ai-gateway-and-security-controls.md#tc-l08-032)): Controlled network path with known baseline.
- **Additional setup** ([TC-L08-033](L08-ai-gateway-and-security-controls.md#tc-l08-033)): Dedicated lab capacity; no production traffic.
- **Additional setup** ([TC-L08-034](L08-ai-gateway-and-security-controls.md#tc-l08-034)): Vendor-documented HA architecture deployed.
- **Additional setup** ([TC-L08-040](L08-ai-gateway-and-security-controls.md#tc-l08-040)): Storage region documented before testing.
- **Developer and IDE test bench** (2 cases): Managed test workstations with two IDE families and AI coding assistant extensions, a CLI coding agent, corporate and personal test accounts, fabricated repositories (general, restricted and infrastructure-as-code) on a lab source-control server, a mock extension marketplace, mock MCP servers and a mock URL endpoint that records requests; no real source code, tokens or keys.

## L09 Identity & Access Mgmt

**Standard setup (all cases):** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per this appendix; platform connected with least-privilege test credentials.

- **Lab environment** (25 cases): Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.
- **Developer and IDE test bench** (1 case): Managed test workstations with two IDE families and AI coding assistant extensions, a CLI coding agent, corporate and personal test accounts, fabricated repositories (general, restricted and infrastructure-as-code) on a lab source-control server, a mock extension marketplace, mock MCP servers and a mock URL endpoint that records requests; no real source code, tokens or keys.

## L10 Data Layer

**Standard setup (all cases):** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per this appendix; platform connected with least-privilege test credentials.

- **Lab environment** (29 cases): Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.
- **Additional setup** ([TC-L10-012](L10-data-layer.md#tc-l10-012)): Endpoints in multiple regions available in the lab or mocked.

## L11 Knowledge & Retrieval Layer

**Standard setup (all cases):** Isolated PoC lab provisioned; lab RAG application, test vector store, fabricated corpus and test users seeded per this appendix; platform connected to the lab knowledge sources with least-privilege test credentials.

- **Lab environment** (25 cases): Lab RAG application with a test vector store, a fabricated corpus of 200 documents with access control lists, registered canary content and test users; no production knowledge sources connected.

## L12 Model Layer

**Standard setup (all cases):** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per this appendix; platform connected to the lab model environment with least-privilege test credentials.

- **Lab environment** (25 cases): Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

## L13 Training & Fine-Tuning Layer

**Standard setup (all cases):** Isolated PoC lab provisioned; lab training environment, fabricated datasets, small open-weight model, mock registry and test users seeded per this appendix; platform connected with least-privilege test credentials.

- **Lab environment** (20 cases): Lab training environment with fabricated datasets, a small open-weight model for fine-tuning, harmless trigger phrases, registered canary strings, a mock model registry and test users; no production data or production training pipelines connected.

## L14 MLOps / LLMOps Layer

**Standard setup (all cases):** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per this appendix; platform connected with least-privilege test credentials.

- **Lab environment** (20 cases): Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.
- **Developer and IDE test bench** (2 cases): Managed test workstations with two IDE families and AI coding assistant extensions, a CLI coding agent, corporate and personal test accounts, fabricated repositories (general, restricted and infrastructure-as-code) on a lab source-control server, a mock extension marketplace, mock MCP servers and a mock URL endpoint that records requests; no real source code, tokens or keys.

## L15 Infrastructure Layer

**Standard setup (all cases):** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per this appendix; platform connected with least-privilege test credentials.

- **Lab environment** (18 cases): Lab Kubernetes cluster with real or simulated GPU nodes, mock inference servers, a test cloud account with fabricated resources, separate network segments, seeded misconfigurations and test users; no production infrastructure, accounts or data connected.
- **Additional setup** ([TC-L15-003](L15-infrastructure-layer.md#tc-l15-003)): Lab GPU hardware or documented simulation; probe is lab-only and harmless.
- **Additional setup** ([TC-L15-008](L15-infrastructure-layer.md#tc-l15-008)): Probes are harmless lab scripts that only attempt connections and reads of canary resources.

## L16 Supply Chain & Third Party

**Standard setup (all cases):** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per this appendix; written vendor evidence requests issued before testing; platform connected with least-privilege test credentials.

- **Lab environment** (25 cases): Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.
- **Developer and IDE test bench** (1 case): Managed test workstations with two IDE families and AI coding assistant extensions, a CLI coding agent, corporate and personal test accounts, fabricated repositories (general, restricted and infrastructure-as-code) on a lab source-control server, a mock extension marketplace, mock MCP servers and a mock URL endpoint that records requests; no real source code, tokens or keys.

## L17 Monitoring, Detection & Response

**Standard setup (all cases):** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per this appendix; no production alerting connected.

- **Lab environment** (30 cases): Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.
- **Developer and IDE test bench** (1 case): Managed test workstations with two IDE families and AI coding assistant extensions, a CLI coding agent, corporate and personal test accounts, fabricated repositories (general, restricted and infrastructure-as-code) on a lab source-control server, a mock extension marketplace, mock MCP servers and a mock URL endpoint that records requests; no real source code, tokens or keys.

