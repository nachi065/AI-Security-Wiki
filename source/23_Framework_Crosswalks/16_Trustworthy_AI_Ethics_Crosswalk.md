---
title: "Trustworthy AI and Ethics Standards Crosswalk"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Framework Crosswalks"
nav_order: 16
description: "The EU Ethics Guidelines for Trustworthy AI, the UNESCO Recommendation on the Ethics of AI and the IEEE 7000-series standards mapped to this wiki's controls, with the gaps."
document_type: AI Security Wiki Reference
version: 1.0
last_reviewed: 2026-10-15
---

# Trustworthy AI and Ethics Standards Crosswalk

> **Purpose:** Let a team whose AI ethics commitments are written against the EU's trustworthy AI guidelines, UNESCO's Recommendation or the IEEE ethics standards find the wiki controls that put them into practice, and see where the wiki stops.

> **Audience:** AI ethics and responsible AI teams, AI governance leads, product owners, model risk teams.

> **Using the two together:** Use these instruments for the values and the design processes. Use this wiki for the control objectives, evidence and tests behind the security, privacy, fairness and oversight parts of them.

**Match** shows how closely the wiki covers each item: **Direct** (the wiki has controls for most of it), **Partial** (the wiki covers part of it, as the last column explains) or **None**. The mappings are this wiki's own judgment and have not been reviewed by the issuing bodies.

## EU Ethics Guidelines for Trustworthy AI

Published by the European Commission's High-Level Expert Group on AI on 8 April 2019: [digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai](https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai). Trustworthy AI is lawful, ethical and robust, and the guidelines set seven key requirements. The Assessment List for Trustworthy AI (ALTAI), published in July 2020, turns them into a self-assessment. *Checked against the Commission's page on 15 October 2026.*

| # | Requirement | Main wiki controls | Match | What the match covers |
|---|---|---|---|---|
| 1 | Human agency and oversight | [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) | Direct | Oversight design, approval of sensitive actions, and the ability to stop a system. |
| 2 | Technical robustness and safety | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034), [AI-CTRL-040](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-040), [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005) | Direct | Adversarial testing, fail-safe operation, model and runtime protection. |
| 3 | Privacy and data governance | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029) | Direct | Privacy compliance, data protection in pipelines, data provenance and quality. |
| 4 | Transparency | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) | Partial | Explanations, grounded output and audit trails. Telling people they are dealing with AI is covered by the regional templates where a law requires it. |
| 5 | Diversity, non-discrimination and fairness | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | Partial | Bias testing and bias profiles. Accessibility for people with disabilities is not covered. |
| 6 | Societal and environmental well-being | None | None | The wiki has no control for societal or environmental effects. See [Well-being and societal impact](#well-being-and-societal-impact). |
| 7 | Accountability | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) | Direct | Roles, risk assessment, audit evidence and redress through human review. |

Of the seven requirements, 4 are a direct match, 2 are partial and 1 has no match.

## UNESCO Recommendation on the Ethics of Artificial Intelligence

Adopted by UNESCO's Member States on 23 November 2021 (SHS/BIO/PI/2021/1): [unesco.org/en/artificial-intelligence/recommendation-ethics](https://www.unesco.org/en/artificial-intelligence/recommendation-ethics); full text on [UNESDOC](https://unesdoc.unesco.org/ark:/48223/pf0000381137). It sets four values, ten principles and eleven areas of policy action. The Recommendation is addressed to Member States. *The values and principles were checked against UNESCO's page, and the policy areas and paragraph numbers against a copy of the full text, on 15 October 2026.*

| Principle | Main wiki controls | Match |
|---|---|---|
| Proportionality and do no harm | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042) | Partial |
| Safety and security | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034), [AI-CTRL-040](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-040) | Direct |
| Right to privacy and data protection | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) | Direct |
| Multi-stakeholder and adaptive governance and collaboration | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-043](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-043) | Partial |
| Responsibility and accountability | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | Direct |
| Transparency and explainability | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | Partial |
| Human oversight and determination | [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | Direct |
| Sustainability | None | None |
| Awareness and literacy | [AI-CTRL-044](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-044) | Direct |
| Fairness and non-discrimination | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | Partial |

Of the eleven policy areas, two apply directly to organizations. **Policy Area 1, Ethical impact assessment** (paragraphs 50 to 53), is the international basis for [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042). **Policy Area 3, Data policy** (paragraphs 71 to 77), supports the data quality and provenance requirements in [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029). The other nine (ethical governance and stewardship; development and international cooperation; environment and ecosystems; gender; culture; education and research; communication and information; economy and labour; health and social well-being) are addressed to governments.

## IEEE 7000-series standards

> **Based on available public data.** IEEE standards are sold by IEEE and their contents pages are not freely published. The titles, edition years, status and scope below were checked on IEEE's own pages on 15 October 2026. The clause structures come from **secondary public sources** (named in each row) and, for IEEE 7001 and IEEE 7010, from papers by members of the working groups that describe the **draft** standards. Clause numbers have not been checked against the published standards and may differ. Verify them against a purchased copy before citing them. This is work in progress.

| Standard | Scope (from IEEE) | Structure from public sources | Main wiki controls | Match |
|---|---|---|---|---|
| [IEEE 7000-2021](https://standards.ieee.org/ieee/7000/6781/) Model Process for Addressing Ethical Concerns during System Design. Active; published 15 Sep 2021 | Processes to elicit and prioritise stakeholders' ethical values and keep them traceable into design | Clause 7 concept of operations and context exploration; 8 ethical values elicitation and prioritization; 9 ethical requirements definition; 10 ethical risk-based design; 11 transparency management (source: [ESE practices notes](https://github.com/ethical-se/ese-practices/blob/main/ESE-BackgroundInformation.md)) | [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042), [AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033); [AI Product Developer Playbook](../07_Role_Based_Playbooks/15A_AI_Product_Developer_Playbook.md) | Partial: the wiki has no step for eliciting stakeholder values at inception. |
| [IEEE 7001-2021](https://standards.ieee.org/ieee/7001/6929) Transparency of Autonomous Systems. Active; published 4 Mar 2022 | Measurable, testable levels of transparency | In the draft: five stakeholder groups (end users; general public and bystanders; safety certification agencies; incident and accident investigators; lawyers and expert witnesses), each with levels 0 to 5, and two processes, a system transparency assessment and a system transparency specification (source: [Winfield et al. 2021](https://www.frontiersin.org/articles/10.3389/frobt.2021.665729/pdf), describing draft P7001/D1) | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Partial: the wiki does not set a target transparency level for each audience. The draft's investigator levels (timestamped logs, decision logs, logged reasons) correspond to [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008). |
| [IEEE 7002-2022](https://standards.ieee.org/ieee/7002/6898/) Data Privacy Process. Active; published 19 Apr 2022 | Engineering process requirements for privacy in systems that use personal data, with privacy impact assessments and conformity checklists | Not found in public sources | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042); [Privacy Law Crosswalk](13_Privacy_Law_Crosswalk.md) | Partial |
| [IEEE 7003-2024](https://standards.ieee.org/ieee/7003/11357) Algorithmic Bias Considerations. Active; published 24 Jan 2025 | Criteria for validation datasets for bias quality control; defining and communicating an algorithm's validated application boundaries; managing user expectations | Clause 4 requirements and boundaries; 5 bias profile; 6 stakeholder identification; 7 data representation; 8 risk and impact assessment; 9.2 design and output evaluation; 9.3 ongoing evaluation (source: [Modulos framework notes](https://docs.modulos.ai/frameworks/ieee-7003), which paraphrase the headings) | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) (bias profile and validated boundaries); [GCC T10 Bias Testing Record](../11_GCC_AI_Compliance/T10_Bias_Testing_Record.md) | Direct |
| [IEEE 7010-2020](https://standards.ieee.org/ieee/7010/7718/) Recommended Practice for Assessing the Impact of Autonomous and Intelligent Systems on Human Well-Being | Well-being impact assessment based on established well-being indicators and stakeholder engagement | Five activities: internal analysis and stakeholder engagement; a well-being indicator dashboard; data planning and collection; data analysis and improvement; iteration (source: [Schiff et al.](https://arxiv.org/pdf/2005.06620), working group members) | None | None |

## Well-being and societal impact

Three instruments on this page, and the [OECD AI Principles Crosswalk](12_OECD_AI_Principles_Crosswalk.md), point to the same gap: the wiki has no control for the effect of an AI system on well-being, society or the environment. This wiki is mainly about security and governance, so it does not add a control for it. An organization that commits to these principles can add an optional well-being section to its impact assessment under [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042), using the IEEE 7010 activities: engage stakeholders, choose three to five well-being indicators, measure them before deployment and again afterwards, and feed the results back into design.

## Attribution

The Ethics Guidelines for Trustworthy AI are published by the European Commission. The Recommendation on the Ethics of Artificial Intelligence is published by UNESCO. IEEE 7000, 7001, 7002, 7003 and 7010 are published by the IEEE Standards Association. This page cites names, numbers and headings and does not reproduce their text.

## Related pages

- [OECD AI Principles Crosswalk](12_OECD_AI_Principles_Crosswalk.md)
- [ISO/IEC AI Standards Crosswalk](15_ISO_IEC_AI_Standards_Crosswalk.md)
- [International AI Instruments Crosswalk](17_International_AI_Instruments_Crosswalk.md)
- [AI Policy, Standards and Acceptable Use](../08_Governance/17_AI_Policy_Standards_and_Acceptable_Use.md)
