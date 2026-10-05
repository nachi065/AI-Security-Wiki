---
title: "AI Risk Methodology"
parent: "Risk Management"
nav_order: 1
document_type: AI Security Wiki Reference
version: 1.0
---

# AI Risk Methodology

> **Purpose:** Define the rating method for assessing AI risks consistently across AI platforms, custom AI applications and agentic AI workflows.

> **Audience:** Risk management, security architecture, GRC, audit, AI product owners.

> **How to use:** Use this page as a wiki reference. Update the evidence, owners, control status, and links as implementation maturity improves.


## Rating Factors

| Factor | Definition |
|---|---|
| Likelihood | Probability of the risk occurring based on exposure, adoption, control maturity and user behavior. |
| Impact | Consequence to confidentiality, integrity, availability, compliance, operational continuity, reputation or critical infrastructure. |
| Existing Control Coverage | Current ability of existing controls to prevent, detect, respond or provide evidence. |
| Residual Risk | Remaining risk after considering current control coverage. |
| Additional Control Requirement | Whether AI-specific controls, governance, monitoring or enforcement are required. |

## Risk Scale

| Rating | Definition |
|---|---|
| Low | Limited likelihood or business impact; existing controls generally sufficient. |
| Medium | Possible risk affecting sensitive information, compliance or business processes; monitoring or governance may be required. |
| High | Likely or significant impact; additional controls, monitoring or enforcement required. |
| Critical | May affect critical infrastructure, restricted data, regulatory obligations or operational continuity; strong preventive and detective controls required. |

## Required Fields for New AI Risk Entry

```markdown
Risk ID:
Risk Name:
AI Channel:
Risk Description:
Example Scenarios:
Potential Impact:
Existing Controls:
Likelihood:
Impact:
Existing Control Coverage:
Residual Risk:
Required AI Security Capabilities:
Evidence Required:
Risk Owner:
Treatment Decision:
Review Date:
```

## Review Triggers

- New AI vendor onboarding.
- New AI integration with enterprise data.
- AI coding assistant adoption.
- New RAG or custom AI application.
- Agentic AI workflow or tool-calling capability.
- Regulatory, audit or third-party risk review.
