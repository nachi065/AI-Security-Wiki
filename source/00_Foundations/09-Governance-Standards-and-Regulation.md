---
title: "9. Governance, Standards and Regulation"
description: "AI governance and standards compared: NIST AI RMF, NIST AI 100-2, ISO/IEC 42001, OWASP, MITRE ATLAS, Google SAIF, ENISA and the EU AI Act timetable."
author: Nachiket Sathaye
parent: "Foundations"
nav_order: 9
document_type: Practitioner Research Paper
---

# 9. Governance, Standards and Regulation

## 9.1 Governance fundamentals

AI risk cannot be delegated to the security team alone. Product owners, data owners, model developers, application engineers, security architects, legal and compliance, procurement, internal audit and executive risk owners all hold part of the accountability. A workable minimum: [Analysis]

- **An AI inventory** (systems, models, datasets, providers, owners, data classes, tools, autonomy level). You cannot govern what you cannot list; include shadow and embedded AI features in SaaS.
- **Named risk ownership** per system, with documented risk acceptance and time-bound exceptions.
- **Policies** covering acceptable use, data handling, model and provider approval, autonomy limits and incident reporting.
- **Assurance** by an independent function: internal audit or a second line that can test the evidence.

## 9.2 The main instruments

| Instrument | What it is | Use it for |
|---|---|---|
| **NIST AI RMF 1.0** (Jan 2023) [3] | Voluntary risk-management framework organised around Govern, Map, Measure and Manage | Programme structure and risk language |
| **NIST AI 600-1** (Jul 2024) [2] | Generative AI profile of the AI RMF | Identifying risks specific to or amplified by generative AI |
| **NIST AI 100-2e2025** (Mar 2025) [1] | Taxonomy and terminology of adversarial machine learning attacks and mitigations | Shared vocabulary for attack classes; testing scope |
| **ISO/IEC 42001:2023** [4] | AI management system requirements | Certifiable management-system approach; governance evidence |
| **ISO/IEC 23894:2023** [5] | Guidance on AI risk management | Integrating AI into enterprise risk processes |
| **ISO/IEC 27001:2022** [6] | Information security management systems | Existing ISMS into which AI controls are added |
| **OWASP Top 10 for LLM Applications 2025** [11] | Community catalogue of LLM application risks | Developer awareness; test-case design |
| **OWASP Top 10 for Agentic Applications** (Dec 2025) [12] | Community catalogue of agentic risks | Agent threat modelling |
| **MITRE ATLAS** [14] | Knowledge base of adversary tactics and techniques against AI-enabled systems | Threat-informed testing; incident description |
| **Google SAIF** [15] | Practitioner framework with a risk map and controls, including an agent-security section | Control-selection ideas for AI development and deployment |
| **ENISA reports** [9][10] | EU agency analysis of AI cybersecurity threats (2020) and research needs (2023) | Threat-landscape and policy context for EU readers |
| **EU AI Act** [7][8] | Binding EU regulation | Legal obligations for in-scope providers and deployers |

*Descriptions summarise the sources cited; consult each document for authoritative scope and wording.*

## 9.3 EU AI Act status (verify before relying)

The AI Act is Regulation (EU) 2024/1689 [7]. General-purpose AI obligations have applied since 2 August 2025. In 2026 EU institutions agreed an "AI Omnibus" amending the timetable. Secondary sources report **[Reported]** that:

- the omnibus was published as Regulation (EU) 2026/1744 on 24 July 2026 and entered into force on 27 July 2026;
- obligations for stand-alone high-risk systems (Annex III) now apply from **2 December 2027**, and for high-risk AI as safety components in regulated products (Annex I) from **2 August 2028**;
- Article 50 transparency obligations apply from 2 August 2026, with a grace period for watermarking of systems already on the market until 2 December 2026;
- new prohibited practices relating to AI-generated child sexual abuse material and non-consensual intimate deepfakes were added [8].

> **Verification required.** These dates come from law-firm commentary, not from the Official Journal. Check the text on EUR-Lex and confirm which obligations apply to your organisation's role (provider, deployer, importer, distributor) before making any compliance decision. This paper is not legal advice.

The Act's Article 15 addresses accuracy, robustness and cybersecurity for high-risk systems, and, to the author's understanding, refers specifically to risks such as data poisoning, model poisoning, adversarial examples and confidentiality attacks. **Check the current text of Article 15** before quoting it. [7]

## 9.4 How the instruments relate

| Need | Primary instruments | Gap to fill yourself |
|---|---|---|
| Programme structure and risk language | NIST AI RMF, ISO/IEC 23894 | Translating into engineering controls |
| Certifiable management system | ISO/IEC 42001 with ISO/IEC 27001 | Technical test criteria; threat-specific controls |
| Attack vocabulary and testing | NIST AI 100-2e2025, OWASP lists, MITRE ATLAS | Pass/fail thresholds, which none of these set |
| Architecture and control ideas | SAIF, ENISA, this paper's reference architecture | Environment-specific implementation |
| Legal compliance | EU AI Act and national law | Interpreting scope and role |

**Analysis.** Management-system standards tell you *that* you need risk assessment, controls and evidence. Attack catalogues tell you *what* can go wrong. Neither tells you the acceptable attack-success rate for a given system. That judgement belongs to the organisation's risk owner and must be written down. [Analysis]

**Selection guidance.** Start from obligations (law, contract), choose one management framework as the spine, adopt one attack taxonomy for testing, and avoid trying to map every framework to every other. A single control set with tagged mappings is easier to maintain than parallel compliance programmes.

**Regional scope.** This page covers the EU AI Act only. For UAE data residency and sovereignty requirements, see [Sovereign AI, UAE Compliance and Data Residency Requirements](../04_Domain_Standards/10_Sovereign_AI_UAE_Compliance_and_Data_Residency.md). For the laws, policies and baselines of the UAE and other GCC states, see the [GCC AI Regulatory Hub](../11_GCC_AI_Compliance/01_GCC_AI_Regulatory_Hub.md), which is compiled from secondary sources.
