---
title: "Framework Crosswalks"
author: Nachiket Sathaye
coauthors: Ankush Jain
description: "Cross-references from this wiki to other frameworks: FINOS AIGF, AI BCF, NIST AI RMF, NIST AI 600-1, NIST AI 100-2, ISO/IEC 42001 and nine further ISO/IEC AI standards, OWASP, MITRE ATLAS, ISO/IEC 27001, NIST CSF, CIS Controls, SOC 2, the OECD AI Principles, trustworthy AI and ethics standards, international AI instruments, the AI Risk Map, the OWASP MCP Top 10, the NIST SSDF and its generative AI profile SP 800-218A, PCI DSS with the PCI SSC guidance on AI systems, and eight privacy laws."
nav_order: 13
has_children: true
---

# Framework Crosswalks

This section connects the wiki to other frameworks. The wiki cites their identifiers without copying their text, so a team that works from another catalogue can find the matching risks, control objectives, evidence and tests here.

## AI frameworks

| Crosswalk | Use it when |
|---|---|
| [FINOS AI Governance Framework Crosswalk](01_FINOS_AIGF_Crosswalk.md) | Your risk catalogue is the FINOS AIGF for financial services, and you need controls, evidence and tests for each FINOS risk and mitigation. |
| [AI BCF Crosswalk](02_AI_BCF_Crosswalk.md) | You start from the short AI Baseline Control Framework (20 controls) and need the matching control objectives, or want to see where this wiki has no equivalent. |
| [NIST AI RMF Crosswalk](03_NIST_AI_RMF_Crosswalk.md) | Your programme is organised around the NIST AI RMF, and you need the control objectives and test cases for each subcategory, or the subcategories the wiki does not reach. |
| [NIST AI 600-1 Generative AI Profile Crosswalk](04_NIST_AI_600_1_GenAI_Profile_Crosswalk.md) | You use the twelve generative AI risks in NIST AI 600-1 and need the matching wiki risks and controls. |
| [ISO/IEC 42001 Crosswalk](05_ISO_IEC_42001_Crosswalk.md) | You are building or auditing an AI management system and need the control objectives and tests behind each Annex A control. |
| [OWASP Top 10 Crosswalk](06_OWASP_Top_10_Crosswalk.md) | You name application risks with the OWASP lists for LLM and agentic applications and need the controls and test cases for each item. |
| [OWASP MCP Top 10 Crosswalk](19_OWASP_MCP_Top_10_Crosswalk.md) | Your agents use MCP servers and you name their risks with the OWASP MCP Top 10 (beta), and need the matching wiki risks and controls. |
| [MITRE ATLAS Crosswalk](07_MITRE_ATLAS_Crosswalk.md) | You work from ATLAS techniques and need the controls that address each one and the test cases that exercise it. |
| [NIST AI 100-2 Crosswalk](14_NIST_AI_100_2_Crosswalk.md) | You describe attacks with the NIST adversarial machine learning taxonomy (NISTAML identifiers) and need the controls and test case layers for each attack class. |
| [ISO/IEC AI Standards Crosswalk](15_ISO_IEC_AI_Standards_Crosswalk.md) | You work with ISO/IEC 38507, 42005, 42006, 23894, TR 24028, 5338, 23053, 22989 or the 5259 data quality series, and need the wiki pages and controls behind each clause. |
| [OECD AI Principles Crosswalk](12_OECD_AI_Principles_Crosswalk.md) | Your AI policy is written against the five OECD values-based principles and you need the controls that put each one into practice. |
| [Trustworthy AI and Ethics Standards Crosswalk](16_Trustworthy_AI_Ethics_Crosswalk.md) | Your ethics commitments follow the EU Ethics Guidelines for Trustworthy AI, the UNESCO Recommendation or the IEEE 7000-series standards. |
| [International AI Instruments Crosswalk](17_International_AI_Instruments_Crosswalk.md) | You need to know where the Council of Europe Framework Convention on AI and the G7 Hiroshima Code of Conduct meet the wiki's controls. |
| [AI Risk Map Crosswalk](18_AI_Risk_Map_Crosswalk.md) | You identify AI risks with the AI Risk Map from RiskFramework.org, organised by who owns each risk, and need the matching register risks and the categories the wiki covers only in part. |

## Security frameworks

These four have no AI-specific content. Each crosswalk shows which wiki controls extend the framework's entries to AI systems.

| Crosswalk | Use it when |
|---|---|
| [ISO/IEC 27001 Crosswalk](08_ISO_IEC_27001_Crosswalk.md) | You run an information security management system and are bringing AI systems into its scope and statement of applicability. |
| [NIST CSF Crosswalk](09_NIST_CSF_Crosswalk.md) | Your security programme reports against the six functions and 22 categories of the Cybersecurity Framework 2.0. |
| [CIS Controls Crosswalk](10_CIS_Controls_Crosswalk.md) | Your baseline is the 18 CIS Critical Security Controls and you need to know what AI systems add to each. |
| [SOC 2 Crosswalk](11_SOC_2_Crosswalk.md) | You are a service organization with AI in the scope of a SOC 2 report, or you read vendors' reports. |

## Secure software development

| Crosswalk | Use it when |
|---|---|
| [NIST SSDF and SP 800-218A Crosswalk](20_NIST_SSDF_Crosswalk.md) | Your development lifecycle follows the NIST Secure Software Development Framework, or you produce or acquire generative AI models and systems under SP 800-218A, and need the controls, code and tests for each practice. |

## Payment card security

| Crosswalk | Use it when |
|---|---|
| [PCI DSS AI Crosswalk](21_PCI_DSS_AI_Crosswalk.md) | Your AI systems sit in or near a cardholder data environment, and you need the controls and tests behind each point of the PCI SSC supplement Security Considerations for AI Systems and the PCI DSS requirements it applies to AI. |

## Privacy laws

| Crosswalk | Use it when |
|---|---|
| [Privacy Law Crosswalk](13_Privacy_Law_Crosswalk.md) | You run AI systems under more than one of the GDPR, the CCPA, Quebec Law 25, the Singapore PDPA and the UAE, Saudi, Qatar and Bahrain data protection laws, and need to see where they differ. |

The NIST AI RMF, ISO/IEC 42001, OWASP, MITRE ATLAS, ISO/IEC 27001, NIST CSF, CIS Controls and SOC 2 pages are generated from the control library and the test cases each time the site is built, so they stay in step with them. So is the table below.

For regional laws and regulators, see the [Regional AI Regulatory Hub](../11_GCC_AI_Compliance/index.md) sections. For sector rules such as HIPAA, PCI DSS and insurance regulation, see the [Sector Overlays](../04_Domain_Standards/10B_Sector_Overlays.md); PCI DSS also has its own [crosswalk](21_PCI_DSS_AI_Crosswalk.md).

## All mappings by control

One row for each wiki control, with the identifiers it cites in each framework. "None" means the framework has no entry that the control supports. Open the control for the names behind the identifiers, or the framework's crosswalk to read the mapping from the other direction.

<!-- framework-crosswalk: summary -->
