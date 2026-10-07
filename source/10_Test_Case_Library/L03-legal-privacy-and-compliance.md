---
title: "L03 Legal, Privacy & Compliance"
author: Nachiket Sathaye
parent: "Test Case Library"
nav_order: 6
---

<a id="top"></a>

# L03 Legal, Privacy & Compliance

**Primary test focus:** UAE/GCC residency, PDPL-type obligations, evidence export, DPIA support

**Controls tested:** [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007), [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013)

**Cases:** 30 (TC-L03-001 to TC-L03-030)
> **Safety boundary.** All cases use fabricated use cases, policies, records and individuals only. This layer is framework-neutral: see the [Framework Adoption Guide](framework-adoption-guide.md) before testing, and complete the Applicable Requirement and Framework Crosswalk fields for each case.

> **Verify before use.** MITRE ATLAS, OWASP LLM and NIST AI RMF identifiers must be checked against the current published versions. Numeric thresholds are starting values to tune. See the [Reference Index](00-reference-index.md) for field definitions and applicability codes.

## Cases in this layer

| ID | Title | Severity | Method | Domain(s) |
|---|---|---|---|---|
| [TC-L03-001](#tc-l03-001) | Register of AI Processing Activities | Critical | Technical | D6, D7 |
| [TC-L03-002](#tc-l03-002) | Lawful Basis or Legal Ground Recording per Processing Activity | High | Evidence | D6, D7 |
| [TC-L03-003](#tc-l03-003) | Notice and Transparency: Disclosing AI Interaction and Processing | High | Technical | D1, D7 |
| [TC-L03-004](#tc-l03-004) | Consent Capture, Evidence and Withdrawal | Critical | Technical | D6, D7 |
| [TC-L03-005](#tc-l03-005) | Data Subject Rights: Access Request Workflow | Critical | Technical | D6, D7 |
| [TC-L03-006](#tc-l03-006) | Data Subject Rights: Correction Request Handling | Medium | Technical | D6, D7 |
| [TC-L03-007](#tc-l03-007) | Data Subject Rights: Erasure Across AI Stores | Critical | Technical | D6, D7 |
| [TC-L03-008](#tc-l03-008) | Rights to Object, Restrict and Request Human Review | High | Technical | D6, D7 |
| [TC-L03-009](#tc-l03-009) | Rights Request Timeline Tracking and Evidence | High | Technical | D7 |
| [TC-L03-010](#tc-l03-010) | Impact Assessment Support (Privacy, Data Protection and AI Impact Assessments) | Critical | Technical | D7 |
| [TC-L03-011](#tc-l03-011) | Impact Assessment Triggers | High | Technical | D7 |
| [TC-L03-012](#tc-l03-012) | Cross-Border Transfer Register and Assessment | Critical | Technical | D7 |
| [TC-L03-013](#tc-l03-013) | Cross-Border Transfer Enforcement | Critical | Technical | D7, D6 |
| [TC-L03-014](#tc-l03-014) | Residency Evidence Export for a Regulator | High | Evidence | D7 |
| [TC-L03-015](#tc-l03-015) | Data Minimisation and Purpose Limitation Enforcement | High | Technical | D6, D7 |
| [TC-L03-016](#tc-l03-016) | Retention Schedule Enforcement for AI Data | High | Technical | D6, D7 |
| [TC-L03-017](#tc-l03-017) | Children's and Vulnerable Persons' Data Handling | High | Technical | D6, D7 |
| [TC-L03-018](#tc-l03-018) | Special and Sensitive Categories of Data: Identification and Heightened Controls | Critical | Technical | D6, D7 |
| [TC-L03-019](#tc-l03-019) | Breach and Incident Notification Workflow | Critical | Technical | D7 |
| [TC-L03-020](#tc-l03-020) | Controller, Processor and Joint Role Mapping with Agreements | High | Technical | D7 |
| [TC-L03-021](#tc-l03-021) | AI Provider Compliance Due-Diligence Evidence | High | Attestation | D7 |
| [TC-L03-022](#tc-l03-022) | Compliance Evidence Export: Formats, Signing and Integrity | High | Technical | D7 |
| [TC-L03-023](#tc-l03-023) | Multi-Framework Compliance Dashboard: Coverage and Gaps | High | Technical | D7 |
| [TC-L03-024](#tc-l03-024) | Adopting a New Framework: Custom Framework Onboarding | Critical | Technical | D7 |
| [TC-L03-025](#tc-l03-025) | Evidence Reuse Across Frameworks | High | Technical | D7 |
| [TC-L03-026](#tc-l03-026) | Regulator Inspection Simulation: Rapid Evidence Request | Critical | Technical | D7 |
| [TC-L03-027](#tc-l03-027) | Litigation Hold and Regulatory Preservation Notice | High | Technical | D6, D7 |
| [TC-L03-028](#tc-l03-028) | Intellectual Property and Copyright Controls for AI Inputs and Outputs | Medium | Technical | D3, D7 |
| [TC-L03-029](#tc-l03-029) | Automated Decision Explanation Records | High | Technical | D3, D7 |
| [TC-L03-030](#tc-l03-030) | Language and Jurisdiction Configuration (Arabic, English and Regional Rule Sets) | Medium | Technical | D7 |

---

## Test cases

<a id="tc-l03-001"></a>

### TC-L03-001: Register of AI Processing Activities

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D6, D7 |
| **Control Theme** | PRV: Privacy and data protection principles |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | Critical |
| **NIST AI RMF Mapping** | MAP and MEASURE (privacy risk examined and managed) |

**Risk Addressed.** Most privacy and data protection frameworks expect a maintained record of what personal data is processed, why, by whom and where; AI projects add new processing that rarely reaches it.

**Business Scenario.** Privacy wants AI processing recorded in the same register as other processing, with a defined minimum content.

**Technical Scenario.** Create register entries for AI use cases and test mandatory content, linkage and change tracking.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 10 fabricated processing activities linked to AI use cases (support chatbot, recruitment screening, fraud scoring, meeting summaries, employee analytics, marketing personalisation, document search, translation, code assistant, medical-style triage); required fields defined by the assessor from the adopted framework (purpose, categories of data, categories of individuals, recipients, transfers, retention, security measures, role of the organisation).

**Procedure**

1. Record the required content list from the adopted framework.
2. Create the 10 entries.
3. Check validation of mandatory fields.
4. Check links to use cases, systems, vendors and datasets.
5. Change a processing detail and check version history and review trigger.
6. Check discovery-driven suggestions for missing entries.
7. Export the register in a regulator-friendly format.

**Edge Cases / Variants.** Processing carried out jointly with another organisation; processing by a department outside privacy's view.

**Expected Result.** All mandatory fields enforced; links present; changes versioned with review triggered; missing entries suggested from discovery or the gap documented; export complete.

**Expected Control Action.** Block incomplete entries.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Export to privacy management tools.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Register export; validation messages.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-002"></a>

### TC-L03-002: Lawful Basis or Legal Ground Recording per Processing Activity

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D6, D7 |
| **Control Theme** | PRV: Privacy and data protection principles |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | High |
| **NIST AI RMF Mapping** | MAP and MEASURE (privacy risk examined and managed) |

**Risk Addressed.** Processing without a recorded legal ground is hard to defend and rights handling depends on it.

**Business Scenario.** Privacy wants a legal ground recorded for each activity with the reasoning.

**Technical Scenario.** Assign grounds to ten processing activities and test validation and downstream effects.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 10 processing activities; ground options configured from the adopted framework (for example consent, contract, legal obligation, legitimate interest-type grounds, public interest, other); 3 activities with weak or missing reasoning.

**Procedure**

1. Configure the list of grounds.
2. Record the ground and reasoning for each activity.
3. Check validation for missing reasoning.
4. Check conditional requirements (for example consent capture where consent is selected).
5. Check review workflow for interest-balancing assessments where applicable.
6. Check effect on rights available.
7. Export.

**Edge Cases / Variants.** Activity with several grounds for different purposes.

**Expected Result.** Missing reasoning rejected; conditional requirements triggered; rights handling adapts to the ground; export complete.

**Expected Control Action.** Gate.

**Expected Record / Log.** Configuration state, record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Link to consent and rights tools.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = partly shown or shown only from documentation; 5 = shown in the live product with exportable evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Ground records.

**Reviewer Notes.** Confirm the evidence is taken from the live product. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l03-003"></a>

### TC-L03-003: Notice and Transparency: Disclosing AI Interaction and Processing

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D1, D7 |
| **Control Theme** | OVS: Human oversight and transparency |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: A, W |
| **Risk Severity** | High |
| **NIST AI RMF Mapping** | GOVERN and MANAGE (human oversight, transparency) |

**Risk Addressed.** People should know when they interact with AI or when AI processes their data, and many frameworks require notices of defined content.

**Business Scenario.** Privacy and legal want notices presented, versioned and evidenced.

**Technical Scenario.** Configure notices for three channels and test display, content and evidence.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 3 channels (chat widget, email assistant, internal HR tool); notice text in English and Arabic; 1 notice update.

**Procedure**

1. Configure notices per channel.
2. Test display at first use and at each session.
3. Check content elements recorded by the assessor from the adopted framework (purpose, data used, recipients, rights, contact).
4. Update the notice and check re-display.
5. Check logging of displays.
6. Check accessibility and right-to-left rendering.
7. Export evidence of display.

**Edge Cases / Variants.** User declining to proceed; embedded AI features inside other products.

**Expected Result.** Notices shown on every channel at required points; update triggers re-display; display logged per user and version; rendering correct in both languages.

**Expected Control Action.** Display and gate.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Logs exportable.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Screenshots; display log.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-004"></a>

### TC-L03-004: Consent Capture, Evidence and Withdrawal

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D6, D7 |
| **Control Theme** | PRV: Privacy and data protection principles |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, A |
| **Risk Severity** | Critical |
| **NIST AI RMF Mapping** | MAP and MEASURE (privacy risk examined and managed) |

**Risk Addressed.** Where consent is the ground, it must be demonstrable and as easy to withdraw as to give.

**Business Scenario.** Privacy wants consent records and effective withdrawal handling.

**Technical Scenario.** Capture and withdraw consent for fabricated individuals and test propagation to AI processing.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 20 fabricated individuals; 3 purposes; 6 withdrawals; 2 purpose changes requiring fresh consent.

**Procedure**

1. Capture consent per purpose.
2. Check the record (who, when, version, wording, channel).
3. Withdraw for 6 individuals.
4. Check propagation to AI processing and data stores within the target time.
5. Change a purpose and check re-consent.
6. Check proof export for one individual.
7. Check handling of withdrawal when data has already been used in training.

**Edge Cases / Variants.** Withdrawal during an active session; consent given on behalf of a minor.

**Expected Result.** Records complete; withdrawal effective within the target; re-consent triggered; proof export available; training-data case documented.

**Expected Control Action.** Stop processing.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Consent platform integration.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Consent records; propagation test.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-005"></a>

### TC-L03-005: Data Subject Rights: Access Request Workflow

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D6, D7 |
| **Control Theme** | PRV: Privacy and data protection principles |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | Critical |
| **NIST AI RMF Mapping** | MAP and MEASURE (privacy risk examined and managed) |

**Risk Addressed.** Individuals can ask what is held about them; AI systems scatter data across prompts, indexes, logs and derived stores.

**Business Scenario.** Privacy wants requests handled across AI stores with evidence.

**Technical Scenario.** Run access requests for fabricated individuals and measure completeness and time.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 3 fabricated individuals appearing in 60 records across conversation history, knowledge index, tickets, logs, analytics and a training dataset; 3 requests.

**Procedure**

1. Log the requests with identity verification.
2. Search across the stores.
3. Compare results to the ground truth list.
4. Check redaction of other people's data.
5. Produce the response pack.
6. Check time tracking against the timeline set by the assessor.
7. Check audit trail.

**Edge Cases / Variants.** Individual known by different names; data inside images and attachments.

**Expected Result.** At least 90 percent of seeded records found; third-party data redacted; response pack produced within the target; audit trail complete.

**Expected Control Action.** N/A.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Export of response pack.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Result vs ground truth; timing.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-006"></a>

### TC-L03-006: Data Subject Rights: Correction Request Handling

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D6, D7 |
| **Control Theme** | PRV: Privacy and data protection principles |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | Medium |
| **NIST AI RMF Mapping** | MAP and MEASURE (privacy risk examined and managed) |

**Risk Addressed.** Incorrect data about a person that flows into AI outputs can cause harm and may need correcting at source and in derived stores.

**Business Scenario.** Privacy wants corrections applied consistently.

**Technical Scenario.** Request corrections for fabricated individuals and trace propagation.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 3 individuals; 5 incorrect data points; stores: source system, knowledge index, summaries, cached outputs.

**Procedure**

1. Log the requests.
2. Correct at source.
3. Check propagation to the index and derived content.
4. Check handling of outputs already shared.
5. Record the outcome and notify the requester.
6. Check audit.

**Edge Cases / Variants.** Disputed correction; correction conflicting with a retention duty.

**Expected Result.** Corrections propagate to derived stores within the target; shared outputs identified; audit complete.

**Expected Control Action.** Workflow.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Source-system integration.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Before and after records.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-007"></a>

### TC-L03-007: Data Subject Rights: Erasure Across AI Stores

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D6, D7 |
| **Control Theme** | RET: Retention, deletion and preservation |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | Critical |
| **NIST AI RMF Mapping** | GOVERN and MANAGE (data lifecycle) |

**Risk Addressed.** Deletion from the source system leaves copies in embeddings, caches, logs and training data.

**Business Scenario.** Privacy wants erasure executed and evidenced across every store the AI pipeline writes to.

**Technical Scenario.** Request erasure for a fabricated individual and verify each store.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 1 individual with data in 8 stores (source, conversation history, vector store, cache, logs, analytics, backup, training dataset); retention exceptions on 1 store.

**Procedure**

1. Log the request.
2. Execute erasure.
3. Verify each store.
4. Check backup handling and statement.
5. Check treatment of the training dataset and model (flag for assessment).
6. Check retention exception handling and communication.
7. Produce completion evidence.

**Edge Cases / Variants.** Data copied to a vendor system; data in a legal hold.

**Expected Result.** All stores handled or exceptions justified; completion evidence produced; model impact flagged; backup approach documented.

**Expected Control Action.** Workflow.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Evidence export.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Store-by-store verification.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-008"></a>

### TC-L03-008: Rights to Object, Restrict and Request Human Review

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D6, D7 |
| **Control Theme** | OVS: Human oversight and transparency |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, A |
| **Risk Severity** | High |
| **NIST AI RMF Mapping** | GOVERN and MANAGE (human oversight, transparency) |

**Risk Addressed.** Where decisions are automated, individuals may be entitled to contest them or ask for human involvement.

**Business Scenario.** Privacy wants objection and review requests captured, routed and evidenced.

**Technical Scenario.** Submit objection and review requests tied to automated decisions.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 5 fabricated individuals; 2 automated decision use cases; requests for restriction, objection and human review.

**Procedure**

1. Link requests to the use case and decision record.
2. Route to the human reviewer.
3. Check that processing is restricted where required.
4. Record the review outcome and rationale.
5. Notify the individual.
6. Check timing and audit.

**Edge Cases / Variants.** Request about a decision made months earlier.

**Expected Result.** Requests linked to the exact decision; restriction applied; human review recorded with rationale; timing tracked.

**Expected Control Action.** Workflow.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Decision log link.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Request records.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-009"></a>

### TC-L03-009: Rights Request Timeline Tracking and Evidence

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | AUD: Audit, evidence and assurance |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | High |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation, evaluation and accountability) |

**Risk Addressed.** Missing deadlines is a common regulatory failing and timelines differ between frameworks.

**Business Scenario.** Privacy wants timelines configured per framework and tracked with extensions recorded.

**Technical Scenario.** Configure two timeline profiles and run requests against them.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 12 requests across access, correction, erasure and objection; two profiles with different deadlines entered by the assessor; 3 extensions; 2 overdue.

**Procedure**

1. Configure timeline profiles.
2. Open the 12 requests.
3. Check clocks start and pause rules.
4. Check reminders and escalation.
5. Record extensions with reasons.
6. Report overdue and average handling time by profile.
7. Export evidence.

**Edge Cases / Variants.** Request received on a holiday; identity verification delaying the clock.

**Expected Result.** Clocks correct per profile; escalation works; extensions recorded; reports accurate.

**Expected Control Action.** Escalate.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Report export.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Timeline report.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-010"></a>

### TC-L03-010: Impact Assessment Support (Privacy, Data Protection and AI Impact Assessments)

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | RSK: Risk management |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Critical |
| **NIST AI RMF Mapping** | MAP and MANAGE (risk identification and treatment) |

**Risk Addressed.** Impact assessments are required by many frameworks for higher-risk processing and are often written without the facts to hand.

**Business Scenario.** Privacy wants assessments supported by pre-filled system and data facts, structured questions and approvals.

**Technical Scenario.** Complete an assessment for one use case using platform data.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 1 use case with known data categories, vendors, transfers and users; assessment template configured by the assessor.

**Procedure**

1. Create the assessment from the use case.
2. Check which sections are pre-filled from inventory and lineage.
3. Complete the questions.
4. Add risks and mitigations and link to controls.
5. Route for review and approval.
6. Check outcome recording including consultation where required.
7. Export the assessment.

**Edge Cases / Variants.** Template differences between frameworks; assessment spanning several systems.

**Expected Result.** Facts pre-filled correctly; risks linked to controls; approvals recorded; export complete.

**Expected Control Action.** N/A.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Export for the privacy office.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Assessment export.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-011"></a>

### TC-L03-011: Impact Assessment Triggers

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | RSK: Risk management |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | High |
| **NIST AI RMF Mapping** | MAP and MANAGE (risk identification and treatment) |

**Risk Addressed.** Assessments are missed when new uses or changes do not trigger them.

**Business Scenario.** Privacy wants triggers based on data, scale, purpose and change.

**Technical Scenario.** Test triggers for new and changed use cases.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 6 use cases or changes: new use of sensitive data, new automated decision, new transfer, large scale expansion, minor UI change, new vendor.

**Procedure**

1. Configure trigger rules from the adopted framework.
2. Apply each change.
3. Check triggers and notifications.
4. Check blocking of go-live until the assessment is done.
5. Check false triggers.
6. Check history.

**Edge Cases / Variants.** Combined small changes; urgent change.

**Expected Result.** Material changes trigger assessments and minor ones do not; go-live gated; history recorded.

**Expected Control Action.** Gate.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Link to change events.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Trigger table.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-012"></a>

### TC-L03-012: Cross-Border Transfer Register and Assessment

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | XBT: Cross-border transfer, residency and jurisdiction |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | Critical |
| **NIST AI RMF Mapping** | GOVERN and MAP (legal and regulatory requirements, third-party context) |

**Risk Addressed.** Transfers to model providers and hosting locations create obligations that differ by framework and are often unknown to privacy teams.

**Business Scenario.** Privacy wants all transfers recorded with the recipient, location, mechanism and assessment.

**Technical Scenario.** Record transfers for use cases and test discovery-driven completeness.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 6 use cases with transfers to 5 destinations (2 approved, 2 requiring assessment, 1 prohibited by policy); transfer mechanisms defined by the assessor.

**Procedure**

1. Create transfer records.
2. Check required content and assessment link.
3. Compare with discovered destinations.
4. Check handling of the prohibited one.
5. Check review dates.
6. Export.

**Edge Cases / Variants.** Transfers through sub-processors; transfers by remote access.

**Expected Result.** Discovered destinations all recorded; prohibited transfer escalated; reviews scheduled; export complete.

**Expected Control Action.** Escalate.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Link to discovery.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Register export.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-013"></a>

### TC-L03-013: Cross-Border Transfer Enforcement

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D7, D6 |
| **Control Theme** | XBT: Cross-border transfer, residency and jurisdiction |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, P, E |
| **Risk Severity** | Critical |
| **NIST AI RMF Mapping** | GOVERN and MAP (legal and regulatory requirements, third-party context) |

**Risk Addressed.** A register means little if data can still flow to disallowed destinations.

**Business Scenario.** Compliance wants technical enforcement of the transfer policy.

**Technical Scenario.** Send fabricated personal data to destinations in allowed and disallowed regions.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 6 mock AI endpoints with region labels; 20 requests with personal data.

**Procedure**

1. Set policy by region and data type.
2. Send requests.
3. Record decisions.
4. Check bypass attempts (alternate endpoint, redirect).
5. Check logging with region and rule.
6. Report violations.

**Edge Cases / Variants.** Endpoint behind a content delivery network.

**Expected Result.** All disallowed transfers blocked or alerted; allowed ones pass; bypass attempts caught.

**Expected Control Action.** Block.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Events to SIEM.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Request table.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-014"></a>

### TC-L03-014: Residency Evidence Export for a Regulator

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | XBT: Cross-border transfer, residency and jurisdiction |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | High |
| **NIST AI RMF Mapping** | GOVERN and MAP (legal and regulatory requirements, third-party context) |

**Risk Addressed.** Regulators and customers ask for proof of where data is held and processed, not statements, and the answer must cover logs, backups and support access as well as primary storage.

**Business Scenario.** Compliance wants a single, dated evidence pack on data locations that stands up to challenge.

**Technical Scenario.** Generate a residency evidence pack for five lab systems and check content against independently observed facts.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 5 systems; data classes (prompts, outputs, embeddings, logs, telemetry, backups, support access records); observed locations from the infrastructure tests; pack template with fields set by the assessor from the adopted framework.

**Procedure**

1. Select scope and date.
2. Generate the pack.
3. Check coverage for each data class and system.
4. Compare each stated location with observed facts.
5. Check how changes during the reporting period are shown.
6. Check signing, dating and versioning.
7. Check redaction of sensitive configuration details.

**Edge Cases / Variants.** Data moved between regions during the period; a system with a failover site in another country.

**Expected Result.** Pack covers every data class and location; at least 95 percent of statements match observation; period changes shown; pack signed and dated; sensitive details redacted.

**Expected Control Action.** N/A.

**Expected Record / Log.** Configuration state, record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Pack export.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = partly shown or shown only from documentation; 5 = shown in the live product with exportable evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Pack sample; comparison table.

**Reviewer Notes.** Confirm the evidence is taken from the live product. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l03-015"></a>

### TC-L03-015: Data Minimisation and Purpose Limitation Enforcement

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D6, D7 |
| **Control Theme** | PRV: Privacy and data protection principles |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, G, A |
| **Risk Severity** | High |
| **NIST AI RMF Mapping** | MAP and MEASURE (privacy risk examined and managed) |

**Risk Addressed.** Sending or keeping more data than a purpose needs is the usual way personal data exposure grows, and minimisation is a stated principle in most frameworks.

**Business Scenario.** Privacy wants evidence that field-level and purpose-based limits operate in practice.

**Technical Scenario.** Define purposes with allowed data fields and test whether extra data is removed before reaching AI services.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 3 use cases with allowed field lists (for example support: name and ticket text only; HR assistant: role and grade only; analytics: pseudonymised identifier only); 100 records each with 6 extra fields; 20 records in which extra data is embedded in free text.

**Procedure**

1. Define each purpose and its allowed fields.
2. Send the records through the platform.
3. Capture what reaches the AI service.
4. Compute the share of extra fields removed.
5. Check handling of free text.
6. Check logging of removals.
7. Request an exception and check approval and expiry.

**Edge Cases / Variants.** Fields renamed by upstream systems; nested structures.

**Expected Result.** At least 98 percent of extra structured fields removed; at least 80 percent of embedded extra data in free text detected; removals logged; exceptions approved and time-limited.

**Expected Control Action.** Strip or block.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Policy export.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Before and after samples; removal log.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-016"></a>

### TC-L03-016: Retention Schedule Enforcement for AI Data

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D6, D7 |
| **Control Theme** | RET: Retention, deletion and preservation |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, W |
| **Risk Severity** | High |
| **NIST AI RMF Mapping** | GOVERN and MANAGE (data lifecycle) |

**Risk Addressed.** Prompts, outputs, embeddings and logs accumulate indefinitely unless retention is enforced technically.

**Business Scenario.** Privacy and records management want schedules defined per data class and enforced.

**Technical Scenario.** Configure retention periods and verify deletion across AI stores.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 5 data classes (conversation history, prompts and outputs, embeddings, logs, training datasets) with retention periods entered by the assessor; 6 stores; backdated records.

**Procedure**

1. Record the schedule.
2. Configure each store.
3. Backdate records across thresholds.
4. Check deletion or archival.
5. Check holds override deletion.
6. Check deletion evidence and logs.
7. Check backup treatment.

**Edge Cases / Variants.** Data referenced by an open request; data in several systems with different clocks.

**Expected Result.** Deletion occurs within the stated window in every store; holds respected; evidence produced; backup approach documented.

**Expected Control Action.** Delete.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Evidence export.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Store-by-store results.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-017"></a>

### TC-L03-017: Children's and Vulnerable Persons' Data Handling

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D6, D7 |
| **Control Theme** | PRV: Privacy and data protection principles |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, A, W |
| **Risk Severity** | High |
| **NIST AI RMF Mapping** | MAP and MEASURE (privacy risk examined and managed) |

**Risk Addressed.** Many frameworks require additional safeguards where minors or vulnerable people are involved.

**Business Scenario.** Privacy wants such data identified, flagged and controlled.

**Technical Scenario.** Seed fabricated records and use cases involving minors and vulnerable groups.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 30 records (10 minors, 10 vulnerable adults, 10 other); 3 use cases (education assistant, health-style support, general chatbot).

**Procedure**

1. Configure flags and age or vulnerability indicators.
2. Process the records.
3. Check detection and labelling.
4. Check policy actions (block, restrict, extra review).
5. Check notice and consent variants.
6. Check reports.

**Edge Cases / Variants.** Age inferred from content; unverified users.

**Expected Result.** At least 90 percent flagged; heightened controls applied; reports available.

**Expected Control Action.** Restrict or block.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Flags in logs.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Detection table.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-018"></a>

### TC-L03-018: Special and Sensitive Categories of Data: Identification and Heightened Controls

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D6, D7 |
| **Control Theme** | PRV: Privacy and data protection principles |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, G |
| **Risk Severity** | Critical |
| **NIST AI RMF Mapping** | MAP and MEASURE (privacy risk examined and managed) |

**Risk Addressed.** Sensitive categories carry stricter conditions and higher penalties, and the list differs between frameworks.

**Business Scenario.** Privacy wants sensitive categories identified and subject to stronger controls.

**Technical Scenario.** Seed fabricated sensitive-category data and test detection and policy.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 120 fabricated records covering categories configured by the assessor from the adopted framework (health, religion, political opinion, biometric, financial, criminal-record type, and others); 120 non-sensitive look-alikes.

**Procedure**

1. Configure the category list.
2. Run detection.
3. Compute recall and precision per category.
4. Check heightened policies (stricter access, no external AI, extra approval).
5. Check Arabic and English coverage.
6. Check reports.

**Edge Cases / Variants.** Context-dependent sensitivity such as a name implying religion.

**Expected Result.** At least 90 percent recall and 85 percent precision per category; heightened policies applied; both languages covered.

**Expected Control Action.** Block or restrict.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Findings to privacy.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Detection table.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-019"></a>

### TC-L03-019: Breach and Incident Notification Workflow

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | INC: Incident and breach management |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Critical |
| **NIST AI RMF Mapping** | MANAGE (incident response and communication) |

**Risk Addressed.** Notification deadlines to regulators and individuals are short, differ by framework and need a documented decision.

**Business Scenario.** Compliance wants a workflow that assesses, decides and tracks notification.

**Technical Scenario.** Run a mock AI-related personal data incident through the workflow.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 1 incident involving fabricated data of 300 individuals; two timeline profiles entered by the assessor; decision tree with criteria; 3 regulators or contacts.

**Procedure**

1. Open the incident from an alert.
2. Complete the assessment (data, individuals, harm, containment).
3. Check the decision logic.
4. Track deadlines and reminders.
5. Generate the notification content for regulator and individuals.
6. Record the decision and approvals.
7. Export the evidence pack.

**Edge Cases / Variants.** Incident discovered late; incident involving a processor.

**Expected Result.** Assessment and decision recorded; deadlines tracked per profile; notifications generated; evidence pack complete.

**Expected Control Action.** Escalate.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Link to incident tools.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Incident record; pack.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-020"></a>

### TC-L03-020: Controller, Processor and Joint Role Mapping with Agreements

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | VND: Third-party and supplier management |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | High |
| **NIST AI RMF Mapping** | GOVERN and MAP (third-party and supply chain risk) |

**Risk Addressed.** Roles determine duties; unrecorded roles and missing agreements are frequent findings.

**Business Scenario.** Privacy wants roles and agreements recorded for every processing activity involving a third party.

**Technical Scenario.** Record roles and agreements for ten third-party relationships.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 10 vendors; roles (controller, processor, joint, sub-processor); agreements with dates and clauses; 3 missing or expired.

**Procedure**

1. Record roles.
2. Link agreements.
3. Check required clauses against a list set by the assessor.
4. Check expiry alerts.
5. Check sub-processor lists and change notices.
6. Report gaps.

**Edge Cases / Variants.** Vendor acting in two roles.

**Expected Result.** Gaps reported; expiry alerts raised; sub-processor changes tracked.

**Expected Control Action.** Alert.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Contract tool link.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Gap report.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-021"></a>

### TC-L03-021: AI Provider Compliance Due-Diligence Evidence

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | VND: Third-party and supplier management |
| **Test Method** | Attestation |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | High |
| **NIST AI RMF Mapping** | GOVERN and MAP (third-party and supply chain risk) |

**Risk Addressed.** Reliance on a provider's claims without evidence is a weak position.

**Business Scenario.** Compliance wants evidence collected, dated and reviewed for each AI provider.

**Technical Scenario.** Collect and review evidence for three providers.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 3 providers; evidence list (certifications, audit reports, data handling terms, location statements, incident history, sub-processors).

**Procedure**

1. Request evidence.
2. Check dates and scope.
3. Record findings.
4. Check reminders for expiry.
5. Check risk rating.
6. Check approval.

**Edge Cases / Variants.** Provider refusing to share.

**Expected Result.** Evidence complete or gaps recorded; expiry reminders work; rating justified.

**Expected Control Action.** Alert.

**Expected Record / Log.** Signed written statement or document from the vendor, dated and attributable to a named role.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Documents.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = no statement; 3 = statement without supporting detail; 5 = statement with technical detail, supporting documents and an offer to demonstrate.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Evidence checklist.

**Reviewer Notes.** Attestation scores below demonstrated evidence. Request a demonstration where possible and record what was and was not verified.

[Back to layer index](#top)

---

<a id="tc-l03-022"></a>

### TC-L03-022: Compliance Evidence Export: Formats, Signing and Integrity

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | AUD: Audit, evidence and assurance |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | High |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation, evaluation and accountability) |

**Risk Addressed.** Evidence that cannot leave the platform in a usable and verifiable form is hard to rely on in an audit or dispute.

**Business Scenario.** Audit wants exports in common formats with integrity proof and full metadata.

**Technical Scenario.** Export evidence in every offered format and verify completeness and integrity.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 30 evidence items of mixed types (documents, logs, configuration exports, screenshots, records); formats offered by the platform (state which); one oversized export.

**Procedure**

1. Export all 30 items in each format.
2. Compare content with the source.
3. Check metadata (who, when, source system, control reference).
4. Check signing or hashing.
5. Verify integrity with an independent tool.
6. Alter one exported copy and verify failure.
7. Test the oversized export and any limits.

**Edge Cases / Variants.** Evidence containing personal data requiring redaction; export by an auditor role.

**Expected Result.** Exports complete in every format; metadata present; integrity verifiable; altered copy fails; limits documented.

**Expected Control Action.** N/A.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Formats documented.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Verification output.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-023"></a>

### TC-L03-023: Multi-Framework Compliance Dashboard: Coverage and Gaps

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | AUD: Audit, evidence and assurance |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | High |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation, evaluation and accountability) |

**Risk Addressed.** Leaders need one view of where the organisation stands against several frameworks, and percentages must be explainable.

**Business Scenario.** Compliance wants coverage, gaps and trends by framework, owner and lifecycle layer.

**Technical Scenario.** Load two frameworks with mappings and evidence states and compare dashboard figures with a hand calculation.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 2 frameworks of 20 requirements each; 40 controls; evidence states (current, stale, missing); owners; 6 months of history.

**Procedure**

1. Load the data.
2. Compare coverage percentages with the calculation sheet.
3. Drill from a percentage to the requirements and evidence.
4. Check trend lines.
5. Filter by owner and lifecycle layer.
6. Check how partly met requirements are counted.
7. Export the view.

**Edge Cases / Variants.** Requirements weighted differently; requirement not applicable to the organisation.

**Expected Result.** Percentages match within 1 percent; drill-down works; partial credit rules visible; filters and export work.

**Expected Control Action.** N/A.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Export.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Calculation comparison.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-024"></a>

### TC-L03-024: Adopting a New Framework: Custom Framework Onboarding

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | AUD: Audit, evidence and assurance |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Critical |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation, evaluation and accountability) |

**Risk Addressed.** The value of a generic library depends on how quickly a new or local framework can be added and mapped without vendor engineering.

**Business Scenario.** Compliance wants to onboard a framework within a working day.

**Technical Scenario.** Create a framework from a requirements list and map existing controls and evidence.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** A fabricated framework of 25 requirements in three domains; 40 existing controls; 30 evidence items; 1 requirement with sub-points.

**Procedure**

1. Create the framework and requirements, including the one with sub-points.
2. Map controls to requirements.
3. Review coverage and gaps.
4. Assign owners.
5. Time the process.
6. Update the framework to a second version and check effect on mappings.
7. Export the framework definition.

**Edge Cases / Variants.** Requirement text with cross-references; framework that applies only to some business units.

**Expected Result.** Framework created and mapped within one working day by the evaluator; sub-points supported; version update handled; export available.

**Expected Control Action.** N/A.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Import and export options.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Time record; coverage view.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-025"></a>

### TC-L03-025: Evidence Reuse Across Frameworks

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | AUD: Audit, evidence and assurance |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | High |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation, evaluation and accountability) |

**Risk Addressed.** Collecting the same evidence several times for different frameworks wastes effort and produces inconsistencies.

**Business Scenario.** Compliance wants one evidence item to support several requirements across frameworks.

**Technical Scenario.** Map evidence to several requirements and test status propagation.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 15 evidence items; 3 frameworks; 45 requirements; 4 items that satisfy a requirement only partly.

**Procedure**

1. Map each item to multiple requirements.
2. Update one item and check status in every framework.
3. Expire an item and check the effect everywhere.
4. Record partial satisfaction.
5. Report reuse rates.
6. Check audit trail of mapping changes.

**Edge Cases / Variants.** Evidence valid only for one jurisdiction.

**Expected Result.** Updates and expiry propagate to every mapped requirement; partial satisfaction visible; reuse report accurate.

**Expected Control Action.** N/A.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Report export.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Propagation test.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-026"></a>

### TC-L03-026: Regulator Inspection Simulation: Rapid Evidence Request

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | AUD: Audit, evidence and assurance |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | Critical |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation, evaluation and accountability) |

**Risk Addressed.** Inspections give short notice and ask for specific records.

**Business Scenario.** Compliance wants the platform tested against a realistic written request.

**Technical Scenario.** Run a timed drill against a written request for fifteen items.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** Request listing 15 items (policy set, processing register extract, rights request log, incident records, transfer records, training records, vendor assessments, impact assessment, control evidence, access logs, retention evidence, board reporting, residency evidence, risk register extract, exception register); time limit set by the assessor; 2 responders.

**Procedure**

1. Issue the request.
2. Collect each item using the platform.
3. Record time per item and gaps.
4. Check redaction of data not requested.
5. Check chain of custody and version stamps.
6. Compile the response.
7. Hold a short review and list improvements.

**Edge Cases / Variants.** Request received outside business hours; request for records older than retention.

**Expected Result.** At least 13 of 15 items produced within the time limit; redaction applied; chain of custody recorded; improvements listed.

**Expected Control Action.** N/A.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Pack export.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Drill record.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-027"></a>

### TC-L03-027: Litigation Hold and Regulatory Preservation Notice

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D6, D7 |
| **Control Theme** | RET: Retention, deletion and preservation |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | High |
| **NIST AI RMF Mapping** | GOVERN and MANAGE (data lifecycle) |

**Risk Addressed.** Deleting data during a dispute or investigation can cause serious consequences, and AI platforms delete on schedule by default.

**Business Scenario.** Legal wants holds applied across AI data and logs.

**Technical Scenario.** Apply a hold and attempt deletion under several routes.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 1 matter; 5 custodians; AI conversations, prompts, outputs, logs and knowledge items; retention expiry and user deletion scenarios.

**Procedure**

1. Create the matter and scope.
2. Apply the hold.
3. Attempt user deletion, administrator deletion and retention expiry.
4. Check that held items remain.
5. Search and export held data.
6. Add a custodian later and check coverage.
7. Release the hold and check normal rules resume.

**Edge Cases / Variants.** Custodian leaves; hold applied after some items were already deleted.

**Expected Result.** Held items preserved under every route; added custodian covered; export works; actions audited.

**Expected Control Action.** Hold.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Export format documented.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Hold audit; deletion attempts.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-028"></a>

### TC-L03-028: Intellectual Property and Copyright Controls for AI Inputs and Outputs

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D3, D7 |
| **Control Theme** | GOV: Governance and accountability |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A, W |
| **Risk Severity** | Medium |
| **NIST AI RMF Mapping** | GOVERN (policies, accountability and oversight) |

**Risk Addressed.** Using restricted content as input, or publishing outputs that copy protected material, creates legal exposure and contract breaches.

**Business Scenario.** Legal wants rules for inputs and outputs enforced and evidenced.

**Technical Scenario.** Configure rules for licensed and restricted content and test inputs and outputs.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 30 fabricated items: 10 with licence markers restricting AI use, 10 with watermarks, 10 clean; outputs from a mock model that reproduces marked content.

**Procedure**

1. Configure rules.
2. Submit the items as inputs.
3. Record decisions.
4. Generate outputs that reproduce marked content.
5. Check detection and labelling on outputs.
6. Check how exceptions and licences are recorded.
7. Check reporting.

**Edge Cases / Variants.** Mixed content with a small restricted portion; content with unclear licence.

**Expected Result.** At least 18 of 20 restricted inputs blocked or flagged; reproduced marked output detected or limitation documented; reporting available.

**Expected Control Action.** Block or label.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Reports.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Decision table.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-029"></a>

### TC-L03-029: Automated Decision Explanation Records

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D3, D7 |
| **Control Theme** | OVS: Human oversight and transparency |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: A, W |
| **Risk Severity** | High |
| **NIST AI RMF Mapping** | GOVERN and MANAGE (human oversight, transparency) |

**Risk Addressed.** People affected by automated decisions may be entitled to meaningful information about the logic and factors involved.

**Business Scenario.** Legal wants explanations generated, stored and retrievable on request.

**Technical Scenario.** Generate explanations for fabricated decisions and test retrieval and content.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 10 fabricated decisions (approve, decline, flag) with 5 to 8 input factors each; 2 requests for explanation.

**Procedure**

1. Run the decisions.
2. Generate and store explanations.
3. Check that the explanation names the main factors and the human review route.
4. Have a non-specialist reviewer rate understandability.
5. Retrieve explanations for the two requests.
6. Check retention and link to the decision record.
7. Check explanation consistency on repeated decisions.

**Edge Cases / Variants.** Complex multi-model decisions; decisions revised after appeal.

**Expected Result.** Explanations available for all decisions and retrievable; reviewer finds at least 8 of 10 understandable; consistency across repeats.

**Expected Control Action.** N/A.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Export.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Explanation samples; reviewer scores.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l03-030"></a>

### TC-L03-030: Language and Jurisdiction Configuration (Arabic, English and Regional Rule Sets)

| Field | Value |
|---|---|
| **Lifecycle Layer** | L03 Legal, Privacy & Compliance |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | XBT: Cross-border transfer, residency and jurisdiction |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, A |
| **Risk Severity** | Medium |
| **NIST AI RMF Mapping** | GOVERN and MAP (legal and regulatory requirements, third-party context) |

**Risk Addressed.** Notices, forms and rule sets must work in the languages and jurisdictions in which the organisation operates.

**Business Scenario.** Compliance wants multilingual and jurisdiction-specific configuration without separate tools.

**Technical Scenario.** Configure two jurisdictions and two languages and test notices, forms and reports.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample processing activities, individuals, requests and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (response timelines, notification periods, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 2 jurisdictions with different rule sets entered by the assessor; Arabic and English; notices, request forms and reports; 1 user in each combination.

**Procedure**

1. Configure the jurisdictions and rule sets.
2. Assign users.
3. Check that different rules apply per jurisdiction.
4. Check notices and forms in both languages.
5. Check right-to-left layout, numerals and dates.
6. Check reports in each language.
7. Check what happens for a user in a third jurisdiction.

**Edge Cases / Variants.** Mixed-language documents; users who travel.

**Expected Result.** Rules apply per jurisdiction; both languages correct including right-to-left rendering; reports in both languages; third jurisdiction handled by a defined default.

**Expected Control Action.** N/A.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Export.

**Audit Evidence.** Record identifier, actor, timestamp, before and after values, approval reference and source evidence exportable for audit.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Framework Crosswalk *(assessor to complete)***

- ISO/IEC 27001 ISMS: `________`
- India DPDP: `________`
- UAE NESA / information assurance: `________`
- UAE PDPL: `________`
- Other: `________`

**Scoring Criteria.** 0 = not demonstrated; 3 = demonstrated but with missing fields, manual workarounds or SLA exceeded; 5 = fully met in the live product with complete evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Screenshots.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

