---
title: "Browser AI Security Standard"
author: Nachiket Sathaye
parent: "Domain Standards"
nav_order: 1
document_type: AI Security Wiki Reference
version: 1.0
---

# Browser AI Security Standard

> **Purpose:** Set security requirements for users accessing browser-based AI platforms such as public or enterprise generative AI services.

> **Audience:** Security engineering, DLP teams, endpoint teams, SOC, AI users, compliance.

> **How to use:** Use this page as a wiki reference. Update the evidence, owners, control status, and links as implementation maturity improves.

| Control Area | Weight | Required Evidence |
|---|---|---|
| Discovery and Visibility | 15% | AI service inventory, user activity reports, device attribution |
| Prompt Inspection | 20% | Sensitive prompt detection logs and policy outcomes |
| File Upload Inspection | 15% | Upload inspection test results and block/warn evidence |
| Policy Enforcement | 15% | Allow, alert, warn, mask, redact or block policy evidence |
| Auditability | 15% | User, device, AI platform, prompt and file upload logs |
| Platform Coverage | 10% | Browser and OS support matrix |
| Operational Impact | 10% | Deployment notes, performance observations, administrative effort |

## Minimum Requirements

- Discover AI platforms accessed from managed endpoints.
- Identify users, devices and browser context.
- Inspect prompts where technically feasible.
- Inspect uploaded files including documents, spreadsheets, PDFs, images and code files where technically feasible.
- Apply classification-aware monitor/warn/redact/block controls.
- Generate investigation-ready audit records.
- Forward AI security events to SOC/SIEM.

## PoC Tests

1. Upload confidential document to public AI platform.
2. Paste architecture details into AI prompt.
3. Upload source code to AI chatbot.
4. Attempt upload of classified information.
5. Access newly emerging or previously unknown AI website.

## Audit Evidence

- AI service inventory export.
- Screenshots of policy enforcement decisions.
- Logs showing user, endpoint, browser, AI site, action and timestamp.
- SIEM event ID or SOC alert reference.
