---
title: "Home"
description: "Open, vendor-neutral AI security wiki: governance, risk, security controls, agentic AI standards, vendor evaluation, regional compliance and 653 test cases."
nav_order: 1
document_type: Enterprise AI Security Reference Architecture and Governance Wiki
version: 2.24
status: Published
author: Nachiket Sathaye
coauthors: Ankush Jain
owner: AI Security Program
custodian: Security Architecture Team
review_cycle: Quarterly
approval_authority: AI Governance Committee
last_updated: 2026-10-10
---

# AI Security Wiki Home

> **Document Type:** Enterprise AI Security Reference Architecture and Governance Wiki  
> **Version:** 2.24  
> **Status:** Published  
> **Original Author:** Nachiket Sathaye ([about the author](#22-about-the-author))  
> **Co-Author:** Ankush Jain ([about the co-author](#23-about-the-co-author))  
> **Intended Use:** Public, vendor-neutral reference and template set for AI security governance, engineering, risk management, assurance, audit, compliance, and vendor evaluation.

## 1. Purpose

The AI Security Wiki is a reference for securing AI adoption across an enterprise. It covers AI governance, AI risk management, secure engineering, operational monitoring, vendor evaluation, and assurance, in pages that can be reused as templates and that say what audit evidence each activity should produce.

The wiki helps teams answer five practical questions:

1. Can this AI use case be safely adopted?
2. What risks, controls, and approvals are required?
3. Which engineering standards apply to the implementation?
4. How will security, privacy, sovereignty, and compliance requirements be evidenced?
5. How will the AI capability be monitored, tested, audited, and improved over time?

New to the subject? Start with [Foundations: AI Security vs. Security of AI](00_Foundations/index.md), the research paper that explains the concepts and sources behind the standards, templates, and test cases in the rest of the wiki.

### How this wiki relates to other frameworks

This wiki is the implementation layer: control objectives, evidence, audit procedures and test cases that turn AI governance requirements into something a team can build, test and audit. It works alongside the catalogues and standards that say what to worry about and what the law expects, and does not replace them.

| If you need to... | Start with | Then use this wiki for |
|---|---|---|
| Build a financial-services AI risk catalogue | FINOS AI Governance Framework | Controls, evidence and tests per risk, through the [FINOS crosswalk](23_Framework_Crosswalks/01_FINOS_AIGF_Crosswalk.md) |
| Set up a first, short AI governance baseline | AI Baseline Control Framework (AI BCF) | Control objectives, evidence and tests, through the [AI BCF crosswalk](23_Framework_Crosswalks/02_AI_BCF_Crosswalk.md) |
| Structure a management system | ISO/IEC 42001 with ISO/IEC 27001 | Technical control objectives and test criteria |
| Structure risk language and a programme | NIST AI RMF | Engineering controls, evidence and scoring |
| Define attack classes for testing | OWASP lists, MITRE ATLAS, NIST AI 100-2 | The 653-case test library |
| Meet regional legal duties | The primary legal texts | The [Regional AI Regulatory Hub](11_GCC_AI_Compliance/index.md) sections |
| Decide which risks apply to a use case | n/a | The [use-case risk triage](02_Risk_Management/02F_AI_Use_Case_Risk_Triage.md) |

The FINOS AI Governance Framework is published by FINOS under CC BY 4.0. This wiki cites its identifiers for traceability and does not reproduce its text.

## 2. Mission Statement

Establish a secure, governed, sovereign, and auditable approach to AI adoption by giving business, technology, cybersecurity, governance, compliance, audit, and vendor evaluation teams a common operating reference.

The aim is to let teams adopt AI while reducing the risk of data leakage, prompt injection, model misuse, insecure agent actions, third-party exposure, regulatory non-compliance, and operational blind spots.

## 3. Strategic Objectives

| Objective | Description |
|---|---|
| Protect Enterprise Data | Prevent unauthorized disclosure of confidential, regulated, operational, customer, and sensitive business information to AI systems. |
| Secure AI Systems | Ensure AI-enabled applications, copilots, agents, models, connectors, APIs, and data pipelines are resilient against relevant threats. |
| Enable Responsible Innovation | Provide practical guardrails that allow teams to adopt AI safely without unnecessary friction. |
| Support Sovereignty and Compliance | Align AI initiatives with UAE data residency, regulatory, privacy, governance, and sector-specific requirements. |
| Standardize AI Risk Decisions | Use a consistent risk assessment, control selection, treatment, exception, and approval process. |
| Improve Audit Readiness | Maintain clear ownership, evidence, control status, test results, and version history for internal and external assurance. |
| Strengthen Vendor Governance | Evaluate AI vendors consistently across security, data handling, model risk, compliance, and operational assurance criteria. |
| Improve Operational Visibility | Establish monitoring, logging, detection, response, and continuous improvement expectations for AI services. |

## 4. Audience

This wiki is intended for the following personas:

| Persona | Primary Need |
|---|---|
| Executive Management | Understand decision points, governance obligations, risk posture, and assurance outcomes. |
| AI Product Owners | Understand required approvals, control gates, risk treatment, and release readiness. |
| AI Product Developers | Implement secure AI applications, integrations, prompts, RAG patterns, agents, APIs, and data flows. |
| AI Security Researchers | Monitor AI threats, evaluate emerging risks, and improve controls. |
| AI Red Teamers | Test AI systems for prompt injection, data leakage, misuse, unsafe tool use, and model abuse. |
| Security Architecture | Define control requirements, review designs, approve exceptions, and maintain standards. |
| Security Engineering | Implement preventive, detective, and responsive controls across the AI lifecycle. |
| SOC and Incident Response | Monitor AI systems, investigate alerts, and respond to AI-related incidents. |
| Vendor Evaluation Teams | Assess supplier capabilities, risks, evidence, contractual controls, and proof-of-concept results. |
| GRC and Compliance | Map AI controls to governance, regulatory, privacy, and assurance requirements. |
| Teams Building, Selling or Auditing AI in the GCC | Find the regional instruments that apply, with role guides and fill-in templates. |
| Teams Building, Selling or Auditing AI under EU Rules | Find the AI Act, GDPR and related instruments that apply, with role guides and fill-in templates. |
| Teams Building, Selling or Auditing AI in Other Jurisdictions | Find the national instruments that apply in Australia, Brazil, Canada, China, India, Japan, Singapore, South Korea, the UK and the US, with a role guide and region-specific templates. |
| Internal Audit | Validate control operation, evidence quality, decision traceability, and governance effectiveness. |

## 5. Wiki Design Principles

The wiki follows eight principles:

- Risk-first: every AI activity starts with a risk, impact, and data sensitivity assessment.
- Control-first: requirements are expressed as reusable control objectives before being mapped to tools or vendors.
- Lifecycle-first: controls apply from discovery through retirement, not only at deployment.
- Persona-friendly: each user group has a clear starting point and operational playbook.
- Vendor-neutral: controls and evaluation criteria are written independently of any product or supplier.
- Sovereignty-aware: architecture and vendor decisions consider UAE residency, jurisdiction, and regulatory expectations.
- Evidence-driven: each control should produce auditable evidence.
- Operationally measurable: ownership, status, exceptions, test results, and improvement actions should be tracked.

## 6. AI Security Operating Model

The wiki supports the following end-to-end operating model:

```text
Discover AI Use Case or Tool
        ↓
Register Intake and Business Owner
        ↓
Classify Data, Users, Integrations, and Criticality
        ↓
Perform AI Risk Assessment
        ↓
Select Required Security, Privacy, Sovereignty, and Compliance Controls
        ↓
Review Architecture and Vendor Posture
        ↓
Approve, Reject, or Treat Risk
        ↓
Implement Secure Design and Controls
        ↓
Validate Through Testing, PoC, and Red Teaming
        ↓
Deploy with Monitoring, Logging, and Incident Response Coverage
        ↓
Collect Evidence and Perform Periodic Assurance
        ↓
Review, Improve, Renew, or Retire
```

## 7. AI Security Lifecycle Navigation

| Lifecycle Stage | Primary Activity | Required Wiki References | Typical Evidence |
|---|---|---|---|
| AI Discovery and Intake | Identify AI tools, use cases, data flows, business owner, and intended users. | [AI Risk Methodology](02_Risk_Management/02A_AI_Risk_Methodology.md), [AI Governance Operating Model](08_Governance/16_AI_Governance_Operating_Model.md) | Intake record, use-case description, business owner, data classification. |
| AI Risk Assessment | Assess business impact, data sensitivity, model exposure, access paths, and vendor dependencies. | [Enterprise AI Risk Register](02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI Security Control Objectives Library](03_Control_Library/03_AI_Security_Control_Objectives_Library.md) | Completed risk assessment, inherent/residual risk, treatment plan. |
| Architecture and Control Design | Define security architecture, data boundaries, identity model, logging, and control requirements. | [AI Security Control Objectives Library](03_Control_Library/03_AI_Security_Control_Objectives_Library.md), [Existing Security Control Baseline](03_Control_Library/04_Existing_Security_Control_Baseline.md), [Microsoft Security Overlap and AI Gaps](03_Control_Library/05_Microsoft_Security_Overlap_and_AI_Gaps.md) | Architecture review, control mapping, exception decisions. |
| AI User Adoption | Govern use of browser AI, enterprise copilots, external AI tools, and acceptable use. | Browser AI security standard, acceptable use standard, governance operating model | User guidance, approved tool list, access controls, awareness records. |
| AI-Assisted Development | Govern developers using AI coding assistants, IDE plugins, and generated code. | IDE security standard, [AI Product Developer Playbook](07_Role_Based_Playbooks/15A_AI_Product_Developer_Playbook.md) | Secure coding checklist, repository review, generated code validation. |
| Custom AI Application Build | Secure LLM apps, RAG pipelines, prompts, APIs, connectors, model gateways, and runtime controls. | [Custom AI Application Runtime Security Standard](04_Domain_Standards/08_Custom_AI_Application_Runtime_Security_Standard.md), [AI Red Team Playbook](06_Testing_and_Assurance/15C_AI_Red_Team_Playbook.md) | Threat model, secure design review, runtime control evidence. |
| Agentic AI Deployment | Govern agents that invoke tools, access systems, perform actions, or chain tasks. | [Agentic AI Security and Tool Governance](04_Domain_Standards/09_Agentic_AI_Security_and_Tool_Governance.md) | Tool permission matrix, approval rules, action logs, rollback controls. |
| Vendor Evaluation | Evaluate AI suppliers, cloud services, models, integrations, and data handling. | [AI Security Vendor Evaluation Master Framework](05_Vendor_Evaluation/11_AI_Security_Vendor_Evaluation_Master_Framework.md) | Vendor questionnaire, evidence pack, PoC results, risk decision. |
| Testing and Assurance | Validate controls through PoC tests, adversarial testing, red teaming, and evidence review. | [AI Security PoC Test Case Library](06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md), [AI Security Audit and Evidence Checklist](06_Testing_and_Assurance/14_AI_Security_Audit_and_Evidence_Checklist.md) | Test results, findings, remediation plan, audit checklist. |
| Monitoring and Operations | Monitor AI usage, suspicious prompts, data leakage, tool invocation, and incidents. | [Assurance: Testing, Monitoring and Response](00_Foundations/08-Assurance-Testing-Monitoring-and-Response.md), [Monitoring, Detection and Response test cases](10_Test_Case_Library/L17-monitoring-detection-and-response.md), runtime standard, governance operating model | Logs, alerts, incident records, response actions. |
| Audit and Continuous Improvement | Review governance effectiveness, control operation, exceptions, and maturity. | [AI Security Audit and Evidence Checklist](06_Testing_and_Assurance/14_AI_Security_Audit_and_Evidence_Checklist.md), [AI Governance Operating Model](08_Governance/16_AI_Governance_Operating_Model.md) | Audit evidence, management actions, maturity roadmap. |
| Regional Compliance (GCC) | Identify the UAE and other GCC instruments that apply, and record what has been verified against the primary text. | [GCC AI Regulatory Hub](11_GCC_AI_Compliance/01_GCC_AI_Regulatory_Hub.md), [Regulatory Crosswalk](11_GCC_AI_Compliance/07_Regulatory_Crosswalk.md), [templates T01 to T12](11_GCC_AI_Compliance/index.md) | Regulator register, impact assessments, residency attestation, bilingual notices. |
| Regional Compliance (EU) | Classify each system by AI Act role and risk tier, identify the EU instruments that apply, and record what has been verified against the primary text. | [EU AI Regulatory Hub](12_EU_AI_Compliance/01_EU_AI_Regulatory_Hub.md), [EU Regulatory Crosswalk](12_EU_AI_Compliance/07_Regulatory_Crosswalk.md), [templates T01 to T12](12_EU_AI_Compliance/index.md) | Classification records, impact assessments, transfer records, transparency notices, technical file index. |
| Regional Compliance (Other Jurisdictions) | Identify the national instruments that apply, and record what has been verified against the primary text. | [Australia](13_Australia_AI_Compliance/index.md), [Brazil](14_Brazil_AI_Compliance/index.md), [Canada](15_Canada_AI_Compliance/index.md), [China](16_China_AI_Compliance/index.md), [India](17_India_AI_Compliance/index.md), [Japan](18_Japan_AI_Compliance/index.md), [Singapore](19_Singapore_AI_Compliance/index.md), [South Korea](20_South_Korea_AI_Compliance/index.md), [UK](21_UK_AI_Compliance/index.md), [US](22_US_AI_Compliance/index.md) | Regulatory register, region-specific records and templates. |

## 8. Navigation by Role

| Role | Start Here | Secondary References | Expected Outcomes |
|---|---|---|---|
| Executive Management | [AI Governance Operating Model](08_Governance/16_AI_Governance_Operating_Model.md) | [Enterprise AI Risk Register](02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI Security Audit and Evidence Checklist](06_Testing_and_Assurance/14_AI_Security_Audit_and_Evidence_Checklist.md) | Clear AI risk posture, governance decisions, accountability, and audit readiness. |
| AI Product Owner | [AI Risk Methodology](02_Risk_Management/02A_AI_Risk_Methodology.md) | [Custom AI Application Runtime Security Standard](04_Domain_Standards/08_Custom_AI_Application_Runtime_Security_Standard.md), [AI Security PoC Test Case Library](06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md) | Approved risk treatment, implementation plan, release evidence. |
| AI Product Developer | [Custom AI Application Runtime Security Standard](04_Domain_Standards/08_Custom_AI_Application_Runtime_Security_Standard.md) | [AI Product Developer Playbook](07_Role_Based_Playbooks/15A_AI_Product_Developer_Playbook.md), [AI Security PoC Test Case Library](06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md), [Guide for AI Practitioners in the GCC](11_GCC_AI_Compliance/02_Guide_AI_Practitioners.md), [Guide for AI Practitioners Working Under EU Rules](12_EU_AI_Compliance/02_Guide_AI_Practitioners.md) | Secure implementation aligned with required controls and test cases. |
| AI Security Researcher | [AI Security Market and Technology Landscape: Summary](01_Strategy_and_Market/01_AI_Security_Market_and_Technology_Landscape.md) | [AI Security Researcher Playbook](07_Role_Based_Playbooks/15B_AI_Security_Researcher_Playbook.md), [AI Security Glossary and Taxonomy](09_Reference/18_AI_Security_Glossary_and_Taxonomy.md) | Updated threat insights, control improvements, and emerging risk intelligence. |
| AI Red Teamer | [AI Red Team Playbook](06_Testing_and_Assurance/15C_AI_Red_Team_Playbook.md) | [Custom AI Application Runtime Security Standard](04_Domain_Standards/08_Custom_AI_Application_Runtime_Security_Standard.md), [Agentic AI Security and Tool Governance](04_Domain_Standards/09_Agentic_AI_Security_and_Tool_Governance.md) | Test plans, findings, exploit paths, recommended mitigations. |
| Security Engineering | [AI Security Control Objectives Library](03_Control_Library/03_AI_Security_Control_Objectives_Library.md) | [Existing Security Control Baseline](03_Control_Library/04_Existing_Security_Control_Baseline.md), [Microsoft Security Overlap and AI Gaps](03_Control_Library/05_Microsoft_Security_Overlap_and_AI_Gaps.md) | Implementable controls, baseline mapping, monitoring requirements. |
| Security Architecture | [AI Security Control Objectives Library](03_Control_Library/03_AI_Security_Control_Objectives_Library.md) | [Custom AI Application Runtime Security Standard](04_Domain_Standards/08_Custom_AI_Application_Runtime_Security_Standard.md), [Sovereign AI, UAE Compliance and Data Residency Requirements](04_Domain_Standards/10_Sovereign_AI_UAE_Compliance_and_Data_Residency.md) | Approved AI designs, control exceptions, reference architectures. |
| SOC and Incident Response | Runtime security standard | [Assurance: Testing, Monitoring and Response](00_Foundations/08-Assurance-Testing-Monitoring-and-Response.md), [AI for Security and AI-Enabled Threats](00_Foundations/10-AI-for-Security-and-AI-Enabled-Threats.md), [AI Incident Response and Forensics test cases](10_Test_Case_Library/D12-ai-incident-response-and-forensics.md), audit evidence checklist | Monitoring coverage, detection logic, investigation and response records. |
| Vendor Evaluation Team | [AI Security Vendor Evaluation Master Framework](05_Vendor_Evaluation/11_AI_Security_Vendor_Evaluation_Master_Framework.md) | [AI Security PoC Test Case Library](06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md), [T03 Vendor Due-Diligence GCC Addendum](11_GCC_AI_Compliance/T03_Vendor_Due_Diligence_GCC_Addendum.md), [T03 Supplier Due-Diligence EU Addendum](12_EU_AI_Compliance/T03_Supplier_Due_Diligence_EU_Addendum.md) | Consistent supplier scoring, risk decision, and evidence retained. |
| Governance and Compliance | [Enterprise AI Risk Register](02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [Sovereign AI, UAE Compliance and Data Residency Requirements](04_Domain_Standards/10_Sovereign_AI_UAE_Compliance_and_Data_Residency.md), [AI Governance Operating Model](08_Governance/16_AI_Governance_Operating_Model.md), [GCC AI Regulatory Hub](11_GCC_AI_Compliance/01_GCC_AI_Regulatory_Hub.md), [Guide for Implementors](11_GCC_AI_Compliance/05_Guide_Implementors.md), [EU AI Regulatory Hub](12_EU_AI_Compliance/01_EU_AI_Regulatory_Hub.md) | Compliance mapping, risk treatment, approval records, and reporting. |
| Internal Audit | [AI Security Audit and Evidence Checklist](06_Testing_and_Assurance/14_AI_Security_Audit_and_Evidence_Checklist.md) | Control library, PoC evidence library, sovereignty requirements, [Guide for Auditors of AI Systems in the GCC](11_GCC_AI_Compliance/04_Guide_Auditors.md), [Guide for Auditors of AI Systems Under EU Rules](12_EU_AI_Compliance/04_Guide_Auditors.md) | Independent evidence validation and control effectiveness assessment. |

## 9. Core Repository Structure

```text
00_Foundations/
  Research paper "AI Security vs. Security of AI": terminology, two-axis model, threat taxonomy, reference architecture,
  assurance, standards, maturity roadmap, and references.

01_Strategy_and_Market/
  AI security market landscape, technology trends, threat intelligence, glossary, and taxonomy.

02_Risk_Management/
  Risk methodology, enterprise AI risk register, risk treatment, exception model, and risk mapping.

03_Control_Library/
  Control objectives, existing baseline, Microsoft overlap, control gaps, and implementation guidance.

04_Domain_Standards/
  Browser AI, IDE AI, runtime AI applications, agentic AI, sovereignty, and data residency standards.

05_Vendor_Evaluation/
  Vendor master framework, supplier evidence model, and proof-of-concept scorecards.

06_Testing_and_Assurance/
  PoC tests, adversarial testing, red team methodology, audit checklist, and evidence library.

07_Role_Based_Playbooks/
  Persona-specific guidance for developers, researchers, red teamers, governance, audit, and operations.

08_Governance/
  Operating model, acceptable AI use, approvals, committees, responsibilities, and reporting cadence.

10_Test_Case_Library/
  653 detailed product evaluation test cases across 17 AI lifecycle layers and 6 emerging domains, with reference index,
  lab prerequisites, and framework adoption guide.

11_GCC_AI_Compliance/
  Regulatory hub for the UAE, Saudi Arabia, Qatar, Bahrain and Oman, role guides, fill-in templates,
  fairness control drivers, regulatory crosswalk, and evidence register.

12_EU_AI_Compliance/
  Regulatory hub for the EU AI Act, GDPR and related EU instruments, role guides, fill-in templates,
  impact assessment and fairness control drivers, regulatory crosswalk, and evidence register.

13_Australia_AI_Compliance/
  Regulatory hub for Australia (Privacy Act automated-decision transparency, consumer law, APRA standards),
  role guide, two templates, and regulatory crosswalk.

14_Brazil_AI_Compliance/
  Regulatory hub for Brazil (LGPD, sector rules, pending AI bill PL 2338/2023), role guide, two templates,
  and regulatory crosswalk.

15_Canada_AI_Compliance/
  Regulatory hub for Canada (PIPEDA, Quebec Law 25, federal automated decision directive, OSFI E-23),\n  role guide, three templates, and regulatory crosswalk.

16_China_AI_Compliance/
  Regulatory hub for mainland China (generative AI, algorithm, deep synthesis, labelling and ethics review\n  measures, PIPL and data laws), role guide, three templates, and regulatory crosswalk.

17_India_AI_Compliance/
  Regulatory hub for India (DPDP Act and Rules, MeitY guidelines, RBI, SEBI, IRDAI, CERT-In), role guide,\n  three templates, and regulatory crosswalk.

18_Japan_AI_Compliance/
  Regulatory hub for Japan (AI Promotion Act, Guidelines for AI Business, APPI, copyright law), role guide,\n  two templates, and regulatory crosswalk.

19_Singapore_AI_Compliance/
  Regulatory hub for Singapore (IMDA frameworks including agentic AI, AI Verify, PDPA, MAS and CSA guidance),\n  role guide, three templates, and regulatory crosswalk.

20_South_Korea_AI_Compliance/
  Regulatory hub for South Korea (AI Basic Act, generative AI labelling, high-impact AI, domestic representative),\n  role guide, three templates, and regulatory crosswalk.

21_UK_AI_Compliance/
  Regulatory hub for the UK (UK GDPR, Data (Use and Access) Act 2025, ICO, FCA and PRA expectations),\n  role guide, three templates, and regulatory crosswalk.

22_US_AI_Compliance/
  Regulatory hub for the US (federal orders and enforcement, NIST AI RMF, state AI laws), role guide,\n  three templates, and regulatory crosswalk.

23_Framework_Crosswalks/
  Cross-references from this wiki to other AI governance frameworks, the FINOS AI Governance Framework (risk and
  mitigation identifiers) and the AI Baseline Control Framework (20 baseline controls).

09_Reference/
  Glossary, taxonomy, abbreviations, mapping references, patterns, and reusable templates.
```

## 10. Standards and Policy Hierarchy

```text
Enterprise AI Security Policy
│
├─ AI Governance Operating Model
├─ AI Risk Management Methodology
├─ AI Security Control Objectives Library
├─ AI User Adoption and Acceptable Use Standard
├─ AI-Assisted Development Security Standard
├─ Custom AI Application Runtime Security Standard
├─ Agentic AI Security and Tool Governance Standard
├─ Sovereign AI, UAE Compliance, and Data Residency Standard
├─ AI Vendor Evaluation Master Framework
├─ AI Testing, Red Teaming, and PoC Test Library
└─ AI Audit and Evidence Checklist
```

## 11. Governance and Accountability

| Function | Responsibility | Typical Evidence |
|---|---|---|
| AI Governance Committee | Provide strategic oversight, approve high-risk AI decisions, review exceptions, and monitor maturity. | Meeting minutes, approvals, risk acceptance records. |
| Business Owner | Own the AI use case, business justification, user population, operational impact, and benefits realization. | Business case, use-case record, user list, process ownership. |
| Data Owner | Confirm classification, permitted use, residency requirements, retention rules, and data-sharing limitations. | Data classification, data flow diagram, approval record. |
| Security Architecture | Approve target architecture, control design, exceptions, and reference patterns. | Architecture review, control mapping, exception register. |
| Security Engineering | Implement preventive and detective controls across identity, data, endpoint, network, cloud, application, and monitoring layers. | Configuration evidence, control test output, deployment records. |
| AI Engineering | Build and maintain AI workflows, prompts, model integrations, RAG pipelines, agents, and application controls. | Design documentation, repository controls, deployment logs. |
| SOC and Incident Response | Monitor AI activity, investigate events, respond to incidents, and recommend detection improvements. | SIEM alerts, incident tickets, investigation notes. |
| GRC and Compliance | Maintain framework mappings, compliance obligations, risk reporting, and audit coordination. | Control mapping, compliance assessment, evidence register. |
| Vendor Management | Coordinate AI supplier due diligence, contract requirements, evidence reviews, and renewal checkpoints. | Vendor assessment, contract clauses, SLA/security addenda. |
| Internal Audit | Independently validate governance, control design, operating effectiveness, and evidence quality. | Audit plan, findings, management action tracking. |

## 12. Control Framework Mapping

The wiki supports mapping AI security requirements to recognized control and governance frameworks. The detailed mapping should be maintained in the control library and audit checklist. How the instruments relate to each other is explained in [Governance, Standards and Regulation](00_Foundations/09-Governance-Standards-and-Regulation.md). UAE and other GCC instruments are listed one by one, with their verification status, in the [GCC AI Regulatory Hub](11_GCC_AI_Compliance/01_GCC_AI_Regulatory_Hub.md). The AI Act, GDPR and related EU instruments are listed the same way in the [EU AI Regulatory Hub](12_EU_AI_Compliance/01_EU_AI_Regulatory_Hub.md).

| Framework / Requirement Area | Wiki Mapping Purpose |
|---|---|
| ISO/IEC 27001 | Information security governance, risk management, access control, operations, supplier security, and audit evidence. |
| ISO/IEC 42001 | AI management system governance, accountability, lifecycle controls, risk treatment, and continuous improvement. |
| NIST AI RMF | AI risk identification, measurement, management, governance, and trustworthiness characteristics. |
| NIST AI 100-2 (Adversarial Machine Learning) | Shared vocabulary for attack classes and the scope of adversarial testing. |
| OWASP Top 10 for LLM Applications and for Agentic Applications | Application and agent risk categories for developer guidance, threat modeling, and test-case design. |
| MITRE ATLAS | Adversary tactics and techniques against AI-enabled systems for threat-informed testing and incident description. |
| EU AI Act | Legal obligations for in-scope providers and deployers of AI systems. |
| NIST Cybersecurity Framework | Identify, Protect, Detect, Respond, and Recover coverage for AI-enabled systems. |
| CIS Controls | Practical safeguards for inventory, identity, access, endpoint, network, data protection, monitoring, and response. |
| UAE Information Assurance and Cybersecurity Expectations | Alignment to local cybersecurity governance, data handling, hosting, resilience, and assurance obligations. |
| UAE Data Residency and Sovereignty Requirements | Jurisdictional control over regulated data, hosting location, cross-border processing, vendor access, and evidence. |
| Privacy and Data Protection Obligations | Data minimization, purpose limitation, consent/legal basis, retention, access, and breach response considerations. |

## 13. Key Control Domains

The control library should maintain detailed objectives, implementation guidance, evidence expectations, and test procedures for at least the following domains:

| Domain | Control Intent |
|---|---|
| AI Inventory and Intake | Maintain a complete register of AI tools, models, agents, data flows, owners, and approval status. |
| Data Protection | Prevent sensitive data disclosure through prompts, training, fine-tuning, logs, telemetry, plugins, or vendor access. |
| Identity and Access Management | Enforce least privilege, strong authentication, role-based access, service identity controls, and privileged action review. |
| Prompt and Input Security | Detect and reduce prompt injection, jailbreak attempts, malicious instructions, unsafe content, and data exfiltration prompts. |
| Output Validation | Manage hallucination, unsafe recommendations, policy violations, misinformation, and unsupported decisions. |
| RAG and Knowledge Security | Protect indexes, embeddings, retrieval permissions, source grounding, and document-level authorization. |
| Agent and Tool Governance | Control tool permissions, action approval, execution boundaries, rollback, and transaction logging. |
| Application and API Security | Secure AI application interfaces, model gateways, secrets, rate limits, session handling, and error handling. |
| Model and Vendor Risk | Evaluate model provenance, data usage, contractual protections, operational resilience, and third-party exposure. |
| Monitoring and Detection | Capture AI activity logs, anomalous prompts, tool calls, data movement, model misuse, and policy violations. |
| Incident Response | Define AI incident categories, escalation paths, investigation evidence, containment, and lessons learned. |
| Audit and Assurance | Maintain traceable evidence of control design, operation, testing, exceptions, and remediation. |

## 14. Vendor-Neutral Operating Rule

This wiki does not publish profiles of individual products or suppliers. Do not use vendor evaluation records as the primary source of truth for controls.

Controls and standards must remain vendor-neutral. Vendor documents should reference the relevant control objectives, evidence requirements, and PoC tests rather than replacing enterprise standards.

Your own vendor evaluation records should be used to record:

- Supplier capabilities and limitations.
- Contractual and compliance evidence.
- Data residency and processing details.
- Model and service security assurances.
- PoC test results.
- Known gaps, compensating controls, and residual risk decisions.

## 15. Wiki Maintenance and Publishing Rules

| Rule | Requirement |
|---|---|
| Ownership | Each wiki document must have a named owner and custodian. |
| Review Frequency | Controlled pages must be reviewed at least quarterly or after major AI, regulatory, or threat changes. |
| Change Control | Significant changes to standards, control objectives, or risk methodology require approval by the appropriate governance authority. |
| Evidence Linkage | Control pages should link to expected evidence, test cases, and audit checklist items. |
| Version History | Every controlled page must maintain a version history with date, author, approver, and summary of change. |
| Cross-Reference Consistency | Document names, control IDs, test IDs, and risk IDs must remain consistent across the wiki. |
| Vendor Neutrality | The wiki names no individual products or suppliers. Vendor evaluation records must map to standards and controls; they must not redefine them. |
| Exceptions | Exceptions must document business justification, compensating controls, expiry date, and approval authority. |

## 16. How to Use This Wiki

1. Start with the lifecycle stage that matches the AI initiative.
2. Use the role navigation table to identify the correct starting document.
3. Register the AI use case or tool before implementation or procurement.
4. Complete the AI risk assessment and apply required control objectives.
5. Use the domain standard that matches the AI implementation pattern.
6. Perform vendor assessment for third-party AI services, platforms, plugins, models, or integrations.
7. Run the required PoC and security tests before production use.
8. Collect evidence continuously for audit, compliance, and management reporting.
9. Update the risk register when controls, scope, vendors, models, or data flows change.
10. Review and improve controls based on incidents, findings, threat intelligence, and regulatory change.

## 17. Priority Implementation Roadmap

| Phase | Focus Area | Outcome |
|---|---|---|
| Phase 1 | Establish inventory, intake, risk methodology, and governance decision model. | AI initiatives become visible, owned, and risk-ranked. |
| Phase 2 | Publish control library, domain standards, and vendor evaluation framework. | Teams apply consistent controls and vendor due diligence. |
| Phase 3 | Implement testing, red teaming, monitoring, and evidence collection. | Security effectiveness becomes measurable and auditable. |
| Phase 4 | Mature reporting, metrics, automation, and continuous improvement. | AI security becomes operationalized and management-visible. |

A time-boxed version of this roadmap (30 days, 90 days, 6 months, 12 to 24 months) is in [Maturity Model and Roadmap](00_Foundations/11-Maturity-Model-and-Roadmap.md).

## 18. Success Metrics

| Metric | Why It Matters |
|---|---|
| Percentage of AI Tools Registered | Measures visibility and intake coverage. |
| Percentage of AI Use Cases Risk Assessed | Measures governance adoption. |
| High-Risk AI Initiatives with Approved Treatment Plans | Measures risk decision quality. |
| AI Vendors Assessed before Onboarding | Measures supplier governance coverage. |
| AI Applications with Completed Security Testing | Measures release readiness. |
| AI Systems with Monitoring and Logging Enabled | Measures operational visibility. |
| Open AI Control Exceptions past Expiry | Measures governance discipline. |
| Audit Evidence Completeness Score | Measures assurance readiness. |
| Number of AI Security Findings Remediated | Measures improvement execution. |

These metrics measure coverage. For control-effectiveness metrics such as injection test success rate, privileged-action gating, and time to disable, see [Assurance: Testing, Monitoring and Response](00_Foundations/08-Assurance-Testing-Monitoring-and-Response.md#85-metrics).

## 19. Document Governance

| Item | Value |
|---|---|
| Original Author | Nachiket Sathaye |
| Document Owner | AI Security Program |
| Custodian | Security Architecture Team |
| Status | Published |
| Review Cycle | Quarterly |
| Approval Authority | AI Governance Committee |
| Primary Users | AI, cybersecurity, GRC, compliance, vendor evaluation, operations, and audit teams |

## 20. Version History

| Version | Date | Author | Summary of Change |
|---|---|---|---|
| 1.0 | Initial release | Nachiket Sathaye | Initial wiki home page with purpose, audience, design principle, role navigation, lifecycle navigation, folder structure, and vendor-neutral operating rule. |
| 2.0 | 2026-07-27 | Nachiket Sathaye | Expanded the home page with mission, strategic objectives, operating model, governance, standards hierarchy, framework mapping, maintenance rules, roadmap, metrics, and fuller navigation. |
| 2.1 | 2026-10-07 | Nachiket Sathaye | Added the Foundations section (research paper: AI Security vs. Security of AI) and linked it from the purpose, navigation, framework mapping, roadmap, and metrics sections. |
| 2.2 | 2026-10-07 | Nachiket Sathaye | Added the GCC AI Compliance section: regulatory hub, four role guides, twelve templates, proposed fairness control, crosswalk and evidence register. Regional content is secondary-sourced and its verification is in progress. |
| 2.3 | 2026-10-07 | Nachiket Sathaye | Added the EU AI Compliance section: regulatory hub, four role guides, twelve templates, proposed impact assessment control, crosswalk and evidence register. EU content comes from secondary sources and from memory of the legal text, and has not been verified against the Official Journal. |
| 2.4 | 2026-10-07 | Nachiket Sathaye | Added the Australia AI Compliance section: regulatory hub, role guide, templates and crosswalk. Its content comes from secondary sources and from memory of the law, and has not been verified against primary legal text. |
| 2.5 | 2026-10-07 | Nachiket Sathaye | Added the Brazil AI Compliance section: regulatory hub, role guide, templates and crosswalk. Its content comes from secondary sources and from memory of the law, and has not been verified against primary legal text. |
| 2.6 | 2026-10-07 | Nachiket Sathaye | Added the Canada AI Compliance section: regulatory hub, role guide, templates and crosswalk. Its content comes from secondary sources and from memory of the law, and has not been verified against primary legal text. |
| 2.7 | 2026-10-07 | Nachiket Sathaye | Added the China AI Compliance section: regulatory hub, role guide, templates and crosswalk. Its content comes from secondary sources and from memory of the law, and has not been verified against primary legal text. |
| 2.8 | 2026-10-07 | Nachiket Sathaye | Added the India AI Compliance section: regulatory hub, role guide, templates and crosswalk. Its content comes from secondary sources and from memory of the law, and has not been verified against primary legal text. |
| 2.9 | 2026-10-07 | Nachiket Sathaye | Added the Japan AI Compliance section: regulatory hub, role guide, templates and crosswalk. Its content comes from secondary sources and from memory of the law, and has not been verified against primary legal text. |
| 2.10 | 2026-10-07 | Nachiket Sathaye | Added the Singapore AI Compliance section: regulatory hub, role guide, templates and crosswalk. Its content comes from secondary sources and from memory of the law, and has not been verified against primary legal text. |
| 2.11 | 2026-10-07 | Nachiket Sathaye | Added the South Korea AI Compliance section: regulatory hub, role guide, templates and crosswalk. Its content comes from secondary sources and from memory of the law, and has not been verified against primary legal text. |
| 2.12 | 2026-10-07 | Nachiket Sathaye | Added the UK AI Compliance section: regulatory hub, role guide, templates and crosswalk. Its content comes from secondary sources and from memory of the law, and has not been verified against primary legal text. |
| 2.13 | 2026-10-07 | Nachiket Sathaye | Added the US AI Compliance section: regulatory hub, role guide, templates and crosswalk. Its content comes from secondary sources and from memory of the law, and has not been verified against primary legal text. |
| 2.14 | 2026-10-07 | Nachiket Sathaye | Added four controls (AI-CTRL-041 to AI-CTRL-044: fairness, impact assessment, authority engagement, AI literacy), nine test cases (TC-L03-031 to TC-L03-039), a sector overlays page and a regional crosswalk by control theme. The regional sections now point to these controls and cases. |
| 2.15 | 2026-10-10 | Nachiket Sathaye | Added 15 risks to the register (AI-R14 to AI-R28), two controls (AI-CTRL-045 human oversight design and AI-CTRL-046 intellectual property), wording changes to six existing controls, FINOS AI Governance Framework columns in the risk to control mapping, a use-case risk triage page, a Framework Crosswalks section with the FINOS and AI BCF crosswalks, and a positioning statement on the home page. |
| 2.16 | 2026-10-10 | Nachiket Sathaye | Changed the licence from CC BY 4.0 to CC BY-SA 4.0; earlier versions remain available under CC BY 4.0. Updated the US bank model risk references after SR 11-7 was replaced by SR 26-2 and OCC Bulletin 2026-13. |
| 2.17 | 2026-10-10 | Nachiket Sathaye | Added a Legal force column to the twelve regional crosswalks and their CSV files, so each instrument is labelled as binding law, binding in scope, guidance, voluntary, proposed, context or unclear. Added a link and identifier check for contributors, and rules for reusing the wiki to the Community Rules. |
| 2.18 | 2026-10-10 | Nachiket Sathaye | Added a Risk, Control and Test Traceability page, generated at build time from the risk mapping and the test cases. Every page footer now shows the date the page last changed, and a page can record a review date with an optional `last_reviewed` line. |
| 2.19 | 2026-10-10 | Nachiket Sathaye | Added three test cases (TC-L03-040 to TC-L03-042) for human oversight effectiveness and AI vendor terms, and pointed four existing cases at AI-CTRL-045 and AI-CTRL-046, so every control now has at least one test case. The library holds 632 cases. |
| 2.20 | 2026-10-10 | Nachiket Sathaye | EU AI Compliance: checked twelve crosswalk rows against the Official Journal or the issuing body's page and tagged them [Verified], with the primary URL and retrieval date. The Digital Omnibus on AI is confirmed as Regulation (EU) 2026/1744, in force since 27 July 2026, with the high-risk dates of 2 December 2027 and 2 August 2028. |
| 2.21 | 2026-10-10 | Nachiket Sathaye | GCC AI Compliance: checked four crosswalk rows (S2, S3, S4 and B1) against documents on the SDAIA and Bahrain Personal Data Protection Authority sites and tagged them [Verified]. SDAIA's current AI Ethics Principles document is SDAIA-P114E, version 1, May 2025. Most other government sites refused automated retrieval, so the remaining rows keep their tags. |
| 2.22 | 2026-10-10 | Nachiket Sathaye | Framework Crosswalks: added five pages. Four are generated at build time from the control library and the test cases (NIST AI RMF, ISO/IEC 42001, the OWASP Top 10 lists and MITRE ATLAS). The fifth maps the twelve generative AI risks in NIST AI 600-1 to the wiki's risks and controls. |
| 2.23 | 2026-10-10 | Nachiket Sathaye | Added 21 test cases: nine on agent-to-agent communication (TC-L06-038 to TC-L06-046), six on identity for training jobs (TC-L13-021 to TC-L13-026) and six on identity for model serving and registries (TC-L12-026 to TC-L12-031). AI-CTRL-006 and AI-CTRL-015 now cite OWASP ASI07, AI-CTRL-016 maps to AI-R08, and three controls gained wording on agent-to-agent and workload identity. The library holds 653 cases. |
| 2.24 | 2026-10-10 | Nachiket Sathaye | Singapore AI Compliance: updated from the MAS Guidelines on Artificial Intelligence Risk Management issued on 7 October 2026, which take effect on 7 October 2027. The crosswalk now maps the Guidelines paragraph by paragraph to wiki controls and test cases, and the SG-T2 template follows the final text. The sector overlays cite the Guidelines. |

## 21. Quick Links

- [Foundations: AI Security vs. Security of AI](00_Foundations/index.md)
- [AI Security Market and Technology Landscape: Summary](01_Strategy_and_Market/01_AI_Security_Market_and_Technology_Landscape.md)
- [AI Risk Methodology](02_Risk_Management/02A_AI_Risk_Methodology.md)
- [Enterprise AI Risk Register](02_Risk_Management/02B_Enterprise_AI_Risk_Register.md)
- [AI Security Control Objectives Library](03_Control_Library/03_AI_Security_Control_Objectives_Library.md)
- [Existing Security Control Baseline](03_Control_Library/04_Existing_Security_Control_Baseline.md)
- [Microsoft Security Overlap and AI Gaps](03_Control_Library/05_Microsoft_Security_Overlap_and_AI_Gaps.md)
- [Custom AI Application Runtime Security Standard](04_Domain_Standards/08_Custom_AI_Application_Runtime_Security_Standard.md)
- [Agentic AI Security and Tool Governance](04_Domain_Standards/09_Agentic_AI_Security_and_Tool_Governance.md)
- [Sovereign AI, UAE Compliance and Data Residency Requirements](04_Domain_Standards/10_Sovereign_AI_UAE_Compliance_and_Data_Residency.md)
- [AI Security Vendor Evaluation Master Framework](05_Vendor_Evaluation/11_AI_Security_Vendor_Evaluation_Master_Framework.md)
- [AI Security PoC Test Case Library](06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md)
- [Test Case Library (653 cases, 17 layers and 6 emerging domains)](10_Test_Case_Library/index.md)
- [GCC AI Compliance (regulatory hub, role guides and templates)](11_GCC_AI_Compliance/index.md)
- [EU AI Compliance (AI Act hub, role guides and templates)](12_EU_AI_Compliance/index.md)
- [Australia AI Compliance (regulatory hub, role guide and templates)](13_Australia_AI_Compliance/index.md)
- [Brazil AI Compliance (regulatory hub, role guide and templates)](14_Brazil_AI_Compliance/index.md)
- [Canada AI Compliance (regulatory hub, role guide and templates)](15_Canada_AI_Compliance/index.md)
- [China AI Compliance (regulatory hub, role guide and templates)](16_China_AI_Compliance/index.md)
- [India AI Compliance (regulatory hub, role guide and templates)](17_India_AI_Compliance/index.md)
- [Japan AI Compliance (regulatory hub, role guide and templates)](18_Japan_AI_Compliance/index.md)
- [Singapore AI Compliance (regulatory hub, role guide and templates)](19_Singapore_AI_Compliance/index.md)
- [South Korea AI Compliance (regulatory hub, role guide and templates)](20_South_Korea_AI_Compliance/index.md)
- [UK AI Compliance (regulatory hub, role guide and templates)](21_UK_AI_Compliance/index.md)
- [US AI Compliance (regulatory hub, role guide and templates)](22_US_AI_Compliance/index.md)
- [Framework Crosswalks (FINOS AIGF, AI BCF, NIST AI RMF, NIST AI 600-1, ISO/IEC 42001, OWASP, MITRE ATLAS)](23_Framework_Crosswalks/index.md)
- [Community Rules](community-rules.md)
- [AI Security Audit and Evidence Checklist](06_Testing_and_Assurance/14_AI_Security_Audit_and_Evidence_Checklist.md)
- [AI Product Developer Playbook](07_Role_Based_Playbooks/15A_AI_Product_Developer_Playbook.md)
- [AI Security Researcher Playbook](07_Role_Based_Playbooks/15B_AI_Security_Researcher_Playbook.md)
- [AI Red Team Playbook](06_Testing_and_Assurance/15C_AI_Red_Team_Playbook.md)
- [AI Governance Operating Model](08_Governance/16_AI_Governance_Operating_Model.md)
- [AI Security Glossary and Taxonomy](09_Reference/18_AI_Security_Glossary_and_Taxonomy.md)

## 22. About the Author

<div class="profile-head"><img class="profile-photo" src="assets/nachiket-sathaye.jpg" alt="Nachiket Sathaye" width="88" height="88"><p><strong>Nachiket Sathaye</strong><br><strong>Cybersecurity Leader, AI Security and Governance</strong></p></div>

Cybersecurity professional with 20+ years of experience across Critical Infrastructure, BFSI and Manufacturing. I work at both the technical and the executive level, aligning GRC, Zero Trust, security architecture and AI governance with business outcomes.

My current focus is helping organisations adopt GenAI, RAG and agentic systems securely across the full AI lifecycle, and building NIST AI RMF, ISO/IEC 42001, EU AI Act and Responsible AI principles into enterprise programmes.

LinkedIn: [linkedin.com/in/nachiket-sathaye](https://www.linkedin.com/in/nachiket-sathaye/)

## 23. About the Co-Author

<div class="profile-head"><img class="profile-photo" src="assets/ankush-jain.jpg" alt="Ankush Jain" width="88" height="88"><p><strong>Ankush Jain</strong><br><strong>Cybersecurity Governance &amp; Risk Leader | AI Security &amp; Digital Trust Strategist | CISSP, CCSP</strong></p></div>

Governance-focused cybersecurity leader with 19+ years of experience protecting critical infrastructure and global enterprises across MENA and APAC. I specialize in cybersecurity governance, enterprise risk management, AI risk reviews, and digital trust frameworks that enable organizations to embrace transformation securely.

LinkedIn: [linkedin.com/in/ankushjai](https://www.linkedin.com/in/ankushjai/)
