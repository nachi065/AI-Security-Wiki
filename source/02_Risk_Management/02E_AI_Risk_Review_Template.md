---
title: "AI Risk Review Template"
author: Nachiket Sathaye
parent: "Risk Management"
nav_order: 5
document_type: AI Security Wiki Reference
version: 1.0
---

# AI Risk Review Template

> **Purpose:** Provide a reusable intake and risk review template for new AI tools, AI applications, AI vendors and agentic AI workflows.

> **Audience:** AI product owners, solution architects, security reviewers, GRC.

## AI Risk Review Intake

```markdown
Project / Tool Name:
Business Owner:
Technical Owner:
Security Reviewer:
Vendor / Platform:
AI Use Case:
Deployment Model:
Users / Departments:
Data Types Processed:
Data Classification:
External Processing Required: Yes / No
Custom AI Application: Yes / No
RAG / Retrieval Used: Yes / No
Agentic Tool Calling Used: Yes / No
Production Target Date:
```

## Required Review Questions

1. What data will be submitted to the AI system?
2. Will users upload documents, code, logs, images or spreadsheets?
3. Are prompts or uploads retained by the vendor?
4. Is customer or employee data processed?
5. Is source code or infrastructure data involved?
6. Are AI APIs integrated with enterprise applications?
7. Does the AI system retrieve data from internal repositories?
8. Can the AI system perform actions, call tools or trigger workflows?
9. Are prompts, responses, source documents and tool calls logged?
10. Can audit evidence be exported for investigation?
11. Where is data processed and stored?
12. Is customer data excluded from model training?

## Approval Decision

```markdown
Approved / Conditionally Approved / Rejected:
Conditions:
Required Controls:
Residual Risk:
Risk Owner:
Review Date:
Next Review Date:
```
