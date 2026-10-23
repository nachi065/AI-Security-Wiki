---
title: "AI Risk Methodology"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Risk Management"
nav_order: 1
document_type: AI Security Wiki Reference
version: 1.2
---

# AI Risk Methodology

> **Purpose:** Define the rating method for assessing AI risks consistently across AI platforms, custom AI applications and agentic AI workflows.

> **Audience:** Risk management, security architecture, GRC, audit, AI product owners.

## Risk Appetite and Criteria

The governing body approves an AI risk appetite statement (see the [AI Governance Operating Model](../08_Governance/16_AI_Governance_Operating_Model.md)). It sets, for each rating on the risk scale below, who may accept the residual risk and how long an acceptance lasts. Record the statement, its approval date and its review date with the risk register. The ratings on this page are the risk criteria; change them only through the same approval.

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

## Scoring Method

The four ratings above are applied with a simple score so that two assessors looking at the same scenario reach the same answer. The method is jurisdiction-neutral and is the same one the [AI Risk Register Template (.xlsx)](../25_Templates/01_AI_Risk_Register_Template.md) uses. Every number below is a default for the governing body to approve or change; none comes from a standard.

**Step 1. Screen for prohibited use first.** If the use case falls into a category that the organization's AI policy prohibits, or that a law the organization is subject to prohibits, stop. Do not score it, do not offer it for risk acceptance and do not raise an exception. Record the decision and the reason, and close the request. A prohibited use is a decision already taken by the governing body (see [Decisions Reserved for the Governing Body](../08_Governance/16_AI_Governance_Operating_Model.md#decisions-reserved-for-the-governing-body)), not a risk to be weighed.

**Step 2. Score likelihood (1 to 4) with the controls that exist today.** Use only controls that are in operation, not planned ones.

| Score | Level | Meaning |
|---|---|---|
| 1 | Low | Unlikely in the next three years, or needs unusual conditions or a skilled, motivated attacker; strong controls in place. |
| 2 | Medium | Could happen within one to three years; the exposure exists and controls are partial. |
| 3 | High | Likely within a year; the AI use is widespread, the path is known or the controls are weak. |
| 4 | Very High | Expected within months, or already happening (for example, observed in monitoring or incidents). |

**Step 3. Score impact (1 to 4)** using the Risk Scale definitions above (1 Low, 2 Medium, 3 High, 4 Critical). Score the worst credible outcome of the scenario, not the worst imaginable one. Record the main impact type (confidentiality, integrity, availability, compliance, financial, people's rights or safety, reputation and so on) in a separate field, so risks that are not about security can be rated on the same scale.

**Step 4. Record existing control coverage** as None, Weak, Partial or Effective:

| Coverage | Meaning |
|---|---|
| None | No control addresses this scenario, or it is planned only. |
| Weak | A control exists but covers only part of the path, or has not been tested. |
| Partial | Controls cover the main path and have been tested, but there are known gaps or no evidence of operation over time. |
| Effective | Controls cover the path, are tested, and current evidence shows they operate ([AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038)). |

Coverage explains the likelihood score; it is not a third factor in the formula. A likelihood of 1 with coverage of None or Weak needs a written reason.

**Step 5. Read the rating from the score** (likelihood multiplied by impact, 1 to 16):

| Score | Rating | Default action | Who may accept the residual risk | Longest acceptance before re-approval |
|---|---|---|---|---|
| 1 to 2 | Low | Manage through routine processes | Risk owner | 12 months |
| 3 to 4 | Medium | Reduce where practical and monitor | Risk owner, with GRC / Compliance agreement | 12 months |
| 6 to 9 | High | Additional controls, monitoring or enforcement; report to the AI Governance Committee | AI Governance Committee | 6 months |
| 12 to 16 | Critical | Strong preventive and detective controls before or immediately after go-live; report to the committee and the governing body | Governing body or accountable executive, on the committee's recommendation | 3 months |

Scores of 5, 7, 10, 11, 13, 14 and 15 cannot occur on a 4 by 4 scale, so the bands have no gaps.

**Step 6. Apply two overrides.** First, a residual impact of 4 (Critical) is reported to the AI Governance Committee whatever the score, because a low likelihood can hide a severe outcome. Second, where an intake form sets a mandatory high tier, for example the override in [T01 AI Use-Case Intake and Risk Tiering](../11_GCC_AI_Compliance/T01_AI_Use_Case_Intake_and_Risk_Tiering.md) for decisions on credit, insurance, employment or eligibility, the use case gets the treatment of that tier even if individual risks score lower. The tier describes the use case; the rating describes one risk scenario within it.

**Step 7. Decide treatment and target.** Choose Mitigate, Avoid, Transfer or Accept ([AI Risk Treatment Plan](02C_AI_Risk_Treatment_Plan.md)), name the controls, and score the target likelihood and impact the treatment should reach. Preventive controls usually lower likelihood; impact falls only when a control limits the harm itself, for example by limiting what data an assistant can reach or how much an agent can spend.

**Step 8. Accept or escalate.** If the target rating is within the approved appetite, the risk owner records acceptance with an expiry date. If it is not, the authority in the Step 5 table decides, and the acceptance expires at the latest after the period shown.

### Calibrating assessors

Ratings drift apart when assessors do not compare their work. Before the first assessment cycle, and once a year after that, have at least two assessors score the four worked examples below independently, then compare. Where scores differ by more than one point on either factor, agree which reading of the scale was right and add a note to the scale. [TC-L02-007](../10_Test_Case_Library/L02-governance-and-risk-mgmt.md#tc-l02-007) tests whether a risk tool supports this comparison.

## Risk Factors and Risk Scenarios

A list of risks, such as the [Enterprise AI Risk Register](02B_Enterprise_AI_Risk_Register.md) or the [AI Risk Map](../23_Framework_Crosswalks/18_AI_Risk_Map_Crosswalk.md), is a list of risk factors: conditions, failure modes or events that contribute to risk. A factor is not ready to rate. Before rating, turn it into a scenario for the system being assessed: what could happen, to which asset or people, through which path, and with what consequence. One factor can give several scenarios, and one scenario can combine several factors.

- **Order is not likelihood.** The position of a risk in a list, or the space it takes, says nothing about how likely or severe it is. Rare, high-impact risks sit beside common ones.
- **Lists seed the assessment; they do not replace it.** Use them to prompt threat modelling and risk identification, alongside a model of the specific system.
- **Scope.** This methodology covers risks from the organization's own adoption of AI. Attacks that others carry out with AI against the organization belong on the threat register; see [AI for Security and AI-Enabled Threats](../00_Foundations/10-AI-for-Security-and-AI-Enabled-Threats.md).

## Owner Domain

Record which of the twelve owner domains a risk belongs to (listed under [Owner Domains](02B_Enterprise_AI_Risk_Register.md#owner-domains) on the register). The domains group risks by the part of the organization that owns them rather than by technology layer, so strategy, finance, workforce and legal risks reach their owners instead of defaulting to security. Some risks have two owners, for example accountability for harm caused by an agent, which sits with both governance and the agent's sponsor. Record the second domain in the risk entry's notes and name one accountable owner.

## When to Quantify

The four-level scale above suits most AI risks. Some scenarios can also be quantified in money, using cyber risk quantification methods such as FAIR (Factor Analysis of Information Risk): estimate how often the loss event could happen and the range of loss each time. This works best where loss data or credible estimates exist, such as data leakage, cost abuse, service disruption or regulatory fines. Other risks, such as erosion of staff expertise, loss of trust or strategic disadvantage, are hard to put a number on and are better reported to the governing body as a narrative with indicators. Record which approach was used for each risk, and do not present a quantified figure as more precise than its inputs.

*The ideas in the three sections above (risk factors versus scenarios, order not implying likelihood, scope, ownership-based domains, split ownership and the choice between quantification and narrative) are adapted from the usage notes of the AI Risk Map v1.3 by Evan Wheeler, RiskFramework.org, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). See the [credit on the risk register](02B_Enterprise_AI_Risk_Register.md#credit-ai-risk-map).*

## Worked Calibration Examples

The four examples below are illustrative. The organization, systems, numbers and decisions are invented to show the method end to end; they are not ratings of any real product or a recommendation for any real system. Use them to train assessors and to check that two people reach the same answer.

### Example 1: Staff pasting customer data into a public chatbot

| Step | Record |
|---|---|
| Scenario | Customer service staff paste customer complaints, including names, account numbers and order history, into a free public chatbot to draft replies. The provider's consumer terms allow it to retain and use inputs. |
| Risks in the register | [AI-R02](02B_Enterprise_AI_Risk_Register.md#ai-r02-shadow-ai-and-ungoverned-ai-usage), [AI-R03](02B_Enterprise_AI_Risk_Register.md#ai-r03-sensitive-data-leakage-through-prompts-and-uploads) |
| Prohibited use? | No. The policy allows approved AI tools for drafting; it does not allow customer data in unapproved tools. |
| Existing controls and coverage | Acceptable use policy and annual training ([AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012)). Web proxy logs show the chatbot is used about 200 times a week from the service team; nothing inspects what is pasted. Coverage: Weak. |
| Likelihood | 4 (Very High): the exposure is already happening, as the proxy logs show. |
| Impact | 3 (High): personal data of customers sent to a third party without a contract; a reportable breach is possible in some jurisdictions. Not 4, because no special-category or restricted data is involved. Impact type: Compliance. |
| Current rating | 4 x 3 = 12, Critical. |
| Treatment | Mitigate: provide an approved enterprise assistant under a contract that excludes training on inputs ([AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014)); inspect prompts and uploads to unapproved AI services and block customer identifiers ([AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002), [AI-CTRL-003](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-003)); keep discovery running for new tools ([AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001)). |
| Target | Likelihood 2 (blocked at the proxy, some residual use from unmanaged devices) x impact 3 = 6, High. |
| Acceptance decision | The target is still above an appetite of Medium, so the AI Governance Committee decides. It accepts the High residual for six months, on condition that unmanaged-device access to customer records is closed within that time, and asks for re-scoring then. |

### Example 2: Prompt injection in a customer support assistant

| Step | Record |
|---|---|
| Scenario | A support assistant answers from help-centre articles and the customer's own open tickets. An attacker writes instructions into a ticket; when an agent asks the assistant to summarise it, the assistant could reveal other customers' ticket details from its retrieval results. |
| Risks in the register | [AI-R05](02B_Enterprise_AI_Risk_Register.md#ai-r05-prompt-injection-against-custom-ai-applications), [AI-R06](02B_Enterprise_AI_Risk_Register.md#ai-r06-ai-output-leakage-and-oversharing) |
| Prohibited use? | No. |
| Existing controls and coverage | Input filter ([AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005)); retrieval scoped to the customer's own tickets in the application code, but not enforced in the vector store ([AI-CTRL-018](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-018)). No adversarial testing yet. Coverage: Weak. |
| Likelihood | 3 (High): the injection path is well known and tickets are attacker-controlled text. |
| Impact | 3 (High): exposure of other customers' personal data. |
| Current rating | 3 x 3 = 9, High. |
| Treatment | Mitigate: enforce per-customer filtering in the vector store, inspect output for other customers' identifiers ([AI-CTRL-020](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-020)), and run adversarial tests before go-live and on each change ([AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034)). |
| Target | Likelihood 2 x impact 2 (the store can no longer return other customers' records, so the worst case is the customer's own data being mishandled) = 4, Medium. |
| Acceptance decision | Within an appetite of Medium. The AI product owner accepts the residual risk for 12 months, with GRC / Compliance agreement, after the adversarial test report shows the filtering holds. |

### Example 3: An agent that can issue refunds

| Step | Record |
|---|---|
| Scenario | A customer-facing agent can look up orders and issue refunds through a payments tool. A manipulated conversation, or a poisoned order note, could lead it to issue refunds that were never due. |
| Risks in the register | [AI-R07](02B_Enterprise_AI_Risk_Register.md#ai-r07-ai-agent-and-tool-calling-abuse), [AI-R24](02B_Enterprise_AI_Risk_Register.md#ai-r24-tool-chain-manipulation-and-injection) |
| Prohibited use? | No. |
| Existing controls and coverage | The agent has its own identity and a scoped payments credential ([AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015), [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016)); a per-refund limit is enforced in the payments service, outside the model ([AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022)). No daily total limit and no human approval. Coverage: Partial. |
| Likelihood | 2 (Medium): the hard per-refund limit blocks large single refunds, but many small ones are possible. |
| Impact | 4 (Critical): repeated refunds at machine speed could cause a material financial loss before anyone notices. |
| Current rating | 2 x 4 = 8, High. |
| Treatment | Mitigate: add a daily total limit in the payments service, require human approval above a lower threshold ([AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023)), alert on refund rate, and give the support lead a kill switch ([AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025)). |
| Target | Likelihood 1 x impact 3 (the daily limit caps the loss) = 3, Medium. |
| Acceptance decision | Within appetite, so the agent sponsor accepts for 12 months. Because the current impact was 4, the risk was also reported to the AI Governance Committee under the Step 6 override, and the committee noted the acceptance. |

### Example 4: Inferring employee emotions from video calls

| Step | Record |
|---|---|
| Scenario | A team proposes a tool that scores employees' emotions from webcam video in internal meetings, to report on engagement. |
| Risks in the register | [AI-R14](02B_Enterprise_AI_Risk_Register.md#ai-r14-biased-or-discriminatory-ai-outcomes), [AI-R28](02B_Enterprise_AI_Risk_Register.md#ai-r28-regulatory-non-compliance-from-unsupervised-ai-decisions) |
| Prohibited use? | Yes. In this example the organization's AI policy lists inferring the emotions of employees as prohibited. In the EU, certain emotion-recognition uses are among the AI Act's prohibited practices (see the [EU AI Regulatory Hub](../12_EU_AI_Compliance/01_EU_AI_Regulatory_Hub.md)); check the exact scope with legal counsel. |
| Scoring | Not scored (Step 1). |
| Acceptance decision | Not eligible for risk acceptance or an exception. The request is closed and the reason recorded. If the team wants a different design, for example an anonymous engagement survey, that is a new use case with its own intake. |

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
Current Score and Rating:
Residual Risk (target score and rating):
Required AI Security Capabilities:
Evidence Required:
Risk Owner:
Owner Domain:
Treatment Decision:
Acceptance Decision (who, date, expiry):
Review Date:
```

## Communication and Consultation

At each stage, consult the people who can inform the assessment or are affected by the result: the business owner, data owner, security architecture, privacy, legal, the teams who operate the system and, for systems that affect people, representatives of the people affected. Record who was consulted and what changed as a result in the risk entry's notes. Report the outcome to the risk owner and, for High and Critical risks, to the AI Governance Committee.

## Review Triggers

- New AI vendor onboarding.
- New AI integration with enterprise data.
- AI coding assistant adoption.
- New RAG or custom AI application.
- Agentic AI workflow or tool-calling capability.
- Regulatory, audit or third-party risk review.
- A change to the system's purpose, users, deployment region or languages, or its data sources (these also trigger a review of its impact assessment, [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042)).
- A material incident, or monitoring that shows the system operating outside its validated boundaries.
- A provider notice of a price change, licence change or model retirement.
- Controls that have not been re-verified since the system last changed.

## Alignment with ISO/IEC 23894

ISO/IEC 23894:2023 gives guidance on AI risk management and follows the ISO 31000 process. The table shows where each step of its clause 6 process is carried out in this wiki. Clause numbers and headings were checked against the publisher's contents preview on 15 October 2026; the clause text was not read.

| ISO/IEC 23894 clause | Wiki page |
|---|---|
| 6.2 Communication and consultation | Communication and Consultation, above |
| 6.3 Scope, context and criteria | Risk Appetite and Criteria, and Risk Scale, above; [AI Use-Case Risk Triage](02F_AI_Use_Case_Risk_Triage.md) |
| 6.4.2 Risk identification | [AI Use-Case Risk Triage](02F_AI_Use_Case_Risk_Triage.md); [Enterprise AI Risk Register](02B_Enterprise_AI_Risk_Register.md) |
| 6.4.3 Risk analysis and 6.4.4 Risk evaluation | Rating Factors and Risk Scale, above |
| 6.5 Risk treatment | [AI Risk Treatment Plan](02C_AI_Risk_Treatment_Plan.md); [AI Risk to Control Mapping](02D_AI_Risk_to_Control_Mapping.md) |
| 6.6 Monitoring and review | Review Triggers, above; [AI Risk Review Template](02E_AI_Risk_Review_Template.md) |
| 6.7 Recording and reporting | Required Fields for New AI Risk Entry, above; [Risk, Control and Test Traceability](02G_Risk_Control_Test_Traceability.md) |

NIST publishes a crosswalk from ISO/IEC 23894 to the NIST AI RMF, so this table can be read together with the [NIST AI RMF Crosswalk](../23_Framework_Crosswalks/03_NIST_AI_RMF_Crosswalk.md). See also the [ISO/IEC AI Standards Crosswalk](../23_Framework_Crosswalks/15_ISO_IEC_AI_Standards_Crosswalk.md).
