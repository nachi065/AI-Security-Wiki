---
title: "Home"
description: "Open, vendor-neutral AI security wiki: governance, risk, security controls, agentic AI standards, vendor evaluation, regional compliance and 629 test cases."
nav_order: 1
document_type: Enterprise AI Security Reference Architecture and Governance Wiki
version: 2.14
status: Published
author: Nachiket Sathaye
coauthors: Ankush Jain
owner: AI Security Program
custodian: Security Architecture Team
review_cycle: Quarterly
approval_authority: AI Governance Committee
last_updated: 2026-10-07
---

# AI Security Wiki Home

> **Document type:** Enterprise AI Security Reference Architecture and Governance Wiki  
> **Version:** 2.14  
> **Status:** Published  
> **Original author:** Nachiket Sathaye ([about the author](#22-about-the-author))  
> **Co-author:** Ankush Jain ([about the co-author](#23-about-the-co-author))  
> **Intended use:** Public, vendor-neutral reference and template set for AI security governance, engineering, risk management, assurance, audit, compliance, and vendor evaluation.

## 1. Purpose

The AI Security Wiki is a reference for securing AI adoption across an enterprise. It covers AI governance, AI risk management, secure engineering, operational monitoring, vendor evaluation, and assurance, in pages that can be reused as templates and that say what audit evidence each activity should produce.

The wiki helps teams answer five practical questions:

1. Can this AI use case be safely adopted?
2. What risks, controls, and approvals are required?
3. Which engineering standards apply to the implementation?
4. How will security, privacy, sovereignty, and compliance requirements be evidenced?
5. How will the AI capability be monitored, tested, audited, and improved over time?

New to the subject? Start with [Foundations: AI Security vs. Security of AI](00_Foundations/index.md), the research paper that explains the concepts and sources behind the standards, templates, and test cases in the rest of the wiki.

## 2. Mission Statement

Establish a secure, governed, sovereign, and auditable approach to AI adoption by giving business, technology, cybersecurity, governance, compliance, audit, and vendor evaluation teams a common operating reference.

The aim is to let teams adopt AI while reducing the risk of data leakage, prompt injection, model misuse, insecure agent actions, third-party exposure, regulatory non-compliance, and operational blind spots.

## 3. Strategic Objectives

| Objective | Description |
|---|---|
| Protect enterprise data | Prevent unauthorized disclosure of confidential, regulated, operational, customer, and sensitive business information to AI systems. |
| Secure AI systems | Ensure AI-enabled applications, copilots, agents, models, connectors, APIs, and data pipelines are resilient against relevant threats. |
| Enable responsible innovation | Provide practical guardrails that allow teams to adopt AI safely without unnecessary friction. |
| Support sovereignty and compliance | Align AI initiatives with UAE data residency, regulatory, privacy, governance, and sector-specific requirements. |
| Standardize AI risk decisions | Use a consistent risk assessment, control selection, treatment, exception, and approval process. |
| Improve audit readiness | Maintain clear ownership, evidence, control status, test results, and version history for internal and external assurance. |
| Strengthen vendor governance | Evaluate AI vendors consistently across security, data handling, model risk, compliance, and operational assurance criteria. |
| Improve operational visibility | Establish monitoring, logging, detection, response, and continuous improvement expectations for AI services. |

## 4. Audience

This wiki is intended for the following personas:

| Persona | Primary Need |
|---|---|
| Executive management | Understand decision points, governance obligations, risk posture, and assurance outcomes. |
| AI product owners | Understand required approvals, control gates, risk treatment, and release readiness. |
| AI product developers | Implement secure AI applications, integrations, prompts, RAG patterns, agents, APIs, and data flows. |
| AI security researchers | Monitor AI threats, evaluate emerging risks, and improve controls. |
| AI red teamers | Test AI systems for prompt injection, data leakage, misuse, unsafe tool use, and model abuse. |
| Security architecture | Define control requirements, review designs, approve exceptions, and maintain standards. |
| Security engineering | Implement preventive, detective, and responsive controls across the AI lifecycle. |
| SOC and incident response | Monitor AI systems, investigate alerts, and respond to AI-related incidents. |
| Vendor evaluation teams | Assess supplier capabilities, risks, evidence, contractual controls, and proof-of-concept results. |
| GRC and compliance | Map AI controls to governance, regulatory, privacy, and assurance requirements. |
| Teams building, selling or auditing AI in the GCC | Find the regional instruments that apply, with role guides and fill-in templates. |
| Teams building, selling or auditing AI under EU rules | Find the AI Act, GDPR and related instruments that apply, with role guides and fill-in templates. |
| Teams building, selling or auditing AI in other jurisdictions | Find the national instruments that apply in Australia, Brazil, Canada, China, India, Japan, Singapore, South Korea, the UK and the US, with a role guide and region-specific templates. |
| Internal audit | Validate control operation, evidence quality, decision traceability, and governance effectiveness. |

## 5. Wiki Design Principles

The wiki follows eight principles:

- Risk-first: every AI activity starts with a risk, impact, and data sensitivity assessment.
- Control-first: requirements are expressed as reusable control objectives before being mapped to tools or vendors.
- Lifecycle-first: controls apply from discovery through retirement, not only at deployment.
- Persona-friendly: each user group has a clear starting point and operational playbook.
- Vendor-neutral: vendor profiles do not replace enterprise control requirements.
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
| AI discovery and intake | Identify AI tools, use cases, data flows, business owner, and intended users. | [AI Risk Methodology](02_Risk_Management/02A_AI_Risk_Methodology.md), [AI Governance Operating Model](08_Governance/16_AI_Governance_Operating_Model.md) | Intake record, use-case description, business owner, data classification. |
| AI risk assessment | Assess business impact, data sensitivity, model exposure, access paths, and vendor dependencies. | [Enterprise AI Risk Register](02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI Security Control Objectives Library](03_Control_Library/03_AI_Security_Control_Objectives_Library.md) | Completed risk assessment, inherent/residual risk, treatment plan. |
| Architecture and control design | Define security architecture, data boundaries, identity model, logging, and control requirements. | [AI Security Control Objectives Library](03_Control_Library/03_AI_Security_Control_Objectives_Library.md), [Existing Security Control Baseline](03_Control_Library/04_Existing_Security_Control_Baseline.md), [Microsoft Security Overlap and AI Gaps](03_Control_Library/05_Microsoft_Security_Overlap_and_AI_Gaps.md) | Architecture review, control mapping, exception decisions. |
| AI user adoption | Govern use of browser AI, enterprise copilots, external AI tools, and acceptable use. | Browser AI security standard, acceptable use standard, governance operating model | User guidance, approved tool list, access controls, awareness records. |
| AI-assisted development | Govern developers using AI coding assistants, IDE plugins, and generated code. | IDE security standard, [AI Product Developer Playbook](07_Role_Based_Playbooks/15A_AI_Product_Developer_Playbook.md) | Secure coding checklist, repository review, generated code validation. |
| Custom AI application build | Secure LLM apps, RAG pipelines, prompts, APIs, connectors, model gateways, and runtime controls. | [Custom AI Application Runtime Security Standard](04_Domain_Standards/08_Custom_AI_Application_Runtime_Security_Standard.md), [AI Red Team Playbook](06_Testing_and_Assurance/15C_AI_Red_Team_Playbook.md) | Threat model, secure design review, runtime control evidence. |
| Agentic AI deployment | Govern agents that invoke tools, access systems, perform actions, or chain tasks. | [Agentic AI Security and Tool Governance](04_Domain_Standards/09_Agentic_AI_Security_and_Tool_Governance.md) | Tool permission matrix, approval rules, action logs, rollback controls. |
| Vendor evaluation | Evaluate AI suppliers, cloud services, models, integrations, and data handling. | [AI Security Vendor Evaluation Master Framework](05_Vendor_Evaluation/11_AI_Security_Vendor_Evaluation_Master_Framework.md), vendor profiles `12A` to `12H` | Vendor questionnaire, evidence pack, PoC results, risk decision. |
| Testing and assurance | Validate controls through PoC tests, adversarial testing, red teaming, and evidence review. | [AI Security PoC Test Case Library](06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md), [AI Security Audit and Evidence Checklist](06_Testing_and_Assurance/14_AI_Security_Audit_and_Evidence_Checklist.md) | Test results, findings, remediation plan, audit checklist. |
| Monitoring and operations | Monitor AI usage, suspicious prompts, data leakage, tool invocation, and incidents. | [Assurance: Testing, Monitoring and Response](00_Foundations/08-Assurance-Testing-Monitoring-and-Response.md), [Monitoring, Detection and Response test cases](10_Test_Case_Library/L17-monitoring-detection-and-response.md), runtime standard, governance operating model | Logs, alerts, incident records, response actions. |
| Audit and continuous improvement | Review governance effectiveness, control operation, exceptions, and maturity. | [AI Security Audit and Evidence Checklist](06_Testing_and_Assurance/14_AI_Security_Audit_and_Evidence_Checklist.md), [AI Governance Operating Model](08_Governance/16_AI_Governance_Operating_Model.md) | Audit evidence, management actions, maturity roadmap. |
| Regional compliance (GCC) | Identify the UAE and other GCC instruments that apply, and record what has been verified against the primary text. | [GCC AI Regulatory Hub](11_GCC_AI_Compliance/01_GCC_AI_Regulatory_Hub.md), [Regulatory Crosswalk](11_GCC_AI_Compliance/07_Regulatory_Crosswalk.md), [templates T01 to T12](11_GCC_AI_Compliance/index.md) | Regulator register, impact assessments, residency attestation, bilingual notices. |
| Regional compliance (EU) | Classify each system by AI Act role and risk tier, identify the EU instruments that apply, and record what has been verified against the primary text. | [EU AI Regulatory Hub](12_EU_AI_Compliance/01_EU_AI_Regulatory_Hub.md), [EU Regulatory Crosswalk](12_EU_AI_Compliance/07_Regulatory_Crosswalk.md), [templates T01 to T12](12_EU_AI_Compliance/index.md) | Classification records, impact assessments, transfer records, transparency notices, technical file index. |
| Regional compliance (other jurisdictions) | Identify the national instruments that apply, and record what has been verified against the primary text. | [Australia](13_Australia_AI_Compliance/index.md), [Brazil](14_Brazil_AI_Compliance/index.md), [Canada](15_Canada_AI_Compliance/index.md), [China](16_China_AI_Compliance/index.md), [India](17_India_AI_Compliance/index.md), [Japan](18_Japan_AI_Compliance/index.md), [Singapore](19_Singapore_AI_Compliance/index.md), [South Korea](20_South_Korea_AI_Compliance/index.md), [UK](21_UK_AI_Compliance/index.md), [US](22_US_AI_Compliance/index.md) | Regulatory register, region-specific records and templates. |

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
| Vendor Evaluation Team | [AI Security Vendor Evaluation Master Framework](05_Vendor_Evaluation/11_AI_Security_Vendor_Evaluation_Master_Framework.md) | Vendor profiles `12A` to `12H`, [AI Security PoC Test Case Library](06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md), [T03 Vendor Due-Diligence GCC Addendum](11_GCC_AI_Compliance/T03_Vendor_Due_Diligence_GCC_Addendum.md), [T03 Supplier Due-Diligence EU Addendum](12_EU_AI_Compliance/T03_Supplier_Due_Diligence_EU_Addendum.md) | Consistent supplier scoring, risk decision, and evidence retained. |
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
  Vendor master framework, supplier evidence model, proof-of-concept scorecards, and vendor profiles.

06_Testing_and_Assurance/
  PoC tests, adversarial testing, red team methodology, audit checklist, and evidence library.

07_Role_Based_Playbooks/
  Persona-specific guidance for developers, researchers, red teamers, governance, audit, and operations.

08_Governance/
  Operating model, acceptable AI use, approvals, committees, responsibilities, and reporting cadence.

10_Test_Case_Library/
  629 detailed product evaluation test cases across 17 AI lifecycle layers and 6 emerging domains, with reference index,
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
| NIST AI 100-2 (adversarial machine learning) | Shared vocabulary for attack classes and the scope of adversarial testing. |
| OWASP Top 10 for LLM Applications and for Agentic Applications | Application and agent risk categories for developer guidance, threat modeling, and test-case design. |
| MITRE ATLAS | Adversary tactics and techniques against AI-enabled systems for threat-informed testing and incident description. |
| EU AI Act | Legal obligations for in-scope providers and deployers of AI systems. |
| NIST Cybersecurity Framework | Identify, Protect, Detect, Respond, and Recover coverage for AI-enabled systems. |
| CIS Controls | Practical safeguards for inventory, identity, access, endpoint, network, data protection, monitoring, and response. |
| UAE information assurance and cybersecurity expectations | Alignment to local cybersecurity governance, data handling, hosting, resilience, and assurance obligations. |
| UAE data residency and sovereignty requirements | Jurisdictional control over regulated data, hosting location, cross-border processing, vendor access, and evidence. |
| Privacy and data protection obligations | Data minimization, purpose limitation, consent/legal basis, retention, access, and breach response considerations. |

## 13. Key Control Domains

The control library should maintain detailed objectives, implementation guidance, evidence expectations, and test procedures for at least the following domains:

| Domain | Control Intent |
|---|---|
| AI inventory and intake | Maintain a complete register of AI tools, models, agents, data flows, owners, and approval status. |
| Data protection | Prevent sensitive data disclosure through prompts, training, fine-tuning, logs, telemetry, plugins, or vendor access. |
| Identity and access management | Enforce least privilege, strong authentication, role-based access, service identity controls, and privileged action review. |
| Prompt and input security | Detect and reduce prompt injection, jailbreak attempts, malicious instructions, unsafe content, and data exfiltration prompts. |
| Output validation | Manage hallucination, unsafe recommendations, policy violations, misinformation, and unsupported decisions. |
| RAG and knowledge security | Protect indexes, embeddings, retrieval permissions, source grounding, and document-level authorization. |
| Agent and tool governance | Control tool permissions, action approval, execution boundaries, rollback, and transaction logging. |
| Application and API security | Secure AI application interfaces, model gateways, secrets, rate limits, session handling, and error handling. |
| Model and vendor risk | Evaluate model provenance, data usage, contractual protections, operational resilience, and third-party exposure. |
| Monitoring and detection | Capture AI activity logs, anomalous prompts, tool calls, data movement, model misuse, and policy violations. |
| Incident response | Define AI incident categories, escalation paths, investigation evidence, containment, and lessons learned. |
| Audit and assurance | Maintain traceable evidence of control design, operation, testing, exceptions, and remediation. |

## 14. Vendor-Neutral Operating Rule

Do not update vendor profiles as the primary source of truth for controls.

Controls and standards must remain vendor-neutral. Vendor documents should reference the relevant control objectives, evidence requirements, and PoC tests rather than replacing enterprise standards.

Vendor profiles should be used to record:

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
| Review frequency | Controlled pages must be reviewed at least quarterly or after major AI, regulatory, or threat changes. |
| Change control | Significant changes to standards, control objectives, or risk methodology require approval by the appropriate governance authority. |
| Evidence linkage | Control pages should link to expected evidence, test cases, and audit checklist items. |
| Version history | Every controlled page must maintain a version history with date, author, approver, and summary of change. |
| Cross-reference consistency | Document names, control IDs, test IDs, and risk IDs must remain consistent across the wiki. |
| Vendor neutrality | Vendor profiles must map to standards and controls; they must not redefine them. |
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
| Percentage of AI tools registered | Measures visibility and intake coverage. |
| Percentage of AI use cases risk assessed | Measures governance adoption. |
| High-risk AI initiatives with approved treatment plans | Measures risk decision quality. |
| AI vendors assessed before onboarding | Measures supplier governance coverage. |
| AI applications with completed security testing | Measures release readiness. |
| AI systems with monitoring and logging enabled | Measures operational visibility. |
| Open AI control exceptions past expiry | Measures governance discipline. |
| Audit evidence completeness score | Measures assurance readiness. |
| Number of AI security findings remediated | Measures improvement execution. |

These metrics measure coverage. For control-effectiveness metrics such as injection test success rate, privileged-action gating, and time to disable, see [Assurance: Testing, Monitoring and Response](00_Foundations/08-Assurance-Testing-Monitoring-and-Response.md#85-metrics).

## 19. Document Governance

| Item | Value |
|---|---|
| Original author | Nachiket Sathaye |
| Document owner | AI Security Program |
| Custodian | Security Architecture Team |
| Status | Published |
| Review cycle | Quarterly |
| Approval authority | AI Governance Committee |
| Primary users | AI, cybersecurity, GRC, compliance, vendor evaluation, operations, and audit teams |

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
- [Test Case Library (629 cases, 17 layers and 6 emerging domains)](10_Test_Case_Library/index.md)
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

## 23. About the Co-author

<div class="profile-head"><img class="profile-photo" src="assets/ankush-jain.jpg" alt="Ankush Jain" width="88" height="88"><p><strong>Ankush Jain</strong><br><strong>Cybersecurity Governance &amp; Risk Leader | AI Security &amp; Digital Trust Strategist | CISSP, CCSP | Aspiring CISO (MENA/UAE)</strong></p></div>

Governance-focused cybersecurity leader with 19+ years of experience protecting critical infrastructure and global enterprises across MENA and APAC. I specialize in cybersecurity governance, enterprise risk management, AI risk reviews, and digital trust frameworks that enable organizations to embrace transformation securely.

LinkedIn: [linkedin.com/in/ankushjai](https://www.linkedin.com/in/ankushjai/)
