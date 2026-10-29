---
title: "Templates"
author: Nachiket Sathaye
coauthors: Ankush Jain
description: "Downloadable .xlsx and .docx templates built from the wiki: an AI risk register, system inventory, use-case triage, vendor scorecard, audit checklist, requirements traceability matrix, security risk review checklist, assurance baseline, control library and crosswalks, test case tracker, acceptable use policy, impact assessment, programme charter and incident report."
nav_order: 15
has_children: true
---

# Templates

This section holds files you can download and fill in. Each one is built from the wiki pages it names, so it stays consistent with them. The ratings and defaults inside a template are examples: replace them with your own before relying on them.

> **How to use:** download the file, read its README and License sheets (or the how-to-use box in a .docx) first, then follow the page that describes it.

| Template | Use it to |
|---|---|
| [AI Risk Register Template (.xlsx)](01_AI_Risk_Register_Template.md) | Assess, treat and track AI risks |
| [AI System Inventory Template (.xlsx)](02_AI_System_Inventory_Template.md) | Keep a record of every AI system, model, agent and AI feature in use |
| [AI Use-Case Risk Triage Template (.xlsx)](03_AI_Use_Case_Risk_Triage_Template.md) | Screen one use case, find the risks that apply and set its tier |
| [AI Security Vendor Evaluation Scorecard (.xlsx)](04_AI_Security_Vendor_Evaluation_Scorecard.md) | Compare AI security products and record due diligence |
| [AI Security Audit and Evidence Checklist Template (.xlsx)](05_AI_Security_Audit_and_Evidence_Checklist_Template.md) | Run a control audit with evidence, findings and exceptions |
| [AI Security Control Library and Crosswalks Template (.xlsx)](06_AI_Security_Control_Library_and_Crosswalks_Template.md) | Track control implementation and framework coverage |
| [AI Security Test Case Tracker Template (.xlsx)](07_AI_Security_Test_Case_Tracker_Template.md) | Plan, run and score AI security tests |
| [AI Acceptable Use Policy Template (.docx)](08_AI_Acceptable_Use_Policy_Template.md) | Draft an AI acceptable use policy |
| [AI Impact Assessment Template (.docx)](09_AI_Impact_Assessment_Template.md) | Assess an AI system's impact on people before go-live |
| [AI Security Programme Charter Template (.docx)](10_AI_Security_Programme_Charter_Template.md) | Set up the AI security and governance programme in one approvable document |
| [AI Incident Report Template (.docx)](11_AI_Incident_Report_Template.md) | Record one AI incident from detection to closure |
| [AI Security Requirements Traceability Matrix Template (.xlsx)](12_AI_Security_Requirements_Traceability_Matrix_Template.md) | Send a scoped set of control requirements to a vendor or system owner and review the answers |
| [AI System Security Risk Review Checklist Template (.xlsx)](13_AI_System_Security_Risk_Review_Checklist_Template.md) | Review one AI system's security risk across its lifecycle and record its impacts and risks |
| [AI Security Assurance Baseline Template (.xlsx)](14_AI_Security_Assurance_Baseline_Template.md) | Send a standalone, domain-organised requirements baseline to a vendor or system owner |

## Data files (CSV)

The same content as plain CSV files, for loading into a GRC tool, a spreadsheet or your own scripts. They are regenerated from the wiki pages every time the site is built, so they always match the pages, and they use the wiki's IDs (AI-R, AI-CTRL and TC), which are never reused. The pages remain the authoritative version.

| File | What it holds | Built from |
|---|---|---|
| [risk_register.csv](data/risk_register.csv) | Every register risk: name, owner domain, example ratings and narrative | [Enterprise AI Risk Register](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) |
| [risk_to_control.csv](data/risk_to_control.csv) | Each risk's primary controls, control IDs and the evidence required | [AI Risk to Control Mapping](../02_Risk_Management/02D_AI_Risk_to_Control_Mapping.md) |
| [controls.csv](data/controls.csv) | Every control objective with its tier, scope and the risks it treats | [Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md) |
| [test_cases.csv](data/test_cases.csv) | Every test case with severity, method and the controls it tests | [Test Case Library](../10_Test_Case_Library/index.md) |
| [ai_risk_map_crosswalk.csv](data/ai_risk_map_crosswalk.csv) | The 55 categories of the AI Risk Map mapped to register risks | [AI Risk Map Crosswalk](../23_Framework_Crosswalks/18_AI_Risk_Map_Crosswalk.md) |

The AI Risk Map crosswalk is adapted from the *AI Risk Map* v1.3 (2026) by Evan Wheeler ([wheels344i-gte/ai-risk-map](https://github.com/wheels344i-gte/ai-risk-map), RiskFramework.org), licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). It maps the map's categories, not its individual factor IDs (AIRM-nnn), because the map's own CSV has not yet been compared with the wiki.
