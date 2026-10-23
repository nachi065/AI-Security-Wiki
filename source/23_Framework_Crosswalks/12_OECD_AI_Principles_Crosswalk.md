---
title: "OECD AI Principles Crosswalk"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Framework Crosswalks"
nav_order: 12
description: "The five values-based OECD AI Principles mapped to this wiki's control objectives, with the principles the wiki covers only in part or not at all."
document_type: AI Security Wiki Reference
version: 1.0
---

# OECD AI Principles Crosswalk

> **Purpose:** Let a team whose AI policy or ethics statement is written against the OECD AI Principles find the wiki control objectives that put each principle into practice, and see where the wiki stops.

> **Audience:** AI governance leads, policy and ethics teams, GRC teams.

> **Using the two together:** Use the OECD AI Principles for the values an AI policy commits to. Use this wiki for the control objectives, evidence and test cases behind the security and governance side of those commitments.

## About the principles and this page

The OECD AI Principles are set out in the OECD Recommendation of the Council on Artificial Intelligence, adopted in May 2019 and revised in May 2024. The Recommendation has two parts. The first holds five values-based principles for everyone who plays an active part in the AI system lifecycle, numbered 1.1 to 1.5. The second holds five recommendations to governments, numbered 2.1 to 2.5.

The Recommendation is addressed to governments and does not bind organizations. It matters to them because many national AI strategies and laws borrow from it, including the definition of an AI system.

> **Verify before use.** The principle names, numbers and dates on this page were written from memory and were not checked against the OECD's published text. The mapping to wiki controls is this wiki's own judgment and has not been reviewed by the OECD.

**Match** shows how closely the wiki covers the principle: **Direct** (the wiki has controls for most of it), **Partial** (the wiki covers part of it, as the last column explains) or **None**.

## Principles to wiki controls

| # | OECD principle | Main wiki controls | Match | What the match covers |
|---|---|---|---|---|
| 1.1 | Inclusive growth, sustainable development and well-being | None | None | The wiki has no control for the social or environmental benefit of an AI system. [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) records the purpose of each use case, which is where an organization could record the benefit it expects. |
| 1.2 | Respect for the rule of law, human rights and democratic values, including fairness and privacy | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041), [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042), [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045) | Partial | Privacy compliance, bias testing, impact assessment on people's rights, and human oversight. Wider effects on democratic values, such as the spread of misleading content by others, are outside the wiki's scope. |
| 1.3 | Transparency and explainability | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | Partial | Explanations for high-impact decisions, grounded output, and the notices that privacy law requires. The wiki has no single control for telling people they are dealing with an AI system; the regional templates cover it where a law asks for it. |
| 1.4 | Robustness, security and safety | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025), [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034), [AI-CTRL-040](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-040) | Direct | Security of AI systems is the wiki's main subject. These five are the closest to the principle's wording: runtime protection, the ability to stop a system, model protection, adversarial testing, and fail-safe operation. Most of the control library supports this principle. |
| 1.5 | Accountability | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | Direct | Named owners for each use case, roles and policy, risk assessment across the lifecycle, audit logs that make decisions traceable, and evidence that controls operate. |

Of the five principles, 2 are a direct match, 2 are partial and 1 has no match.

## What this page does not map

The five recommendations to governments (2.1 to 2.5) cover public investment in research, the policy environment, skills and international cooperation. They are addressed to states and have no counterpart in an organization's control library.

## Attribution

The OECD AI Principles are published by the Organisation for Economic Co-operation and Development. This page cites the principle names and does not reproduce their text.

## Related pages

- [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md)
- [Governance, Standards and Regulation](../00_Foundations/09-Governance-Standards-and-Regulation.md)
- [AI Policy, Standards and Acceptable Use](../08_Governance/17_AI_Policy_Standards_and_Acceptable_Use.md)
- [NIST AI RMF Crosswalk](03_NIST_AI_RMF_Crosswalk.md)
