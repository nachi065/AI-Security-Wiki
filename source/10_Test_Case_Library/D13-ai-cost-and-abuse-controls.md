---
title: "D13 AI Cost and Abuse Controls"
author: Nachiket Sathaye
parent: "Test Case Library"
nav_order: 26
---

<a id="top"></a>

# D13 AI Cost and Abuse Controls

**Focus:** AI cost and abuse controls: attribution, budgets, denial of wallet, key abuse, runaway agents, shadow spend, enforcement

**Controls tested:** [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls (21 cases), [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) AI Discovery (1 case), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) Third-Party and Vendor AI Assurance (1 case), [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) Least Privilege and Scoped Credentials (1 case), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) Agent Containment and Kill Switch (1 case)

**Cases:** 21 (TC-D13-001 to TC-D13-021)  |  **Series:** Emerging domains

> **Safety boundary.** All cases use synthetic data and lab targets only. Use a mock provider, fabricated keys and lab endpoints only. Abuse scripts must never be pointed at real provider accounts or real customer traffic, and tests must never try to defeat a challenge mechanism.

> **How this relates to the layer cases.** Domain cases cross-reference the layer cases they build on (see **Related Layer Cases** in each case). The layer case tests the platform control; the domain case tests the buyer concern from the domain's own point of view. Verify all ATLAS, OWASP and NIST identifiers before use, and treat numeric thresholds as starting values.

## Cases in this domain

| ID | Title | Severity | Method | Controls |
|---|---|---|---|---|
| [TC-D13-001](#tc-d13-001) | Cost Attribution: Tagging Spend to Team, Application, User and Key | High | Technical | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) |
| [TC-D13-002](#tc-d13-002) | Token Accounting Accuracy Against Provider Invoices | High | Technical | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) |
| [TC-D13-003](#tc-d13-003) | Budget Hierarchy and Enforcement: Organisation, Team, Application, User and Key | Critical | Technical | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) |
| [TC-D13-004](#tc-d13-004) | Real-Time Spend Anomaly Detection | High | Technical | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) |
| [TC-D13-005](#tc-d13-005) | Leaked or Stolen API Key: Cost-Spike Detection and Automatic Containment | Critical | Technical | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036), [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) |
| [TC-D13-006](#tc-d13-006) | Denial of Wallet via Public Chatbot Endpoints: Anonymous Traffic Abuse | Critical | Technical | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) |
| [TC-D13-007](#tc-d13-007) | Quota and Credit Abuse: Multi-Account, Free-Tier and Trial Exploitation | High | Technical | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) |
| [TC-D13-008](#tc-d13-008) | Prompt and Output Expansion Abuse: Length and Amplification Limits | High | Technical | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) |
| [TC-D13-009](#tc-d13-009) | Tool Fan-Out and Recursive Agent Cost Explosion | Critical | Technical | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) |
| [TC-D13-010](#tc-d13-010) | Retry Storms, Timeouts and the Cost of Failure Handling | Medium | Technical | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) |
| [TC-D13-011](#tc-d13-011) | Caching and Prefix Reuse: Cost Effects and Cache Abuse | Medium | Technical | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) |
| [TC-D13-012](#tc-d13-012) | Model Routing Cost Controls: Premium Model Misuse and Downgrade Policy | High | Technical | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) |
| [TC-D13-013](#tc-d13-013) | Rate and Concurrency Limits per Identity, Key and Network | High | Technical | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) |
| [TC-D13-014](#tc-d13-014) | Circuit Breakers and Automatic Actions on Budget Breach | Critical | Technical | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) |
| [TC-D13-015](#tc-d13-015) | Batch Jobs, Scheduled Runs and Long-Running Tasks: Timeouts and Spend Ceilings | High | Technical | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) |
| [TC-D13-016](#tc-d13-016) | GPU and Self-Hosted Inference Cost Abuse | High | Technical | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) |
| [TC-D13-017](#tc-d13-017) | Shadow Spend Discovery: Unapproved AI Subscriptions and Direct Provider Accounts | High | Technical | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036), [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) |
| [TC-D13-018](#tc-d13-018) | Spend Approval Workflow for Expensive Models, Features and Contracts | Medium | Technical | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) |
| [TC-D13-019](#tc-d13-019) | Cost Controls for Third-Party and Embedded AI Features | Medium | Evidence | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) |
| [TC-D13-020](#tc-d13-020) | Cost Reporting, Chargeback Evidence and Dispute Handling | Medium | Evidence | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) |
| [TC-D13-021](#tc-d13-021) | Abuse Enforcement Ladder: Warn, Throttle, Suspend and Appeal for Authenticated Users | High | Technical | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) |

---

## Test cases

<a id="tc-d13-001"></a>

### TC-D13-001: Cost Attribution: Tagging Spend to Team, Application, User and Key

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L08, L05 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A, P |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L08-031](L08-ai-gateway-and-security-controls.md#tc-l08-031), [TC-L05-025](L05-ai-applications.md#tc-l05-025) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls |

**Risk Addressed.** Spend that cannot be attributed cannot be controlled, charged back or investigated.

**Business Scenario.** Finance and platform owners want every request's cost tied to a team, application, user and key.

**Technical Scenario.** Generate known usage from several teams and compare attributed cost with ground truth.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** 5 teams, 8 applications, 20 users, 12 keys; 20,000 requests with known token counts; 8 requests with missing or wrong tags; mock pricing for 3 models.

**Procedure**

1. Record the ground truth by team, application, user, key and model.
2. Generate the usage.
3. Pull the attribution report.
4. Compare cost per dimension.
5. Check the handling of untagged and mis-tagged requests.
6. Check tag inheritance (key to application to team).
7. Export the report for chargeback.

**Edge Cases / Variants.** Shared keys; requests routed through an agent acting for a user.

**Expected Detection.** Attributed cost within 2 percent of ground truth per team and application; untagged spend isolated and reported; tag inheritance works; export available.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Export to finance systems.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Attribution vs ground truth.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d13-002"></a>

### TC-D13-002: Token Accounting Accuracy Against Provider Invoices

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L08 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, P |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L08-031](L08-ai-gateway-and-security-controls.md#tc-l08-031) |
| **MITRE ATLAS Mapping** | N/A (assurance control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation and accountability) |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls |

**Risk Addressed.** Platform meters that disagree with provider invoices cause disputes and hide waste.

**Business Scenario.** Finance wants metered usage reconciled with the provider's billing export.

**Technical Scenario.** Compare the platform's counts with a mock provider's billing export.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** 1 week of usage (50,000 requests); mock provider billing export with its own counts; special cases: streaming, cached prompts, retries, tool calls, images and audio, failed requests.

**Procedure**

1. Generate the usage.
2. Export both datasets.
3. Reconcile totals and per-day figures.
4. Investigate differences by case type.
5. Check treatment of cached tokens and retries.
6. Check handling of provider price changes mid-period.
7. Document the reconciliation procedure.

**Edge Cases / Variants.** Provider rounding rules; usage in several currencies.

**Expected Detection.** Totals within 2 percent; differences explained by case type; price changes handled; reconciliation repeatable.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Export.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Reconciliation table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d13-003"></a>

### TC-D13-003: Budget Hierarchy and Enforcement: Organisation, Team, Application, User and Key

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L08 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | Critical |
| **Related Layer Cases** | [TC-L08-031](L08-ai-gateway-and-security-controls.md#tc-l08-031) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls |

**Risk Addressed.** A single global cap protects the organisation but lets one runaway key consume everyone's budget.

**Business Scenario.** Platform owners want nested budgets with defined behaviour at each level.

**Technical Scenario.** Configure nested budgets and drive spend through each level.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** Budgets: organisation 100 units, 3 teams at 30 each, 6 applications at 10 each, 10 users at 2 each, 4 keys at 3 each; load script that reaches each limit in turn.

**Procedure**

1. Configure the hierarchy.
2. Run load to reach the key budget.
3. Check the effect at each level (alert, throttle, block).
4. Reach the application and team budgets.
5. Check that exhausting one team does not stop others.
6. Check carry-over and reset rules.
7. Change a budget and check effect time.

**Edge Cases / Variants.** Budget reached mid-request; budget shared by two applications.

**Expected Detection.** Each level enforced at its limit with the configured action; other teams unaffected; resets on schedule; changes effective within 5 minutes.

**Expected Prevention / Control Action.** Alert, throttle or block per level.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events to SIEM and chat.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Level-by-level table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d13-004"></a>

### TC-D13-004: Real-Time Spend Anomaly Detection

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L08, L17 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, G |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L17-007](L17-monitoring-detection-and-response.md#tc-l17-007), [TC-L09-017](L09-identity-and-access-mgmt.md#tc-l09-017) |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls |

**Risk Addressed.** Monthly invoices find overspend weeks late; spikes need catching in minutes.

**Business Scenario.** Finance and operations want anomalies in spend detected early with context.

**Technical Scenario.** Build a baseline and inject spend anomalies.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** 14 days of simulated baseline across 5 teams; 6 anomalies: sudden spike, slow ramp, off-hours burst, new expensive model, new application, key used from a new network.

**Procedure**

1. Load the baseline.
2. Inject each anomaly.
3. Record detection time and alert content.
4. Check context (who, what, model, key).
5. Run legitimate events (launch day) and check false alarms.
6. Check routing and escalation.
7. Check tuning.

**Edge Cases / Variants.** Gradual drift over many weeks; seasonal peaks.

**Expected Detection.** At least 5 of 6 anomalies detected; spikes within 10 minutes; false alarms on legitimate events under 2 per week; alerts include actor, model and key.

**Expected Prevention / Control Action.** Alert or throttle.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Alerts to chat, SIEM and finance.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Detection table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d13-005"></a>

### TC-D13-005: Leaked or Stolen API Key: Cost-Spike Detection and Automatic Containment

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L09, L08 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, P |
| **Risk Severity** | Critical |
| **Related Layer Cases** | [TC-L09-014](L09-identity-and-access-mgmt.md#tc-l09-014), [TC-L09-017](L09-identity-and-access-mgmt.md#tc-l09-017) |
| **MITRE ATLAS Mapping** | AML.T0055 Unsecured Credentials |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls; [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) Least Privilege and Scoped Credentials |

**Risk Addressed.** A leaked key can run up large bills within minutes, long before anyone reads an invoice.

**Business Scenario.** Security wants misuse of a provider key detected and the key contained automatically.

**Technical Scenario.** Simulate use of a fabricated key from unexpected places and volumes.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** 2 fabricated keys with normal usage profiles; misuse: use from a new network at 20 times normal volume, use of models never previously used, use at an unusual hour, use from two networks at once.

**Procedure**

1. Establish normal use for 3 days (simulated).
2. Run each misuse.
3. Record time to detection and containment.
4. Check actions (throttle, suspend, rotate).
5. Check notification to the owner.
6. Restore with a new key and check application recovery.
7. Check evidence for investigation.

**Edge Cases / Variants.** Key used within normal volume but from a hostile network; key shared by design between two sites.

**Expected Detection.** Misuse detected within 5 minutes; key suspended automatically per policy; owner notified; application recovers with the new key within the stated time.

**Expected Prevention / Control Action.** Suspend key.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events to SIEM.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Timeline.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d13-006"></a>

### TC-D13-006: Denial of Wallet via Public Chatbot Endpoints: Anonymous Traffic Abuse

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L08, L05 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | Critical |
| **Related Layer Cases** | [TC-L08-030](L08-ai-gateway-and-security-controls.md#tc-l08-030), [TC-L08-023](L08-ai-gateway-and-security-controls.md#tc-l08-023) |
| **MITRE ATLAS Mapping** | AML.T0029 Denial of AI Service; AML.T0034 Cost Harvesting |
| **OWASP LLM / GenAI Mapping** | LLM10:2025 Unbounded Consumption |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls |

**Risk Addressed.** Public chat endpoints can be driven by automated traffic to burn budget, with no account to block.

**Business Scenario.** Security wants per-address, per-session and global limits and abuse signals on anonymous endpoints.

**Technical Scenario.** Drive scripted anonymous traffic at a lab public chatbot.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** 1 lab public chatbot; scripts: single address at high rate, 500 addresses at low rate, long-prompt flood, session cycling, replay of identical requests; challenge mechanism available in the lab; spend cap.

**Procedure**

1. Configure per-address, per-session and global limits and the challenge mechanism.
2. Run each script.
3. Record when limits and challenges activate and the spend incurred.
4. Check legitimate users during the attack.
5. Check alerts.
6. Check cost per blocked request.
7. Document that the test never attempts to defeat the challenge mechanism.

**Edge Cases / Variants.** Distributed low-rate traffic; traffic from a cloud provider range.

**Expected Detection.** Spend during each attack capped at the configured ceiling; legitimate users still served; alerts within 5 minutes; limits and challenges activate as configured.

**Expected Prevention / Control Action.** Throttle or challenge.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events to SIEM.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Attack table; spend chart.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d13-007"></a>

### TC-D13-007: Quota and Credit Abuse: Multi-Account, Free-Tier and Trial Exploitation

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L08, L05 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: A, G |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L08-030](L08-ai-gateway-and-security-controls.md#tc-l08-030) |
| **MITRE ATLAS Mapping** | AML.T0029 Denial of AI Service; AML.T0034 Cost Harvesting |
| **OWASP LLM / GenAI Mapping** | LLM10:2025 Unbounded Consumption |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls |

**Risk Addressed.** Free tiers, trials and credits attract mass account creation that drains budget and masks other abuse.

**Business Scenario.** Product owners want signup and credit abuse detected and limited.

**Technical Scenario.** Create many lab accounts and consume trial credits.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** 1 lab service with free tier and referral credits; 200 scripted accounts from a small set of addresses and devices; 20 genuine accounts.

**Procedure**

1. Run the scripted signup waves.
2. Check detection signals (address, device, email patterns, behaviour).
3. Check limits on credits and tier.
4. Check effect on genuine accounts.
5. Check review and appeal path for wrongly flagged accounts.
6. Check reporting on credit spend by cohort.

**Edge Cases / Variants.** Referral rings; accounts created slowly over weeks.

**Expected Detection.** At least 85 percent of scripted accounts limited before consuming more than 20 percent of the credit pool; genuine accounts affected under 5 percent; appeal path works.

**Expected Prevention / Control Action.** Limit or review.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events to the abuse team.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Cohort table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d13-008"></a>

### TC-D13-008: Prompt and Output Expansion Abuse: Length and Amplification Limits

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L12, L08 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L12-022](L12-model-layer.md#tc-l12-022), [TC-L07-032](L07-prompt-and-context-layer.md#tc-l07-032) |
| **MITRE ATLAS Mapping** | AML.T0029 Denial of AI Service; AML.T0034 Cost Harvesting |
| **OWASP LLM / GenAI Mapping** | LLM10:2025 Unbounded Consumption |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls |

**Risk Addressed.** Prompts that demand very long outputs or expand repeatedly multiply cost per request.

**Business Scenario.** Operations wants input, output and total-token ceilings enforced per request and per session.

**Technical Scenario.** Send expansion-style prompts and compare cost with ceilings.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** 12 prompts: maximum-length requests, repeat-until-limit, nested expansion, translate into many languages, long document summary (legitimate), conversation growing every turn; ceilings: 4,000 output tokens, 20,000 context tokens, 100,000 per session.

**Procedure**

1. Set ceilings.
2. Run the prompts.
3. Record tokens and cost per request.
4. Check truncation behaviour and messages.
5. Check legitimate long requests still complete.
6. Check session-level accumulation.
7. Check alerts for repeated ceiling hits.

**Edge Cases / Variants.** Streaming responses cut mid-sentence; hidden reasoning tokens counted.

**Expected Detection.** No request exceeds the ceilings; legitimate long summary completes; session ceiling enforced; alerts on repeated hits.

**Expected Prevention / Control Action.** Truncate or block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events with token counts.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Token table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d13-009"></a>

### TC-D13-009: Tool Fan-Out and Recursive Agent Cost Explosion

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L06, L08 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | Critical |
| **Related Layer Cases** | [TC-L06-021](L06-agent-orchestration-layer.md#tc-l06-021), [TC-L06-024](L06-agent-orchestration-layer.md#tc-l06-024) |
| **MITRE ATLAS Mapping** | AML.T0053 AI Agent Tool Invocation |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls; [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) Agent Containment and Kill Switch |

**Risk Addressed.** One request that triggers hundreds of tool calls, model calls and sub-agents can cost far more than expected.

**Business Scenario.** Operations wants cost caps per task and per agent, with early warning before the cap.

**Technical Scenario.** Run scripted agents that fan out, loop and spawn sub-agents against a mock provider.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** 4 behaviours: fan-out to 200 tool calls, loop of repeated retries, recursive sub-agent spawning to depth 8, parallel agents sharing one budget; per-task cap of 50 units, per-agent cap of 200.

**Procedure**

1. Configure caps and early-warning thresholds.
2. Run each behaviour.
3. Record cost at stop and the stopping mechanism.
4. Check partial results preserved.
5. Check legitimate multi-step tasks (30 calls) complete.
6. Check attribution of cost to the initiating user.
7. Check alerts.

**Edge Cases / Variants.** Costs incurred by external tools billed separately; sub-agents using another provider.

**Expected Detection.** Each behaviour stopped before 110 percent of its cap; legitimate task completes; cost attributed; alert at the warning threshold.

**Expected Prevention / Control Action.** Stop task.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events to SIEM.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Cost-at-stop table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d13-010"></a>

### TC-D13-010: Retry Storms, Timeouts and the Cost of Failure Handling

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L08 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | Medium |
| **Related Layer Cases** | [TC-L08-033](L08-ai-gateway-and-security-controls.md#tc-l08-033) |
| **MITRE ATLAS Mapping** | AML.T0029 Denial of AI Service; AML.T0034 Cost Harvesting |
| **OWASP LLM / GenAI Mapping** | LLM10:2025 Unbounded Consumption |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls |

**Risk Addressed.** Poorly tuned retries multiply cost during provider trouble and can overload the service further.

**Business Scenario.** Operations wants retry, timeout and backoff settings that limit cost and amplification.

**Technical Scenario.** Inject provider errors and slow responses and measure request and cost amplification.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** Mock provider with error rates of 10, 30 and 60 percent, slow responses at 10 times normal, rate limit responses; 5,000 requests; retry settings: none, fixed, exponential with jitter.

**Procedure**

1. Record baseline cost.
2. Inject each condition under each retry setting.
3. Measure requests sent per original request and total cost.
4. Check circuit-breaker behaviour.
5. Check idempotency of billed calls.
6. Check user-visible behaviour.
7. Check alerts on amplification.

**Edge Cases / Variants.** Retries across two layers (SDK and gateway) multiplying each other.

**Expected Detection.** Amplification under 1.5 times at 30 percent errors with recommended settings; circuit breaker opens at the stated threshold; alerts raised.

**Expected Prevention / Control Action.** Circuit-break.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Metrics to monitoring.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Amplification table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d13-011"></a>

### TC-D13-011: Caching and Prefix Reuse: Cost Effects and Cache Abuse

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L08, L10 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | Medium |
| **Related Layer Cases** | [TC-L08-031](L08-ai-gateway-and-security-controls.md#tc-l08-031), [TC-L10-010](L10-data-layer.md#tc-l10-010) |
| **MITRE ATLAS Mapping** | AML.T0029 Denial of AI Service; AML.T0034 Cost Harvesting |
| **OWASP LLM / GenAI Mapping** | LLM10:2025 Unbounded Consumption |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls |

**Risk Addressed.** Caching cuts cost when it works, and attackers or bad configuration can bypass it to push cost up or poison what is cached.

**Business Scenario.** Operations wants cache behaviour measured and protected against cost-driving bypass.

**Technical Scenario.** Run repeated and varied requests with caching enabled and attempt to defeat it.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** 1 application with response and prefix caching; 2,000 requests: 60 percent repeated, 40 percent unique; bypass attempts: tiny random changes to each prompt, unique session identifiers, cache-control manipulation; cache poisoning probe with a canary answer.

**Procedure**

1. Measure cost and hit rate with legitimate repetition.
2. Run the bypass attempts.
3. Record hit rate and cost change.
4. Check detection of cache-bypass patterns.
5. Check that cache entries are isolated by user or tenant.
6. Probe cache poisoning and check that the canary answer does not reach another user.
7. Check cache expiry and invalidation.

**Edge Cases / Variants.** Cache shared across tenants by design; provider-side caching outside the platform's control.

**Expected Detection.** Hit rate at least 50 percent on repeated traffic; bypass patterns flagged; no cross-user cache contamination; invalidation works.

**Expected Prevention / Control Action.** Flag or limit.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Metrics to monitoring.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Hit-rate table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d13-012"></a>

### TC-D13-012: Model Routing Cost Controls: Premium Model Misuse and Downgrade Policy

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L12, L08 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L12-021](L12-model-layer.md#tc-l12-021), [TC-L08-028](L08-ai-gateway-and-security-controls.md#tc-l08-028) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls |

**Risk Addressed.** Routing everything to the most expensive model, or silently to a cheaper and weaker one, changes both cost and risk.

**Business Scenario.** Platform owners want model choice governed by purpose, budget and policy.

**Technical Scenario.** Configure routing rules and test premium, standard and fallback paths.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** 3 models (premium, standard, small) with different prices and policy status; 4 request classes (sensitive, routine, bulk, experimental); rules by class, user and budget level; 300 requests.

**Procedure**

1. Set the routing policy.
2. Send each class.
3. Record model chosen and cost.
4. Attempt to request the premium model directly for routine work.
5. Check automatic downgrade near a budget limit and notification.
6. Check that downgrades respect security policy (sensitive data never goes to a non-approved model).
7. Check reports on premium usage.

**Edge Cases / Variants.** Model alias changing price; fallback to a model in a different region.

**Expected Detection.** Routing matches policy for at least 98 percent of requests; direct premium requests handled per rule; downgrades never violate security policy; reports accurate.

**Expected Prevention / Control Action.** Route or deny.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Decision logs.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Routing table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d13-013"></a>

### TC-D13-013: Rate and Concurrency Limits per Identity, Key and Network

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L08 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L08-030](L08-ai-gateway-and-security-controls.md#tc-l08-030) |
| **MITRE ATLAS Mapping** | AML.T0029 Denial of AI Service; AML.T0034 Cost Harvesting |
| **OWASP LLM / GenAI Mapping** | LLM10:2025 Unbounded Consumption |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls |

**Risk Addressed.** Limits set only globally let one user, key or address crowd out everyone else.

**Business Scenario.** Operations wants fair limits at several levels with predictable behaviour.

**Technical Scenario.** Apply layered limits and test fairness and burst behaviour.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** 20 users, 6 keys, 3 networks; limits: 60 requests per minute per user, 300 per key, 1,000 per network, concurrency 5 per user; load scripts: steady, burst of 200, sustained over-limit from one user.

**Procedure**

1. Configure the limits.
2. Run steady load and confirm no throttling.
3. Run the burst.
4. Run the over-limit user.
5. Record effect on others.
6. Check responses and retry guidance.
7. Check limit changes and effect time.

**Edge Cases / Variants.** Many users behind one network address; limit applied to a key used by many users.

**Expected Detection.** Limits enforced at each level; others unaffected by the over-limit user; clear responses; changes effective within 5 minutes.

**Expected Prevention / Control Action.** Throttle.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events with limit name.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Fairness table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d13-014"></a>

### TC-D13-014: Circuit Breakers and Automatic Actions on Budget Breach

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L08 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | Critical |
| **Related Layer Cases** | [TC-L08-031](L08-ai-gateway-and-security-controls.md#tc-l08-031) |
| **MITRE ATLAS Mapping** | AML.T0053 AI Agent Tool Invocation |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls |

**Risk Addressed.** Alerts that nobody reads at 3am do not stop spend; automatic actions can also take essential services down.

**Business Scenario.** Operations wants graded automatic actions that protect budget and keep critical services running.

**Technical Scenario.** Configure graded actions and trigger them in sequence.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** Budget with thresholds at 70, 90 and 100 percent; actions: notify, throttle non-critical applications, switch to a cheaper model, suspend non-critical applications, suspend all; 3 critical and 5 non-critical applications; manual override.

**Procedure**

1. Configure the thresholds and actions.
2. Drive spend through each threshold.
3. Record the actions and timing.
4. Check that critical applications are exempt or protected.
5. Check notification content.
6. Use the manual override and check audit.
7. Reset and check restoration.

**Edge Cases / Variants.** Breach caused by a legitimate event; override abused.

**Expected Detection.** Each action occurs at its threshold within 2 minutes; critical applications remain available; override audited; restoration works.

**Expected Prevention / Control Action.** Graded automatic actions.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events to chat and ticketing.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Threshold table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d13-015"></a>

### TC-D13-015: Batch Jobs, Scheduled Runs and Long-Running Tasks: Timeouts and Spend Ceilings

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L06, L08 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A, P |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L06-024](L06-agent-orchestration-layer.md#tc-l06-024) |
| **MITRE ATLAS Mapping** | AML.T0029 Denial of AI Service; AML.T0034 Cost Harvesting |
| **OWASP LLM / GenAI Mapping** | LLM10:2025 Unbounded Consumption |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls |

**Risk Addressed.** Overnight jobs run unattended, so a bug or bad input can burn budget for hours.

**Business Scenario.** Operations wants ceilings and timeouts for jobs that nobody watches.

**Technical Scenario.** Run scheduled jobs with defects and check ceilings.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** 4 jobs: nightly summarisation (normal), job with an infinite loop, job processing an unexpectedly large input set, job retrying a failing step forever; ceilings: time 2 hours, spend 40 units, calls 5,000.

**Procedure**

1. Configure ceilings per job.
2. Run the normal job.
3. Run each faulty job.
4. Record when each stops and the cost.
5. Check partial results and job state.
6. Check alerts and the report in the morning.
7. Check that ceilings can be raised only with approval.

**Edge Cases / Variants.** Job spanning midnight budget reset; job restarted automatically by a scheduler.

**Expected Detection.** Faulty jobs stopped at or below their ceilings; normal job unaffected; alerts and report produced; ceiling increases approved and logged.

**Expected Prevention / Control Action.** Stop job.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Alerts to owners.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Job table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d13-016"></a>

### TC-D13-016: GPU and Self-Hosted Inference Cost Abuse

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L15, L13 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, E |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L13-020](L13-training-and-fine-tuning-layer.md#tc-l13-020), [TC-L15-017](L15-infrastructure-layer.md#tc-l15-017) |
| **MITRE ATLAS Mapping** | AML.T0029 Denial of AI Service; AML.T0034 Cost Harvesting |
| **OWASP LLM / GenAI Mapping** | LLM10:2025 Unbounded Consumption |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls |

**Risk Addressed.** Self-hosted capacity costs money whether it is used well or not, and spare capacity attracts misuse.

**Business Scenario.** Operations wants idle capacity, oversized allocations and unauthorised jobs found.

**Technical Scenario.** Create misuse patterns on lab self-hosted capacity.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** Lab cluster with 8 GPU units; patterns: idle allocation held for days, oversized request for small work, unauthorised training job, unusual continuous high load, jobs submitted by a service account.

**Procedure**

1. Define approved usage and quotas.
2. Create each pattern.
3. Check detection and alerts.
4. Check cost attribution to teams.
5. Check reclaim actions for idle capacity.
6. Check approval for large requests.
7. Report utilisation and waste.

**Edge Cases / Variants.** Spot capacity pre-empted; shared capacity between teams.

**Expected Detection.** All patterns detected within the stated interval; idle capacity reclaimed per policy; waste report accurate.

**Expected Prevention / Control Action.** Reclaim or stop.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Alerts to platform and finance.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Pattern table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d13-017"></a>

### TC-D13-017: Shadow Spend Discovery: Unapproved AI Subscriptions and Direct Provider Accounts

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L04, L05 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, E |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L04-001](L04-human-interaction-layer.md#tc-l04-001), [TC-L05-001](L05-ai-applications.md#tc-l05-001) |
| **MITRE ATLAS Mapping** | N/A (visibility control); Reconnaissance/Discovery context only |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (unmanaged AI components) |
| **NIST AI RMF Mapping** | MAP 1.1; GOVERN 6.1 |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls; [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) AI Discovery |

**Risk Addressed.** AI services bought on cards and expense claims sit outside central budgets and security review.

**Business Scenario.** Finance and security want unapproved AI spend found through billing, expense and network signals.

**Technical Scenario.** Seed spending signals across several sources and compare discovery with ground truth.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** 25 signals: 8 card or expense lines for AI subscriptions, 5 direct provider accounts, 4 browser-based subscriptions seen in traffic, 4 SaaS add-ons, 4 approved subscriptions; mock billing export and expense feed.

**Procedure**

1. Record ground truth.
2. Load the feeds.
3. Run discovery.
4. Compare findings.
5. Check matching to approved vendors and owners.
6. Route one finding for review and close with a decision.
7. Report spend by category.

**Edge Cases / Variants.** Subscription paid by an individual and reclaimed later; per-seat price changes.

**Expected Detection.** At least 18 of 21 unapproved items found; approved ones not flagged; routing and decision recorded.

**Expected Prevention / Control Action.** Review and approve or stop.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Feed integrations.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Discovery table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d13-018"></a>

### TC-D13-018: Spend Approval Workflow for Expensive Models, Features and Contracts

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L02, L08 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, G |
| **Risk Severity** | Medium |
| **Related Layer Cases** | [TC-L02-010](L02-governance-and-risk-mgmt.md#tc-l02-010) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls |

**Risk Addressed.** Costly choices made by individual teams commit the organisation beyond its plan.

**Business Scenario.** Finance wants approval thresholds for premium models, large allocations and new contracts.

**Technical Scenario.** Submit requests of different sizes and track approvals.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** 8 requests: premium model access, new application budget, budget increase, GPU allocation, long-term commitment, small experiment, emergency increase, request that exceeds the requester's authority.

**Procedure**

1. Configure thresholds and approvers.
2. Submit the requests.
3. Check routing.
4. Approve and reject.
5. Check that approved changes take effect in the platform and rejected ones do not.
6. Check emergency path and review.
7. Check records.

**Edge Cases / Variants.** Request split into several smaller ones to avoid the threshold.

**Expected Detection.** Routing by threshold; approvals applied to actual settings; emergency path time-limited and reviewed; records complete.

**Expected Prevention / Control Action.** Gate.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Ticketing and finance integration.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Request records.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d13-019"></a>

### TC-D13-019: Cost Controls for Third-Party and Embedded AI Features

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L05, L16 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: P, W |
| **Risk Severity** | Medium |
| **Related Layer Cases** | [TC-L05-005](L05-ai-applications.md#tc-l05-005), [TC-L16-010](L16-supply-chain-and-third-party.md#tc-l16-010) |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls; [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) Third-Party and Vendor AI Assurance |

**Risk Addressed.** AI add-ons inside other products are metered by the vendor, with limits and overage prices the buyer rarely sees.

**Business Scenario.** Finance wants usage limits, overage terms and usage visibility for embedded AI features.

**Technical Scenario.** Review three lab SaaS products with AI add-ons and test visibility and controls.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** 3 mock SaaS tenants with AI features, usage meters, caps and overage prices; 4 weeks of simulated usage including one overage.

**Procedure**

1. List the AI features, plans and caps.
2. Check usage visibility to the customer.
3. Check alert options near caps.
4. Cause an overage and check billing treatment.
5. Check the ability to disable the feature or set a spending limit.
6. Check contract terms on price changes.
7. Record gaps.

**Edge Cases / Variants.** Feature enabled by default for all users; usage metered per action rather than per token.

**Expected Detection.** Usage visible to the customer; cap alerts available; overage treatment documented; disable or limit control exists; gaps recorded.

**Expected Prevention / Control Action.** Limit.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Usage export.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Feature table.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to domain index](#top)

---

<a id="tc-d13-020"></a>

### TC-D13-020: Cost Reporting, Chargeback Evidence and Dispute Handling

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L08, L02 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: G, P, W |
| **Risk Severity** | Medium |
| **Related Layer Cases** | [TC-L08-031](L08-ai-gateway-and-security-controls.md#tc-l08-031) |
| **MITRE ATLAS Mapping** | N/A (assurance control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation and accountability) |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls |

**Risk Addressed.** Teams contest charges they cannot trace, and auditors want to see how costs were allocated.

**Business Scenario.** Finance wants reports and an evidence trail for allocations and disputes.

**Technical Scenario.** Produce chargeback reports and run a dispute through the evidence trail.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** 1 month of usage for 5 teams; 2 disputed charges (a key shared by two teams, a spike during an attack); allocation rules.

**Procedure**

1. Generate the monthly report.
2. Check against ground truth.
3. Open the two disputes.
4. Trace each to request-level evidence.
5. Adjust allocation with approval.
6. Check audit of adjustments.
7. Export evidence for finance.

**Edge Cases / Variants.** Retroactive tag changes; shared platform costs.

**Expected Detection.** Report matches ground truth; disputes traced to requests; adjustments approved and audited; export complete.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Finance export.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Dispute records.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to domain index](#top)

---

<a id="tc-d13-021"></a>

### TC-D13-021: Abuse Enforcement Ladder: Warn, Throttle, Suspend and Appeal for Authenticated Users

| Field | Value |
|---|---|
| **Use-Case Domain** | D13: AI Cost and Abuse Controls |
| **Lifecycle Layer(s)** | L08, L05 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: A, G, W |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L08-030](L08-ai-gateway-and-security-controls.md#tc-l08-030), [TC-L08-039](L08-ai-gateway-and-security-controls.md#tc-l08-039) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls |

**Risk Addressed.** Authenticated users can abuse allowances by automation, sharing accounts or hammering expensive features, and heavy-handed bans harm genuine users.

**Business Scenario.** Product owners want graded, auditable actions with an appeal route.

**Technical Scenario.** Run abuse patterns by lab users and walk the enforcement ladder.

**Preconditions.** Isolated PoC lab provisioned; lab applications and gateway pointed at a mock provider with per-token pricing, fabricated keys and budgets, abuse scripts acting only on lab endpoints and a mock billing export seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md). Lab AI applications and a gateway pointed at a mock provider with per-token pricing and configurable rate limits; fabricated keys, accounts and budgets; load and abuse scripts that act only against lab endpoints; a mock billing export and expense feed; no real provider accounts, spend or customer traffic.

**Test Data.** 10 lab users: 4 abusers (automation, account sharing, repeated limit testing, resale of access), 3 heavy genuine users, 3 normal users; ladder: warn, throttle, temporary suspend, permanent suspend; appeal workflow.

**Procedure**

1. Configure the ladder and thresholds.
2. Run the behaviours.
3. Record the actions and timing per user.
4. Check messages.
5. Check that genuine heavy users are not suspended.
6. File and decide an appeal.
7. Check audit and reporting.

**Edge Cases / Variants.** Abuser who changes accounts; heavy user with a legitimate batch need.

**Expected Detection.** Abusers reach the correct rung within the stated time; genuine heavy users not suspended; appeals tracked and decided; audit complete.

**Expected Prevention / Control Action.** Warn, throttle or suspend.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Spend, budget and abuse state visible in the cost and abuse dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events to the abuse team.

**Forensic Evidence.** Request, key, user, application, team, model, tokens, cost, policy decision and timestamp exportable for investigation, chargeback and dispute handling.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Ladder table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

