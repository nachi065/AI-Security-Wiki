---
title: "AI BCF Crosswalk"
author: Nachiket Sathaye
parent: "Framework Crosswalks"
nav_order: 2
description: "How the AI Baseline Control Framework (AI BCF) and this wiki each work on their own, and where each of the 20 AI BCF controls is implemented in the wiki."
document_type: AI Security Wiki Reference
version: 1.0
---

# AI BCF Crosswalk

> **Purpose:** Show how the AI Baseline Control Framework (AI BCF) and this wiki each work on their own, and where each AI BCF control is implemented in the wiki.

> **Audience:** Security and governance leads building a first AI governance baseline, auditors, and teams in small or mid-sized organisations.

> **Credit:** This crosswalk exists because of the AI BCF, created by Jan van Dijke. See [Credit and licence](#credit-and-licence).

## The two at a glance

| | AI BCF | AI Security Wiki |
|---|---|---|
| What it is | A short governance baseline: 20 controls in five domains (Govern, Comply, Register, Access, Track). Each control is typed Baseline, Tier II or Trigger. | An open, vendor-neutral reference for securing AI adoption: 46 control objectives with evidence and audit tests, a 28-risk register, domain standards, vendor evaluation, regional compliance hubs and 653 test cases. |
| Author | Jan van Dijke | Nachiket Sathaye and Ankush Jain |
| Version | v1.0, 2 October 2026 | See the [home page](../index.md) |
| Where | [aibcf.org](https://aibcf.org/) | This site |
| Licence | CC BY-SA 4.0 | CC BY-SA 4.0 |

## Purpose and goals

**AI BCF: what to have in place.** It gives an organisation a compact list of governance controls for its use of AI. It separates the controls everyone needs (Baseline) from those for more mature organisations (Tier II) and those that apply only in certain situations (Trigger). Because it is short, it is easy to read, adopt and audit against. This description comes from its published structure; for the author's own statement of purpose, see [aibcf.org](https://aibcf.org/).

**This wiki: how to implement and prove it.** It helps teams decide whether an AI use case can be adopted safely and which risks, controls and approvals apply. It turns requirements into control objectives with evidence, audit procedures and test cases, and it covers security depth: runtime protection, agents, supply chain, data, resilience and incident response.

## How each serves on its own

| Use AI BCF alone when... | Use the wiki alone when... |
|---|---|
| You are starting out, or are a small organisation, and need a baseline fast. | You are building or buying AI systems and need security controls, tests and evidence. |
| You want a short checklist for a board, a customer questionnaire or a first internal review. | You are running a vendor evaluation or proof of concept. |
| You mainly need governance, not technical security controls. | You need regional legal pointers and fill-in templates. |

## How they fit together

AI BCF says what the baseline is. The wiki shows how to implement and test it: control objectives, evidence to collect, audit tests and test cases for each, plus security controls that sit beyond a governance baseline. The table below maps each AI BCF control to the wiki. Most are covered by one or more wiki control objectives. A few have no equivalent in the wiki yet. They are shown as gaps and are candidates for new wiki controls.

## How this crosswalk was made

AI BCF controls have identifiers (for example GV.1) but no titles. The short labels below are this wiki's own paraphrase, not AI BCF text. Read each control's exact wording, trigger conditions and sources at [aibcf.org/controls](https://aibcf.org/controls/). The mapping to wiki controls is this wiki's judgment, made from the AI BCF control wording and the wiki's control objectives. It is not an official AI BCF document. It was prepared against AI BCF v1.0, so check [aibcf.org](https://aibcf.org/) for the latest version.

**Match:** **Direct** means the wiki control objective covers the AI BCF control. **Partial** means it covers part of it. **Gap** means the wiki has no control objective for it.

## AI BCF to wiki

| AI BCF | Domain | Type | Label (wiki paraphrase) | Wiki control objectives and pages | Match |
|---|---|---|---|---|---|
| GV.1 | Govern | Baseline | AI position documented | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012); [Governance Operating Model](../08_Governance/16_AI_Governance_Operating_Model.md); [AI Policy, Standards and Acceptable Use](../08_Governance/17_AI_Policy_Standards_and_Acceptable_Use.md) | Direct |
| GV.2 | Govern | Baseline | AI roles and responsibilities assigned | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012); [Governance Operating Model](../08_Governance/16_AI_Governance_Operating_Model.md) | Direct |
| GV.3 | Govern | Baseline | Training on AI use, with records | [AI-CTRL-044](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-044) | Direct |
| GV.4 | Govern | Baseline | AI risks registered and reviewed | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011); [Risk Register](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md); [Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md) | Direct |
| CM.1 | Comply | Baseline | Legal and regulatory requirements known and managed | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-043](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-043); [Regional AI Regulatory Hub](../11_GCC_AI_Compliance/index.md) sections | Direct |
| CM.2 | Comply | Baseline | AI content and interactions marked as AI | No control objective. Templates only: [GCC T06 Bilingual AI Use Notice](../11_GCC_AI_Compliance/T06_Bilingual_AI_Use_Notice.md), [EU T06 Transparency Notice](../12_EU_AI_Compliance/T06_Transparency_Notice.md) | Gap |
| CM.3 | Comply | Trigger | High-risk use logged, overseen and disclosed | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041); notices as for CM.2 | Partial |
| CM.4 | Comply | Trigger | Fundamental rights impact assessment before high-risk use | [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042); [EU T02](../12_EU_AI_Compliance/T02_Impact_Assessment_FRIA_DPIA.md), [GCC T02](../11_GCC_AI_Compliance/T02_AI_Impact_Assessment.md) | Direct |
| RG.1 | Register | Baseline | AI systems and providers registered and classified | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031); [GCC T09 inventory](../11_GCC_AI_Compliance/T09_AI_System_Inventory.md) | Direct |
| RG.2 | Register | Tier II | Purpose of each AI use registered | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006) | Direct |
| RG.3 | Register | Tier II | Proportionality weighed against alternatives | No control objective | Gap |
| RG.4 | Register | Baseline | Decommissioning and offboarding of AI systems | No control objective. [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) covers stopping an agent, not retiring a system and removing its access | Gap |
| RG.5 | Register | Baseline | AI risks and training exposure in supplier privacy assessments | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007) | Direct |
| AC.1 | Access | Baseline | Access review before AI inherits users' rights | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016), [AI-CTRL-018](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-018) | Direct |
| AC.2 | Access | Trigger | Named identity and documented scope for AI with its own credentials | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015), [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) | Direct |
| AC.3 | Access | Trigger | Named owner for each autonomous AI system | [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006) | Direct |
| AC.4 | Access | Tier II | AI access rights granted under the access control model | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015), [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) | Partial |
| TR.1 | Track | Tier II | Performance indicators for deployed AI | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | Partial |
| TR.2 | Track | Tier II | Internal feedback on AI usage collected and reviewed | No control objective. Override metrics in [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045) are a partial fit | Gap |
| TR.3 | Track | Tier II | Errors in AI output logged and communicated | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Partial |

## What the comparison shows

**Coverage.** Of the 20 AI BCF controls, 12 are covered directly, 4 partly and 4 not at all by a control objective in this wiki.

**Gaps in the wiki.** Four AI BCF controls have no control objective here: marking AI content as AI (CM.2), weighing proportionality against alternatives (RG.3), decommissioning and offboarding (RG.4), and collecting internal feedback on AI use (TR.2). CM.3, AC.4, TR.1 and TR.3 are covered only in part. These are candidates for new control objectives. Until then, use the AI BCF wording for them.

**What the wiki adds.** The wiki goes well beyond a 20-control baseline in security depth: runtime and prompt-injection controls, agent containment and memory integrity, supply chain, data protection in pipelines, adversarial testing, incident response, cost abuse and 653 test cases. None of these have an AI BCF equivalent, because AI BCF is a governance baseline and not a security control set.

**Where AI BCF is stronger.** Its Trigger and Tier II types tell a small organisation which controls to start with. The wiki's tiering in [T01](../11_GCC_AI_Compliance/T01_AI_Use_Case_Intake_and_Risk_Tiering.md) scores each use case but does not give a starter set of controls.

## Credit and licence

This crosswalk exists because of the **AI Baseline Control Framework (AI BCF)**, created and maintained by **Jan van Dijke**. Thank you, Jan, for a clear and practical baseline, and for allowing this wiki to reference and link to it.

Credit:

> AI Baseline Control Framework (AI BCF) v1.0, Jan van Dijke, [aibcf.org](https://aibcf.org/), CC BY-SA 4.0

- Framework: [aibcf.org](https://aibcf.org/)
- Author: [Jan van Dijke on LinkedIn](https://www.linkedin.com/in/ACoAABXxfLIB4VxRSJzYxoxy316Wq0cv-vAL4Kw)
- Licence: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

AI BCF is published under CC BY-SA 4.0, which requires derived material to carry the same licence. This wiki is published under CC BY-SA 4.0 as well. This page cites AI BCF identifiers and uses its own labels and wording, and does not reproduce AI BCF control text. If AI BCF text is quoted in this wiki later, that text must be credited as above.

## Related pages

- [FINOS AI Governance Framework Crosswalk](01_FINOS_AIGF_Crosswalk.md)
- [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md)
- [T01 AI Use-Case Intake and Risk Tiering](../11_GCC_AI_Compliance/T01_AI_Use_Case_Intake_and_Risk_Tiering.md)
