---
title: "AI Risk Map Crosswalk"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Framework Crosswalks"
nav_order: 18
description: "The 55 categories of the AI Risk Map (RiskFramework.org, v1.3) mapped to this wiki's risk register, with the categories the wiki covers only in part."
document_type: AI Security Wiki Reference
version: 1.2
last_reviewed: 2026-10-29
---

# AI Risk Map Crosswalk

> **Purpose:** Let a team that uses the AI Risk Map to identify AI risks find the matching risks in this wiki's register, and through them the controls, evidence and test cases.

> **Audience:** Risk, security, legal and business teams; GRC and audit; AI governance leads.

> **Using the two together:** Use the map to widen the view of where AI risk can come from and who owns it. Use this wiki to rate the risks that apply and to treat them with controls, evidence and tests.

## About the map and this page

The *AI Risk Map* v1.3 (2026) by Evan Wheeler (GitHub [wheels344i-gte](https://github.com/wheels344i-gte)), published at RiskFramework.org and in the GitHub repository [wheels344i-gte/ai-risk-map](https://github.com/wheels344i-gte/ai-risk-map), is a one-page thought-starter for identifying the risks of an organization's adoption of AI before a formal assessment. It lists 196 risk factors in 55 categories and 12 domains, and groups them by who owns the risk rather than by how the technology works. Some factors are marked as split pairs, where another domain owns the other side. The map names its sources (among them the NIST AI RMF, the EU AI Act, ISO/IEC 42001, the OWASP lists and MITRE ATLAS) and says a companion workbook gives the source of each factor.

The domain and category names below were read from the map itself, a PDF supplied to this wiki on 17 October 2026. On 29 October 2026 the map's website (https://riskframework.org/ai-risk-map/) was read and still showed version 1.3 with the same counts. The website also offers a taxonomy workbook (with the source of each factor and the author's scope decisions), a flat CSV with stable factor IDs (AIRM-nnn) and a Markdown version for AI assistants. These files have not yet been compared with this page, so the mapping is still by category, not by factor ID. The mapping to wiki risks is this wiki's own judgment and has not been reviewed by the map's author. The map's author takes proposed changes to the map as [issues on its GitHub repository](https://github.com/wheels344i-gte/ai-risk-map/issues), not pull requests.

**Match** shows how closely the wiki covers the category: **Direct** (one or more register risks cover it), **Partial** (the wiki covers part of it, as the last column explains) or **None**. A category is mapped as a whole; individual risk factors are not.

## Map categories to wiki risks

| Map domain | Category | Wiki risks | Match | What the match leaves out |
|---|---|---|---|---|
| 01 AI Governance and Accountability | Governance and oversight | [AI-R02](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R18](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Partial | Shadow AI and use beyond approved purpose are register risks. Board oversight and the governance body are covered by the [AI Governance Operating Model](../08_Governance/16_AI_Governance_Operating_Model.md), not as risks. |
| 01 AI Governance and Accountability | Roles and accountability | [AI-R28](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Partial | Named accountable owners are required in AI-R28 and the operating model. Segregation of duties was considered and not added as a separate risk; see [Considered and Not Added](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md#considered-and-not-added). |
| 01 AI Governance and Accountability | Policy and standards | [AI-R02](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Partial | Covered by [AI Policy, Standards and Acceptable Use](../08_Governance/17_AI_Policy_Standards_and_Acceptable_Use.md) and AI-CTRL-012 rather than as register risks. |
| 01 AI Governance and Accountability | Risk-management integration | None | Partial | Covered by the [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md) (risk appetite) and impact assessment under AI-CTRL-042, not as a register risk. |
| 01 AI Governance and Accountability | Audit and assurance | [AI-R09](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R40](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Partial | Auditability and AI in financial reporting controls are register risks; independent assurance is AI-CTRL-038. Internal audit competence has no separate risk. |
| 02 Strategy and Value Realization | Competitive position | [AI-R29](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 02 Strategy and Value Realization | AI strategy and roadmap | [AI-R29](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 02 Strategy and Value Realization | Use-case selection and sourcing | [AI-R29](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R18](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Partial | The choice between training, fine-tuning, retrieval and an API has no separate risk. |
| 02 Strategy and Value Realization | Value measurement / ROI | [AI-R29](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R30](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 03 Data and Privacy | Sourcing and provenance | [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R27](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Partial | Training data provenance is under AI-CTRL-029. Data lineage through the pipeline has no separate risk. |
| 03 Data and Privacy | Quality and labeling | [AI-R17](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 03 Data and Privacy | Privacy and consent | [AI-R03](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R06](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R10](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R28](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R49](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 03 Data and Privacy | Training-data rights and IP | [AI-R27](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R36](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 03 Data and Privacy | Retention and disposal | [AI-R38](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R21](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R49](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 04 Model Development and Performance | Design and training | [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Partial | Pipeline and registry security is AI-CTRL-030. Choosing an unsuitable model for the problem has no separate risk. |
| 04 Model Development and Performance | Accuracy and validation | [AI-R12](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R39](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 04 Model Development and Performance | Robustness and drift | [AI-R17](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R16](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 04 Model Development and Performance | Explainability | [AI-R15](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 04 Model Development and Performance | Reproducibility and documentation | [AI-R15](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R09](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R50](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 05 Security and Adversarial Threats | Data and pipeline attacks | [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R05](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct | Poisoning is treated by AI-CTRL-029 and tampering with retrieval sources by AI-CTRL-019. |
| 05 Security and Adversarial Threats | Model attacks | [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R47](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 05 Security and Adversarial Threats | Inference-time (input) attacks | [AI-R05](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R26](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 05 Security and Adversarial Threats | Output and integration security | [AI-R06](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R24](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 05 Security and Adversarial Threats | Supply-chain and artifact integrity | [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R23](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R43](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 05 Security and Adversarial Threats | AI access and identity | [AI-R22](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R46](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R06](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 06 Safety, Ethics and Responsible AI | Bias and fairness | [AI-R14](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R32](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 06 Safety, Ethics and Responsible AI | Harmful / inaccurate output | [AI-R12](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R20](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 06 Safety, Ethics and Responsible AI | Transparency, disclosure and provenance | [AI-R42](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R16](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R53](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Partial | Disclosure that a user is talking to AI is part of AI-R42 and labelling of generated content is AI-R53. Telling customers when your AI service changes has no separate risk. |
| 06 Safety, Ethics and Responsible AI | Misuse and dual-use | [AI-R12](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Partial | Treated as one kind of harmful output, as in the [NIST AI 600-1 Crosswalk](04_NIST_AI_600_1_GenAI_Profile_Crosswalk.md). |
| 06 Safety, Ethics and Responsible AI | Human agency and over-reliance | [AI-R19](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R42](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 07 Operations and Resilience | MLOps and deployment | [AI-R02](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R16](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R50](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 07 Operations and Resilience | Monitoring and observability | [AI-R09](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R45](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 07 Operations and Resilience | Availability and scalability | [AI-R13](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R11](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 07 Operations and Resilience | Incident management | [AI-R09](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R48](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 07 Operations and Resilience | Change and lifecycle management | [AI-R16](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R31](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 08 Legal, Regulatory and Compliance | Regulatory compliance | [AI-R28](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R37](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 08 Legal, Regulatory and Compliance | IP and liability | [AI-R27](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R36](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R51](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 08 Legal, Regulatory and Compliance | Contractual and licensing | [AI-R36](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R10](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Partial | Vendor contract terms are covered by the [vendor evaluation framework](../05_Vendor_Evaluation/11_AI_Security_Vendor_Evaluation_Master_Framework.md) and AI-CTRL-014. |
| 08 Legal, Regulatory and Compliance | Cross-border | [AI-R10](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 09 Third-Party and Model Supply Chain | Foundation-model dependence | [AI-R31](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R32](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 09 Third-Party and Model Supply Chain | Vendor due diligence | [AI-R10](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R41](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Partial | Covered mainly by AI-CTRL-014 and the vendor evaluation framework. |
| 09 Third-Party and Model Supply Chain | Lock-in and portability | [AI-R31](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 09 Third-Party and Model Supply Chain | Open-source component risk | [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R44](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R52](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 10 Workforce, Human and Societal | Skills and talent | [AI-R34](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R33](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 10 Workforce, Human and Societal | Deskilling and loss of institutional knowledge | [AI-R33](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 10 Workforce, Human and Societal | Workforce disruption / change | [AI-R34](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 10 Workforce, Human and Societal | Societal and reputational | [AI-R20](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R41](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Partial | Harm to people who never chose to use the system is addressed through impact assessment (AI-CTRL-042), not as a register risk. |
| 11 Financial and Resource | Cost and compute economics | [AI-R11](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R30](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R35](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 11 Financial and Resource | Investment / procurement | [AI-R30](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 11 Financial and Resource | Scaling and resource constraints | [AI-R13](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R31](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 12 Autonomy and Delegated Action (Agentic AI) | Autonomy, alignment and oversight | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R19](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 12 Autonomy and Delegated Action (Agentic AI) | Tool access and authorization | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R22](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R23](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 12 Autonomy and Delegated Action (Agentic AI) | Memory and context integrity | [AI-R21](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 12 Autonomy and Delegated Action (Agentic AI) | Multi-agent orchestration | [AI-R25](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |
| 12 Autonomy and Delegated Action (Agentic AI) | Action integrity and traceability | [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R09](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R54](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | Direct |  |

Of the 55 categories, 42 are a direct match and 13 are partial. No category is left without a match. Register entries AI-R29 to AI-R46 were added from the map on 17 October 2026 to close the largest gaps, and AI-R47 to AI-R54 on 29 October 2026 to close most of the partial matches that remained (31 direct and 24 partial before).

## What the map added to this wiki

Comparing the map with the register showed that the register was strong on security, data and agent risks and thin on the risks owned outside security. Version 1.2 of the [Enterprise AI Risk Register](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) added eighteen risks adapted from the map (AI-R29 to AI-R46), version 1.4 added eight more (AI-R47 to AI-R54) for categories that were still partial, and an Owner Domain column that uses the map's twelve domains. Version 1.1 of the [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md) added guidance from the map's usage notes on risk factors and scenarios, ownership and when to quantify. The [AI Use-Case Risk Triage](../02_Risk_Management/02F_AI_Use_Case_Risk_Triage.md) has new questions so the added risks are found at intake.

The partial matches above are where a team may still want to add risks of its own; the [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md) lists the fields a new entry needs.

## Attribution

The AI Risk Map v1.3 (2026) is © 2026 Evan Wheeler (GitHub [wheels344i-gte](https://github.com/wheels344i-gte)) and licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source: the map's GitHub repository, [https://github.com/wheels344i-gte/ai-risk-map](https://github.com/wheels344i-gte/ai-risk-map), and its website, https://riskframework.org/ai-risk-map/. Suggested citation, as the author gives it: Wheeler, E. (2026). *AI Risk Map* v1.3. Licensed CC BY-SA 4.0. This page cites the map's domain and category names. The register entries adapted from the map paraphrase its risk factors, and say which domain each came from. The map credits parts of its content to the Databricks AI Security Framework (DASF) and the Databricks AI Governance Framework, which it states are © Databricks and licensed CC BY-SA 4.0.

## Related pages

- [Enterprise AI Risk Register](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md)
- [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md)
- [AI Risk to Control Mapping](../02_Risk_Management/02D_AI_Risk_to_Control_Mapping.md)
- [NIST AI 600-1 Generative AI Profile Crosswalk](04_NIST_AI_600_1_GenAI_Profile_Crosswalk.md)
