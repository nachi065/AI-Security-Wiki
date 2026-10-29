---
title: "AI Security Requirements Traceability Matrix Template (.xlsx)"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Templates"
nav_order: 12
description: "A downloadable Excel requirements matrix for the security review of one AI system: every requirement of the wiki's controls, scoped by assurance stage and deployment model, with columns for the vendor's response and the assessor's review and a live dashboard."
document_type: AI Security Wiki Template
version: 1.4
---

# AI Security Requirements Traceability Matrix Template (.xlsx)

**[Download the AI Security Requirements Traceability Matrix Template (.xlsx)](AI_Security_Requirements_Traceability_Matrix.xlsx)**

> **Purpose:** Review the security of one AI system, whether you build it or buy it. Scope the requirements to the review, send them to the vendor or system owner, review what comes back, and report progress and gaps. Each requirement traces to a control in the [Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md), the risks it treats, its test cases and the framework and regional crosswalks.

> **Audience:** Security architects, vendor and third-party risk teams, GRC and assurance teams, and vendors answering a security review.

> **Before you rely on it:** The framework and regional references come from the wiki's crosswalks, which mark many regional sources as reported rather than verified (see [Regulatory Verification Status](../09_Reference/21_Regulatory_Verification_Status.md)). Check them against each source before using the matrix as compliance evidence. In Scope, Mandatory, the assurance stage and the deployment model are starting values: change them to fit your review.

## What is in the workbook

| Sheet | What it holds | Built from |
|---|---|---|
| README and License | How to use the workbook, the assurance stages and deployment models, colour legend, sources, licence, credit and disclaimer | Written for the workbook |
| Dashboard | Live counts: scope, vendor responses, review status, open gaps on mandatory requirements, and breakdowns by assurance stage, deployment model and control family | Calculated from the RTM sheet |
| RTM | One row per requirement: the control, tier, assurance stage, deployment model, evidence required, audit test, risks, test case count, NIST AI RMF, ISO/IEC 42001, OWASP and ISO/IEC 27001 references, and the regional crosswalk rows that name the control. Then In Scope and Mandatory, the vendor's columns, the assessor's columns and a response check | [Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md), [Risk, Control and Test Traceability](../02_Risk_Management/02G_Risk_Control_Test_Traceability.md), [Framework Crosswalks](../23_Framework_Crosswalks/index.md) and the regional Regulatory Crosswalk pages |
| Lists | Dropdown values, including thirteen evidence types | Written for the workbook |

Each sentence of a control's **Implementation Expectation** is one requirement, with an ID such as `AI-CTRL-005.R2`. The matrix therefore holds every requirement the library sets, in the library's own words, and changes when the library changes.

## Who fills in what

| Columns | Filled in by | Values |
|---|---|---|
| In Scope, Mandatory | Assessor, before issuing | Y or N. In Scope starts at Y. Mandatory starts at Y for Baseline-tier controls and N for Advanced-tier controls. |
| Vendor Response, Implementation Details, Evidence Type, Evidence Link | Vendor or system owner | Yes, No, Partial or N/A, with how the requirement is met and where the evidence is |
| Review Status, Assessor Comments, Remediation Owner, Due Date | Assessor | Pending, Accepted, Gap, Risk Accepted or Not Applicable |
| Response Check | Calculated | Flags rows awaiting a response, a Yes or Partial with no detail, a Yes with no evidence link, and a Gap with no owner or due date |

A "Yes" with no implementation detail counts as unanswered.

## How to use it

1. **Scope.** Filter by Assurance Stage (the gate you are at), Deployment Model and Tier. Set In Scope to N on rows that do not apply and adjust Mandatory to your risk appetite.
2. **Issue.** Send the RTM sheet to the vendor or system owner. You can hide the white reference columns first; the regional crosswalk columns are grouped and hidden already.
3. **Collect.** The vendor completes the four blue columns.
4. **Review.** Check each answer and its evidence against the control's Evidence Required and Audit Test Procedure, then set Review Status. Give every Gap a remediation owner and due date.
5. **Report.** Use the Dashboard for progress and gaps. Record accepted risks in the [AI Risk Register Template](01_AI_Risk_Register_Template.md) and approved exceptions under [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037).
6. **Repeat.** Reassess at least annually and on material change, such as a new model or version, a new data source, a new tool or a change in autonomy.

## Assurance stages and deployment models

Every control in the library names the [assurance stage](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#assurance-stages-and-deployment-models) at which a reviewer first checks it (Discovery, Design, Implementation, Platform or Production) and the deployment models it applies to (All, Cloud, or PaaS/IaaS/Self-hosted). The matrix carries both fields for every requirement. For SaaS and AIaaS services, controls marked PaaS/IaaS/Self-hosted are the supplier's to operate: ask for its assurance evidence under [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) instead.

## How it relates to the other templates

| Template | Use it for |
|---|---|
| [AI Security Vendor Evaluation Scorecard](04_AI_Security_Vendor_Evaluation_Scorecard.md) | Comparing several AI security products and shortlisting one |
| This matrix | Reviewing one AI system, bought or built, against every control requirement |
| [AI Security Assurance Baseline](14_AI_Security_Assurance_Baseline_Template.md) | The same kind of review with a standalone, domain-organised requirement set and an optional UAE and Dubai overlay |
| [AI System Security Risk Review Checklist](13_AI_System_Security_Risk_Review_Checklist_Template.md) | Lifecycle review questions with an impact and risk record |
| [AI Security Audit and Evidence Checklist](05_AI_Security_Audit_and_Evidence_Checklist_Template.md) | Testing whether controls operated over an audit period |
| [AI Security Control Library and Crosswalks](06_AI_Security_Control_Library_and_Crosswalks_Template.md) | Tracking which controls your organisation has implemented |

## Licence and credit

The workbook is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), like the rest of the wiki. Its layout follows a requirements matrix that Nachiket Sathaye and Ankush Jain drafted for an AI security review. Suggested credit: "AI Security Requirements Traceability Matrix" by Nachiket Sathaye and Ankush Jain, AI Security Wiki, licensed under CC BY-SA 4.0. If you share an adapted version, say what you changed and release it under the same licence. Framework names, identifiers and short titles belong to their owners and are cited for mapping only.
