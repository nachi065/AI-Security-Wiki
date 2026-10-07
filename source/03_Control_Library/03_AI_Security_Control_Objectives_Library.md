---
title: "AI Security Control Objectives Library"
author: Nachiket Sathaye
parent: "Control Library"
nav_order: 1
document_type: AI Security Wiki Reference
version: 2.0
---

# AI Security Control Objectives Library

> **Purpose:** Define reusable AI security control objectives for governance, engineering, vendor evaluation and audit testing.

> **Audience:** Security engineering, GRC, audit, AI product teams, SOC.

> **How to use:** Use this page as a wiki reference. Select controls by risk tier, then update the evidence, owners, control status, and links as implementation maturity improves.

The library holds **36 control objectives in 11 families**. Each control has a stable ID that the rest of the wiki uses: the [AI Risk to Control Mapping](../02_Risk_Management/02D_AI_Risk_to_Control_Mapping.md) links risks to controls, the [domain standards](../04_Domain_Standards/index.md) cite the controls they apply, the [AI Security Audit and Evidence Checklist](../06_Testing_and_Assurance/14_AI_Security_Audit_and_Evidence_Checklist.md) lists the evidence, and each page of the [Test Case Library](../10_Test_Case_Library/index.md) names the controls it tests.

The controls follow the design principle set out in the [Foundations paper](../00_Foundations/07-Reference-Architecture.md): the model is an untrusted component, and authority to act, access data or spend money is enforced outside it.

> **Verify before use.** OWASP, MITRE ATLAS, NIST AI RMF and ISO/IEC 42001 references must be checked against the current published versions. Owners and review frequencies are starting values; set your own.

## Control families

| Family | Controls |
|---|---|
| Governance and Compliance | [AI-CTRL-007](#ai-ctrl-007), [AI-CTRL-011](#ai-ctrl-011), [AI-CTRL-012](#ai-ctrl-012), [AI-CTRL-013](#ai-ctrl-013), [AI-CTRL-014](#ai-ctrl-014) |
| Discovery and Workforce AI Use | [AI-CTRL-001](#ai-ctrl-001), [AI-CTRL-002](#ai-ctrl-002), [AI-CTRL-003](#ai-ctrl-003), [AI-CTRL-004](#ai-ctrl-004), [AI-CTRL-010](#ai-ctrl-010) |
| Identity and Access | [AI-CTRL-015](#ai-ctrl-015), [AI-CTRL-016](#ai-ctrl-016) |
| Data and Retrieval | [AI-CTRL-017](#ai-ctrl-017), [AI-CTRL-018](#ai-ctrl-018), [AI-CTRL-019](#ai-ctrl-019) |
| Application Runtime | [AI-CTRL-005](#ai-ctrl-005), [AI-CTRL-020](#ai-ctrl-020), [AI-CTRL-021](#ai-ctrl-021) |
| Agents and Tools | [AI-CTRL-006](#ai-ctrl-006), [AI-CTRL-022](#ai-ctrl-022), [AI-CTRL-023](#ai-ctrl-023), [AI-CTRL-024](#ai-ctrl-024), [AI-CTRL-025](#ai-ctrl-025), [AI-CTRL-026](#ai-ctrl-026), [AI-CTRL-027](#ai-ctrl-027) |
| Model, Training and Pipeline | [AI-CTRL-028](#ai-ctrl-028), [AI-CTRL-029](#ai-ctrl-029), [AI-CTRL-030](#ai-ctrl-030) |
| Supply Chain and Infrastructure | [AI-CTRL-031](#ai-ctrl-031), [AI-CTRL-032](#ai-ctrl-032) |
| Assurance and Testing | [AI-CTRL-033](#ai-ctrl-033), [AI-CTRL-034](#ai-ctrl-034) |
| Detection and Response | [AI-CTRL-008](#ai-ctrl-008), [AI-CTRL-009](#ai-ctrl-009), [AI-CTRL-035](#ai-ctrl-035) |
| Cost and Abuse | [AI-CTRL-036](#ai-ctrl-036) |

## Control index

| Control ID | Control Name | Family | Objective |
|---|---|---|---|
| [AI-CTRL-001](#ai-ctrl-001) | AI Discovery | Discovery and Workforce AI Use | Identify approved/unapproved AI platforms across browsers, endpoints, IDEs, SaaS, APIs and custom apps. |
| [AI-CTRL-002](#ai-ctrl-002) | Prompt Inspection | Discovery and Workforce AI Use | Detect sensitive, restricted or risky content submitted to AI platforms. |
| [AI-CTRL-003](#ai-ctrl-003) | File Upload Protection | Discovery and Workforce AI Use | Prevent uploads of confidential or restricted files to unauthorized AI services. |
| [AI-CTRL-004](#ai-ctrl-004) | IDE AI Governance | Discovery and Workforce AI Use | Monitor and control AI coding assistants, source code sharing and secret leakage. |
| [AI-CTRL-005](#ai-ctrl-005) | Runtime AI Security | Application Runtime | Protect custom AI applications from prompt injection, misuse and output leakage. |
| [AI-CTRL-006](#ai-ctrl-006) | Agent Governance | Agents and Tools | Monitor AI agents, tool calls, API access and autonomous actions. |
| [AI-CTRL-007](#ai-ctrl-007) | Data Sovereignty | Governance and Compliance | Ensure prompts, logs and uploads are processed and retained in approved locations. |
| [AI-CTRL-008](#ai-ctrl-008) | Auditability | Detection and Response | Maintain logs for prompts, responses, files, users, devices, applications and actions. |
| [AI-CTRL-009](#ai-ctrl-009) | SOC Integration | Detection and Response | Forward AI security events and logs to monitoring and response platforms. |
| [AI-CTRL-010](#ai-ctrl-010) | Policy Enforcement | Discovery and Workforce AI Use | Support monitor, warn, redact, block and allow policies based on risk and classification. |
| [AI-CTRL-011](#ai-ctrl-011) | AI Use-Case Registry and Risk Tiering | Governance and Compliance | Record every AI use case with a business owner and a risk tier that decides which controls apply. |
| [AI-CTRL-012](#ai-ctrl-012) | AI Policy and Acceptable Use | Governance and Compliance | Set and communicate the rules for using and building AI, and map each rule to a control. |
| [AI-CTRL-013](#ai-ctrl-013) | Privacy and Regulatory Compliance | Governance and Compliance | Meet privacy and regulatory obligations for personal data handled by AI systems. |
| [AI-CTRL-014](#ai-ctrl-014) | Third-Party and Vendor AI Assurance | Governance and Compliance | Assess AI vendors and embedded AI features before use, and reassess when they change. |
| [AI-CTRL-015](#ai-ctrl-015) | Human and Agent Identity | Identity and Access | Give every user, application and agent that uses AI a unique, attributable identity. |
| [AI-CTRL-016](#ai-ctrl-016) | Least Privilege and Scoped Credentials | Identity and Access | Limit what each AI workload and agent can reach to the minimum its task needs. |
| [AI-CTRL-017](#ai-ctrl-017) | Data Protection in AI Pipelines | Data and Retrieval | Apply classification, minimization and isolation to data that AI systems ingest, process and produce. |
| [AI-CTRL-018](#ai-ctrl-018) | Retrieval Access Control | Data and Retrieval | Return only content the requesting user is entitled to see. |
| [AI-CTRL-019](#ai-ctrl-019) | Knowledge Base Integrity | Data and Retrieval | Stop untrusted or poisoned content from entering the corpus that AI systems retrieve from. |
| [AI-CTRL-020](#ai-ctrl-020) | Output Handling | Application Runtime | Treat model output as untrusted input to whatever consumes it. |
| [AI-CTRL-021](#ai-ctrl-021) | Multimodal and Voice Input Security | Application Runtime | Apply the same inspection and policy to images, documents, audio and video as to text. |
| [AI-CTRL-022](#ai-ctrl-022) | Deterministic Action Authorization | Agents and Tools | Enforce authority to act, access data or spend money outside the model. |
| [AI-CTRL-023](#ai-ctrl-023) | Human Approval for Sensitive Actions | Agents and Tools | Require a person to approve irreversible or high-impact actions before they run. |
| [AI-CTRL-024](#ai-ctrl-024) | Tool and MCP Server Governance | Agents and Tools | Allow agents to use only vetted tools and tool servers, and detect when they change. |
| [AI-CTRL-025](#ai-ctrl-025) | Agent Containment and Kill Switch | Agents and Tools | Stop an agent, revoke its access and limit the damage within minutes. |
| [AI-CTRL-026](#ai-ctrl-026) | Agent Memory and Context Integrity | Agents and Tools | Prevent poisoned or cross-user content from persisting in agent memory and context. |
| [AI-CTRL-027](#ai-ctrl-027) | Agent Execution Isolation | Agents and Tools | Run agent-generated code and browser or computer-use sessions in isolation. |
| [AI-CTRL-028](#ai-ctrl-028) | Model Protection | Model, Training and Pipeline | Protect models from theft, extraction and adversarial inputs. |
| [AI-CTRL-029](#ai-ctrl-029) | Training and Fine-Tuning Data Integrity | Model, Training and Pipeline | Know where training data came from and detect tampering before it shapes a model. |
| [AI-CTRL-030](#ai-ctrl-030) | ML Pipeline and Model Registry Security | Model, Training and Pipeline | Protect the pipeline that builds, stores and releases models and prompts. |
| [AI-CTRL-031](#ai-ctrl-031) | AI Supply Chain and AI-BOM | Supply Chain and Infrastructure | Know exactly which models, datasets, packages and prompts run in each environment. |
| [AI-CTRL-032](#ai-ctrl-032) | AI Infrastructure Hardening | Supply Chain and Infrastructure | Harden and segment the infrastructure that trains and serves models. |
| [AI-CTRL-033](#ai-ctrl-033) | AI Security Review and Release Gate | Assurance and Testing | Review every AI system against its threats before production and after material change. |
| [AI-CTRL-034](#ai-ctrl-034) | Adversarial Testing and Continuous Evaluation | Assurance and Testing | Test AI systems against attacks before release and continuously afterwards. |
| [AI-CTRL-035](#ai-ctrl-035) | AI Incident Response and Forensics | Detection and Response | Detect, contain, investigate and recover from AI security incidents. |
| [AI-CTRL-036](#ai-ctrl-036) | AI Cost and Abuse Controls | Cost and Abuse | Attribute AI spend and stop abuse that exhausts budget or capacity. |

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
| **OWASP** | LLM02 Sensitive Information Disclosure |
| **MITRE ATLAS** | — |
| **NIST AI RMF** | GOVERN, MAP |
| **ISO/IEC 42001 Annex A** | A.7 Data for AI systems; A.10 Third-party and customer relationships |
| **Tested By** | [L03](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md), [L15](../10_Test_Case_Library/L15-infrastructure-layer.md) |

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
| **OWASP** | — |
| **MITRE ATLAS** | — |
| **NIST AI RMF** | GOVERN, MAP |
| **ISO/IEC 42001 Annex A** | A.3 Internal organization; A.5 Assessing impacts of AI systems |
| **Tested By** | [L01](../10_Test_Case_Library/L01-business-and-use-cases.md), [L02](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md) |

<a id="ai-ctrl-012"></a>

#### AI-CTRL-012: AI Policy and Acceptable Use

| Field | Detail |
|---|---|
| **Control Objective** | Set and communicate the rules for using and building AI, and map each rule to a control. |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents |
| **Risk Mapping** | [AI-R02](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R03](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Publish an AI policy and acceptable-use standard with scope, owner and review date. Map each policy statement to a control in this library. Train users and reinforce the rules at the point of use. |
| **Evidence Required** | Approved policy; policy-to-control mapping; training records; coaching events. |
| **Audit Test Procedure** | Select policy statements and trace each to a control and to evidence that it operates. Confirm the policy was reviewed within its cycle. |
| **Control Owner** | GRC |
| **Review Frequency** | Annually |
| **OWASP** | — |
| **MITRE ATLAS** | — |
| **NIST AI RMF** | GOVERN |
| **ISO/IEC 42001 Annex A** | A.2 Policies related to AI; A.9 Use of AI systems |
| **Tested By** | [L02](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md), [L04](../10_Test_Case_Library/L04-human-interaction-layer.md) |

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
| **OWASP** | LLM02 Sensitive Information Disclosure |
| **MITRE ATLAS** | AML.T0057 LLM Data Leakage |
| **NIST AI RMF** | GOVERN, MAP |
| **ISO/IEC 42001 Annex A** | A.5 Assessing impacts of AI systems; A.7 Data for AI systems |
| **Tested By** | [L03](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md) |

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
| **OWASP** | LLM03 Supply Chain |
| **MITRE ATLAS** | AML.T0010 AI Supply Chain Compromise |
| **NIST AI RMF** | GOVERN, MAP |
| **ISO/IEC 42001 Annex A** | A.10 Third-party and customer relationships |
| **Tested By** | [L16](../10_Test_Case_Library/L16-supply-chain-and-third-party.md) |

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
| **OWASP** | LLM03 Supply Chain |
| **MITRE ATLAS** | — |
| **NIST AI RMF** | GOVERN, MAP |
| **ISO/IEC 42001 Annex A** | A.4 Resources for AI systems; A.9 Use of AI systems |
| **Tested By** | [L04](../10_Test_Case_Library/L04-human-interaction-layer.md), [L05](../10_Test_Case_Library/L05-ai-applications.md) |

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
| **OWASP** | LLM02 Sensitive Information Disclosure |
| **MITRE ATLAS** | AML.T0057 LLM Data Leakage |
| **NIST AI RMF** | MEASURE, MANAGE |
| **ISO/IEC 42001 Annex A** | A.7 Data for AI systems; A.9 Use of AI systems |
| **Tested By** | [L04](../10_Test_Case_Library/L04-human-interaction-layer.md), [L08](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md) |

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
| **OWASP** | LLM02 Sensitive Information Disclosure |
| **MITRE ATLAS** | AML.T0057 LLM Data Leakage |
| **NIST AI RMF** | MEASURE, MANAGE |
| **ISO/IEC 42001 Annex A** | A.7 Data for AI systems; A.9 Use of AI systems |
| **Tested By** | [L04](../10_Test_Case_Library/L04-human-interaction-layer.md), [L08](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md) |

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
| **OWASP** | LLM02 Sensitive Information Disclosure; LLM03 Supply Chain |
| **MITRE ATLAS** | AML.T0057 LLM Data Leakage; AML.T0055 Unsecured Credentials |
| **NIST AI RMF** | MEASURE, MANAGE |
| **ISO/IEC 42001 Annex A** | A.9 Use of AI systems |
| **Tested By** | [L04](../10_Test_Case_Library/L04-human-interaction-layer.md), [L05](../10_Test_Case_Library/L05-ai-applications.md), [L08](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md), [L14](../10_Test_Case_Library/L14-mlops-llmops-layer.md) |

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
| **OWASP** | LLM02 Sensitive Information Disclosure |
| **MITRE ATLAS** | AML.T0057 LLM Data Leakage |
| **NIST AI RMF** | MANAGE |
| **ISO/IEC 42001 Annex A** | A.2 Policies related to AI; A.9 Use of AI systems |
| **Tested By** | [L04](../10_Test_Case_Library/L04-human-interaction-layer.md), [L08](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md) |

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
| **OWASP** | LLM06 Excessive Agency; ASI03 Identity & Privilege Abuse |
| **MITRE ATLAS** | AML.T0012 Valid Accounts |
| **NIST AI RMF** | MANAGE |
| **ISO/IEC 42001 Annex A** | A.3 Internal organization; A.4 Resources for AI systems |
| **Tested By** | [L09](../10_Test_Case_Library/L09-identity-and-access-mgmt.md), [D09](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md) |

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
| **OWASP** | LLM06 Excessive Agency; ASI03 Identity & Privilege Abuse |
| **MITRE ATLAS** | AML.T0012 Valid Accounts; AML.T0055 Unsecured Credentials |
| **NIST AI RMF** | MANAGE |
| **ISO/IEC 42001 Annex A** | A.4 Resources for AI systems |
| **Tested By** | [L09](../10_Test_Case_Library/L09-identity-and-access-mgmt.md), [D09](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md) |

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
| **OWASP** | LLM02 Sensitive Information Disclosure |
| **MITRE ATLAS** | AML.T0057 LLM Data Leakage |
| **NIST AI RMF** | MEASURE, MANAGE |
| **ISO/IEC 42001 Annex A** | A.7 Data for AI systems |
| **Tested By** | [L10](../10_Test_Case_Library/L10-data-layer.md) |

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
| **OWASP** | LLM08 Vector and Embedding Weaknesses; LLM02 Sensitive Information Disclosure |
| **MITRE ATLAS** | AML.T0057 LLM Data Leakage |
| **NIST AI RMF** | MEASURE, MANAGE |
| **ISO/IEC 42001 Annex A** | A.7 Data for AI systems |
| **Tested By** | [L11](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md) |

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
| **OWASP** | LLM04 Data and Model Poisoning; LLM08 Vector and Embedding Weaknesses |
| **MITRE ATLAS** | AML.T0020 Poison Training Data; AML.T0051 LLM Prompt Injection |
| **NIST AI RMF** | MEASURE, MANAGE |
| **ISO/IEC 42001 Annex A** | A.7 Data for AI systems |
| **Tested By** | [L11](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md) |

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
| **OWASP** | LLM01 Prompt Injection; LLM07 System Prompt Leakage |
| **MITRE ATLAS** | AML.T0051 LLM Prompt Injection; AML.T0054 LLM Jailbreak; AML.T0056 LLM Meta Prompt Extraction |
| **NIST AI RMF** | MEASURE, MANAGE |
| **ISO/IEC 42001 Annex A** | A.6 AI system life cycle |
| **Tested By** | [L05](../10_Test_Case_Library/L05-ai-applications.md), [L07](../10_Test_Case_Library/L07-prompt-and-context-layer.md), [L08](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md) |

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
| **OWASP** | LLM05 Improper Output Handling; LLM02 Sensitive Information Disclosure |
| **MITRE ATLAS** | AML.T0057 LLM Data Leakage |
| **NIST AI RMF** | MEASURE, MANAGE |
| **ISO/IEC 42001 Annex A** | A.6 AI system life cycle |
| **Tested By** | [L05](../10_Test_Case_Library/L05-ai-applications.md), [L08](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md) |

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
| **OWASP** | LLM01 Prompt Injection; LLM02 Sensitive Information Disclosure |
| **MITRE ATLAS** | AML.T0051 LLM Prompt Injection; AML.T0057 LLM Data Leakage |
| **NIST AI RMF** | MEASURE, MANAGE |
| **ISO/IEC 42001 Annex A** | A.6 AI system life cycle; A.7 Data for AI systems |
| **Tested By** | [D11](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md), [L04](../10_Test_Case_Library/L04-human-interaction-layer.md) |

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
| **OWASP** | LLM06 Excessive Agency; ASI10 Rogue Agents |
| **MITRE ATLAS** | AML.T0053 LLM Plugin Compromise |
| **NIST AI RMF** | GOVERN, MANAGE |
| **ISO/IEC 42001 Annex A** | A.4 Resources for AI systems; A.9 Use of AI systems |
| **Tested By** | [L06](../10_Test_Case_Library/L06-agent-orchestration-layer.md), [D09](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md) |

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
| **OWASP** | LLM06 Excessive Agency; ASI02 Tool Misuse & Exploitation |
| **MITRE ATLAS** | AML.T0053 LLM Plugin Compromise |
| **NIST AI RMF** | MANAGE |
| **ISO/IEC 42001 Annex A** | A.6 AI system life cycle; A.9 Use of AI systems |
| **Tested By** | [L06](../10_Test_Case_Library/L06-agent-orchestration-layer.md), [L09](../10_Test_Case_Library/L09-identity-and-access-mgmt.md) |

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
| **OWASP** | LLM06 Excessive Agency; ASI09 Human-Agent Trust Exploitation |
| **MITRE ATLAS** | — |
| **NIST AI RMF** | MANAGE |
| **ISO/IEC 42001 Annex A** | A.9 Use of AI systems |
| **Tested By** | [L06](../10_Test_Case_Library/L06-agent-orchestration-layer.md), [D10](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md) |

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
| **OWASP** | LLM03 Supply Chain; ASI04 Agentic Supply Chain Vulnerabilities; ASI02 Tool Misuse & Exploitation |
| **MITRE ATLAS** | AML.T0053 LLM Plugin Compromise; AML.T0010 AI Supply Chain Compromise |
| **NIST AI RMF** | GOVERN, MANAGE |
| **ISO/IEC 42001 Annex A** | A.10 Third-party and customer relationships |
| **Tested By** | [L06](../10_Test_Case_Library/L06-agent-orchestration-layer.md), [L16](../10_Test_Case_Library/L16-supply-chain-and-third-party.md) |

<a id="ai-ctrl-025"></a>

#### AI-CTRL-025: Agent Containment and Kill Switch

| Field | Detail |
|---|---|
| **Control Objective** | Stop an agent, revoke its access and limit the damage within minutes. |
| **Applies To** | Agents |
| **Risk Mapping** | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Provide a tested way to stop a single agent and to revoke credentials for all agents. Set limits on steps, time and spend per task. Know which actions can be rolled back and how. |
| **Evidence Required** | Kill switch procedure; test records with timings; task limits configuration. |
| **Audit Test Procedure** | Start a long-running test agent and stop it. Measure the time until no further actions occur and credentials are invalid. |
| **Control Owner** | AI Platform Team / SOC |
| **Review Frequency** | Semi-annually |
| **OWASP** | LLM06 Excessive Agency; ASI08 Cascading Failures; ASI10 Rogue Agents |
| **MITRE ATLAS** | — |
| **NIST AI RMF** | MANAGE |
| **ISO/IEC 42001 Annex A** | A.6 AI system life cycle |
| **Tested By** | [L06](../10_Test_Case_Library/L06-agent-orchestration-layer.md), [D10](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md), [D12](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md) |

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
| **OWASP** | LLM01 Prompt Injection; ASI06 Memory & Context Poisoning |
| **MITRE ATLAS** | AML.T0051 LLM Prompt Injection |
| **NIST AI RMF** | MEASURE, MANAGE |
| **ISO/IEC 42001 Annex A** | A.6 AI system life cycle |
| **Tested By** | [L07](../10_Test_Case_Library/L07-prompt-and-context-layer.md) |

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
| **OWASP** | LLM06 Excessive Agency; ASI05 Unexpected Code Execution (RCE) |
| **MITRE ATLAS** | AML.T0050 Command and Scripting Interpreter |
| **NIST AI RMF** | MANAGE |
| **ISO/IEC 42001 Annex A** | A.6 AI system life cycle |
| **Tested By** | [L06](../10_Test_Case_Library/L06-agent-orchestration-layer.md), [D10](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md) |

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
| **OWASP** | LLM10 Unbounded Consumption; LLM03 Supply Chain |
| **MITRE ATLAS** | AML.T0024 Exfiltration via AI Inference API; AML.T0043 Craft Adversarial Data |
| **NIST AI RMF** | MEASURE, MANAGE |
| **ISO/IEC 42001 Annex A** | A.6 AI system life cycle |
| **Tested By** | [L12](../10_Test_Case_Library/L12-model-layer.md) |

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
| **OWASP** | LLM04 Data and Model Poisoning |
| **MITRE ATLAS** | AML.T0020 Poison Training Data |
| **NIST AI RMF** | MAP, MEASURE |
| **ISO/IEC 42001 Annex A** | A.7 Data for AI systems |
| **Tested By** | [L13](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md) |

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
| **OWASP** | LLM03 Supply Chain; LLM04 Data and Model Poisoning |
| **MITRE ATLAS** | AML.T0010 AI Supply Chain Compromise; AML.T0012 Valid Accounts |
| **NIST AI RMF** | MEASURE, MANAGE |
| **ISO/IEC 42001 Annex A** | A.6 AI system life cycle |
| **Tested By** | [L14](../10_Test_Case_Library/L14-mlops-llmops-layer.md) |

### Supply Chain and Infrastructure

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
| **OWASP** | LLM03 Supply Chain |
| **MITRE ATLAS** | AML.T0010 AI Supply Chain Compromise |
| **NIST AI RMF** | GOVERN, MAP, MANAGE |
| **ISO/IEC 42001 Annex A** | A.10 Third-party and customer relationships; A.4 Resources for AI systems |
| **Tested By** | [L16](../10_Test_Case_Library/L16-supply-chain-and-third-party.md) |

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
| **OWASP** | LLM03 Supply Chain; LLM02 Sensitive Information Disclosure |
| **MITRE ATLAS** | AML.T0049 Exploit Public-Facing Application; AML.T0055 Unsecured Credentials |
| **NIST AI RMF** | MANAGE |
| **ISO/IEC 42001 Annex A** | A.4 Resources for AI systems |
| **Tested By** | [L15](../10_Test_Case_Library/L15-infrastructure-layer.md) |

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
| **OWASP** | — |
| **MITRE ATLAS** | — |
| **NIST AI RMF** | GOVERN, MAP |
| **ISO/IEC 42001 Annex A** | A.5 Assessing impacts of AI systems; A.6 AI system life cycle |
| **Tested By** | [L01](../10_Test_Case_Library/L01-business-and-use-cases.md), [L02](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md) |

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
| **OWASP** | LLM01 Prompt Injection; LLM10 Unbounded Consumption |
| **MITRE ATLAS** | AML.T0051 LLM Prompt Injection; AML.T0054 LLM Jailbreak |
| **NIST AI RMF** | MEASURE |
| **ISO/IEC 42001 Annex A** | A.6 AI system life cycle |
| **Tested By** | [D08](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md) |

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
| **OWASP** | LLM02 Sensitive Information Disclosure; LLM06 Excessive Agency |
| **MITRE ATLAS** | — |
| **NIST AI RMF** | MEASURE, MANAGE |
| **ISO/IEC 42001 Annex A** | A.6 AI system life cycle; A.8 Information for interested parties |
| **Tested By** | [L17](../10_Test_Case_Library/L17-monitoring-detection-and-response.md), [D12](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md) |

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
| **OWASP** | LLM06 Excessive Agency |
| **MITRE ATLAS** | — |
| **NIST AI RMF** | MEASURE, MANAGE |
| **ISO/IEC 42001 Annex A** | A.6 AI system life cycle |
| **Tested By** | [L17](../10_Test_Case_Library/L17-monitoring-detection-and-response.md) |

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
| **OWASP** | LLM06 Excessive Agency |
| **MITRE ATLAS** | — |
| **NIST AI RMF** | MANAGE |
| **ISO/IEC 42001 Annex A** | A.6 AI system life cycle; A.8 Information for interested parties |
| **Tested By** | [D12](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md), [L17](../10_Test_Case_Library/L17-monitoring-detection-and-response.md) |

### Cost and Abuse

<a id="ai-ctrl-036"></a>

#### AI-CTRL-036: AI Cost and Abuse Controls

| Field | Detail |
|---|---|
| **Control Objective** | Attribute AI spend and stop abuse that exhausts budget or capacity. |
| **Applies To** | AI APIs / Custom AI Applications / Agents |
| **Risk Mapping** | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Attribute usage to team, application, user and key. Set budgets, rate limits and quotas with enforcement. Detect spend anomalies and leaked keys, and limit loops and retries in agents. |
| **Evidence Required** | Cost attribution reports; budget and quota configuration; anomaly alerts; key revocation records. |
| **Audit Test Procedure** | Drive a test key past its budget and confirm enforcement. Simulate a traffic spike on a public endpoint and confirm detection and throttling. |
| **Control Owner** | FinOps / AI Platform Team |
| **Review Frequency** | Quarterly |
| **OWASP** | LLM10 Unbounded Consumption |
| **MITRE ATLAS** | AML.T0034 Cost Harvesting; AML.T0029 Denial of AI Service |
| **NIST AI RMF** | MANAGE |
| **ISO/IEC 42001 Annex A** | A.4 Resources for AI systems |
| **Tested By** | [D13](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md), [L08](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md) |

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
OWASP / MITRE ATLAS / NIST AI RMF / ISO/IEC 42001

## Tested By
```

## Evidence Expectations

Evidence should be exportable, timestamped, attributable to user/device/application where applicable, and suitable for audit or incident investigation.
