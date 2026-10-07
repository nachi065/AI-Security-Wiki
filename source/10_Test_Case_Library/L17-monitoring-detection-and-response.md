---
title: "L17 Monitoring, Detection & Response"
author: Nachiket Sathaye
parent: "Test Case Library"
nav_order: 20
---

<a id="top"></a>

# L17 Monitoring, Detection & Response

**Primary test focus:** telemetry, SIEM/SOAR integration, AI incident response, forensics

**Controls tested:** [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-009](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035)

**Cases:** 31 (TC-L17-001 to TC-L17-031)
> **Safety boundary.** Infrastructure and SOC cases use a lab cluster, mock inference servers, a test cloud account and a lab SIEM and SOAR only. Probe and compromise-simulation scripts are harmless lab tools that only attempt connections and reads of canary resources. Never run them against production systems, and never connect lab alerting to production on-call routing. Cases marked Attestation rest on vendor documents and score below demonstrated evidence.

> **Verify before use.** MITRE ATLAS, OWASP LLM and NIST AI RMF identifiers must be checked against the current published versions. Numeric thresholds are starting values to tune. See the [Reference Index](00-reference-index.md) for field definitions and applicability codes.

## Cases in this layer

| ID | Title | Severity | Method | Domain(s) |
|---|---|---|---|---|
| [TC-L17-001](#tc-l17-001) | Telemetry Coverage Map Across the 17 Layers | High | Evidence | D3, D5, D7 |
| [TC-L17-002](#tc-l17-002) | Event Schema and Field Completeness | High | Technical | D3 |
| [TC-L17-003](#tc-l17-003) | Log Delivery to SIEM: Formats, Reliability and Backfill | High | Technical | D3 |
| [TC-L17-004](#tc-l17-004) | Log Integrity and Tamper Evidence | High | Technical | D7 |
| [TC-L17-005](#tc-l17-005) | Log Retention, Immutability and Storage Location | Medium | Evidence | D7 |
| [TC-L17-006](#tc-l17-006) | Prebuilt AI Detection Content and SIEM Rules | High | Technical | D3, D5 |
| [TC-L17-007](#tc-l17-007) | Alert Quality: Severity, Deduplication and Noise | High | Technical | D3 |
| [TC-L17-008](#tc-l17-008) | Alert Enrichment with User, Device, Asset and Risk Context | Medium | Technical | D1, D3 |
| [TC-L17-009](#tc-l17-009) | Correlation of AI Events with Endpoint, Identity and Network Events | High | Technical | D3, D6 |
| [TC-L17-010](#tc-l17-010) | Detection of Data Exfiltration Through AI Services | Critical | Technical | D6, D1 |
| [TC-L17-011](#tc-l17-011) | Detection of Account Takeover on AI Tools | High | Technical | D1, D3 |
| [TC-L17-012](#tc-l17-012) | Detection of Agent Compromise Indicators | Critical | Technical | D5 |
| [TC-L17-013](#tc-l17-013) | Detection of Insider Misuse and Policy Evasion | High | Technical | D1, D6 |
| [TC-L17-014](#tc-l17-014) | Mapping of Detections to MITRE ATLAS and ATT&CK | Medium | Evidence | D3 |
| [TC-L17-015](#tc-l17-015) | SOAR Playbooks for Automated Containment | Critical | Technical | D5, D3 |
| [TC-L17-016](#tc-l17-016) | SOAR and Ticketing Integration: Bidirectional Flow | High | Technical | D3 |
| [TC-L17-017](#tc-l17-017) | Case Management and Evidence Attachment | Medium | Technical | D6 |
| [TC-L17-018](#tc-l17-018) | AI Incident Response Runbook and Tabletop Exercise | High | Technical | D3, D5, D7 |
| [TC-L17-019](#tc-l17-019) | Containment Time Measurement | High | Technical | D5 |
| [TC-L17-020](#tc-l17-020) | Forensics: Conversation and Tool Call Reconstruction | Critical | Technical | D6, D5 |
| [TC-L17-021](#tc-l17-021) | Forensics: Evidence Preservation, Legal Hold and Integrity | High | Technical | D7 |
| [TC-L17-022](#tc-l17-022) | Forensics: Cross-User, Agent and Tool Timeline | High | Technical | D5, D3 |
| [TC-L17-023](#tc-l17-023) | Post-Incident Feedback into Policy and Detection | Medium | Evidence | D3 |
| [TC-L17-024](#tc-l17-024) | AI Threat Intelligence Ingestion | Medium | Technical | D3 |
| [TC-L17-025](#tc-l17-025) | Dashboards and Executive Metrics (Detection and Response Times) | Medium | Evidence | D7 |
| [TC-L17-026](#tc-l17-026) | Regulatory Incident Reporting Evidence (UAE and GCC) | High | Evidence | D7 |
| [TC-L17-027](#tc-l17-027) | 24x7 Monitoring, MDR Support and Escalation Model | High | Attestation | D7 |
| [TC-L17-028](#tc-l17-028) | Platform Health and Silent Failure Detection | High | Technical | D3 |
| [TC-L17-029](#tc-l17-029) | Purple-Team Detection Validation: Replay of Earlier Attacks | High | Technical | D3, D5, D6 |
| [TC-L17-030](#tc-l17-030) | SOC Analyst Access to Raw Prompts: Masking, Role Separation and Unmask Audit | High | Technical | D1, D7 |
| [TC-L17-031](#tc-l17-031) | Developer AI Activity Telemetry and Investigation Timeline | High | Technical | D2, D6 |

---

## Test cases

<a id="tc-l17-001"></a>

### TC-L17-001: Telemetry Coverage Map Across the 17 Layers

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D3, D5, D7 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Detection can only be as good as the events the platform produces, and gaps are usually discovered during an incident.

**Business Scenario.** SOC leads want to know which lifecycle layers generate events, what kinds, and which are blind spots.

**Technical Scenario.** Generate a standard set of activities across the layers and map which produce platform events.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 30 activities spread over layers L04 to L16: unsanctioned tool use, prompt injection attempt, sensitive paste, agent tool call, MCP server added, token scope violation, model download, vector store query, dataset upload, pipeline promotion, secret in prompt, admin policy change, and similar; coverage checklist by layer.

**Procedure**

1. List the activities and the expected event for each.
2. Execute all 30 in the lab.
3. Check the platform and SIEM for a matching event.
4. Record presence, timing and completeness per activity.
5. Build the coverage map by layer.
6. Review gaps with the vendor and record whether each gap is a roadmap item, a configuration option or out of scope.
7. Repeat after enabling every optional source.

**Edge Cases / Variants.** Activities by service accounts; activities during platform maintenance.

**Expected Detection.** At least 24 of 30 activities produce an event; layers without any events identified and explained; every gap has a stated answer from the vendor.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Coverage matrix exportable.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Coverage map; vendor gap responses.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l17-002"></a>

### TC-L17-002: Event Schema and Field Completeness

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D3 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Events missing user, agent, model, tool or decision fields cannot be correlated or investigated.

**Business Scenario.** Detection engineers want normalised events carrying the fields needed for rules and investigations.

**Technical Scenario.** Generate events from several sources and inspect field presence, naming and types.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 100 events from 10 event types (policy block, detection, tool call, approval, login, configuration change, inventory change, kill switch, DLP match, error); required field list: time, tenant, user, device, agent, model, tool, resource, policy, decision, severity, session identifier, correlation identifier, source layer.

**Procedure**

1. Agree the required field list.
2. Generate the events.
3. Export a sample.
4. Check field presence per event type.
5. Check types, formats and time zones.
6. Check consistency of names across event types.
7. Check documentation of the schema and versioning of changes.
8. Check handling of sensitive values.

**Edge Cases / Variants.** Events from older agent versions; events from third-party sources.

**Expected Detection.** At least 95 percent of required fields present where applicable; consistent names and time in UTC; schema documented with version; sensitive values masked per policy.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Schema document attached.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Field completeness table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-003"></a>

### TC-L17-003: Log Delivery to SIEM: Formats, Reliability and Backfill

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D3 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Lost or late events create silent detection gaps, and some integrations drop events during outages.

**Business Scenario.** SOC engineers want reliable delivery with defined formats and recovery after interruption.

**Technical Scenario.** Configure delivery to the lab SIEM using each supported method and test outages.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** Delivery methods (syslog, API pull, webhook, object storage, native connector) as offered; 5,000 events over 30 minutes; outage of 30 minutes; duplicate and out-of-order scenarios.

**Procedure**

1. Configure each delivery method.
2. Send the 5,000 events.
3. Compare counts and content at the SIEM.
4. Break the connection for 30 minutes during traffic.
5. Restore and check backfill and duplicates.
6. Check ordering and time stamps.
7. Check authentication and encryption of the channel.
8. Measure delivery delay.

**Edge Cases / Variants.** Burst of 10 times normal volume; SIEM temporarily rejecting events.

**Expected Detection.** Zero event loss in normal operation; backfill complete after outage with no more than 1 percent duplicates; delay under 2 minutes; channel authenticated and encrypted.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** SIEM parsers or apps available.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Count reconciliation; delay table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-004"></a>

### TC-L17-004: Log Integrity and Tamper Evidence

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Altered or deleted logs undermine investigations and regulatory defence.

**Business Scenario.** Audit wants evidence that platform logs cannot be changed unnoticed.

**Technical Scenario.** Attempt to alter and delete events and check protection and detection.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** Platform logs and audit trail; 3 admin roles; attempts: edit event, delete event, delete range, disable logging, change retention.

**Procedure**

1. Review the integrity design (hash chaining, signing, write-once storage).
2. Attempt each alteration as each role.
3. Check whether attempts are blocked, logged and alerted.
4. Verify integrity of a sample using the vendor's tool or an independent check.
5. Export a signed slice.
6. Check clock synchronisation and drift handling.

**Edge Cases / Variants.** Alteration at storage level by an infrastructure administrator.

**Expected Detection.** All alteration attempts blocked or detected and alerted; integrity verification passes for untouched logs and fails for altered copies; signed export supported.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Alerts to SIEM.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Attempt table; verification output.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-005"></a>

### TC-L17-005: Log Retention, Immutability and Storage Location

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Short retention or the wrong storage location breaks investigations and regulatory obligations.

**Business Scenario.** Compliance wants retention periods, immutability and location controlled and evidenced.

**Technical Scenario.** Configure retention and check enforcement, immutability and location.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** Retention tiers (hot 30 days, warm 180 days, archive 7 years); sample data; legal hold; location requirement.

**Procedure**

1. Configure tiers.
2. Backdate data to cross each boundary.
3. Check movement and accessibility.
4. Apply legal hold and attempt deletion.
5. Check immutability.
6. Verify storage location for each tier.
7. Check deletion after expiry and its evidence.

**Edge Cases / Variants.** Region change during the retention period.

**Expected Detection.** Tiers behave as configured; hold prevents deletion; immutability enforced; storage in the permitted region; deletion evidence produced.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Export.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Retention test records.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l17-006"></a>

### TC-L17-006: Prebuilt AI Detection Content and SIEM Rules

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D3, D5 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Teams without ready detection content spend months building it and miss early attacks.

**Business Scenario.** SOC wants usable AI detections shipped with the platform or its integration.

**Technical Scenario.** Load the vendor's detection content into the lab SIEM and run attack and benign scenarios.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** Vendor rule pack; 20 attack scenarios (prompt injection burst, data leak, shadow AI spike, new agent, token misuse, model exfiltration attempt, kill switch event, policy tamper, repeated approval denials, off-hours bulk retrieval, and similar) and 20 benign scenarios.

**Procedure**

1. Load the content.
2. Review rule documentation and mapping.
3. Replay the attack scenarios.
4. Record which rules fire.
5. Replay benign scenarios and record false positives.
6. Tune one noisy rule and check effect.
7. Check update cadence and versioning of the content.

**Edge Cases / Variants.** Scenarios spread over days; scenarios from several users at once.

**Expected Detection.** At least 16 of 20 attack scenarios detected; false positives under 10 percent of benign scenarios; rules documented with severity and response guidance; content updated at least quarterly.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Rules importable into the SIEM.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Scenario results table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-007"></a>

### TC-L17-007: Alert Quality: Severity, Deduplication and Noise

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D3 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** A noisy platform trains analysts to ignore it.

**Business Scenario.** SOC wants measured alert volume, duplication and accuracy over a realistic period.

**Technical Scenario.** Run seven simulated days of mixed benign and malicious activity and measure alerts.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 7 days of simulated traffic for 50 users and 5 agents; 15 seeded malicious events; normal peaks (month-end, release day).

**Procedure**

1. Run the simulated week.
2. Count alerts by severity.
3. Check which seeded events produced alerts.
4. Check duplicate and related alerts for grouping.
5. Have two analysts classify a sample of 100 alerts.
6. Compute precision and alerts per analyst per day.
7. Tune and repeat one day.

**Edge Cases / Variants.** New feature launch causing legitimate spikes; seasonal usage.

**Expected Detection.** At least 13 of 15 malicious events alerted at appropriate severity; precision at least 70 percent in the sample; duplicates grouped; fewer than 50 actionable alerts per analyst per day.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Alert metrics exportable.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Alert counts; analyst classification sheet.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-008"></a>

### TC-L17-008: Alert Enrichment with User, Device, Asset and Risk Context

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D1, D3 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Analysts waste time looking up who a user is and what an asset does.

**Business Scenario.** SOC wants alerts to arrive with context.

**Technical Scenario.** Generate alerts and check enrichment against known facts.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 20 alerts involving users, devices, agents and applications with known attributes in the directory, asset system and risk register.

**Procedure**

1. Generate the alerts.
2. Check enrichment: user role, department, manager, device posture, application owner, data sensitivity, agent owner, recent related alerts.
3. Compare with ground truth.
4. Check the effect of stale directory data.
5. Check time to enrich.
6. Check what enrichment is stored versus retrieved on demand.

**Edge Cases / Variants.** User who changed department during the alert window.

**Expected Detection.** At least 90 percent of enrichment fields correct; stale data handled with a visible age; enrichment within 30 seconds.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Directory and asset integrations.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Enrichment comparison.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-009"></a>

### TC-L17-009: Correlation of AI Events with Endpoint, Identity and Network Events

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D3, D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Real incidents span tools; AI events alone rarely tell the story.

**Business Scenario.** SOC wants AI events correlated with other telemetry.

**Technical Scenario.** Run three multi-source scenarios and check the correlated view.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 3 scenarios: compromised account uses an AI tool to summarise sensitive files then uploads to personal storage; malicious extension reads page content and posts to an AI API; agent token used from a new network and tools abused.

**Procedure**

1. Generate events across identity, endpoint, network and AI sources.
2. Check that the SIEM or platform joins them by user, device, session or token.
3. Check timeline views.
4. Check whether a single incident is created.
5. Measure time to build the picture manually versus using correlation.
6. Check correlation key quality.

**Edge Cases / Variants.** Events with different user identifiers across systems.

**Expected Detection.** All 3 scenarios appear as a single incident or linked set; time to understand reduced by at least half compared with manual search; correlation keys documented.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Correlation rules and keys.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Timelines; manual versus assisted timing.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-010"></a>

### TC-L17-010: Detection of Data Exfiltration Through AI Services

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D6, D1 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0025 Exfiltration via Cyber Means |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** Data leaves a little at a time through legitimate AI services and may not trigger any single-event rule.

**Business Scenario.** DLP and SOC teams want volume and sensitivity patterns detected over time.

**Technical Scenario.** Simulate low-and-slow and burst exfiltration to approved and unapproved AI services.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 3 test users; 4 patterns: single large upload, 50 small pastes in a day, slow daily pastes over 2 weeks (simulated time), upload of encoded content; fabricated sensitive data.

**Procedure**

1. Set normal baselines.
2. Run each pattern.
3. Record detection time and signal.
4. Check cumulative thresholds and trend detection.
5. Check user and data context in alerts.
6. Run heavy but legitimate usage by a fourth user and check false positives.

**Edge Cases / Variants.** Use of several accounts; use of several AI services in sequence.

**Expected Detection.** At least 3 of 4 patterns detected; the burst within minutes; cumulative detection documented; legitimate heavy user not blocked without review.

**Expected Prevention / Control Action.** Alert or block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Alerts to SIEM and DLP.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Detection table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-011"></a>

### TC-L17-011: Detection of Account Takeover on AI Tools

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D1, D3 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Stolen sessions on AI tools give attackers access to chat history and connected data.

**Business Scenario.** SOC wants takeover signals recognised.

**Technical Scenario.** Simulate takeover patterns for test accounts.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 3 accounts; scenarios: login from a new country with impossible travel, new device with immediate bulk history export, changed behaviour (sudden long prompts at 3am), token reuse from two networks.

**Procedure**

1. Establish baselines for 7 days.
2. Run each scenario.
3. Record detection and time.
4. Check response options.
5. Check false positives from travel and VPN use by legitimate users.
6. Check use of the identity provider's risk signals.

**Edge Cases / Variants.** Corporate VPN exit nodes in other countries.

**Expected Detection.** At least 3 of 4 scenarios detected within 15 minutes; false positives for legitimate travel under 5 percent.

**Expected Prevention / Control Action.** Step-up or block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Alerts to SIEM.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Detection table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-012"></a>

### TC-L17-012: Detection of Agent Compromise Indicators

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D5 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0053 LLM Plugin Compromise |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** A compromised agent behaves differently in small ways before it does damage.

**Business Scenario.** SOC wants indicators for hijacked or misbehaving agents.

**Technical Scenario.** Replay five compromise indicators for lab agents.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 3 agents with 14 days of baseline; indicators: new tool never used before, tenfold call volume, reading a new data source, call to a new external domain, repeated blocked actions followed by success.

**Procedure**

1. Load the baseline.
2. Replay each indicator.
3. Record detection and severity.
4. Check linking to the agent's owner and recent changes.
5. Check suggested containment.
6. Run a legitimate change after approval and check suppression.

**Edge Cases / Variants.** Gradual escalation of tool use over weeks.

**Expected Detection.** At least 4 of 5 indicators detected within 15 minutes; legitimate approved change not alerted; owner and containment shown.

**Expected Prevention / Control Action.** Alert or hold.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Alerts to SIEM and SOAR.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Detection table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-013"></a>

### TC-L17-013: Detection of Insider Misuse and Policy Evasion

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D1, D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Insiders probe controls, try workarounds and move data in ways that look like normal work.

**Business Scenario.** SOC and HR want repeated evasion and misuse patterns surfaced with proportionate handling.

**Technical Scenario.** Run an insider script with several evasion attempts and a heavy but legitimate user.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 2 users: one scripted to hit blocks, try alternate tools, rephrase blocked prompts, use personal accounts and encode data; one legitimate heavy user; 14 simulated days.

**Procedure**

1. Run the scripts.
2. Check how repeated blocks and rephrasing are linked.
3. Check detection of alternate tool use.
4. Check risk score progression.
5. Check how the legitimate heavy user scores.
6. Check privacy controls on viewing identity and the case-opening process.

**Edge Cases / Variants.** Insider with a legitimate reason to test controls (security team).

**Expected Detection.** Evasion sequence linked into one story within the stated time; legitimate user scored low; identity viewing controlled and audited.

**Expected Prevention / Control Action.** Alert.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Cases to the case system.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Risk score chart; case record.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-014"></a>

### TC-L17-014: Mapping of Detections to MITRE ATLAS and ATT&CK

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D3 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Detections without a framework mapping are hard to compare, prioritise and report.

**Business Scenario.** Security leadership wants detection coverage expressed in recognised frameworks.

**Technical Scenario.** Review the platform's mapping of detections and compare with an independent mapping.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 20 detections; independent mapping prepared by the evaluator against current published framework versions.

**Procedure**

1. Export the vendor's mapping.
2. Check identifiers and names against the current published versions.
3. Compare with the independent mapping.
4. List agreements and differences.
5. Check how the mapping is maintained and versioned.
6. Check coverage view.

**Edge Cases / Variants.** Detections spanning several techniques.

**Expected Detection.** At least 80 percent agreement; invalid or outdated identifiers corrected by the vendor; mapping versioned.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Export.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Comparison table.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l17-015"></a>

### TC-L17-015: SOAR Playbooks for Automated Containment

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D5, D3 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0053 LLM Plugin Compromise |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Manual containment is too slow when an agent or account is misusing data, but automatic actions can themselves cause outages.

**Business Scenario.** SOC wants playbooks that contain AI incidents quickly and safely.

**Technical Scenario.** Build and run playbooks for five containment actions using the platform's actions or APIs.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 5 playbooks: disable an agent, revoke a token, block a user from an AI service, quarantine a knowledge source, isolate an endpoint agent; test targets for each; approval step for high-impact actions.

**Procedure**

1. Build each playbook with the platform's actions.
2. Trigger each with a simulated alert.
3. Measure time from alert to effect.
4. Verify the effect on the target.
5. Test the approval step for the high-impact ones.
6. Test rollback.
7. Test what happens when the platform action fails or times out.

**Edge Cases / Variants.** Action against a production-critical agent; duplicate alerts triggering the same action twice.

**Expected Detection.** All 5 playbooks work end to end; time to effect under 2 minutes for automatic actions; approvals enforced; rollback works; failures handled with alerts.

**Expected Prevention / Control Action.** Contain automatically or after approval.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** API and connector documentation.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Playbook runs; timing table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-016"></a>

### TC-L17-016: SOAR and Ticketing Integration: Bidirectional Flow

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D3 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** One-way alert feeds leave tickets and platform state out of step.

**Business Scenario.** SOC wants alert, ticket, action and closure to stay synchronised.

**Technical Scenario.** Run alerts through the full loop and check state at each end.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 10 alerts; mock ticketing system; platform and SOAR configured with credentials.

**Procedure**

1. Generate 10 alerts.
2. Check ticket creation, fields and links.
3. Update status in the ticket and check the platform.
4. Take an action in the platform and check the ticket note.
5. Close an incident and check alert state.
6. Check behaviour when the ticket system is unavailable.
7. Check authentication method and permissions of the integration account.

**Edge Cases / Variants.** Ticket edited by two people; very large alert bursts.

**Expected Detection.** All 10 alerts create tickets with correct fields; status and notes sync in both directions within 2 minutes; failure handling queued and retried; integration account least-privilege.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Connector or API.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** State comparison table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-017"></a>

### TC-L17-017: Case Management and Evidence Attachment

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Evidence scattered across tools slows investigations, loses context and weakens any later disciplinary or legal step.

**Business Scenario.** Investigators want one case holding every piece of AI-related evidence with originals preserved.

**Technical Scenario.** Open a case from related alerts and build it using the platform's evidence, notes and tasks, then export it.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 1 case built from 8 related alerts about one fabricated insider scenario; evidence types: conversation extracts, tool call records, policy decisions, user timeline, screenshots, exported logs; 2 investigators and 1 reviewer; 1 attempt by an unauthorised user to open the case.

**Procedure**

1. Create the case from the alerts.
2. Attach each evidence type and record how originals are preserved and hashed.
3. Add notes, tasks and assignees.
4. Attempt access as the unauthorised user and as the reviewer.
5. Check the case audit trail.
6. Export the case in the offered formats and check completeness.
7. Close the case and check retention and re-opening rules.

**Edge Cases / Variants.** Case spanning two tenants; case with legal sensitivity requiring restricted membership; evidence added after closure.

**Expected Detection.** Case holds all evidence with hashes; originals unchanged; access limited to assigned roles and every access audited; export complete and readable; closure and retention follow policy.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Export to case or legal tools.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Case record; export sample; audit trail.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-018"></a>

### TC-L17-018: AI Incident Response Runbook and Tabletop Exercise

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D3, D5, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Teams practised only on malware and phishing struggle with prompt injection, model misbehaviour and agent incidents.

**Business Scenario.** Incident response wants runbooks tested against AI scenarios using the platform's tooling.

**Technical Scenario.** Run a facilitated exercise with three scenarios and the platform's evidence.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 3 scenarios: indirect injection causes an agent to send data externally; a poisoned knowledge document spreads false guidance; a model update causes unsafe outputs; participants from security, engineering, legal and communications.

**Procedure**

1. Provide the runbook.
2. Start each scenario with an injected alert.
3. Participants use the platform to scope.
4. Record decisions, times and gaps.
5. Check use of platform actions (kill switch, rollback, quarantine).
6. Debrief and list actions.
7. Update the runbook.

**Edge Cases / Variants.** Scenario at night with the primary responder unavailable.

**Expected Detection.** Scope established within 30 minutes per scenario; platform actions used correctly; gaps listed with owners; runbook updated.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Runbook document.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Exercise notes and timings.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-019"></a>

### TC-L17-019: Containment Time Measurement

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D5 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0053 LLM Plugin Compromise |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Time from first malicious event to verified containment decides how much damage an AI incident does, and it is rarely measured.

**Business Scenario.** SOC wants contained-time figures for each type of AI incident, with and without automation.

**Technical Scenario.** Run five timed scenarios, record every stage and compare manual and automated handling.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 5 scenarios: agent misuse (unexpected tool calls), token abuse from a new network, data leak through an AI service, poisoned knowledge source, faulty model release; stopwatch definitions agreed in advance; 2 analysts; automation playbooks from the earlier case.

**Procedure**

1. Define stage boundaries: event, detection, triage complete, decision, action started, effect verified.
2. Run each scenario manually and record stage times.
3. Compute totals and the longest stage.
4. Repeat each scenario with automation enabled.
5. Compare.
6. Check that logs and the case record let you verify each timestamp.
7. Identify the slowest handoff in each scenario.

**Edge Cases / Variants.** Scenario beginning at night; scenario where the first alert is a false positive.

**Expected Detection.** Median time to contain under 30 minutes manual and under 5 minutes automated; every stage timestamp verifiable from logs; longest stage identified per scenario.

**Expected Prevention / Control Action.** Contain.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Metrics export.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Stage timing table by scenario and mode.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-020"></a>

### TC-L17-020: Forensics: Conversation and Tool Call Reconstruction

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D6, D5 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Without full conversation and tool records, investigators cannot show what the user asked, what the model said or what an agent did.

**Business Scenario.** Investigators want complete, ordered reconstruction with chain of custody.

**Technical Scenario.** Reconstruct three scripted incidents from platform records only.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 3 incidents with scripted conversations (8 to 15 turns), 2 tool calls each, 1 blocked action; investigator with platform access only.

**Procedure**

1. Run the incidents.
2. Ask the investigator to reconstruct each.
3. Compare with scripts.
4. Check fidelity: prompts, responses, system prompt version, retrieved chunks, tool arguments, decisions.
5. Check masking and unmask audit.
6. Check chain of custody for the export.

**Edge Cases / Variants.** Conversations deleted by the user; streaming responses.

**Expected Detection.** At least 95 percent of turns and all tool calls reconstructed; versions and decisions present; chain of custody recorded.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Export for case tools.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Reconstruction vs script.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-021"></a>

### TC-L17-021: Forensics: Evidence Preservation, Legal Hold and Integrity

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Evidence that was not preserved, or cannot be shown unaltered, may be useless.

**Business Scenario.** Legal and investigation teams want preservation and integrity proven.

**Technical Scenario.** Preserve evidence for an incident and test hold, hashing and export.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 1 incident with 200 records; legal hold; export to evidence storage.

**Procedure**

1. Apply preservation to the incident.
2. Attempt deletion and expiry.
3. Export with hashes.
4. Verify hashes independently.
5. Alter an exported copy and verify failure.
6. Check access logging for the evidence.

**Edge Cases / Variants.** Hold applied after some records have expired.

**Expected Detection.** Preserved records immune to deletion; hashes verify; altered copy fails verification; access logged.

**Expected Prevention / Control Action.** Hold.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Evidence export.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Hash verification output.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-022"></a>

### TC-L17-022: Forensics: Cross-User, Agent and Tool Timeline

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D5, D3 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Incidents rarely involve one actor; investigators need an ordered story across people, agents and tools.

**Business Scenario.** Investigators want a single timeline.

**Technical Scenario.** Build a timeline for a multi-actor scenario.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** Scenario with 2 users, 3 agents, 4 tools, 1 MCP server; 40 events over 2 hours.

**Procedure**

1. Run the scenario.
2. Build the timeline with the platform.
3. Compare with the script.
4. Check filters and pivots.
5. Check handling of clock differences.
6. Export.

**Edge Cases / Variants.** Events from systems with 2-minute clock drift.

**Expected Detection.** At least 38 of 40 events in correct order; pivots by actor and tool work; export complete.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Export.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Timeline comparison.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-023"></a>

### TC-L17-023: Post-Incident Feedback into Policy and Detection

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D3 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Lessons that never become rules or detections turn into repeat incidents.

**Business Scenario.** Security wants a short, auditable path from incident finding to a tested policy or detection change.

**Technical Scenario.** Take findings from the exercises and push each through the platform's change process.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 5 findings: a missing detection for slow exfiltration, an over-broad agent permission, a noisy rule, a policy gap for browser agents, a runbook step with no platform action; change approvers; replay set from earlier attack tests.

**Procedure**

1. Record each finding with owner and target date.
2. Draft the policy or detection change in the platform.
3. Test it against the relevant replay set and against 20 benign events.
4. Submit for approval and record approver and time.
5. Deploy to production-equivalent lab and check versioning.
6. Re-run the original scenario and confirm the finding is closed.
7. Check reporting on finding closure rates.

**Edge Cases / Variants.** Finding that needs a business process change rather than a platform change.

**Expected Detection.** All 5 findings closed with a tested change; false positives from changes under 5 percent of benign events; approvals and versions recorded; closure report available.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Change records to GRC or tickets.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Finding-to-change table; re-test results.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l17-024"></a>

### TC-L17-024: AI Threat Intelligence Ingestion

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D3 |
| **Test Method** | Technical |
| **Vendor Applicability** | Partial: P, G |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** New prompt attacks, malicious tool servers and compromised model hashes appear constantly and are only useful if detection can use them quickly.

**Business Scenario.** SOC wants external AI-specific intelligence turned into detections with measurable effect.

**Technical Scenario.** Ingest a sample feed and test matching, ageing, removal and sharing.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** Sample feed of 30 indicators (known malicious tool server addresses, attack string fragments, hashes of compromised model files, suspicious domains, malicious package names); 10 lab events matching indicators and 10 similar-looking non-matching events; 1 indicator to be withdrawn.

**Procedure**

1. Check supported feed formats and transport (state them, for example STIX/TAXII if offered).
2. Ingest the feed.
3. Replay the 20 events.
4. Record matches, alerts and context shown.
5. Withdraw one indicator and check that it stops matching.
6. Check ageing and confidence handling.
7. Check whether the platform can share its own findings back, and under what controls.

**Edge Cases / Variants.** Indicators with wildcard patterns; indicators that overlap legitimate services.

**Expected Detection.** At least 9 of 10 matching events detected; non-matching events not flagged; withdrawn indicator stops matching within the stated time; ageing works; sharing controlled.

**Expected Prevention / Control Action.** Alert.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Standard feed formats.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Match table; indicator lifecycle test.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-025"></a>

### TC-L17-025: Dashboards and Executive Metrics (Detection and Response Times)

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Leaders manage what they can see; wrong or undefined metrics send management in the wrong direction.

**Business Scenario.** Security leadership wants a small set of reliable, defined metrics for AI risk and response.

**Technical Scenario.** Load known simulated data and check each dashboard metric against hand-calculated values.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 30 days of simulated data for 200 users and 10 agents; 10 metrics: incidents by type, mean time to detect, mean time to contain, blocked actions, shadow AI trend, top risk users, open exceptions, agents without owners, telemetry coverage, open findings by age; calculation sheet prepared in advance.

**Procedure**

1. Load the data.
2. Compare each metric with the calculation sheet.
3. Check metric definitions and whether they can be inspected.
4. Check drill-down from each metric to the underlying events.
5. Schedule a weekly report and check delivery and content.
6. Check access control on dashboards and exports.
7. Change a policy and check the metric reflects it.

**Edge Cases / Variants.** Metrics that differ by time zone; users counted under several identities.

**Expected Detection.** At least 9 of 10 metrics match within 2 percent; every metric has a visible definition; drill-down works; scheduled report delivered; access controlled.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Report export and scheduling.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Metric comparison table.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l17-026"></a>

### TC-L17-026: Regulatory Incident Reporting Evidence (UAE and GCC)

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Regulators expect timely, specific incident reports and evidence of data affected.

**Business Scenario.** Compliance wants the information needed for a report produced quickly.

**Technical Scenario.** Run a mock reportable incident and generate the information pack.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 1 incident involving fabricated personal data of 200 individuals; reporting template with fields (nature, data affected, time, systems, containment, notification decision).

**Procedure**

1. Run the incident.
2. Generate the pack.
3. Compare with the template.
4. Check data subject counts and categories.
5. Time the process.
6. Check the evidence trail for decisions.

**Edge Cases / Variants.** Incident discovered after several weeks.

**Expected Detection.** Pack covers at least 90 percent of template fields; counts accurate; produced within 4 hours.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Report export.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Pack vs template.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l17-027"></a>

### TC-L17-027: 24x7 Monitoring, MDR Support and Escalation Model

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Attestation |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** An alert at 2am is worthless if no one is accountable for it, and managed services often have narrower coverage than the sales material suggests.

**Business Scenario.** Procurement wants the support, monitoring and escalation model documented and tested before commitment.

**Technical Scenario.** Review the service description and run an out-of-hours escalation drill.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** Vendor service descriptions; named escalation contacts; mock critical alert; requirements checklist (hours, tiers, languages, locations, response and resolution times, data access by vendor staff, reporting).

**Procedure**

1. Request the model in writing.
2. Map it to the checklist.
3. Send a mock critical alert outside business hours through the official channel.
4. Measure acknowledgement and first action.
5. Check what customer data the vendor's analysts can see and under what approvals.
6. Review sample service reports and review meeting arrangements.
7. Check holiday and surge coverage.

**Edge Cases / Variants.** Alert raised during a public holiday; vendor analyst located in a different country from the data.

**Expected Detection.** Acknowledgement and first action within stated times; escalation reached a named person; vendor data access controlled and logged; service reports provided.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Signed written statement from the vendor.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Documents attached.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = no statement; 3 = statement without supporting detail; 5 = statement with technical detail and an offer to demonstrate.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Drill timeline; checklist mapping.

**Reviewer Notes.** Attestation scores below demonstrated evidence. Request a demonstration where possible.

[Back to layer index](#top)

---

<a id="tc-l17-028"></a>

### TC-L17-028: Platform Health and Silent Failure Detection

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D3 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** The worst failure is the one nobody notices: an agent that stopped reporting, ingestion that stalled, or a certificate that expired.

**Business Scenario.** Operations wants failures of the platform itself detected and routed.

**Technical Scenario.** Induce six failures in the lab deployment and measure detection and notification.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 6 failures: endpoint agent offline, gateway node down, event ingestion stopped, classifier service degraded, certificate expiry, licence limit reached; heartbeat design documentation; alert routing to the lab chat and ticketing.

**Procedure**

1. Document the heartbeat and health model.
2. Induce each failure separately.
3. Record the time to alert and the alert content.
4. Check routing and escalation.
5. Check whether protection continues, fails open or fails closed.
6. Restore and check the recovery notice.
7. Induce a partial failure (one of three gateway nodes slow) and check detection.

**Edge Cases / Variants.** Failure that begins during a maintenance window; clock drift causing false health alarms.

**Expected Detection.** All 6 failures alerted within 10 minutes; alerts say what is affected and what protection state results; routing correct; partial failure detected or limitation documented.

**Expected Prevention / Control Action.** Alert.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Alerts to monitoring and chat.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Failure table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-029"></a>

### TC-L17-029: Purple-Team Detection Validation: Replay of Earlier Attacks

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D3, D5, D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Detection claimed on paper may fail end to end.

**Business Scenario.** Security wants proof that earlier attack tests are visible to the SOC.

**Technical Scenario.** Replay a sample of attacks from the other layers and follow each to an analyst's screen.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 25 attacks sampled across L04, L07, L08, L09, L10 and L06.

**Procedure**

1. Replay the 25 attacks.
2. Check for platform events.
3. Check SIEM alerts.
4. Check triage and enrichment.
5. Record end-to-end time.
6. Identify attacks that never reach an analyst.
7. Repeat after tuning.

**Edge Cases / Variants.** Attacks in other languages.

**Expected Detection.** At least 20 of 25 reach an analyst with correct context; end-to-end time recorded; gaps with causes.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** SIEM and ticketing.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Replay table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-030"></a>

### TC-L17-030: SOC Analyst Access to Raw Prompts: Masking, Role Separation and Unmask Audit

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D1, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage (secondary) |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; GOVERN 1.1 |

**Risk Addressed.** Analysts reading raw prompts may see personal or confidential content, and unrestricted access breaches employee privacy expectations and some employment or data protection rules.

**Business Scenario.** Privacy and HR want analyst access proportionate, justified and audited.

**Technical Scenario.** Test analyst roles, default masking and the unmask process on seeded events.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Lab SIEM and SOAR (open-source or vendor-neutral), the platform's event feed, simulated incident scenarios, test analysts and a mock ticketing system; no production alerting, ticketing or on-call routing connected.

**Test Data.** 3 roles (tier 1 analyst, investigator, privacy officer); 20 events containing fabricated personal and confidential content; 2 unmask requests with justification (one approved, one refused).

**Procedure**

1. View all events as each role and note what is masked.
2. Request unmask without justification and with justification.
3. Check approval, time limit and automatic re-masking.
4. Check the audit entry for every unmask including requester, approver, reason and fields.
5. Export events as each role and check masking.
6. Check search behaviour (can an analyst search for a name in masked content).
7. Check alerts on unusual unmask volumes.

**Edge Cases / Variants.** Break-glass unmask during an active incident; privacy officer reviewing their own team's access.

**Expected Detection.** Tier 1 sees masked content only; investigator unmasks only with approval; every unmask audited; exports respect masking; search cannot be used to reveal masked values; unusual unmask volume alerted.

**Expected Prevention / Control Action.** Mask.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Audit export to SIEM.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Role comparison; audit log extract.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l17-031"></a>

### TC-L17-031: Developer AI Activity Telemetry and Investigation Timeline

| Field | Value |
|---|---|
| **Lifecycle Layer** | L17 Monitoring, Detection & Response |
| **Use-Case Domain(s)** | D2, D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, G, P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** When code or secrets leak through a coding assistant, investigators must reconstruct what was sent, from which repository and by which tool, and most SOC tooling holds no such record.

**Business Scenario.** The SOC wants IDE, CLI and coding agent events in the SIEM with enough context to build a timeline.

**Technical Scenario.** Generate a scripted sequence of developer AI events and check their arrival, fields and correlation in the lab SIEM.

**Preconditions.** Isolated PoC lab provisioned; lab SIEM and SOAR, the platform's event feed, simulated incident scenarios, test analysts and mock ticketing seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); no production alerting connected. Test workstation with an IDE assistant, a CLI coding agent and one mock MCP server, all reporting to the platform.

**Test Data.** Scripted sequence of 12 events: extension install, sign-in, 4 prompts (1 containing a fake secret), 2 agent commands, 1 MCP tool call, 1 blocked prompt, 1 policy override, 1 extension removal.

**Procedure**

1. Run the sequence.
2. Confirm all 12 events reach the SIEM.
3. Check the required fields on each event.
4. Build a timeline for the test user.
5. Pivot from the fake secret to the repository and file.
6. Measure delivery time.

**Edge Cases / Variants.** Workstation offline for part of the sequence; events from a remote development host.

**Expected Detection.** 12 of 12 events in the SIEM within the documented delivery time with user, device, tool, repository, action and decision fields; the timeline can be reconstructed in order.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Detection, alert and case state visible in the platform and SIEM within the documented refresh interval.

**Expected Integration Evidence.** Events parse into the SIEM schema without custom scripting, or the vendor supplies the parser.

**Forensic Evidence.** Event, alert, case and action identifiers with actor, source layer, decision and timestamp, plus evidence hashes, exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection is met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** SIEM event export; timeline; delivery-time measurements.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---
