---
title: "FINOS AI Governance Framework Crosswalk"
author: Nachiket Sathaye
parent: "Framework Crosswalks"
nav_order: 1
description: "Index from every FINOS AI Governance Framework risk and mitigation to this wiki's risks, control objectives and tests, with the regulatory references FINOS lists."
document_type: AI Security Wiki Reference
version: 1.0
---

# FINOS AI Governance Framework Crosswalk

> **Purpose:** Let a team that uses the FINOS AI Governance Framework (AIGF) as its financial-services AI risk catalogue find the matching risks, control objectives, evidence and tests in this wiki.

> **Audience:** Banks, insurers and other regulated firms; GRC, audit and security architecture teams.

> **Using the two together:** Use FINOS for the sector risk catalogue. Use this wiki for the control objectives, evidence, audit procedures and test cases that implement it.

## About FINOS and this page

The AIGF is published by FINOS (the Fintech Open Source Foundation) as an open catalogue of AI risks and mitigations for financial services. Its repository (github.com/finos/ai-governance-framework) states the Creative Commons Attribution 4.0 International licence in its LICENSE, LICENSE.spdx and NOTICE files, the same licence as this wiki.

This page was built from the repository at commit `a149dd1` (7 October 2026), which holds 24 risks and 25 mitigations. FINOS changes its framework over time, so check the identifiers against the current version at https://air-governance-framework.finos.org/ before relying on them. AIR-SEC-030, AIR-PREV-024, AIR-PREV-025 are marked Draft by FINOS.

**What is taken from FINOS:** identifiers, titles, status, the links between FINOS risks and mitigations, and the EU AI Act and ISO/IEC 42001 references that FINOS lists for each entry. **What is not:** FINOS descriptions and guidance text. **What is this wiki's own:** every mapping to wiki risks and controls. Those are judgments made from FINOS titles and links, not from a line-by-line reading of each FINOS page, and they have not been reviewed by FINOS.

## FINOS risks to wiki risks

**Match** shows how closely the wiki risk fits the FINOS risk: **Direct** (same risk) or **Partial** (overlaps part of it). The wiki risk IDs link to the [AI Risk to Control Mapping](../02_Risk_Management/02D_AI_Risk_to_Control_Mapping.md). EU AI Act articles are the ones FINOS lists for the risk.

| FINOS risk | Title | FINOS status | Wiki risks | Match | EU AI Act (per FINOS) |
|---|---|---|---|---|---|
| AIR-OP-004 | Hallucination and Inaccurate Outputs | Approved | AI-R12 | Direct | Art. 15, Art. 13, Art. 9 |
| AIR-OP-005 | Foundation Model Versioning | Approved | AI-R16 | Direct | Art. 9, Art. 15, Art. 53 |
| AIR-OP-006 | Non-Deterministic Behaviour | Approved | AI-R16 | Direct | Art. 9, Art. 15, Art. 14 |
| AIR-OP-007 | Availability of Foundational Model | Approved | AI-R13 | Direct | Art. 15, Art. 26, Art. 53 |
| AIR-OP-014 | Inadequate System Alignment | Approved | AI-R18 | Partial | Art. 5, Art. 9, Art. 14 |
| AIR-OP-016 | Bias and Discrimination | Approved | AI-R14 | Direct | Art. 5, Art. 9, Art. 10, Art. 14, Art. 27 |
| AIR-OP-017 | Lack of Explainability | Approved | AI-R15 | Direct | Art. 13, Art. 14, Art. 50, Art. 86 |
| AIR-OP-018 | Model Overreach / Expanded Use | Approved | AI-R18 | Partial | Art. 6, Art. 14, Art. 26 |
| AIR-OP-019 | Data Quality and Drift | Approved | AI-R17 | Direct | Art. 10, Art. 9, Art. 15 |
| AIR-OP-020 | Reputational Risk | Approved | AI-R20 | Direct | Art. 5, Art. 9, Art. 14 |
| AIR-OP-028 | Multi-Agent Trust Boundary Violations | Approved | AI-R25 | Direct | None listed |
| AIR-RC-001 | Information Leaked To Hosted Model | Approved | AI-R01, AI-R03, AI-R04, AI-R10 | Partial | Art. 10, Art. 13, Art. 53 |
| AIR-RC-022 | Regulatory Compliance and Oversight | Approved | AI-R19, AI-R28 | Direct | Art. 8, Art. 10, Art. 16, Art. 21, Art. 27 |
| AIR-RC-023 | Intellectual Property (IP) and Copyright | Approved | AI-R27 | Direct | Art. 10, Art. 11, Art. 53 |
| AIR-SEC-002 | Information Leaked to Vector Store | Approved | AI-R06 | Partial | Art. 10, Art. 15, Art. 16 |
| AIR-SEC-008 | Tampering With the Foundational Model | Approved | AI-R08 | Partial | Art. 15, Art. 16, Art. 53 |
| AIR-SEC-009 | Data Poisoning | Approved | AI-R08 | Partial | Art. 10, Art. 15, Art. 53 |
| AIR-SEC-010 | Prompt Injection | Approved | AI-R05 | Direct | Art. 5, Art. 15, Art. 14 |
| AIR-SEC-024 | Agent Action Authorization Bypass | Approved | AI-R07 | Partial | None listed |
| AIR-SEC-025 | Tool Chain Manipulation and Injection | Approved | AI-R24 | Direct | None listed |
| AIR-SEC-026 | MCP Server Supply Chain Compromise | Approved | AI-R23, AI-R08 | Direct | None listed |
| AIR-SEC-027 | Agent State Persistence Poisoning | Approved | AI-R21 | Direct | None listed |
| AIR-SEC-029 | Agent-Mediated Credential Discovery and Harvesting | Approved | AI-R22 | Direct | None listed |
| AIR-SEC-030 | Skill/Plugin Supply Chain Compromise | Draft | AI-R23 | Direct | None listed |

Wiki risks with no FINOS equivalent in the repository: AI-R02 (shadow AI), AI-R09 (auditability, which FINOS treats through detective mitigations), AI-R11 (cost abuse, treated by FINOS only as the mitigation AIR-DET-009) and AI-R26 (reasoning trace exposure).

## FINOS mitigations to wiki controls

The control mapping is this wiki's judgment from FINOS titles. The EU AI Act and ISO/IEC 42001 Annex A references are as listed by FINOS, with FINOS's `A-6-2` style written as `A.6.2`. They are FINOS's mapping and have not been separately verified here. FINOS also lists NIST SP 800-53 controls for some mitigations; see the FINOS page.

| FINOS mitigation | Title | FINOS status | Wiki control objectives | EU AI Act (per FINOS) | ISO/IEC 42001 Annex A (per FINOS) |
|---|---|---|---|---|---|
| AIR-DET-001 | AI Data Leakage Prevention and Detection | Approved | [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002), [AI-CTRL-003](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-003), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) | None listed | A.7.2, A.6.2.6, A.5.2 |
| AIR-DET-004 | AI System Observability | Approved | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-009](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009) | None listed | A.6.2.6, A.6.2.8 |
| AIR-DET-009 | AI System Alerting and Denial of Wallet (DoW) / Spend Monitoring | Approved | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) | None listed | A.6.2.6, A.4.2 |
| AIR-DET-011 | Human Feedback Loop for AI Systems | Approved | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034), [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045) | Art. 14, Art. 72 | A.6.2.6, A.8.2, A.8.3, A.3.3 |
| AIR-DET-013 | Providing Citations and Source Traceability for AI-Generated Information | Approved | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | Art. 13, Art. 86 | A.8.2, A.6.1.2, A.6.2.7 |
| AIR-DET-015 | Using Large Language Models for Automated Evaluation (LLM-as-a-Judge) | Approved | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | None listed | A.6.2.4, A.6.2.6 |
| AIR-DET-016 | Preserving Source Data Access Controls in AI Systems | Approved | [AI-CTRL-018](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-018) | None listed | A.7.2, A.7.3, A.9.2 |
| AIR-DET-021 | Agent Decision Audit and Explainability | Approved | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | Art. 12, Art. 26, Art. 72, Art. 13, Art. 86 | A.8.3, A.6.2.6 |
| AIR-PREV-002 | Data Filtering From External Knowledge Bases | Approved | [AI-CTRL-019](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-019) | None listed | A.7.2, A.7.3, A.7.4, A.7.6 |
| AIR-PREV-003 | User/App/Model Firewalling/Filtering | Approved | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-020](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-020) | None listed | A.6.1.3, A.6.2.2, A.9.2 |
| AIR-PREV-005 | System Acceptance Testing | Approved | [AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) | Art. 9, Art. 15 | A.6.2.4, A.6.2.5 |
| AIR-PREV-006 | Data Quality & Classification/Sensitivity | Approved | [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-019](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-019) | Art. 10 | A.7.4, A.7.2, A.4.3 |
| AIR-PREV-007 | Legal and Contractual Frameworks for AI Systems | Approved | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-046](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-046) | None listed | A.2.3, A.10.2, A.10.3, A.8.5 |
| AIR-PREV-008 | Quality of Service (QoS) and DDoS Prevention for AI Systems | Approved | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036), [AI-CTRL-040](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-040) | None listed | A.6.2.6, A.4.5 |
| AIR-PREV-010 | AI Model Version Pinning | Approved | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) | None listed | A.6.2.3, A.6.2.5, A.6.2.6, A.4.4 |
| AIR-PREV-012 | Role-Based Access Control for AI Data | Approved | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016), [AI-CTRL-018](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-018) | None listed | A.3.2, A.7.2 |
| AIR-PREV-014 | Encryption of AI Data at Rest | Approved | [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-032](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-032) | None listed | A.7.2 |
| AIR-PREV-017 | AI Firewall Implementation and Management | Approved | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005) | None listed | A.6.1.3, A.6.2.2, A.9.2 |
| AIR-PREV-018 | Agent Authority Least Privilege Framework | Approved | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016), [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022) | None listed | None listed |
| AIR-PREV-019 | Tool Chain Validation and Sanitization | Approved | [AI-CTRL-020](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-020), [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022), [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024) | None listed | None listed |
| AIR-PREV-020 | MCP Server Security Governance | Approved | [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024) | None listed | None listed |
| AIR-PREV-022 | Multi-Agent Isolation and Segmentation | Approved | [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006), [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027) | None listed | None listed |
| AIR-PREV-023 | Agentic System Credential Protection Framework | Approved | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015), [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) | None listed | None listed |
| AIR-PREV-024 | Human-in-the-Loop Action Approval Gate | Draft | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045) | Art. 14 | A.6.2.6, A.9.2 |
| AIR-PREV-025 | Skill/Plugin Integrity and Governance | Draft | [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) | None listed | None listed |

## Regulatory pointers checked for this crosswalk

These are the legal references the new and changed controls rely on, with what was checked and how. Nothing here is legal advice.

| Reference | What was checked | Source and date | Status |
|---|---|---|---|
| EU AI Act Article 10 | Title "Data and Data Governance" | artificialintelligenceact.eu, 10 Oct 2026 | Title checked in a secondary source. The page shows amended text; paragraph 5 appears removed and Article 4a is referenced. Check the Official Journal. |
| EU AI Act Article 12 | Title "Record-Keeping" | artificialintelligenceact.eu, 10 Oct 2026 | Title checked in a secondary source |
| EU AI Act Article 13 | Title "Transparency and Provision of Information to Deployers" | artificialintelligenceact.eu, 10 Oct 2026 | Title checked in a secondary source |
| EU AI Act Article 14 | Title "Human Oversight" | artificialintelligenceact.eu, 10 Oct 2026 | Title checked in a secondary source |
| EU AI Act Article 26 | Title "Obligations of Deployers of High-Risk AI Systems"; paragraph 2 on oversight by competent, trained people | artificialintelligenceact.eu, 10 Oct 2026 | Checked in a secondary source |
| EU AI Act Article 53 | Title "Obligations for Providers of General-Purpose AI Models"; paragraph 1 includes a copyright compliance policy | artificialintelligenceact.eu, 10 Oct 2026 | Checked in a secondary source |
| EU AI Act Article 86 | Title "Right to Explanation of Individual Decision-Making" | artificialintelligenceact.eu, 10 Oct 2026 | Checked in a secondary source |
| GDPR Article 22 | Title "Automated individual decision-making, including profiling" | Earlier check in this project | Title only |
| SR 11-7 | Federal Reserve and OCC supervisory guidance on model risk management, 4 April 2011 | Earlier check in this project | Date and issuers only |
| PRA SS1/23 | Published 17 May 2023, effective 17 May 2024; a current version published and effective 23 April 2026 | Earlier check in this project | Dates only; the wiki has not mapped its principles |

The EU AI Act is being amended, and the secondary source shows amended text. Article numbers and content may change again. Check every EU reference against the Official Journal of the European Union before citing it in an audit or filing.

## Attribution

The FINOS AI Governance Framework is published by FINOS under the Creative Commons Attribution 4.0 International licence (CC BY 4.0). Source: https://air-governance-framework.finos.org/ and https://github.com/finos/ai-governance-framework. This page cites FINOS identifiers, titles and reference lists and does not reproduce FINOS description text. It was not produced or endorsed by FINOS.

## Related pages

- [AI Risk to Control Mapping](../02_Risk_Management/02D_AI_Risk_to_Control_Mapping.md)
- [Enterprise AI Risk Register](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md)
- [AI Use-Case Risk Triage](../02_Risk_Management/02F_AI_Use_Case_Risk_Triage.md)
- [Sector Overlays: Financial Services](../04_Domain_Standards/10B_Sector_Overlays.md)
