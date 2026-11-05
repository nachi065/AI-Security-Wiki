---
title: "AI Security Control Objectives Library"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Control Library"
nav_order: 1
document_type: AI Security Wiki Reference
version: 2.7
---

# AI Security Control Objectives Library

> **Purpose:** Define reusable AI security control objectives for governance, engineering, vendor evaluation and audit testing.

> **Audience:** Security engineering, GRC, audit, AI product teams, SOC.

> **How to use:** Select controls by risk tier, then update the evidence, owners, control status, and links as implementation maturity improves.

The library holds **{{n:controls}} control objectives in {{n:families}} families**, split into a [Baseline and an Advanced tier](06_Control_Tiers.md). Each control has a stable ID that the rest of the wiki uses: the [AI Risk to Control Mapping](../02_Risk_Management/02D_AI_Risk_to_Control_Mapping.md) links risks to controls, the [domain standards](../04_Domain_Standards/index.md) cite the controls they apply, the [AI Security Audit and Evidence Checklist](../06_Testing_and_Assurance/14_AI_Security_Audit_and_Evidence_Checklist.md) lists the evidence, and every one of the {{n:tests}} cases in the [Test Case Library](../10_Test_Case_Library/index.md) names the control it tests.

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
| ISO/IEC 27001 | 2022 | Annex A controls, for example `A.8.15`; management system clauses, for example `Clause 6.1.2` |
| NIST Cybersecurity Framework | 2.0 | Categories, for example `PR.DS` |
| CIS Critical Security Controls | 8 | Controls `CIS 1` to `CIS 18` |
| SOC 2 (AICPA Trust Services Criteria) | 2017, with the 2022 points of focus | Criteria, for example `CC6.1` |
| AI Security Wiki (own) | This page | `AI-CTRL-001` to `AI-CTRL-046` |

The last four are general security frameworks with no AI-specific content. A control cites the entries it supports when it is applied to an AI system. The labels after the SOC 2 criteria numbers are this wiki's own short descriptions, because the criteria text belongs to the AICPA.

> **Verify before use.** Frameworks are revised. MITRE ATLAS in particular is updated monthly and renames techniques. Check identifiers against the current published versions before quoting them in an RFP or audit. Owners and review frequencies are starting values; set your own.

## Assurance stages and deployment models

Each control names the **assurance stage** at which a reviewer first checks it, and the **deployment models** it applies to. Use them to scope a review: filter to the stage you are at and the way the AI system is delivered. The [AI Security Requirements Traceability Matrix](../25_Templates/12_AI_Security_Requirements_Traceability_Matrix_Template.md) carries both fields for every requirement.

| Assurance stage | What is checked |
|---|---|
| Discovery | Before design or purchase: the use case is registered, tiered and in scope of policy, and the supplier is screened. |
| Design | The design: data flows, authority, oversight and impact assessments, before build or configuration starts. |
| Implementation | The built or configured system, before release: inspection, access, output handling and testing. |
| Platform | The hosting platform and infrastructure: isolation, hardening, logging pipelines, resilience and cost limits. |
| Production | The system in operation: monitoring, response, containment, audit evidence and regulator duties. |

The stage is where checking starts, not where it ends. A control first checked at Design is tested again before release and in periodic audits, at its review frequency.

| Deployment model | Meaning |
|---|---|
| All | Applies however the AI system is delivered. For a SaaS or AIaaS service, the supplier provides the evidence and you check it under [AI-CTRL-014](#ai-ctrl-014). |
| Cloud | Applies when any part of the system is hosted by a cloud or AI service provider (SaaS, AIaaS, PaaS or IaaS). |
| PaaS/IaaS/Self-hosted | Applies when you host or operate the model, pipeline or infrastructure yourself. For SaaS and AIaaS, the supplier owns it and you ask for its assurance evidence instead. |

The stage and deployment model of each control are the wiki's starting values. Change them to suit your own review process.

## Control families

| Family | Controls |
|---|---|
| Governance and Compliance | [AI-CTRL-007](#ai-ctrl-007), [AI-CTRL-011](#ai-ctrl-011), [AI-CTRL-012](#ai-ctrl-012), [AI-CTRL-013](#ai-ctrl-013), [AI-CTRL-014](#ai-ctrl-014), [AI-CTRL-037](#ai-ctrl-037), [AI-CTRL-042](#ai-ctrl-042), [AI-CTRL-043](#ai-ctrl-043), [AI-CTRL-044](#ai-ctrl-044), [AI-CTRL-045](#ai-ctrl-045), [AI-CTRL-046](#ai-ctrl-046) |
| Discovery and Workforce AI Use | [AI-CTRL-001](#ai-ctrl-001), [AI-CTRL-002](#ai-ctrl-002), [AI-CTRL-003](#ai-ctrl-003), [AI-CTRL-004](#ai-ctrl-004), [AI-CTRL-010](#ai-ctrl-010) |
| Identity and Access | [AI-CTRL-015](#ai-ctrl-015), [AI-CTRL-016](#ai-ctrl-016) |
| Data and Retrieval | [AI-CTRL-017](#ai-ctrl-017), [AI-CTRL-018](#ai-ctrl-018), [AI-CTRL-019](#ai-ctrl-019) |
| Application Runtime | [AI-CTRL-005](#ai-ctrl-005), [AI-CTRL-020](#ai-ctrl-020), [AI-CTRL-021](#ai-ctrl-021), [AI-CTRL-039](#ai-ctrl-039) |
| Agents and Tools | [AI-CTRL-006](#ai-ctrl-006), [AI-CTRL-022](#ai-ctrl-022), [AI-CTRL-023](#ai-ctrl-023), [AI-CTRL-024](#ai-ctrl-024), [AI-CTRL-025](#ai-ctrl-025), [AI-CTRL-026](#ai-ctrl-026), [AI-CTRL-027](#ai-ctrl-027) |
| Model, Training and Pipeline | [AI-CTRL-028](#ai-ctrl-028), [AI-CTRL-029](#ai-ctrl-029), [AI-CTRL-030](#ai-ctrl-030) |
| Supply Chain, Infrastructure and Resilience | [AI-CTRL-031](#ai-ctrl-031), [AI-CTRL-032](#ai-ctrl-032), [AI-CTRL-040](#ai-ctrl-040) |
| Assurance and Testing | [AI-CTRL-033](#ai-ctrl-033), [AI-CTRL-034](#ai-ctrl-034), [AI-CTRL-038](#ai-ctrl-038), [AI-CTRL-041](#ai-ctrl-041) |
| Detection and Response | [AI-CTRL-008](#ai-ctrl-008), [AI-CTRL-009](#ai-ctrl-009), [AI-CTRL-035](#ai-ctrl-035) |
| Cost and Abuse | [AI-CTRL-036](#ai-ctrl-036) |

## Control index

| Control ID | Control Name | Family | Objective | Test Cases |
|---|---|---|---|---|
| [AI-CTRL-001](#ai-ctrl-001) | AI Discovery | Discovery and Workforce AI Use | Identify approved/unapproved AI platforms across browsers, endpoints, IDEs, SaaS, APIs and custom apps. | 33 |
| [AI-CTRL-002](#ai-ctrl-002) | Prompt Inspection | Discovery and Workforce AI Use | Detect sensitive, restricted or risky content submitted to AI platforms. | 16 |
| [AI-CTRL-003](#ai-ctrl-003) | File Upload Protection | Discovery and Workforce AI Use | Prevent uploads of confidential or restricted files to unauthorized AI services. | 6 |
| [AI-CTRL-004](#ai-ctrl-004) | IDE AI Governance | Discovery and Workforce AI Use | Monitor and control AI coding assistants, source code sharing and secret leakage. | 19 |
| [AI-CTRL-005](#ai-ctrl-005) | Runtime AI Security | Application Runtime | Protect custom AI applications from prompt injection, misuse and output leakage. | 52 |
| [AI-CTRL-006](#ai-ctrl-006) | Agent Governance | Agents and Tools | Monitor AI agents, tool calls, API access and autonomous actions. | 15 |
| [AI-CTRL-007](#ai-ctrl-007) | Data Sovereignty | Governance and Compliance | Ensure prompts, logs and uploads are processed and retained in approved locations. | 15 |
| [AI-CTRL-008](#ai-ctrl-008) | Auditability | Detection and Response | Maintain logs for prompts, responses, files, users, devices, applications and actions. | 23 |
| [AI-CTRL-009](#ai-ctrl-009) | SOC Integration | Detection and Response | Forward AI security events and logs to monitoring and response platforms. | 22 |
| [AI-CTRL-010](#ai-ctrl-010) | Policy Enforcement | Discovery and Workforce AI Use | Support monitor, warn, redact, block and allow policies based on risk and classification. | 28 |
| [AI-CTRL-011](#ai-ctrl-011) | AI Use-Case Registry and Risk Tiering | Governance and Compliance | Record every AI use case with a business owner and a risk tier that decides which controls apply. | 19 |
| [AI-CTRL-012](#ai-ctrl-012) | AI Policy, Roles and Acceptable Use | Governance and Compliance | Set and communicate the rules and responsibilities for using and building AI, and map each rule to a control. | 8 |
| [AI-CTRL-013](#ai-ctrl-013) | Privacy and Regulatory Compliance | Governance and Compliance | Meet privacy and regulatory obligations for personal data handled by AI systems. | 41 |
| [AI-CTRL-014](#ai-ctrl-014) | Third-Party and Vendor AI Assurance | Governance and Compliance | Assess AI vendors and embedded AI features before use, and reassess when they change. | 26 |
| [AI-CTRL-015](#ai-ctrl-015) | Human and Agent Identity | Identity and Access | Give every user, application and agent that uses AI a unique, attributable identity. | 45 |
| [AI-CTRL-016](#ai-ctrl-016) | Least Privilege and Scoped Credentials | Identity and Access | Limit what each AI workload and agent can reach to the minimum its task needs. | 53 |
| [AI-CTRL-017](#ai-ctrl-017) | Data Protection in AI Pipelines | Data and Retrieval | Apply classification, minimization and isolation to data that AI systems ingest, process and produce. | 39 |
| [AI-CTRL-018](#ai-ctrl-018) | Retrieval Access Control | Data and Retrieval | Return only content the requesting user is entitled to see. | 10 |
| [AI-CTRL-019](#ai-ctrl-019) | Knowledge Base Integrity | Data and Retrieval | Stop untrusted or poisoned content from entering the corpus that AI systems retrieve from. | 15 |
| [AI-CTRL-020](#ai-ctrl-020) | Output Handling | Application Runtime | Treat model output as untrusted input to whatever consumes it. | 14 |
| [AI-CTRL-021](#ai-ctrl-021) | Multimodal and Voice Input Security | Application Runtime | Apply the same inspection and policy to images, documents, audio and video as to text. | 28 |
| [AI-CTRL-022](#ai-ctrl-022) | Deterministic Action Authorization | Agents and Tools | Enforce authority to act, access data or spend money outside the model. | 19 |
| [AI-CTRL-023](#ai-ctrl-023) | Human Approval for Sensitive Actions | Agents and Tools | Require a person to approve irreversible or high-impact actions before they run. | 8 |
| [AI-CTRL-024](#ai-ctrl-024) | Tool and MCP Server Governance | Agents and Tools | Allow agents to use only vetted tools and tool servers, and detect when they change. | 16 |
| [AI-CTRL-025](#ai-ctrl-025) | AI Containment and Kill Switch | Agents and Tools | Stop an agent or suspend a high-risk AI model, revoke its access and limit the damage within minutes. | 13 |
| [AI-CTRL-026](#ai-ctrl-026) | Agent Memory and Context Integrity | Agents and Tools | Prevent poisoned or cross-user content from persisting in agent memory and context. | 9 |
| [AI-CTRL-027](#ai-ctrl-027) | Agent Execution Isolation | Agents and Tools | Run agent-generated code and browser or computer-use sessions in isolation. | 12 |
| [AI-CTRL-028](#ai-ctrl-028) | Model Protection | Model, Training and Pipeline | Protect models from theft, extraction and adversarial inputs. | 20 |
| [AI-CTRL-029](#ai-ctrl-029) | Training and Fine-Tuning Data Integrity | Model, Training and Pipeline | Know where training data came from and detect tampering before it shapes a model. | 18 |
| [AI-CTRL-030](#ai-ctrl-030) | ML Pipeline and Model Registry Security | Model, Training and Pipeline | Protect the pipeline that builds, stores and releases models and prompts. | 16 |
| [AI-CTRL-031](#ai-ctrl-031) | AI Supply Chain and AI-BOM | Supply Chain, Infrastructure and Resilience | Know exactly which models, datasets, packages and prompts run in each environment. | 25 |
| [AI-CTRL-032](#ai-ctrl-032) | AI Infrastructure Hardening | Supply Chain, Infrastructure and Resilience | Harden and segment the infrastructure that trains and serves models. | 27 |
| [AI-CTRL-033](#ai-ctrl-033) | AI Security Review and Release Gate | Assurance and Testing | Review every AI system against its threats before production and after material change. | 8 |
| [AI-CTRL-034](#ai-ctrl-034) | Adversarial Testing and Continuous Evaluation | Assurance and Testing | Test AI systems against attacks before release and continuously afterwards. | 38 |
| [AI-CTRL-035](#ai-ctrl-035) | AI Incident Response and Forensics | Detection and Response | Detect, contain, investigate and recover from AI security incidents. | 40 |
| [AI-CTRL-036](#ai-ctrl-036) | AI Cost and Abuse Controls | Cost and Abuse | Attribute AI spend and stop abuse that exhausts budget or capacity. | 30 |
| [AI-CTRL-037](#ai-ctrl-037) | AI Risk Assessment and Exception Management | Governance and Compliance | Assess, treat and accept AI risks consistently, and keep every exception owned and time-bound. | 10 |
| [AI-CTRL-038](#ai-ctrl-038) | Control Assurance and Audit Evidence | Assurance and Testing | Show, with current evidence, that each AI control is operating and that findings are closed. | 17 |
| [AI-CTRL-039](#ai-ctrl-039) | Output Reliability and Content Safety | Application Runtime | Keep AI output grounded, within its approved scope and free of harmful content. | 9 |
| [AI-CTRL-040](#ai-ctrl-040) | AI Service Resilience and Fail-Safe Operation | Supply Chain, Infrastructure and Resilience | Keep AI services and their security controls available, and make them fail safely. | 14 |
| [AI-CTRL-041](#ai-ctrl-041) | Fairness, Bias Testing and Explainability | Assurance and Testing | Test AI systems that make or support high-impact decisions for unfair bias, and keep explanations that a person can understand and a reviewer can challenge. | 7 |
| [AI-CTRL-042](#ai-ctrl-042) | Fundamental Rights and Data Protection Impact Assessment | Governance and Compliance | Assess the impact on people's rights before deploying AI that is high-risk or that puts personal data at risk, and keep the assessment current. | 4 |
| [AI-CTRL-043](#ai-ctrl-043) | Regulator and Authority Engagement | Governance and Compliance | Know which authorities oversee each AI system, meet the registration, filing and notification duties they set, and keep a record of every contact. | 4 |
| [AI-CTRL-044](#ai-ctrl-044) | AI Literacy and Role-Based Competence | Governance and Compliance | Give everyone who builds, operates, oversees or uses AI the knowledge their role needs, and keep the records that show it. | 3 |
| [AI-CTRL-045](#ai-ctrl-045) | Human Oversight Design and Effectiveness | Governance and Compliance | Design human review so the people named as overseers can understand, challenge, override and stop an AI system, and show with measures that they do. | 4 |
| [AI-CTRL-046](#ai-ctrl-046) | Intellectual Property and Copyright Governance | Governance and Compliance | Control the intellectual property and copyright exposure of AI inputs, outputs and training data. | 4 |

A test case is counted under every control it tests, so the counts add up to more than {{n:tests}}.

## Control entries

### Governance and Compliance

<a id="ai-ctrl-007"></a>

#### AI-CTRL-007: Data Sovereignty

| Field | Detail |
|---|---|
| **Control Objective** | Ensure prompts, logs and uploads are processed and retained in approved locations. |
| **Tier** | Advanced |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents / Vendors |
| **Assurance Stage** | Discovery |
| **Deployment Model** | Cloud |
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
| **ISO/IEC 27001** | A.5.14 Information transfer; A.5.23 Information security for use of cloud services; A.5.31 Legal, statutory, regulatory and contractual requirements; A.5.33 Protection of records; A.8.10 Information deletion |
| **NIST CSF** | GV.OC Organizational Context; GV.SC Cybersecurity Supply Chain Risk Management; PR.DS Data Security |
| **CIS Controls** | CIS 3 Data Protection; CIS 15 Service Provider Management |
| **SOC 2** | C1.1 Identification of confidential information; C1.2 Disposal of confidential information; CC9.2 Vendor and business partner risk; P4.2 Retention |
| **Tested By (15 cases)** | **L03:** [012](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-012), [013](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-013), [014](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-014)<br>**L08:** [001](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-001)<br>**L10:** [012](../10_Test_Case_Library/L10-data-layer.md#tc-l10-012), [013](../10_Test_Case_Library/L10-data-layer.md#tc-l10-013), [014](../10_Test_Case_Library/L10-data-layer.md#tc-l10-014), [015](../10_Test_Case_Library/L10-data-layer.md#tc-l10-015), [025](../10_Test_Case_Library/L10-data-layer.md#tc-l10-025)<br>**L11:** [027](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-027)<br>**L15:** [013](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-013), [014](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-014), [015](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-015), [020](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-020)<br>**L16:** [019](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-019) |

<a id="ai-ctrl-011"></a>

#### AI-CTRL-011: AI Use-Case Registry and Risk Tiering

| Field | Detail |
|---|---|
| **Control Objective** | Record every AI use case with a business owner and a risk tier that decides which controls apply. |
| **Tier** | Baseline |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents / Vendors |
| **Assurance Stage** | Discovery |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R02](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R18](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Require intake and approval before deployment. Record owner, purpose, data, model, users and autonomy for each use case. Assign a risk tier using published criteria, and re-tier when the use case changes. Define what counts as AI use, include third-party and embedded AI, and restrict AI that is not in the registry: block it or treat it as shadow AI to be approved or removed. |
| **Evidence Required** | Use-case registry; intake and approval records; tiering criteria; re-tiering history; rule that restricts unlisted AI and records of its enforcement. |
| **Audit Test Procedure** | Sample use cases in production and confirm each has a registry entry, an owner and a tier consistent with the criteria. Sample registry entries and confirm they match what is deployed. |
| **Control Owner** | AI Governance Lead |
| **Review Frequency** | Quarterly |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-011. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-011. |
| **MITRE ATLAS Mitigations** | None published in MITRE ATLAS mitigations. The wiki's own identifier applies: AI-CTRL-011. |
| **NIST AI RMF** | GOVERN 1.6; GOVERN 1.3; GOVERN 1.7; MAP 1.1 |
| **ISO/IEC 42001** | A.4.2 Resource documentation; A.5.2 AI system impact assessment process; A.9.4 Intended use of the AI system |
| **ISO/IEC 27001** | A.5.8 Information security in project management; A.5.9 Inventory of information and other associated assets; A.5.12 Classification of information |
| **NIST CSF** | GV.RM Risk Management Strategy; ID.AM Asset Management; ID.RA Risk Assessment |
| **CIS Controls** | CIS 1 Inventory and Control of Enterprise Assets; CIS 2 Inventory and Control of Software Assets |
| **SOC 2** | CC3.1 Objectives for risk assessment; CC3.2 Risk identification and analysis |
| **Tested By (19 cases)** | **L01:** [001](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-001), [002](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-002), [003](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-003), [004](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-004), [005](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-005), [006](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-006), [007](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-007), [008](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-008), [009](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-009), [013](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-013), [016](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-016), [019](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-019), [020](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-020)<br>**L03:** [037](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-037)<br>**L05:** [007](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-007), [029](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-029)<br>**L07:** [042](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-042)<br>**L12:** [024](../10_Test_Case_Library/L12-model-layer.md#tc-l12-024), [025](../10_Test_Case_Library/L12-model-layer.md#tc-l12-025) |

<a id="ai-ctrl-012"></a>

#### AI-CTRL-012: AI Policy, Roles and Acceptable Use

| Field | Detail |
|---|---|
| **Control Objective** | Set and communicate the rules and responsibilities for using and building AI, and map each rule to a control. |
| **Tier** | Baseline |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents |
| **Assurance Stage** | Discovery |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R02](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R03](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R18](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R19](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R27](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R28](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Publish an AI policy and acceptable-use standard with scope, owner and review date. Have the board, or the body that holds that authority, approve an AI strategy that states the organization's approach to AI and its AI risk appetite, and review it at least annually. Define roles and decision rights across the three lines, and record governance decisions. Map each policy statement to a control in this library. Train users and reinforce the rules at the point of use. Align the AI policy with the information security, privacy, data and other organizational policies it touches, and record where they overlap or conflict. Include AI acceptable use in terms of employment and contractor agreements, and handle breaches through the existing disciplinary process. |
| **Evidence Required** | Approved policy; board-approved AI strategy and risk appetite with its review record; roles and responsibilities record; governance decision log; policy-to-control mapping; training and acknowledgement records; policy alignment record; employment and contractor terms covering AI use. |
| **Audit Test Procedure** | Select policy statements and trace each to a control and to evidence that it operates. Confirm the policy was reviewed within its cycle. |
| **Control Owner** | GRC |
| **Review Frequency** | Annually |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-012. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-012. |
| **MITRE ATLAS Mitigations** | AML.M0018 User Training |
| **NIST AI RMF** | GOVERN 1.2; GOVERN 1.4; GOVERN 2.1; GOVERN 2.2 |
| **ISO/IEC 42001** | A.2.2 AI policy; A.2.4 Review of the AI policy; A.3.2 AI roles and responsibilities; A.2.3 Alignment with other organizational policies |
| **ISO/IEC 27001** | A.5.1 Policies for information security; A.5.2 Information security roles and responsibilities; A.5.4 Management responsibilities; A.5.10 Acceptable use of information and other associated assets; A.6.2 Terms and conditions of employment; A.6.4 Disciplinary process |
| **NIST CSF** | GV.PO Policy; GV.RR Roles, Responsibilities, and Authorities |
| **CIS Controls** | None published in the CIS Controls. The wiki's own identifier applies: AI-CTRL-012. |
| **SOC 2** | CC1.3 Structures, reporting lines and responsibilities; CC2.2 Internal communication; CC5.3 Policies and procedures |
| **Tested By (8 cases)** | **L02:** [001](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-001), [002](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-002), [004](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-004), [005](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-005), [022](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-022), [023](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-023)<br>**L04:** [011](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-011)<br>**L08:** [043](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-043) |

<a id="ai-ctrl-013"></a>

#### AI-CTRL-013: Privacy and Regulatory Compliance

| Field | Detail |
|---|---|
| **Control Objective** | Meet privacy and regulatory obligations for personal data handled by AI systems. |
| **Tier** | Baseline |
| **Applies To** | Browser AI / AI APIs / Custom AI Applications / Agents / Vendors |
| **Assurance Stage** | Design |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R03](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R10](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R27](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R28](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
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
| **ISO/IEC 27001** | A.5.31 Legal, statutory, regulatory and contractual requirements; A.5.34 Privacy and protection of PII; A.8.10 Information deletion; A.8.11 Data masking |
| **NIST CSF** | GV.OC Organizational Context; PR.DS Data Security |
| **CIS Controls** | CIS 3 Data Protection |
| **SOC 2** | P1.1 Notice; P3.1 Collection; P4.1 Use; P4.2 Retention; P5.1 Access by data subjects |
| **Tested By (41 cases)** | **D11:** [007](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-007), [018](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-018), [019](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-019), [020](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-020)<br>**D12:** [015](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-015), [016](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-016)<br>**L01:** [010](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-010), [011](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-011)<br>**L02:** [020](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-020)<br>**L03:** [001](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-001), [002](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-002), [003](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-003), [004](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-004), [005](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-005), [006](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-006), [007](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-007), [008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008), [009](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-009), [010](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-010), [011](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-011), [015](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-015), [016](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-016), [017](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-017), [018](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-018), [019](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-019), [020](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-020), [028](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-028), [029](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-029), [030](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-030), [036](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-036)<br>**L04:** [027](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-027)<br>**L07:** [030](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-030), [044](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-044), [045](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-045)<br>**L10:** [020](../10_Test_Case_Library/L10-data-layer.md#tc-l10-020), [021](../10_Test_Case_Library/L10-data-layer.md#tc-l10-021), [022](../10_Test_Case_Library/L10-data-layer.md#tc-l10-022)<br>**L13:** [002](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-002), [007](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-007), [019](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-019)<br>**L17:** [026](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-026) |

<a id="ai-ctrl-014"></a>

#### AI-CTRL-014: Third-Party and Vendor AI Assurance

| Field | Detail |
|---|---|
| **Control Objective** | Assess AI vendors and embedded AI features before use, and reassess when they change. |
| **Tier** | Baseline |
| **Applies To** | Vendors / AI APIs / Browser AI |
| **Assurance Stage** | Discovery |
| **Deployment Model** | Cloud |
| **Risk Mapping** | [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R10](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R16](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Evaluate vendors against the vendor evaluation framework. Cover training use of customer data, retention, sub-processors, model changes and incident notification in contracts; by default the contract should bar the provider from using personal or confidential data to train or improve its models unless the organization has authorised it. Include audit rights, a right to have the service suspended, and exit and concentration risk where few providers can replace it. Re-evaluate when a vendor changes model or terms. Treat AI built into other products (document readers, content tools, chat widgets on payment pages) as a third-party service when it can reach sensitive data, list the provider with other service providers, and review its due diligence evidence on a set cycle. At contract end, have the provider return or delete the organization's data, fine-tuned models, embeddings and logs, and get written confirmation. |
| **Evidence Required** | Vendor assessments; contract clauses; sub-processor list; model change notices; exit return or deletion confirmation. |
| **Audit Test Procedure** | Sample AI vendors in use and confirm each has a current assessment and the required contract terms. Confirm the last model or terms change triggered a review. |
| **Control Owner** | Procurement / GRC |
| **Review Frequency** | Annually and on vendor change |
| **OWASP** | LLM03:2025 Supply Chain |
| **MITRE ATLAS Techniques** | AML.T0010 Supply Chain Compromise; AML.T0109 AI Supply Chain Rug Pull |
| **MITRE ATLAS Mitigations** | None published in MITRE ATLAS mitigations. The wiki's own identifier applies: AI-CTRL-014. |
| **NIST AI RMF** | GOVERN 6.1; GOVERN 6.2; MANAGE 3.1 |
| **ISO/IEC 42001** | A.10.2 Allocating responsibilities; A.10.3 Suppliers |
| **ISO/IEC 27001** | A.5.19 Information security in supplier relationships; A.5.20 Addressing information security within supplier agreements; A.5.21 Managing information security in the ICT supply chain; A.5.22 Monitoring, review and change management of supplier services; A.5.23 Information security for use of cloud services; A.5.11 Return of assets |
| **NIST CSF** | GV.SC Cybersecurity Supply Chain Risk Management |
| **CIS Controls** | CIS 15 Service Provider Management |
| **SOC 2** | CC9.2 Vendor and business partner risk |
| **Tested By (26 cases)** | **D09:** [018](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-018)<br>**D12:** [017](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-017)<br>**D13:** [019](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-019)<br>**L01:** [017](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-017)<br>**L02:** [021](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-021)<br>**L03:** [020](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-020), [021](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-021)<br>**L05:** [036](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-036)<br>**L06:** [032](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-032), [043](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-043)<br>**L10:** [025](../10_Test_Case_Library/L10-data-layer.md#tc-l10-025)<br>**L11:** [026](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-026)<br>**L13:** [009](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-009)<br>**L15:** [016](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-016)<br>**L16:** [008](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-008), [009](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-009), [010](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-010), [011](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-011), [012](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-012), [018](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-018), [019](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-019), [020](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-020), [021](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-021), [022](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-022), [023](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-023), [025](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-025) |

<a id="ai-ctrl-037"></a>

#### AI-CTRL-037: AI Risk Assessment and Exception Management

| Field | Detail |
|---|---|
| **Control Objective** | Assess, treat and accept AI risks consistently, and keep every exception owned and time-bound. |
| **Tier** | Advanced |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents / Vendors |
| **Assurance Stage** | Design |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R02](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R18](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R28](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R55](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Keep an AI risk register with an owner and a score for every risk. Use one scoring method so that different assessors reach the same result. Accept residual risk only at the right authority level. Give every exception an owner, a compensating control and an expiry date that the technical control enforces. Allow for attackers who use AI: set remediation and exception time limits for exposed systems on the assumption that a disclosed vulnerability can be exploited within days, and size vulnerability triage for a higher volume of findings (AI-R55). |
| **Evidence Required** | AI risk register; treatment plans; risk acceptance records; exception register with expiry dates. |
| **Audit Test Procedure** | Sample accepted risks and confirm the approver had the authority. Let a test exception expire and confirm the technical control blocks the activity again. |
| **Control Owner** | Cyber Risk / GRC |
| **Review Frequency** | Quarterly |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-037. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-037. |
| **MITRE ATLAS Mitigations** | None published in MITRE ATLAS mitigations. The wiki's own identifier applies: AI-CTRL-037. |
| **NIST AI RMF** | GOVERN 1.3; MAP 1.5; MANAGE 1.2; MANAGE 1.4 |
| **ISO/IEC 42001** | Clause 6.1.2 AI risk assessment; Clause 6.1.3 AI risk treatment |
| **ISO/IEC 27001** | Clause 6.1.2 Information security risk assessment; Clause 6.1.3 Information security risk treatment |
| **NIST CSF** | GV.RM Risk Management Strategy; ID.RA Risk Assessment |
| **CIS Controls** | None published in the CIS Controls. The wiki's own identifier applies: AI-CTRL-037. |
| **SOC 2** | CC3.1 Objectives for risk assessment; CC3.2 Risk identification and analysis; CC9.1 Risk mitigation for business disruption |
| **Tested By (10 cases)** | **L02:** [006](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-006), [007](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-007), [008](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-008), [009](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-009), [010](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-010), [011](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-011), [012](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-012)<br>**L04:** [013](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-013), [014](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-014), [015](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-015) |

<a id="ai-ctrl-042"></a>

#### AI-CTRL-042: Fundamental Rights and Data Protection Impact Assessment

| Field | Detail |
|---|---|
| **Control Objective** | Assess the impact on people's rights before deploying AI that is high-risk or that puts personal data at risk, and keep the assessment current. |
| **Tier** | Advanced |
| **Applies To** | AI APIs / Custom AI Applications / Agents / Vendors |
| **Assurance Stage** | Design |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R10](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R12](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R28](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Run a combined data protection and fundamental rights impact assessment before go-live for in-scope systems. Record purpose, data, groups affected, risks, oversight, mitigation, consultation and decision. Include intended and reasonably foreseeable unintended uses and misuse, the deployment regions and languages, the data and its quality, and benefits as well as harms, as listed in ISO/IEC 42005:2025 clause 6. Record the data protection officer's advice and how it was handled. Reassess on material change and at least annually. |
| **Evidence Required** | Completed assessments; data protection officer advice; approvals dated before go-live; review dates; reassessment records. |
| **Audit Test Procedure** | Sample in-scope systems and confirm the assessment predates go-live. Check that each risk maps to a mitigation. Confirm that the last material change triggered a reassessment. |
| **Control Owner** | Data Protection Officer / AI Governance Lead |
| **Review Frequency** | Before deployment, annually and on material change |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-042. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-042. |
| **MITRE ATLAS Mitigations** | None published in MITRE ATLAS mitigations. The wiki's own identifier applies: AI-CTRL-042. |
| **NIST AI RMF** | MAP 5.1; MAP 1.1; GOVERN 1.1 |
| **ISO/IEC 42001** | A.5.2 AI system impact assessment process; A.5.3 Documentation of AI system impact assessments; A.5.4 Assessing AI system impact on individuals or groups of individuals; A.5.5 Assessing societal impacts of AI systems |
| **ISO/IEC 27001** | A.5.8 Information security in project management; A.5.31 Legal, statutory, regulatory and contractual requirements; A.5.34 Privacy and protection of PII |
| **NIST CSF** | GV.OC Organizational Context; ID.RA Risk Assessment |
| **CIS Controls** | None published in the CIS Controls. The wiki's own identifier applies: AI-CTRL-042. |
| **SOC 2** | CC3.2 Risk identification and analysis |
| **Tested By (4 cases)** | **L03:** [010](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-010), [011](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-011), [034](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-034), [044](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-044) |

<a id="ai-ctrl-043"></a>

#### AI-CTRL-043: Regulator and Authority Engagement

| Field | Detail |
|---|---|
| **Control Objective** | Know which authorities oversee each AI system, meet the registration, filing and notification duties they set, and keep a record of every contact. |
| **Tier** | Advanced |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents / Vendors |
| **Assurance Stage** | Production |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R09](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R10](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Keep a register of the authorities and ethics bodies relevant to each AI system and jurisdiction, with the duties each one sets and an owner for each duty. Track filings, registrations and local representative appointments to their due dates. Log every contact and its outcome. Watch for new guidance and pending rules, and review the register on a schedule. Keep contact with AI security interest groups and information-sharing communities, and record what is shared with them. |
| **Evidence Required** | Authority register; filing and registration records; representative appointments; contact log; watchlist of pending rules. |
| **Audit Test Procedure** | Sample AI systems and confirm each lists its authorities and duties. Trace one filing or notification to its due date and evidence. Confirm the register was reviewed in the period. |
| **Control Owner** | Legal / Compliance |
| **Review Frequency** | Quarterly |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-043. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-043. |
| **MITRE ATLAS Mitigations** | None published in MITRE ATLAS mitigations. The wiki's own identifier applies: AI-CTRL-043. |
| **NIST AI RMF** | GOVERN 1.1; GOVERN 5.1 |
| **ISO/IEC 42001** | Clause 4.2 Understanding the needs and expectations of interested parties; A.8.3 External reporting; A.8.5 Information for interested parties |
| **ISO/IEC 27001** | A.5.5 Contact with authorities; A.5.31 Legal, statutory, regulatory and contractual requirements; A.5.6 Contact with special interest groups |
| **NIST CSF** | GV.OC Organizational Context; RS.CO Incident Response Reporting and Communication |
| **CIS Controls** | CIS 17 Incident Response Management |
| **SOC 2** | CC2.3 External communication |
| **Tested By (4 cases)** | **D12:** [016](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-016)<br>**L02:** [020](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-020)<br>**L03:** [019](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-019), [039](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-039) |

<a id="ai-ctrl-044"></a>

#### AI-CTRL-044: AI Literacy and Role-Based Competence

| Field | Detail |
|---|---|
| **Control Objective** | Give everyone who builds, operates, oversees or uses AI the knowledge their role needs, and keep the records that show it. |
| **Tier** | Advanced |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R02](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R19](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Define the knowledge each role group needs, from board members to human reviewers and contractors. Deliver role-based training on a schedule and when a role or a system changes. Record completion and results. Check that the training works, for example through scenario tests and reviewer override rates. |
| **Evidence Required** | Role and needs matrix; programme and modules; completion records; effectiveness checks. |
| **Audit Test Procedure** | Sample staff in three role groups and confirm each completed training that matches the role. Confirm human reviewers were trained before they were assigned. Review one effectiveness check. |
| **Control Owner** | AI Governance Lead / HR |
| **Review Frequency** | Annually and on role change |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-044. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-044. |
| **MITRE ATLAS Mitigations** | None published in MITRE ATLAS mitigations. The wiki's own identifier applies: AI-CTRL-044. |
| **NIST AI RMF** | GOVERN 2.2; MAP 3.4 |
| **ISO/IEC 42001** | Clause 7.2 Competence; Clause 7.3 Awareness; A.4.6 Human resources |
| **ISO/IEC 27001** | A.6.3 Information security awareness, education and training |
| **NIST CSF** | PR.AT Awareness and Training |
| **CIS Controls** | CIS 14 Security Awareness and Skills Training |
| **SOC 2** | CC1.4 Competence; CC2.2 Internal communication |
| **Tested By (3 cases)** | **L02:** [022](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-022)<br>**L03:** [038](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-038), [045](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-045) |

<a id="ai-ctrl-045"></a>

#### AI-CTRL-045: Human Oversight Design and Effectiveness

| Field | Detail |
|---|---|
| **Control Objective** | Design human review so the people named as overseers can understand, challenge, override and stop an AI system, and show with measures that they do. |
| **Tier** | Advanced |
| **Applies To** | Custom AI Applications / Agents / Vendors |
| **Assurance Stage** | Design |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R12](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R14](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R18](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R19](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R28](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Set, by risk tier, where a person must review, approve or be able to intervene: before the output is used, while the system runs, and after the fact by sampling. Give each overseer the evidence behind the output (sources, confidence, alternatives) and not only the result, the authority and time to override, and training that matches the role ([AI-CTRL-044](#ai-ctrl-044)). Keep the volume per reviewer low enough to be reviewed, and give overseers a way to stop or roll back the system ([AI-CTRL-025](#ai-ctrl-025)). Measure effectiveness: override and escalation rates, time per review, results of independent re-review of a sample, and detection of seeded errors. Reassess the design when the measures show rubber-stamping. This control covers oversight of AI-assisted decisions in general; [AI-CTRL-023](#ai-ctrl-023) gates specific irreversible agent actions. Before an agent may act without per-action approval (a person over the loop rather than in it), record and approve: why per-action approval is not workable, the responsible person and why they are suited, which actions run without approval, the minimum privileges, how output is validated, how actions are logged and how often logs are reviewed, how the agent is disabled and on what triggers, and how its actions are reversed. Keep per-action approval for any action involving cleartext payment card data. |
| **Evidence Required** | Oversight design record per in-scope use case; overseer roles, authority and training records; sampled re-review results; override and escalation metrics; seeded-error test results. |
| **Audit Test Procedure** | Select a high-tier use case and compare the oversight points in operation with the design record. Interview two overseers about the evidence they see and their authority to override. Submit a set of known-wrong outputs and measure how many are caught. Confirm the overseers can stop the system and that override metrics are reviewed. |
| **Control Owner** | AI Governance Lead / Application Owner |
| **Review Frequency** | Semi-annually and on material change |
| **Regulatory Pointers** | EU AI Act Article 14 (Human Oversight) and Article 26(2) (deployers assign oversight to competent, trained people with authority and support); GDPR Article 22 (Automated individual decision-making, including profiling). GCC: see rows U3, U6, U9 and Q4 of the [GCC AI Regulatory Hub](../11_GCC_AI_Compliance/01_GCC_AI_Regulatory_Hub.md). Article titles and paragraph content were checked on 10 October 2026 against a secondary source (artificialintelligenceact.eu) that shows amended text; check the Official Journal text before citing. |
| **OWASP** | LLM06:2025 Excessive Agency; ASI09 Human-Agent Trust Exploitation |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-045. |
| **MITRE ATLAS Mitigations** | AML.M0029 Human In-the-Loop for AI Agent Actions |
| **NIST AI RMF** | MAP 3.5; GOVERN 3.2 |
| **ISO/IEC 42001** | A.9.2 Processes for responsible use of AI systems; A.9.3 Objectives for responsible use of AI system |
| **ISO/IEC 27001** | None published in ISO/IEC 27001 Annex A. The wiki's own identifier applies: AI-CTRL-045. |
| **NIST CSF** | GV.RR Roles, Responsibilities, and Authorities |
| **CIS Controls** | None published in the CIS Controls. The wiki's own identifier applies: AI-CTRL-045. |
| **SOC 2** | None published in the SOC 2 criteria. The wiki's own identifier applies: AI-CTRL-045. |
| **Tested By (4 cases)** | **L01:** [012](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-012), [022](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-022)<br>**L03:** [040](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-040), [041](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-041) |

<a id="ai-ctrl-046"></a>

#### AI-CTRL-046: Intellectual Property and Copyright Governance

| Field | Detail |
|---|---|
| **Control Objective** | Control the intellectual property and copyright exposure of AI inputs, outputs and training data. |
| **Tier** | Advanced |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Vendors |
| **Assurance Stage** | Design |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R27](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Set a policy on what third-party copyrighted or licensed material staff may submit to AI tools, and on how AI output may be used in products, code and publications. Review vendor terms for ownership of output, indemnity for infringement claims and use of inputs for training. Record the source and licence of training and fine-tuning data ([AI-CTRL-029](#ai-ctrl-029)). Where policy requires, scan AI-generated code and content for licence and similarity matches before release. Record exceptions with an owner and an expiry date. |
| **Evidence Required** | IP and acceptable-use policy; vendor terms review; training data provenance and licence records; scan results; exception log. |
| **Audit Test Procedure** | Sample vendors and confirm the terms were reviewed for output ownership and indemnity. Sample released AI-generated artefacts and confirm a scan result or a documented exception. Sample fine-tuning datasets and confirm source and licence are recorded. |
| **Control Owner** | Legal / Compliance |
| **Review Frequency** | Annually and when vendor terms change |
| **Regulatory Pointers** | EU AI Act Article 53(1): providers of general-purpose AI models keep a copyright compliance policy and publish a summary of training content (checked on 10 October 2026 against artificialintelligenceact.eu, a secondary source). GCC: row S9 of the [GCC AI Regulatory Hub](../11_GCC_AI_Compliance/01_GCC_AI_Regulatory_Hub.md) (Saudi copyright exception for text and data mining, tagged [Reported]). |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-046. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-046. |
| **MITRE ATLAS Mitigations** | None published in MITRE ATLAS mitigations. The wiki's own identifier applies: AI-CTRL-046. |
| **NIST AI RMF** | MAP 4.1 |
| **ISO/IEC 42001** | A.7.5 Data provenance; A.10.3 Suppliers |
| **ISO/IEC 27001** | A.5.20 Addressing information security within supplier agreements; A.5.31 Legal, statutory, regulatory and contractual requirements; A.5.32 Intellectual property rights |
| **NIST CSF** | GV.OC Organizational Context |
| **CIS Controls** | None published in the CIS Controls. The wiki's own identifier applies: AI-CTRL-046. |
| **SOC 2** | None published in the SOC 2 criteria. The wiki's own identifier applies: AI-CTRL-046. |
| **Tested By (4 cases)** | **L03:** [028](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-028), [042](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-042)<br>**L05:** [035](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-035)<br>**L13:** [007](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-007) |

### Discovery and Workforce AI Use

<a id="ai-ctrl-001"></a>

#### AI-CTRL-001: AI Discovery

| Field | Detail |
|---|---|
| **Control Objective** | Identify approved/unapproved AI platforms across browsers, endpoints, IDEs, SaaS, APIs and custom apps. |
| **Tier** | Baseline |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents |
| **Assurance Stage** | Discovery |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R02](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Discover AI services, extensions, plugins, embedded SaaS AI features and API usage continuously. Classify each as approved, tolerated or unapproved, and attribute use to a user, device and application. Look for local models and agents and for AI add-ons such as browser extensions and IDE plug-ins on endpoints, use software allow-listing to stop unapproved installs, and watch network traffic for AI patterns such as Model Context Protocol (MCP) connections. Policy and training alone do not stop shadow AI. |
| **Evidence Required** | AI service inventory; usage dashboard; user and device reports; classification of each service. |
| **Audit Test Procedure** | Seed a known set of approved and unapproved AI tools in a test group and compare the discovered inventory with ground truth. Confirm new tools appear within the stated interval. |
| **Control Owner** | Security Engineering |
| **Review Frequency** | Quarterly |
| **OWASP** | LLM03:2025 Supply Chain |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-001. |
| **MITRE ATLAS Mitigations** | None published in MITRE ATLAS mitigations. The wiki's own identifier applies: AI-CTRL-001. |
| **NIST AI RMF** | GOVERN 1.6; GOVERN 6.1 |
| **ISO/IEC 42001** | A.4.2 Resource documentation |
| **ISO/IEC 27001** | A.5.9 Inventory of information and other associated assets; A.8.16 Monitoring activities; A.8.23 Web filtering; A.8.1 User endpoint devices |
| **NIST CSF** | ID.AM Asset Management; DE.CM Continuous Monitoring |
| **CIS Controls** | CIS 1 Inventory and Control of Enterprise Assets; CIS 2 Inventory and Control of Software Assets; CIS 9 Email and Web Browser Protections |
| **SOC 2** | CC6.8 Unauthorized or malicious software; CC7.2 Monitoring for anomalies |
| **Tested By (33 cases)** | **D10:** [001](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-001), [022](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-022)<br>**D11:** [001](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-001)<br>**D13:** [017](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-017)<br>**L01:** [008](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-008)<br>**L04:** [001](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-001), [002](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-002), [003](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-003), [004](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-004), [005](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-005), [006](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-006), [007](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-007), [008](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-008), [009](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-009), [010](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-010), [024](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-024), [025](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-025)<br>**L05:** [001](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-001), [002](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-002), [003](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-003), [004](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-004), [005](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-005), [006](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-006), [007](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-007), [008](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-008), [009](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-009), [011](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-011), [029](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-029)<br>**L11:** [001](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-001)<br>**L12:** [001](../10_Test_Case_Library/L12-model-layer.md#tc-l12-001)<br>**L14:** [001](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-001), [018](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-018)<br>**L15:** [001](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-001) |

<a id="ai-ctrl-002"></a>

#### AI-CTRL-002: Prompt Inspection

| Field | Detail |
|---|---|
| **Control Objective** | Detect sensitive, restricted or risky content submitted to AI platforms. |
| **Tier** | Baseline |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R01](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R03](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R27](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
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
| **ISO/IEC 27001** | A.5.12 Classification of information; A.8.11 Data masking; A.8.12 Data leakage prevention; A.8.1 User endpoint devices |
| **NIST CSF** | PR.DS Data Security; DE.CM Continuous Monitoring |
| **CIS Controls** | CIS 3 Data Protection |
| **SOC 2** | CC6.7 Transmission, movement and removal of information; C1.1 Identification of confidential information |
| **Tested By (16 cases)** | **D11:** [006](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-006), [015](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-015), [016](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-016)<br>**L04:** [012](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-012), [017](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-017), [019](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-019), [028](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-028)<br>**L08:** [004](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-004), [005](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-005), [006](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-006), [007](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-007), [008](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-008), [010](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-010), [011](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-011), [014](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-014), [027](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-027) |

<a id="ai-ctrl-003"></a>

#### AI-CTRL-003: File Upload Protection

| Field | Detail |
|---|---|
| **Control Objective** | Prevent uploads of confidential or restricted files to unauthorized AI services. |
| **Tier** | Advanced |
| **Applies To** | Browser AI / AI APIs / Custom AI Applications |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R01](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R03](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R27](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
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
| **ISO/IEC 27001** | A.5.10 Acceptable use of information and other associated assets; A.5.14 Information transfer; A.8.12 Data leakage prevention |
| **NIST CSF** | PR.DS Data Security |
| **CIS Controls** | CIS 3 Data Protection; CIS 9 Email and Web Browser Protections |
| **SOC 2** | CC6.7 Transmission, movement and removal of information; C1.1 Identification of confidential information |
| **Tested By (6 cases)** | **D10:** [009](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-009)<br>**L04:** [018](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-018), [020](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-020), [022](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-022)<br>**L08:** [012](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-012), [013](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-013) |

<a id="ai-ctrl-004"></a>

#### AI-CTRL-004: IDE AI Governance

| Field | Detail |
|---|---|
| **Control Objective** | Monitor and control AI coding assistants, source code sharing and secret leakage. |
| **Tier** | Advanced |
| **Applies To** | IDE AI |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R04](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R22](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
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
| **ISO/IEC 27001** | A.8.4 Access to source code; A.8.12 Data leakage prevention; A.8.28 Secure coding; A.8.1 User endpoint devices |
| **NIST CSF** | PR.DS Data Security; PR.PS Platform Security |
| **CIS Controls** | CIS 3 Data Protection; CIS 16 Application Software Security |
| **SOC 2** | CC6.7 Transmission, movement and removal of information; CC8.1 Change management |
| **Tested By (19 cases)** | **L04:** [019](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-019), [031](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-031), [032](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-032)<br>**L05:** [004](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-004), [031](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-031), [032](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-032), [033](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-033), [034](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-034), [035](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-035)<br>**L06:** [037](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-037)<br>**L07:** [041](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-041)<br>**L08:** [007](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-007), [041](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-041), [042](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-042)<br>**L09:** [026](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-026)<br>**L14:** [021](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-021), [024](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-024)<br>**L16:** [026](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-026)<br>**L17:** [031](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-031) |

<a id="ai-ctrl-010"></a>

#### AI-CTRL-010: Policy Enforcement

| Field | Detail |
|---|---|
| **Control Objective** | Support monitor, warn, redact, block and allow policies based on risk and classification. |
| **Tier** | Advanced |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
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
| **ISO/IEC 27001** | A.5.10 Acceptable use of information and other associated assets; A.5.12 Classification of information; A.8.12 Data leakage prevention; A.8.23 Web filtering |
| **NIST CSF** | GV.PO Policy; PR.DS Data Security |
| **CIS Controls** | CIS 3 Data Protection; CIS 9 Email and Web Browser Protections |
| **SOC 2** | CC5.3 Policies and procedures; CC6.7 Transmission, movement and removal of information |
| **Tested By (28 cases)** | **L02:** [011](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-011)<br>**L04:** [009](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-009), [011](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-011), [012](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-012), [013](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-013), [016](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-016), [025](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-025), [026](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-026), [029](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-029)<br>**L05:** [028](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-028)<br>**L08:** [001](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-001), [002](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-002), [003](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-003), [009](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-009), [010](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-010), [021](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-021), [022](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-022), [023](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-023), [024](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-024), [025](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-025), [026](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-026), [028](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-028), [036](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-036), [037](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-037), [038](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-038), [041](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-041), [043](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-043)<br>**L12:** [021](../10_Test_Case_Library/L12-model-layer.md#tc-l12-021) |

### Identity and Access

<a id="ai-ctrl-015"></a>

#### AI-CTRL-015: Human and Agent Identity

| Field | Detail |
|---|---|
| **Control Objective** | Give every user, application and agent that uses AI a unique, attributable identity. |
| **Tier** | Baseline |
| **Applies To** | AI APIs / Custom AI Applications / Agents |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R22](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R25](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Issue a unique identity to each agent and AI workload, with a named human sponsor. Do not share keys between workloads. Recertify identities on a schedule and remove them when the sponsor leaves or the use case ends. Authenticate agents to each other and sign the messages they exchange, so that one agent cannot pass as another. Give training jobs, pipelines and model-serving processes their own workload identities. An agent cannot provide a possession or inherence factor, so it cannot perform multi-factor authentication. Where a person would need MFA for the same access, give the agent a device-bound credential, preferably cryptographic (for example a device-specific certificate over mutual TLS), limited in time and never reusable by another system or person, and never use the agent to get around an MFA requirement. |
| **Evidence Required** | Identity registry; sponsor records; recertification results; orphaned identity report. |
| **Audit Test Procedure** | Sample agent identities and confirm each has a sponsor and a current recertification. Remove a test sponsor and confirm the agent identity is flagged. |
| **Control Owner** | IAM Team |
| **Review Frequency** | Semi-annually |
| **OWASP** | LLM06:2025 Excessive Agency; ASI03 Identity & Privilege Abuse; ASI07 Insecure Inter-Agent Communication |
| **MITRE ATLAS Techniques** | AML.T0012 Valid Accounts; AML.T0073 Impersonation; AML.T0091 Use Alternate Authentication Material |
| **MITRE ATLAS Mitigations** | AML.M0019 Control Access to AI Models and Data in Production |
| **NIST AI RMF** | MEASURE 2.7; MEASURE 2.8 |
| **ISO/IEC 42001** | None published in ISO/IEC 42001. The wiki's own identifier applies: AI-CTRL-015. |
| **ISO/IEC 27001** | A.5.16 Identity management; A.5.17 Authentication information; A.8.5 Secure authentication |
| **NIST CSF** | PR.AA Identity Management, Authentication, and Access Control |
| **CIS Controls** | CIS 5 Account Management; CIS 6 Access Control Management |
| **SOC 2** | CC6.1 Logical access security; CC6.2 Registration and removal of access |
| **Tested By (45 cases)** | **D09:** [001](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-001), [002](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-002), [003](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-003), [004](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-004), [008](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-008), [011](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-011), [012](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-012), [013](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-013), [015](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-015), [016](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-016), [017](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-017), [018](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-018), [019](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-019), [020](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-020)<br>**D10:** [015](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-015)<br>**D11:** [017](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-017)<br>**L04:** [030](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-030)<br>**L06:** [010](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-010), [018](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-018), [035](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-035), [038](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-038), [041](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-041), [042](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-042), [043](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-043)<br>**L09:** [001](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-001), [002](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-002), [010](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-010), [011](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-011), [012](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-012), [017](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-017), [018](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-018), [020](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-020), [021](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-021), [024](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-024), [025](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-025), [027](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-027)<br>**L12:** [013](../10_Test_Case_Library/L12-model-layer.md#tc-l12-013), [026](../10_Test_Case_Library/L12-model-layer.md#tc-l12-026), [027](../10_Test_Case_Library/L12-model-layer.md#tc-l12-027), [030](../10_Test_Case_Library/L12-model-layer.md#tc-l12-030), [031](../10_Test_Case_Library/L12-model-layer.md#tc-l12-031)<br>**L13:** [021](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-021), [024](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-024), [025](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-025), [026](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-026) |

<a id="ai-ctrl-016"></a>

#### AI-CTRL-016: Least Privilege and Scoped Credentials

| Field | Detail |
|---|---|
| **Control Objective** | Limit what each AI workload and agent can reach to the minimum its task needs. |
| **Tier** | Baseline |
| **Applies To** | AI APIs / Custom AI Applications / Agents |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R06](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R22](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Use short-lived credentials scoped per tool and resource. Act with the end user's rights where a user is present, not with a broad service account. Detect and correct permission drift. Keep secrets out of locations an agent can read, such as environment variables, configuration files and shell history; issue short-lived tokens scoped to one task at the moment of the call; and plant canary credentials to detect an agent searching for credentials it was never given. Apply the same limits to training jobs, pipelines and model-serving identities: scope them to the datasets and models the task names, and revoke them when the job ends. |
| **Evidence Required** | Permission maps; token scope configuration; access review records; drift reports. |
| **Audit Test Procedure** | Have a test agent attempt a tool or resource outside its scope and confirm it is denied and logged. Confirm credentials expire as configured. |
| **Control Owner** | IAM Team |
| **Review Frequency** | Quarterly |
| **OWASP** | LLM06:2025 Excessive Agency; ASI03 Identity & Privilege Abuse |
| **MITRE ATLAS Techniques** | AML.T0012 Valid Accounts; AML.T0055 Unsecured Credentials; AML.T0083 Credentials from AI Agent Configuration; AML.T0098 AI Agent Tool Credential Harvesting |
| **MITRE ATLAS Mitigations** | AML.M0026 Manage AI Agent Service Access; AML.M0027 Manage User-Delegated AI Agent Access; AML.M0028 Enforce Access Controls for AI Agent Tools |
| **NIST AI RMF** | MEASURE 2.7; MANAGE 1.3 |
| **ISO/IEC 42001** | None published in ISO/IEC 42001. The wiki's own identifier applies: AI-CTRL-016. |
| **ISO/IEC 27001** | A.5.15 Access control; A.5.18 Access rights; A.8.2 Privileged access rights; A.8.3 Information access restriction |
| **NIST CSF** | PR.AA Identity Management, Authentication, and Access Control |
| **CIS Controls** | CIS 5 Account Management; CIS 6 Access Control Management |
| **SOC 2** | CC6.1 Logical access security; CC6.3 Role-based access and least privilege |
| **Tested By (53 cases)** | **D09:** [005](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-005), [006](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-006), [007](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-007), [009](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-009), [010](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-010), [014](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-014)<br>**D10:** [003](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-003), [021](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-021)<br>**D13:** [005](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-005)<br>**L05:** [010](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-010)<br>**L06:** [012](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-012), [013](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-013), [017](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-017), [019](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-019), [039](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-039), [044](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-044), [047](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-047)<br>**L07:** [039](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-039)<br>**L08:** [029](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-029), [039](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-039)<br>**L09:** [003](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-003), [004](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-004), [005](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-005), [006](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-006), [007](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-007), [008](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-008), [009](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-009), [013](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-013), [014](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-014), [015](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-015), [016](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-016), [019](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-019), [022](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-022), [023](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-023), [026](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-026), [027](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-027)<br>**L10:** [017](../10_Test_Case_Library/L10-data-layer.md#tc-l10-017), [034](../10_Test_Case_Library/L10-data-layer.md#tc-l10-034)<br>**L11:** [022](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-022)<br>**L12:** [014](../10_Test_Case_Library/L12-model-layer.md#tc-l12-014), [026](../10_Test_Case_Library/L12-model-layer.md#tc-l12-026), [028](../10_Test_Case_Library/L12-model-layer.md#tc-l12-028), [029](../10_Test_Case_Library/L12-model-layer.md#tc-l12-029), [030](../10_Test_Case_Library/L12-model-layer.md#tc-l12-030)<br>**L13:** [008](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-008), [021](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-021), [022](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-022), [023](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-023), [024](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-024)<br>**L14:** [004](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-004), [008](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-008), [022](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-022)<br>**L15:** [010](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-010) |

### Data and Retrieval

<a id="ai-ctrl-017"></a>

#### AI-CTRL-017: Data Protection in AI Pipelines

| Field | Detail |
|---|---|
| **Control Objective** | Apply classification, minimization and isolation to data that AI systems ingest, process and produce. |
| **Tier** | Baseline |
| **Applies To** | AI APIs / Custom AI Applications / Agents |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R01](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R03](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R06](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R17](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Carry data classification into AI pipelines. Minimize or mask sensitive fields before they reach a model. Keep tenants separate in indexes, caches, memory and logs, and record data lineage. Never give a model or agent cleartext high-impact secrets (cryptographic keys, key components, passwords) or ask it to generate them or the random values behind them; route cryptography through a key service or HSM interface that exposes only the keys and functions the task needs. Judge the data an AI system can reach by what it could obtain, not what it is meant to use: tokens or encrypted data plus a reachable detokenisation, decryption or access-management path count as cleartext. Show in the data flow diagrams the data stores AI operation creates (prompt and response logs, transcripts, caches, retrieved context, tool results, agent scratchpads, orchestration state) and mask sensitive values before they are written. |
| **Evidence Required** | Data flow diagrams; classification and masking rules; tenant isolation tests; lineage records. |
| **Audit Test Procedure** | Send labelled sensitive records through the pipeline and confirm masking at each stage. Attempt to read another tenant's data through the AI interface. |
| **Control Owner** | Data Owner / Security Engineering |
| **Review Frequency** | Semi-annually |
| **OWASP** | LLM02:2025 Sensitive Information Disclosure |
| **MITRE ATLAS Techniques** | AML.T0057 LLM Data Leakage; AML.T0085 Data from AI Services; AML.T0025 Exfiltration via Cyber Means |
| **MITRE ATLAS Mitigations** | AML.M0012 Encrypt Sensitive Information; AML.M0005 Control Access to AI Models and Data at Rest |
| **NIST AI RMF** | MEASURE 2.10; MEASURE 2.7 |
| **ISO/IEC 42001** | A.4.3 Data resources; A.7.6 Data preparation |
| **ISO/IEC 27001** | A.5.12 Classification of information; A.5.13 Labelling of information; A.8.10 Information deletion; A.8.11 Data masking; A.8.12 Data leakage prevention; A.8.24 Use of cryptography; A.8.33 Test information |
| **NIST CSF** | ID.AM Asset Management; PR.DS Data Security |
| **CIS Controls** | CIS 3 Data Protection |
| **SOC 2** | CC6.1 Logical access security; CC6.7 Transmission, movement and removal of information; C1.1 Identification of confidential information; C1.2 Disposal of confidential information |
| **Tested By (39 cases)** | **D08:** [023](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-023)<br>**D10:** [017](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-017)<br>**D11:** [022](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-022)<br>**L03:** [015](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-015), [018](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-018)<br>**L05:** [023](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-023)<br>**L06:** [044](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-044)<br>**L07:** [043](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-043)<br>**L08:** [040](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-040), [044](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-044)<br>**L10:** [001](../10_Test_Case_Library/L10-data-layer.md#tc-l10-001), [002](../10_Test_Case_Library/L10-data-layer.md#tc-l10-002), [003](../10_Test_Case_Library/L10-data-layer.md#tc-l10-003), [004](../10_Test_Case_Library/L10-data-layer.md#tc-l10-004), [005](../10_Test_Case_Library/L10-data-layer.md#tc-l10-005), [007](../10_Test_Case_Library/L10-data-layer.md#tc-l10-007), [008](../10_Test_Case_Library/L10-data-layer.md#tc-l10-008), [009](../10_Test_Case_Library/L10-data-layer.md#tc-l10-009), [010](../10_Test_Case_Library/L10-data-layer.md#tc-l10-010), [011](../10_Test_Case_Library/L10-data-layer.md#tc-l10-011), [015](../10_Test_Case_Library/L10-data-layer.md#tc-l10-015), [016](../10_Test_Case_Library/L10-data-layer.md#tc-l10-016), [020](../10_Test_Case_Library/L10-data-layer.md#tc-l10-020), [023](../10_Test_Case_Library/L10-data-layer.md#tc-l10-023), [029](../10_Test_Case_Library/L10-data-layer.md#tc-l10-029), [034](../10_Test_Case_Library/L10-data-layer.md#tc-l10-034), [035](../10_Test_Case_Library/L10-data-layer.md#tc-l10-035)<br>**L11:** [007](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-007), [012](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-012), [015](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-015), [023](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-023), [027](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-027)<br>**L12:** [033](../10_Test_Case_Library/L12-model-layer.md#tc-l12-033), [034](../10_Test_Case_Library/L12-model-layer.md#tc-l12-034)<br>**L13:** [006](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-006), [009](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-009)<br>**L14:** [015](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-015)<br>**L15:** [012](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-012)<br>**L17:** [032](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-032) |

<a id="ai-ctrl-018"></a>

#### AI-CTRL-018: Retrieval Access Control

| Field | Detail |
|---|---|
| **Control Objective** | Return only content the requesting user is entitled to see. |
| **Tier** | Baseline |
| **Applies To** | Custom AI Applications / Agents |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R06](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Enforce document-level permissions at query time using the end user's identity. Propagate permission changes to the index promptly. Do not rely on the model to withhold content. Return citations that users can check. |
| **Evidence Required** | Permission test results; retrieval logs with source documents; propagation timing. |
| **Audit Test Procedure** | Query as users with different entitlements and confirm restricted documents are never retrieved. Revoke access to a document and measure how long it remains retrievable. |
| **Control Owner** | Application Owner |
| **Review Frequency** | Quarterly |
| **OWASP** | LLM08:2025 Vector and Embedding Weaknesses; LLM02:2025 Sensitive Information Disclosure |
| **MITRE ATLAS Techniques** | AML.T0057 LLM Data Leakage; AML.T0085 Data from AI Services; AML.T0064 Gather RAG-Indexed Targets; AML.T0082 RAG Credential Harvesting |
| **MITRE ATLAS Mitigations** | AML.M0027 Manage User-Delegated AI Agent Access; AML.M0019 Control Access to AI Models and Data in Production |
| **NIST AI RMF** | MEASURE 2.10; MEASURE 2.7 |
| **ISO/IEC 42001** | None published in ISO/IEC 42001. The wiki's own identifier applies: AI-CTRL-018. |
| **ISO/IEC 27001** | A.5.15 Access control; A.8.3 Information access restriction |
| **NIST CSF** | PR.AA Identity Management, Authentication, and Access Control; PR.DS Data Security |
| **CIS Controls** | CIS 3 Data Protection; CIS 6 Access Control Management |
| **SOC 2** | CC6.1 Logical access security; CC6.3 Role-based access and least privilege |
| **Tested By (10 cases)** | **L10:** [006](../10_Test_Case_Library/L10-data-layer.md#tc-l10-006), [018](../10_Test_Case_Library/L10-data-layer.md#tc-l10-018), [019](../10_Test_Case_Library/L10-data-layer.md#tc-l10-019)<br>**L11:** [004](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-004), [005](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-005), [006](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-006), [007](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-007), [016](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-016), [019](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-019), [028](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-028) |

<a id="ai-ctrl-019"></a>

#### AI-CTRL-019: Knowledge Base Integrity

| Field | Detail |
|---|---|
| **Control Objective** | Stop untrusted or poisoned content from entering the corpus that AI systems retrieve from. |
| **Tier** | Advanced |
| **Applies To** | Custom AI Applications / Agents |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R05](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R17](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Control who and what can write to the corpus. Record the source of every indexed item. Scan ingested content for embedded instructions, and keep the ability to find and remove items by source. Record an owner and a freshness limit for each source, and monitor retrieval quality for drift so that superseded or degraded content is found and removed. Measure the corpus against data quality thresholds for currentness, credibility of source and duplication, so that stale or low-quality content is treated as a defect and not only tampering. |
| **Evidence Required** | Ingestion access list; provenance records; ingestion scan results; removal test. |
| **Audit Test Procedure** | Add a document with a planted instruction and a false fact through each ingestion path. Confirm it is detected or neutralized, and that it can be traced and removed. |
| **Control Owner** | Application Owner |
| **Review Frequency** | Quarterly |
| **OWASP** | LLM04:2025 Data and Model Poisoning; LLM08:2025 Vector and Embedding Weaknesses |
| **MITRE ATLAS Techniques** | AML.T0070 RAG Poisoning; AML.T0071 False RAG Entry Injection; AML.T0066 Retrieval Content Crafting |
| **MITRE ATLAS Mitigations** | AML.M0025 Maintain AI Dataset Provenance |
| **NIST AI RMF** | MEASURE 2.7; MAP 2.3 |
| **ISO/IEC 42001** | A.7.3 Acquisition of data; A.7.4 Quality of data for AI systems; A.7.5 Data provenance |
| **ISO/IEC 27001** | A.8.32 Change management |
| **NIST CSF** | PR.DS Data Security |
| **CIS Controls** | None published in the CIS Controls. The wiki's own identifier applies: AI-CTRL-019. |
| **SOC 2** | PI1.2 Inputs; CC8.1 Change management |
| **Tested By (15 cases)** | **L07:** [012](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-012)<br>**L10:** [024](../10_Test_Case_Library/L10-data-layer.md#tc-l10-024), [032](../10_Test_Case_Library/L10-data-layer.md#tc-l10-032)<br>**L11:** [001](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-001), [008](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-008), [009](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-009), [010](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-010), [011](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-011), [013](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-013), [014](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-014), [017](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-017), [018](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-018), [021](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-021), [026](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-026), [028](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-028) |

### Application Runtime

<a id="ai-ctrl-005"></a>

#### AI-CTRL-005: Runtime AI Security

| Field | Detail |
|---|---|
| **Control Objective** | Protect custom AI applications from prompt injection, misuse and output leakage. |
| **Tier** | Baseline |
| **Applies To** | Custom AI Applications / AI APIs |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R05](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R06](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R24](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
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
| **ISO/IEC 27001** | A.8.16 Monitoring activities; A.8.26 Application security requirements; A.8.27 Secure system architecture and engineering principles |
| **NIST CSF** | PR.PS Platform Security; PR.DS Data Security; DE.CM Continuous Monitoring |
| **CIS Controls** | CIS 13 Network Monitoring and Defense; CIS 16 Application Software Security |
| **SOC 2** | CC6.6 Protection against threats from outside the boundary; CC7.2 Monitoring for anomalies |
| **Tested By (52 cases)** | **D10:** [010](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-010), [011](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-011), [012](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-012)<br>**D11:** [002](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-002), [003](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-003), [012](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-012), [013](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-013)<br>**L05:** [012](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-012), [026](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-026)<br>**L06:** [020](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-020), [027](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-027)<br>**L07:** [001](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-001), [002](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-002), [003](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-003), [004](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-004), [005](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-005), [006](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-006), [007](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-007), [008](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-008), [009](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-009), [010](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-010), [011](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-011), [012](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-012), [013](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-013), [014](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-014), [015](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-015), [016](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-016), [017](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-017), [018](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-018), [019](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-019), [020](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-020), [021](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-021), [022](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-022), [023](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-023), [024](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-024), [025](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-025), [026](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-026), [031](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-031), [032](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-032), [033](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-033), [035](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-035), [036](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-036), [037](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-037), [039](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-039), [041](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-041)<br>**L08:** [015](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-015), [016](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-016), [019](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-019)<br>**L11:** [014](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-014), [020](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-020)<br>**L14:** [022](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-022)<br>**L16:** [016](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-016) |

<a id="ai-ctrl-020"></a>

#### AI-CTRL-020: Output Handling

| Field | Detail |
|---|---|
| **Control Objective** | Treat model output as untrusted input to whatever consumes it. |
| **Tier** | Baseline |
| **Applies To** | Custom AI Applications / AI APIs / Agents |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R05](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R06](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R24](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R26](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Validate and encode output before it is rendered, executed or passed to another system. Restrict what output can trigger, such as links, images and calls. Inspect responses for sensitive data. Treat reasoning traces, intermediate tool output and system instructions as sensitive content. Decide whether each is shown to users or written to logs, apply the same classification as the final output, and test for leakage. |
| **Evidence Required** | Output validation rules; response inspection logs; injection test results. |
| **Audit Test Procedure** | Induce the model to emit script, markup and command payloads and confirm none executes downstream. Confirm sensitive data in a response is detected. |
| **Control Owner** | AppSec |
| **Review Frequency** | Before each release and quarterly |
| **OWASP** | LLM05:2025 Improper Output Handling; LLM02:2025 Sensitive Information Disclosure |
| **MITRE ATLAS Techniques** | AML.T0077 LLM Response Rendering; AML.T0067 LLM Trusted Output Components Manipulation; AML.T0057 LLM Data Leakage |
| **MITRE ATLAS Mitigations** | AML.M0033 Input and Output Validation for AI Agent Components; AML.M0020 Generative AI Guardrails |
| **NIST AI RMF** | MEASURE 2.7; MEASURE 2.10 |
| **ISO/IEC 42001** | A.6.2.4 AI system verification and validation; A.6.2.6 AI system operation and monitoring |
| **ISO/IEC 27001** | A.8.26 Application security requirements; A.8.28 Secure coding |
| **NIST CSF** | PR.PS Platform Security |
| **CIS Controls** | CIS 16 Application Software Security |
| **SOC 2** | PI1.4 Outputs |
| **Tested By (14 cases)** | **D11:** [021](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-021)<br>**L05:** [014](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-014), [015](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-015), [016](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-016), [017](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-017), [020](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-020), [022](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-022), [024](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-024)<br>**L06:** [030](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-030), [040](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-040)<br>**L07:** [016](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-016)<br>**L08:** [020](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-020), [035](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-035), [044](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-044) |

<a id="ai-ctrl-021"></a>

#### AI-CTRL-021: Multimodal and Voice Input Security

| Field | Detail |
|---|---|
| **Control Objective** | Apply the same inspection and policy to images, documents, audio and video as to text. |
| **Tier** | Advanced |
| **Applies To** | Browser AI / Custom AI Applications / Agents |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
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
| **ISO/IEC 27001** | A.8.7 Protection against malware; A.8.12 Data leakage prevention; A.8.26 Application security requirements |
| **NIST CSF** | PR.DS Data Security; DE.CM Continuous Monitoring |
| **CIS Controls** | CIS 3 Data Protection; CIS 10 Malware Defenses |
| **SOC 2** | CC6.7 Transmission, movement and removal of information; CC6.8 Unauthorized or malicious software |
| **Tested By (28 cases)** | **D11:** [001](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-001), [002](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-002), [003](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-003), [004](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-004), [005](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-005), [006](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-006), [007](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-007), [008](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-008), [009](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-009), [010](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-010), [011](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-011), [012](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-012), [013](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-013), [014](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-014), [015](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-015), [016](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-016), [017](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-017), [018](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-018), [019](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-019), [020](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-020), [021](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-021), [022](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-022)<br>**L04:** [020](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-020), [021](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-021), [022](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-022)<br>**L07:** [014](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-014), [023](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-023)<br>**L08:** [013](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-013) |

<a id="ai-ctrl-039"></a>

#### AI-CTRL-039: Output Reliability and Content Safety

| Field | Detail |
|---|---|
| **Control Objective** | Keep AI output grounded, within its approved scope and free of harmful content. |
| **Tier** | Advanced |
| **Applies To** | Custom AI Applications / AI APIs / IDE AI |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R12](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R14](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R20](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
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
| **ISO/IEC 27001** | None published in ISO/IEC 27001 Annex A. The wiki's own identifier applies: AI-CTRL-039. |
| **NIST CSF** | None published in the NIST CSF categories. The wiki's own identifier applies: AI-CTRL-039. |
| **CIS Controls** | None published in the CIS Controls. The wiki's own identifier applies: AI-CTRL-039. |
| **SOC 2** | PI1.3 Processing; PI1.4 Outputs |
| **Tested By (9 cases)** | **L03:** [033](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-033), [035](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-035)<br>**L05:** [018](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-018), [019](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-019), [021](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-021)<br>**L08:** [017](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-017), [018](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-018)<br>**L12:** [017](../10_Test_Case_Library/L12-model-layer.md#tc-l12-017)<br>**L17:** [033](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-033) |

### Agents and Tools

<a id="ai-ctrl-006"></a>

#### AI-CTRL-006: Agent Governance

| Field | Detail |
|---|---|
| **Control Objective** | Monitor AI agents, tool calls, API access and autonomous actions. |
| **Tier** | Baseline |
| **Applies To** | Agents |
| **Assurance Stage** | Design |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R25](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Keep a registry of every agent with its owner, purpose, model, tools, data scope and approval status. Monitor decisions, tool calls and delegation chains, and detect unregistered agents. Keep a map of which agents may call or delegate to which, and alert on links outside it. |
| **Evidence Required** | Agent registry; tool access logs; delegation maps; shadow agent reports. |
| **Audit Test Procedure** | Deploy registered and unregistered test agents. Confirm the unregistered agents are detected, and that owner, tools and data scope are correct for the registered ones. |
| **Control Owner** | AI Platform Team |
| **Review Frequency** | Quarterly |
| **OWASP** | LLM06:2025 Excessive Agency; ASI10 Rogue Agents; ASI07 Insecure Inter-Agent Communication |
| **MITRE ATLAS Techniques** | AML.T0081 Modify AI Agent Configuration |
| **MITRE ATLAS Mitigations** | AML.M0038 AI Agent Scope Drift Detection; AML.M0024 AI Telemetry Logging and Monitoring |
| **NIST AI RMF** | GOVERN 1.6; MEASURE 2.4 |
| **ISO/IEC 42001** | A.4.2 Resource documentation; A.6.2.6 AI system operation and monitoring |
| **ISO/IEC 27001** | A.5.15 Access control; A.8.15 Logging; A.8.16 Monitoring activities |
| **NIST CSF** | PR.AA Identity Management, Authentication, and Access Control; DE.CM Continuous Monitoring |
| **CIS Controls** | CIS 6 Access Control Management; CIS 8 Audit Log Management |
| **SOC 2** | CC6.1 Logical access security; CC7.2 Monitoring for anomalies |
| **Tested By (15 cases)** | **D09:** [020](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-020)<br>**D10:** [001](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-001), [023](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-023)<br>**L04:** [023](../10_Test_Case_Library/L04-human-interaction-layer.md#tc-l04-023)<br>**L06:** [001](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-001), [002](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-002), [003](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-003), [004](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-004), [017](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-017), [029](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-029), [034](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-034), [035](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-035), [038](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-038), [045](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-045)<br>**L17:** [012](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-012) |

<a id="ai-ctrl-022"></a>

#### AI-CTRL-022: Deterministic Action Authorization

| Field | Detail |
|---|---|
| **Control Objective** | Enforce authority to act, access data or spend money outside the model. |
| **Tier** | Baseline |
| **Applies To** | Agents / Custom AI Applications |
| **Assurance Stage** | Design |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R24](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Place a policy enforcement point between the model and every tool. It authorizes each call with deterministic rules using the real parameters, the acting identity and the end user's rights. Model output is advice, never authority. |
| **Evidence Required** | Policy rules; allow and deny logs; architecture review record. |
| **Audit Test Procedure** | Instruct a test agent, through injected content, to make a call the policy forbids. Confirm the enforcement point denies it regardless of what the model outputs. |
| **Control Owner** | Security Architecture |
| **Review Frequency** | Semi-annually |
| **OWASP** | LLM06:2025 Excessive Agency; ASI02 Tool Misuse & Exploitation |
| **MITRE ATLAS Techniques** | AML.T0053 AI Agent Tool Invocation; AML.T0086 Exfiltration via AI Agent Tool Invocation; AML.T0101 Data Destruction via AI Agent Tool Invocation |
| **MITRE ATLAS Mitigations** | AML.M0028 Enforce Access Controls for AI Agent Tools; AML.M0030 Restrict AI Agent Tool Invocation on Untrusted Data; AML.M0033 Input and Output Validation for AI Agent Components |
| **NIST AI RMF** | MEASURE 2.7; MANAGE 1.3 |
| **ISO/IEC 42001** | A.6.2.2 AI system requirements and specification |
| **ISO/IEC 27001** | A.5.3 Segregation of duties; A.5.15 Access control; A.8.3 Information access restriction |
| **NIST CSF** | PR.AA Identity Management, Authentication, and Access Control |
| **CIS Controls** | CIS 6 Access Control Management |
| **SOC 2** | CC6.1 Logical access security; CC6.3 Role-based access and least privilege |
| **Tested By (19 cases)** | **D09:** [010](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-010)<br>**D10:** [004](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-004), [005](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-005), [006](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-006), [007](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-007), [012](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-012), [014](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-014)<br>**L05:** [022](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-022)<br>**L06:** [011](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-011), [014](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-014), [019](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-019), [024](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-024), [033](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-033), [036](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-036), [039](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-039), [040](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-040)<br>**L07:** [008](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-008)<br>**L09:** [006](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-006)<br>**L14:** [023](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-023) |

<a id="ai-ctrl-023"></a>

#### AI-CTRL-023: Human Approval for Sensitive Actions

| Field | Detail |
|---|---|
| **Control Objective** | Require a person to approve irreversible or high-impact actions before they run. |
| **Tier** | Baseline |
| **Applies To** | Agents |
| **Assurance Stage** | Design |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R19](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
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
| **ISO/IEC 27001** | A.5.3 Segregation of duties |
| **NIST CSF** | PR.AA Identity Management, Authentication, and Access Control |
| **CIS Controls** | None published in the CIS Controls. The wiki's own identifier applies: AI-CTRL-023. |
| **SOC 2** | None published in the SOC 2 criteria. The wiki's own identifier applies: AI-CTRL-023. |
| **Tested By (8 cases)** | **D10:** [006](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-006), [013](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-013)<br>**L01:** [012](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-012), [022](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-022)<br>**L06:** [015](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-015), [016](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-016)<br>**L07:** [038](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-038)<br>**L09:** [012](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-012) |

<a id="ai-ctrl-024"></a>

#### AI-CTRL-024: Tool and MCP Server Governance

| Field | Detail |
|---|---|
| **Control Objective** | Allow agents to use only vetted tools and tool servers, and detect when they change. |
| **Tier** | Baseline |
| **Applies To** | Agents / IDE AI |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R23](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R24](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Keep an allow-list of tools, plugins and MCP servers with an owner for each. Validate tool schemas, pin versions, and re-approve when a tool definition changes after approval. The same governance applies to agent skills and plugins: approve them from an allowlist after review, pin the version, check integrity on load and keep a procedure to remove one quickly. Treat tools that can override system or application controls, such as shells, database consoles and administration APIs, as privileged utilities: give them only to named agents that need them, and log every use. |
| **Evidence Required** | Tool and MCP server registry; allow-list configuration; change detection alerts. |
| **Audit Test Procedure** | Connect an unlisted tool server and confirm it is blocked. Change the description of an approved tool and confirm the change is detected before use. |
| **Control Owner** | AI Platform Team |
| **Review Frequency** | Quarterly |
| **OWASP** | LLM03:2025 Supply Chain; ASI04 Agentic Supply Chain Vulnerabilities; ASI02 Tool Misuse & Exploitation |
| **MITRE ATLAS Techniques** | AML.T0110 AI Agent Tool Poisoning; AML.T0109 AI Supply Chain Rug Pull; AML.T0099 AI Agent Tool Data Poisoning; AML.T0010 Supply Chain Compromise |
| **MITRE ATLAS Mitigations** | AML.M0028 Enforce Access Controls for AI Agent Tools; AML.M0014 Verify AI Artifacts |
| **NIST AI RMF** | GOVERN 6.1; MAP 4.1; MAP 4.2; MANAGE 3.1 |
| **ISO/IEC 42001** | A.10.3 Suppliers; A.4.4 Tooling resources |
| **ISO/IEC 27001** | A.5.19 Information security in supplier relationships; A.5.21 Managing information security in the ICT supply chain; A.8.9 Configuration management; A.8.19 Installation of software on operational systems; A.8.32 Change management; A.8.18 Use of privileged utility programs |
| **NIST CSF** | GV.SC Cybersecurity Supply Chain Risk Management; PR.PS Platform Security |
| **CIS Controls** | CIS 2 Inventory and Control of Software Assets; CIS 15 Service Provider Management; CIS 16 Application Software Security |
| **SOC 2** | CC6.8 Unauthorized or malicious software; CC8.1 Change management; CC9.2 Vendor and business partner risk |
| **Tested By (16 cases)** | **D10:** [022](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-022)<br>**L06:** [005](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-005), [006](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-006), [007](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-007), [008](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-008), [009](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-009), [010](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-010), [011](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-011), [012](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-012), [013](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-013), [032](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-032), [037](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-037), [041](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-041), [047](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-047)<br>**L16:** [015](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-015), [026](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-026) |

<a id="ai-ctrl-025"></a>

#### AI-CTRL-025: AI Containment and Kill Switch

| Field | Detail |
|---|---|
| **Control Objective** | Stop an agent or suspend a high-risk AI model, revoke its access and limit the damage within minutes, with a tested fallback. |
| **Tier** | Baseline |
| **Applies To** | Agents / Custom AI Applications / AI APIs / Vendors |
| **Assurance Stage** | Production |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R11](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R21](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R25](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R55](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Provide a tested way to stop a single agent and to revoke credentials for all agents. Set limits on steps, time and spend per task. Know which actions can be rolled back and how. For every AI use case rated high risk or material, including models that are not agents (for example credit, fraud or pricing models) and third-party AI, name who may suspend it, set the triggers (risk tolerance breached, incident, regulator request), route decisions to a fallback or manual process while it is off, require re-approval before restart, and test activation at least once a year. Where a vendor runs the model, secure the right to have it suspended in the contract. Keep the log of every action the AI system took through containment and rollback; nothing the stop or the reversal does may remove it. Where an agent can reach cleartext payment card data, shut it down automatically (fail secure) on unusual activity such as an attempt to reach a system outside its scope. |
| **Evidence Required** | Kill switch procedure; register of kill switches for high-risk use cases with owners, triggers and fallbacks; test records with timings; task limits configuration. |
| **Audit Test Procedure** | Start a long-running test agent and stop it. Measure the time until no further actions occur and credentials are invalid. Sample high-risk use cases and confirm each has a kill switch, a fallback and a test within the last year; suspend one model in the lab and confirm decisions route to the fallback. |
| **Control Owner** | AI Platform Team / SOC |
| **Review Frequency** | Semi-annually |
| **OWASP** | LLM06:2025 Excessive Agency; ASI08 Cascading Failures; ASI10 Rogue Agents |
| **MITRE ATLAS Techniques** | AML.T0053 AI Agent Tool Invocation; AML.T0034 Cost Harvesting |
| **MITRE ATLAS Mitigations** | AML.M0037 AI Agent Authority Expansion Controls; AML.M0036 Limit AI Workload Resource Consumption |
| **NIST AI RMF** | MANAGE 2.4; MANAGE 2.3 |
| **ISO/IEC 42001** | A.6.2.6 AI system operation and monitoring |
| **ISO/IEC 27001** | A.5.18 Access rights; A.5.26 Response to information security incidents |
| **NIST CSF** | RS.MA Incident Management; RS.MI Incident Mitigation |
| **CIS Controls** | CIS 6 Access Control Management; CIS 17 Incident Response Management |
| **SOC 2** | CC6.2 Registration and removal of access; CC7.4 Incident response |
| **Tested By (13 cases)** | **D09:** [016](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-016)<br>**D10:** [019](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-019), [020](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-020)<br>**D12:** [011](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-011)<br>**D13:** [009](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md#tc-d13-009)<br>**L01:** [021](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-021), [022](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-022)<br>**L06:** [021](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-021), [022](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-022), [023](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-023), [024](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-024), [046](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-046)<br>**L17:** [019](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-019) |

<a id="ai-ctrl-026"></a>

#### AI-CTRL-026: Agent Memory and Context Integrity

| Field | Detail |
|---|---|
| **Control Objective** | Prevent poisoned or cross-user content from persisting in agent memory and context. |
| **Tier** | Advanced |
| **Applies To** | Agents / Custom AI Applications |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R05](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R21](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Separate memory by user and tenant. Record the source of each memory item, apply expiry, and provide a way to inspect and purge memory. Do not let untrusted content write to long-term memory unchecked. Keep an inventory of memory stores with a named owner for each. Write down what each assistant may and may not remember, and enforce it when memory is written. Let users see, correct and delete what is remembered about them, and include memory in data subject access and erasure requests. |
| **Evidence Required** | Memory isolation tests; memory provenance records; purge procedure and test; memory store inventory with owners; memory write policy and enforcement results; access and erasure request records that cover memory. |
| **Audit Test Procedure** | Plant an instruction in memory through untrusted content and confirm it does not affect a later session. Confirm one user cannot read another's memory. |
| **Control Owner** | Application Owner |
| **Review Frequency** | Semi-annually |
| **OWASP** | LLM04:2025 Data and Model Poisoning; LLM01:2025 Prompt Injection; ASI06 Memory & Context Poisoning |
| **MITRE ATLAS Techniques** | AML.T0080 AI Agent Context Poisoning; AML.T0092 Manipulate User LLM Chat History; AML.T0094 Delay Execution of LLM Instructions |
| **MITRE ATLAS Mitigations** | AML.M0031 Memory Hardening |
| **NIST AI RMF** | MEASURE 2.7; MEASURE 2.10 |
| **ISO/IEC 42001** | A.6.2.6 AI system operation and monitoring |
| **ISO/IEC 27001** | A.8.3 Information access restriction |
| **NIST CSF** | PR.DS Data Security |
| **CIS Controls** | CIS 3 Data Protection |
| **SOC 2** | CC6.1 Logical access security; PI1.5 Stored items |
| **Tested By (9 cases)** | **L07:** [027](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-027), [028](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-028), [029](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-029), [030](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-030), [035](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-035), [042](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-042), [043](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-043), [044](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-044), [045](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-045) |

<a id="ai-ctrl-027"></a>

#### AI-CTRL-027: Agent Execution Isolation

| Field | Detail |
|---|---|
| **Control Objective** | Run agent-generated code and browser or computer-use sessions in isolation. |
| **Tier** | Baseline |
| **Applies To** | Agents |
| **Assurance Stage** | Platform |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R21](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R22](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R25](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R55](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
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
| **ISO/IEC 27001** | A.8.22 Segregation of networks; A.8.27 Secure system architecture and engineering principles; A.8.31 Separation of development, test and production environments |
| **NIST CSF** | PR.PS Platform Security; PR.IR Technology Infrastructure Resilience |
| **CIS Controls** | CIS 4 Secure Configuration of Enterprise Assets and Software; CIS 12 Network Infrastructure Management; CIS 16 Application Software Security |
| **SOC 2** | CC6.6 Protection against threats from outside the boundary; CC6.8 Unauthorized or malicious software |
| **Tested By (12 cases)** | **D10:** [002](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-002), [003](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-003), [008](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-008), [009](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-009), [016](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-016), [021](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-021)<br>**L06:** [025](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-025), [026](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-026), [031](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-031), [036](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-036), [046](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-046)<br>**L10:** [035](../10_Test_Case_Library/L10-data-layer.md#tc-l10-035) |

### Model, Training and Pipeline

<a id="ai-ctrl-028"></a>

#### AI-CTRL-028: Model Protection

| Field | Detail |
|---|---|
| **Control Objective** | Protect models from theft, extraction and adversarial inputs. |
| **Tier** | Advanced |
| **Applies To** | Custom AI Applications / AI APIs |
| **Assurance Stage** | Platform |
| **Deployment Model** | PaaS/IaaS/Self-hosted |
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
| **ISO/IEC 27001** | A.5.15 Access control; A.8.3 Information access restriction; A.8.12 Data leakage prevention; A.8.24 Use of cryptography |
| **NIST CSF** | PR.AA Identity Management, Authentication, and Access Control; PR.DS Data Security |
| **CIS Controls** | CIS 3 Data Protection; CIS 6 Access Control Management |
| **SOC 2** | CC6.1 Logical access security; CC6.7 Transmission, movement and removal of information; C1.1 Identification of confidential information |
| **Tested By (20 cases)** | **D11:** [004](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md#tc-d11-004)<br>**L12:** [002](../10_Test_Case_Library/L12-model-layer.md#tc-l12-002), [003](../10_Test_Case_Library/L12-model-layer.md#tc-l12-003), [004](../10_Test_Case_Library/L12-model-layer.md#tc-l12-004), [007](../10_Test_Case_Library/L12-model-layer.md#tc-l12-007), [008](../10_Test_Case_Library/L12-model-layer.md#tc-l12-008), [009](../10_Test_Case_Library/L12-model-layer.md#tc-l12-009), [010](../10_Test_Case_Library/L12-model-layer.md#tc-l12-010), [011](../10_Test_Case_Library/L12-model-layer.md#tc-l12-011), [012](../10_Test_Case_Library/L12-model-layer.md#tc-l12-012), [013](../10_Test_Case_Library/L12-model-layer.md#tc-l12-013), [015](../10_Test_Case_Library/L12-model-layer.md#tc-l12-015), [024](../10_Test_Case_Library/L12-model-layer.md#tc-l12-024), [028](../10_Test_Case_Library/L12-model-layer.md#tc-l12-028), [029](../10_Test_Case_Library/L12-model-layer.md#tc-l12-029), [032](../10_Test_Case_Library/L12-model-layer.md#tc-l12-032), [034](../10_Test_Case_Library/L12-model-layer.md#tc-l12-034)<br>**L13:** [017](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-017)<br>**L15:** [011](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-011)<br>**L16:** [005](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-005) |

<a id="ai-ctrl-029"></a>

#### AI-CTRL-029: Training and Fine-Tuning Data Integrity

| Field | Detail |
|---|---|
| **Control Objective** | Know where training data came from and detect tampering before it shapes a model. |
| **Tier** | Advanced |
| **Applies To** | Custom AI Applications |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Record provenance for every dataset. Verify integrity before each training or fine-tuning run. Screen data for sensitive content and poisoning, and keep the ability to trace a model back to its data. Define a data quality profile for each dataset: choose the quality characteristics that matter for the task (for example completeness, accuracy, balance and representativeness, as named in ISO/IEC 5259-2), set a measured threshold for each, and have the data owner approve them. Check the thresholds before each run, and treat labelling quality as part of the profile when data is labelled. |
| **Evidence Required** | Dataset provenance records; integrity checks; screening results; model-to-data lineage; approved data quality profile and the measured results for each run. |
| **Audit Test Procedure** | Alter a sample of a test dataset and confirm the integrity check fails the run. Trace a deployed model back to the exact dataset versions used. |
| **Control Owner** | ML Engineering / Data Owner |
| **Review Frequency** | Before each training run |
| **OWASP** | LLM04:2025 Data and Model Poisoning |
| **MITRE ATLAS Techniques** | AML.T0020 Training Data Poisoning; AML.T0059 Erode Dataset Integrity |
| **MITRE ATLAS Mitigations** | AML.M0007 Sanitize Training Data; AML.M0025 Maintain AI Dataset Provenance |
| **NIST AI RMF** | MAP 2.3; MAP 4.1; MEASURE 2.7; MEASURE 2.10 |
| **ISO/IEC 42001** | A.7.2 Data for development and enhancement of AI system; A.7.3 Acquisition of data; A.7.4 Quality of data for AI systems; A.7.5 Data provenance |
| **ISO/IEC 27001** | A.5.9 Inventory of information and other associated assets; A.5.21 Managing information security in the ICT supply chain; A.8.33 Test information |
| **NIST CSF** | GV.SC Cybersecurity Supply Chain Risk Management; ID.AM Asset Management; PR.DS Data Security |
| **CIS Controls** | CIS 3 Data Protection |
| **SOC 2** | PI1.2 Inputs |
| **Tested By (18 cases)** | **D12:** [013](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-013)<br>**L10:** [031](../10_Test_Case_Library/L10-data-layer.md#tc-l10-031), [033](../10_Test_Case_Library/L10-data-layer.md#tc-l10-033)<br>**L13:** [001](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-001), [002](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-002), [003](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-003), [004](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-004), [005](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-005), [006](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-006), [007](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-007), [008](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-008), [013](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-013), [014](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-014), [015](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-015), [016](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-016), [018](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-018), [022](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-022)<br>**L14:** [014](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-014) |

<a id="ai-ctrl-030"></a>

#### AI-CTRL-030: ML Pipeline and Model Registry Security

| Field | Detail |
|---|---|
| **Control Objective** | Protect the pipeline that builds, stores and releases models and prompts. |
| **Tier** | Advanced |
| **Applies To** | Custom AI Applications |
| **Assurance Stage** | Platform |
| **Deployment Model** | PaaS/IaaS/Self-hosted |
| **Risk Mapping** | [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Sign model artifacts and verify signatures at deployment. Restrict who can write to the registry. Gate releases on security tests, and version models, prompts and configuration together. |
| **Evidence Required** | Signing configuration; registry access list; release gate results; version history. |
| **Audit Test Procedure** | Attempt to deploy an unsigned or altered artifact and confirm it is rejected. Confirm a failed security test blocks a release. |
| **Control Owner** | MLOps / DevSecOps |
| **Review Frequency** | Semi-annually |
| **OWASP** | LLM03:2025 Supply Chain; LLM04:2025 Data and Model Poisoning |
| **MITRE ATLAS Techniques** | AML.T0010 Supply Chain Compromise; AML.T0018 Manipulate AI Model; AML.T0119 Exploit Automated Artifact Processing Pipeline |
| **MITRE ATLAS Mitigations** | AML.M0013 Code Signing; AML.M0014 Verify AI Artifacts |
| **NIST AI RMF** | MEASURE 2.7; MAP 4.2 |
| **ISO/IEC 42001** | A.6.2.5 AI system deployment; A.6.2.3 Documentation of AI system design and development; A.6.1.3 Processes for responsible design and development; A.6.2.7 AI system technical documentation |
| **ISO/IEC 27001** | A.8.4 Access to source code; A.8.9 Configuration management; A.8.25 Secure development life cycle; A.8.29 Security testing in development and acceptance; A.8.31 Separation of development, test and production environments; A.8.32 Change management |
| **NIST CSF** | PR.AA Identity Management, Authentication, and Access Control; PR.PS Platform Security |
| **CIS Controls** | CIS 4 Secure Configuration of Enterprise Assets and Software; CIS 16 Application Software Security |
| **SOC 2** | CC6.1 Logical access security; CC8.1 Change management |
| **Tested By (16 cases)** | **D08:** [020](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-020)<br>**L07:** [034](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-034)<br>**L12:** [004](../10_Test_Case_Library/L12-model-layer.md#tc-l12-004), [023](../10_Test_Case_Library/L12-model-layer.md#tc-l12-023)<br>**L13:** [012](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-012), [013](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-013)<br>**L14:** [001](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-001), [002](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-002), [003](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-003), [004](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-004), [005](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-005), [012](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-012), [013](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-013), [014](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-014), [018](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-018), [019](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-019) |

### Supply Chain, Infrastructure and Resilience

<a id="ai-ctrl-031"></a>

#### AI-CTRL-031: AI Supply Chain and AI-BOM

| Field | Detail |
|---|---|
| **Control Objective** | Know exactly which models, datasets, packages and prompts run in each environment. |
| **Tier** | Advanced |
| **Applies To** | Custom AI Applications / Agents / IDE AI / Vendors |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R16](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R23](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Maintain an AI bill of materials per system. Take models and packages only from approved sources, verify provenance, and scan them. Re-run security tests when any component changes, including a provider-side model update. Pin model versions rather than using floating aliases such as "latest", and track provider deprecation and change notices so that a model change is a reviewed change. Record in the AI-BOM the model and version, harness and orchestration components, where it is hosted and who runs it, the data and systems it can reach with the restrictions on them, the provider's data use and retention terms, and the intended users and use cases. Authorise, list and monitor for tampering any AI script or widget loaded on a payment page, as for any other page script. |
| **Evidence Required** | AI-BOM; approved source list; scan reports; change-triggered test records. |
| **Audit Test Procedure** | Compare the AI-BOM of a sampled system with what is deployed. Introduce a component from an unapproved source and confirm it is blocked or flagged. |
| **Control Owner** | DevSecOps |
| **Review Frequency** | Quarterly |
| **OWASP** | LLM03:2025 Supply Chain |
| **MITRE ATLAS Techniques** | AML.T0010 Supply Chain Compromise; AML.T0109 AI Supply Chain Rug Pull; AML.T0115 Publish Poisoned AI Artifacts; AML.T0111 AI Supply Chain Reputation Inflation |
| **MITRE ATLAS Mitigations** | AML.M0023 Maintain an AI Bill of Materials; AML.M0014 Verify AI Artifacts; AML.M0016 Vulnerability Scanning |
| **NIST AI RMF** | GOVERN 6.1; MAP 4.1; MANAGE 3.1; MANAGE 3.2 |
| **ISO/IEC 42001** | A.10.3 Suppliers; A.4.2 Resource documentation; A.7.5 Data provenance; A.6.2.7 AI system technical documentation |
| **ISO/IEC 27001** | A.5.9 Inventory of information and other associated assets; A.5.21 Managing information security in the ICT supply chain; A.8.8 Management of technical vulnerabilities; A.8.19 Installation of software on operational systems; A.8.30 Outsourced development |
| **NIST CSF** | GV.SC Cybersecurity Supply Chain Risk Management; ID.AM Asset Management; ID.RA Risk Assessment |
| **CIS Controls** | CIS 2 Inventory and Control of Software Assets; CIS 7 Continuous Vulnerability Management; CIS 15 Service Provider Management; CIS 16 Application Software Security |
| **SOC 2** | CC7.1 Detection of configuration changes and vulnerabilities; CC9.2 Vendor and business partner risk |
| **Tested By (25 cases)** | **L05:** [019](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-019), [036](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-036)<br>**L08:** [028](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-028), [042](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-042)<br>**L12:** [001](../10_Test_Case_Library/L12-model-layer.md#tc-l12-001), [002](../10_Test_Case_Library/L12-model-layer.md#tc-l12-002), [005](../10_Test_Case_Library/L12-model-layer.md#tc-l12-005), [006](../10_Test_Case_Library/L12-model-layer.md#tc-l12-006), [018](../10_Test_Case_Library/L12-model-layer.md#tc-l12-018), [019](../10_Test_Case_Library/L12-model-layer.md#tc-l12-019)<br>**L13:** [014](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-014)<br>**L14:** [009](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-009)<br>**L16:** [001](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-001), [002](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-002), [003](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-003), [004](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-004), [005](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-005), [006](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-006), [007](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-007), [013](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-013), [014](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-014), [015](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-015), [016](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-016), [017](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-017), [024](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-024) |

<a id="ai-ctrl-032"></a>

#### AI-CTRL-032: AI Infrastructure Hardening

| Field | Detail |
|---|---|
| **Control Objective** | Harden and segment the infrastructure that trains and serves models. |
| **Tier** | Advanced |
| **Applies To** | Custom AI Applications |
| **Assurance Stage** | Platform |
| **Deployment Model** | PaaS/IaaS/Self-hosted |
| **Risk Mapping** | [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R10](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Separate experimentation, training, evaluation and production. Isolate model runtimes at the network level and allow only required egress. Manage secrets centrally, and isolate tenants on shared GPUs. Set security requirements for the model APIs and other network services that AI systems call, including authentication, encryption in transit and the endpoints allowed, and monitor them. |
| **Evidence Required** | Network segmentation rules; secrets management configuration; hardening baseline; isolation tests. |
| **Audit Test Procedure** | Attempt to reach production data from the experimentation environment and to open unapproved egress from a model runtime. Confirm both fail. |
| **Control Owner** | Platform Engineering |
| **Review Frequency** | Semi-annually |
| **OWASP** | LLM03:2025 Supply Chain |
| **MITRE ATLAS Techniques** | AML.T0049 Exploit Public-Facing Application; AML.T0132 Misconfigured or Publicly Exposed AI Services; AML.T0055 Unsecured Credentials; AML.T0025 Exfiltration via Cyber Means |
| **MITRE ATLAS Mitigations** | AML.M0005 Control Access to AI Models and Data at Rest; AML.M0012 Encrypt Sensitive Information; AML.M0016 Vulnerability Scanning; AML.M0019 Control Access to AI Models and Data in Production |
| **NIST AI RMF** | MEASURE 2.7; MAP 4.2 |
| **ISO/IEC 42001** | A.4.5 System and computing resources |
| **ISO/IEC 27001** | A.5.23 Information security for use of cloud services; A.8.8 Management of technical vulnerabilities; A.8.9 Configuration management; A.8.20 Networks security; A.8.22 Segregation of networks; A.8.24 Use of cryptography; A.8.21 Security of network services |
| **NIST CSF** | PR.DS Data Security; PR.PS Platform Security; PR.IR Technology Infrastructure Resilience |
| **CIS Controls** | CIS 4 Secure Configuration of Enterprise Assets and Software; CIS 7 Continuous Vulnerability Management; CIS 12 Network Infrastructure Management; CIS 13 Network Monitoring and Defense |
| **SOC 2** | CC6.1 Logical access security; CC6.6 Protection against threats from outside the boundary; CC7.1 Detection of configuration changes and vulnerabilities |
| **Tested By (27 cases)** | **L06:** [042](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-042)<br>**L09:** [019](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-019)<br>**L10:** [023](../10_Test_Case_Library/L10-data-layer.md#tc-l10-023)<br>**L11:** [002](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-002), [003](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-003)<br>**L12:** [020](../10_Test_Case_Library/L12-model-layer.md#tc-l12-020)<br>**L13:** [011](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-011)<br>**L14:** [006](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-006), [007](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-007), [010](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-010), [011](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-011), [020](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-020)<br>**L15:** [001](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-001), [002](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-002), [003](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-003), [004](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-004), [005](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-005), [006](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-006), [007](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-007), [008](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-008), [009](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-009), [010](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-010), [011](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-011), [012](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-012), [015](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-015), [016](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-016)<br>**L16:** [017](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-017) |

<a id="ai-ctrl-040"></a>

#### AI-CTRL-040: AI Service Resilience and Fail-Safe Operation

| Field | Detail |
|---|---|
| **Control Objective** | Keep AI services and their security controls available, and make them fail safely. |
| **Tier** | Advanced |
| **Applies To** | AI APIs / Custom AI Applications / Agents / Vendors |
| **Assurance Stage** | Platform |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R13](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R16](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
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
| **ISO/IEC 27001** | A.5.29 Information security during disruption; A.5.30 ICT readiness for business continuity; A.8.6 Capacity management; A.8.13 Information backup; A.8.14 Redundancy of information processing facilities |
| **NIST CSF** | PR.IR Technology Infrastructure Resilience; RC.RP Incident Recovery Plan Execution |
| **CIS Controls** | CIS 11 Data Recovery |
| **SOC 2** | A1.1 Capacity; A1.2 Backup and recovery infrastructure; A1.3 Recovery plan testing; CC9.1 Risk mitigation for business disruption |
| **Tested By (14 cases)** | **L01:** [018](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-018), [021](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-021)<br>**L05:** [013](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-013), [030](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-030)<br>**L08:** [032](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-032), [033](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-033), [034](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-034), [035](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-035)<br>**L11:** [025](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-025)<br>**L12:** [021](../10_Test_Case_Library/L12-model-layer.md#tc-l12-021)<br>**L15:** [019](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-019)<br>**L16:** [012](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-012), [020](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-020)<br>**L17:** [028](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-028) |

### Assurance and Testing

<a id="ai-ctrl-033"></a>

#### AI-CTRL-033: AI Security Review and Release Gate

| Field | Detail |
|---|---|
| **Control Objective** | Review every AI system against its threats before production and after material change. |
| **Tier** | Baseline |
| **Applies To** | Custom AI Applications / Agents / Vendors |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R05](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R14](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R16](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R55](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Threat model each system: assets, trust boundaries, worst-case output and maximum damage. Select controls from this library by risk tier. Record open risks and exceptions, and require sign-off before release. When an agent changes production systems, each change carries the same record as a person's change: reason, security impact, approval by an authorised person, test results and a rollback that was tested before approval. Set documented objectives for responsible development, such as security, privacy, reliability and fairness targets, and use them as release criteria. |
| **Evidence Required** | Threat models; architecture review records; control selection; approvals and exceptions; responsible development objectives. |
| **Audit Test Procedure** | Sample production systems and confirm each has a current threat model, a control selection that matches its tier and a signed approval. |
| **Control Owner** | Security Architecture |
| **Review Frequency** | Before each release and annually |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-033. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-033. |
| **MITRE ATLAS Mitigations** | None published in MITRE ATLAS mitigations. The wiki's own identifier applies: AI-CTRL-033. |
| **NIST AI RMF** | MANAGE 1.1; GOVERN 4.2; MEASURE 2.7 |
| **ISO/IEC 42001** | A.5.2 AI system impact assessment process; A.6.2.2 AI system requirements and specification; A.6.2.4 AI system verification and validation; A.6.2.5 AI system deployment; A.6.1.2 Objectives for responsible development of AI systems; A.6.1.3 Processes for responsible design and development |
| **ISO/IEC 27001** | A.5.8 Information security in project management; A.8.25 Secure development life cycle; A.8.27 Secure system architecture and engineering principles; A.8.29 Security testing in development and acceptance; A.8.32 Change management |
| **NIST CSF** | ID.RA Risk Assessment; PR.PS Platform Security |
| **CIS Controls** | CIS 16 Application Software Security |
| **SOC 2** | CC3.4 Assessment of change; CC8.1 Change management |
| **Tested By (8 cases)** | **L01:** [002](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-002), [013](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-013), [014](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-014), [015](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-015)<br>**L06:** [034](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-034)<br>**L12:** [032](../10_Test_Case_Library/L12-model-layer.md#tc-l12-032)<br>**L14:** [012](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-012), [023](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-023) |

<a id="ai-ctrl-034"></a>

#### AI-CTRL-034: Adversarial Testing and Continuous Evaluation

| Field | Detail |
|---|---|
| **Control Objective** | Test AI systems against attacks before release and continuously afterwards. |
| **Tier** | Advanced |
| **Applies To** | Custom AI Applications / Agents |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R05](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R16](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R17](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R20](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Red team each system against defined threat cases before release. Run a regression suite in the pipeline and whenever the model, prompt, tools or data change. The risk owner sets the acceptable attack success rate in writing. Re-run the regression suite whenever the model version, prompt, retrieval source or guardrail changes, including changes made by the provider, and set a tolerance for run-to-run output variation. Review each system's behaviour against its defined parameters at least quarterly, or at a frequency set by a documented risk analysis, and re-validate before go-live and after any change. Where an AI reviewer replaces manual code review, measure its detection rate on seeded flaws and re-measure when its model or configuration changes. Track AI threat intelligence, such as new MITRE ATLAS techniques, published incidents and provider advisories, and add relevant techniques to the threat cases and regression suite. Before testing a production system, agree the scope, timing and safeguards with its owner, and use test accounts and test data. |
| **Evidence Required** | Red team reports; regression suite results; agreed thresholds; retest records; threat intelligence review log; production test authorisations. |
| **Audit Test Procedure** | Confirm the last model or prompt change triggered the regression suite. Reproduce a sample of reported findings and confirm fixes hold. |
| **Control Owner** | AI Red Team / AppSec |
| **Review Frequency** | Before each release and continuously |
| **OWASP** | LLM01:2025 Prompt Injection; LLM02:2025 Sensitive Information Disclosure; LLM03:2025 Supply Chain; LLM04:2025 Data and Model Poisoning; LLM05:2025 Improper Output Handling; LLM06:2025 Excessive Agency; LLM07:2025 System Prompt Leakage; LLM08:2025 Vector and Embedding Weaknesses; LLM09:2025 Misinformation; LLM10:2025 Unbounded Consumption |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-034. |
| **MITRE ATLAS Mitigations** | AML.M0035 AI Red Team |
| **NIST AI RMF** | MEASURE 2.7; MEASURE 2.6; MEASURE 2.1; GOVERN 4.3 |
| **ISO/IEC 42001** | A.6.2.4 AI system verification and validation |
| **ISO/IEC 27001** | A.8.8 Management of technical vulnerabilities; A.8.29 Security testing in development and acceptance; A.5.7 Threat intelligence; A.8.34 Protection of information systems during audit testing |
| **NIST CSF** | ID.RA Risk Assessment; ID.IM Improvement |
| **CIS Controls** | CIS 7 Continuous Vulnerability Management; CIS 18 Penetration Testing |
| **SOC 2** | CC4.1 Ongoing and separate evaluations; CC7.1 Detection of configuration changes and vulnerabilities |
| **Tested By (38 cases)** | **D08:** [001](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-001), [002](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-002), [003](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-003), [004](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-004), [005](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-005), [006](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-006), [007](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-007), [008](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-008), [009](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-009), [010](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-010), [011](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-011), [012](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-012), [013](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-013), [014](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-014), [015](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-015), [016](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-016), [017](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-017), [018](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-018), [019](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-019), [020](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-020), [021](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-021), [022](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-022), [023](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-023), [024](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-024), [025](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md#tc-d08-025)<br>**D12:** [014](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-014)<br>**L05:** [027](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-027)<br>**L07:** [024](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-024), [040](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-040)<br>**L12:** [016](../10_Test_Case_Library/L12-model-layer.md#tc-l12-016), [018](../10_Test_Case_Library/L12-model-layer.md#tc-l12-018), [033](../10_Test_Case_Library/L12-model-layer.md#tc-l12-033)<br>**L13:** [010](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-010)<br>**L14:** [002](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-002), [016](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-016), [017](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-017), [024](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-024)<br>**L17:** [029](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-029) |

<a id="ai-ctrl-038"></a>

#### AI-CTRL-038: Control Assurance and Audit Evidence

| Field | Detail |
|---|---|
| **Control Objective** | Show, with current evidence, that each AI control is operating and that findings are closed. |
| **Tier** | Advanced |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents / Vendors |
| **Assurance Stage** | Production |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R09](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R15](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R28](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
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
| **ISO/IEC 27001** | A.5.33 Protection of records; A.5.35 Independent review of information security; A.5.36 Compliance with policies, rules and standards for information security; Clause 9.2 Internal audit |
| **NIST CSF** | GV.OV Oversight; ID.IM Improvement |
| **CIS Controls** | None published in the CIS Controls. The wiki's own identifier applies: AI-CTRL-038. |
| **SOC 2** | CC4.1 Ongoing and separate evaluations; CC4.2 Communication of deficiencies |
| **Tested By (17 cases)** | **D09:** [019](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-019)<br>**L02:** [003](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-003), [013](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-013), [014](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-014), [015](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-015), [016](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-016), [017](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-017), [018](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-018), [019](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-019), [024](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-024), [025](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-025)<br>**L03:** [022](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-022), [023](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-023), [024](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-024), [025](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-025), [026](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-026)<br>**L10:** [030](../10_Test_Case_Library/L10-data-layer.md#tc-l10-030) |

<a id="ai-ctrl-041"></a>

#### AI-CTRL-041: Fairness, Bias Testing and Explainability

| Field | Detail |
|---|---|
| **Control Objective** | Test AI systems that make or support high-impact decisions for unfair bias, and keep explanations that a person can understand and a reviewer can challenge. |
| **Tier** | Advanced |
| **Applies To** | Custom AI Applications / Agents / Vendors |
| **Assurance Stage** | Implementation |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R12](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R14](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R15](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Define which decisions are high-impact. Identify the relevant groups with legal input. Test for bias before release, at least annually and on material model change, and record the method, data, thresholds, results and approvals. Where sensitive data is needed for testing, record why it is necessary and the safeguards. Tell customers before an AI-powered service is provided that AI is used and what its main risks and limits are, in plain language. Give an explanation for each high-impact decision and a route to human review. Block or condition release when a threshold fails. Keep a versioned bias profile for each system that records which differences in treatment are intended and which are not, the stakeholder groups considered, how representative the test data is, the risks accepted and who accepted them, and the application boundaries within which the system was validated; monitor for drift outside them. |
| **Evidence Required** | Bias test plan and results; customer AI-use notices; threshold approvals; necessity record for sensitive data; explanation records; human-review log; retest evidence; current bias profile with its validated application boundaries. |
| **Audit Test Procedure** | Sample high-impact use cases and confirm a current bias test exists. Re-perform one test. Trace one decision to its explanation and review outcome. Confirm a failed result led to action. |
| **Control Owner** | AI Governance Lead / Model Risk |
| **Review Frequency** | Annually and on material model change |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-041. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-041. |
| **MITRE ATLAS Mitigations** | None published in MITRE ATLAS mitigations. The wiki's own identifier applies: AI-CTRL-041. |
| **NIST AI RMF** | MEASURE 2.11; MEASURE 2.9; MAP 5.1 |
| **ISO/IEC 42001** | A.5.4 Assessing AI system impact on individuals or groups of individuals; A.6.2.4 AI system verification and validation; A.8.2 System documentation and information for users; A.10.4 Customers |
| **ISO/IEC 27001** | None published in ISO/IEC 27001 Annex A. The wiki's own identifier applies: AI-CTRL-041. |
| **NIST CSF** | None published in the NIST CSF categories. The wiki's own identifier applies: AI-CTRL-041. |
| **CIS Controls** | None published in the CIS Controls. The wiki's own identifier applies: AI-CTRL-041. |
| **SOC 2** | None published in the SOC 2 criteria. The wiki's own identifier applies: AI-CTRL-041. |
| **Tested By (7 cases)** | **L03:** [008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008), [029](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-029), [031](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-031), [032](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-032), [033](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-033), [043](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-043)<br>**L12:** [033](../10_Test_Case_Library/L12-model-layer.md#tc-l12-033) |

### Detection and Response

<a id="ai-ctrl-008"></a>

#### AI-CTRL-008: Auditability

| Field | Detail |
|---|---|
| **Control Objective** | Maintain logs for prompts, responses, files, users, devices, applications and actions. |
| **Tier** | Baseline |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents |
| **Assurance Stage** | Platform |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R09](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R15](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R26](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Log prompts, responses, uploads, retrieved sources, model calls, tool calls and policy decisions according to policy. Records must be timestamped, attributable, exportable and retained for the approved period. Record enough detail to validate, investigate, attribute and reconstruct each AI-assisted action, while masking or tokenising payment card and other sensitive data before it is written. |
| **Evidence Required** | Exportable audit records; log schema; retention policy; sample reconstruction. |
| **Audit Test Procedure** | Pick a completed test interaction and reconstruct it from logs alone: who, what was sent, what was retrieved, what the model returned and what action followed. |
| **Control Owner** | Security Engineering |
| **Review Frequency** | Semi-annually |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-008. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-008. |
| **MITRE ATLAS Mitigations** | AML.M0024 AI Telemetry Logging and Monitoring |
| **NIST AI RMF** | MEASURE 2.4; MEASURE 2.8; MANAGE 4.1 |
| **ISO/IEC 42001** | A.6.2.8 AI system recording of event logs |
| **ISO/IEC 27001** | A.5.28 Collection of evidence; A.5.33 Protection of records; A.8.15 Logging; A.8.17 Clock synchronization |
| **NIST CSF** | PR.PS Platform Security; DE.CM Continuous Monitoring |
| **CIS Controls** | CIS 8 Audit Log Management |
| **SOC 2** | CC7.2 Monitoring for anomalies |
| **Tested By (23 cases)** | **D09:** [012](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-012)<br>**D10:** [018](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md#tc-d10-018)<br>**D12:** [006](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-006)<br>**L02:** [025](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-025)<br>**L05:** [025](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-025)<br>**L06:** [028](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-028), [045](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-045)<br>**L08:** [040](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-040)<br>**L09:** [025](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-025)<br>**L10:** [026](../10_Test_Case_Library/L10-data-layer.md#tc-l10-026)<br>**L11:** [024](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-024)<br>**L12:** [031](../10_Test_Case_Library/L12-model-layer.md#tc-l12-031)<br>**L13:** [025](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-025)<br>**L14:** [019](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-019)<br>**L15:** [018](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-018)<br>**L17:** [001](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-001), [002](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-002), [004](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-004), [005](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-005), [020](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-020), [030](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-030), [031](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-031), [032](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-032) |

<a id="ai-ctrl-009"></a>

#### AI-CTRL-009: SOC Integration

| Field | Detail |
|---|---|
| **Control Objective** | Forward AI security events and logs to monitoring and response platforms. |
| **Tier** | Advanced |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents |
| **Assurance Stage** | Production |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R09](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Forward AI security events to the SIEM with a documented schema. Build detections and runbooks for AI-specific events, and correlate them with identity, endpoint and network telemetry. |
| **Evidence Required** | SIEM event IDs; parser mapping; detection rules; runbooks; alert samples. |
| **Audit Test Procedure** | Trigger each AI event type in the lab and confirm it arrives in the SIEM within the stated time, parses correctly and raises the expected alert. |
| **Control Owner** | SOC |
| **Review Frequency** | Semi-annually |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-009. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-009. |
| **MITRE ATLAS Mitigations** | AML.M0024 AI Telemetry Logging and Monitoring |
| **NIST AI RMF** | MEASURE 2.4; MEASURE 3.1; MANAGE 4.1 |
| **ISO/IEC 42001** | A.6.2.6 AI system operation and monitoring; A.6.2.8 AI system recording of event logs |
| **ISO/IEC 27001** | A.5.25 Assessment and decision on information security events; A.8.15 Logging; A.8.16 Monitoring activities; A.5.37 Documented operating procedures |
| **NIST CSF** | DE.CM Continuous Monitoring; DE.AE Adverse Event Analysis |
| **CIS Controls** | CIS 8 Audit Log Management; CIS 13 Network Monitoring and Defense |
| **SOC 2** | CC7.2 Monitoring for anomalies; CC7.3 Evaluation of security events |
| **Tested By (22 cases)** | **L06:** [029](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-029)<br>**L07:** [037](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-037)<br>**L09:** [017](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-017)<br>**L14:** [016](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-016)<br>**L17:** [001](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-001), [003](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-003), [006](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-006), [007](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-007), [008](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-008), [009](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-009), [010](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-010), [011](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-011), [012](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-012), [013](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-013), [014](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-014), [015](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-015), [016](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-016), [024](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-024), [025](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-025), [027](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-027), [028](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-028), [029](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-029) |

<a id="ai-ctrl-035"></a>

#### AI-CTRL-035: AI Incident Response and Forensics

| Field | Detail |
|---|---|
| **Control Objective** | Detect, contain, investigate and recover from AI security incidents. |
| **Tier** | Baseline |
| **Applies To** | Browser AI / IDE AI / AI APIs / Custom AI Applications / Agents / Vendors |
| **Assurance Stage** | Production |
| **Deployment Model** | All |
| **Risk Mapping** | [AI-R09](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R20](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| **Implementation Expectation** | Maintain AI-specific playbooks and an incident taxonomy. Preserve state needed for investigation: prompts, context, index snapshots, memory and model version. Define containment options and how to work with the model provider. Include AI failure scenarios in the incident response plan and its tests, even before one has caused a loss: successful prompt injection, model poisoning, an agent acting outside its defined scope, and shadow AI found with access to sensitive data. |
| **Evidence Required** | Playbooks; exercise records; preserved-state checklist; provider contact and escalation path. |
| **Audit Test Procedure** | Run a tabletop or lab exercise for a prompt injection incident. Confirm the interaction can be replayed, scoped and contained using the playbook. |
| **Control Owner** | SOC / Incident Response |
| **Review Frequency** | Annually and after each incident |
| **OWASP** | None published in the OWASP Top 10 lists. The wiki's own identifier applies: AI-CTRL-035. |
| **MITRE ATLAS Techniques** | None published in MITRE ATLAS techniques. The wiki's own identifier applies: AI-CTRL-035. |
| **MITRE ATLAS Mitigations** | AML.M0024 AI Telemetry Logging and Monitoring |
| **NIST AI RMF** | MANAGE 4.3; MANAGE 2.3; GOVERN 4.3; GOVERN 6.2 |
| **ISO/IEC 42001** | A.8.4 Communication of incidents; A.8.3 External reporting; A.3.3 Reporting of concerns; A.6.2.6 AI system operation and monitoring |
| **ISO/IEC 27001** | A.5.24 Information security incident management planning and preparation; A.5.25 Assessment and decision on information security events; A.5.26 Response to information security incidents; A.5.27 Learning from information security incidents; A.5.28 Collection of evidence; A.6.8 Information security event reporting; A.5.37 Documented operating procedures |
| **NIST CSF** | DE.AE Adverse Event Analysis; RS.MA Incident Management; RS.AN Incident Analysis; RS.CO Incident Response Reporting and Communication; RS.MI Incident Mitigation; RC.RP Incident Recovery Plan Execution |
| **CIS Controls** | CIS 17 Incident Response Management |
| **SOC 2** | CC7.3 Evaluation of security events; CC7.4 Incident response; CC7.5 Recovery from incidents |
| **Tested By (40 cases)** | **D09:** [017](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-017)<br>**D12:** [001](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-001), [002](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-002), [003](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-003), [004](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-004), [005](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-005), [006](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-006), [007](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-007), [008](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-008), [009](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-009), [010](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-010), [011](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-011), [012](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-012), [013](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-013), [014](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-014), [015](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-015), [016](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-016), [017](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-017), [018](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-018), [019](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-019), [020](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-020), [021](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-021), [022](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-022)<br>**L03:** [019](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-019), [027](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-027)<br>**L10:** [027](../10_Test_Case_Library/L10-data-layer.md#tc-l10-027), [028](../10_Test_Case_Library/L10-data-layer.md#tc-l10-028)<br>**L16:** [021](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-021), [024](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-024)<br>**L17:** [015](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-015), [017](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-017), [018](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-018), [019](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-019), [020](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-020), [021](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-021), [022](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-022), [023](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-023), [026](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-026), [027](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-027), [033](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-033) |

### Cost and Abuse

<a id="ai-ctrl-036"></a>

#### AI-CTRL-036: AI Cost and Abuse Controls

| Field | Detail |
|---|---|
| **Control Objective** | Attribute AI spend and stop abuse that exhausts budget or capacity. |
| **Tier** | Baseline |
| **Applies To** | AI APIs / Custom AI Applications / Agents |
| **Assurance Stage** | Platform |
| **Deployment Model** | All |
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
| **ISO/IEC 27001** | A.8.6 Capacity management; A.8.16 Monitoring activities |
| **NIST CSF** | PR.IR Technology Infrastructure Resilience; DE.CM Continuous Monitoring |
| **CIS Controls** | None published in the CIS Controls. The wiki's own identifier applies: AI-CTRL-036. |
| **SOC 2** | A1.1 Capacity |
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
