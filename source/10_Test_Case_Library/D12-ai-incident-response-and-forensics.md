---
title: "D12 AI Incident Response and Forensics"
author: Nachiket Sathaye
parent: "Test Case Library"
nav_order: 25
---

<a id="top"></a>

# D12 AI Incident Response and Forensics

**Focus:** AI incident response and forensics: taxonomy, state preservation, replay, scoping, containment, provider coordination, evidence handling

**Controls tested:** [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035)

**Cases:** 22 (TC-D12-001 to TC-D12-022)  |  **Series:** Emerging domains

> **Safety boundary.** All cases use synthetic data and lab targets only. Use scripted lab incidents with known ground truth and fabricated data only. Never run lab exercises against production systems or real incidents.

> **How this relates to the layer cases.** Domain cases cross-reference the layer cases they build on (see **Related Layer Cases** in each case). The layer case tests the platform control; the domain case tests the buyer concern from the domain's own point of view. Verify all ATLAS, OWASP and NIST identifiers before use, and treat numeric thresholds as starting values.

## Cases in this domain

| ID | Title | Severity | Method |
|---|---|---|---|
| [TC-D12-001](#tc-d12-001) | AI Incident Taxonomy and Severity Classification | High | Evidence |
| [TC-D12-002](#tc-d12-002) | AI Incident Intake: Detection Alerts, User Reports and Third-Party Notices | High | Technical |
| [TC-D12-003](#tc-d12-003) | Triage Runbooks by AI Incident Type | Critical | Technical |
| [TC-D12-004](#tc-d12-004) | Preserving AI System State at Incident Time: Model, Prompt, Configuration, Tools and Policy | Critical | Technical |
| [TC-D12-005](#tc-d12-005) | Retrieval Index and Knowledge Snapshots for Forensics | High | Technical |
| [TC-D12-006](#tc-d12-006) | Reconstructing What the Model Saw: Context, Memory and Retrieved Content | Critical | Technical |
| [TC-D12-007](#tc-d12-007) | Deterministic Replay: Reproducing an Incident with Pinned Versions and Recorded Inputs | High | Technical |
| [TC-D12-008](#tc-d12-008) | Attribution Analysis: Attacker, Insider, Misconfiguration or Model Fault | High | Technical |
| [TC-D12-009](#tc-d12-009) | Scoping and Blast Radius: Users, Data, Systems and Outputs Affected | Critical | Technical |
| [TC-D12-010](#tc-d12-010) | Downstream Propagation of Harmful or False Outputs | High | Technical |
| [TC-D12-011](#tc-d12-011) | Containment Option Catalogue and Selection Guidance | Critical | Technical |
| [TC-D12-012](#tc-d12-012) | Eradication and Recovery Validation | High | Technical |
| [TC-D12-013](#tc-d12-013) | Poisoning and Training-Data Incident Forensics | Critical | Technical |
| [TC-D12-014](#tc-d12-014) | Model Behaviour Regression Incident | High | Technical |
| [TC-D12-015](#tc-d12-015) | Harm Assessment and Affected-Person Identification | Critical | Technical |
| [TC-D12-016](#tc-d12-016) | Notification Decision and Communications (Framework-Neutral) | Critical | Technical |
| [TC-D12-017](#tc-d12-017) | Third-Party and Model-Provider Incident Coordination | High | Evidence |
| [TC-D12-018](#tc-d12-018) | Evidence Handling for AI Artefacts and Chain of Custody | Critical | Technical |
| [TC-D12-019](#tc-d12-019) | Forensic Tooling Access, Separation of Duties and Audit | High | Technical |
| [TC-D12-020](#tc-d12-020) | AI Root-Cause Analysis Method and Recurrence Tracking | High | Evidence |
| [TC-D12-021](#tc-d12-021) | Near-Miss and Blocked-Attack Learning | Medium | Technical |
| [TC-D12-022](#tc-d12-022) | AI Incident Register, Metrics and Trend Analysis | Medium | Evidence |

---

## Test cases

<a id="tc-d12-001"></a>

### TC-D12-001: AI Incident Taxonomy and Severity Classification

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L17, L02 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L17-018](L17-monitoring-detection-and-response.md#tc-l17-018), [TC-L17-026](L17-monitoring-detection-and-response.md#tc-l17-026) |
| **MITRE ATLAS Mapping** | N/A (response control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE (incident response and communication) |

**Risk Addressed.** Without agreed incident types and severity criteria, AI events are handled inconsistently, under-reported or escalated too late.

**Business Scenario.** Security and risk want a taxonomy and severity scheme specific to AI incidents, configured in the platform.

**Technical Scenario.** Configure the taxonomy and run twelve scripted events through classification.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** 12 scripted events: prompt-injection data leak, agent taking an unapproved action, poisoned knowledge document, model update causing unsafe outputs, harmful output reaching a customer, biased decision pattern, supply chain compromise of a component, credential theft, runaway cost event, outage of an AI service, privacy complaint about an output, near-miss blocked attack; severity criteria (impact, scope, data, reversibility) and categories set by the assessor.

**Procedure**

1. Enter the taxonomy and severity criteria.
2. Classify the 12 events using the platform.
3. Compare classifications with an expert reviewer's answers.
4. Check that criteria are visible when classifying.
5. Check re-classification when facts change.
6. Check that classification drives workflow (routing, deadlines, notification triggers).
7. Check reports by category.

**Edge Cases / Variants.** Events that fit two categories; events starting as low and escalating.

**Expected Detection.** At least 10 of 12 classifications agree with the expert; criteria visible at classification time; re-classification audited; classification drives routing and deadlines.

**Expected Prevention / Control Action.** Route by severity.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Taxonomy export to ticketing and SIEM.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Classification comparison.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to domain index](#top)

---

<a id="tc-d12-002"></a>

### TC-D12-002: AI Incident Intake: Detection Alerts, User Reports and Third-Party Notices

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L17 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P, A |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L17-016](L17-monitoring-detection-and-response.md#tc-l17-016), [TC-L17-017](L17-monitoring-detection-and-response.md#tc-l17-017) |
| **MITRE ATLAS Mapping** | N/A (response control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE (incident response and communication) |

**Risk Addressed.** Many AI incidents are first noticed by users, staff or providers, not by tools, and need a defined way in.

**Business Scenario.** Operations wants every intake route working and every report triaged within a set time.

**Technical Scenario.** Submit reports through each intake route and track handling.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** 6 routes: platform alert, in-application report of harmful or wrong output, staff email or form, customer complaint, provider notice, regulator or media enquiry (simulated); 18 reports with different severity, 3 duplicates, 2 incomplete.

**Procedure**

1. Submit the reports through each route.
2. Check creation of incident records and links to evidence.
3. Check duplicate detection and merging.
4. Check handling of incomplete reports (request for details).
5. Measure time to acknowledgement and triage.
6. Check protection of reporter identity where requested.
7. Check reporting on volume by route.

**Edge Cases / Variants.** Report in Arabic; report from a person who is not an employee.

**Expected Detection.** All 6 routes create records; duplicates merged; incomplete reports followed up; acknowledgement within the stated time; reporter identity protected where requested.

**Expected Prevention / Control Action.** Triage.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Ticketing integration.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Intake record table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d12-003"></a>

### TC-D12-003: Triage Runbooks by AI Incident Type

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L17 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | Critical |
| **Related Layer Cases** | [TC-L17-018](L17-monitoring-detection-and-response.md#tc-l17-018), [TC-L17-019](L17-monitoring-detection-and-response.md#tc-l17-019) |
| **MITRE ATLAS Mapping** | N/A (response control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE (incident response and communication) |

**Risk Addressed.** Generic runbooks do not tell responders what to check first when the problem is a model, an index or an agent.

**Business Scenario.** Responders want type-specific triage steps and decision support inside the platform.

**Technical Scenario.** Run six scripted incidents through type-specific runbooks and measure completeness and time to scope.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** 6 runbooks: injection with data leak, agent misuse, poisoned retrieval source, model regression, harmful output, vendor or model-provider incident; 6 scripted incidents with ground-truth causes; 2 responders.

**Procedure**

1. Load the runbooks.
2. Start each incident with the initial alert only.
3. Have responders follow the runbook.
4. Record steps taken, evidence pulled and time to a first scope statement.
5. Compare conclusions with ground truth.
6. Check where the platform provides queries, links and actions directly from the runbook.
7. Collect responder feedback on gaps.

**Edge Cases / Variants.** Incident that matches two runbooks; responder new to AI incidents.

**Expected Detection.** First scope statement within 30 minutes for at least 5 of 6 incidents; conclusions match ground truth in at least 5; runbook steps link to platform queries and actions.

**Expected Prevention / Control Action.** Guided response.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Runbook export.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Exercise log.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d12-004"></a>

### TC-D12-004: Preserving AI System State at Incident Time: Model, Prompt, Configuration, Tools and Policy

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L17, L14, L12 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, A |
| **Risk Severity** | Critical |
| **Related Layer Cases** | [TC-L17-021](L17-monitoring-detection-and-response.md#tc-l17-021), [TC-L12-018](L12-model-layer.md#tc-l12-018) |
| **MITRE ATLAS Mapping** | N/A (assurance control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation and accountability) |

**Risk Addressed.** Logs show what happened but not what exactly was running; prompts, models, tool definitions and policies change often.

**Business Scenario.** Investigators want a point-in-time record of every component that shaped the incident.

**Technical Scenario.** Run an application through a change history, trigger an incident and capture state at the time.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** 1 application with 6 changes over a simulated month (model version, system prompt edits, tool added, guardrail rule changed, retrieval setting changed, policy changed); incident at a known time.

**Procedure**

1. Make the six changes at recorded times.
2. Trigger the incident.
3. Ask the platform for the full state at the incident time.
4. Compare with the change record.
5. Check completeness: model identifier and version, system prompt version, tool and MCP definitions, guardrail and policy versions, retrieval configuration, feature flags.
6. Request the state at an earlier time and check accuracy.
7. Check that the snapshot is tamper-evident.

**Edge Cases / Variants.** Change made outside the platform; component updated by a provider without notice.

**Expected Detection.** State at incident time matches the change record for every component; earlier-time query accurate; snapshot tamper-evident and exportable.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Export for case file.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** State snapshot; comparison with change record.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d12-005"></a>

### TC-D12-005: Retrieval Index and Knowledge Snapshots for Forensics

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L11, L17 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, A |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L11-011](L11-knowledge-and-retrieval-layer.md#tc-l11-011), [TC-L17-020](L17-monitoring-detection-and-response.md#tc-l17-020) |
| **MITRE ATLAS Mapping** | N/A (assurance control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation and accountability) |

**Risk Addressed.** If the index has changed since the incident, investigators cannot tell what the assistant could retrieve at the time.

**Business Scenario.** Investigators want the content and ranking of the knowledge base reconstructable at a past date.

**Technical Scenario.** Modify a lab knowledge base over time and reconstruct its state at the incident time.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** 1 RAG application; 200 documents; 30 changes over a simulated month (additions, edits, deletions, permission changes); incident at a known time involving a poisoned document later removed.

**Procedure**

1. Make the changes at recorded times.
2. Trigger the incident.
3. Remove the poisoned document afterwards.
4. Ask the platform for the index state at incident time.
5. Check that the removed document and its permissions are shown.
6. Re-run the incident query against the reconstructed state if supported.
7. Check storage cost and retention of snapshots.

**Edge Cases / Variants.** Embedding model changed since the incident; document edited in place.

**Expected Detection.** Reconstructed state includes the removed document and correct permissions; query against the reconstructed state returns the original result or variance is explained; retention stated.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Export.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Reconstruction comparison.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d12-006"></a>

### TC-D12-006: Reconstructing What the Model Saw: Context, Memory and Retrieved Content

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L17, L05 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: A, G, P |
| **Risk Severity** | Critical |
| **Related Layer Cases** | [TC-L17-020](L17-monitoring-detection-and-response.md#tc-l17-020), [TC-L05-025](L05-ai-applications.md#tc-l05-025) |
| **MITRE ATLAS Mapping** | N/A (assurance control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation and accountability) |

**Risk Addressed.** The answer depends on everything in the context window, including memory, retrieved chunks and tool results the user never saw.

**Business Scenario.** Investigators want the complete model input for any response, not only the user's prompt.

**Technical Scenario.** Run five conversations with memory, retrieval and tool calls and reconstruct the model inputs.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** 5 conversations: with persistent memory entries, with retrieved chunks from 3 documents, with 2 tool results, with a system prompt update mid-session, with a truncated context; incident on one response.

**Procedure**

1. Run the conversations.
2. Select the incident response.
3. Ask the platform to reconstruct the exact model input.
4. Compare with the recorded inputs (full prompt assembly).
5. Check inclusion of memory entries, chunk text and identifiers, tool results, system and developer messages and truncation points.
6. Check masking and access controls.
7. Check that the reconstruction notes which parts could not be recovered.

**Edge Cases / Variants.** Streaming responses; conversations spanning several sessions.

**Expected Detection.** At least 4 of 5 reconstructions complete; truncation points shown; missing parts identified; access controlled and masked.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Export.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Reconstruction table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d12-007"></a>

### TC-D12-007: Deterministic Replay: Reproducing an Incident with Pinned Versions and Recorded Inputs

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L17, L12, L14 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, A |
| **Risk Severity** | High |
| **Related Layer Cases** | TC-D08-016, [TC-L12-018](L12-model-layer.md#tc-l12-018) |
| **MITRE ATLAS Mapping** | N/A (assurance control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation and accountability) |

**Risk Addressed.** If an incident cannot be reproduced, root cause analysis rests on opinion, and fixes cannot be verified.

**Business Scenario.** Investigators want to replay an incident under the same conditions and see how far results match.

**Technical Scenario.** Replay five recorded incidents using pinned versions and settings.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** 5 recorded incidents; settings captured: model version, parameters (temperature, seed where available), prompts, retrieved content, tool results (mocked from record); lab-hosted model and a hosted provider model.

**Procedure**

1. Record the incidents.
2. Replay each three times with all captured inputs.
3. Compare outputs for match and variance.
4. Replay with one component changed (new model version) and compare.
5. Check how tool results are mocked from the record without live side effects.
6. Check reporting of replay fidelity.
7. Check that replay cannot reach production systems.

**Edge Cases / Variants.** Provider model without seed control; incident depending on time-sensitive data.

**Expected Detection.** Replay reproduces the incident behaviour in at least 4 of 5 cases or variance is quantified; side effects never occur; fidelity report produced.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Export.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Replay comparison.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d12-008"></a>

### TC-D12-008: Attribution Analysis: Attacker, Insider, Misconfiguration or Model Fault

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L17 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L17-022](L17-monitoring-detection-and-response.md#tc-l17-022) |
| **MITRE ATLAS Mapping** | N/A (response control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE (incident response and communication) |

**Risk Addressed.** Treating a model fault as an attack, or the reverse, leads to wrong containment and wrong notifications.

**Business Scenario.** Investigators want structured evidence for each possible cause.

**Technical Scenario.** Run six scripted incidents with different true causes and check attribution quality.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** 6 incidents: external injection attack, insider misuse, misconfigured access, provider model regression, poisoned data, user error; ground-truth cause for each; 3 investigators.

**Procedure**

1. Give investigators the initial alert only.
2. Let them work using the platform.
3. Record the conclusion, confidence and evidence used.
4. Compare with ground truth.
5. Check whether the platform offers a cause checklist and the evidence each cause requires.
6. Check recording of alternative hypotheses and why they were rejected.
7. Check handling of uncertain attribution.

**Edge Cases / Variants.** Incident with two causes; insider acting through a compromised account.

**Expected Detection.** At least 5 of 6 correct attributions; hypotheses and evidence recorded; uncertainty stated where evidence is incomplete.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Case export.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Attribution table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d12-009"></a>

### TC-D12-009: Scoping and Blast Radius: Users, Data, Systems and Outputs Affected

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L17, L10 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, W |
| **Risk Severity** | Critical |
| **Related Layer Cases** | [TC-L10-026](L10-data-layer.md#tc-l10-026), [TC-L17-022](L17-monitoring-detection-and-response.md#tc-l17-022) |
| **MITRE ATLAS Mapping** | N/A (response control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE (incident response and communication) |

**Risk Addressed.** Missing part of the scope means harm continues or notifications are incomplete.

**Business Scenario.** Responders want the platform to list every user, data item, system and output touched by the incident.

**Technical Scenario.** Run three incidents of increasing reach and compare the platform's scope with ground truth.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** 3 incidents: single user data leak, shared knowledge source poisoned (30 users affected), agent action across 3 systems; ground-truth lists of users, records, outputs and systems.

**Procedure**

1. Trigger each incident.
2. Ask the platform for scope.
3. Compare lists with ground truth.
4. Compute completeness and over-inclusion.
5. Check time to produce.
6. Check export for notification and remediation.
7. Check updates to scope as new evidence arrives.

**Edge Cases / Variants.** Outputs forwarded outside the organisation; data copied to personal workspaces.

**Expected Detection.** At least 90 percent of affected users, records and systems identified; over-inclusion under 15 percent; scope updates audited.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Export for notification workflow.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Scope vs ground truth.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d12-010"></a>

### TC-D12-010: Downstream Propagation of Harmful or False Outputs

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L17, L05 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: A, G, P |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L17-022](L17-monitoring-detection-and-response.md#tc-l17-022) |
| **MITRE ATLAS Mapping** | AML.T0049 Exploit Public-Facing Application (downstream impact) |
| **OWASP LLM / GenAI Mapping** | LLM05:2025 Improper Output Handling |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** A wrong or harmful output may already be in documents, tickets, emails and customer messages by the time it is noticed.

**Business Scenario.** Responders want to find and recall downstream copies of affected outputs.

**Technical Scenario.** Generate a false output and let it flow into lab systems, then trace and recall.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** 1 false output (fabricated policy statement) produced for 6 users; copies: saved in 4 documents, pasted in 3 tickets, sent in 2 emails, quoted in 1 customer message (all lab); output fingerprinting enabled.

**Procedure**

1. Produce the output and let users reuse it.
2. Start the trace from the output.
3. Identify downstream copies and recipients.
4. Check the platform's recall or notice options.
5. Compare found copies with ground truth.
6. Check handling of paraphrased copies.
7. Check evidence of recall actions.

**Edge Cases / Variants.** Output translated or summarised before reuse.

**Expected Detection.** At least 8 of 10 copies found; paraphrased copies flagged where fingerprinting allows or limitation documented; recall actions recorded.

**Expected Prevention / Control Action.** Notify or recall.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Integration with document and messaging systems where available.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Copy table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d12-011"></a>

### TC-D12-011: Containment Option Catalogue and Selection Guidance

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L17, L06, L12 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P, G |
| **Risk Severity** | Critical |
| **Related Layer Cases** | [TC-L17-015](L17-monitoring-detection-and-response.md#tc-l17-015), [TC-L06-022](L06-agent-orchestration-layer.md#tc-l06-022) |
| **MITRE ATLAS Mapping** | AML.T0053 LLM Plugin Compromise |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Responders choose between rolling back a model, disabling a tool, quarantining an index or blocking a user, each with business impact; choosing wrongly costs time or service.

**Business Scenario.** Responders want the available actions listed with impact, approval and reversal for each incident type.

**Technical Scenario.** Present four incidents and have responders choose and execute containment.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** 4 incidents: injection leak from a tool-using agent, poisoned index, model regression, compromised key; catalogue of actions (disable tool, roll back model, quarantine documents, revoke token, block user, disable feature, change guardrail); impact descriptions per action.

**Procedure**

1. Load the catalogue with impact and approval needs.
2. Present each incident.
3. Responders select actions.
4. Execute through the platform.
5. Measure time from decision to effect.
6. Check approvals and logging.
7. Reverse one action and check the restore path.
8. Check the guidance offered when two actions are possible.

**Edge Cases / Variants.** Containment that stops a critical business service; containment requiring provider cooperation.

**Expected Detection.** Correct containment chosen for at least 3 of 4; actions take effect within the stated times; reversals work; approvals and logs complete.

**Expected Prevention / Control Action.** Contain.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Actions through APIs.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Action log.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d12-012"></a>

### TC-D12-012: Eradication and Recovery Validation

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L17, L14, L07 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | High |
| **Related Layer Cases** | TC-D08-019, [TC-L17-023](L17-monitoring-detection-and-response.md#tc-l17-023) |
| **MITRE ATLAS Mapping** | N/A (response control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE (incident response and communication) |

**Risk Addressed.** Restoring service before checking that the cause is gone invites a repeat incident within hours.

**Business Scenario.** Responders want recovery gated on verified removal of the cause.

**Technical Scenario.** Run three incidents through eradication and recovery with gating checks.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** 3 incidents: poisoned document in an index, stolen credential, weakened guardrail after a change; recovery checklist; regression pack from earlier attack tests (D08).

**Procedure**

1. Complete containment.
2. Define the eradication tasks (remove content, rotate credentials, restore rule).
3. Verify each task with evidence.
4. Run the regression pack against the restored system.
5. Check that return to service needs sign-off.
6. Check monitoring intensity after recovery.
7. Check closure evidence.

**Edge Cases / Variants.** Recovery under business pressure; partial eradication accepted with a recorded risk.

**Expected Detection.** Recovery blocked until each eradication task is verified; regression pack passes before sign-off; heightened monitoring period configured.

**Expected Prevention / Control Action.** Gate recovery.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Evidence export.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Checklist; regression results.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d12-013"></a>

### TC-D12-013: Poisoning and Training-Data Incident Forensics

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L13, L10, L11 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Critical |
| **Related Layer Cases** | [TC-L13-004](L13-training-and-fine-tuning-layer.md#tc-l13-004), [TC-L10-008](L10-data-layer.md#tc-l10-008) |
| **MITRE ATLAS Mapping** | AML.T0020 Poison Training Data (applied by analogy to stored context, memory and ingested data); verify against current ATLAS |
| **OWASP LLM / GenAI Mapping** | LLM04:2025 Data and Model Poisoning; LLM01:2025 Prompt Injection |
| **NIST AI RMF Mapping** | MAP 2.3; MEASURE 2.7 |

**Risk Addressed.** Once poisoned data is in a model or index, finding it, its source and every model affected is hard without lineage.

**Business Scenario.** Investigators want poisoned records traced to their source and to every downstream model and index.

**Technical Scenario.** Seed a dataset with poisoned records, train and index, then investigate from a symptom.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** Dataset of 3,000 records with 30 poisoned records from one source; 2 fine-tuned models and 1 index built from it; symptom: a benign trigger phrase producing a marker response.

**Procedure**

1. Seed and train.
2. Start from the symptom report.
3. Use lineage to identify candidate data.
4. Identify the poisoned records and their source and ingestion time.
5. List every model and index built from them.
6. Decide on rollback and retraining.
7. Verify removal and retest the symptom.

**Edge Cases / Variants.** Poison split across several sources; data already used in a deleted model version.

**Expected Detection.** At least 27 of 30 poisoned records identified; all 3 downstream artefacts found; source and time established; retest shows symptom removed.

**Expected Prevention / Control Action.** Quarantine data and artefacts.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Lineage export.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Trace table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d12-014"></a>

### TC-D12-014: Model Behaviour Regression Incident

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L12, L17, L16 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, G |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L12-018](L12-model-layer.md#tc-l12-018), [TC-L16-021](L16-supply-chain-and-third-party.md#tc-l16-021) |
| **MITRE ATLAS Mapping** | N/A (response control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE (incident response and communication) |

**Risk Addressed.** A provider or internal model update can change safety and accuracy overnight, and the evidence is often lost.

**Business Scenario.** Responders want regression evidence, escalation to the provider and a rollback path.

**Technical Scenario.** Simulate a model update that degrades behaviour and run the incident.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** Mock provider with versions A and B; 40 canary prompts; behaviour regression on 8 of them after the switch; 2 dependent applications.

**Procedure**

1. Detect the regression via canaries or reports.
2. Capture before and after evidence.
3. Identify affected applications.
4. Pin or roll back the version.
5. Raise the issue with the mock provider with evidence.
6. Check communication to application owners.
7. Record lessons and update monitoring.

**Edge Cases / Variants.** Silent alias change; regression affecting only one language.

**Expected Detection.** Regression detected within the canary interval; evidence package complete; rollback effective in under 15 minutes; provider escalation recorded.

**Expected Prevention / Control Action.** Pin or roll back.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Evidence package export.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Canary comparison.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d12-015"></a>

### TC-D12-015: Harm Assessment and Affected-Person Identification

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L17, L03 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Critical |
| **Related Layer Cases** | [TC-L17-026](L17-monitoring-detection-and-response.md#tc-l17-026), [TC-L03-019](L03-legal-privacy-and-compliance.md#tc-l03-019) |
| **MITRE ATLAS Mapping** | N/A (governance control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MAP and MANAGE (risk identification and treatment) |

**Risk Addressed.** Where AI outputs influenced decisions about people, responders must identify who was affected and how.

**Business Scenario.** Governance wants a structured assessment of impact on individuals and a list of those affected.

**Technical Scenario.** Run an incident in which an AI-supported process gave wrong outcomes to fabricated individuals.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** 1 scenario: eligibility assistant gave wrong guidance to 40 fabricated applicants over 3 days; 12 of them acted on it; outcomes recorded; harm categories set by the assessor.

**Procedure**

1. Identify the affected period and cases from the logs.
2. List individuals who received the output.
3. Classify who relied on it and the outcome.
4. Rate harm per person using the assessor's categories.
5. Produce remediation actions per person.
6. Check privacy controls on the list.
7. Export the assessment.

**Edge Cases / Variants.** Individuals who received the output through a third party; outputs partially relied on.

**Expected Detection.** At least 38 of 40 individuals identified; reliance and outcome correct for at least 10 of 12; remediation list produced; access to the list controlled.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Export for the privacy and legal teams.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Assessment record.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d12-016"></a>

### TC-D12-016: Notification Decision and Communications (Framework-Neutral)

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L03, L17 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Critical |
| **Related Layer Cases** | [TC-L03-019](L03-legal-privacy-and-compliance.md#tc-l03-019), [TC-L17-026](L17-monitoring-detection-and-response.md#tc-l17-026) |
| **MITRE ATLAS Mapping** | N/A (response control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE (incident response and communication) |

**Risk Addressed.** Notification duties and timelines differ by framework, so the decision, its reasoning and its timing must be recorded.

**Business Scenario.** Compliance and communications want a decision record and message drafts tied to the incident facts.

**Technical Scenario.** Run two incidents through the notification decision process with parameters supplied by the assessor.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** 2 incidents (personal data exposure of 120 fabricated individuals; unsafe advice to customers); timelines and criteria entered by the assessor from the adopted framework; templates for regulator, affected individuals, customers and staff.

**Procedure**

1. Enter the parameters.
2. Complete the assessment from incident facts.
3. Record the decision and reasoning.
4. Track clocks and reminders.
5. Generate message drafts from the facts.
6. Record approvals.
7. Export the decision file.

**Edge Cases / Variants.** Incident with several jurisdictions; facts changing after notification.

**Expected Detection.** Decision, reasoning and approvals recorded; clocks accurate; drafts match facts; decision file exportable.

**Expected Prevention / Control Action.** Escalate.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Export to legal file.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Decision file.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d12-017"></a>

### TC-D12-017: Third-Party and Model-Provider Incident Coordination

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L16, L17 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L16-021](L16-supply-chain-and-third-party.md#tc-l16-021), [TC-L16-010](L16-supply-chain-and-third-party.md#tc-l16-010) |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |

**Risk Addressed.** Many AI incidents involve a provider whose cooperation, logs and fixes are needed and whose terms may limit what is shared.

**Business Scenario.** Responders want the cooperation route, evidence requests and service levels tested before they are needed.

**Technical Scenario.** Run a mock joint incident with a provider contact and review the contract terms.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** 2 mock providers; incident requiring provider logs and a fix; contract terms for notice, cooperation, evidence and service levels; provider contact list.

**Procedure**

1. Review the contract terms.
2. Raise the incident with each provider through the stated route.
3. Request logs and a statement of root cause.
4. Measure acknowledgement and response times.
5. Check what evidence the provider will give and in what format.
6. Check joint communication handling.
7. Record gaps.

**Edge Cases / Variants.** Provider incident affecting many customers at once.

**Expected Detection.** Provider acknowledges within the contracted time; evidence request answered or refused with reasons; gaps recorded and owned.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Documents attached.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Request log; response times.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to domain index](#top)

---

<a id="tc-d12-018"></a>

### TC-D12-018: Evidence Handling for AI Artefacts and Chain of Custody

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L17, L03 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, W |
| **Risk Severity** | Critical |
| **Related Layer Cases** | [TC-L17-021](L17-monitoring-detection-and-response.md#tc-l17-021), [TC-L03-027](L03-legal-privacy-and-compliance.md#tc-l03-027) |
| **MITRE ATLAS Mapping** | N/A (assurance control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation and accountability) |

**Risk Addressed.** AI evidence is more than logs: models, indexes, prompts and configurations must be preserved and shown unchanged.

**Business Scenario.** Legal and investigators want artefacts hashed, stored and tracked from collection to use.

**Technical Scenario.** Collect evidence from a scripted incident and check handling.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** Evidence set: 30 log extracts, 1 prompt version, 1 model configuration, 1 index snapshot, 1 policy export, 5 screenshots; 3 handlers.

**Procedure**

1. Collect each item with hash and time.
2. Transfer between handlers and record custody.
3. Alter one item and check detection.
4. Check storage protections and access logs.
5. Export a custody report.
6. Check legal hold integration.
7. Check retention until release.

**Edge Cases / Variants.** Evidence larger than a standard storage object; evidence collected remotely.

**Expected Detection.** All items hashed; custody complete; altered item detected; access logged; report exportable.

**Expected Prevention / Control Action.** Preserve.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Export.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Custody report.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d12-019"></a>

### TC-D12-019: Forensic Tooling Access, Separation of Duties and Audit

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L17, L10 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, W |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L17-030](L17-monitoring-detection-and-response.md#tc-l17-030) |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Investigators read sensitive conversations; unrestricted forensic access is itself a privacy and insider risk.

**Business Scenario.** Privacy and security want investigator access scoped, approved and audited.

**Technical Scenario.** Test forensic roles and approvals on a seeded case.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** 3 roles (responder, investigator, privacy reviewer); case with 40 conversations containing fabricated personal data; approval workflow for unmasking.

**Procedure**

1. Open the case in each role.
2. Check default masking.
3. Request unmasking with justification.
4. Approve and time-limit.
5. Check audit of every view and export.
6. Check that investigators cannot alter source records.
7. Check alerts on unusual access.

**Edge Cases / Variants.** Investigator who is also a data subject; urgent access during a live incident.

**Expected Detection.** Masking default; unmask needs approval and expires; every access audited; source records immutable; unusual access alerted.

**Expected Prevention / Control Action.** Restrict.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Audit export.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Role test table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d12-020"></a>

### TC-D12-020: AI Root-Cause Analysis Method and Recurrence Tracking

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L17, L02 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L17-023](L17-monitoring-detection-and-response.md#tc-l17-023) |
| **MITRE ATLAS Mapping** | N/A (assurance control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation and accountability) |

**Risk Addressed.** Root-cause reports that name only a rule or a person miss model, data and process factors, and similar incidents recur.

**Business Scenario.** Governance wants a structured method covering technical, data, model, process and human factors, with recurrence tracked.

**Technical Scenario.** Run root-cause analysis on four closed lab incidents and test the method.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** 4 incidents; factor categories (model, data, prompt, tool, access, process, vendor, human); 2 incidents with a common underlying cause.

**Procedure**

1. Complete the analysis template for each incident.
2. Check that every factor category is considered.
3. Link actions to causes.
4. Check linking of incidents with a common cause.
5. Check overdue-action tracking.
6. Check closure verification.
7. Report recurrence by cause.

**Edge Cases / Variants.** Cause outside the organisation's control.

**Expected Detection.** All factor categories addressed; common cause across two incidents found; actions tracked to verified closure.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Export.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Analysis records.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to domain index](#top)

---

<a id="tc-d12-021"></a>

### TC-D12-021: Near-Miss and Blocked-Attack Learning

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L17 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, G |
| **Risk Severity** | Medium |
| **Related Layer Cases** | [TC-L17-023](L17-monitoring-detection-and-response.md#tc-l17-023), [TC-L17-024](L17-monitoring-detection-and-response.md#tc-l17-024) |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Blocked attacks show how the system is being tested; ignoring them wastes the best free intelligence available.

**Business Scenario.** Security wants near-misses captured, summarised and fed into controls.

**Technical Scenario.** Generate blocked attacks and near-misses and test capture and review.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** 60 blocked events (injection, exfiltration attempts, policy evasion) and 5 near-misses (action prevented at the last step); weekly review.

**Procedure**

1. Generate events.
2. Check capture as near-miss records.
3. Check clustering by technique and target.
4. Run the weekly review and record decisions.
5. Convert two into detection or policy improvements.
6. Check effect on later events.
7. Report trends.

**Edge Cases / Variants.** Attack waves from one source.

**Expected Detection.** Near-misses captured and clustered; at least two improvements implemented and tested; trend report available.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Export.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Review record.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d12-022"></a>

### TC-D12-022: AI Incident Register, Metrics and Trend Analysis

| Field | Value |
|---|---|
| **Use-Case Domain** | D12: AI Incident Response and Forensics |
| **Lifecycle Layer(s)** | L17, L02 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Medium |
| **Related Layer Cases** | [TC-L02-019](L02-governance-and-risk-mgmt.md#tc-l02-019) |
| **MITRE ATLAS Mapping** | N/A (assurance control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation and accountability) |

**Risk Addressed.** Leadership needs to see numbers by type, time to detect and contain, recurrence and cost.

**Business Scenario.** Governance wants a reliable register and a small set of defined metrics.

**Technical Scenario.** Load 12 months of simulated incidents and check indicators against hand calculation.

**Preconditions.** Isolated PoC lab provisioned; lab AI applications with versioned prompts, models and indexes, lab SIEM and case tools, scripted incident scenarios with ground truth and test responders seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab AI applications (chatbot, RAG assistant, tool-using agent) with versioned prompts, models and indexes; a lab SIEM, ticketing and case tool; scripted incident scenarios with known ground truth; test responders, an investigator and a legal reviewer; no production systems, real incidents or real personal data.

**Test Data.** 60 simulated incidents across types and severities; indicators: count by type, mean time to detect, mean time to contain, mean time to recover, recurrence rate, notification rate, cost estimate; calculation sheet.

**Procedure**

1. Load the incidents.
2. Compare indicators with the calculation sheet.
3. Check definitions.
4. Check trends and filters.
5. Check drill-down.
6. Check schedule and export.
7. Check access control.

**Edge Cases / Variants.** Incidents reclassified after closure.

**Expected Detection.** All indicators match within 2 percent; definitions visible; drill-down works; reports scheduled and access controlled.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Incident, evidence and case state visible in the incident response workspace within the documented refresh interval.

**Expected Integration Evidence.** Report export.

**Forensic Evidence.** Incident, evidence and case identifiers with component versions, actors, decisions, approvals, hashes and timestamps exportable for investigation and audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Indicator table.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to domain index](#top)

---

