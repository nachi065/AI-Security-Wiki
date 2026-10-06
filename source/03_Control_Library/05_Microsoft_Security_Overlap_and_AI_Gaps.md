---
title: "Microsoft Security Overlap and AI Gaps"
author: Nachiket Sathaye
parent: "Control Library"
nav_order: 3
document_type: AI Security Wiki Reference
version: 1.0
---

# Microsoft Security Overlap and AI Gaps

> **Purpose:** Show, for organizations that use Microsoft security products, where those capabilities generally help with AI governance and where dedicated AI controls may still be required.

> **Audience:** Microsoft security administrators, Purview/DLP teams, Defender teams, Sentinel/SOC teams, procurement and governance.

> **How to use:** Use this page as a template. Confirm which products and features are actually licensed and deployed in your environment, and validate each gap before using it in a vendor evaluation.

> **Illustrative example:** This page describes general product capabilities, not the deployment or gaps of any specific organization. The same analysis applies to any other incumbent security stack.

| Area | General Microsoft Capability | Common AI-Specific Gap | Vendor Evaluation Focus |
|---|---|---|---|
| Identity | Authentication, MFA, Conditional Access, RBAC, privileged access | Agent identity and tool-level authorization | Validate integration with identity controls |
| Purview / Information Protection | Classification, labels, encryption, governance | Prompt and output context across AI channels | Validate classification-aware AI enforcement |
| DLP | Endpoint, cloud and email DLP | IDE prompts, AI APIs, browser AI uploads may need validation | Validate AI-specific data leakage controls |
| Defender for Cloud Apps / SaaS Governance | SaaS visibility and shadow IT discovery | Deep AI prompt inspection and AI-specific classification | Validate AI service discovery and policy depth |
| Sentinel / SOC | Centralized monitoring and investigation | AI-specific telemetry and prompt/tool context | Validate alert enrichment and forensic evidence |
| Power Platform Governance | Governance of low-code/platform apps | Agentic AI and tool-calling governance | Validate agent/tool controls |

## Procurement Guidance

Vendors should be scored higher only where they provide measurable AI-specific capabilities beyond the incumbent Microsoft controls. If a vendor capability overlaps with controls already in place, require evidence that it provides deeper AI context, broader channel coverage, better enforcement, more complete auditability or improved operational integration.
