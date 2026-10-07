---
title: "AI Security Control Objectives Library"
author: Nachiket Sathaye
parent: "Control Library"
nav_order: 1
document_type: AI Security Wiki Reference
version: 2.1
---

# AI Security Control Objectives Library

> **Purpose:** Define reusable AI security control objectives for governance, engineering, vendor evaluation and audit testing.

> **Audience:** Security engineering, GRC, audit, AI product teams, SOC.

> **How to use:** Select controls by risk tier, then update the evidence, owners, control status, and links as implementation maturity improves.

The library holds **40 control objectives in 11 families**. Each control has a stable ID that the rest of the wiki uses: the [AI Risk to Control Mapping](../02_Risk_Management/02D_AI_Risk_to_Control_Mapping.md) links risks to controls, the [domain standards](../04_Domain_Standards/index.md) cite the controls they apply, the [AI Security Audit and Evidence Checklist](../06_Testing_and_Assurance/14_AI_Security_Audit_and_Evidence_Checklist.md) lists the evidence, and every one of the 620 cases in the [Test Case Library](../10_Test_Case_Library/index.md) names the control it tests.

The controls follow the design principle set out in the [Foundations paper](../00_Foundations/07-Reference-Architecture.md): the model is an untrusted component, and authority to act, access data or spend money is enforced outside it.

## Framework identifiers

Each control cites the identifiers published by the framework owner. Where a framework has no matching entry, the cell says so and the wiki's own control ID stands in.

| Framework | Version used | Identifier format |
|---|---|---|
| OWASP Top 10 for LLM Applications | 2025 | `LLM01:2025` to `LLM10:2025` |
| OWASP Top 10 for Agentic Applications | 2026 | `ASI01` to `ASI10` |
| MITRE ATLAS | 2026.09 | Techniques `AML.T####`; mitigations `AML.M####` |
| NIST AI Risk Management Framework | 1.0 | Subcategories, for example `MEASURE 2.7` |
| ISO/IEC 42001 | 2023 | Annex A controls, for example `A.6.2.4`; management system clauses, for example `Clause 9.2` |
| AI Security Wiki (own) | This page | `AI-CTRL-001` to `AI-CTRL-040` |

> **Verify before use.** Frameworks are revised. MITRE ATLAS in particular is updated monthly and renames techniques. Check identifiers against the current published versions before quoting them in an RFP or audit. Owners and review frequencies are starting values; set your own.

## Control families

| Family | Controls |
|---|---|
| Governance and Compliance | [AI-CTRL-007](#ai-ctrl-007), [AI-CTRL-011](#ai-ctrl-011), [AI-CTRL-012](#ai-ctrl-012), [AI-CTRL-013](#ai-ctrl-013), [AI-CTRL-014](#ai-ctrl-014), [AI-CTRL-037](#ai-ctrl-037) |
| Discovery and Workforce AI Use | [AI-CTRL-001](#ai-ctrl-001), [AI-CTRL-002](#ai-ctrl-002), [AI-CTRL-003](#ai-ctrl-003), [AI-CTRL-004](#ai-ctrl-004), [AI-CTRL-010](#ai-ctrl-010) |
| Identity and Access | [AI-CTRL-015](#ai-ctrl-015), [AI-CTRL-016](#ai-ctrl-016) |
| Data and Retrieval | [AI-CTRL-017](#ai-ctrl-017), [AI-CTRL-018](#ai-ctrl-018), [AI-CTRL-019](#ai-ctrl-019) |
| Application Runtime | [AI-CTRL-005](#ai-ctrl-005), [AI-CTRL-020](#ai-ctrl-020), [AI-CTRL-021](#ai-ctrl-021), [AI-CTRL-039](#ai-ctrl-039) |
| Agents and Tools | [AI-CTRL-006](#ai-ctrl-006), [AI-CTRL-022](#ai-ctrl-022), [AI-CTRL-023](#ai-ctrl-023), [AI-CTRL-024](#ai-ctrl-024), [AI-CTRL-025](#ai-ctrl-025), [AI-CTRL-026](#ai-ctrl-026), [AI-CTRL-027](#ai-ctrl-027) |
| Model, Training and Pipeline | [AI-CTRL-028](#ai-ctrl-028), [AI-CTRL-029](#ai-ctrl-029), [AI-CTRL-030](#ai-ctrl-030) |
| Supply Chain, Infrastructure and Resilience | [AI-CTRL-031](#ai-ctrl-031), [AI-CTRL-032](#ai-ctrl-032), [AI-CTRL-040](#ai-ctrl-040) |
| Assurance and Testing | [AI-CTRL-033](#ai-ctrl-033), [AI-CTRL-034](#ai-ctrl-034), [AI-CTRL-038](#ai-ctrl-038) |
| Detection and Response | [AI-CTRL-008](#ai-ctrl-008), [AI-CTRL-009](#ai-ctrl-009), [AI-CTRL-035](#ai-ctrl-035) |
| Cost and Abuse | [AI-CTRL-036](#ai-ctrl-036) |

## Control index

| Control ID | Control Name | Family | Objective | Test Cases |
|---|---|---|---|---|
| [AI-CTRL-001](#ai-ctrl-001) | AI Discovery | Discovery and Workforce AI Use | Identify approved/unapproved AI platforms across browsers, endpoints, IDEs, SaaS, APIs and custom apps. | 33 |
| [AI-CTRL-002](#ai-ctrl-002) | Prompt Inspection | Discovery and Workforce AI Use | Detect sensitive, restricted or risky content submitted to AI platforms. | 16 |
| [AI-CTRL-003](#ai-ctrl-003) | File Upload Protection | Discovery and Workforce AI Use | Prevent uploads of confidential or restricted files to unauthorized AI services. | 6 |
| [AI-CTRL-004](#ai-ctrl-004) | IDE AI Governance | Discovery and Workforce AI Use | Monitor and control AI coding assistants, source code sharing and secret leakage. | 18 |
| [AI-CTRL-005](#ai-ctrl-005) | Runtime AI Security | Application Runtime | Protect custom AI applications from prompt injection, misuse and output leakage. | 52 |
| [AI-CTRL-006](#ai-ctrl-006) | Agent Governance | Agents and Tools | Monitor AI agents, tool calls, API access and autonomous actions. | 13 |
| [AI-CTRL-007](#ai-ctrl-007) | Data Sovereignty | Governance and Compliance | Ensure prompts, logs and uploads are processed and retained in approved locations. | 14 |
| [AI-CTRL-008](#ai-ctrl-008) | Auditability | Detection and Response | Maintain logs for prompts, responses, files, users, devices, applications and actions. | 19 |
| [AI-CTRL-009](#ai-ctrl-009) | SOC Integration | Detection and Response | Forward AI security events and logs to monitoring and response platforms. | 22 |
| [AI-CTRL-010](#ai-ctrl-010) | Policy Enforcement | Discovery and Workforce AI Use | Support monitor, warn, redact, block and allow policies based on risk and classification. | 27 |
| [AI-CTRL-011](#ai-ctrl-011) | AI Use-Case Registry and Risk Tiering | Governance and Compliance | Record every AI use case with a business owner and a risk tier that decides which controls apply. | 17 |
| [AI-CTRL-012](#ai-ctrl-012) | AI Policy, Roles and Acceptable Use | Governance and Compliance | Set and communicate the rules and responsibilities for using and building AI, and map each rule to a control. | 7 |
| [AI-CTRL-013](#ai-ctrl-013) | Privacy and Regulatory Compliance | Governance and Compliance | Meet privacy and regulatory obligations for personal data handled by AI systems. | 38 |
| [AI-CTRL-014](#ai-ctrl-014) | Third-Party and Vendor AI Assurance | Governance and Compliance | Assess AI vendors and embedded AI features before use, and reassess when they change. | 23 |
| [AI-CTRL-015](#ai-ctrl-015) | Human and Agent Identity | Identity and Access | Give every user, application and agent that uses AI a unique, attributable identity. | 31 |
| [AI-CTRL-016](#ai-ctrl-016) | Least Privilege and Scoped Credentials | Identity and Access | Limit what each AI workload and agent can reach to the minimum its task needs. | 39 |
| [AI-CTRL-017](#ai-ctrl-017) | Data Protection in AI Pipelines | Data and Retrieval | Apply classification, minimization and isolation to data that AI systems ingest, process and produce. | 30 |
| [AI-CTRL-018](#ai-ctrl-018) | Retrieval Access Control | Data and Retrieval | Return only content the requesting user is entitled to see. | 9 |
| [AI-CTRL-019](#ai-ctrl-019) | Knowledge Base Integrity | Data and Retrieval | Stop untrusted or poisoned content from entering the corpus that AI systems retrieve from. | 12 |
| [AI-CTRL-020](#ai-ctrl-020) | Output Handling | Application Runtime | Treat model output as untrusted input to whatever consumes it. | 12 |
| [AI-CTRL-021](#ai-ctrl-021) | Multimodal and Voice Input Security | Application Runtime | Apply the same inspection and policy to images, documents, audio and video as to text. | 28 |
| [AI-CTRL-022](#ai-ctrl-022) | Deterministic Action Authorization | Agents and Tools | Enforce authority to act, access data or spend money outside the model. | 16 |
| [AI-CTRL-023](#ai-ctrl-023) | Human Approval for Sensitive Actions | Agents and Tools | Require a person to approve irreversible or high-impact actions before they run. | 7 |
| [AI-CTRL-024](#ai-ctrl-024) | Tool and MCP Server Governance | Agents and Tools | Allow agents to use only vetted tools and tool servers, and detect when they change. | 14 |
| [AI-CTRL-025](#ai-ctrl-025) | Agent Containment and Kill Switch | Agents and Tools | Stop an agent, revoke its access and limit the damage within minutes. | 10 |
| [AI-CTRL-026](#ai-ctrl-026) | Agent Memory and Context Integrity | Agents and Tools | Prevent poisoned or cross-user content from persisting in agent memory and context. | 5 |
| [AI-CTRL-027](#ai-ctrl-027) | Agent Execution Isolation | Agents and Tools | Run agent-generated code and browser or computer-use sessions in isolation. | 10 |
| [AI-CTRL-028](#ai-ctrl-028) | Model Protection | Model, Training and Pipeline | Protect models from theft, extraction and adversarial inputs. | 16 |
| [AI-CTRL-029](#ai-ctrl-029) | Training and Fine-Tuning Data Integrity | Model, Training and Pipeline | Know where training data came from and detect tampering before it shapes a model. | 15 |
| [AI-CTRL-030](#ai-ctrl-030) | ML Pipeline and Model Registry Security | Model, Training and Pipeline | Protect the pipeline that builds, stores and releases models and prompts. | 16 |
| [AI-CTRL-031](#ai-ctrl-031) | AI Supply Chain and AI-BOM | Supply Chain, Infrastructure and Resilience | Know exactly which models, datasets, packages and prompts run in each environment. | 24 |
| [AI-CTRL-032](#ai-ctrl-032) | AI Infrastructure Hardening | Supply Chain, Infrastructure and Resilience | Harden and segment the infrastructure that trains and serves models. | 26 |
| [AI-CTRL-033](#ai-ctrl-033) | AI Security Review and Release Gate | Assurance and Testing | Review every AI system against its threats before production and after material change. | 6 |
| [AI-CTRL-034](#ai-ctrl-034) | Adversarial Testing and Continuous Evaluation | Assurance and Testing | Test AI systems against attacks before release and continuously afterwards. | 36 |
| [AI-CTRL-035](#ai-ctrl-035) | AI Incident Response and Forensics | Detection and Response | Detect, contain, investigate and recover from AI security incidents. | 39 |
| [AI-CTRL-036](#ai-ctrl-036) | AI Cost and Abuse Controls | Cost and Abuse | Attribute AI spend and stop abuse that exhausts budget or capacity. | 30 |
| [AI-CTRL-037](#ai-ctrl-037) | AI Risk Assessment and Exception Management | Governance and Compliance | Assess, treat and accept AI risks consistently, and keep every exception owned and time-bound. | 10 |
| [AI-CTRL-038](#ai-ctrl-038) | Control Assurance and Audit Evidence | Assurance and Testing | Show, with current evidence, that each AI control is operating and that findings are closed. | 17 |
| [AI-CTRL-039](#ai-ctrl-039) | Output Reliability and Content Safety | Application Runtime | Keep AI output grounded, within its approved scope and free of harmful content. | 6 |
| [AI-CTRL-040](#ai-ctrl-040) | AI Service Resilience and Fail-Safe Operation | Supply Chain, Infrastructure and Resilience | Keep AI services and their security controls available, and make them fail safely. | 13 |

A test case is counted under every control it tests, so the counts add up to more than 620.

## Control entries

### Governance and Compliance

<a id="ai-ctrl-007"></a>

#### AI-CTRL-007: Data Sovereignty

| Field | Detail |
|---|---|
| **Control Objective** | Ensure prompts, logs and uploads are processed and retained in approved locations. |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents / Vendors |
| **Risk Mapping** | [AI-R10](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Confirm where prompts, uploads, outputs, metadata and logs are processed and stored, including the control plane and support access. Configure retention and training exclusion, and record any cross-border transfer. |
| **Evidence Required** | Residency attestation; retention configuration; training exclusion terms; administrative access logs. |
| **Audit Test Procedure** | Trace a test prompt and upload end to end and verify processing and storage locations against the approved list. Verify retention settings by checking that expired records are gone. |
| **Control Owner** | GRC / Legal |
| **Review Frequency** | Annually and on vendor change |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-007. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-007. |
| **MITRE ATLAS Mitigations** | None published in MITRE ATLAS mitigations. The wiki's own identifier applies: AI-CTRL-007. |
| **NIST AI RMF** | GOVERN 1.1; GOVERN 6.1; MAP 4.1 |
| **ISO/IEC 42001** | A.10.3 Suppliers; A.4.5 System and computing resources |
| **Tested By (14 cases)** | **L03:** [012](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-012), [013](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-013), [014](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-014)<br>**L08:** [001](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-001)<br>**L10:** [012](../10_Test_Case_Library/L10-data-layer.md#tc-l10-012), [013](../10_Test_Case_Library/L10-data-layer.md#tc-l10-013), [014](../10_Test_Case_Library/L10-data-layer.md#tc-l10-014), [015](../10_Test_Case_Library/L10-data-layer.md#tc-l10-015), [025](../10_Test_Case_Library/L10-data-layer.md#tc-l10-025)<br>**L15:** [013](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-013), [014](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-014), [015](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-015), [020](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-020)<br>**L16:** [019](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-019) |

<a id="ai-ctrl-011"></a>

#### AI-CTRL-011: AI Use-Case Registry and Risk Tiering

| Field | Detail |
|---|---|
| **Control Objective** | Record every AI use case with a business owner and a risk tier that decides which controls apply. |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents / Vendors |
| **Risk Mapping** | [AI-R02](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Require intake and approval before deployment. Record owner, purpose, data, model, users and autonomy for each use case. Assign a risk tier using published criteria, and re-tier when the use case changes. |
| **Evidence Required** | Use-case registry; intake and approval records; tiering criteria; re-tiering history. |
| **Audit Test Procedure** | Sample use cases in production and confirm each has a registry entry, an owner and a tier consistent with the criteria. Sample registry entries and confirm they match what is deployed. |
| **Control Owner** | AI Governance Lead |
| **Review Frequency** | Quarterly |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-011. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-011. |
| **MITRE ATLAS Mitigations** | None published in MITRE ATLAS mitigations. The wiki's own identifier applies: AI-CTRL-011. |
| **NIST AI RMF** | GOVERN 1.6; GOVERN 1.3; GOVERN 1.7; MAP 1.1 |
| **ISO/IEC 42001** | A.4.2 Resource documentation; A.5.2 AI system impact assessment process; A.9.4 Intended use of the AI system |
| **Tested By (17 cases)** | **L01:** [001](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-001), [002](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-002), [003](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-003), [004](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-004), [005](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-005), [006](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-006), [007](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-007), [008](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-008), [009](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-009), [013](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-013), [016](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-016), [019](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-019), [020](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-020)<br>**L05:** [007](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-007), [029](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-029)<br>**L12:** [024](../10_Test_Case_Library/L12-model-layer.md#tc-l12-024), [025](../10_Test_Case_Library/L12-model-layer.md#tc-l12-025) |

<a id="ai-ctrl-012"></a>

#### AI-CTRL-012: AI Policy, Roles and Acceptable Use

| Field | Detail |
|---|---|
| **Control Objective** | Set and communicate the rules and responsibilities for using and building AI, and map each rule to a control. |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents |
| **Risk Mapping** | [AI-R02](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R03](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Publish an AI policy and acceptable-use standard with scope, owner and review date. Define roles and decision rights, and record governance decisions. Map each policy statement to a control in this library. Train users and reinforce the rules at the point of use. |
| **Evidence Required** | Approved policy; roles and responsibilities record; governance decision log; policy-to-control mapping; training and acknowledgement records. |
| **Audit Test Procedure** | Select policy statements and trace each to a control and to evidence that it operates. Confirm the policy was reviewed within its cycle. |
| **Control Owner** | GRC |
| **Review Frequency** | Annually |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-012. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-012. |
| **MITRE ATLAS Mitigations** | AML.M0018 User Training |
| **NIST AI RMF** | GOVERN 1.2; GOVERN 1.4; GOVERN 2.1; GOVERN 2.2 |
| **ISO/IEC 42001** | A.2.2 AI policy; A.2.4 Review of the AI policy; A.3.2 AI roles and responsibilities |
| **Tested By (7 cases)** | **L02:** [001](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-001), [002](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-002), [004](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-004), [005](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-005), [022](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-022), [023](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-023)<br>**L04:** [011](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-011) |

<a id="ai-ctrl-013"></a>

#### AI-CTRL-013: Privacy and Regulatory Compliance

| Field | Detail |
|---|---|
| **Control Objective** | Meet privacy and regulatory obligations for personal data handled by AI systems. |
| **Applies To** | Browser AI / AI APIs / Custom AI Applications / Agents / Vendors |
| **Risk Mapping** | [AI-R03](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R10](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Complete a privacy impact assessment for AI systems that process personal data. Define lawful basis, minimization, retention and data subject request handling, including data held in prompts, logs, indexes and memory. |
| **Evidence Required** | Impact assessments; records of processing; data subject request tests; evidence exports. |
| **Audit Test Procedure** | Run a data subject access and deletion request against a test identity and confirm the data is found and removed across prompts, logs, indexes and memory. |
| **Control Owner** | Privacy Office / Legal |
| **Review Frequency** | Annually and on material change |
| **OWASP** | LLM02:2025 Sensitive Information Disclosure |
| **MITRE ATLAS Techniques** | AML.T0057 LLM Data Leakage |
| **MITRE ATLAS Mitigations** | None published in MITRE ATLAS mitigations. The wiki's own identifier applies: AI-CTRL-013. |
| **NIST AI RMF** | GOVERN 1.1; MAP 5.1; MEASURE 2.10 |
| **ISO/IEC 42001** | A.5.2 AI system impact assessment process; A.5.3 Documentation of AI system impact assessments; A.5.4 Assessing AI system impact on individuals or groups of individuals |
| **Tested By (38 cases)** | **D11:** [007](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-007), [018](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-018), [019](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-019), [020](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-020)<br>**D12:** [015](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-015), [016](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-016)<br>**L01:** [010](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-010), [011](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-011)<br>**L02:** [020](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-020)<br>**L03:** [001](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-001), [002](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-002), [003](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-003), [004](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-004), [005](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-005), [006](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-006), [007](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-007), [008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008), [009](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-009), [010](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-010), [011](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-011), [015](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-015), [016](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-016), [017](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-017), [018](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-018), [019](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-019), [020](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-020), [028](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-028), [029](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-029), [030](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-030)<br>**L04:** [027](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-027)<br>**L07:** [030](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-030)<br>**L10:** [020](../10_Test_Case_Library/L10-data-layer.md#tc-l10-020), [021](../10_Test_Case_Library/L10-data-layer.md#tc-l10-021), [022](../10_Test_Case_Library/L10-data-layer.md#tc-l10-022)<br>**L13:** [002](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-002), [007](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-007), [019](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-019)<br>**L17:** [026](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-026) |

<a id="ai-ctrl-014"></a>

#### AI-CTRL-014: Third-Party and Vendor AI Assurance

| Field | Detail |
|---|---|
| **Control Objective** | Assess AI vendors and embedded AI features before use, and reassess when they change. |
| **Applies To** | Vendors / AI APIs / Browser AI |
| **Risk Mapping** | [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R10](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Evaluate vendors against the vendor evaluation framework. Cover training use of customer data, retention, sub-processors, model changes and incident notification in contracts. Re-evaluate when a vendor changes model or terms. |
| **Evidence Required** | Vendor assessments; contract clauses; sub-processor list; model change notices. |
| **Audit Test Procedure** | Sample AI vendors in use and confirm each has a current assessment and the required contract terms. Confirm the last model or terms change triggered a review. |
| **Control Owner** | Procurement / GRC |
| **Review Frequency** | Annually and on vendor change |
| **OWASP** | LLM03:2025 Supply Chain |
| **MITRE ATLAS Techniques** | AML.T0010 AI Supply Chain Compromise; AML.T0109 AI Supply Chain Rug Pull |
| **MITRE ATLAS Mitigations** | None published in MITRE ATLAS mitigations. The wiki's own identifier applies: AI-CTRL-014. |
| **NIST AI RMF** | GOVERN 6.1; GOVERN 6.2; MANAGE 3.1 |
| **ISO/IEC 42001** | A.10.2 Allocating responsibilities; A.10.3 Suppliers |
| **Tested By (23 cases)** | **D09:** [018](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-018)<br>**D12:** [017](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-017)<br>**D13:** [019](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-019)<br>**L01:** [017](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-017)<br>**L02:** [021](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-021)<br>**L03:** [020](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-020), [021](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-021)<br>**L06:** [032](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-032)<br>**L10:** [025](../10_Test_Case_Library/L10-data-layer.md#tc-l10-025)<br>**L13:** [009](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-009)<br>**L15:** [016](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-016)<br>**L16:** [008](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-008), [009](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-009), [010](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-010), [011](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-011), [012](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-012), [018](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-018), [019](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-019), [020](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-020), [021](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-021), [022](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-022), [023](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-023), [025](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-025) |

<a id="ai-ctrl-037"></a>

#### AI-CTRL-037: AI Risk Assessment and Exception Management

| Field | Detail |
|---|---|
| **Control Objective** | Assess, treat and accept AI risks consistently, and keep every exception owned and time-bound. |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents / Vendors |
| **Risk Mapping** | [AI-R02](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Keep an AI risk register with an owner and a score for every risk. Use one scoring method so that different assessors reach the same result. Accept residual risk only at the right authority level. Give every exception an owner, a compensating control and an expiry date that the technical control enforces. |
| **Evidence Required** | AI risk register; treatment plans; risk acceptance records; exception register with expiry dates. |
| **Audit Test Procedure** | Sample accepted risks and confirm the approver had the authority. Let a test exception expire and confirm the technical control blocks the activity again. |
| **Control Owner** | Cyber Risk / GRC |
| **Review Frequency** | Quarterly |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-037. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-037. |
| **MITRE ATLAS Mitigations** | None published in MITRE ATLAS mitigations. The wiki's own identifier applies: AI-CTRL-037. |
| **NIST AI RMF** | GOVERN 1.3; MAP 1.5; MANAGE 1.2; MANAGE 1.4 |
| **ISO/IEC 42001** | Clause 6.1.2 AI risk assessment; Clause 6.1.3 AI risk treatment |
| **Tested By (10 cases)** | **L02:** [006](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-006), [007](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-007), [008](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-008), [009](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-009), [010](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-010), [011](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-011), [012](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-012)<br>**L04:** [013](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-013), [014](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-014), [015](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-015) |

### Discovery and Workforce AI Use

<a id="ai-ctrl-001"></a>

#### AI-CTRL-001: AI Discovery

| Field | Detail |
|---|---|
| **Control Objective** | Identify approved/unapproved AI platforms across browsers, endpoints, IDEs, SaaS, APIs and custom apps. |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents |
| **Risk Mapping** | [AI-R02](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Discover AI services, extensions, plugins, embedded SaaS AI features and API usage continuously. Classify each as approved, tolerated or unapproved, and attribute use to a user, device and application. |
| **Evidence Required** | AI service inventory; usage dashboard; user and device reports; classification of each service. |
| **Audit Test Procedure** | Seed a known set of approved and unapproved AI tools in a test group and compare the discovered inventory with ground truth. Confirm new tools appear within the stated interval. |
| **Control Owner** | Security Engineering |
| **Review Frequency** | Quarterly |
| **OWASP** | LLM03:2025 Supply Chain |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-001. |
| **MITRE ATLAS Mitigations** | None published in MITRE ATLAS mitigations. The wiki's own identifier applies: AI-CTRL-001. |
| **NIST AI RMF** | GOVERN 1.6; GOVERN 6.1 |
| **ISO/IEC 42001** | A.4.2 Resource documentation |
| **Tested By (33 cases)** | **D10:** [001](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-001), [022](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-022)<br>**D11:** [001](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-001)<br>**D13:** [017](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-017)<br>**L01:** [008](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-008)<br>**L04:** [001](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-001), [002](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-002), [003](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-003), [004](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-004), [005](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-005), [006](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-006), [007](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-007), [008](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-008), [009](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-009), [010](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-010), [024](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-024), [025](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-025)<br>**L05:** [001](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-001), [002](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-002), [003](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-003), [004](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-004), [005](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-005), [006](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-006), [007](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-007), [008](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-008), [009](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-009), [011](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-011), [029](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-029)<br>**L11:** [001](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-001)<br>**L12:** [001](../10_Test_Case_Library/L12-model-layer.md#tc-l12-001)<br>**L14:** [001](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-001), [018](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-018)<br>**L15:** [001](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-001) |

<a id="ai-ctrl-002"></a>

#### AI-CTRL-002: Prompt Inspection

| Field | Detail |
|---|---|
| **Control Objective** | Detect sensitive, restricted or risky content submitted to AI platforms. |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications |
| **Risk Mapping** | [AI-R01](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R03](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Inspect prompts in line or at the endpoint for classified data, personal data, credentials and source code. Apply the data classification scheme already in use, and record the policy outcome for every detection. |
| **Evidence Required** | Prompt detection logs; policy outcomes; sampled test results by data type. |
| **Audit Test Procedure** | Submit a labelled set of sensitive and benign prompts through each channel. Measure detection rate and false positives, and confirm each detection is logged with user, device and destination. |
| **Control Owner** | AI Security Team |
| **Review Frequency** | Quarterly |
| **OWASP** | LLM02:2025 Sensitive Information Disclosure |
| **MITRE ATLAS Techniques** | AML.T0057 LLM Data Leakage |
| **MITRE ATLAS Mitigations** | AML.M0020 Generative AI Guardrails |
| **NIST AI RMF** | MEASURE 2.10; MANAGE 4.1 |
| **ISO/IEC 42001** | A.9.2 Processes for responsible use of AI systems |
| **Tested By (16 cases)** | **D11:** [006](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-006), [015](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-015), [016](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-016)<br>**L04:** [012](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-012), [017](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-017), [019](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-019), [028](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-028)<br>**L08:** [004](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-004), [005](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-005), [006](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-006), [007](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-007), [008](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-008), [010](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-010), [011](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-011), [014](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-014), [027](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-027) |

<a id="ai-ctrl-003"></a>

#### AI-CTRL-003: File Upload Protection

| Field | Detail |
|---|---|
| **Control Objective** | Prevent uploads of confidential or restricted files to unauthorized AI services. |
| **Applies To** | Browser AI / AI APIs / Custom AI Applications |
| **Risk Mapping** | [AI-R01](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R03](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Inspect files sent to AI services, including nested archives, images and documents with embedded content. Block or warn according to classification and the approval status of the destination. |
| **Evidence Required** | Upload block and warn logs; classification policy; file type coverage matrix. |
| **Audit Test Procedure** | Upload labelled test files of each supported type to approved and unapproved services. Confirm the expected action and log entry for each. |
| **Control Owner** | DLP Team |
| **Review Frequency** | Quarterly |
| **OWASP** | LLM02:2025 Sensitive Information Disclosure |
| **MITRE ATLAS Techniques** | AML.T0057 LLM Data Leakage |
| **MITRE ATLAS Mitigations** | AML.M0020 Generative AI Guardrails |
| **NIST AI RMF** | MEASURE 2.10; MANAGE 4.1 |
| **ISO/IEC 42001** | A.9.2 Processes for responsible use of AI systems |
| **Tested By (6 cases)** | **D10:** [009](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-009)<br>**L04:** [018](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-018), [020](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-020), [022](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-022)<br>**L08:** [012](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-012), [013](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-013) |

<a id="ai-ctrl-004"></a>

#### AI-CTRL-004: IDE AI Governance

| Field | Detail |
|---|---|
| **Control Objective** | Monitor and control AI coding assistants, source code sharing and secret leakage. |
| **Applies To** | IDE AI |
| **Risk Mapping** | [AI-R04](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Inventory AI coding assistants and extensions. Detect proprietary source code and secrets in assistant traffic, restrict assistants on restricted repositories, and attribute activity to developer, device and IDE. |
| **Evidence Required** | IDE assistant inventory; secret and source code detection events; repository policy; developer rules. |
| **Audit Test Procedure** | Send seeded secrets and marked source code through each approved assistant. Confirm detection, policy action and attribution. Confirm an unapproved extension is discovered. |
| **Control Owner** | DevSecOps |
| **Review Frequency** | Quarterly |
| **OWASP** | LLM02:2025 Sensitive Information Disclosure; LLM03:2025 Supply Chain |
| **MITRE ATLAS Techniques** | AML.T0057 LLM Data Leakage; AML.T0055 Unsecured Credentials |
| **MITRE ATLAS Mitigations** | None published in MITRE ATLAS mitigations. The wiki's own identifier applies: AI-CTRL-004. |
| **NIST AI RMF** | GOVERN 6.1; MEASURE 2.10; MANAGE 4.1 |
| **ISO/IEC 42001** | A.9.2 Processes for responsible use of AI systems; A.4.4 Tooling resources |
| **Tested By (18 cases)** | **L04:** [019](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-019), [031](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-031), [032](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-032)<br>**L05:** [004](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-004), [031](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-031), [032](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-032), [033](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-033), [034](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-034), [035](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-035)<br>**L06:** [037](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-037)<br>**L07:** [041](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-041)<br>**L08:** [007](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-007), [041](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-041), [042](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-042)<br>**L09:** [026](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-026)<br>**L14:** [021](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-021)<br>**L16:** [026](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-026)<br>**L17:** [031](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-031) |

<a id="ai-ctrl-010"></a>

#### AI-CTRL-010: Policy Enforcement

| Field | Detail |
|---|---|
| **Control Objective** | Support monitor, warn, redact, block and allow policies based on risk and classification. |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications |
| **Risk Mapping** | [AI-R01](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R02](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R03](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Apply graduated actions by user group, destination, data classification and risk. Coach users at the point of use, resist simple bypass, and manage exceptions with an owner and expiry date. |
| **Evidence Required** | Policy configuration; action logs by type; exception register; bypass test results. |
| **Audit Test Procedure** | For each policy action, run a matching test and confirm the action and log entry. Attempt documented bypass methods and record the result. |
| **Control Owner** | AI Security Team |
| **Review Frequency** | Quarterly |
| **OWASP** | LLM02:2025 Sensitive Information Disclosure |
| **MITRE ATLAS Techniques** | AML.T0057 LLM Data Leakage |
| **MITRE ATLAS Mitigations** | AML.M0020 Generative AI Guardrails |
| **NIST AI RMF** | GOVERN 1.4; MANAGE 1.3 |
| **ISO/IEC 42001** | A.9.2 Processes for responsible use of AI systems; A.2.2 AI policy |
| **Tested By (27 cases)** | **L02:** [011](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-011)<br>**L04:** [009](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-009), [011](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-011), [012](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-012), [013](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-013), [016](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-016), [025](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-025), [026](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-026), [029](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-029)<br>**L05:** [028](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-028)<br>**L08:** [001](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-001), [002](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-002), [003](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-003), [009](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-009), [010](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-010), [021](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-021), [022](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-022), [023](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-023), [024](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-024), [025](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-025), [026](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-026), [028](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-028), [036](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-036), [037](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-037), [038](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-038), [041](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-041)<br>**L12:** [021](../10_Test_Case_Library/L12-model-layer.md#tc-l12-021) |

### Identity and Access

<a id="ai-ctrl-015"></a>

#### AI-CTRL-015: Human and Agent Identity

| Field | Detail |
|---|---|
| **Control Objective** | Give every user, application and agent that uses AI a unique, attributable identity. |
| **Applies To** | AI APIs / Custom AI Applications / Agents |
| **Risk Mapping** | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Issue a unique identity to each agent and AI workload, with a named human sponsor. Do not share keys between workloads. Recertify identities on a schedule and remove them when the sponsor leaves or the use case ends. |
| **Evidence Required** | Identity registry; sponsor records; recertification results; orphaned identity report. |
| **Audit Test Procedure** | Sample agent identities and confirm each has a sponsor and a current recertification. Remove a test sponsor and confirm the agent identity is flagged. |
| **Control Owner** | IAM Team |
| **Review Frequency** | Semi-annually |
| **OWASP** | LLM06:2025 Excessive Agency; ASI03 Identity & Privilege Abuse |
| **MITRE ATLAS Techniques** | AML.T0012 Valid Accounts; AML.T0073 Impersonation; AML.T0091 Use Alternate Authentication Material |
| **MITRE ATLAS Mitigations** | AML.M0019 Control Access to AI Models and Data in Production |
| **NIST AI RMF** | MEASURE 2.7; MEASURE 2.8 |
| **ISO/IEC 42001** | None published in ISO/IEC 42001. The wiki's own identifier applies: AI-CTRL-015. |
| **Tested By (31 cases)** | **D09:** [001](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-001), [002](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-002), [003](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-003), [004](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-004), [008](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-008), [011](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-011), [012](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-012), [013](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-013), [015](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-015), [016](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-016), [017](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-017), [018](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-018), [019](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-019), [020](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-020)<br>**D10:** [015](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-015)<br>**D11:** [017](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-017)<br>**L04:** [030](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-030)<br>**L06:** [010](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-010), [018](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-018), [035](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-035)<br>**L09:** [001](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-001), [002](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-002), [010](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-010), [011](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-011), [012](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-012), [017](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-017), [018](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-018), [020](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-020), [021](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-021), [024](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-024), [025](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-025) |

<a id="ai-ctrl-016"></a>

#### AI-CTRL-016: Least Privilege and Scoped Credentials

| Field | Detail |
|---|---|
| **Control Objective** | Limit what each AI workload and agent can reach to the minimum its task needs. |
| **Applies To** | AI APIs / Custom AI Applications / Agents |
| **Risk Mapping** | [AI-R06](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Use short-lived credentials scoped per tool and resource. Act with the end user's rights where a user is present, not with a broad service account. Detect and correct permission drift. |
| **Evidence Required** | Permission maps; token scope configuration; access review records; drift reports. |
| **Audit Test Procedure** | Have a test agent attempt a tool or resource outside its scope and confirm it is denied and logged. Confirm credentials expire as configured. |
| **Control Owner** | IAM Team |
| **Review Frequency** | Quarterly |
| **OWASP** | LLM06:2025 Excessive Agency; ASI03 Identity & Privilege Abuse |
| **MITRE ATLAS Techniques** | AML.T0012 Valid Accounts; AML.T0055 Unsecured Credentials; AML.T0083 Credentials from AI Agent Configuration; AML.T0098 AI Agent Tool Credential Harvesting |
| **MITRE ATLAS Mitigations** | AML.M0026 Privileged AI Agent Permissions Configuration; AML.M0027 Single-User AI Agent Permissions Configuration; AML.M0028 AI Agent Tools Permissions Configuration |
| **NIST AI RMF** | MEASURE 2.7; MANAGE 1.3 |
| **ISO/IEC 42001** | None published in ISO/IEC 42001. The wiki's own identifier applies: AI-CTRL-016. |
| **Tested By (39 cases)** | **D09:** [005](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-005), [006](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-006), [007](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-007), [009](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-009), [010](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-010), [014](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-014)<br>**D10:** [003](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-003), [021](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-021)<br>**D13:** [005](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-005)<br>**L05:** [010](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-010)<br>**L06:** [012](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-012), [013](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-013), [017](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-017), [019](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-019)<br>**L07:** [039](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-039)<br>**L08:** [029](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-029), [039](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-039)<br>**L09:** [003](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-003), [004](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-004), [005](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-005), [006](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-006), [007](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-007), [008](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-008), [009](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-009), [013](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-013), [014](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-014), [015](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-015), [016](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-016), [019](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-019), [022](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-022), [023](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-023), [026](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-026)<br>**L10:** [017](../10_Test_Case_Library/L10-data-layer.md#tc-l10-017)<br>**L11:** [022](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-022)<br>**L12:** [014](../10_Test_Case_Library/L12-model-layer.md#tc-l12-014)<br>**L13:** [008](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-008)<br>**L14:** [008](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-008), [022](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-022)<br>**L15:** [010](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-010) |

### Data and Retrieval

<a id="ai-ctrl-017"></a>

#### AI-CTRL-017: Data Protection in AI Pipelines

| Field | Detail |
|---|---|
| **Control Objective** | Apply classification, minimization and isolation to data that AI systems ingest, process and produce. |
| **Applies To** | AI APIs / Custom AI Applications / Agents |
| **Risk Mapping** | [AI-R01](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R03](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R06](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Carry data classification into AI pipelines. Minimize or mask sensitive fields before they reach a model. Keep tenants separate in indexes, caches, memory and logs, and record data lineage. |
| **Evidence Required** | Data flow diagrams; classification and masking rules; tenant isolation tests; lineage records. |
| **Audit Test Procedure** | Send labelled sensitive records through the pipeline and confirm masking at each stage. Attempt to read another tenant's data through the AI interface. |
| **Control Owner** | Data Owner / Security Engineering |
| **Review Frequency** | Semi-annually |
| **OWASP** | LLM02:2025 Sensitive Information Disclosure |
| **MITRE ATLAS Techniques** | AML.T0057 LLM Data Leakage; AML.T0085 Data from AI Services; AML.T0025 Exfiltration via Cyber Means |
| **MITRE ATLAS Mitigations** | AML.M0012 Encrypt Sensitive Information; AML.M0005 Control Access to AI Models and Data at Rest |
| **NIST AI RMF** | MEASURE 2.10; MEASURE 2.7 |
| **ISO/IEC 42001** | A.4.3 Data resources; A.7.6 Data preparation |
| **Tested By (30 cases)** | **D08:** [023](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-023)<br>**D10:** [017](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-017)<br>**D11:** [022](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-022)<br>**L03:** [015](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-015), [018](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-018)<br>**L05:** [023](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-023)<br>**L08:** [040](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-040)<br>**L10:** [001](../10_Test_Case_Library/L10-data-layer.md#tc-l10-001), [002](../10_Test_Case_Library/L10-data-layer.md#tc-l10-002), [003](../10_Test_Case_Library/L10-data-layer.md#tc-l10-003), [004](../10_Test_Case_Library/L10-data-layer.md#tc-l10-004), [005](../10_Test_Case_Library/L10-data-layer.md#tc-l10-005), [007](../10_Test_Case_Library/L10-data-layer.md#tc-l10-007), [008](../10_Test_Case_Library/L10-data-layer.md#tc-l10-008), [009](../10_Test_Case_Library/L10-data-layer.md#tc-l10-009), [010](../10_Test_Case_Library/L10-data-layer.md#tc-l10-010), [011](../10_Test_Case_Library/L10-data-layer.md#tc-l10-011), [015](../10_Test_Case_Library/L10-data-layer.md#tc-l10-015), [016](../10_Test_Case_Library/L10-data-layer.md#tc-l10-016), [020](../10_Test_Case_Library/L10-data-layer.md#tc-l10-020), [023](../10_Test_Case_Library/L10-data-layer.md#tc-l10-023), [029](../10_Test_Case_Library/L10-data-layer.md#tc-l10-029)<br>**L11:** [007](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-007), [012](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-012), [015](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-015), [023](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-023)<br>**L13:** [006](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-006), [009](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-009)<br>**L14:** [015](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-015)<br>**L15:** [012](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-012) |

<a id="ai-ctrl-018"></a>

#### AI-CTRL-018: Retrieval Access Control

| Field | Detail |
|---|---|
| **Control Objective** | Return only content the requesting user is entitled to see. |
| **Applies To** | Custom AI Applications / Agents |
| **Risk Mapping** | [AI-R06](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Enforce document-level permissions at query time using the end user's identity. Propagate permission changes to the index promptly. Do not rely on the model to withhold content. Return citations that users can check. |
| **Evidence Required** | Permission test results; retrieval logs with source documents; propagation timing. |
| **Audit Test Procedure** | Query as users with different entitlements and confirm restricted documents are never retrieved. Revoke access to a document and measure how long it remains retrievable. |
| **Control Owner** | Application Owner |
| **Review Frequency** | Quarterly |
| **OWASP** | LLM08:2025 Vector and Embedding Weaknesses; LLM02:2025 Sensitive Information Disclosure |
| **MITRE ATLAS Techniques** | AML.T0057 LLM Data Leakage; AML.T0085 Data from AI Services; AML.T0064 Gather RAG-Indexed Targets; AML.T0082 RAG Credential Harvesting |
| **MITRE ATLAS Mitigations** | AML.M0027 Single-User AI Agent Permissions Configuration; AML.M0019 Control Access to AI Models and Data in Production |
| **NIST AI RMF** | MEASURE 2.10; MEASURE 2.7 |
| **ISO/IEC 42001** | None published in ISO/IEC 42001. The wiki's own identifier applies: AI-CTRL-018. |
| **Tested By (9 cases)** | **L10:** [006](../10_Test_Case_Library/L10-data-layer.md#tc-l10-006), [018](../10_Test_Case_Library/L10-data-layer.md#tc-l10-018), [019](../10_Test_Case_Library/L10-data-layer.md#tc-l10-019)<br>**L11:** [004](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-004), [005](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-005), [006](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-006), [007](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-007), [016](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-016), [019](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-019) |

<a id="ai-ctrl-019"></a>

#### AI-CTRL-019: Knowledge Base Integrity

| Field | Detail |
|---|---|
| **Control Objective** | Stop untrusted or poisoned content from entering the corpus that AI systems retrieve from. |
| **Applies To** | Custom AI Applications / Agents |
| **Risk Mapping** | [AI-R05](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Control who and what can write to the corpus. Record the source of every indexed item. Scan ingested content for embedded instructions, and keep the ability to find and remove items by source. |
| **Evidence Required** | Ingestion access list; provenance records; ingestion scan results; removal test. |
| **Audit Test Procedure** | Add a document with a planted instruction and a false fact through each ingestion path. Confirm it is detected or neutralized, and that it can be traced and removed. |
| **Control Owner** | Application Owner |
| **Review Frequency** | Quarterly |
| **OWASP** | LLM04:2025 Data and Model Poisoning; LLM08:2025 Vector and Embedding Weaknesses |
| **MITRE ATLAS Techniques** | AML.T0070 RAG Poisoning; AML.T0071 False RAG Entry Injection; AML.T0066 Retrieval Content Crafting |
| **MITRE ATLAS Mitigations** | AML.M0025 Maintain AI Dataset Provenance |
| **NIST AI RMF** | MEASURE 2.7; MAP 2.3 |
| **ISO/IEC 42001** | A.7.3 Acquisition of data; A.7.4 Quality of data for AI systems; A.7.5 Data provenance |
| **Tested By (12 cases)** | **L07:** [012](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-012)<br>**L10:** [024](../10_Test_Case_Library/L10-data-layer.md#tc-l10-024)<br>**L11:** [001](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-001), [008](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-008), [009](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-009), [010](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-010), [011](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-011), [013](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-013), [014](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-014), [017](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-017), [018](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-018), [021](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-021) |

### Application Runtime

<a id="ai-ctrl-005"></a>

#### AI-CTRL-005: Runtime AI Security

| Field | Detail |
|---|---|
| **Control Objective** | Protect custom AI applications from prompt injection, misuse and output leakage. |
| **Applies To** | Custom AI Applications / AI APIs |
| **Risk Mapping** | [AI-R05](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R06](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Inspect inputs and retrieved content for direct and indirect prompt injection and jailbreaks. Treat retrieved text as untrusted data. Protect the system prompt, and keep high-privilege tools out of sessions that read untrusted content. |
| **Evidence Required** | Prompt injection test reports; runtime logs; guardrail configuration; bypass test results. |
| **Audit Test Procedure** | Run the prompt injection and jailbreak cases with the control disabled and then enabled. Record attack success rate in both states against the agreed threshold. |
| **Control Owner** | AppSec |
| **Review Frequency** | Before each release and quarterly |
| **OWASP** | LLM01:2025 Prompt Injection; LLM07:2025 System Prompt Leakage; ASI01 Agent Goal Hijack |
| **MITRE ATLAS Techniques** | AML.T0051 LLM Prompt Injection; AML.T0054 LLM Jailbreak; AML.T0056 Extract LLM System Prompt; AML.T0068 LLM Prompt Obfuscation; AML.T0093 Prompt Infiltration via Public-Facing Application |
| **MITRE ATLAS Mitigations** | AML.M0020 Generative AI Guardrails; AML.M0021 Generative AI Guidelines; AML.M0033 Input and Output Validation for AI Agent Components |
| **NIST AI RMF** | MEASURE 2.7; MANAGE 1.3 |
| **ISO/IEC 42001** | A.6.2.4 AI system verification and validation; A.6.2.6 AI system operation and monitoring |
| **Tested By (52 cases)** | **D10:** [010](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-010), [011](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-011), [012](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-012)<br>**D11:** [002](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-002), [003](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-003), [012](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-012), [013](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-013)<br>**L05:** [012](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-012), [026](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-026)<br>**L06:** [020](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-020), [027](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-027)<br>**L07:** [001](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-001), [002](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-002), [003](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-003), [004](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-004), [005](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-005), [006](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-006), [007](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-007), [008](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-008), [009](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-009), [010](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-010), [011](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-011), [012](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-012), [013](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-013), [014](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-014), [015](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-015), [016](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-016), [017](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-017), [018](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-018), [019](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-019), [020](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-020), [021](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-021), [022](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-022), [023](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-023), [024](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-024), [025](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-025), [026](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-026), [031](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-031), [032](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-032), [033](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-033), [035](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-035), [036](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-036), [037](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-037), [039](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-039), [041](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-041)<br>**L08:** [015](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-015), [016](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-016), [019](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-019)<br>**L11:** [014](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-014), [020](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-020)<br>**L14:** [022](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-022)<br>**L16:** [016](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-016) |

<a id="ai-ctrl-020"></a>

#### AI-CTRL-020: Output Handling

| Field | Detail |
|---|---|
| **Control Objective** | Treat model output as untrusted input to whatever consumes it. |
| **Applies To** | Custom AI Applications / AI APIs / Agents |
| **Risk Mapping** | [AI-R05](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R06](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Validate and encode output before it is rendered, executed or passed to another system. Restrict what output can trigger, such as links, images and calls. Inspect responses for sensitive data. |
| **Evidence Required** | Output validation rules; response inspection logs; injection test results. |
| **Audit Test Procedure** | Induce the model to emit script, markup and command payloads and confirm none executes downstream. Confirm sensitive data in a response is detected. |
| **Control Owner** | AppSec |
| **Review Frequency** | Before each release and quarterly |
| **OWASP** | LLM05:2025 Improper Output Handling; LLM02:2025 Sensitive Information Disclosure |
| **MITRE ATLAS Techniques** | AML.T0077 LLM Response Rendering; AML.T0067 LLM Trusted Output Components Manipulation; AML.T0057 LLM Data Leakage |
| **MITRE ATLAS Mitigations** | AML.M0033 Input and Output Validation for AI Agent Components; AML.M0020 Generative AI Guardrails |
| **NIST AI RMF** | MEASURE 2.7; MEASURE 2.10 |
| **ISO/IEC 42001** | A.6.2.4 AI system verification and validation; A.6.2.6 AI system operation and monitoring |
| **Tested By (12 cases)** | **D11:** [021](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-021)<br>**L05:** [014](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-014), [015](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-015), [016](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-016), [017](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-017), [020](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-020), [022](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-022), [024](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-024)<br>**L06:** [030](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-030)<br>**L07:** [016](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-016)<br>**L08:** [020](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-020), [035](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-035) |

<a id="ai-ctrl-021"></a>

#### AI-CTRL-021: Multimodal and Voice Input Security

| Field | Detail |
|---|---|
| **Control Objective** | Apply the same inspection and policy to images, documents, audio and video as to text. |
| **Applies To** | Browser AI / Custom AI Applications / Agents |
| **Risk Mapping** | [AI-R03](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R05](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Inspect non-text inputs for sensitive content and hidden instructions. Do not treat voice as proof of identity for sensitive actions. Govern recordings and transcripts under the retention policy. |
| **Evidence Required** | Modality coverage matrix; detection results by modality; recording retention configuration. |
| **Audit Test Procedure** | Submit images, documents and audio carrying sensitive data and hidden instructions. Compare detection with the text-channel result for the same content. |
| **Control Owner** | AI Security Team |
| **Review Frequency** | Semi-annually |
| **OWASP** | LLM01:2025 Prompt Injection; LLM02:2025 Sensitive Information Disclosure |
| **MITRE ATLAS Techniques** | AML.T0129 Triggers in Multimodal Inputs; AML.T0051 LLM Prompt Injection; AML.T0088 Generate Deepfakes |
| **MITRE ATLAS Mitigations** | AML.M0034 Deepfake Detection; AML.M0020 Generative AI Guardrails |
| **NIST AI RMF** | MEASURE 2.7; MEASURE 2.10 |
| **ISO/IEC 42001** | A.6.2.4 AI system verification and validation |
| **Tested By (28 cases)** | **D11:** [001](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-001), [002](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-002), [003](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-003), [004](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-004), [005](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-005), [006](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-006), [007](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-007), [008](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-008), [009](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-009), [010](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-010), [011](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-011), [012](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-012), [013](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-013), [014](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-014), [015](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-015), [016](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-016), [017](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-017), [018](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-018), [019](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-019), [020](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-020), [021](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-021), [022](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-022)<br>**L04:** [020](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-020), [021](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-021), [022](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-022)<br>**L07:** [014](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-014), [023](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-023)<br>**L08:** [013](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-013) |

<a id="ai-ctrl-039"></a>

#### AI-CTRL-039: Output Reliability and Content Safety

| Field | Detail |
|---|---|
| **Control Objective** | Keep AI output grounded, within its approved scope and free of harmful content. |
| **Applies To** | Custom AI Applications / AI APIs / IDE AI |
| **Risk Mapping** | [AI-R12](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Ground answers in approved sources and verify citations. Restrict assistants to their approved topics. Filter harmful and policy-violating output. Detect fabricated packages, links and references before users act on them, and measure factual accuracy against a baseline. |
| **Evidence Required** | Grounding and citation test results; topic policy; harmful content filter results; factuality baseline. |
| **Audit Test Procedure** | Ask questions the sources cannot answer and confirm the assistant says so. Confirm fabricated package names and links are flagged, and off-topic requests are refused. |
| **Control Owner** | Application Owner / AppSec |
| **Review Frequency** | Before each release and quarterly |
| **OWASP** | LLM09:2025 Misinformation |
| **MITRE ATLAS Techniques** | AML.T0062 Discover LLM Hallucinations; AML.T0060 Publish Hallucinated Entities; AML.T0048 External Harms |
| **MITRE ATLAS Mitigations** | AML.M0020 Generative AI Guardrails; AML.M0022 Generative AI Model Alignment |
| **NIST AI RMF** | MEASURE 2.5; MEASURE 2.6; MAP 2.2 |
| **ISO/IEC 42001** | A.6.2.4 AI system verification and validation; A.8.2 System documentation and information for users |
| **Tested By (6 cases)** | **L05:** [018](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-018), [019](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-019), [021](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-021)<br>**L08:** [017](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-017), [018](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-018)<br>**L12:** [017](../10_Test_Case_Library/L12-model-layer.md#tc-l12-017) |

### Agents and Tools

<a id="ai-ctrl-006"></a>

#### AI-CTRL-006: Agent Governance

| Field | Detail |
|---|---|
| **Control Objective** | Monitor AI agents, tool calls, API access and autonomous actions. |
| **Applies To** | Agents |
| **Risk Mapping** | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Keep a registry of every agent with its owner, purpose, model, tools, data scope and approval status. Monitor decisions, tool calls and delegation chains, and detect unregistered agents. |
| **Evidence Required** | Agent registry; tool access logs; delegation maps; shadow agent reports. |
| **Audit Test Procedure** | Deploy registered and unregistered test agents. Confirm the unregistered agents are detected, and that owner, tools and data scope are correct for the registered ones. |
| **Control Owner** | AI Platform Team |
| **Review Frequency** | Quarterly |
| **OWASP** | LLM06:2025 Excessive Agency; ASI10 Rogue Agents |
| **MITRE ATLAS Techniques** | AML.T0081 Modify AI Agent Configuration |
| **MITRE ATLAS Mitigations** | AML.M0038 AI Agent Scope Drift Detection; AML.M0024 AI Telemetry Logging |
| **NIST AI RMF** | GOVERN 1.6; MEASURE 2.4 |
| **ISO/IEC 42001** | A.4.2 Resource documentation; A.6.2.6 AI system operation and monitoring |
| **Tested By (13 cases)** | **D09:** [020](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-020)<br>**D10:** [001](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-001), [023](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-023)<br>**L04:** [023](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-023)<br>**L06:** [001](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-001), [002](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-002), [003](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-003), [004](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-004), [017](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-017), [029](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-029), [034](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-034), [035](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-035)<br>**L17:** [012](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-012) |

<a id="ai-ctrl-022"></a>

#### AI-CTRL-022: Deterministic Action Authorization

| Field | Detail |
|---|---|
| **Control Objective** | Enforce authority to act, access data or spend money outside the model. |
| **Applies To** | Agents / Custom AI Applications |
| **Risk Mapping** | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Place a policy enforcement point between the model and every tool. It authorizes each call with deterministic rules using the real parameters, the acting identity and the end user's rights. Model output is advice, never authority. |
| **Evidence Required** | Policy rules; allow and deny logs; architecture review record. |
| **Audit Test Procedure** | Instruct a test agent, through injected content, to make a call the policy forbids. Confirm the enforcement point denies it regardless of what the model outputs. |
| **Control Owner** | Security Architecture |
| **Review Frequency** | Semi-annually |
| **OWASP** | LLM06:2025 Excessive Agency; ASI02 Tool Misuse & Exploitation |
| **MITRE ATLAS Techniques** | AML.T0053 AI Agent Tool Invocation; AML.T0086 Exfiltration via AI Agent Tool Invocation; AML.T0101 Data Destruction via AI Agent Tool Invocation |
| **MITRE ATLAS Mitigations** | AML.M0028 AI Agent Tools Permissions Configuration; AML.M0030 Restrict AI Agent Tool Invocation on Untrusted Data; AML.M0033 Input and Output Validation for AI Agent Components |
| **NIST AI RMF** | MEASURE 2.7; MANAGE 1.3 |
| **ISO/IEC 42001** | A.6.2.2 AI system requirements and specification |
| **Tested By (16 cases)** | **D09:** [010](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-010)<br>**D10:** [004](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-004), [005](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-005), [006](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-006), [007](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-007), [012](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-012), [014](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-014)<br>**L05:** [022](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-022)<br>**L06:** [011](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-011), [014](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-014), [019](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-019), [024](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-024), [033](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-033), [036](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-036)<br>**L07:** [008](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-008)<br>**L09:** [006](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-006) |

<a id="ai-ctrl-023"></a>

#### AI-CTRL-023: Human Approval for Sensitive Actions

| Field | Detail |
|---|---|
| **Control Objective** | Require a person to approve irreversible or high-impact actions before they run. |
| **Applies To** | Agents |
| **Risk Mapping** | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Define which actions need approval. Show the approver the real parameters and the consequence, not a model-written summary. Record the decision, and guard against approval fatigue by keeping the set of gated actions small. |
| **Evidence Required** | List of gated actions; approval logs with parameters shown; rejection samples. |
| **Audit Test Procedure** | Trigger a gated action and confirm it does not run without approval. Confirm the approver sees the real parameters and that the decision is logged. |
| **Control Owner** | Application Owner |
| **Review Frequency** | Semi-annually |
| **OWASP** | LLM06:2025 Excessive Agency; ASI09 Human-Agent Trust Exploitation |
| **MITRE ATLAS Techniques** | AML.T0053 AI Agent Tool Invocation; AML.T0101 Data Destruction via AI Agent Tool Invocation |
| **MITRE ATLAS Mitigations** | AML.M0029 Human In-the-Loop for AI Agent Actions |
| **NIST AI RMF** | MAP 3.5; GOVERN 3.2 |
| **ISO/IEC 42001** | A.9.2 Processes for responsible use of AI systems; A.9.3 Objectives for responsible use of AI system |
| **Tested By (7 cases)** | **D10:** [006](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-006), [013](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-013)<br>**L01:** [012](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-012)<br>**L06:** [015](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-015), [016](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-016)<br>**L07:** [038](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-038)<br>**L09:** [012](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-012) |

<a id="ai-ctrl-024"></a>

#### AI-CTRL-024: Tool and MCP Server Governance

| Field | Detail |
|---|---|
| **Control Objective** | Allow agents to use only vetted tools and tool servers, and detect when they change. |
| **Applies To** | Agents / IDE AI |
| **Risk Mapping** | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Keep an allow-list of tools, plugins and MCP servers with an owner for each. Validate tool schemas, pin versions, and re-approve when a tool definition changes after approval. |
| **Evidence Required** | Tool and MCP server registry; allow-list configuration; change detection alerts. |
| **Audit Test Procedure** | Connect an unlisted tool server and confirm it is blocked. Change the description of an approved tool and confirm the change is detected before use. |
| **Control Owner** | AI Platform Team |
| **Review Frequency** | Quarterly |
| **OWASP** | LLM03:2025 Supply Chain; ASI04 Agentic Supply Chain Vulnerabilities; ASI02 Tool Misuse & Exploitation |
| **MITRE ATLAS Techniques** | AML.T0110 AI Agent Tool Poisoning; AML.T0109 AI Supply Chain Rug Pull; AML.T0099 AI Agent Tool Data Poisoning; AML.T0010 AI Supply Chain Compromise |
| **MITRE ATLAS Mitigations** | AML.M0028 AI Agent Tools Permissions Configuration; AML.M0014 Verify AI Artifacts |
| **NIST AI RMF** | GOVERN 6.1; MAP 4.1; MAP 4.2; MANAGE 3.1 |
| **ISO/IEC 42001** | A.10.3 Suppliers; A.4.4 Tooling resources |
| **Tested By (14 cases)** | **D10:** [022](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-022)<br>**L06:** [005](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-005), [006](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-006), [007](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-007), [008](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-008), [009](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-009), [010](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-010), [011](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-011), [012](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-012), [013](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-013), [032](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-032), [037](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-037)<br>**L16:** [015](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-015), [026](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-026) |

<a id="ai-ctrl-025"></a>

#### AI-CTRL-025: Agent Containment and Kill Switch

| Field | Detail |
|---|---|
| **Control Objective** | Stop an agent, revoke its access and limit the damage within minutes. |
| **Applies To** | Agents |
| **Risk Mapping** | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R11](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Provide a tested way to stop a single agent and to revoke credentials for all agents. Set limits on steps, time and spend per task. Know which actions can be rolled back and how. |
| **Evidence Required** | Kill switch procedure; test records with timings; task limits configuration. |
| **Audit Test Procedure** | Start a long-running test agent and stop it. Measure the time until no further actions occur and credentials are invalid. |
| **Control Owner** | AI Platform Team / SOC |
| **Review Frequency** | Semi-annually |
| **OWASP** | LLM06:2025 Excessive Agency; ASI08 Cascading Failures; ASI10 Rogue Agents |
| **MITRE ATLAS Techniques** | AML.T0053 AI Agent Tool Invocation; AML.T0034 Cost Harvesting |
| **MITRE ATLAS Mitigations** | AML.M0037 AI Agent Authority Expansion Controls; AML.M0036 Limit AI Workload Resource Consumption |
| **NIST AI RMF** | MANAGE 2.4; MANAGE 2.3 |
| **ISO/IEC 42001** | A.6.2.6 AI system operation and monitoring |
| **Tested By (10 cases)** | **D09:** [016](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-016)<br>**D10:** [019](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-019), [020](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-020)<br>**D12:** [011](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-011)<br>**D13:** [009](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-009)<br>**L06:** [021](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-021), [022](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-022), [023](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-023), [024](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-024)<br>**L17:** [019](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-019) |

<a id="ai-ctrl-026"></a>

#### AI-CTRL-026: Agent Memory and Context Integrity

| Field | Detail |
|---|---|
| **Control Objective** | Prevent poisoned or cross-user content from persisting in agent memory and context. |
| **Applies To** | Agents / Custom AI Applications |
| **Risk Mapping** | [AI-R05](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Separate memory by user and tenant. Record the source of each memory item, apply expiry, and provide a way to inspect and purge memory. Do not let untrusted content write to long-term memory unchecked. |
| **Evidence Required** | Memory isolation tests; memory provenance records; purge procedure and test. |
| **Audit Test Procedure** | Plant an instruction in memory through untrusted content and confirm it does not affect a later session. Confirm one user cannot read another's memory. |
| **Control Owner** | Application Owner |
| **Review Frequency** | Semi-annually |
| **OWASP** | LLM04:2025 Data and Model Poisoning; LLM01:2025 Prompt Injection; ASI06 Memory & Context Poisoning |
| **MITRE ATLAS Techniques** | AML.T0080 AI Agent Context Poisoning; AML.T0092 Manipulate User LLM Chat History; AML.T0094 Delay Execution of LLM Instructions |
| **MITRE ATLAS Mitigations** | AML.M0031 Memory Hardening |
| **NIST AI RMF** | MEASURE 2.7; MEASURE 2.10 |
| **ISO/IEC 42001** | A.6.2.6 AI system operation and monitoring |
| **Tested By (5 cases)** | **L07:** [027](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-027), [028](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-028), [029](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-029), [030](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-030), [035](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-035) |

<a id="ai-ctrl-027"></a>

#### AI-CTRL-027: Agent Execution Isolation

| Field | Detail |
|---|---|
| **Control Objective** | Run agent-generated code and browser or computer-use sessions in isolation. |
| **Applies To** | Agents |
| **Risk Mapping** | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Execute generated code in a sandbox with no network, filesystem or secrets access by default. Run browser and computer-use agents in a separate profile or container with their own credentials and sessions. |
| **Evidence Required** | Sandbox configuration; egress rules; isolation test results. |
| **Audit Test Procedure** | Have a test agent run code that tries to reach the network, read secrets and write outside its workspace. Confirm each attempt fails and is logged. |
| **Control Owner** | Platform Engineering |
| **Review Frequency** | Semi-annually |
| **OWASP** | LLM06:2025 Excessive Agency; ASI05 Unexpected Code Execution (RCE) |
| **MITRE ATLAS Techniques** | AML.T0050 Command and Scripting Interpreter; AML.T0105 Escape to Host; AML.T0102 Generate Malicious Commands |
| **MITRE ATLAS Mitigations** | AML.M0032 Segmentation of AI Agent Components; AML.M0011 Restrict Library Loading |
| **NIST AI RMF** | MEASURE 2.7; MANAGE 1.3 |
| **ISO/IEC 42001** | A.4.5 System and computing resources; A.6.2.5 AI system deployment |
| **Tested By (10 cases)** | **D10:** [002](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-002), [003](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-003), [008](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-008), [009](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-009), [016](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-016), [021](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-021)<br>**L06:** [025](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-025), [026](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-026), [031](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-031), [036](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-036) |

### Model, Training and Pipeline

<a id="ai-ctrl-028"></a>

#### AI-CTRL-028: Model Protection

| Field | Detail |
|---|---|
| **Control Objective** | Protect models from theft, extraction and adversarial inputs. |
| **Applies To** | Custom AI Applications / AI APIs |
| **Risk Mapping** | [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Restrict access to model weights and encrypt them at rest. Limit and monitor inference queries for extraction patterns. Scan models before use, and test robustness for models that make security or safety decisions. |
| **Evidence Required** | Model access list; query monitoring rules; model scan reports; robustness test results. |
| **Audit Test Procedure** | Run a scripted extraction pattern against a test endpoint and confirm it is detected and throttled. Attempt to read model weights with a non-privileged identity. |
| **Control Owner** | ML Engineering |
| **Review Frequency** | Semi-annually |
| **OWASP** | LLM10:2025 Unbounded Consumption; LLM02:2025 Sensitive Information Disclosure |
| **MITRE ATLAS Techniques** | AML.T0024 Exfiltration via AI Inference API; AML.T0043 Craft Adversarial Data; AML.T0015 Evade AI Model; AML.T0044 Full AI Model Access; AML.T0018 Manipulate AI Model |
| **MITRE ATLAS Mitigations** | AML.M0004 Limit AI Service Query Volume and Rate; AML.M0005 Control Access to AI Models and Data at Rest; AML.M0003 Predictive AI Model Hardening; AML.M0015 Predictive AI Adversarial Input Detection; AML.M0008 Validate AI Model |
| **NIST AI RMF** | MEASURE 2.7; MEASURE 2.5 |
| **ISO/IEC 42001** | A.6.2.4 AI system verification and validation; A.6.2.6 AI system operation and monitoring |
| **Tested By (16 cases)** | **D11:** [004](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-004)<br>**L12:** [002](../10_Test_Case_Library/L12-model-layer.md#tc-l12-002), [003](../10_Test_Case_Library/L12-model-layer.md#tc-l12-003), [004](../10_Test_Case_Library/L12-model-layer.md#tc-l12-004), [007](../10_Test_Case_Library/L12-model-layer.md#tc-l12-007), [008](../10_Test_Case_Library/L12-model-layer.md#tc-l12-008), [009](../10_Test_Case_Library/L12-model-layer.md#tc-l12-009), [010](../10_Test_Case_Library/L12-model-layer.md#tc-l12-010), [011](../10_Test_Case_Library/L12-model-layer.md#tc-l12-011), [012](../10_Test_Case_Library/L12-model-layer.md#tc-l12-012), [013](../10_Test_Case_Library/L12-model-layer.md#tc-l12-013), [015](../10_Test_Case_Library/L12-model-layer.md#tc-l12-015), [024](../10_Test_Case_Library/L12-model-layer.md#tc-l12-024)<br>**L13:** [017](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-017)<br>**L15:** [011](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-011)<br>**L16:** [005](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-005) |

<a id="ai-ctrl-029"></a>

#### AI-CTRL-029: Training and Fine-Tuning Data Integrity

| Field | Detail |
|---|---|
| **Control Objective** | Know where training data came from and detect tampering before it shapes a model. |
| **Applies To** | Custom AI Applications |
| **Risk Mapping** | [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Record provenance for every dataset. Verify integrity before each training or fine-tuning run. Screen data for sensitive content and poisoning, and keep the ability to trace a model back to its data. |
| **Evidence Required** | Dataset provenance records; integrity checks; screening results; model-to-data lineage. |
| **Audit Test Procedure** | Alter a sample of a test dataset and confirm the integrity check fails the run. Trace a deployed model back to the exact dataset versions used. |
| **Control Owner** | ML Engineering / Data Owner |
| **Review Frequency** | Before each training run |
| **OWASP** | LLM04:2025 Data and Model Poisoning |
| **MITRE ATLAS Techniques** | AML.T0020 Training Data Poisoning; AML.T0059 Erode Dataset Integrity |
| **MITRE ATLAS Mitigations** | AML.M0007 Sanitize Training Data; AML.M0025 Maintain AI Dataset Provenance |
| **NIST AI RMF** | MAP 2.3; MAP 4.1; MEASURE 2.7; MEASURE 2.10 |
| **ISO/IEC 42001** | A.7.2 Data for development and enhancement of AI system; A.7.3 Acquisition of data; A.7.4 Quality of data for AI systems; A.7.5 Data provenance |
| **Tested By (15 cases)** | **D12:** [013](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-013)<br>**L13:** [001](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-001), [002](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-002), [003](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-003), [004](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-004), [005](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-005), [006](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-006), [007](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-007), [008](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-008), [013](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-013), [014](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-014), [015](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-015), [016](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-016), [018](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-018)<br>**L14:** [014](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-014) |

<a id="ai-ctrl-030"></a>

#### AI-CTRL-030: ML Pipeline and Model Registry Security

| Field | Detail |
|---|---|
| **Control Objective** | Protect the pipeline that builds, stores and releases models and prompts. |
| **Applies To** | Custom AI Applications |
| **Risk Mapping** | [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Sign model artifacts and verify signatures at deployment. Restrict who can write to the registry. Gate releases on security tests, and version models, prompts and configuration together. |
| **Evidence Required** | Signing configuration; registry access list; release gate results; version history. |
| **Audit Test Procedure** | Attempt to deploy an unsigned or altered artifact and confirm it is rejected. Confirm a failed security test blocks a release. |
| **Control Owner** | MLOps / DevSecOps |
| **Review Frequency** | Semi-annually |
| **OWASP** | LLM03:2025 Supply Chain; LLM04:2025 Data and Model Poisoning |
| **MITRE ATLAS Techniques** | AML.T0010 AI Supply Chain Compromise; AML.T0018 Manipulate AI Model; AML.T0119 Exploit Automated Artifact Processing Pipeline |
| **MITRE ATLAS Mitigations** | AML.M0013 Code Signing; AML.M0014 Verify AI Artifacts |
| **NIST AI RMF** | MEASURE 2.7; MAP 4.2 |
| **ISO/IEC 42001** | A.6.2.5 AI system deployment; A.6.2.3 Documentation of AI system design and development |
| **Tested By (16 cases)** | **D08:** [020](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-020)<br>**L07:** [034](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-034)<br>**L12:** [004](../10_Test_Case_Library/L12-model-layer.md#tc-l12-004), [023](../10_Test_Case_Library/L12-model-layer.md#tc-l12-023)<br>**L13:** [012](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-012), [013](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-013)<br>**L14:** [001](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-001), [002](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-002), [003](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-003), [004](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-004), [005](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-005), [012](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-012), [013](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-013), [014](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-014), [018](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-018), [019](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-019) |

### Supply Chain, Infrastructure and Resilience

<a id="ai-ctrl-031"></a>

#### AI-CTRL-031: AI Supply Chain and AI-BOM

| Field | Detail |
|---|---|
| **Control Objective** | Know exactly which models, datasets, packages and prompts run in each environment. |
| **Applies To** | Custom AI Applications / Agents / IDE AI / Vendors |
| **Risk Mapping** | [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Maintain an AI bill of materials per system. Take models and packages only from approved sources, verify provenance, and scan them. Re-run security tests when any component changes, including a provider-side model update. |
| **Evidence Required** | AI-BOM; approved source list; scan reports; change-triggered test records. |
| **Audit Test Procedure** | Compare the AI-BOM of a sampled system with what is deployed. Introduce a component from an unapproved source and confirm it is blocked or flagged. |
| **Control Owner** | DevSecOps |
| **Review Frequency** | Quarterly |
| **OWASP** | LLM03:2025 Supply Chain |
| **MITRE ATLAS Techniques** | AML.T0010 AI Supply Chain Compromise; AML.T0109 AI Supply Chain Rug Pull; AML.T0115 Publish Poisoned AI Artifacts; AML.T0111 AI Supply Chain Reputation Inflation |
| **MITRE ATLAS Mitigations** | AML.M0023 AI Bill of Materials; AML.M0014 Verify AI Artifacts; AML.M0016 Vulnerability Scanning |
| **NIST AI RMF** | GOVERN 6.1; MAP 4.1; MANAGE 3.1; MANAGE 3.2 |
| **ISO/IEC 42001** | A.10.3 Suppliers; A.4.2 Resource documentation; A.7.5 Data provenance |
| **Tested By (24 cases)** | **L05:** [019](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-019)<br>**L08:** [028](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-028), [042](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-042)<br>**L12:** [001](../10_Test_Case_Library/L12-model-layer.md#tc-l12-001), [002](../10_Test_Case_Library/L12-model-layer.md#tc-l12-002), [005](../10_Test_Case_Library/L12-model-layer.md#tc-l12-005), [006](../10_Test_Case_Library/L12-model-layer.md#tc-l12-006), [018](../10_Test_Case_Library/L12-model-layer.md#tc-l12-018), [019](../10_Test_Case_Library/L12-model-layer.md#tc-l12-019)<br>**L13:** [014](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-014)<br>**L14:** [009](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-009)<br>**L16:** [001](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-001), [002](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-002), [003](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-003), [004](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-004), [005](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-005), [006](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-006), [007](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-007), [013](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-013), [014](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-014), [015](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-015), [016](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-016), [017](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-017), [024](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-024) |

<a id="ai-ctrl-032"></a>

#### AI-CTRL-032: AI Infrastructure Hardening

| Field | Detail |
|---|---|
| **Control Objective** | Harden and segment the infrastructure that trains and serves models. |
| **Applies To** | Custom AI Applications |
| **Risk Mapping** | [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R10](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Separate experimentation, training, evaluation and production. Isolate model runtimes at the network level and allow only required egress. Manage secrets centrally, and isolate tenants on shared GPUs. |
| **Evidence Required** | Network segmentation rules; secrets management configuration; hardening baseline; isolation tests. |
| **Audit Test Procedure** | Attempt to reach production data from the experimentation environment and to open unapproved egress from a model runtime. Confirm both fail. |
| **Control Owner** | Platform Engineering |
| **Review Frequency** | Semi-annually |
| **OWASP** | LLM03:2025 Supply Chain |
| **MITRE ATLAS Techniques** | AML.T0049 Exploit Public-Facing Application; AML.T0132 Misconfigured or Publicly Exposed AI Services; AML.T0055 Unsecured Credentials; AML.T0025 Exfiltration via Cyber Means |
| **MITRE ATLAS Mitigations** | AML.M0005 Control Access to AI Models and Data at Rest; AML.M0012 Encrypt Sensitive Information; AML.M0016 Vulnerability Scanning; AML.M0019 Control Access to AI Models and Data in Production |
| **NIST AI RMF** | MEASURE 2.7; MAP 4.2 |
| **ISO/IEC 42001** | A.4.5 System and computing resources |
| **Tested By (26 cases)** | **L09:** [019](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-019)<br>**L10:** [023](../10_Test_Case_Library/L10-data-layer.md#tc-l10-023)<br>**L11:** [002](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-002), [003](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-003)<br>**L12:** [020](../10_Test_Case_Library/L12-model-layer.md#tc-l12-020)<br>**L13:** [011](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-011)<br>**L14:** [006](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-006), [007](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-007), [010](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-010), [011](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-011), [020](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-020)<br>**L15:** [001](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-001), [002](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-002), [003](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-003), [004](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-004), [005](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-005), [006](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-006), [007](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-007), [008](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-008), [009](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-009), [010](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-010), [011](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-011), [012](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-012), [015](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-015), [016](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-016)<br>**L16:** [017](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-017) |

<a id="ai-ctrl-040"></a>

#### AI-CTRL-040: AI Service Resilience and Fail-Safe Operation

| Field | Detail |
|---|---|
| **Control Objective** | Keep AI services and their security controls available, and make them fail safely. |
| **Applies To** | AI APIs / Custom AI Applications / Agents / Vendors |
| **Risk Mapping** | [AI-R13](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Decide for each control whether it fails open or closed, and test it. Measure the latency and quality cost of controls so that teams do not remove them. Provide failover that keeps guardrails, residency and logging intact. Keep tested fallback paths for AI-dependent processes, tested backups and an exit plan for each provider. Detect silent failure of controls. |
| **Evidence Required** | Fail-mode test results; latency and load measurements; failover and restore tests; continuity and exit plans; health monitoring alerts. |
| **Audit Test Procedure** | Disable the protection layer in the lab and confirm the documented fail mode. Fail over to the secondary model or region and confirm policy, logging and residency still hold. |
| **Control Owner** | Platform Engineering / Application Owner |
| **Review Frequency** | Semi-annually |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-040. |
| **MITRE ATLAS Techniques** | AML.T0029 Denial of AI Service |
| **MITRE ATLAS Mitigations** | AML.M0036 Limit AI Workload Resource Consumption |
| **NIST AI RMF** | MEASURE 2.7; GOVERN 6.2; MANAGE 2.3 |
| **ISO/IEC 42001** | A.6.2.6 AI system operation and monitoring; A.4.5 System and computing resources |
| **Tested By (13 cases)** | **L01:** [018](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-018)<br>**L05:** [013](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-013), [030](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-030)<br>**L08:** [032](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-032), [033](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-033), [034](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-034), [035](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-035)<br>**L11:** [025](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-025)<br>**L12:** [021](../10_Test_Case_Library/L12-model-layer.md#tc-l12-021)<br>**L15:** [019](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-019)<br>**L16:** [012](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-012), [020](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-020)<br>**L17:** [028](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-028) |

### Assurance and Testing

<a id="ai-ctrl-033"></a>

#### AI-CTRL-033: AI Security Review and Release Gate

| Field | Detail |
|---|---|
| **Control Objective** | Review every AI system against its threats before production and after material change. |
| **Applies To** | Custom AI Applications / Agents / Vendors |
| **Risk Mapping** | [AI-R05](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Threat model each system: assets, trust boundaries, worst-case output and maximum damage. Select controls from this library by risk tier. Record open risks and exceptions, and require sign-off before release. |
| **Evidence Required** | Threat models; architecture review records; control selection; approvals and exceptions. |
| **Audit Test Procedure** | Sample production systems and confirm each has a current threat model, a control selection that matches its tier and a signed approval. |
| **Control Owner** | Security Architecture |
| **Review Frequency** | Before each release and annually |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-033. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-033. |
| **MITRE ATLAS Mitigations** | None published in MITRE ATLAS mitigations. The wiki's own identifier applies: AI-CTRL-033. |
| **NIST AI RMF** | MANAGE 1.1; GOVERN 4.2; MEASURE 2.7 |
| **ISO/IEC 42001** | A.5.2 AI system impact assessment process; A.6.2.2 AI system requirements and specification; A.6.2.4 AI system verification and validation; A.6.2.5 AI system deployment |
| **Tested By (6 cases)** | **L01:** [002](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-002), [013](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-013), [014](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-014), [015](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-015)<br>**L06:** [034](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-034)<br>**L14:** [012](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-012) |

<a id="ai-ctrl-034"></a>

#### AI-CTRL-034: Adversarial Testing and Continuous Evaluation

| Field | Detail |
|---|---|
| **Control Objective** | Test AI systems against attacks before release and continuously afterwards. |
| **Applies To** | Custom AI Applications / Agents |
| **Risk Mapping** | [AI-R05](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Red team each system against defined threat cases before release. Run a regression suite in the pipeline and whenever the model, prompt, tools or data change. The risk owner sets the acceptable attack success rate in writing. |
| **Evidence Required** | Red team reports; regression suite results; agreed thresholds; retest records. |
| **Audit Test Procedure** | Confirm the last model or prompt change triggered the regression suite. Reproduce a sample of reported findings and confirm fixes hold. |
| **Control Owner** | AI Red Team / AppSec |
| **Review Frequency** | Before each release and continuously |
| **OWASP** | LLM01:2025 Prompt Injection; LLM02:2025 Sensitive Information Disclosure; LLM03:2025 Supply Chain; LLM04:2025 Data and Model Poisoning; LLM05:2025 Improper Output Handling; LLM06:2025 Excessive Agency; LLM07:2025 System Prompt Leakage; LLM08:2025 Vector and Embedding Weaknesses; LLM09:2025 Misinformation; LLM10:2025 Unbounded Consumption |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-034. |
| **MITRE ATLAS Mitigations** | AML.M0035 AI Red Team |
| **NIST AI RMF** | MEASURE 2.7; MEASURE 2.6; MEASURE 2.1; GOVERN 4.3 |
| **ISO/IEC 42001** | A.6.2.4 AI system verification and validation |
| **Tested By (36 cases)** | **D08:** [001](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-001), [002](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-002), [003](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-003), [004](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-004), [005](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-005), [006](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-006), [007](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-007), [008](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-008), [009](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-009), [010](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-010), [011](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-011), [012](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-012), [013](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-013), [014](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-014), [015](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-015), [016](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-016), [017](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-017), [018](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-018), [019](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-019), [020](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-020), [021](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-021), [022](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-022), [023](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-023), [024](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-024), [025](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-025)<br>**D12:** [014](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-014)<br>**L05:** [027](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-027)<br>**L07:** [024](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-024), [040](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-040)<br>**L12:** [016](../10_Test_Case_Library/L12-model-layer.md#tc-l12-016), [018](../10_Test_Case_Library/L12-model-layer.md#tc-l12-018)<br>**L13:** [010](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-010)<br>**L14:** [002](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-002), [016](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-016), [017](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-017)<br>**L17:** [029](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-029) |

<a id="ai-ctrl-038"></a>

#### AI-CTRL-038: Control Assurance and Audit Evidence

| Field | Detail |
|---|---|
| **Control Objective** | Show, with current evidence, that each AI control is operating and that findings are closed. |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents / Vendors |
| **Risk Mapping** | [AI-R09](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Measure control effectiveness on a schedule. Collect evidence automatically where possible and record its age. Have control owners attest periodically. Track findings to verified closure, and protect governance records from silent change. |
| **Evidence Required** | Control effectiveness results; evidence packs with collection dates; owner attestations; findings log; record change history. |
| **Audit Test Procedure** | Request an evidence pack for a sampled control at short notice and check that the evidence is current. Confirm a closed finding was verified before closure. |
| **Control Owner** | GRC / Internal Audit |
| **Review Frequency** | Quarterly |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-038. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-038. |
| **MITRE ATLAS Mitigations** | None published in MITRE ATLAS mitigations. The wiki's own identifier applies: AI-CTRL-038. |
| **NIST AI RMF** | GOVERN 1.5; MEASURE 1.2; MEASURE 1.3; MANAGE 4.2 |
| **ISO/IEC 42001** | Clause 9.1 Monitoring, measurement, analysis and evaluation; Clause 9.2 Internal audit; Clause 9.3 Management review; Clause 10.2 Nonconformity and corrective action |
| **Tested By (17 cases)** | **D09:** [019](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-019)<br>**L02:** [003](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-003), [013](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-013), [014](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-014), [015](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-015), [016](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-016), [017](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-017), [018](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-018), [019](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-019), [024](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-024), [025](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-025)<br>**L03:** [022](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-022), [023](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-023), [024](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-024), [025](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-025), [026](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-026)<br>**L10:** [030](../10_Test_Case_Library/L10-data-layer.md#tc-l10-030) |

### Detection and Response

<a id="ai-ctrl-008"></a>

#### AI-CTRL-008: Auditability

| Field | Detail |
|---|---|
| **Control Objective** | Maintain logs for prompts, responses, files, users, devices, applications and actions. |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents |
| **Risk Mapping** | [AI-R09](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Log prompts, responses, uploads, retrieved sources, model calls, tool calls and policy decisions according to policy. Records must be timestamped, attributable, exportable and retained for the approved period. |
| **Evidence Required** | Exportable audit records; log schema; retention policy; sample reconstruction. |
| **Audit Test Procedure** | Pick a completed test interaction and reconstruct it from logs alone: who, what was sent, what was retrieved, what the model returned and what action followed. |
| **Control Owner** | Security Engineering |
| **Review Frequency** | Semi-annually |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-008. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-008. |
| **MITRE ATLAS Mitigations** | AML.M0024 AI Telemetry Logging |
| **NIST AI RMF** | MEASURE 2.4; MEASURE 2.8; MANAGE 4.1 |
| **ISO/IEC 42001** | A.6.2.8 AI system recording of event logs |
| **Tested By (19 cases)** | **D09:** [012](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-012)<br>**D10:** [018](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-018)<br>**D12:** [006](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-006)<br>**L02:** [025](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-025)<br>**L05:** [025](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-025)<br>**L06:** [028](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-028)<br>**L08:** [040](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-040)<br>**L09:** [025](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-025)<br>**L10:** [026](../10_Test_Case_Library/L10-data-layer.md#tc-l10-026)<br>**L11:** [024](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-024)<br>**L14:** [019](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-019)<br>**L15:** [018](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-018)<br>**L17:** [001](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-001), [002](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-002), [004](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-004), [005](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-005), [020](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-020), [030](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-030), [031](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-031) |

<a id="ai-ctrl-009"></a>

#### AI-CTRL-009: SOC Integration

| Field | Detail |
|---|---|
| **Control Objective** | Forward AI security events and logs to monitoring and response platforms. |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents |
| **Risk Mapping** | [AI-R09](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Forward AI security events to the SIEM with a documented schema. Build detections and runbooks for AI-specific events, and correlate them with identity, endpoint and network telemetry. |
| **Evidence Required** | SIEM event IDs; parser mapping; detection rules; runbooks; alert samples. |
| **Audit Test Procedure** | Trigger each AI event type in the lab and confirm it arrives in the SIEM within the stated time, parses correctly and raises the expected alert. |
| **Control Owner** | SOC |
| **Review Frequency** | Semi-annually |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-009. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-009. |
| **MITRE ATLAS Mitigations** | AML.M0024 AI Telemetry Logging |
| **NIST AI RMF** | MEASURE 2.4; MEASURE 3.1; MANAGE 4.1 |
| **ISO/IEC 42001** | A.6.2.6 AI system operation and monitoring; A.6.2.8 AI system recording of event logs |
| **Tested By (22 cases)** | **L06:** [029](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-029)<br>**L07:** [037](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-037)<br>**L09:** [017](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-017)<br>**L14:** [016](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-016)<br>**L17:** [001](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-001), [003](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-003), [006](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-006), [007](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-007), [008](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-008), [009](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-009), [010](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-010), [011](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-011), [012](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-012), [013](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-013), [014](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-014), [015](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-015), [016](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-016), [024](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-024), [025](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-025), [027](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-027), [028](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-028), [029](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-029) |

<a id="ai-ctrl-035"></a>

#### AI-CTRL-035: AI Incident Response and Forensics

| Field | Detail |
|---|---|
| **Control Objective** | Detect, contain, investigate and recover from AI security incidents. |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents / Vendors |
| **Risk Mapping** | [AI-R09](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Maintain AI-specific playbooks and an incident taxonomy. Preserve state needed for investigation: prompts, context, index snapshots, memory and model version. Define containment options and how to work with the model provider. |
| **Evidence Required** | Playbooks; exercise records; preserved-state checklist; provider contact and escalation path. |
| **Audit Test Procedure** | Run a tabletop or lab exercise for a prompt injection incident. Confirm the interaction can be replayed, scoped and contained using the playbook. |
| **Control Owner** | SOC / Incident Response |
| **Review Frequency** | Annually and after each incident |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-035. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-035. |
| **MITRE ATLAS Mitigations** | AML.M0024 AI Telemetry Logging |
| **NIST AI RMF** | MANAGE 4.3; MANAGE 2.3; GOVERN 4.3; GOVERN 6.2 |
| **ISO/IEC 42001** | A.8.4 Communication of incidents; A.8.3 External reporting; A.3.3 Reporting of concerns; A.6.2.6 AI system operation and monitoring |
| **Tested By (39 cases)** | **D09:** [017](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-017)<br>**D12:** [001](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-001), [002](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-002), [003](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-003), [004](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-004), [005](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-005), [006](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-006), [007](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-007), [008](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-008), [009](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-009), [010](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-010), [011](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-011), [012](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-012), [013](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-013), [014](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-014), [015](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-015), [016](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-016), [017](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-017), [018](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-018), [019](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-019), [020](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-020), [021](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-021), [022](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-022)<br>**L03:** [019](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-019), [027](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-027)<br>**L10:** [027](../10_Test_Case_Library/L10-data-layer.md#tc-l10-027), [028](../10_Test_Case_Library/L10-data-layer.md#tc-l10-028)<br>**L16:** [021](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-021), [024](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-024)<br>**L17:** [015](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-015), [017](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-017), [018](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-018), [019](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-019), [020](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-020), [021](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-021), [022](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-022), [023](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-023), [026](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-026), [027](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-027) |

### Cost and Abuse

<a id="ai-ctrl-036"></a>

#### AI-CTRL-036: AI Cost and Abuse Controls

| Field | Detail |
|---|---|
| **Control Objective** | Attribute AI spend and stop abuse that exhausts budget or capacity. |
| **Applies To** | AI APIs / Custom AI Applications / Agents |
| **Risk Mapping** | [AI-R11](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Attribute usage to team, application, user and key. Set budgets, rate limits and quotas with enforcement. Detect spend anomalies and leaked keys, and limit loops and retries in agents. |
| **Evidence Required** | Cost attribution reports; budget and quota configuration; anomaly alerts; key revocation records. |
| **Audit Test Procedure** | Drive a test key past its budget and confirm enforcement. Simulate a traffic spike on a public endpoint and confirm detection and throttling. |
| **Control Owner** | FinOps / AI Platform Team |
| **Review Frequency** | Quarterly |
| **OWASP** | LLM10:2025 Unbounded Consumption |
| **MITRE ATLAS Techniques** | AML.T0034 Cost Harvesting; AML.T0029 Denial of AI Service; AML.T0046 Spamming AI System with Chaff Data |
| **MITRE ATLAS Mitigations** | AML.M0004 Limit AI Service Query Volume and Rate; AML.M0036 Limit AI Workload Resource Consumption |
| **NIST AI RMF** | MEASURE 2.7; MANAGE 4.1 |
| **ISO/IEC 42001** | A.4.5 System and computing resources |
| **Tested By (30 cases)** | **D11:** [011](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-011)<br>**D13:** [001](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-001), [002](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-002), [003](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-003), [004](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-004), [005](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-005), [006](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-006), [007](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-007), [008](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-008), [009](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-009), [010](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-010), [011](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-011), [012](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-012), [013](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-013), [014](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-014), [015](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-015), [016](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-016), [017](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-017), [018](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-018), [019](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-019), [020](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-020), [021](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-021)<br>**L06:** [021](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-021)<br>**L07:** [032](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-032)<br>**L08:** [030](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-030), [031](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-031)<br>**L12:** [013](../10_Test_Case_Library/L12-model-layer.md#tc-l12-013), [022](../10_Test_Case_Library/L12-model-layer.md#tc-l12-022)<br>**L13:** [020](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-020)<br>**L15:** [017](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-017) |

Case numbers in **Tested By** are short for the full ID: under L06, `001` is `TC-L06-001`.

## Standard Control Entry Template

Use this template when adding a control. Give it the next free ID and do not reuse or renumber existing IDs, because other pages link to them.

```markdown
# Control ID: AI-CTRL-XXX
## Control Name

## Control Objective

## Applies To
Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents / Vendors

## Risk Mapping

## Implementation Expectation

## Evidence Required

## Audit Test Procedure

## Control Owner

## Review Frequency

## Framework Mapping
OWASP / MITRE ATLAS techniques and mitigations / NIST AI RMF / ISO/IEC 42001

## Tested By
```

## Evidence Expectations

Evidence should be exportable, timestamped, attributable to user/device/application where applicable, and suitable for audit or incident investigation.
