---
title: "Enterprise AI Risk Register"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Risk Management"
nav_order: 2
document_type: AI Security Wiki Reference
version: 1.4
---

# Enterprise AI Risk Register

> **Purpose:** Provide a sample enterprise AI risk register covering AI usage, development, applications, agents, auditability, sovereignty, cost, output reliability and resilience, and the strategy, financial, workforce and legal risks of adopting AI, as a starting template.

> **Audience:** Governance, cyber risk, security architecture, audit, AI product owners.

> **How to use:** Use this page as a template. Re-score each risk using the AI Risk Methodology for your own environment, and add owners, evidence and treatment status. The [AI Risk Register Template](../25_Templates/01_AI_Risk_Register_Template.md) gives you the same register as an Excel workbook.

> **Scope of AI-R14 to AI-R28:** These fifteen entries were added in version 1.1 to make operational risks (bias, explainability, model change, drift, oversight, reputation) and agentic risks (memory poisoning, credential harvesting, plugin supply chain, tool chains, trust boundaries) first-class entries. The Example Priority column is not re-ranked across all {{n:risks}} risks; re-rank it with the AI Risk Methodology. Each risk is cross-referenced to the FINOS AI Governance Framework in the [risk to control mapping](02D_AI_Risk_to_Control_Mapping.md).

> **Scope of AI-R47 to AI-R54:** These eight entries were added in version 1.4 to close categories of the [AI Risk Map](#credit-ai-risk-map) that the register covered only in part: model extraction and inference, incident handling, personal data inside models, training-serving skew, liability, unmaintained open-source components, labelling of AI-generated content and agent actions seen from outside. Each passes the tests in [What Belongs on the Register](02A_AI_Risk_Methodology.md#what-belongs-on-the-register); where only the map names a risk, the narrative says so. AI-R29 and AI-R31 were widened at the same time.

> **Scope of AI-R29 to AI-R46:** These eighteen entries were added in version 1.2 to cover risks that the [AI Risk Map](#credit-ai-risk-map) identifies and that the register did not have: strategy and value, cost and investment, provider concentration, workforce, energy use, licensing and legal records, model validation, financial reporting, capability claims and emotional dependence, and five specific security and agent risks. Each narrative names the map domain it was adapted from.

> **Owner Domain:** The number is the domain of the [AI Risk Map](#credit-ai-risk-map) that the risk falls in. The map groups risks by who owns them rather than by how the technology works, so the column shows which part of the organization should hold each risk. The assignment of AI-R01 to AI-R28 is this wiki's judgement. The domains are listed under [Owner Domains](#owner-domains), and the [AI Risk Map Crosswalk](../23_Framework_Crosswalks/18_AI_Risk_Map_Crosswalk.md) maps each of the map's categories to this register.

> **Illustrative example:** The ratings and entries on this page are generic examples, not an assessment of any specific organization. Replace them with your own findings before relying on them.

| Risk ID | Risk Area | Owner Domain | Example Likelihood | Example Impact | Example Residual Risk | Example Priority |
|---|---|---|---|---|---|---|
| AI-R01 | Critical Infrastructure Information Exposure | 03 | High | Critical | Critical | 1 |
| AI-R02 | Shadow AI and Ungoverned AI Usage | 01 | High | High | High | 2 |
| AI-R03 | Sensitive Data Leakage Through Prompts and Uploads | 03 | High | Critical | High | 3 |
| AI-R04 | IDE-Based Source Code and Credential Exposure | 03 | Medium-High | High | High | 4 |
| AI-R05 | Prompt Injection Against Custom AI Applications | 05 | Medium | Critical | High | 5 |
| AI-R06 | AI Output Leakage and Oversharing | 05 | Medium | High | High | 6 |
| AI-R07 | AI Agent and Tool-Calling Abuse | 12 | Medium | Critical | Critical | 7 |
| AI-R08 | AI Supply Chain and Model Integrity Risk | 09 | Medium | High | High | 8 |
| AI-R09 | Lack of AI Auditability and Forensic Visibility | 07 | High | High | High | 9 |
| AI-R10 | Data Sovereignty and Third-Party Processing Risk | 08 | Medium | Critical | High | 10 |
| AI-R11 | AI Cost Abuse and Resource Exhaustion | 07 | Medium | High | High | 11 |
| AI-R12 | Unreliable or Harmful AI Output | 06 | Medium | High | High | 12 |
| AI-R13 | AI Service Disruption and Dependency Failure | 07 | Medium | High | Medium | 13 |
| AI-R14 | Biased or Discriminatory AI Outcomes | 06 | Medium | High | High | 14 |
| AI-R15 | Lack of Explainability and Decision Traceability | 04 | Medium | High | High | 15 |
| AI-R16 | Foundation Model Version Change and Non-Deterministic Behaviour | 07 | High | Medium | High | 16 |
| AI-R17 | Data Quality Degradation and Model Drift | 04 | Medium | High | High | 17 |
| AI-R18 | Model Overreach and Use Beyond Approved Purpose | 01 | Medium | High | High | 18 |
| AI-R19 | Insufficient or Ineffective Human Oversight | 06 | Medium | High | High | 19 |
| AI-R20 | Reputational Harm from AI Behaviour | 10 | Medium | High | Medium | 20 |
| AI-R21 | Agent Memory and State Persistence Poisoning | 12 | Medium | High | High | 21 |
| AI-R22 | Agent-Mediated Credential Discovery and Harvesting | 12 | Medium | Critical | High | 22 |
| AI-R23 | Skill, Plugin and MCP Server Supply Chain Compromise | 12 | Medium | Critical | High | 23 |
| AI-R24 | Tool Chain Manipulation and Injection | 12 | Medium | Critical | High | 24 |
| AI-R25 | Multi-Agent Trust Boundary Violation | 12 | Medium | High | High | 25 |
| AI-R26 | Reasoning Trace and Intermediate Output Exposure | 05 | Medium | Medium | Medium | 26 |
| AI-R27 | Intellectual Property and Copyright Infringement | 08 | Medium | High | High | 27 |
| AI-R28 | Regulatory Non-Compliance from Unsupervised AI Decisions | 08 | Medium | Critical | High | 28 |
| AI-R29 | Unrealised AI Value and Misaligned AI Strategy | 02 | Medium | High | Medium | 29 |
| AI-R30 | AI Cost Volatility and Stranded Investment | 11 | Medium | High | Medium | 30 |
| AI-R31 | Model Provider Concentration, Lock-in and Deprecation | 09 | Medium | High | High | 31 |
| AI-R32 | Model Monoculture and Correlated Failure | 09 | Medium | High | Medium | 32 |
| AI-R33 | Workforce Deskilling and Loss of Institutional Knowledge | 10 | Medium | High | Medium | 33 |
| AI-R34 | Workforce Change Failure and Skills Shortage | 10 | Medium | Medium | Medium | 34 |
| AI-R35 | Unmeasured Energy and Water Use of AI | 11 | High | Medium | Medium | 35 |
| AI-R36 | AI Output Ownership and Model Licence Breach | 08 | Medium | High | Medium | 36 |
| AI-R37 | Provider Obligations Triggered by Modifying a Model | 08 | Medium | High | High | 37 |
| AI-R38 | AI Records Not Preserved for Legal Hold and Discovery | 03 | Medium | High | High | 38 |
| AI-R39 | Missing Independent Model Validation | 04 | Medium | High | High | 39 |
| AI-R40 | AI Output Relied On in Financial Reporting Controls | 01 | Medium | High | High | 40 |
| AI-R41 | AI-Washing and Unverified AI Capability Claims | 10 | Medium | High | Medium | 41 |
| AI-R42 | Anthropomorphism and Emotional Dependence | 06 | Medium | High | Medium | 42 |
| AI-R43 | Hallucinated Package Dependencies | 05 | Medium | High | High | 43 |
| AI-R44 | Safety Training Removed from Self-Hosted Models | 09 | Medium | High | Medium | 44 |
| AI-R45 | Agent Activity Indistinguishable from Attack | 07 | Medium | High | High | 45 |
| AI-R46 | Insider Use of Agents to Exceed Own Access | 05 | Medium | High | High | 46 |
| AI-R47 | Model Extraction and Inference Attacks | 05 | Medium | High | Medium | 47 |
| AI-R48 | AI Incidents Not Recognised or Handled | 07 | Medium | High | High | 48 |
| AI-R49 | Personal Data That Cannot Be Removed from Models | 03 | Medium | High | High | 49 |
| AI-R50 | Training-Serving Skew and Unreproducible Models | 04 | Medium | Medium | Medium | 50 |
| AI-R51 | Liability for Harm Caused by AI Decisions | 08 | Low | High | Medium | 51 |
| AI-R52 | Unmaintained Open-Source AI Components | 09 | Medium | Medium | Medium | 52 |
| AI-R53 | Unlabelled AI-Generated Content | 06 | Medium | High | Medium | 53 |
| AI-R54 | Agent Actions Others Cannot Identify as AI | 12 | Medium | Medium | Medium | 54 |

## Risk Narratives

### AI-R01: Critical Infrastructure Information Exposure
Users may submit sensitive infrastructure, architecture, security, operational or business information into AI tools for summarization, translation, troubleshooting or code support. Required controls include prompt inspection, upload inspection, classification-aware policy enforcement, audit logging and SOC alerting.

### AI-R02: Shadow AI and Ungoverned AI Usage
Unapproved AI use may occur through public AI sites, browser extensions, IDE plugins, SaaS features, APIs or desktop AI applications. Required controls include AI discovery, tool classification, allow/monitor/warn/block policy, endpoint visibility and reporting.

### AI-R03: Sensitive Data Leakage Through Prompts and Uploads
AI interactions can contain confidential data, personal data, credentials, source code, logs and business documents. Required controls include sensitive data detection, redaction/masking/warning/blocking and evidence generation.

### AI-R04: IDE-Based Source Code and Credential Exposure
AI coding assistants can expose source code, API keys, internal URLs, infrastructure-as-code and application logic. Required controls include IDE visibility, secret detection, source code protection and developer governance.

### AI-R05: Prompt Injection Against Custom AI Applications
Custom AI applications, RAG systems and internal chatbots can be manipulated through direct or indirect prompt injection. Required controls include runtime inspection, RAG security validation, guardrails and output filtering.

### AI-R06: AI Output Leakage and Oversharing
AI responses may aggregate or expose information beyond the intended context due to permission hygiene, weak retrieval controls or prompt manipulation. Required controls include output inspection, source-document logging and permission-aware response governance.

### AI-R07: AI Agent and Tool-Calling Abuse
Agents can call tools, APIs and workflows. Risks include excessive privilege, unauthorized action, tool misuse, MCP compromise and insufficient traceability. Required controls include identity, least privilege, approvals, tool governance and action logging.

### AI-R08: AI Supply Chain and Model Integrity Risk
AI applications rely on models, libraries, datasets, plugins, extensions and MCP servers. Required controls include AI asset inventory, model inventory, AI BOM, model scanning, plugin governance and vulnerability integration.

### AI-R09: Lack of AI Auditability and Forensic Visibility
Investigations are weak if prompts, responses, uploads, retrieved documents, model calls, tool invocations and agent decisions cannot be reconstructed. Required controls include policy-based logging, audit export, SIEM integration and retention controls.

### AI-R10: Data Sovereignty and Third-Party Processing Risk
AI platforms may process or retain prompts, uploads, metadata and logs in external locations. Required controls include data residency validation, training exclusion, retention configuration, administrative access logging and deployment model assessment.

### AI-R11: AI Cost Abuse and Resource Exhaustion
AI usage is metered, so leaked keys, automated traffic against public endpoints, runaway agents and retry loops can exhaust budget or capacity within hours. Required controls include cost attribution, budgets and quotas with enforcement, rate limits, spend anomaly detection, key revocation and limits on agent loops.

### AI-R12: Unreliable or Harmful AI Output
AI systems can give confident wrong answers, invent sources, packages and links, drift outside their approved scope or produce harmful content, and people act on the result. Required controls include grounding in approved sources, citation verification, topic restriction, harmful content filtering and factuality evaluation.

### AI-R13: AI Service Disruption and Dependency Failure
Business processes come to depend on AI services, model providers and the security controls in front of them. Outages, provider changes, overload or a control that fails open can stop the process or silently remove protection. Required controls include defined fail modes, failover that keeps policy intact, fallback paths, tested backups, provider exit plans and detection of silent control failure.

### AI-R14: Biased or Discriminatory AI Outcomes
AI outputs or decisions can disadvantage people or groups because of skewed data, proxy variables or the way a prompt frames the task. Required controls include group-level fairness testing before release and in operation, review of proxy variables, documented thresholds and human review of adverse outcomes.

### AI-R15: Lack of Explainability and Decision Traceability
The basis for an AI-assisted decision may not be explainable to a customer, reviewer or regulator, and the decision may not be reconstructable later. Required controls include decision records that name the model version, prompt template and sources, explanation templates by audience and retention that matches the decision's life.

### AI-R16: Foundation Model Version Change and Non-Deterministic Behaviour
Providers update, replace or retire models, and the same input can give different outputs. Guardrails, prompts and safety evaluations that passed before can regress without any change on the customer side. Required controls include version pinning, tracking of provider notices, a regression suite on every change, tolerance limits for output variation and tested rollback.

### AI-R17: Data Quality Degradation and Model Drift
Source data, retrieval content or input patterns change over time, so output quality or safety falls without any code change. Required controls include quality baselines, freshness limits and named owners for each source, drift indicators with thresholds and a defined response when a threshold is crossed.

### AI-R18: Model Overreach and Use Beyond Approved Purpose
A system approved for a low-risk purpose may later be used for a higher-risk one, or its autonomy and data access may grow without a new assessment. Required controls include a purpose statement per use case, change triggers that force reassessment and monitoring of actual use against the approved purpose.

### AI-R19: Insufficient or Ineffective Human Oversight
A person may be nominally in the loop but unable or unwilling to review meaningfully, through automation bias, missing context, no authority to override or a volume that forces rubber-stamping. Required controls include oversight points set by risk tier, reviewer context, authority and training, and effectiveness measures such as override rates and sampled re-review.

### AI-R20: Reputational Harm from AI Behaviour
A public-facing or customer-facing AI system may say something offensive, misleading or off-brand, or make a commitment the organisation did not intend, and the output becomes public. Required controls include content filtering, topic restriction, adversarial testing before release and a public-incident response path.

### AI-R21: Agent Memory and State Persistence Poisoning
Malicious or wrong content written into an agent's long-term memory or saved state can influence later sessions or other users and survive restarts. Required controls include memory integrity checks, provenance for stored entries, purge and rollback procedures and isolation of memory between users.

### AI-R22: Agent-Mediated Credential Discovery and Harvesting
An agent with file, shell or environment access can find and use credentials it was never meant to hold, and an injected instruction can make it send them out. Required controls include keeping secrets out of agent-readable locations, short-lived scoped tokens issued at call time, canary credentials and separate identities for agents.

### AI-R23: Skill, Plugin and MCP Server Supply Chain Compromise
Agent skills, plugins and MCP servers run with the agent's authority, and a compromised or malicious one can act as the agent. This narrows AI-R08 to the agent extension surface. Required controls include an allowlist, review before approval, version pinning, integrity checks and removal procedures.

### AI-R24: Tool Chain Manipulation and Injection
An attacker can steer an agent through a sequence of individually permitted tool calls, or inject instructions through tool inputs and outputs, so the combined effect is one nobody authorised. Required controls include deterministic checks on call sequences, validation of tool inputs and outputs and runtime inspection.

### AI-R25: Multi-Agent Trust Boundary Violation
Agents that call or delegate to other agents can pass on instructions, data or authority across boundaries nobody intended, so one compromised agent affects the rest. Required controls include an agent trust map, identity for every agent, containment and isolation between agents and logging of inter-agent requests.

### AI-R26: Reasoning Trace and Intermediate Output Exposure
Reasoning steps, intermediate tool output and system instructions can expose sensitive data, internal logic or attack paths when they are shown to users or written to logs. Required controls include classifying these traces, deciding what is displayed and retained, and testing for leakage.

### AI-R27: Intellectual Property and Copyright Infringement
Staff may submit third-party copyrighted or licensed material to AI tools, and AI output or training data may infringe the rights of others or carry licence obligations into products and code. Required controls include a usage policy, review of vendor terms for output ownership and indemnity, provenance records for training data and scanning of released output where policy requires.

### AI-R28: Regulatory Non-Compliance from Unsupervised AI Decisions
A regulated process may use AI without the supervision, records or accountability the regulator expects of a human performing the same step. Required controls include an obligation register, impact assessment, decision records, human oversight appropriate to the tier and a named accountable owner.

### AI-R29: Unrealised AI Value and Misaligned AI Strategy
AI may be adopted because of hype rather than a stated problem, pilots may stall without ever showing value, returns may depend on redesigning work nobody planned to redesign, and the full cost of data, integration and people may not be counted. The opposite also applies: failing to weigh the competitive cost of not adopting AI is a risk too, as is customers starting to reach the organization through their own AI agents, which can cut it off from the customer relationship. Required controls include a business case with a success measure and a risk and benefit weighing for each use case, a stage gate that stops or scales a pilot on evidence, and a review of value delivered after go-live. Adapted from AI Risk Map domain 02 (Strategy and Value Realization).

### AI-R30: AI Cost Volatility and Stranded Investment
Providers can change token prices, tiers or context limits on their own terms, usage forecasts made in a pilot rarely hold at production scale, and money can be committed to a system that is scaled too early or kept going past failure. Insurance cover may also exclude AI losses or define a user as a human only. This differs from AI-R11, which is about abuse; this risk arises from normal use. Required controls include cost forecasts that are revisited as usage grows, contract terms on price changes, a decision point to stop funding, and a review of insurance wording for AI. Adapted from AI Risk Map domain 11 (Financial and Resource).

### AI-R31: Model Provider Concentration, Lock-in and Deprecation
Many systems may depend on a few model providers, proprietary APIs and fine-tunes make switching costly, and fine-tuned models, embeddings and prompts often do not transfer between providers. A provider can retire a model or change its behaviour and force an unplanned migration, and shortages of GPUs, compute capacity or power can limit how far a system can scale, or lead a provider to ration capacity. AI-R13 covers outages and AI-R16 covers version changes; this risk covers the dependence itself. Required controls include a record of which systems depend on which provider and model, exit provisions in contracts, a tested migration path for critical systems and tracking of provider deprecation notices. Adapted from AI Risk Map domain 09 (Third-Party and Model Supply Chain).

### AI-R32: Model Monoculture and Correlated Failure
When many systems, or a system and the controls that check it, use the same underlying model, one blind spot or bias is repeated everywhere at once and independent checks are not independent. Required controls include an inventory that records the base model behind each system, a deliberate choice of a different model or a non-AI method where a check must be independent, and evaluation that looks for errors shared across systems. Adapted from AI Risk Map domain 09 (Third-Party and Model Supply Chain).

### AI-R33: Workforce Deskilling and Loss of Institutional Knowledge
Staff who hand work to AI can lose the expertise needed to check it, knowledge held in people's heads disappears as AI replaces processes, and the organization may be unable to operate when the AI is unavailable. Specialists who leave can take undocumented prompt and model knowledge with them. Required controls include keeping manual competence for critical processes and testing it, documented fallback procedures, and recording prompts, configurations and design decisions as part of the system. Adapted from AI Risk Map domain 10 (Workforce, Human and Societal).

### AI-R34: Workforce Change Failure and Skills Shortage
Leaders may manage AI like a conventional IT rollout and underestimate how much it changes the work itself, staff may resist or quietly avoid AI because of fear of displacement or distrust of its output, and AI and AI-risk specialists are scarce. Required controls include a change plan for each significant deployment, consultation with affected staff, adoption and trust measures, and AI literacy and role-based training. Adapted from AI Risk Map domain 10 (Workforce, Human and Societal).

### AI-R35: Unmeasured Energy and Water Use of AI
Training and inference use energy and, in many data centres, water for cooling, and these are rarely measured or weighed against the value of a use case. This can conflict with an organization's sustainability commitments and reporting. Required controls include an estimate of energy use per system from usage data and provider information, its inclusion in the use-case decision, and reporting where sustainability commitments require it. Adapted from AI Risk Map domain 11 (Financial and Resource).

### AI-R36: AI Output Ownership and Model Licence Breach
Who owns AI-generated content, and whether it can be protected by copyright at all, is unsettled in many jurisdictions. Open-weight models come with licences that may restrict commercial use, user numbers, fields of use or the training of other models, and those terms can be breached without anyone noticing. AI-R27 covers infringing the rights of others; this risk covers the organization's own rights and licence obligations. Required controls include a register of model licences and their conditions, review of output ownership in vendor terms, and legal advice before relying on ownership of AI-generated assets. Adapted from AI Risk Map domain 08 (Legal, Regulatory and Compliance).

### AI-R37: Provider Obligations Triggered by Modifying a Model
Fine-tuning, rebranding or changing the intended purpose of a third-party model can turn a deployer into a provider under some laws, with heavier obligations. Under the EU AI Act this can happen through a substantial modification or a change of purpose to a high-risk use (see the [EU AI Regulatory Hub](../12_EU_AI_Compliance/01_EU_AI_Regulatory_Hub.md)). Required controls include a role classification for each AI system that is repeated when the model, its purpose or its branding changes, and legal review of the obligations that follow. Adapted from AI Risk Map domain 08 (Legal, Regulatory and Compliance).

### AI-R38: AI Records Not Preserved for Legal Hold and Discovery
Prompts, outputs and agent traces can be relevant to litigation, regulatory inquiries or disputes, and may be subject to a legal hold. Short retention settings in AI tools and data spread across several stores can mean they are deleted or cannot be found. AI-R09 covers forensic visibility for security; this risk covers legal preservation. Required controls include a retention schedule that names AI records, a way to apply a legal hold to them, and a tested search across the stores that hold them. Adapted from AI Risk Map domain 03 (Data and Privacy).

### AI-R39: Missing Independent Model Validation
A model may be approved by the team that built or bought it, with no independent validation or effective challenge, and validation data may not represent real use, so weaknesses show only with live users. Model risk management guidance in banking, such as the US supervisory guidance SR 11-7, expects independent validation. Required controls include validation by people independent of the developer, test data that reflects intended use, and validation repeated when the model or its use changes. Adapted from AI Risk Map domain 04 (Model Development and Performance).

### AI-R40: AI Output Relied On in Financial Reporting Controls
AI may prepare reconciliations, journal entries or other inputs to financial reporting without the scope of internal control testing being changed to cover it. If nobody records which artifacts AI produced, a flaw in the model cannot be traced to what it affected. Required controls include notifying internal control owners and auditors when AI enters a financial reporting process, recording which outputs AI produced, and testing the AI step as part of the control. Adapted from AI Risk Map domain 01 (AI Governance and Accountability).

### AI-R41: AI-Washing and Unverified AI Capability Claims
An organization may overstate what its AI does to customers, investors or regulators, and may buy products whose "AI-powered" claims it cannot verify. Both can lead to regulatory action, disputes and lost trust. Required controls include review of external AI claims against evidence before publication, and testing of vendor capability claims during evaluation. Adapted from AI Risk Map domain 10 (Workforce, Human and Societal).

### AI-R42: Anthropomorphism and Emotional Dependence
People can attribute human qualities to conversational AI and come to depend on it emotionally, which raises the risk of manipulation and of harm to vulnerable users, including minors. This goes beyond the automation bias covered by AI-R19. Required controls include design review of personas and conversational style, clear disclosure that the user is talking to AI, safeguards and escalation for vulnerable users, and monitoring for patterns of dependence. Adapted from AI Risk Map domain 06 (Safety, Ethics and Responsible AI).

### AI-R43: Hallucinated Package Dependencies
AI coding assistants and agents can suggest or install packages that do not exist. An attacker who registers those names in a public package registry gets their code installed. AI-R12 covers invented packages as an output reliability problem; this risk covers the attack. Required controls include installing only from an approved registry or proxy, checking that a suggested package exists and is established before use, and dependency scanning in the release gate. Adapted from AI Risk Map domain 05 (Security and Adversarial Threats).

### AI-R44: Safety Training Removed from Self-Hosted Models
Open-weight models can be fine-tuned or modified so that their safety training is weakened or removed, and modified versions are published under names that hide their lineage. A team that self-hosts such a model may not know its refusals no longer work. Required controls include verifying where model weights came from, safety and refusal evaluation before deployment and after any fine-tuning, and recording the model's lineage in the AI-BOM. Adapted from AI Risk Map domain 09 (Third-Party and Model Supply Chain).

### AI-R45: Agent Activity Indistinguishable from Attack
Approved agents that read widely, call many tools and act quickly can look the same in logs as an attacker using agentic tooling, so detections either drown in false alarms or are tuned until they miss real attacks. Required controls include a distinct identity for each agent in telemetry, a record of who authorised each agent's task, and detection rules that use that context. Adapted from AI Risk Map domain 07 (Operations and Resilience).

### AI-R46: Insider Use of Agents to Exceed Own Access
An employee can ask an agent that holds broader permissions to read or do things the employee could not do directly. This turns the agent into a way around access controls. Required controls include agents acting with the requesting user's permissions, not a broader service identity, checks on the user's entitlement at each action, and logging that names both the user and the agent. Adapted from AI Risk Map domain 05 (Security and Adversarial Threats).

### AI-R47: Model Extraction and Inference Attacks
An attacker who can query a model at volume can copy its behaviour into a model of their own, or work out whether a given record was in its training data. Both are possible through an ordinary API or chat interface, without access to the model files. AI-R08 covers the supply chain and AI-R06 covers data leaking in outputs; this risk covers attacks that use the model's answers to steal the model or reveal its training data. Required controls include rate limits and query-pattern detection, limits on how much detail outputs reveal (such as confidence scores), and extraction and membership inference testing before release. Adapted from AI Risk Map domain 05 (Security and Adversarial Threats). Also named in NIST AI 100-2 as model extraction and membership inference (see the [NIST AI 100-2 Crosswalk](../23_Framework_Crosswalks/14_NIST_AI_100_2_Crosswalk.md)).

### AI-R48: AI Incidents Not Recognised or Handled
An incident response plan written for conventional systems may not recognise an AI incident, such as a successful prompt injection, an agent acting outside its task, harmful output reaching customers or a model behaving differently after a provider change. Such events can go unreported, be closed as user error, or miss legal reporting deadlines. Required controls include AI incident categories and severity criteria in the response plan, routing of AI alerts to the security operations team, the evidence to preserve for each AI component, exercises that use AI scenarios, and a record of which incidents must be reported to which authority. Adapted from AI Risk Map domain 07 (Operations and Resilience). Also named in the EU AI Act, Article 73, as serious incident reporting for high-risk systems (see the [EU AI Regulatory Hub](../12_EU_AI_Compliance/01_EU_AI_Regulatory_Hub.md)).

### AI-R49: Personal Data That Cannot Be Removed from Models
Once personal data has been used to train or fine-tune a model, or copied into embeddings and caches, it may not be possible to delete it on request or at the end of its retention period. A model may also repeat it in outputs. Required controls include knowing which training, fine-tuning and retrieval stores hold personal data, a procedure for data subject requests that covers models, embeddings and replicated stores, filtering or retraining decisions when deletion is required, and an assessment of whether the model itself holds personal data before it is shared or reused. Adapted from AI Risk Map domain 03 (Data and Privacy). Also named in the GDPR (the right to erasure, Article 17) and in EDPB Opinion 28/2024 on AI models and personal data (see the [EU AI Regulatory Hub](../12_EU_AI_Compliance/01_EU_AI_Regulatory_Hub.md)).

### AI-R50: Training-Serving Skew and Unreproducible Models
A model can behave differently in production from how it behaved in evaluation because features, preprocessing or data are prepared differently in the two places. Without versioned code, data and settings, a model cannot be rebuilt to investigate a fault or to show a regulator how it was produced. AI-R17 covers drift over time; this risk covers a gap that exists from the first day. Required controls include one shared definition of features and preprocessing for training and serving, versioning of the data, code and settings behind each model, a check that production inputs match the evaluation data, and a test that a model can be rebuilt from its records. Adapted from AI Risk Map domains 04 (Model Development and Performance) and 07 (Operations and Resilience). No second source has been checked, so this entry is partly the wiki's own framing.

### AI-R51: Liability for Harm Caused by AI Decisions
When an AI decision or output harms a customer or a third party, the organization may be liable even if a vendor built the model, and contracts may leave the organization carrying the loss. Some laws now treat software, including AI, as a product for liability purposes. Required controls include an impact assessment that names who could be harmed and how, human oversight sized to the harm, contract terms that allocate liability and indemnity with AI vendors, and a recorded acceptance of the residual risk by an accountable owner. Adapted from AI Risk Map domain 08 (Legal, Regulatory and Compliance). Also named in the new EU Product Liability Directive, which covers software (see the [EU AI Regulatory Hub](../12_EU_AI_Compliance/01_EU_AI_Regulatory_Hub.md)).

### AI-R52: Unmaintained Open-Source AI Components
AI systems often depend on open-source libraries, model-serving tools, agent frameworks and models that a small number of volunteers maintain. A component can be abandoned, stop receiving security fixes, or change owner, while systems keep using it. AI-R08 covers tampered components and AI-R43 covers invented package names; this risk covers genuine components that are no longer maintained. Required controls include recording each component's maintenance status in the AI-BOM, a release-gate check for unmaintained or end-of-life components, and a plan to replace or take over components that critical systems rely on. Adapted from AI Risk Map domain 09 (Third-Party and Model Supply Chain). No second source has been checked, so this entry is partly the wiki's own framing.

### AI-R53: Unlabelled AI-Generated Content
Images, audio, video and text generated by AI can be taken for real when they are not marked as AI-generated, and some laws now require marking or labelling. Content that loses its marking when it is edited or shared can still cause the same harm. AI-R41 covers claims about AI capability; this risk covers the content itself. Required controls include machine-readable marking of generated content where the law or the use case requires it, visible labels where people could be misled, a test that the marking survives the system's normal output path, and a record of which jurisdictions' labelling rules apply. Adapted from AI Risk Map domain 06 (Safety, Ethics and Responsible AI). Also named in the EU AI Act, Article 50 (see the [EU AI Regulatory Hub](../12_EU_AI_Compliance/01_EU_AI_Regulatory_Hub.md)), and in China's rules on labelling AI-generated content (see the [CN-T2 Content Labelling Implementation Record](../16_China_AI_Compliance/CN-T2_Content_Labelling_Implementation_Record.md)).

### AI-R54: Agent Actions Others Cannot Identify as AI
When an agent sends messages, makes bookings, files requests or calls other organizations' systems, the people and systems on the other side may not be able to tell that an agent acted, or for whom. That makes disputes hard to resolve and can breach the other party's terms. AI-R07 covers what the agent is allowed to do and AI-R45 covers how its activity looks in your own logs; this risk covers how it appears to others. Required controls include identifying the agent and the organization it acts for in outbound messages and requests where the other party expects it, keeping a record of each external action that names the agent and the user who started it, and following other services' rules on automated access. Adapted from AI Risk Map domain 12 (Autonomy and Delegated Action). No second source has been checked, so this entry is partly the wiki's own framing.

## Considered and Not Added

Risks proposed for this register and left out, with the reason. The tests are in [What Belongs on the Register](02A_AI_Risk_Methodology.md#what-belongs-on-the-register). A decision can be reopened when there is new information; say what changed.

| Proposed risk | Decision | Reason |
|---|---|---|
| Attacks that others carry out with AI against the organization, such as deepfake fraud, voice cloning or AI-written phishing | Out of scope | These are threats from outside, not risks of the organization's own adoption of AI, and belong on the threat register. See [AI for Security and AI-Enabled Threats](../00_Foundations/10-AI-for-Security-and-AI-Enabled-Threats.md). |
| General IT risks with no AI-specific change, such as unpatched servers hosting a model | Not added | Fails the AI-specific test; these stay on the enterprise risk register and are treated by general security controls. |
| Segregation of duties across AI configuration, operation and review (AI Risk Map, Roles and accountability) | Not added | Fails the distinct-response test: general segregation-of-duties controls apply, and the [release gate](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033) already requires review before a change reaches production. |
| Customers reaching the organization through their own AI agents and bypassing it (AI Risk Map, Competitive position) | Merged into AI-R29 | Same owner and response as other strategy risks; added to AI-R29's narrative in version 1.4. |
| Shortage of GPUs, compute capacity or power (AI Risk Map, Scaling and resource constraints) | Merged into AI-R31 | Same response as provider dependence (dependency record, exit and migration plans); added to AI-R31's narrative in version 1.4. |

## Owner Domains

The twelve domains of the AI Risk Map, used in the Owner Domain column. The likely owner is this wiki's suggestion, not part of the map; assign owners to fit your own organization.

| Domain | AI Risk Map domain | Likely owner |
|---|---|---|
| 01 | AI Governance and Accountability | AI governance committee, chief risk officer |
| 02 | Strategy and Value Realization | Executive sponsor, business owners |
| 03 | Data and Privacy | Data protection officer, data owners |
| 04 | Model Development and Performance | Model owners, model risk management |
| 05 | Security and Adversarial Threats | CISO |
| 06 | Safety, Ethics and Responsible AI | Responsible AI lead, product owners |
| 07 | Operations and Resilience | AI platform owner, IT operations |
| 08 | Legal, Regulatory and Compliance | General counsel, compliance |
| 09 | Third-Party and Model Supply Chain | Procurement, third-party risk |
| 10 | Workforce, Human and Societal | HR, communications |
| 11 | Financial and Resource | CFO, FinOps |
| 12 | Autonomy and Delegated Action (Agentic AI) | Agent sponsors, AI platform owner |

## Credit: AI Risk Map

The Owner Domain column, the domain names above and entries AI-R29 to AI-R54 are adapted from the *AI Risk Map* v1.3 (2026) by Evan Wheeler (GitHub [wheels344i-gte](https://github.com/wheels344i-gte)), published in the repository [wheels344i-gte/ai-risk-map](https://github.com/wheels344i-gte/ai-risk-map) and at RiskFramework.org (https://riskframework.org/), licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Changes: the risk factors were paraphrased, combined into register entries, given controls and ratings, and mapped to this wiki. The map is a one-page thought-starter of 196 risk factors in 12 domains; its authors list its sources on the map and say a companion workbook gives the source of each factor. This wiki used the one-page map only.
