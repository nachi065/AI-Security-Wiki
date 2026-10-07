---
title: "Foundations"
description: "AI security vs. security of AI: a practitioner research paper separating the terms, with a two-axis model, design principle, reference architecture and cited sources."
author: Nachiket Sathaye
nav_order: 2
has_children: true
document_type: Practitioner Research Paper
---

# AI Security vs. Security of AI

**A practitioner research paper on protecting AI systems, securing AI-enabled enterprises, and using AI for defence**

*Revision: October 2026 · Status: living document · Author: Nachiket Sathaye · Licence: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)*

---

## Abstract

"AI security", "security of AI", "secure AI" and "AI for security" are used interchangeably in vendor material, procurement documents and board papers. They describe different problems with different owners, controls and evidence. This paper separates them and gives practitioners a working model for deciding which problem is actually on the table.

The argument has four parts.

1. **Terminology.** *Security of AI* is the protection of AI systems and their lifecycle. *AI for security* is the use of AI in defensive work. *AI security* is the enterprise umbrella that contains both, plus the security consequences of AI-enabled business processes and AI-enabled attackers. ([Page 1](01-Terminology-and-Two-Axis-Model.md))
2. **A two-axis model.** Every AI security question can be placed by *what is being protected* (the object) and *what outcome is required* (the mission). The same technology, such as a coding agent, generates obligations in several cells at once. ([Page 1](01-Terminology-and-Two-Axis-Model.md))
3. **A design principle.** Treat the model as an untrusted component whose output is advisory. Authority to act, access data or spend money must be enforced outside the model by deterministic controls. ([Pages 2, 4, 5, 7](02-AI-System-Boundary-and-Assets.md))
4. **An operating model.** Conventional controls, AI-specific controls and governance controls need to be run as one programme, tied to evidence, and mapped to the standards that auditors and regulators already use. ([Pages 8 to 11](08-Assurance-Testing-Monitoring-and-Response.md))

The paper is a synthesis. It does not report new experiments. Where a claim rests on published research or a standards document it is cited; where it is the author's analysis it is labelled as such.

## How claims are labelled

| Label | Meaning |
|---|---|
| **[Documented]** | Stated in a cited paper, standard or regulation |
| **[Reported]** | Stated in a cited secondary source (vendor, law-firm or community report); verify before relying on it |
| **[Analysis]** | The author's reasoning or recommendation; not independently evidenced |

## Contents

| Page | Topic |
|---|---|
| [1. Terminology and the Two-Axis Model](01-Terminology-and-Two-Axis-Model.md) | Definitions, object × mission matrix, lifecycle |
| [2. The AI System Boundary and Assets](02-AI-System-Boundary-and-Assets.md) | Components, trust boundaries, what must be protected |
| [3. Threat Taxonomy](03-Threat-Taxonomy.md) | Training-time, inference-time, model-level and ecosystem threats |
| [4. LLMs, Prompt Injection and RAG](04-LLMs-Prompt-Injection-and-RAG.md) | Instruction/data confusion, retrieval trust |
| [5. Agents, Identity and Excessive Agency](05-Agents-Identity-and-Excessive-Agency.md) | Tool use, delegation, approval gates |
| [6. Supply Chain and Infrastructure](06-Supply-Chain-and-Infrastructure.md) | Models, datasets, packages, GPUs, cloud |
| [7. Reference Architecture](07-Reference-Architecture.md) | Layers, policy enforcement, zero trust |
| [8. Assurance: Testing, Monitoring and Response](08-Assurance-Testing-Monitoring-and-Response.md) | Threat modelling, red teaming, telemetry, incident response, metrics |
| [9. Governance, Standards and Regulation](09-Governance-Standards-and-Regulation.md) | NIST, ISO, OWASP, MITRE, SAIF, ENISA, EU AI Act |
| [10. AI for Security and AI-Enabled Threats](10-AI-for-Security-and-AI-Enabled-Threats.md) | Defensive use and offensive use |
| [11. Maturity Model and Roadmap](11-Maturity-Model-and-Roadmap.md) | Five levels, 30-day to 24-month plan |
| [12. Illustrative Scenarios](12-Illustrative-Scenarios.md) | Four worked, hypothetical scenarios |
| [13. Limitations and Research Gaps](13-Limitations-and-Research-Gaps.md) | What this paper cannot claim; open problems |
| [Appendices](Appendices.md) | Questionnaire, worksheets, test procedures, glossary |
| [References](References.md) | Verified sources |

## How this paper relates to the rest of the wiki

The paper explains the concepts and the sources. The other sections of the wiki turn them into standards, templates and test cases.

| Paper page | Where the wiki puts it into practice |
|---|---|
| 3. Threat Taxonomy | [Enterprise AI Risk Register](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [Model Layer test cases](../10_Test_Case_Library/L12-model-layer.md), [Training and Fine-Tuning test cases](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md) |
| 4. LLMs, Prompt Injection and RAG | [Custom AI Application Runtime Security Standard](../04_Domain_Standards/08_Custom_AI_Application_Runtime_Security_Standard.md), [Prompt and Context test cases](../10_Test_Case_Library/L07-prompt-and-context-layer.md), [Knowledge and Retrieval test cases](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md) |
| 5. Agents, Identity and Excessive Agency | [Agentic AI Security and Tool Governance](../04_Domain_Standards/09_Agentic_AI_Security_and_Tool_Governance.md), [Agent Orchestration test cases](../10_Test_Case_Library/L06-agent-orchestration-layer.md), [Agent and Non-Human Identity Governance test cases](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md) |
| 6. Supply Chain and Infrastructure | [Supply Chain and Third Party test cases](../10_Test_Case_Library/L16-supply-chain-and-third-party.md), [Infrastructure test cases](../10_Test_Case_Library/L15-infrastructure-layer.md), [Vendor Evaluation Master Framework](../05_Vendor_Evaluation/11_AI_Security_Vendor_Evaluation_Master_Framework.md) |
| 7. Reference Architecture | [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md) |
| 8. Assurance: Testing, Monitoring and Response | [AI Red Team Playbook](../06_Testing_and_Assurance/15C_AI_Red_Team_Playbook.md), [AI Security Audit and Evidence Checklist](../06_Testing_and_Assurance/14_AI_Security_Audit_and_Evidence_Checklist.md), [Monitoring, Detection and Response test cases](../10_Test_Case_Library/L17-monitoring-detection-and-response.md), [AI Incident Response and Forensics test cases](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md) |
| 9. Governance, Standards and Regulation | [AI Governance Operating Model](../08_Governance/16_AI_Governance_Operating_Model.md), [Sovereign AI, UAE Compliance and Data Residency Requirements](../04_Domain_Standards/10_Sovereign_AI_UAE_Compliance_and_Data_Residency.md), [GCC AI Regulatory Hub](../11_GCC_AI_Compliance/01_GCC_AI_Regulatory_Hub.md), [EU AI Regulatory Hub](../12_EU_AI_Compliance/01_EU_AI_Regulatory_Hub.md) |
| 11. Maturity Model and Roadmap | [AI Security Maturity Model](../01_Strategy_and_Market/01_AI_Security_Market_and_Technology_Landscape_Expanded.md#8-ai-security-maturity-model) |
| Appendices | [AI Risk Review Template](../02_Risk_Management/02E_AI_Risk_Review_Template.md), [AI Security Glossary and Taxonomy](../09_Reference/18_AI_Security_Glossary_and_Taxonomy.md) |

## Suggested citation

> Sathaye, N. *AI Security vs. Security of AI: A Practitioner Research Paper.* AI Security Wiki, living document, revision October 2026. https://nachi065.github.io/AI-Security-Wiki/00_Foundations/

## Important notice

This is practitioner research, not legal advice, certification guidance or a vendor assessment. Standards and regulations change; confirm the current text and applicability of each instrument before relying on it. AI security is an empirical field, and attack feasibility and mitigation effectiveness change quickly.
