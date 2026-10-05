---
title: "Custom AI Application Runtime Security Standard"
parent: "Domain Standards"
nav_order: 3
document_type: AI Security Wiki Reference
version: 1.0
---

# Custom AI Application Runtime Security Standard

> **Purpose:** Define security controls for internal AI applications, RAG systems, AI APIs and AI-enabled business applications.

> **Audience:** AI product developers, AppSec, DevSecOps, cloud architects, AI platform engineers, red teamers.

> **How to use:** Use this page as a wiki reference. Update the evidence, owners, control status, and links as implementation maturity improves.


## Scope

This standard applies to internal AI assistants, enterprise knowledge chatbots, RAG implementations, Azure OpenAI or similar AI APIs, customer-facing AI services, AI-enabled portals and AI applications connected to enterprise repositories or business systems.

## Required Security Gates

| Gate | Requirement | Evidence |
|---|---|---|
| Input Security | Prompt injection and malicious input testing completed. | Red team results, test cases |
| Retrieval Security | Source permissions and retrieval boundaries validated. | Permission test evidence, retrieval logs |
| Output Security | Sensitive output filtering and response governance enabled. | Output inspection logs |
| API Security | Authentication, authorization, rate limits and API logging enforced. | API gateway policy evidence |
| Data Protection | Data minimization and classification-aware controls implemented. | Data flow and classification evidence |
| Logging | Prompts, responses, retrieved sources, user context and model/API calls logged based on policy. | Audit export, log samples |
| SOC Integration | Alerts integrated with monitoring and response workflows. | SIEM event IDs |
| Production Approval | Security review completed before production. | Approval record |

## Runtime Threat Scenarios

- Direct prompt injection.
- Indirect prompt injection through retrieved documents.
- Unauthorized retrieval from internal knowledge sources.
- Sensitive output leakage.
- AI API abuse.
- Weak authorization between AI application and backend data source.
- Untrusted plugin, library or model dependency.

## Production Readiness Checklist

- [ ] AI application owner assigned.
- [ ] Data classification completed.
- [ ] RAG source repositories approved.
- [ ] Authentication and authorization reviewed.
- [ ] Prompt injection testing completed.
- [ ] Output leakage testing completed.
- [ ] Logging and retention defined.
- [ ] SOC alerting enabled.
- [ ] Vendor or model processing terms reviewed.
- [ ] Residual risk accepted by owner.
