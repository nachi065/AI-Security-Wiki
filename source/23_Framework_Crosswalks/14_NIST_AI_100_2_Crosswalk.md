---
title: "NIST AI 100-2 Crosswalk"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Framework Crosswalks"
nav_order: 14
description: "The attack classes in NIST AI 100-2e2025, by their NISTAML identifiers, mapped to this wiki's control objectives and the test case layers that exercise them."
document_type: AI Security Wiki Reference
version: 1.0
last_reviewed: 2026-10-15
---

# NIST AI 100-2 Crosswalk

> **Purpose:** Let a team that describes attacks with the NIST adversarial machine learning taxonomy find the wiki control objectives that defend against each attack class, and the test case layers that exercise them.

> **Audience:** Red teams, security architects, threat modellers, AI security testers.

> **Using the two together:** Use NIST AI 100-2 for the vocabulary of attacks and the attacker objectives behind them. Use this wiki for the controls, evidence and tests that answer each one.

## About the report and this page

NIST AI 100-2e2025, *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations*, was published by the US National Institute of Standards and Technology in March 2025: [csrc.nist.gov/pubs/ai/100/2/e2025/final](https://csrc.nist.gov/pubs/ai/100/2/e2025/final). It has two taxonomies:

- **Predictive AI** (section 2): evasion attacks (2.2), poisoning attacks (2.3) and privacy attacks (2.4).
- **Generative AI** (section 3): supply chain attacks (3.2), direct prompting attacks (3.3), indirect prompt injection (3.4), security of agents (3.5) and benchmarks for AML vulnerabilities (3.6).

Both taxonomies classify attacks by the attacker's objective. Each attack class has an identifier of the form `NISTAML.0XY`, where the first two digits name the objective: 01 availability violations, 02 integrity violations, 03 privacy compromises, 04 misuse violations (generative AI only) and 05 supply chain attacks. An attack class that serves more than one objective keeps the same identifier under each.

> **Checked against the source.** The section headings, identifiers and attack class names on this page were read from the published PDF on 15 October 2026 with a retrieval tool, not line by line. The mapping to wiki controls is this wiki's own judgment and has not been reviewed by NIST. NIST intends to update the report, so check for a newer edition.

> **Correction notice.** Before 15 October 2026, [Foundations section 3.1](../00_Foundations/03-Threat-Taxonomy.md) described the generative AI taxonomy as "evasion, poisoning, privacy and misuse" classes. That was inaccurate and has been corrected.

## Attack classes to wiki controls

The table lists each identifier once. **Objective** shows the objectives the report files it under. **Test case layers** points to the layers of the [Test Case Library](../10_Test_Case_Library/index.md) where the matching cases sit; open the controls to see the individual cases that test them.

| Identifier | Attack class | Objective | Main wiki controls | Test case layers |
|---|---|---|---|---|
| NISTAML.011 | Model poisoning | Availability (predictive) | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) | [L14](../10_Test_Case_Library/L14-mlops-llmops-layer.md), [L16](../10_Test_Case_Library/L16-supply-chain-and-third-party.md) |
| NISTAML.012 | Clean-label poisoning | Availability and integrity (predictive) | [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) | [L13](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md) |
| NISTAML.013 | Data poisoning | Availability (predictive); availability and integrity (generative) | [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029), [AI-CTRL-019](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-019), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) | [L13](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md), [L11](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md) |
| NISTAML.014 | Energy-latency | Availability (predictive) | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036), [AI-CTRL-040](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-040) | [D13](../10_Test_Case_Library/D13-ai-cost-and-abuse-controls.md) |
| NISTAML.015 | Indirect prompt injection | Availability, integrity and privacy (generative) | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-019](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-019), [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022), [AI-CTRL-026](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-026) | [L07](../10_Test_Case_Library/L07-prompt-and-context-layer.md), [L11](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md), [D10](../10_Test_Case_Library/D10-browser-and-computer-use-agents.md) |
| NISTAML.018 | Prompt injection | Availability, integrity, privacy and misuse (generative) | [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002), [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) | [L07](../10_Test_Case_Library/L07-prompt-and-context-layer.md), [L08](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md), [D08](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md) |
| NISTAML.021 | Clean-label backdoor | Integrity (predictive) | [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) | [L13](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md) |
| NISTAML.022 | Evasion | Integrity (predictive) | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-021](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-021), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) | [L12](../10_Test_Case_Library/L12-model-layer.md), [D11](../10_Test_Case_Library/D11-multimodal-and-voice-input-security.md) |
| NISTAML.023 | Backdoor poisoning | Integrity (predictive); integrity and privacy (generative) | [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) | [L13](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md), [L16](../10_Test_Case_Library/L16-supply-chain-and-third-party.md) |
| NISTAML.024 | Targeted poisoning | Integrity (predictive and generative) | [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029), [AI-CTRL-019](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-019), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) | [L13](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md), [L11](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md) |
| NISTAML.025 | Black-box evasion | Integrity (predictive) | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034), [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) | [L12](../10_Test_Case_Library/L12-model-layer.md) |
| NISTAML.026 | Model poisoning | Integrity (predictive) | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) | [L14](../10_Test_Case_Library/L14-mlops-llmops-layer.md) |
| NISTAML.027 | Misaligned outputs | Integrity (generative) | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034), [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045) | [L05](../10_Test_Case_Library/L05-ai-applications.md), [D08](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md) |
| NISTAML.031 | Model extraction | Privacy (predictive) | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) | [L12](../10_Test_Case_Library/L12-model-layer.md) |
| NISTAML.032 | Reconstruction | Privacy (predictive) | [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) | [L12](../10_Test_Case_Library/L12-model-layer.md) |
| NISTAML.033 | Membership inference | Privacy (predictive and generative) | [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) | [L12](../10_Test_Case_Library/L12-model-layer.md), [L13](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md) |
| NISTAML.034 | Property inference | Privacy (predictive) | [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) | [L12](../10_Test_Case_Library/L12-model-layer.md) |
| NISTAML.035 | Prompt extraction | Privacy (generative) | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-020](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-020) | [L07](../10_Test_Case_Library/L07-prompt-and-context-layer.md) |
| NISTAML.036 | Leaking information from user interactions | Privacy (generative) | [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-018](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-018), [AI-CTRL-020](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-020) | [L10](../10_Test_Case_Library/L10-data-layer.md), [L08](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md) |
| NISTAML.037 | Training data attacks | Privacy (generative) | [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029) | [L13](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md) |
| NISTAML.038 | Data extraction | Privacy (generative) | [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-020](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-020), [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) | [L10](../10_Test_Case_Library/L10-data-layer.md), [L12](../10_Test_Case_Library/L12-model-layer.md) |
| NISTAML.039 | Compromising connected resources | Privacy (generative) | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016), [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022), [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024), [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027) | [L06](../10_Test_Case_Library/L06-agent-orchestration-layer.md), [D09](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md) |
| NISTAML.051 | Model poisoning (supply chain) | Supply chain (predictive and generative) | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031), [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030), [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) | [L16](../10_Test_Case_Library/L16-supply-chain-and-third-party.md) |

NISTAML.011 and NISTAML.026 are both named model poisoning: the report files the first under availability and the second under integrity.

## Report sections without an identifier

| Report section | Main wiki controls and pages |
|---|---|
| 3.5 Security of agents | [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006), [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025), [AI-CTRL-026](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-026), [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027); [Agentic AI Security and Tool Governance](../04_Domain_Standards/09_Agentic_AI_Security_and_Tool_Governance.md) |
| 3.6 Benchmarks for AML vulnerabilities | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034); [AI Red Teaming and Continuous Testing](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md) |
| 4.1 Key challenges in AML | [Limitations and Research Gaps](../00_Foundations/13-Limitations-and-Research-Gaps.md) |

## Relationship to the other attack catalogues

The wiki's test cases cite MITRE ATLAS techniques and OWASP items directly, and their crosswalks are generated from those citations. NIST AI 100-2 identifiers are not yet recorded in each control and test case, so this page is maintained by hand. See the [MITRE ATLAS Crosswalk](07_MITRE_ATLAS_Crosswalk.md), the [OWASP Top 10 Crosswalk](06_OWASP_Top_10_Crosswalk.md) and [Threat Taxonomy](../00_Foundations/03-Threat-Taxonomy.md).

## Attribution

NIST AI 100-2e2025 is a publication of the US National Institute of Standards and Technology. This page cites its identifiers, section headings and attack class names, and does not reproduce its text.

## Related pages

- [Threat Taxonomy](../00_Foundations/03-Threat-Taxonomy.md)
- [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md)
- [MITRE ATLAS Crosswalk](07_MITRE_ATLAS_Crosswalk.md)
- [AI Red Team Playbook](../06_Testing_and_Assurance/15C_AI_Red_Team_Playbook.md)
