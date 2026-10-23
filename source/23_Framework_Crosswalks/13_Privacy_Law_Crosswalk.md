---
title: "Privacy Law Crosswalk"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Framework Crosswalks"
nav_order: 13
description: "Eight privacy laws compared by the themes that matter for AI systems, with the wiki control objectives for each theme: GDPR, CCPA, Quebec Law 25, Singapore PDPA and the UAE, Saudi, Qatar and Bahrain data protection laws."
document_type: AI Security Wiki Reference
version: 1.0
---

# Privacy Law Crosswalk

> **Purpose:** Let a team that runs AI systems across several jurisdictions see, theme by theme, where eight privacy laws ask for the same thing and where they differ, and which wiki controls answer each theme.

> **Audience:** Privacy and data protection officers, legal and compliance teams, GRC teams, AI product owners.

> **How to use:** Find the theme in the first column, read across to the laws that apply to you, then open the wiki controls in the last column. Each law's ID (for example E2 or U1) is its row in the regional crosswalk, which records the instrument's legal force and verification status.

> **Verification required.** Every provision number on this page is [Recalled]: stated from memory of the law and not checked against the primary text. Cells marked [Unverified] are less certain still. "Not researched" means this wiki has no information, which is different from the law being silent. Implementing regulations and regulator guidance change the detail in every one of these laws. Check the primary text before relying on any cell. This is not legal advice.

## The eight laws

| Law | Jurisdiction | Regional row | Regional section |
|---|---|---|---|
| General Data Protection Regulation (GDPR), Regulation (EU) 2016/679 | European Union | E2 | [EU Regulatory Crosswalk](../12_EU_AI_Compliance/07_Regulatory_Crosswalk.md) |
| California Consumer Privacy Act (CCPA), as amended, with its regulations | California, US | US8 | [US Regulatory Crosswalk](../22_US_AI_Compliance/03_Regulatory_Crosswalk.md) |
| Quebec Law 25, which amended the Act respecting the protection of personal information in the private sector | Quebec, Canada | CA3 | [Canada Regulatory Crosswalk](../15_Canada_AI_Compliance/03_Regulatory_Crosswalk.md) |
| Personal Data Protection Act 2012 (PDPA) | Singapore | SG4 | [Singapore Regulatory Crosswalk](../19_Singapore_AI_Compliance/03_Regulatory_Crosswalk.md) |
| Federal Decree-Law 45/2021 (UAE PDPL) | United Arab Emirates, outside the DIFC and ADGM | U1 | [GCC Regulatory Crosswalk](../11_GCC_AI_Compliance/07_Regulatory_Crosswalk.md) |
| Personal Data Protection Law (Saudi PDPL) | Saudi Arabia | S1 | [GCC Regulatory Crosswalk](../11_GCC_AI_Compliance/07_Regulatory_Crosswalk.md) |
| Law 13/2016 on personal data privacy protection (Qatar PDPPL) | Qatar, outside the Qatar Financial Centre | Q1 | [GCC Regulatory Crosswalk](../11_GCC_AI_Compliance/07_Regulatory_Crosswalk.md) |
| Law 30/2018 (Bahrain PDPL) | Bahrain | B1 | [GCC Regulatory Crosswalk](../11_GCC_AI_Compliance/07_Regulatory_Crosswalk.md) |

The DIFC and ADGM free zones in the UAE have their own data protection laws (rows U6 and U7). DIFC Regulation 10 sets duties for autonomous and semi-autonomous systems that the federal law does not. They are not compared here.

## European Union, California, Quebec and Singapore

| Theme | GDPR | CCPA | Quebec Law 25 | Singapore PDPA | Wiki controls |
|---|---|---|---|---|---|
| Automated decisions about individuals | Art. 22: a right not to be subject to a solely automated decision with legal or similarly significant effect, with exceptions and safeguards | Regulations on automated decision-making technology: pre-use notice, opt-out and access for significant decisions; see row US8 for dates | s. 12.1: tell the person when a decision is made only by automated processing, explain it on request, and let them have it reviewed by a person | No specific right. The PDPC advisory guidelines on AI recommendation and decision systems apply the general obligations | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041), [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045) |
| Impact assessment before risky processing | Art. 35: data protection impact assessment for high-risk processing | Risk assessment regulations; see row US8 for dates | s. 3.3: privacy impact assessment for any project that acquires, develops or redesigns a system that handles personal information | No general duty. An assessment is required to rely on deemed consent by notification or on the legitimate interests exception | [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042) |
| Breach notification | Arts. 33 and 34: to the authority within 72 hours, and to individuals when the risk is high | Not in the CCPA itself. California's breach notice statute (Civil Code s. 1798.82) applies, and s. 1798.150 gives a private right of action after some breaches | ss. 3.5 to 3.8: report a confidentiality incident that presents a risk of serious injury, and keep a register of all incidents | Part 6A: notify the PDPC within 3 calendar days of assessing a breach as notifiable | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035), [AI-CTRL-043](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-043) |
| Transfers outside the jurisdiction | Chapter V (Arts. 44 to 49): adequacy decision, safeguards or a derogation | No restriction on transfers abroad | s. 17: privacy impact assessment before personal information leaves Quebec | s. 26: the recipient must give comparable protection | [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007) |
| Retention and deletion | Art. 5(1)(e) storage limitation; Art. 17 erasure | Disclose retention periods and keep data no longer than reasonably necessary; right to delete | s. 23: destroy or anonymize when the purpose is met | s. 25: stop retaining when the purpose no longer needs it. There is no right to erasure | [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) |
| Requests from individuals | Arts. 15 to 21: access, rectification, erasure, restriction, portability and objection | Rights to know, delete, correct, and opt out of sale or sharing | ss. 27 to 28.1: access, rectification, and an end to dissemination | ss. 21 and 22: access and correction | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) |
| Vendors that process the data | Art. 28: processor contract with set terms | Written contract with each service provider and contractor | s. 18.3: written agreement with the service provider | Data intermediaries carry the protection, retention and breach duties directly; the organization stays responsible | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) |

## United Arab Emirates, Saudi Arabia, Qatar and Bahrain

| Theme | UAE PDPL | Saudi PDPL | Qatar PDPPL | Bahrain PDPL | Wiki controls |
|---|---|---|---|---|---|
| Automated decisions about individuals | Art. 18: a right to object to decisions made by automated processing that have legal or serious effects | Not researched | Not researched | Art. 22: a right to object to decisions based only on automated processing [Unverified] | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041), [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045) |
| Impact assessment before risky processing | Art. 21: data protection impact assessment for high-risk processing | Required by the Implementing Regulation in listed cases [Unverified] | Expected by the regulator's guidelines [Unverified] | No impact assessment recalled. Some processing needs prior notice to, or authorization from, the Authority [Unverified] | [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042) |
| Breach notification | Art. 9: to the Data Office, and to individuals where their privacy is at risk. The period is left to the Executive Regulation | Art. 20, with 72 hours to the authority under the Implementing Regulation | Art. 14: to the authority and the individual when serious damage may follow [Unverified] | Not researched | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035), [AI-CTRL-043](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-043) |
| Transfers outside the jurisdiction | Arts. 22 and 23: adequate protection, or a listed exception | Art. 29 and the transfer regulation | Art. 15 [Unverified] | Arts. 12 and 13: adequate countries listed by the Authority, or its authorization [Unverified] | [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007) |
| Retention and deletion | Art. 5: keep no longer than the purpose needs; Art. 15 erasure | Art. 18: destroy when the purpose ends | Not researched | Not researched | [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) |
| Requests from individuals | Arts. 13 to 18 | Art. 4 | Not researched | Not researched | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) |
| Vendors that process the data | Art. 8: processor duties | Art. 8: the controller must choose a processor that gives guarantees and stays responsible | Not researched | Not researched | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) |

The GCC hub records open questions for these laws: the UAE Executive Regulation is reported as pending, and sources conflict on Saudi enforcement dates. See the [GCC AI Regulatory Hub](../11_GCC_AI_Compliance/01_GCC_AI_Regulatory_Hub.md).

## What the comparison shows

A programme built to the strictest cell in each row covers most of the others. For AI systems that usually means:

- For automated decisions, tell the person, be able to explain the decision, and offer review by a person. Quebec asks for all three, and the GDPR and California regulations get there by other routes. [CA-T2](../15_Canada_AI_Compliance/CA-T2_Quebec_Law_25_ADM_Record.md) is a record for one decision system.
- Do an impact assessment before deployment for any AI system that handles personal data and affects people. [EU T02](../12_EU_AI_Compliance/T02_Impact_Assessment_FRIA_DPIA.md) combines the data protection assessment with the AI Act's fundamental rights assessment.
- Plan breach notification for 72 hours. Singapore's 3 calendar days run from the assessment of the breach, so the clock can start later than the GDPR's. The [EU](../12_EU_AI_Compliance/T05_AI_Incident_and_Breach_Reporting_Workflow.md) and [GCC](../11_GCC_AI_Compliance/T05_AI_Incident_and_Breach_Notification_Workflow.md) workflows set out the steps.
- Record where prompts, logs and training data go for every AI vendor. California has no transfer rule, and the other seven laws each have one. The [EU T04](../12_EU_AI_Compliance/T04_Data_Location_and_Transfer_Record.md) and [GCC T04](../11_GCC_AI_Compliance/T04_Data_Residency_Attestation.md) templates hold the record.

Deletion is where the laws differ most for AI. A right to erasure under the GDPR or the CCPA raises the question of personal data already used to train a model. Singapore has no erasure right at all.

## What this page does not cover

- Other privacy laws that the regional sections list, among them the UK GDPR, Brazil's LGPD, India's DPDP Act, China's PIPL, Japan's APPI and Australia's Privacy Act. Each has a row in its own regional crosswalk.
- Sector privacy rules such as HIPAA. See the [Sector Overlays](../04_Domain_Standards/10B_Sector_Overlays.md).
- Lawful basis for training a model on personal data, which turns on facts and regulator guidance more than on the text of the law.

## Related pages

- [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md)
- [Sovereign AI, UAE Compliance and Data Residency Requirements](../04_Domain_Standards/10_Sovereign_AI_UAE_Compliance_and_Data_Residency.md)
- [Sector Overlays](../04_Domain_Standards/10B_Sector_Overlays.md)
- [SOC 2 Crosswalk](11_SOC_2_Crosswalk.md), for the privacy criteria
