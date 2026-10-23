---
title: "ISO/IEC AI Standards Crosswalk"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Framework Crosswalks"
nav_order: 15
description: "Nine ISO/IEC AI standards beyond ISO/IEC 42001 (38507, 42005, 42006, 23894, TR 24028, 5338, 23053, 22989 and the 5259 series) mapped clause by clause to this wiki's pages and controls."
document_type: AI Security Wiki Reference
version: 1.0
last_reviewed: 2026-10-15
---

# ISO/IEC AI Standards Crosswalk

> **Purpose:** Show where the wiki puts into practice the ISO/IEC AI standards that sit around ISO/IEC 42001: board governance, impact assessment, certification, risk management, trustworthiness, lifecycle, ML system structure, terminology and data quality.

> **Audience:** AI management system owners, GRC teams, internal auditors, data owners, architects.

> **Using the two together:** Use the standards for the requirements and guidance. Use this wiki for the control objectives, templates, evidence and tests that implement them. The [ISO/IEC 42001 Crosswalk](05_ISO_IEC_42001_Crosswalk.md) covers the management system standard itself.

## How this page was checked

> **Verify before use.** ISO and IEC standards are sold by their publishers and their text is copyrighted. This page cites edition, clause numbers and clause headings only. They were checked on 15 October 2026 against the publishers' own product pages and against the contents pages in the free previews that standards stores publish. **No clause text was read**, so each mapping below is this wiki's judgment from the clause heading. Check each clause against your own copy before you rely on the mapping.

| Standard | Title | Edition | Publisher page |
|---|---|---|---|
| ISO/IEC 38507:2022 | Governance implications of the use of artificial intelligence by organizations | Ed. 1, April 2022 | [iso.org/standard/56641](https://www.iso.org/standard/56641.html) |
| ISO/IEC 42005:2025 | AI system impact assessment | Ed. 1, May 2025 | [iso.org/standard/44545](https://www.iso.org/standard/44545.html) |
| ISO/IEC 42006:2025 | Requirements for bodies providing audit and certification of AI management systems | Ed. 1, July 2025 | [iso.org/standard/44546](https://www.iso.org/standard/44546.html) |
| ISO/IEC 23894:2023 | Guidance on risk management | 2023 | Contents checked in a store preview; [NIST crosswalk to the AI RMF](https://airc.nist.gov/documents/3/ai-2025-00109_revised_ISO_IEC_23894_Crosswalk_to_the_NIST_AI_RMF.pdf) |
| ISO/IEC TR 24028:2020 | Overview of trustworthiness in artificial intelligence | 2020 (Technical Report) | [iso.org/standard/77608](https://www.iso.org/standard/77608.html) |
| ISO/IEC 5338:2023 | AI system life cycle processes | 2023 | [iso.org/standard/81118](https://www.iso.org/standard/81118.html) |
| ISO/IEC 23053:2022 | Framework for AI systems using machine learning | 2022 | [iso.org/standard/74438](https://www.iso.org/standard/74438.html) |
| ISO/IEC 22989:2022 | AI concepts and terminology | 2022 | [iso.org/standard/74296](https://www.iso.org/standard/74296.html) |
| ISO/IEC 5259-1 to 5259-5 | Data quality for analytics and machine learning | Parts 1 to 4: 2024; Part 5: 2025 | [ISO bundle page](https://committee.iso.org/publication/PUB200525.html) |

## ISO/IEC 38507: governance by the board

Guidance for members of the governing body on enabling and governing the use of AI.

| Clause | Heading | Where the wiki covers it |
|---|---|---|
| 4.2, 4.3 | Maintaining governance and accountability when introducing AI | Governing body and accountable executive rows in the [AI Governance Operating Model](../08_Governance/16_AI_Governance_Operating_Model.md) |
| 6.2 | Governance oversight of AI | Board-Level Reporting in the [AI Governance Operating Model](../08_Governance/16_AI_Governance_Operating_Model.md); [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) |
| 6.3 | Governance of decision-making | Decisions Reserved for the Governing Body; [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045) |
| 6.4 | Governance of data use | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029) |
| 6.5 | Culture and values | [AI Policy, Standards and Acceptable Use](../08_Governance/17_AI_Policy_Standards_and_Acceptable_Use.md); [AI-CTRL-044](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-044) |
| 6.6 | Compliance | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-043](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-043) |
| 6.7 | Risk (appetite, management, objectives, sources, controls) | Risk Appetite and Criteria in the [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md); [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) |

## ISO/IEC 42005: AI system impact assessment

Guidance on an impact assessment process (clause 5) and on what to document (clause 6). Annexes A and B give guidance for use with ISO/IEC 42001 and ISO/IEC 23894, and Annex E gives an example template.

| Clause | Heading | Where the wiki covers it |
|---|---|---|
| 5.4, 5.12 | Timing; monitoring and review | Review Triggers in the [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md); [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042) |
| 5.7 | Thresholds for sensitive uses, restricted uses and impact scales | "When to run a full impact assessment" in the [AI Use-Case Risk Triage](../02_Risk_Management/02F_AI_Use_Case_Risk_Triage.md) |
| 5.11 | Approval process | [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042) (approvals dated before go-live) |
| 6.3 | AI system information, including intended and unintended uses | [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042), [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) |
| 6.4 | Data information and quality | [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029), [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042) |
| 6.6 | Deployment environment (geography, languages, constraints) | [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007) |
| 6.7 | Relevant interested parties | [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) |
| 6.8 | Actual and reasonably foreseeable impacts, including failures and misuse | [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042); [EU T02 Impact Assessment](../12_EU_AI_Compliance/T02_Impact_Assessment_FRIA_DPIA.md); [GCC T02 AI Impact Assessment](../11_GCC_AI_Compliance/T02_AI_Impact_Assessment.md) |
| 6.9 | Measures to address harms and benefits | [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042); [AI Risk Treatment Plan](../02_Risk_Management/02C_AI_Risk_Treatment_Plan.md) |

**Gap:** the wiki's impact assessment templates focus on harms. Clause 6.8.2 asks for benefits as well as harms; record the expected benefit in the use-case registry ([AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011)) until the templates are revised.

## ISO/IEC 42006: certification of AI management systems

Requirements for bodies that audit and certify against ISO/IEC 42001, in addition to ISO/IEC 17021-1. It binds certification bodies, not the organization being certified, but it shows what an AI management system audit will look for. See "Preparing for ISO/IEC 42001 Certification" in the [AI Security Audit and Evidence Checklist](../06_Testing_and_Assurance/14_AI_Security_Audit_and_Evidence_Checklist.md).

| Clause | Heading | Where the wiki covers it |
|---|---|---|
| 7.1.3 | Specific technical competence requirements | Evidence by control in the [AI Security Audit and Evidence Checklist](../06_Testing_and_Assurance/14_AI_Security_Audit_and_Evidence_Checklist.md) |
| 8.4.2 | Access to the documentation of the organization | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) |
| 9.1.3 | Scope of certification | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011); vendor certificate scope in the [Vendor Evaluation Master Framework](../05_Vendor_Evaluation/11_AI_Security_Vendor_Evaluation_Master_Framework.md) |
| 9.1.4 and Annex A | Determining audit time | Registry counts by tier ([AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011)); vendor AI list ([AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014)) |
| 9.6 | Maintaining certification | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) |

## ISO/IEC 23894: AI risk management

Guidance on AI risk management that follows the ISO 31000 framework (clause 5) and process (clause 6). The wiki's process mapping is in "Alignment with ISO/IEC 23894" in the [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md).

| Clause | Heading | Where the wiki covers it |
|---|---|---|
| 5.2 to 5.4 | Leadership, integration and design of the framework | [AI Governance Operating Model](../08_Governance/16_AI_Governance_Operating_Model.md); [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) |
| 6.2 to 6.7 | Risk management process | [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md) and the Risk Management section |
| Annex B | Risk sources | [Enterprise AI Risk Register](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md); [Threat Taxonomy](../00_Foundations/03-Threat-Taxonomy.md) |
| Annex C | Risk management and the AI system life cycle | [Risk, Control and Test Traceability](../02_Risk_Management/02G_Risk_Control_Test_Traceability.md) |

## ISO/IEC TR 24028: trustworthiness

A 2020 Technical Report that surveys threats to trustworthiness and mitigations. It predates generative AI, so use it for concepts rather than for current LLM threats.

| Clause | Heading | Where the wiki covers it |
|---|---|---|
| 8.2 | AI-specific security threats (data poisoning, adversarial attacks, model stealing, hardware threats) | [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034), [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-032](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-032); [Threat Taxonomy](../00_Foundations/03-Threat-Taxonomy.md) |
| 8.3 | AI-specific privacy threats | [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) |
| 8.4 to 8.6 | Bias, unpredictability, opaqueness | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) |
| 9.2, 9.3 | Transparency; explainability (ex-ante and ex-post, levels, evaluation) | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) |
| 9.4 | Controllability, including human-in-the-loop control points | [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) |
| 9.10 | Testing and evaluation | [AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) |
| 9.11.3 | Product labelling | [EU T06 Transparency Notice](../12_EU_AI_Compliance/T06_Transparency_Notice.md) |

## ISO/IEC 5338: AI system life cycle processes

Adapts the ISO/IEC/IEEE 15288 system life cycle processes to AI, and adds AI-specific technical processes.

| Clause | Heading | Where the wiki covers it |
|---|---|---|
| 6.1.1, 6.1.2 | Acquisition and supply processes | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014); [Vendor Evaluation](../05_Vendor_Evaluation/index.md) |
| 6.3.4, 6.3.5 | Risk management; configuration management | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) |
| 6.4.7 | Knowledge acquisition process | [AI-CTRL-019](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-019) |
| 6.4.8 | AI data engineering process | [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) |
| 6.4.11, 6.4.13 | Verification and validation processes | [AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) |
| 6.4.14 | Continuous validation process | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) |
| 6.4.15, 6.4.16 | Operation and maintenance processes | [AI-CTRL-009](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009), [AI-CTRL-040](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-040) |
| 6.4.17 | Disposal process | **Partial.** No control is dedicated to retiring an AI system. [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) records status and [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030) covers the model registry. |

## ISO/IEC 23053: ML system framework

Describes the components of an ML system and the ML pipeline. It predates LLM and agent architectures; the wiki's [Reference Architecture](../00_Foundations/07-Reference-Architecture.md) extends it.

| Clause | Heading | Where the wiki covers it |
|---|---|---|
| 6.3 to 6.5 | Model, data and tools | [AI System Boundary and Assets](../00_Foundations/02-AI-System-Boundary-and-Assets.md) |
| 8.2, 8.3 | Data acquisition and preparation | [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017); [L10 Data Layer](../10_Test_Case_Library/L10-data-layer.md) |
| 8.4, 8.5 | Modelling; verification and validation | [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034); [L13](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md) |
| 8.6, 8.7 | Model deployment and operation | [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030), [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005); [L14](../10_Test_Case_Library/L14-mlops-llmops-layer.md) |

## ISO/IEC 22989: concepts and terminology

| Clause | Heading | Where the wiki covers it |
|---|---|---|
| 3 | Terms and definitions | [AI Security Glossary and Taxonomy](../09_Reference/18_AI_Security_Glossary_and_Taxonomy.md) |
| 5.15 | Trustworthiness (robustness, reliability, resilience, controllability, explainability, predictability, transparency, bias and fairness) | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034), [AI-CTRL-040](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-040), [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) |
| 5.19 | AI stakeholder roles (provider, producer, customer, partner, subject, relevant authorities) | [Terminology and the Two-Axis Model](../00_Foundations/01-Terminology-and-Two-Axis-Model.md); "Standard Vocabulary" in the [glossary](../09_Reference/18_AI_Security_Glossary_and_Taxonomy.md#standard-vocabulary) |
| 6.2 | AI system life cycle stages (inception to retirement) | Home page section 6 lifecycle |

## ISO/IEC 5259: data quality for analytics and ML

| Part and clause | Heading | Where the wiki covers it |
|---|---|---|
| 5259-1, 5.3 | Data life cycle for analytics and ML | [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) |
| 5259-2, 6 | Data quality characteristics (24, from accuracy and completeness to balance, representativeness and timeliness) | Data quality profile in [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029); corpus quality in [AI-CTRL-019](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-019); [TC-L10-031](../10_Test_Case_Library/L10-data-layer.md#tc-l10-031), [TC-L10-032](../10_Test_Case_Library/L10-data-layer.md#tc-l10-032) |
| 5259-2, 8 | Data quality reporting | Board-Level Reporting in the [AI Governance Operating Model](../08_Governance/16_AI_Governance_Operating_Model.md) |
| 5259-3, 9 | Management of data quality in supply chains | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) |
| 5259-3, 12.8 | Data quality justification | [TC-L10-033](../10_Test_Case_Library/L10-data-layer.md#tc-l10-033) |
| 5259-4, 8 | Data labelling methods and process | [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029) (labelling quality as part of the profile) |
| 5259-5, 7 and 8 | Responsibilities of the governing body and of management | Data Owner row in the [AI Governance Operating Model](../08_Governance/16_AI_Governance_Operating_Model.md) |

## Attribution

ISO/IEC standards are published by the International Organization for Standardization and the International Electrotechnical Commission. This page cites standard numbers, clause numbers and headings only, and does not reproduce their text.

## Related pages

- [ISO/IEC 42001 Crosswalk](05_ISO_IEC_42001_Crosswalk.md)
- [AI Governance Operating Model](../08_Governance/16_AI_Governance_Operating_Model.md)
- [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md)
- [Governance, Standards and Regulation](../00_Foundations/09-Governance-Standards-and-Regulation.md)
