---
title: "NIST AI 600-1 Generative AI Profile Crosswalk"
author: Nachiket Sathaye
parent: "Framework Crosswalks"
nav_order: 4
description: "The twelve generative AI risks in NIST AI 600-1 mapped to this wiki's risks and control objectives, with the risks the wiki covers only in part or not at all."
document_type: AI Security Wiki Reference
version: 1.0
---

# NIST AI 600-1 Generative AI Profile Crosswalk

> **Purpose:** Let a team that uses the NIST Generative AI Profile to name its generative AI risks find the matching risks and control objectives in this wiki, and see where the wiki stops.

> **Audience:** GRC, risk and audit teams; AI governance leads; security architecture.

> **Using the two together:** Use AI 600-1 for the list of generative AI risks and its suggested actions. Use this wiki for the control objectives, evidence and test cases on the security and governance side of those risks.

## About the profile and this page

NIST AI 600-1, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*, was published by the US National Institute of Standards and Technology in July 2024. It is a companion to the AI RMF 1.0. Section 2 defines twelve risks that generative AI creates or makes worse, and section 3 lists suggested actions under AI RMF subcategories. It is available free at https://doi.org/10.6028/NIST.AI.600-1.

The twelve risk names in the table were read from section 2 of the published document on 10 October 2026. The mapping to wiki risks and controls is this wiki's own judgment, made from the risk definitions, and has not been reviewed by NIST.

**Match** shows how closely the wiki covers the AI 600-1 risk: **Direct** (the wiki has a risk for it), **Partial** (the wiki covers part of it, as the last column explains) or **None**.

## AI 600-1 risks to wiki risks and controls

| # | AI 600-1 risk | Wiki risks | Main wiki controls | Match | What the match covers |
|---|---|---|---|---|---|
| 1 | CBRN Information or Capabilities | [AI-R12](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | Partial | The wiki treats this as one kind of harmful output. It has no risk or test case specific to chemical, biological, radiological or nuclear content. |
| 2 | Confabulation | [AI-R12](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045) | Direct | Grounding, citation checks and factual accuracy measures, with human review of outputs. |
| 3 | Dangerous, Violent, or Hateful Content | [AI-R12](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R20](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) | Partial | Covered through harmful content filtering and adversarial testing. TC-L08-018 tests output filters for hate, violence and self-harm content among its categories. |
| 4 | Data Privacy | [AI-R03](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R06](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R10](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002), [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042) | Direct | Leakage through prompts and outputs, third-party processing and impact assessment. |
| 5 | Environmental Impacts | None | None | None | The wiki has no risk or control for environmental impact. AI-CTRL-036 attributes usage by team and application, which could feed an estimate. |
| 6 | Harmful Bias or Homogenization | [AI-R14](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | Partial | Bias and performance gaps between groups are covered. Homogenization of outputs across systems that share a model is not. |
| 7 | Human-AI Configuration | [AI-R19](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045), [AI-CTRL-044](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-044), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | Partial | Over-reliance and automation bias are covered through oversight design and training. Anthropomorphism and emotional reliance on a system are not. |
| 8 | Information Integrity | [AI-R12](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R20](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | Partial | The accuracy of an organization's own AI output is covered. Disinformation campaigns run by others with generative AI are outside the wiki's scope. |
| 9 | Information Security | [AI-R05](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R24](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-032](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-032), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) | Partial | The attack surface of AI systems is the wiki's main subject. Attackers using generative AI to lower the cost of their own operations is discussed in [AI for Security and AI-Enabled Threats](../00_Foundations/10-AI-for-Security-and-AI-Enabled-Threats.md) and is not a register risk. |
| 10 | Intellectual Property | [AI-R27](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-046](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-046), [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | Direct | Policy on inputs and outputs, vendor terms and training data provenance. |
| 11 | Obscene, Degrading, and/or Abusive Content | [AI-R12](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | Partial | Covered as harmful output. The wiki has no risk or test case specific to synthetic child sexual abuse material or non-consensual intimate images. |
| 12 | Value Chain and Component Integration | [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R23](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031), [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024) | Direct | Vendor assurance, AI bill of materials, and governance of plugins and MCP servers. |

Of the twelve risks, 4 are a direct match, 7 are partial and 1 has no match.

## Where the wiki stops

The wiki is about securing and governing an organization's own use of AI. Three kinds of AI 600-1 risk fall partly or wholly outside that:

- **Harm to society at large.** Environmental impact, homogenization across systems that share a model, and disinformation campaigns run by others are not register risks.
- **Specific categories of harmful content.** The wiki has one risk for unreliable or harmful output (AI-R12) and one control for content safety (AI-CTRL-039). One test case, [TC-L08-018](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-018), exercises output filters across six content categories, among them hate, violence and sexual content. No test case covers weapons-related content or abusive imagery of real people.
- **The human side of human-AI interaction.** Oversight design, reviewer training and approval steps are covered. How people come to trust or depend on a system beyond that is not.

A team that needs these covered should take them from AI 600-1 and add them to its own register; the [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md) explains how to rate an added risk and lists the fields a new entry needs.

## What this page does not map

Section 3 of AI 600-1 lists suggested actions under AI RMF subcategories. They are not mapped one by one here. To go from a subcategory to wiki controls, use the [NIST AI RMF Crosswalk](03_NIST_AI_RMF_Crosswalk.md).

## Attribution

NIST publications are works of the United States Government. This page cites the risk names from section 2 of NIST AI 600-1 and does not reproduce its definitions or suggested actions.

## Related pages

- [NIST AI RMF Crosswalk](03_NIST_AI_RMF_Crosswalk.md)
- [Enterprise AI Risk Register](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md)
- [AI Risk to Control Mapping](../02_Risk_Management/02D_AI_Risk_to_Control_Mapping.md)
- [Risk, Control and Test Traceability](../02_Risk_Management/02G_Risk_Control_Test_Traceability.md)
