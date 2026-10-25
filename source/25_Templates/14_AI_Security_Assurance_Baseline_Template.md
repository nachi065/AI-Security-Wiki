---
title: "AI Security Assurance Baseline Template (.xlsx)"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Templates"
nav_order: 14
description: "A downloadable Excel requirements baseline for the security review of an AI, GenAI or agentic system: 165 testable requirements in 14 domains mapped to ISO/IEC 42001, NIST AI RMF, the EU AI Act and OWASP, with vendor and assessor columns, a dashboard and an optional UAE and Dubai overlay."
document_type: AI Security Wiki Template
version: 1.0
---

# AI Security Assurance Baseline Template (.xlsx)

**[Download the AI Security Assurance Baseline Template (.xlsx)](AI_Security_Assurance_Baseline.xlsx)**

> **Purpose:** Review the security of one AI, GenAI or agentic system, built in-house or bought, against a pick-and-choose set of testable requirements. Scope the baseline to the review, send it to the vendor or system owner, review the evidence that comes back, and report progress and gaps.

> **Audience:** Security architects, vendor and third-party risk teams, GRC and assurance teams, and vendors answering a security review.

> **Before you rely on it:** The framework mappings show the primary alignment for each requirement, not an exhaustive cross-reference; check them against your own control library before using the baseline for compliance reporting. The agentic column uses the T1 to T15 codes of OWASP's "Agentic AI: Threats and Mitigations", not the ASI01 to ASI10 codes of the OWASP Top 10 for Agentic Applications that the wiki's controls use. The optional UAE and Dubai references are domain-level or thematic and have not been checked against the primary texts (see [Regulatory Verification Status](../09_Reference/21_Regulatory_Verification_Status.md)).

## What is in the workbook

| Sheet | What it holds |
|---|---|
| README and License | Purpose, how to scope and issue it, the column legend, caveats, licence, credit and disclaimer |
| Dashboard | Live counts: scope, vendor responses, review status, open gaps on mandatory requirements, and breakdowns by assurance stage, security domain and framework |
| Baseline | 165 requirements in 14 domains, plus one worked example. Each has a stage, a Mandatory flag, the deployment models it applies to, the evidence type and evidence required, and ISO/IEC 42001 Annex A, NIST AI RMF, EU AI Act, OWASP LLM Top 10 (2025) and OWASP agentic threat references |
| UAE and Dubai Overlay | Optional: 15 requirements for an entity under UAE federal or Dubai Government rules, such as information classification, data sovereignty and cloud provider certification, with the UAE and Dubai reference columns |
| UAE and Dubai Mapping | Optional: where each general requirement aligns with UAE and Dubai instruments |
| Lists | Dropdown values, including thirteen evidence types |

The fourteen domains are AI Governance and Accountability; AI Risk and Impact Management; Data Governance and Privacy; Model Lifecycle and Development Security; AI Supply Chain and Third-Party Risk; Prompt and Inference Security; Agentic AI and Tool Use Security; Identity, Access and Secrets Management; Platform and Infrastructure Security; Logging, Monitoring and Detection; Transparency, Explainability and Human Oversight; Incident Response and Resilience; Secure Operations and Change Management; and Legal, Regulatory and Compliance.

## How to use it

1. **Scope.** Filter the Baseline sheet by Stage (the assurance gate you are at), Mandatory, Deployment Applicability or a framework column, and set In Scope to N on rows that do not apply. Delete the two UAE and Dubai sheets if they do not apply to you, or add an overlay sheet for your own jurisdiction in the same layout.
2. **Issue.** Delete the worked example and send the Baseline sheet to the vendor or system owner, who completes the blue columns: response, implementation details, evidence type and evidence link.
3. **Review.** Check each answer and its evidence. A "Yes" with no implementation detail counts as unanswered, and the Response Check column flags it. Set Review Status and record the rationale, gap, remediation owner and date in Comments.
4. **Report.** Use the Dashboard for progress and gaps. Record accepted risks in the [AI Risk Register Template](01_AI_Risk_Register_Template.md).

## How it relates to the other templates

| Template | Use it for |
|---|---|
| This baseline | A standalone, domain-organised requirement set to send to a vendor or system owner |
| [AI Security Requirements Traceability Matrix](12_AI_Security_Requirements_Traceability_Matrix_Template.md) | The same kind of review when you work from the wiki's {{n:controls}} controls: every requirement traces to the wiki's risks, test cases and regional crosswalks |
| [AI System Security Risk Review Checklist](13_AI_System_Security_Risk_Review_Checklist_Template.md) | Review questions across the lifecycle, with an impact and risk record |
| [AI Security Vendor Evaluation Scorecard](04_AI_Security_Vendor_Evaluation_Scorecard.md) | Comparing several AI security products and shortlisting one |

## Licence and credit

Written by Nachiket Sathaye and Ankush Jain for AI security reviews, and made region-neutral for the wiki in October 2026: the UAE and Dubai requirements and references moved to optional sheets. The workbook is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), like the rest of the wiki. Suggested credit: "AI Security Assurance Baseline" by Nachiket Sathaye and Ankush Jain, AI Security Wiki, licensed under CC BY-SA 4.0. If you share an adapted version, say what you changed and release it under the same licence. Framework names, identifiers and short titles belong to their owners and are cited for mapping only.
