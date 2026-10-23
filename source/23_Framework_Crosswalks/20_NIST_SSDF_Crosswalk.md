---
title: "NIST SSDF and SP 800-218A Crosswalk"
author: Nachiket Sathaye
parent: "Framework Crosswalks"
nav_order: 20
description: "The practices of the NIST Secure Software Development Framework (SP 800-218, version 1.1) and its generative AI community profile (SP 800-218A) mapped to this wiki's controls, standards, Builder Track code and test cases."
document_type: AI Security Wiki Reference
version: 1.0
last_reviewed: 2026-10-23
---

# NIST SSDF and SP 800-218A Crosswalk

> **Purpose:** Let a team that organises secure development around the NIST Secure Software Development Framework (SSDF) find the wiki controls, standards, code and tests that apply each SSDF practice to AI systems and to code written with AI assistants and coding agents.

> **Audience:** Application security, DevSecOps, platform engineering, AI model and AI system producers, software acquirers, GRC.

> **Using the two together:** Use the SSDF for the practices and tasks of a secure development lifecycle, and SP 800-218A for what those practices add for generative AI models and the systems built on them. Use this wiki for the controls, evidence, working code and test cases that show each practice is in place.

## About the framework and this page

**NIST SP 800-218, Secure Software Development Framework (SSDF) Version 1.1: Recommendations for Mitigating the Risk of Software Vulnerabilities**, was published in February 2022. It groups its practices into four groups: Prepare the Organization (PO), Protect the Software (PS), Produce Well-Secured Software (PW) and Respond to Vulnerabilities (RV). Each practice has tasks, numbered for example PS.1.1.

**NIST SP 800-218A, Secure Software Development Practices for Generative AI and Dual-Use Foundation Models: An SSDF Community Profile**, was published in July 2024. It names three audiences: AI model producers, AI system producers (organisations building software that uses a generative AI or dual-use foundation model) and AI system acquirers. It adds recommendations to the SSDF tasks, modifies some practices, and adds practices that are not part of SSDF 1.1. NIST states that the profile should not be used without SP 800-218.

Two numbering points matter when citing:

- In SSDF 1.1, the former practice PW.3 was moved: its first task became PO.1.3, which the text marks "Formerly PW.3.1".
- SP 800-218A reuses the number **PW.3** for a new practice, "Confirm the Integrity of Training, Testing, Fine-Tuning, and Aligning Data Before Use", and adds task **PO.5.3** on continuously monitoring software execution performance and behaviour in development environments. Both are marked in the profile as not part of SSDF 1.1.

> **Verify before use.** The publication titles, dates and audiences, the four groups, the titles of PO.1 to PO.5 and PS.1, the new PW.3 practice and task PO.5.3, and the PW.3 renumbering above were read from the NIST publication pages and PDFs on 23 October 2026 [Verified]. The other practice titles below were read from a partial read of the PDFs and checked against memory [Reported]; check them against SP 800-218 before quoting them. On 23 October 2026 the NIST SSDF project page treated SP 800-218 version 1.1 as current and listed no revision; check for a newer version before citing. The mapping is this wiki's own judgement and has not been reviewed by NIST.

**Match** is **Direct** when the wiki has a control, evidence and tests for the practice as it applies to AI, and **Partial** when it covers only part, as the last column explains.

## SSDF practices to wiki controls

### Prepare the Organization (PO)

| Practice | Title | Main wiki controls | Wiki pages and code | Match | Notes |
|---|---|---|---|---|---|
| PO.1 | Define Security Requirements for Software Development | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033) | [AI Policy Standards and Acceptable Use](../08_Governance/17_AI_Policy_Standards_and_Acceptable_Use.md), [Domain Standards](../04_Domain_Standards/index.md) | Direct | SP 800-218A marks PO.1 as modified for AI. The domain standards are the AI security requirements a development team works to. |
| PO.2 | Implement Roles and Responsibilities | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-044](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-044) | [AI Governance Operating Model](../08_Governance/16_AI_Governance_Operating_Model.md), [AI Product Developer Playbook](../07_Role_Based_Playbooks/15A_AI_Product_Developer_Playbook.md) | Direct | Role-based training is in the governance operating model. |
| PO.3 | Implement Supporting Toolchains | [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004), [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030) | [AI Coding Assistant and Coding Agent Security Standard](../04_Domain_Standards/07_IDE_AI_Coding_Assistant_Security_Standard.md), [Developer Pipeline Checks](../24_Builder_Track/04_Developer_Pipeline_Checks.md) | Direct | AI coding assistants and coding agents are now part of the toolchain. The standard governs them; the Builder Track page runs the same checks in the agent, before commit and in CI. |
| PO.4 | Define and Use Criteria for Software Security Checks | [AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) | [CI/CD release stages](../08_Governance/18_AI_Operating_Defaults.md#cicd-release-stages-for-ai-applications), [pipeline gates](../04_Domain_Standards/07_IDE_AI_Coding_Assistant_Security_Standard.md#pipeline-gates-for-ai-assisted-code) | Direct | The two tables say which checks run at each stage and which ones block. |
| PO.5 | Implement and Maintain Secure Environments for Software Development | [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030), [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027), [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016), [AI-CTRL-009](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009) | [ML pipeline tests](../10_Test_Case_Library/L14-mlops-llmops-layer.md), [coding agent guardrails](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-036) | Direct | SP 800-218A adds PO.5.3, monitoring development environments for suspicious activity. AI-CTRL-009 and the L14 audit trail case ([TC-L14-019](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-019)) cover it for pipelines; coding agents on developer machines are covered by [TC-L06-036](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-036) and [TC-L09-026](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-026). |

### Protect the Software (PS)

| Practice | Title | Main wiki controls | Wiki pages and code | Match | Notes |
|---|---|---|---|---|---|
| PS.1 | Protect All Forms of Code and Data from Unauthorized Access and Tampering | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030) | [Model layer tests](../10_Test_Case_Library/L12-model-layer.md), [Prompts and configuration as code](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-005) | Direct | SP 800-218A extends secure code storage to AI models, model weights, pipelines and reward models. AI-CTRL-028 protects weights; AI-CTRL-030 protects pipelines and the registry. |
| PS.2 | Provide a Mechanism for Verifying Software Release Integrity | [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) | [CI/CD release stages](../08_Governance/18_AI_Operating_Defaults.md#cicd-release-stages-for-ai-applications) (signing and signature verification) | Direct | Signing of models, containers and prompt bundles, verified at deployment. |
| PS.3 | Archive and Protect Each Software Release | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) | [AI-assisted commit identification](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-021), [Developer Pipeline Checks](../24_Builder_Track/04_Developer_Pipeline_Checks.md) | Partial | The AI-BOM records model and dataset provenance, and the AI-Assistance trailer records which changes an assistant or agent made. The wiki has no guidance on archiving releases themselves; that is general SSDF practice. |

### Produce Well-Secured Software (PW)

| Practice | Title | Main wiki controls | Wiki pages and code | Match | Notes |
|---|---|---|---|---|---|
| PW.1 | Design Software to Meet Security Requirements and Mitigate Security Risks | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033) | [Reference Architecture](../00_Foundations/07-Reference-Architecture.md), [Agent Architecture Patterns](../24_Builder_Track/02_Agent_Architecture_Patterns.md) | Direct | Risk assessment and design patterns that contain prompt injection and excessive agency. |
| PW.2 | Review the Software Design to Verify Compliance with Security Requirements and Risk Information | [AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033) | [Architect's review checklist](../24_Builder_Track/02_Agent_Architecture_Patterns.md) | Direct | The release gate requires a security review record. |
| PW.3 | Confirm the Integrity of Training, Testing, Fine-Tuning, and Aligning Data Before Use (SP 800-218A only) | [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029), [AI-CTRL-019](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-019) | [Training and fine-tuning tests](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md), [Predictive Model Monitoring and Adversarial ML](../04_Domain_Standards/11_Predictive_Model_Monitoring_and_Adversarial_ML.md) | Direct | Applies to model producers and to teams that fine-tune. Poisoning, provenance and personal data in training data are tested in L13. |
| PW.4 | Reuse Existing, Well-Secured Software When Feasible Instead of Duplicating Functionality | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | [Supply chain tests](../10_Test_Case_Library/L16-supply-chain-and-third-party.md), [dependency verification](../04_Domain_Standards/07_IDE_AI_Coding_Assistant_Security_Standard.md#control-requirements) | Direct | Includes verifying that a package an assistant suggests exists and is not typosquatted ([TC-L05-019](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-019), [TC-L16-004](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-004)). |
| PW.5 | Create Source Code by Adhering to Secure Coding Practices | [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004), [AI-CTRL-020](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-020) | [AI Coding Assistant and Coding Agent Security Standard](../04_Domain_Standards/07_IDE_AI_Coding_Assistant_Security_Standard.md), [Secure Your First Agent](../24_Builder_Track/01_Secure_Your_First_Agent.md) | Direct | Generated code is held to the same secure coding rules; LLM output is handled as untrusted input. |
| PW.6 | Configure the Compilation, Interpreter, and Build Processes to Improve Executable Security | [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030) | [Pipeline runner least privilege](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-008) | Partial | The wiki covers pipeline and runner security, not compiler and build hardening, which is the same for AI software as for any other. |
| PW.7 | Review and/or Analyze Human-Readable Code to Identify Vulnerabilities and Verify Compliance with Security Requirements | [AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) | [Insecure code suggestion detection](../10_Test_Case_Library/L05-ai-applications.md#tc-l05-034), [Developer Pipeline Checks](../24_Builder_Track/04_Developer_Pipeline_Checks.md) | Direct | SP 800-218A extends review to scanning models for malicious content; the release stages table includes a model file scan. |
| PW.8 | Test Executable Code to Identify Vulnerabilities and Verify Compliance with Security Requirements | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) | [Test Case Library](../10_Test_Case_Library/index.md), [payload kit](../10_Test_Case_Library/payload-kit.md), [AI Red Team Playbook](../06_Testing_and_Assurance/15C_AI_Red_Team_Playbook.md) | Direct | The {{n:tests}} test cases are the AI-specific testing; each shows its validation level. |
| PW.9 | Configure Software to Have Secure Settings by Default | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-032](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-032) | [Custom AI Application Runtime Security Standard](../04_Domain_Standards/08_Custom_AI_Application_Runtime_Security_Standard.md) | Partial | Runtime and infrastructure defaults are covered; the wiki has no secure-defaults checklist for AI products shipped to customers. |

### Respond to Vulnerabilities (RV)

| Practice | Title | Main wiki controls | Wiki pages and code | Match | Notes |
|---|---|---|---|---|---|
| RV.1 | Identify and Confirm Vulnerabilities on an Ongoing Basis | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034), [AI-CTRL-009](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009) | [Monitoring, detection and response tests](../10_Test_Case_Library/L17-monitoring-detection-and-response.md) | Direct | Scheduled re-runs of the evaluation and adversarial suites, and provider model change monitoring ([TC-L16-013](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-013)). |
| RV.2 | Assess, Prioritize, and Remediate Vulnerabilities | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md), [operating defaults](../08_Governance/18_AI_Operating_Defaults.md) | Direct | Severity, response times and exception limits are in the operating defaults. |
| RV.3 | Analyze Vulnerabilities to Identify Their Root Causes | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [Post-incident feedback](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-023), [AI Security Incident Casebook](../09_Reference/20_AI_Security_Incident_Casebook.md) | Direct | Model behaviour regressions and poisoning have their own forensic cases in the incident domain. |

Of the 20 practices in this table, 17 are a direct match and 3 are partial.

## Where the wiki stops

The SSDF is about the whole development lifecycle of any software. This wiki adds what changes when the software is an AI system or is written with AI help. It does not repeat general practice that is the same for every product: compiler and build hardening, release archiving and secure default settings for shipped products. Use the SSDF itself for those.

SP 800-218A adds many recommendations to individual SSDF tasks. This page maps at practice level only. For a statement against SP 800-218A, map at task level from the profile itself.

## Attribution

NIST SP 800-218 and SP 800-218A are publications of the US National Institute of Standards and Technology. This page cites practice identifiers and titles only. Read the publications on the [SP 800-218 page](https://csrc.nist.gov/pubs/sp/800/218/final) and the [SP 800-218A page](https://csrc.nist.gov/pubs/sp/800/218/a/final), both read on 23 October 2026.

## Related pages

- [AI Coding Assistant and Coding Agent Security Standard](../04_Domain_Standards/07_IDE_AI_Coding_Assistant_Security_Standard.md)
- [Developer Pipeline Checks](../24_Builder_Track/04_Developer_Pipeline_Checks.md)
- [ISO/IEC 27001 Crosswalk](08_ISO_IEC_27001_Crosswalk.md)
- [NIST AI RMF Crosswalk](03_NIST_AI_RMF_Crosswalk.md)
- [Illustrative Operating Defaults](../08_Governance/18_AI_Operating_Defaults.md)
