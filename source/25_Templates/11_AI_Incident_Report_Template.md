---
title: "AI Incident Report Template (.docx)"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Templates"
nav_order: 11
description: "A downloadable Word template for recording one AI incident from detection to closure: summary, what happened, timeline, containment, evidence, notifications with their legal source, root cause across eight factors, impact, actions and closure."
document_type: AI Security Wiki Template
version: 1.0
---

# AI Incident Report Template (.docx)

**[Download the AI Incident Report Template (.docx)](AI_Incident_Report_Template.docx)**

> **Purpose:** Record one AI incident in a consistent way, so that containment, evidence, notifications and lessons are not lost, as [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) asks.

> **Audience:** Incident leads, SOC, AI product owners, data protection officers and legal.

> **Before you rely on it:** Severity levels and response times come from the wiki's illustrative [AI Operating Defaults](../08_Governance/18_AI_Operating_Defaults.md#ai-incident-severity-and-response-times). Notification deadlines are not set by this template: take each one from the law or contract that applies and record its source. This is not legal advice.

## What is in the document

| Section | What it records | Built from |
|---|---|---|
| 1 to 2. Summary and what happened | ID, severity, type, systems and versions involved, description and impact in plain language | [AI Operating Defaults](../08_Governance/18_AI_Operating_Defaults.md#ai-incident-severity-and-response-times) |
| 3. Timeline | Every event and action with time, actor and evidence reference | [D12 AI Incident Response and Forensics](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md) |
| 4. Response | Containment and who authorised it, preserved evidence, provider contact, escalation, and each notification with its legal or contractual source, clock start and deadline | [TC-L03-019](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-019), [TC-D12-016](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-016) |
| 5. Root cause | Model, data, prompt, tool, access, process, vendor and human factors | [TC-D12-020](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-020) |
| 6 to 8. Impact, actions and closure | People, data, money, regulatory and reputational impact; actions with owners and verification; review and closure | [AI Governance Operating Model](../08_Governance/16_AI_Governance_Operating_Model.md#board-level-reporting) |

For jurisdiction-specific notification workflows, see the incident templates in the regional sections, for example [GCC T05](../11_GCC_AI_Compliance/T05_AI_Incident_and_Breach_Notification_Workflow.md), [EU T05](../12_EU_AI_Compliance/T05_AI_Incident_and_Breach_Reporting_Workflow.md) and [India IN-T2](../17_India_AI_Compliance/IN-T2_Breach_and_Incident_Workflow.md). Their legal citations carry the verification tags of their sections.

## Licence and credit

The document is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), like the rest of the wiki. Suggested credit: "AI Incident Report" by Nachiket Sathaye and Ankush Jain, AI Security Wiki, licensed under CC BY-SA 4.0. If you share an adapted version, say what you changed and release it under the same licence.
