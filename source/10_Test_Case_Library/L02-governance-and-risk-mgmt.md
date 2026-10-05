---
title: "L02 Governance & Risk Mgmt"
parent: "Test Case Library"
nav_order: 5
---

<a id="top"></a>

# L02 Governance & Risk Mgmt

**Primary test focus:** policy-to-control mapping, risk register, exceptions workflow

**Cases:** 25 (TC-L02-001 to TC-L02-025)  |  **Batch:** 6

> **Safety boundary.** All cases use fabricated use cases, policies, records and individuals only. This layer is framework-neutral: see the [Framework Adoption Guide](framework-adoption-guide.md) before testing, and complete the Applicable Requirement and Framework Crosswalk fields for each case.

> **Verify before use.** MITRE ATLAS, OWASP LLM and NIST AI RMF identifiers must be checked against the current published versions. Numeric thresholds are starting values to tune. See the [Reference Index](00-reference-index.md) for field definitions and applicability codes.

## Cases in this layer

| ID | Title | Severity | Method | Domain(s) |
|---|---|---|---|---|
| [TC-L02-001](#tc-l02-001) | AI Policy Framework: Scope, Ownership, Approval and Review Cycle | High | Evidence | D7 |
| [TC-L02-002](#tc-l02-002) | Policy-to-Control Mapping | Critical | Technical | D3, D7 |
| [TC-L02-003](#tc-l02-003) | Control Library and Multi-Framework Crosswalk Capability | Critical | Technical | D7 |
| [TC-L02-004](#tc-l02-004) | Roles and Responsibilities (RACI) Recorded and Enforced | High | Technical | D3 |
| [TC-L02-005](#tc-l02-005) | AI Governance Committee Workflow and Decision Record | Medium | Evidence | D3, D7 |
| [TC-L02-006](#tc-l02-006) | AI Risk Register: Creation, Scoring and Ownership | Critical | Technical | D3 |
| [TC-L02-007](#tc-l02-007) | Risk Assessment Consistency Between Assessors | High | Technical | D3 |
| [TC-L02-008](#tc-l02-008) | Risk Treatment Tracking | High | Technical | D3 |
| [TC-L02-009](#tc-l02-009) | Residual Risk Acceptance with Authority Limits | Critical | Technical | D3, D7 |
| [TC-L02-010](#tc-l02-010) | Exception and Waiver Workflow: Request, Approval, Expiry and Review | Critical | Technical | D3, D7 |
| [TC-L02-011](#tc-l02-011) | Exception Expiry Enforced in Technical Controls | High | Technical | D1, D3 |
| [TC-L02-012](#tc-l02-012) | Exception Reporting, Ageing and Concentration | Medium | Evidence | D3 |
| [TC-L02-013](#tc-l02-013) | Control Effectiveness Measurement and Evidence Freshness | Critical | Technical | D3, D7 |
| [TC-L02-014](#tc-l02-014) | Control Owner Attestation | Medium | Technical | D3 |
| [TC-L02-015](#tc-l02-015) | Automated Evidence Collection and Freshness | High | Technical | D3, D7 |
| [TC-L02-016](#tc-l02-016) | Audit Readiness: Evidence Pack on Demand | Critical | Technical | D7 |
| [TC-L02-017](#tc-l02-017) | Internal and External Audit Support: Read-Only Access and Sampling | High | Technical | D7 |
| [TC-L02-018](#tc-l02-018) | Finding, Nonconformity and Corrective Action Management | High | Technical | D3 |
| [TC-L02-019](#tc-l02-019) | Governance Metrics and KPI Reporting | Medium | Evidence | D7 |
| [TC-L02-020](#tc-l02-020) | Regulatory and Framework Change Management | High | Technical | D7 |
| [TC-L02-021](#tc-l02-021) | Third-Party Governance Integration | High | Technical | D7 |
| [TC-L02-022](#tc-l02-022) | Training and Awareness Tracking for AI Policies | Medium | Technical | D1, D7 |
| [TC-L02-023](#tc-l02-023) | Acceptable Use Acknowledgement and Re-Acknowledgement | Medium | Technical | D1, D7 |
| [TC-L02-024](#tc-l02-024) | Management Review Inputs and Outputs | Medium | Evidence | D7 |
| [TC-L02-025](#tc-l02-025) | Governance Record Integrity: Change History and Tamper Evidence | High | Technical | D7 |

---

## Test cases

<a id="tc-l02-001"></a>

### TC-L02-001: AI Policy Framework: Scope, Ownership, Approval and Review Cycle

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | POL: Policy and standards |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN (policies and procedures) |

**Risk Addressed.** Policies without an owner, approval and review date are ignored and cannot be defended in an audit.

**Business Scenario.** Governance wants each AI policy and standard held with its metadata and review status in one place.

**Technical Scenario.** Load a set of fabricated policies and check metadata handling, review reminders and publication to users.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 8 fabricated policies and standards (acceptable use, data handling for AI, model approval, agent permissions, third-party AI, incident response for AI, logging and monitoring, exception handling); metadata fields: owner, approver, version, effective date, next review, scope, framework references.

**Procedure**

1. Load the 8 documents and fill metadata.
2. Check mandatory metadata enforcement.
3. Move one policy through draft, review, approval and publication.
4. Backdate one review date and check reminders and overdue reporting.
5. Check version history and the ability to compare versions.
6. Check publication to staff and acknowledgement tracking.
7. Export the policy register.

**Edge Cases / Variants.** Policy owned by two functions; policy retired and replaced.

**Expected Result.** Mandatory metadata enforced; workflow states recorded with approver and time; overdue reviews flagged; version comparison available; register exportable.

**Expected Control Action.** N/A.

**Expected Record / Log.** Configuration state, record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Register exportable to GRC.

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

**Evidence to Capture.** Register export; workflow audit trail.

**Reviewer Notes.** Confirm the evidence is taken from the live product. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l02-002"></a>

### TC-L02-002: Policy-to-Control Mapping

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D3, D7 |
| **Control Theme** | POL: Policy and standards |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN (policies and procedures) |

**Risk Addressed.** A policy statement with no control behind it is a promise, not a safeguard.

**Business Scenario.** Governance wants each policy statement mapped to the controls that enforce it and to the evidence that proves it.

**Technical Scenario.** Break two policies into statements and map each to platform controls, then test the mapping against actual enforcement.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 2 policies decomposed into 30 statements (for example 'agents must not access production data without approval', 'prompts containing personal data must not be sent to unapproved services'); control inventory from the platform; 6 statements with no suitable control.

**Procedure**

1. Decompose the policies into statements.
2. Map each statement to one or more controls and evidence sources.
3. Review unmapped statements.
4. For five mapped statements, test the control in the lab and confirm it enforces the statement.
5. Check that mappings update when a control changes.
6. Export the traceability matrix.

**Edge Cases / Variants.** Statements enforced only by human process; statements enforced by several controls in combination.

**Expected Result.** All 30 statements mapped or flagged as gaps; unmapped statements reported; five tested controls enforce their statements; matrix exportable.

**Expected Control Action.** N/A.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Matrix to GRC.

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

**Evidence to Capture.** Traceability matrix; enforcement tests.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l02-003"></a>

### TC-L02-003: Control Library and Multi-Framework Crosswalk Capability

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | AUD: Audit, evidence and assurance |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation, evaluation and accountability) |

**Risk Addressed.** Organisations answer to several frameworks; mapping each separately wastes effort and produces inconsistent answers.

**Business Scenario.** Compliance wants one control set mapped to several frameworks.

**Technical Scenario.** Load a control set, map it to two frameworks and add a third custom framework.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** Control set of 40 generic controls; two framework templates entered by the assessor (any two from the adopted list, as short lists of 15 requirements each); one custom framework of 10 requirements built during the test.

**Procedure**

1. Load the control set.
2. Load the two framework requirement lists.
3. Map controls to requirements (many to many).
4. Check coverage views per framework.
5. Create the custom framework and map it.
6. Change one control and check effect on all mapped frameworks.
7. Export the crosswalk.

**Edge Cases / Variants.** Requirement mapped to controls from several layers; framework updated to a new version.

**Expected Result.** Many-to-many mapping supported; coverage correct per framework; custom framework added without vendor assistance within one hour; change propagates; crosswalk exportable.

**Expected Control Action.** N/A.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Crosswalk export.

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

**Evidence to Capture.** Coverage views; export.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l02-004"></a>

### TC-L02-004: Roles and Responsibilities (RACI) Recorded and Enforced

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D3 |
| **Control Theme** | GOV: Governance and accountability |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN (policies, accountability and oversight) |

**Risk Addressed.** Unclear responsibility means decisions are not taken, and approvals by the wrong person undermine the control.

**Business Scenario.** Governance wants responsibilities recorded and approval rights enforced by role.

**Technical Scenario.** Define roles and test whether the platform enforces who may approve, change and view.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 6 roles (executive sponsor, risk owner, control owner, use-case owner, privacy lead, auditor); 10 actions (approve use case, accept risk, change policy, grant exception, view evidence, edit control mapping, and similar); 4 test users.

**Procedure**

1. Define the RACI matrix.
2. Assign users to roles.
3. Attempt each action as each user.
4. Compare with the matrix.
5. Attempt separation-of-duties violations (requestor approves own request).
6. Check audit of role changes.
7. Check delegation and absence handling.

**Edge Cases / Variants.** User holding two conflicting roles; role holder on leave.

**Expected Result.** All outcomes match the matrix; separation of duties enforced; role changes audited; delegation time-limited.

**Expected Control Action.** Block.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Role sync from the directory.

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

**Evidence to Capture.** Outcome matrix; audit extract.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l02-005"></a>

### TC-L02-005: AI Governance Committee Workflow and Decision Record

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D3, D7 |
| **Control Theme** | GOV: Governance and accountability |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN (policies, accountability and oversight) |

**Risk Addressed.** Committee decisions recorded in email threads cannot be evidenced or tracked.

**Business Scenario.** Governance wants meetings, decisions and actions recorded and linked to the items decided.

**Technical Scenario.** Run a mock committee cycle in the platform.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 1 meeting; agenda of 5 items (2 use case approvals, 1 risk acceptance, 1 policy change, 1 exception); 5 members; quorum rule.

**Procedure**

1. Schedule the meeting and build the agenda from pending items.
2. Record attendance and quorum.
3. Record decisions with rationale.
4. Create actions with owners and dates.
5. Check that decisions update the linked items.
6. Generate minutes.
7. Check follow-up tracking at the next meeting.

**Edge Cases / Variants.** Decision reversed at the following meeting; conflict of interest declared.

**Expected Result.** Decisions linked to items and applied; quorum recorded; actions tracked; minutes generated and retained.

**Expected Control Action.** N/A.

**Expected Record / Log.** Configuration state, record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Minutes export.

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

**Evidence to Capture.** Minutes; action tracker.

**Reviewer Notes.** Confirm the evidence is taken from the live product. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l02-006"></a>

### TC-L02-006: AI Risk Register: Creation, Scoring and Ownership

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D3 |
| **Control Theme** | RSK: Risk management |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MAP and MANAGE (risk identification and treatment) |

**Risk Addressed.** A register with unowned or unscored risks gives false comfort and cannot support decisions.

**Business Scenario.** Risk management wants AI risks recorded with scoring, owners and links to use cases and controls.

**Technical Scenario.** Create fabricated AI risks and test scoring, linkage and ownership rules.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 15 fabricated risks (training data leakage, agent over-permission, model drift, vendor lock-in, prompt injection, unlawful transfer, biased outcomes, and similar); scoring method defined by the organisation (likelihood and impact scales).

**Procedure**

1. Enter the scoring method.
2. Create the 15 risks with owners.
3. Check calculated scores and rating bands.
4. Link risks to use cases, controls and incidents.
5. Check validation (owner required, score justification).
6. Check history of score changes.
7. Export the register and a heat map.

**Edge Cases / Variants.** Risk with several owners; risk spanning several use cases.

**Expected Result.** Scores calculated per the method; links work; validation enforced; history retained; heat map and export available.

**Expected Control Action.** N/A.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Export to enterprise risk tools.

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

**Evidence to Capture.** Register export; heat map.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l02-007"></a>

### TC-L02-007: Risk Assessment Consistency Between Assessors

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D3 |
| **Control Theme** | RSK: Risk management |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MAP and MANAGE (risk identification and treatment) |

**Risk Addressed.** Assessments that depend on who performs them produce unreliable rankings.

**Business Scenario.** Risk management wants assessment guidance that gives similar results across people.

**Technical Scenario.** Have two assessors rate the same ten scenarios independently.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 10 fabricated risk scenarios; two assessors; scoring guidance and examples embedded in the platform.

**Procedure**

1. Provide the scenarios.
2. Assessor A rates all ten.
3. Assessor B rates all ten independently.
4. Compare scores and bands.
5. Review the guidance the platform provides at rating time.
6. Check rationale capture.
7. Check calibration features (examples, historical decisions).

**Edge Cases / Variants.** Scenarios with incomplete information.

**Expected Result.** At least 8 of 10 within the same band; rationale captured for each rating; guidance available at the point of rating.

**Expected Control Action.** N/A.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Comparison export.

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

**Evidence to Capture.** Score comparison.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l02-008"></a>

### TC-L02-008: Risk Treatment Tracking

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D3 |
| **Control Theme** | RSK: Risk management |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MAP and MANAGE (risk identification and treatment) |

**Risk Addressed.** Risks that are accepted by default or left untreated accumulate silently.

**Business Scenario.** Risk management wants treatment decisions, tasks and due dates tracked to closure.

**Technical Scenario.** Record treatment decisions for ten risks and track tasks.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 10 risks with decisions: 4 mitigate, 2 accept, 2 transfer, 2 avoid; 14 tasks with owners and due dates; 3 overdue.

**Procedure**

1. Record decisions.
2. Create tasks and link to controls.
3. Check overdue handling and escalation.
4. Complete tasks and check effect on residual risk.
5. Check evidence attachment.
6. Report treatment status.

**Edge Cases / Variants.** Task blocked by a vendor; task spanning two quarters.

**Expected Result.** Decisions recorded; overdue tasks escalated; residual risk updates; evidence attached; status report accurate.

**Expected Control Action.** Escalate.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Tasks to ticketing.

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

**Evidence to Capture.** Treatment report.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l02-009"></a>

### TC-L02-009: Residual Risk Acceptance with Authority Limits

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D3, D7 |
| **Control Theme** | RSK: Risk management |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MAP and MANAGE (risk identification and treatment) |

**Risk Addressed.** Risk acceptance by someone without authority is invalid and often hidden.

**Business Scenario.** Governance wants acceptance limited by authority level and time.

**Technical Scenario.** Attempt acceptances at different levels and check enforcement.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 5 risks of different residual levels; authority limits (for example low by owner, medium by committee, high by executive); acceptance expiry of 12 months.

**Procedure**

1. Configure limits and expiry.
2. Attempt acceptance of each risk by each level.
3. Check blocks and routing.
4. Accept a risk validly and record rationale.
5. Backdate to expiry and check reminders.
6. Check the acceptance register.

**Edge Cases / Variants.** Acceptance by a delegate; risk whose level changes after acceptance.

**Expected Result.** Acceptances above authority blocked and routed; valid acceptance recorded with rationale; expiry reminders; register accurate.

**Expected Control Action.** Block and route.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Register export.

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

**Evidence to Capture.** Attempt table.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l02-010"></a>

### TC-L02-010: Exception and Waiver Workflow: Request, Approval, Expiry and Review

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D3, D7 |
| **Control Theme** | GOV: Governance and accountability |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN (policies, accountability and oversight) |

**Risk Addressed.** Exceptions without expiry become permanent holes in policy.

**Business Scenario.** Governance wants exceptions approved, time-limited and reviewed.

**Technical Scenario.** Run exceptions through the platform with different scopes and durations.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 8 exception requests (policy, control, use case); durations from 1 day to 12 months; 2 requests with missing justification; approvers by risk level.

**Procedure**

1. Submit the 8 requests.
2. Check validation of justification and compensating controls.
3. Route and approve or reject.
4. Check expiry dates and reminders.
5. Backdate and check automatic expiry and effect.
6. Check review at renewal.
7. Check reporting by age and owner.

**Edge Cases / Variants.** Exception requested after the fact; exception covering many systems.

**Expected Result.** Missing justification rejected; compensating controls recorded; expiry enforced; renewals require review; reports accurate.

**Expected Control Action.** Gate.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Exceptions feed enforcement tools.

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

**Evidence to Capture.** Workflow audit; expiry test.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l02-011"></a>

### TC-L02-011: Exception Expiry Enforced in Technical Controls

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D1, D3 |
| **Control Theme** | GOV: Governance and accountability |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, E, G |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN (policies, accountability and oversight) |

**Risk Addressed.** An expired exception on paper is meaningless if the technical control still allows the activity.

**Business Scenario.** Security wants expiry reflected in enforcement without manual work.

**Technical Scenario.** Grant a short exception that opens a technical control, then let it expire.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 2 exceptions (access to a blocked AI tool, bypass of an agent approval step); 1-hour validity; 2 test users.

**Procedure**

1. Grant the exceptions.
2. Verify the controls allow the activities.
3. Wait for or advance to expiry.
4. Re-test.
5. Check logs of enforcement change.
6. Extend one exception and check approval needed.

**Edge Cases / Variants.** Exception expiring during an active session.

**Expected Result.** Controls revert at expiry within the stated time without manual change; logs record change; extension requires approval.

**Expected Control Action.** Revert.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Integration with enforcement tools.

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

**Evidence to Capture.** Before and after tests.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l02-012"></a>

### TC-L02-012: Exception Reporting, Ageing and Concentration

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D3 |
| **Control Theme** | GOV: Governance and accountability |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN (policies, accountability and oversight) |

**Risk Addressed.** A growing pile of old exceptions signals a control that does not fit the business, or a risk being tolerated by default.

**Business Scenario.** Governance wants exceptions reported by age, owner, control and risk.

**Technical Scenario.** Load a fabricated exception population and test the reports.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 60 exceptions with ages from 1 day to 3 years, 8 owners, 12 controls, 4 risk levels; 10 expired but still active; 5 renewed more than twice.

**Procedure**

1. Load the exceptions.
2. Run reports by age, owner, control and risk.
3. Check counts against the calculation sheet.
4. Check flags for repeated renewal and expired-but-active items.
5. Check drill-down.
6. Schedule the report and check delivery.
7. Export.

**Edge Cases / Variants.** Exceptions covering several controls; exceptions without an owner.

**Expected Result.** Counts exact; repeated renewals and expired-active items flagged; drill-down works; scheduled delivery works.

**Expected Control Action.** N/A.

**Expected Record / Log.** Configuration state, record or export that supports the claim, with timestamp and the identity of the person who produced it.

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

**Scoring Criteria.** 0 = not demonstrated; 3 = partly shown or shown only from documentation; 5 = shown in the live product with exportable evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Report vs calculation sheet.

**Reviewer Notes.** Confirm the evidence is taken from the live product. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l02-013"></a>

### TC-L02-013: Control Effectiveness Measurement and Evidence Freshness

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D3, D7 |
| **Control Theme** | AUD: Audit, evidence and assurance |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation, evaluation and accountability) |

**Risk Addressed.** A control that existed at design time but is not working today is the most common audit finding.

**Business Scenario.** Compliance wants controls tested regularly and evidence age visible.

**Technical Scenario.** Define test procedures for ten controls and run them, including controls that have degraded.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 10 controls with test procedures (for example 'agent kill switch works', 'sensitive paste blocked', 'access removed on leaving'); 3 controls deliberately misconfigured in the lab; evidence age thresholds.

**Procedure**

1. Define the test procedure and frequency for each control.
2. Run the tests (manual and automated where supported).
3. Record results and evidence.
4. Check that the 3 degraded controls are shown as ineffective.
5. Check ageing: backdate evidence beyond the threshold.
6. Check the effect on compliance status.
7. Report effectiveness by control and by framework.

**Edge Cases / Variants.** Control tested by its own owner; control with no automated test.

**Expected Result.** All 3 degraded controls detected; stale evidence flagged; compliance status updates; reports available by framework.

**Expected Control Action.** N/A.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Test results to GRC.

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

**Evidence to Capture.** Test results; stale evidence flag.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l02-014"></a>

### TC-L02-014: Control Owner Attestation

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D3 |
| **Control Theme** | AUD: Audit, evidence and assurance |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation, evaluation and accountability) |

**Risk Addressed.** Periodic attestation keeps accountability current and catches silent changes, but only if non-response and negative answers are handled.

**Business Scenario.** Compliance wants control owners to attest on a schedule with evidence, and exceptions to be followed up.

**Technical Scenario.** Run an attestation campaign for twelve controls with non-responding and dissenting owners.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 12 controls; 6 owners; 14-day campaign window; 2 owners who never respond; 1 owner who attests that a control is not effective; 1 owner who leaves the organisation during the campaign.

**Procedure**

1. Create the campaign with the question set (control operated as designed, evidence available, changes since last period).
2. Send to owners.
3. Track responses, reminders and escalation to line managers.
4. Check the negative attestation creates a finding.
5. Check evidence attachment requirements.
6. Handle the leaver: check reassignment.
7. Check campaign history and comparison with the previous period.

**Edge Cases / Variants.** Owner attesting for a control run by a supplier; attestation by a delegate.

**Expected Result.** Reminders and escalation operate; negative attestation creates a finding with owner and date; leaver's controls reassigned; history retained and comparable.

**Expected Control Action.** Escalate.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Directory integration.

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

**Evidence to Capture.** Campaign report; finding record.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l02-015"></a>

### TC-L02-015: Automated Evidence Collection and Freshness

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D3, D7 |
| **Control Theme** | AUD: Audit, evidence and assurance |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation, evaluation and accountability) |

**Risk Addressed.** Point-in-time evidence collected manually before an audit is expensive and often stale.

**Business Scenario.** Compliance wants evidence collected from the platform continuously and dated.

**Technical Scenario.** Configure automated evidence sources and check content, timing and gaps.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 10 evidence items (policy documents, configuration exports, access lists, log samples, test results, training records, vendor reports, incident records, risk register snapshot, inventory); 3 sources deliberately interrupted.

**Procedure**

1. Configure the collection schedule.
2. Check items collected and timestamps.
3. Interrupt three sources.
4. Check gap alerts.
5. Check integrity (hash) and immutability of stored evidence.
6. Check retention.
7. Check mapping of each item to controls.

**Edge Cases / Variants.** Source changes format; evidence containing personal data.

**Expected Result.** Evidence collected on schedule; gaps alerted within the stated time; integrity protected; mapping to controls shown.

**Expected Control Action.** Alert.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Connectors and APIs.

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

**Evidence to Capture.** Collection log.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l02-016"></a>

### TC-L02-016: Audit Readiness: Evidence Pack on Demand

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | AUD: Audit, evidence and assurance |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation, evaluation and accountability) |

**Risk Addressed.** Last-minute scrambling for evidence is a symptom of weak control.

**Business Scenario.** Compliance wants an evidence pack for any selected framework produced quickly.

**Technical Scenario.** Request evidence packs for two frameworks and for a sampled period.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** Two frameworks (from the adopted list); 20 requirements each; 12 months of fabricated evidence; 3 requirements with missing evidence.

**Procedure**

1. Select framework and period.
2. Generate the pack.
3. Check mapping of evidence to each requirement.
4. Check missing evidence is clearly shown.
5. Check export formats and integrity.
6. Time the process.
7. Check redaction of sensitive data in the pack.

**Edge Cases / Variants.** Framework with sub-clauses; sampling over a period.

**Expected Result.** Pack covers at least 90 percent of requirements with the correct evidence; missing items listed; generated within 1 hour; sensitive data redacted.

**Expected Control Action.** N/A.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Export formats.

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

**Evidence to Capture.** Pack sample; timing.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l02-017"></a>

### TC-L02-017: Internal and External Audit Support: Read-Only Access and Sampling

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | AUD: Audit, evidence and assurance |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation, evaluation and accountability) |

**Risk Addressed.** Auditors need enough access to reach a conclusion, without any ability to change what they examine.

**Business Scenario.** Audit wants auditor access that is read-only, scoped, time-limited and logged.

**Technical Scenario.** Create an auditor role and run a sampling exercise across several record types.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 1 auditor role; 300 records (change records, exceptions, incidents, access reviews, approvals); sample size of 25; 2 auditors, one external with a 5-day window.

**Procedure**

1. Create the role with scope and time limit.
2. Attempt every change action as the auditor.
3. Draw a random sample and a risk-based sample.
4. Retrieve underlying evidence for each sampled item.
5. Check that auditor requests and views are logged.
6. Check export restrictions.
7. Let the external access expire and revoke the internal one early; verify both.

**Edge Cases / Variants.** Auditor requesting evidence containing personal data; sampling across two systems.

**Expected Result.** Auditor cannot change any record; samples drawn reproducibly with the seed recorded; evidence retrievable; access fully logged; expiry and revocation immediate.

**Expected Control Action.** Restrict.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Access log export.

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

**Evidence to Capture.** Access test results; log extract.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l02-018"></a>

### TC-L02-018: Finding, Nonconformity and Corrective Action Management

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D3 |
| **Control Theme** | AUD: Audit, evidence and assurance |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation, evaluation and accountability) |

**Risk Addressed.** Findings not tracked to closure recur, and unverified closure is a repeat finding in waiting.

**Business Scenario.** Compliance wants findings recorded, assigned, tracked and independently verified.

**Technical Scenario.** Record findings from the PoC and follow corrective actions through to verified closure.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 8 findings of differing severity from earlier tests; owners; due dates; 2 overdue; 1 disputed by the owner; 1 requiring a vendor fix.

**Procedure**

1. Create each finding with source evidence and severity.
2. Assign actions with due dates.
3. Check reminders and escalation by severity and age.
4. Close two actions with evidence and check independent verification is required.
5. Process the disputed finding including recorded outcome.
6. Link the vendor-fix finding to the vendor assessment.
7. Report ageing and recurrence.

**Edge Cases / Variants.** Finding raised by an external regulator; action that closes only after a release.

**Expected Result.** Overdue items escalated; closure needs evidence and an independent verifier; dispute recorded with outcome; vendor link works; ageing and recurrence reports accurate.

**Expected Control Action.** Escalate.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Tickets and vendor register.

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

**Evidence to Capture.** Finding report.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l02-019"></a>

### TC-L02-019: Governance Metrics and KPI Reporting

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | GOV: Governance and accountability |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN (policies, accountability and oversight) |

**Risk Addressed.** Boards cannot oversee what is not measured, and unexplained metrics get ignored.

**Business Scenario.** Leadership wants a small, defined set of governance indicators that can be traced to records.

**Technical Scenario.** Load simulated records and compare each indicator with hand calculation.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 12 months of simulated data; 12 indicators: policies in date, open exceptions, risks above appetite, overdue actions, attestations on time, training completion, AI incidents, open audit findings, coverage by framework, evidence freshness, vendors without assessment, use cases without owner; calculation sheet prepared in advance.

**Procedure**

1. Load the data.
2. Compare each indicator with the calculation sheet.
3. Check that definitions can be inspected.
4. Check trend lines and threshold colouring.
5. Drill down from two indicators to the records.
6. Schedule a board report and check content and access control.
7. Change a definition and check restatement and change record.

**Edge Cases / Variants.** Indicator definitions that differ between frameworks; restated history.

**Expected Result.** At least 11 of 12 indicators match within 2 percent; definitions visible; drill-down works; definition changes recorded.

**Expected Control Action.** N/A.

**Expected Record / Log.** Configuration state, record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Report export and scheduling.

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

**Evidence to Capture.** Indicator comparison table.

**Reviewer Notes.** Confirm the evidence is taken from the live product. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l02-020"></a>

### TC-L02-020: Regulatory and Framework Change Management

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | GOV: Governance and accountability |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN (policies, accountability and oversight) |

**Risk Addressed.** New or revised requirements are missed or implemented late, and nobody can show how a change was handled.

**Business Scenario.** Compliance wants changes traced from the requirement through impact assessment to control update.

**Technical Scenario.** Record a framework update and follow it through the platform.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 1 framework update: 3 new requirements, 2 changed, 1 withdrawn, 1 with a future effective date; 40 mapped controls; 12 affected use cases.

**Procedure**

1. Record the update and effective dates.
2. Run impact analysis on mapped controls, use cases and policies.
3. Create tasks with owners.
4. Update mappings and policies.
5. Check the gap view before and after.
6. Check handling of the withdrawn requirement.
7. Check history and reporting of time to implement.

**Edge Cases / Variants.** Overlapping requirements from two frameworks; jurisdiction-specific requirement.

**Expected Result.** Impacted items listed; tasks created; gap view correct; withdrawal handled; history and timing recorded.

**Expected Control Action.** N/A.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Update import where offered.

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

**Evidence to Capture.** Impact report; history.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l02-021"></a>

### TC-L02-021: Third-Party Governance Integration

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | VND: Third-party and supplier management |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN and MAP (third-party and supply chain risk) |

**Risk Addressed.** Third-party AI risk managed in a separate tool becomes disconnected from the risk register and use-case approvals.

**Business Scenario.** Governance wants vendor assessments linked to risks, use cases and findings.

**Technical Scenario.** Link vendors to use cases and risks and test alerts and propagation.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 6 vendors with assessments of differing age; 2 with open critical findings; 5 use cases; 1 vendor with an expired assessment.

**Procedure**

1. Link vendors to use cases.
2. Import assessment status and findings.
3. Check that critical findings create or update risk entries.
4. Check alerts when an assessment expires.
5. Check the effect on use-case status or required review.
6. Report vendors without assessment.
7. Export.

**Edge Cases / Variants.** Vendor serving many use cases; vendor with several legal entities.

**Expected Result.** Links work in both directions; findings create risk entries; expiry alerts raised; use-case review triggered; export available.

**Expected Control Action.** Alert.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Vendor management tool integration.

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

**Evidence to Capture.** Link view; alerts.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l02-022"></a>

### TC-L02-022: Training and Awareness Tracking for AI Policies

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D1, D7 |
| **Control Theme** | TRN: Training and awareness |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN (workforce competence and awareness) |

**Risk Addressed.** Policies are not followed if people do not know them, and many frameworks expect evidence of awareness and training.

**Business Scenario.** HR and compliance want completion tracked by role with evidence.

**Technical Scenario.** Assign courses by role and track completion, overdue handling and new joiners.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 40 test users across 4 roles (general staff, developers, data scientists, administrators); 3 courses; 5 users overdue; 3 new joiners; 2 contractors.

**Procedure**

1. Define role-to-course mapping.
2. Assign courses.
3. Track completion through the learning system integration or manual upload.
4. Check reminders and escalation.
5. Handle new joiners and contractors.
6. Check assessment pass marks if applicable.
7. Export completion evidence by role and period.

**Edge Cases / Variants.** Staff changing role; training in two languages.

**Expected Result.** Assignments follow roles; escalation works; joiners and contractors handled; export accurate.

**Expected Control Action.** Escalate.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Learning system integration.

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

**Evidence to Capture.** Completion report.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l02-023"></a>

### TC-L02-023: Acceptable Use Acknowledgement and Re-Acknowledgement

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D1, D7 |
| **Control Theme** | TRN: Training and awareness |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, E |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN (workforce competence and awareness) |

**Risk Addressed.** Acknowledgement of AI acceptable use is often the first evidence requested after an incident.

**Business Scenario.** Compliance wants acknowledgements captured, dated, version-linked and renewed.

**Technical Scenario.** Run an acknowledgement campaign that includes a policy version change.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 40 users; 1 acceptable use policy; v1 then v2 published mid-campaign; 5 users who do not acknowledge.

**Procedure**

1. Publish v1.
2. Collect acknowledgements.
3. Publish v2 and check re-acknowledgement is triggered.
4. Check the effect on access for non-acknowledged users per configured policy.
5. Check reminders and escalation.
6. Report by user, version and date.
7. Check evidence integrity.

**Edge Cases / Variants.** Users on long leave; multi-language policy versions.

**Expected Result.** Re-acknowledgement triggered by the new version; non-acknowledged users handled per policy; reports accurate; evidence tamper-evident.

**Expected Control Action.** Gate.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Directory integration.

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

**Evidence to Capture.** Acknowledgement report.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l02-024"></a>

### TC-L02-024: Management Review Inputs and Outputs

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | GOV: Governance and accountability |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN (policies, accountability and oversight) |

**Risk Addressed.** Several management system standards require review of defined inputs by top management with recorded outputs.

**Business Scenario.** Governance wants a standard review pack and tracked decisions.

**Technical Scenario.** Prepare and run a mock management review using platform data.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** Input categories: audit results, incident summary, risk status, KPI trends, changes in context, supplier performance, improvement opportunities; 5 reviewers; 6 decisions.

**Procedure**

1. Generate the input pack.
2. Check each input category is present and sourced.
3. Run the review and record attendance.
4. Record decisions and rationale.
5. Create actions with owners.
6. Check follow-up at the next cycle.
7. Export the minutes.

**Edge Cases / Variants.** Review postponed; decisions overturned.

**Expected Result.** Pack covers every category with data sources; decisions and actions recorded and tracked; follow-up visible; minutes exportable.

**Expected Control Action.** N/A.

**Expected Record / Log.** Configuration state, record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Minutes export.

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

**Evidence to Capture.** Review record.

**Reviewer Notes.** Confirm the evidence is taken from the live product. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l02-025"></a>

### TC-L02-025: Governance Record Integrity: Change History and Tamper Evidence

| Field | Value |
|---|---|
| **Lifecycle Layer** | L02 Governance & Risk Mgmt |
| **Use-Case Domain(s)** | D7 |
| **Control Theme** | AUD: Audit, evidence and assurance |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation, evaluation and accountability) |

**Risk Addressed.** Records that can be edited silently have little evidential value in an audit, dispute or investigation.

**Business Scenario.** Audit wants history and tamper evidence on governance records.

**Technical Scenario.** Alter key records under different roles and check history, protection and detection.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample policies, risks, exceptions and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, review periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** Records: policies, risks, exceptions, approvals, attestations; 3 roles; 20 edits including 3 attempts to delete history and 3 backdated edits.

**Procedure**

1. Edit each record type and review history entries (who, what, when, before and after).
2. Attempt to delete or alter history as each role.
3. Attempt backdating.
4. Check alerts on suspicious changes.
5. Export records with integrity proof and verify independently.
6. Alter an exported copy and check verification fails.
7. Check bulk-edit handling.

**Edge Cases / Variants.** Edits through the API; bulk import overwriting records.

**Expected Result.** History complete with before and after values; deletion and backdating blocked or flagged; integrity proof verifies and fails for altered copies; bulk edits recorded individually.

**Expected Control Action.** Block.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Audit export.

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

**Evidence to Capture.** History extract; verification output.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

