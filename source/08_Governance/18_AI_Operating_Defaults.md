---
title: "AI Operating Defaults"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Governance"
nav_order: 3
description: "Illustrative starting values for running an AI security programme: exception limits, incident severity and response times, monitoring thresholds, a review and audit calendar, CI/CD release stages and a log retention baseline."
document_type: AI Security Wiki Reference
version: 1.0
---

# AI Operating Defaults

> **Purpose:** Give a programme the concrete numbers it needs on day one (how long an exception may last, how fast to respond to an incident, when a monitoring signal needs action, what to review when, which pipeline checks block a release and how long to keep which logs) so that teams are not left to invent them one by one.

> **Audience:** AI governance leads, GRC, security operations, platform and MLOps teams.

> **Illustrative example:** Every number on this page is a starting value chosen for this wiki. None is taken from a standard or a law, and none has been tested against your systems. Agree each one, record who approved it, and replace any that a law, regulator, contract or your own risk appetite sets differently. Where a law sets a deadline or a period, the law wins; see the regional section for that jurisdiction.

## Exceptions and Risk Acceptance

An exception lets a system run without meeting a control, for a fixed time, with a compensating measure. A risk acceptance records that a residual risk is tolerated. Both expire. The acceptance periods below repeat the [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md#scoring-method); the exception limits are shorter because an exception means a known control is missing.

| Rating of the risk the missing control treats | Who approves the exception | Longest exception | Renewals allowed | Compensating measure | Longest risk acceptance |
|---|---|---|---|---|---|
| Low | GRC / Compliance | 6 months | 2 | Recommended | 12 months |
| Medium | GRC / Compliance | 6 months | 1 | Required | 12 months |
| High | AI Governance Committee | 3 months | 1 | Required, and tested | 6 months |
| Critical | Governing body or accountable executive, on the committee's recommendation | 1 month | None; redesign or stop | Required, tested and monitored | 3 months |

- An exception record names the control, the system, the reason, the compensating measure, the owner and the expiry date ([TC-L02-010](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-010)).
- On expiry the exception lapses; it is not renewed by silence. Where possible, enforce the expiry in the technical control itself ([TC-L02-011](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-011)).
- Report open exceptions, their age and any system with more than three open exceptions to the AI Governance Committee each month ([TC-L02-012](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-012)).
- No exception is granted for a prohibited use, or for a decision reserved for the governing body.

## AI Incident Severity and Response Times

Classify an AI incident by its worst current or credible effect, and reclassify as facts change. The response times are internal targets measured from the time the incident is declared. They do not replace any notification deadline that a law or contract sets: track those separately, from the moment the law says the clock starts ([TC-L03-019](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-019), [TC-D12-016](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-016)).

| Severity | Examples | Acknowledge | Contain | Escalate to | Status updates |
|---|---|---|---|---|---|
| SEV 1 Critical | An agent taking harmful actions in production systems; restricted or special-category personal data exposed through an AI system; AI output causing harm to people at scale; a compromised model or tool server in production | 15 minutes | 4 hours | Accountable executive, Legal, Data Protection Officer; governing body if material | Every 2 hours until contained |
| SEV 2 High | Confirmed prompt injection that reached data or tools without lasting harm; confidential data sent to an unapproved AI service in bulk; a high-impact decision system found outside its validated boundaries | 1 hour | 24 hours | AI Governance Committee chair, Data Protection Officer if personal data is involved | Daily |
| SEV 3 Medium | Guardrail bypass with no data reached; repeated policy violations by one user; a quality failure affecting a small number of users; runaway cost stopped by a budget limit | 4 business hours | 5 business days | System owner and risk owner | Weekly |
| SEV 4 Low | Blocked attacks and near misses; single policy violations; minor quality issues | 2 business days | Next planned release | System owner | In the monthly report |

- **Stop first when people or money are at risk.** For SEV 1, anyone named as able to stop the system may do so without waiting for approval ([AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025)); see [Decision Rights](16_AI_Governance_Operating_Model.md#decision-rights).
- **Preserve before you fix.** Capture prompts, context, retrieved content, tool calls, model and prompt versions, index snapshots and agent memory before changing them ([AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035)).
- **Review afterwards.** SEV 1 and SEV 2 incidents get a post-incident review within 10 business days, with root causes across model, data, prompt, tool, access, process, vendor and human factors ([TC-D12-020](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-020)). Record each incident on the [AI Incident Report Template (.docx)](../25_Templates/11_AI_Incident_Report_Template.md).

## Monitoring Thresholds

Each threshold is a point at which someone must look, not proof of an attack or a failure. Set a baseline over the first two to four weeks of normal use, then alert on change from that baseline. Tune the numbers once you know your false-positive rate. Classic predictive models have their own signals; see [Predictive Model Monitoring and Adversarial ML](../04_Domain_Standards/11_Predictive_Model_Monitoring_and_Adversarial_ML.md).

| Signal | Applies to | Look when | Act when |
|---|---|---|---|
| Prompt injection or jailbreak detections | Assistants, RAG applications, agents | Daily count is more than twice the baseline | Any detection followed by a tool call or data access, or more than 20 from one user or source in an hour |
| Guardrail or policy block rate | Any filtered AI service | Rate moves more than 50 percent from baseline in a week | A sudden fall to near zero (the guardrail may have stopped working) or a sustained rise |
| Sensitive data in prompts or uploads | Workforce AI tools | Any restricted data, or a rise of more than 50 percent in a week | Restricted or special-category data sent to an unapproved service |
| Tool calls denied by policy | Agents | More than 5 percent of an agent's calls in a day | Any denied attempt at an irreversible action, or a new tool the agent was not granted |
| Human approval decisions | Agents with approval steps | Approval rate above 98 percent, or median decision time under 5 seconds | Either for two weeks running (approvals may be rubber-stamped; see [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045)) |
| Spend and token use | Every AI application, key and agent | 80 percent of the monthly budget, or daily spend three times the baseline | 100 percent of budget, or an hourly spike that suggests a loop or a leaked key ([AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036)) |
| Quality failures (wrong answers, wrong tool choices) | Assistants and agents | Evaluation score falls more than 5 points from the release baseline, or user-reported errors double | A regression on a safety or high-impact test set, whatever the size |
| Model or provider change | Any third-party model | Any new model version or provider notice | Before switching: rerun the release evaluation and adversarial tests |
| Telemetry health | All AI event sources | A source silent for more than 1 hour | A source silent for more than 4 hours, or log volume down more than 50 percent without a known reason ([TC-L17-028](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-028)) |

## Review and Audit Calendar

### Programme activities

| When | Activity | Owner | Source in this wiki |
|---|---|---|---|
| Monthly | AI Governance Committee meeting; open exceptions and their age; SEV 1 and SEV 2 incidents | Committee chair | [AI Governance Operating Model](16_AI_Governance_Operating_Model.md#committee-charters) |
| Monthly | Shadow AI discovery results and unapproved tools | Security | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) |
| Quarterly | Report to the governing body | Accountable executive | [Board-Level Reporting](16_AI_Governance_Operating_Model.md#board-level-reporting) |
| Quarterly | Risk register review: High and Critical risks, overdue treatments, expiring acceptances | Risk owners, GRC | [AI Risk Review Template](../02_Risk_Management/02E_AI_Risk_Review_Template.md) |
| Quarterly | Agent and tool grant recertification | Agent sponsors | [Agent and Non-Human Identity Governance](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md) test domain |
| Quarterly | Authority register and pending rules watchlist | Legal / Compliance | [AI-CTRL-043](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-043) |
| Semi-annually | Human oversight measures for high-tier use cases | AI governance lead | [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045) |
| Annually | AI policy, risk appetite, these operating defaults and both committee charters | Governing body, accountable executive | [AI Policy, Standards and Acceptable Use](17_AI_Policy_Standards_and_Acceptable_Use.md) |
| Annually | Assessor calibration on the worked examples | GRC | [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md#calibrating-assessors) |
| Annually | Impact assessments and bias tests for in-scope systems, even without a change | Data Protection Officer, model risk | [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042), [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) |
| Annually | AI incident tabletop exercise | SOC | [TC-L17-018](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-018) |
| Annually | Role-based training and its effectiveness check | AI governance lead, HR | [Role-Based Training Plan](16_AI_Governance_Operating_Model.md#role-based-training-plan) |
| Annually | Internal audit of the AI controls, using the audit checklist | Internal audit | [AI Security Audit and Evidence Checklist](../06_Testing_and_Assurance/14_AI_Security_Audit_and_Evidence_Checklist.md) |

### Control reviews

The table below is generated from the Review Frequency of each record in the [Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md), so it changes when the library does.

<!-- review-calendar -->

## CI/CD Release Stages for AI Applications

Which checks run where, whether they are automated, and whether a failure stops the release. "Blocks" means the pipeline stops until the issue is fixed or an exception is approved under the limits above. The stages apply to applications, agents, prompts and configuration, and to fine-tuned or self-hosted models. [TC-L14-002](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-002) tests the gates.

| Stage | Check | Automated | Blocks release | Control |
|---|---|---|---|---|
| Commit | Secrets in code, prompts, notebooks and configuration | Yes | Yes | [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030) |
| Commit | Prompts and agent configuration changed only through reviewed pull requests | Yes | Yes | [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030) |
| Build | Dependency scan of ML libraries and serving images; packages that do not exist or were recently registered | Yes | Yes for Critical and High findings | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) |
| Build | Model file scan (unsafe serialization) and provenance; AI-BOM generated | Yes | Yes | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) |
| Build | Sign models, containers and prompt bundles | Yes | Yes if signing fails | [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030) |
| Test | Evaluation suite: quality, safety and task success against the release baseline | Yes | Yes on a regression in a safety or high-impact set; otherwise warn | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) |
| Test | Adversarial tests (prompt injection, jailbreak, data leakage, tool misuse), including the [payload kit](../10_Test_Case_Library/payload-kit.md) cases that apply | Yes | Yes if a previously passing case fails | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) |
| Test | Bias test for high-impact decision systems | Partly | Yes if an approved threshold fails | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) |
| Release | Security review and release gate record, including the agent's tool grants and approval steps | No | Yes | [AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033) |
| Release | Impact assessment current and approved, where required | No | Yes | [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042) |
| Deploy | Signature verified and admission policy checked | Yes | Yes | [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030) |
| Deploy | Staged rollout with a tested rollback and kill switch | Partly | Yes if rollback is not tested | [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) |
| Operate | Monitoring signals above, and scheduled re-runs of the evaluation and adversarial suites | Yes | No; raises an incident or a change | [AI-CTRL-009](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009) |

## Log Retention Baseline

Which AI records to keep, and a default minimum period. Two limits pull against each other: investigations, audits and some laws need records kept, while data protection laws require personal data to be kept no longer than needed. So keep the security metadata longer than the content, mask personal data where you can, and apply legal holds instead of keeping everything for everyone ([TC-L17-005](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-005), [TC-L03-027](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-027)). Some laws set minimum log retention for certain AI systems; the EU AI Act does for high-risk systems. Check the period that applies to you in the regional section before adopting these defaults.

| Record | What it holds | Default minimum | Notes |
|---|---|---|---|
| AI security events | Detections, policy decisions, blocks, guardrail results, alerts | 12 months searchable | Long enough to look back over a year of activity during an investigation |
| Agent actions and tool calls | Agent identity, tool, arguments, decision (executed, blocked, pending), approver | 12 months | Needed to reconstruct what an agent did and who approved it |
| Prompts and responses | Full content of interactions | 90 days, masked where possible | Shortest that supports investigation; extend under legal hold only |
| Retrieved content references | Which documents or records were retrieved for each response | 12 months (references, not copies) | Lets an investigation show what the model saw without keeping the content twice |
| Administrative and configuration changes | Changes to models, prompts, guardrails, tool grants, retention settings | 3 years | Change history is evidence for audits across several cycles |
| Model and data lineage | Model versions, training and fine-tuning datasets, evaluations, approvals | Life of the model plus 3 years | Needed to answer questions about a model after it is retired |
| Human oversight records | Review decisions, overrides, escalations, time per review | 3 years | Evidence that oversight worked ([AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045)) |
| Incident records and evidence | Case file, preserved artefacts, chain of custody | 5 years after closure, or longer under legal hold | |
| Tracing and evaluation platforms | Full traces used by engineers | 30 days | Often hold full prompts with wider access; keep short ([TC-L17-032](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-032)) |

Keep logs where they cannot be altered by the people whose actions they record, in the approved location for the data they contain ([AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007)).
