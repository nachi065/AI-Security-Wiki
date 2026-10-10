---
title: "Sector Overlays: Financial Services, Insurance, Health and Government"
author: Nachiket Sathaye
parent: "Domain Standards"
nav_order: 6
description: "Sector expectations for AI in financial services, insurance, health and government, mapped to wiki controls, test cases, regional instruments and templates."
document_type: AI Security Wiki Reference
version: 1.0
---

# Sector Overlays: Financial Services, Insurance, Health and Government

> **Purpose:** Show what sector regulators and public-sector buyers expect of AI systems, and which wiki controls, test cases and templates meet each expectation.

> **Audience:** GRC and compliance teams, model risk, security architecture, vendors that sell to regulated sectors, auditors.

> **Verification required.** Every regional instrument named on this page comes from the regional compliance sections, which were compiled on 7 October 2026 from secondary sources and from memory of the law. No primary legal text was read. The tags [Reported], [Recalled], [Conflict] and [Unverified] are explained in each regional section. Check the primary text before relying on any of them. This is not legal advice.

## How to use this page

Apply the wiki's controls as usual, then add the rows for your sector. Each row names the control, a test case that exercises it and the regional instruments that ask for it. The instrument IDs (for example U9 or IN5) are rows in the region's crosswalk, which gives the instrument's name and verification status. Open the regional hub for the detail.

## 1. Financial services

Banks, lenders, securities firms and payment providers.

For a financial-services AI risk catalogue, the FINOS AI Governance Framework is an open reference. This wiki cross-references it in the [FINOS crosswalk](../23_Framework_Crosswalks/01_FINOS_AIGF_Crosswalk.md): use FINOS for the risk catalogue and this wiki for controls, evidence and tests.

| Expectation | Wiki controls | Test cases | Regional instruments |
|---|---|---|---|
| Board and senior management accountability for AI | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | [TC-L01-003](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-003), [TC-L02-024](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-024) | [GCC](../11_GCC_AI_Compliance/01_GCC_AI_Regulatory_Hub.md): CBUAE Guidance Note (U9) [Reported]; [UK](../21_UK_AI_Compliance/01_UK_AI_Regulatory_Hub.md): FCA approach and SM&CR (UK5) [Recalled]; [India](../17_India_AI_Compliance/01_India_AI_Regulatory_Hub.md): RBI FREE-AI report (IN5) [Reported]; Singapore: MAS Guidelines paras 3.1 to 3.6 (SG5) [Verified] |
| Complete AI and model inventory with a risk or materiality rating | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | [TC-L01-001](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-001), [TC-L01-005](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-005) | GCC: CBUAE (U9), QCB guideline (Q4) [Reported]; [Singapore](../19_Singapore_AI_Compliance/01_Singapore_AI_Regulatory_Hub.md): MAS Guidelines on AI Risk Management, paras 4.5 to 4.13 (SG5) [Verified]; UK: PRA SS1/23 (UK6) [Recalled]; [Canada](../15_Canada_AI_Compliance/01_Canada_AI_Regulatory_Hub.md): OSFI E-23 (CA6) [Unverified] |
| Independent validation and model risk management | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [TC-L02-013](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-013) | India: RBI draft model risk guidance (IN6) [Reported]; UK: PRA SS1/23 (UK6) [Recalled]; Canada: OSFI E-23 (CA6) [Unverified]; [US](../22_US_AI_Compliance/01_US_AI_Regulatory_Hub.md): SR 26-2 and OCC Bulletin 2026-13, which replaced SR 11-7 (US12); see the note below; Singapore: MAS Guidelines para 5.19, for high-risk use cases (SG5) [Verified] |
| Bias testing and fair customer outcomes | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [TC-L03-031](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-031), [TC-L03-032](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-032) | GCC: CBUAE annual bias testing (U9) [Reported]; Singapore: MAS FEAT (SG6) and MAS Guidelines paras 5.7 to 5.8 (SG5) [Verified]; UK: Consumer Duty (UK5) [Recalled]; US: ECOA and anti-discrimination law (US12) [Recalled] |
| Explanation of adverse decisions and human review | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | [TC-L03-029](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-029), [TC-L03-008](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-008) | GCC: CBUAE (U9) [Reported]; US: ECOA adverse action (US12) [Recalled]; [EU](../12_EU_AI_Compliance/01_EU_AI_Regulatory_Hub.md): AI Act Art. 86 and GDPR Art. 22 [Recalled] |
| Meaningful human oversight of AI-assisted decisions | [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | [TC-L01-012](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-012), [TC-L03-040](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-040), [TC-L03-041](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-041) | EU: AI Act Article 14 and Article 26(2); GDPR Article 22. GCC: U3, U6, U9, Q4 [Reported]. See the control for the verification status; Singapore: MAS Guidelines para 5.9 (SG5) [Verified] |
| Ability to stop an AI system | [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) | [TC-L01-012](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-012) | GCC: CBUAE kill-switch expectation (U9) [Reported]; Singapore: MAS Guidelines paras 5.3 and 5.23, kill switches for high-risk AI (SG5) [Verified] |
| Due diligence on AI suppliers and outsourcing | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | [TC-L03-021](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-021), [TC-L02-021](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-021) | GCC: CBUAE (U9) [Reported]; [Australia](../13_Australia_AI_Compliance/01_Australia_AI_Regulatory_Hub.md): APRA CPS 230 (AU8) [Recalled]; EU: DORA (E6) [Reported]; India: SEBI circulars (IN7) [Reported]; Singapore: MAS Guidelines paras 5.10 to 5.11 (SG5) [Verified] |
| Operational resilience of services that depend on AI | [AI-CTRL-040](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-040) | [TC-L01-018](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-018) | Australia: APRA CPS 230 (AU8) [Recalled]; EU: DORA (E6) [Reported]; UK: operational resilience rules (UK5) [Recalled]; Singapore: MAS Guidelines para 5.3, contingency plans (SG5) [Verified] |
| Incident reporting to the supervisor | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | [TC-L03-019](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-019) | EU: DORA (E6) [Reported]; India: RBI, SEBI and IRDAI sector directions [Unverified]; Australia: APRA CPS 234 (AU8) [Recalled] |
| Classification of credit decisions as high-risk or consequential | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | [TC-L03-037](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-037) | EU: AI Act Annex III, essential services including credit [Reported]; US: state consequential-decision laws (US5) [Conflict] |

US model risk guidance: SR 11-7 was replaced on 17 April 2026 by revised interagency guidance (Federal Reserve SR 26-2, OCC Bulletin 2026-13). The revised guidance leaves generative AI and agentic AI models out of scope because they are novel and rapidly evolving, and the agencies plan a request for information on banks' use of AI. Applying SR 11-7 practices to those systems is optional. They remain a usable benchmark for independent validation and monitoring if you want one. Details and sources are in the [US AI Regulatory Hub](../22_US_AI_Compliance/01_US_AI_Regulatory_Hub.md).

Templates: [IN-T3 Regulated-Entity AI Readiness Checklist](../17_India_AI_Compliance/IN-T3_Regulated_Entity_AI_Readiness.md), [UK-T2 Regulated-Firm AI Checklist](../21_UK_AI_Compliance/UK-T2_Regulated_Firm_AI_Checklist.md), [SG-T2 AI Inventory and Risk Materiality Assessment](../19_Singapore_AI_Compliance/SG-T2_MAS_Style_Inventory_and_Materiality.md), [CA-T3 OSFI E-23 Model Inventory Addendum](../15_Canada_AI_Compliance/CA-T3_OSFI_E23_Inventory_Addendum.md), [GCC T10 Bias Testing Record](../11_GCC_AI_Compliance/T10_Bias_Testing_Record.md).

SAMA expectations for Saudi Arabia were not researched.

## 2. Insurance

| Expectation | Wiki controls | Test cases | Regional instruments |
|---|---|---|---|
| Classification of life and health insurance decisions | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | [TC-L03-037](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-037) | EU: AI Act Annex III, essential services including insurance [Reported]; US: state consequential-decision definitions (US5) [Reported for Colorado] |
| Fundamental rights impact assessment before deployment | [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042) | [TC-L03-034](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-034) | EU: AI Act Art. 27, for deployers in life and health insurance [Recalled; scope to verify] |
| Bias testing of underwriting and claims decisions | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [TC-L03-031](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-031), [TC-L03-032](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-032) | EU: AI Act Art. 10 [Recalled]; US: anti-discrimination law (US12) [Recalled] |
| AI-specific cybersecurity readiness | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) | [AI Red Teaming and Continuous Testing cases](../10_Test_Case_Library/D08-ai-red-teaming-and-continuous-testing.md) | India: IRDAI AI-cybersecurity readiness directive (IN8) [Reported] |
| Operational resilience and third-party risk | [AI-CTRL-040](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-040), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) | [TC-L01-018](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-018), [TC-L03-021](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-021) | EU: DORA (E6) [Reported]; Australia: APRA CPS 230 and CPS 234 (AU8) [Recalled] |

Templates: [IN-T3 Regulated-Entity AI Readiness Checklist](../17_India_AI_Compliance/IN-T3_Regulated_Entity_AI_Readiness.md), [EU T02 Impact Assessment](../12_EU_AI_Compliance/T02_Impact_Assessment_FRIA_DPIA.md), [US-T2 Consequential-Decision and Discrimination Impact Assessment](../22_US_AI_Compliance/US-T2_Consequential_Decision_Impact_Assessment.md).

## 3. Health

| Expectation | Wiki controls | Test cases | Regional instruments |
|---|---|---|---|
| Heightened controls for health data | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) | [TC-L03-018](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-018) | EU: GDPR special category data (E2) [Recalled]; US: HIPAA (US12) [Recalled] |
| Classification of AI in medical devices and healthcare | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) | [TC-L03-037](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-037) | EU: AI Act Annex I product law, date reported as 2 August 2028 [Reported]; [South Korea](../20_South_Korea_AI_Compliance/01_South_Korea_AI_Regulatory_Hub.md): healthcare listed as high-impact (KR3) [Conflict]; US: FDA for medical AI (US12) [Recalled] |
| Human oversight of decisions that affect health | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | [TC-L01-012](../10_Test_Case_Library/L01-business-and-use-cases.md#tc-l01-012) | EU: AI Act Art. 14 [Recalled]; South Korea: high-impact AI duties (KR3) [Conflict] |
| Impact assessment before deployment | [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042) | [TC-L03-034](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-034), [TC-L03-010](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-010) | EU: GDPR Art. 35 [Recalled]; South Korea: impact assessment for high-impact AI (KR3) [Conflict] |

Templates: [EU T10 Technical Documentation Index and Conformity Checklist](../12_EU_AI_Compliance/T10_Technical_Documentation_and_Conformity_Checklist.md), [KR-T1 High-Impact AI Determination](../20_South_Korea_AI_Compliance/KR-T1_High_Impact_AI_Determination.md).

Sector rules for health in Japan and the GCC states were not researched.

## 4. Government and public sector

Public bodies, and vendors that sell to them.

| Expectation | Wiki controls | Test cases | Regional instruments |
|---|---|---|---|
| Algorithmic impact assessment with controls set by impact level | [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | [TC-L03-034](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-034), [TC-L03-011](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-011) | Canada: Treasury Board Directive and Algorithmic Impact Assessment (CA4) [Reported]; EU: AI Act Art. 27 for public bodies [Recalled; scope to verify] |
| Published record of algorithmic tools and automated decisions | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | [TC-L03-036](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-036) | UK: Algorithmic Transparency Recording Standard (UK11) [Recalled]; Australia: Privacy Act APP 1.7 to 1.9 (AU2) [Reported] |
| Ethics self-assessment or certification asked for in tenders | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [TC-L02-016](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-016) | GCC: UAE AI Ethics self-assessment (U4) [Reported], Dubai AI Seal (U12) [Unverified] |
| Government AI policy that binds public bodies | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | [TC-L02-001](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-001) | GCC: Bahrain General Policy (B2) [Reported], Oman National AI Policy (O1) [Reported] |
| Data residency and sovereignty | [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007) | [TC-L03-012](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-012), [TC-L03-014](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-014) | GCC: see [Sovereign AI, UAE Compliance and Data Residency Requirements](10_Sovereign_AI_UAE_Compliance_and_Data_Residency.md) |
| Filings and contact with the authority | [AI-CTRL-043](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-043) | [TC-L03-039](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-039) | [China](../16_China_AI_Compliance/01_China_AI_Regulatory_Hub.md): filings with the CAC (CN1, CN2) [Reported]; South Korea: domestic representative (KR5) [Reported] |

Templates: [CA-T1 Algorithmic Impact Assessment Worksheet](../15_Canada_AI_Compliance/CA-T1_Algorithmic_Impact_Assessment_Worksheet.md), [UK-T3 Public-Sector Algorithmic Transparency Record](../21_UK_AI_Compliance/UK-T3_Public_Sector_Transparency_Record.md), [AU-T1 Automated Decision Transparency Register](../13_Australia_AI_Compliance/AU-T1_ADM_Transparency_Register.md), [GCC T07 AI Ethics Self-Assessment Worksheet](../11_GCC_AI_Compliance/T07_Ethics_Self_Assessment_Worksheet.md).
