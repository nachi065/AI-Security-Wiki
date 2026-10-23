---
title: "AI Governance Operating Model"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Governance"
nav_order: 1
document_type: AI Security Wiki Reference
version: 1.1
---

# AI Governance Operating Model

> **Purpose:** Define ownership, gates, workflow, reporting and continuous governance for AI adoption.

> **Audience:** Governance, compliance, security leadership, architecture review boards, AI steering committee.

| Gate | Applies To | Required Review |
|---|---|---|
| Gate 1 | Any AI tool | AI usage and data handling review |
| Gate 2 | AI with sensitive data | DLP, classification and data protection review |
| Gate 3 | Custom AI application | AppSec, prompt injection and runtime review |
| Gate 4 | Agentic AI | Tool, API, approval workflow and privilege review |
| Gate 5 | Vendor AI platform | Sovereignty, third-party processing and procurement review |
| Gate 6 | Production AI | Audit logging, SOC integration and evidence readiness review |

## Governance Bodies

| Function | Responsibility |
|---|---|
| Governing body (board, or its risk or audit committee) | Set the organization's AI risk appetite, approve the categories of AI use that are prohibited or high-risk, and oversee AI risk, compliance and data quality through regular reporting. Accountability stays with the governing body when decisions are automated. |
| Accountable executive | Own AI governance on behalf of the governing body, chair or sponsor the AI governance committee, and report AI risk, incidents and exceptions upward. |
| AI Governance Committee | Approve high-risk use cases, risk acceptances and exceptions; review impact assessments; track maturity against this operating model. |
| Data Owner (AI datasets) | Own the quality, provenance and permitted use of each dataset used to train, fine-tune or ground an AI system, and approve its data quality thresholds. |
| AI Product Owner | Define use case, data scope and business justification. |
| Security Architecture | Review AI design, controls, integrations and residual risk. |
| GRC / Compliance | Validate policy, regulatory, audit and sovereignty requirements. |
| Data Protection / DLP | Validate data classification and leakage controls. |
| AppSec / DevSecOps | Validate custom AI application and AI-assisted development controls. |
| SOC | Validate alerting, logging, investigation and monitoring. |
| Procurement / Legal | Validate vendor terms, data processing, residency and contractual controls. |
| AI Platform Owner | Run the shared AI platform: the model gateway and allow-list, embedding services, vector stores, agent memory services and tracing tools. Keep their inventories current and apply approved changes. |
| Agent Sponsor | Answer for one agent: its purpose, the tools and systems it may use, its recertification and its retirement. Every agent has exactly one named sponsor. |

## Component Ownership

Each part of an AI application stack needs a person who answers for it. The table below names the accountable role for nine components that teams commonly build with, the decision that role owns, and the test cases that check the decision is recorded and enforced. It is one workable allocation, not a requirement of any standard: rename the roles to match your organization, but keep one accountable role per row.

| Component | Ownership question | Accountable | Consulted | Tested by |
|---|---|---|---|---|
| Models | Who decides which models are approved for use? | AI Governance Committee for models used in high-risk use cases; AI Platform Owner for all others, under the tier rules in the [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md) | Security Architecture, Procurement / Legal, Data Protection | [TC-L12-025](../10_Test_Case_Library/L12-model-layer.md#tc-l12-025), [TC-L12-032](../10_Test_Case_Library/L12-model-layer.md#tc-l12-032), [TC-L08-028](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-028) |
| Agents | Who defines what an agent is allowed to do? | Agent Sponsor, within the purpose approved for the use case | AI Product Owner, Security Architecture (Gate 4) | [TC-D09-002](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-002), [TC-D09-003](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-003), [TC-L06-013](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-013), [TC-L06-034](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-034) |
| Embeddings | Who determines what data gets embedded? | Data Owner of each source decides what is embedded; AI Platform Owner approves the embedding model and provider | Data Protection, Procurement / Legal | [TC-L11-015](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-015), [TC-L11-026](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-026), [TC-L11-027](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-027) |
| Retrieval (RAG) | Who owns the documents behind it? | Data Owner of each knowledge source | AI Product Owner | [TC-L11-001](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-001), [TC-L11-010](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-010), [TC-L10-032](../10_Test_Case_Library/L10-data-layer.md#tc-l10-032) |
| Guardrails | Who defines and enforces the guardrails? | Security Architecture defines security and data rules, and the AI Product Owner defines topic and scope rules; the AI Platform Owner enforces them | GRC / Compliance, Data Protection | [TC-L08-043](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-043), [TC-L08-036](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-036), [TC-L08-039](../10_Test_Case_Library/L08-ai-gateway-and-security-controls.md#tc-l08-039) |
| Tools and MCP servers | Who grants access to which systems? | Owner of the target system, together with the Agent Sponsor | Identity and access management, Security Architecture | [TC-L06-047](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-047), [TC-L06-006](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-006), [TC-L09-005](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-005), [TC-D09-005](../10_Test_Case_Library/D09-agent-and-non-human-identity-governance.md#tc-d09-005) |
| Observability | Who investigates failures and reviews what went wrong? | SOC for security incidents; AI Product Owner for quality failures (wrong answers, wrong tool choices, regressions); AI Platform Owner for the tracing tools themselves | Data Protection | [TC-L17-032](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-032), [TC-L17-033](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-033), [TC-D12-020](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-020) |
| Vector databases | Who controls what data gets indexed? | Data Owner approves each index or collection and its scope; AI Platform Owner runs the store | Data Protection, Security Architecture | [TC-L11-028](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-028), [TC-L11-004](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-004), [TC-L11-007](../10_Test_Case_Library/L11-knowledge-and-retrieval-layer.md#tc-l11-007), [TC-L10-021](../10_Test_Case_Library/L10-data-layer.md#tc-l10-021) |
| Agent memory | Who is accountable for what it remembers? | AI Product Owner of the assistant or agent that writes the memory | Data Protection sets what may be remembered and handles access and erasure requests | [TC-L07-042](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-042), [TC-L07-043](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-043), [TC-L07-044](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-044), [TC-L07-045](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-045), [TC-L07-028](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-028) |

Record the accountable person for each live component in the use-case registry or the relevant inventory. A component without a named owner should not pass Gate 6.

## Decisions Reserved for the Governing Body

The governing body should not delegate these decisions, even where it delegates the work behind them:

- The AI risk appetite statement and the risk criteria used in the [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md).
- The categories of AI use that are prohibited, and the categories that always count as high-risk.
- Acceptance of residual risk rated Critical for an AI use case.
- The AI policy and its scope ([AI Policy, Standards and Acceptable Use](17_AI_Policy_Standards_and_Acceptable_Use.md)).
- The level of human oversight required where AI makes or supports decisions about people.

## Committee Charters

The tables below are starting charters for the two bodies most organizations need below the governing body. The meeting frequencies, membership and quorum are illustrative defaults, not requirements of any standard; adapt them and have the governing body or accountable executive approve the result. A smaller organization can merge the two bodies, as long as the decision rights below stay with named people.

### AI Governance Committee

| Item | Charter |
|---|---|
| Purpose | Decide on high-risk AI use, risk acceptances above the risk owner's authority, and exceptions; oversee the AI risk register and report to the governing body. |
| Authority | Delegated by the governing body through the accountable executive. Cannot approve a use the governing body has prohibited, or accept a Critical residual risk on its own (see [Decisions Reserved for the Governing Body](#decisions-reserved-for-the-governing-body)). |
| Chair | The accountable executive or a delegate named in writing. |
| Members | GRC / Compliance, Security (CISO or delegate), Data Protection Officer, Legal, Data Owner representative, AI Platform Owner, and a business representative for each use case on the agenda. Internal audit attends as an observer and does not vote. |
| Quorum | Chair plus at least half the members, including Security and the Data Protection Officer or their delegates. |
| Frequency | Monthly, and within five working days when an urgent decision is requested. |
| Inputs | Use-case intake and tier ([T01](../11_GCC_AI_Compliance/T01_AI_Use_Case_Intake_and_Risk_Tiering.md)), risk assessment scored under the [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md), impact assessment ([AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042)), exception requests, incident and monitoring summaries. |
| Outputs | A decision record for each item: decision, conditions, owner, expiry or review date, and dissent if any. A quarterly report to the governing body covering the items under [Board-Level Reporting](#board-level-reporting). |
| Conflicts | A member who sponsors or owns the item under decision states it and does not vote on it. |
| Review of this charter | Annually, and after any material incident in which a committee decision played a part. |

### AI Security Review Board

| Item | Charter |
|---|---|
| Purpose | Carry out the technical reviews at Gates 3 to 6 and recommend go or no-go to the decision owner. |
| Authority | Recommends; does not accept risk. May block a release that fails a mandatory control until the decision owner decides. |
| Chair | Security Architecture. |
| Members | AppSec / DevSecOps, SOC, AI Platform Owner, Data Protection / DLP, and the AI product owner and agent sponsor for the item under review. |
| Quorum | Chair plus AppSec and the AI Platform Owner, or their delegates. |
| Frequency | Weekly or per release, so that review does not hold up delivery. |
| Inputs | Design and threat model, release gate evidence ([AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033)), adversarial test results ([AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034)), open findings. |
| Outputs | Gate decision record with findings, mandatory fixes and the residual risks passed to the risk owner. |
| Review of this charter | Annually. |

## Decision Rights

Who recommends, who approves and where a decision escalates. "Approve" means the named role owns the decision and its record. The allocation is one workable default; rename roles to match your organization, but keep exactly one approver per row.

| Decision | Recommends | Approves | Escalates to | Kept informed |
|---|---|---|---|---|
| AI risk appetite and risk criteria | Accountable executive | Governing body | None | AI Governance Committee |
| Prohibited and always-high-risk categories of AI use | AI Governance Committee | Governing body | None | All staff, through the AI policy |
| AI policy and acceptable use | GRC / Compliance | Governing body | None | All staff |
| New AI use case, Low or Medium tier | AI Product Owner | Risk owner, with Security and Data Protection review at the applicable gates | AI Governance Committee if a reviewer objects | AI Platform Owner |
| New AI use case, High tier | AI Security Review Board and Data Protection Officer | AI Governance Committee | Governing body if the residual risk is Critical | Accountable executive |
| Model approved for general use | AI Platform Owner | AI Platform Owner, within the tier rules | AI Governance Committee for models used in high-risk use cases | Security Architecture |
| Agent permissions and tool grants | Agent Sponsor | Owner of the target system | AI Governance Committee if the grant includes irreversible actions without human approval | Security Architecture, SOC |
| Release of a custom AI application or agent | AI Security Review Board | AI Product Owner, after the board's go recommendation | AI Governance Committee on a no-go the owner disputes | SOC |
| Acceptance of residual risk | Risk owner | Authority for the rating in the [AI Risk Methodology](../02_Risk_Management/02A_AI_Risk_Methodology.md#scoring-method) | The next authority up when appetite is exceeded | GRC / Compliance |
| Exception to a policy or control | Requesting owner | AI Governance Committee (High and Critical); GRC / Compliance (Low and Medium) | Governing body for an exception to a reserved decision | Internal audit |
| Stopping an AI system in an incident | SOC or the system's overseer | Anyone named as able to stop it ([AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025)); confirmation by the accountable executive within one working day | Governing body for a material incident | Data Protection Officer, Legal, Communications |
| Notification to a regulator or authority | Legal / Data Protection Officer | Accountable executive | Governing body for a material incident | AI Governance Committee |
| Retirement of an AI system | AI Product Owner | Risk owner | AI Governance Committee if other systems depend on it | AI Platform Owner, Data Owner |

## Role-Based Training Plan

Training for [AI-CTRL-044](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-044). The groups, topics and intervals are a starting plan to adapt; where a law sets a specific literacy duty, check that the plan meets it (for the EU see [T07 AI Literacy Programme Record](../12_EU_AI_Compliance/T07_AI_Literacy_Programme_Record.md)).

| Role group | What they need to know or do | When | How effectiveness is checked |
|---|---|---|---|
| Governing body and executives | AI risk appetite, reserved decisions, how to read the AI risk report, accountability that stays with them | On appointment and annually | Board evaluation; quality of questions recorded in minutes |
| AI Governance Committee and risk owners | Scoring method and calibration, acceptance authority, impact assessment review | On appointment, annually, and with each change to the method | Calibration exercise against the [worked examples](../02_Risk_Management/02A_AI_Risk_Methodology.md#worked-calibration-examples) |
| All staff | Acceptable use, which tools are approved, what data may not be entered, how to report a problem | At joining and annually; on a policy change | Short scenario quiz; trend in prompt and upload policy violations |
| Developers and engineers using AI assistants | Secure use of coding assistants, reviewing AI-generated code, secrets, hallucinated packages | Before access is granted and annually | Insecure AI-generated code findings; secrets detected in prompts |
| Builders of AI applications and agents | Prompt injection, tool and permission design, release gate, adversarial testing | Before the first release and annually | Release gate findings per release; adversarial test results |
| Human reviewers and overseers | The system's limits, what evidence to check, authority to override and stop, automation bias | Before assignment, and on each material change to the system | Seeded-error catch rate and override rate ([AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045)) |
| SOC and incident responders | AI telemetry, AI incident types, evidence preservation, provider coordination | Annually, with a tabletop exercise | Exercise results and time to contain |
| Procurement, legal and vendor managers | AI terms: training on inputs, output ownership, indemnity, residency, sub-processors | On appointment and annually | Contract review findings |
| Contractors and third parties with access | The same as the staff group they work alongside | Before access | Access is not granted without a completion record |

Record completion and results by person and role ([TC-L03-038](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-038)) and check that the training changes behaviour ([TC-L03-045](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-045)).

## Board-Level Reporting

Report these to the governing body at least each quarter:

- Number of AI use cases by risk tier, and how many are high-risk or use sensitive data.
- Critical and high AI risks open past their treatment date.
- Exceptions past their expiry date.
- Material AI incidents and near misses, with root causes.
- Impact assessments overdue for review.
- Datasets in use below their approved data quality thresholds.
- Status of AI regulatory obligations and authority engagement.

## Continuous Governance Metrics

- Number of approved AI tools.
- Number of unapproved AI tools detected.
- AI prompt/file policy violations.
- AI coding assistant usage and detections.
- Custom AI apps reviewed.
- Agentic AI workflows approved.
- AI components without a named owner (models, agents, indexes, memory stores, tool grants).
- Open AI risks and exceptions.
- Vendor sovereignty validations completed.
- SOC alerts and incidents related to AI usage.

## Standards Basis

The governing body layer, the reserved decisions and the board-level reporting above follow the structure of ISO/IEC 38507:2022 (Governance implications of the use of artificial intelligence by organizations): clause 4.3 on maintaining accountability when introducing AI, and clause 6 on policies for governance oversight (6.2), decision-making (6.3), data use (6.4), culture and values (6.5), compliance (6.6) and risk appetite and management (6.7). The data owner row and the data quality metric follow ISO/IEC 5259-5:2025, clauses 7 and 8 (responsibilities of the governing body and of management for data quality). Clause numbers and headings were checked against the publishers' contents previews on 15 October 2026; the clause text was not read. See the [ISO/IEC AI Standards Crosswalk](../23_Framework_Crosswalks/15_ISO_IEC_AI_Standards_Crosswalk.md).

