---
title: "L01 Business & Use Cases"
parent: "Test Case Library"
nav_order: 4
---

<a id="top"></a>

# L01 Business & Use Cases

**Primary test focus:** use-case registry, risk-tiering, business-owner attribution

**Cases:** 20 (TC-L01-001 to TC-L01-020)  |  **Batch:** 6

> **Safety boundary.** All cases use fabricated use cases, policies, records and individuals only. This layer is framework-neutral: see the [Framework Adoption Guide](framework-adoption-guide.md) before testing, and complete the Applicable Requirement and Framework Crosswalk fields for each case.

> **Verify before use.** MITRE ATLAS, OWASP LLM and NIST AI RMF identifiers must be checked against the current published versions. Numeric thresholds are starting values to tune. See the [Reference Index](00-reference-index.md) for field definitions and applicability codes.

## Cases in this layer

| ID | Title | Severity | Method | Domain(s) |
|---|---|---|---|---|
| [TC-L01-001](#tc-l01-001) | AI Use-Case Registry: Creation, Mandatory Fields and Uniqueness | High | Technical | D3, D7 |
| [TC-L01-002](#tc-l01-002) | Use-Case Intake and Approval Workflow Before Deployment | Critical | Technical | D3, D7 |
| [TC-L01-003](#tc-l01-003) | Business Owner and Accountable Executive Attribution | High | Technical | D3 |
| [TC-L01-004](#tc-l01-004) | Use-Case to System, Model and Data Traceability | High | Technical | D3, D4, D6 |
| [TC-L01-005](#tc-l01-005) | Risk Tiering of Use Cases: Criteria and Consistency | Critical | Technical | D3, D7 |
| [TC-L01-006](#tc-l01-006) | Screening for Prohibited or Restricted Use Cases | Critical | Technical | D3, D7 |
| [TC-L01-007](#tc-l01-007) | Intended Purpose Documentation and Purpose-Drift Detection | High | Technical | D3, D6 |
| [TC-L01-008](#tc-l01-008) | Reconciliation of Discovered AI Use Against the Registry | Critical | Technical | D1, D3 |
| [TC-L01-009](#tc-l01-009) | Business Impact and Criticality Classification | Medium | Technical | D3, D7 |
| [TC-L01-010](#tc-l01-010) | Impacted Persons and Stakeholder Identification | High | Technical | D3, D7 |
| [TC-L01-011](#tc-l01-011) | Identification of Automated Decisions and Profiling | Critical | Technical | D3, D6, D7 |
| [TC-L01-012](#tc-l01-012) | Human Oversight Design Recorded and Tested | Critical | Evidence | D3, D5 |
| [TC-L01-013](#tc-l01-013) | Use-Case Lifecycle States and Required Controls per State | Medium | Technical | D3 |
| [TC-L01-014](#tc-l01-014) | Pilot and Proof-of-Concept Guardrails | High | Technical | D3, D6 |
| [TC-L01-015](#tc-l01-015) | Material Change Triggers Re-Assessment | High | Technical | D3, D4 |
| [TC-L01-016](#tc-l01-016) | Benefit, Risk and KPI Tracking per Use Case | Low | Evidence | D3 |
| [TC-L01-017](#tc-l01-017) | Third-Party AI Dependency Recording per Use Case | High | Technical | D3, D4 |
| [TC-L01-018](#tc-l01-018) | Fallback and Continuity Plans for AI-Dependent Processes | Medium | Evidence | D3, D7 |
| [TC-L01-019](#tc-l01-019) | Use-Case Retirement and Decommission Evidence | Medium | Evidence | D3, D7 |
| [TC-L01-020](#tc-l01-020) | Portfolio View and Executive Reporting on Use Cases | Medium | Evidence | D3, D7 |

---

## Test cases

<a id="tc-l01-001"></a>

### TC-L01-001: AI Use-Case Registry: Creation, Mandatory Fields and Uniqueness

| Field | Value |
|---|---|
| **Lifecycle Layer** | L01 Business & Use Cases |
| **Use-Case Domain(s)** | D3, D7 |
| **Control Theme** | INV: Inventory and classification |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MAP (context and inventory of AI systems) |

**Risk Addressed.** An organisation cannot govern or report on AI it has not recorded, and registries with optional fields fill with incomplete entries.

**Business Scenario.** Governance wants every AI use case recorded with a minimum set of fields before work proceeds.

**Technical Scenario.** Create use cases in the platform's registry with complete, incomplete and duplicate entries and test enforcement of mandatory fields.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 12 fabricated use cases: 6 complete, 3 missing one mandatory field each, 2 near-duplicates of existing entries, 1 with special characters and a very long description; mandatory field list agreed in advance (name, purpose, business owner, data used, model or service, users affected, risk tier, status, review date).

**Procedure**

1. Agree and record the mandatory field list.
2. Attempt to create each of the 12 entries.
3. Record acceptance, rejection and the messages shown.
4. Check duplicate detection and merge handling.
5. Edit a record and check version history.
6. Attempt to delete a record and check retention of history.
7. Export the registry and check field completeness and format.

**Edge Cases / Variants.** Bulk import of 500 entries; entries created by an integration account.

**Expected Result.** All incomplete entries rejected or marked incomplete with clear messages; duplicates flagged; version history kept; deletion preserves an audit record; export contains every field.

**Expected Control Action.** Block incomplete submission.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Registry exportable to GRC or asset tools.

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

**Evidence to Capture.** Registry export; rejection messages; version history.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l01-002"></a>

### TC-L01-002: Use-Case Intake and Approval Workflow Before Deployment

| Field | Value |
|---|---|
| **Lifecycle Layer** | L01 Business & Use Cases |
| **Use-Case Domain(s)** | D3, D7 |
| **Control Theme** | GOV: Governance and accountability |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN (policies, accountability and oversight) |

**Risk Addressed.** Deployment ahead of approval is the most common way unreviewed AI reaches production.

**Business Scenario.** Governance wants a documented intake route in which defined approvers decide before any production use.

**Technical Scenario.** Submit use cases of different risk and test routing, approval, rejection and the link to technical enforcement.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 6 use cases (2 low, 2 medium, 2 high risk); approver roles defined for each tier; one use case submitted with a request for emergency approval.

**Procedure**

1. Configure routes and approvers by tier.
2. Submit the six use cases.
3. Check routing and notifications.
4. Approve two, reject one, request changes on one.
5. Attempt to mark a rejected use case as live.
6. Check whether production controls (for example access to the application or model) depend on approval status.
7. Test the emergency route and its after-the-fact review.

**Edge Cases / Variants.** Approver absent; approval requested by the approver's own team.

**Expected Result.** Each use case routed to the correct approvers; rejected use case cannot go live; production access linked to status or the gap documented; emergency route time-limited and reviewed.

**Expected Control Action.** Gate.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Status feeds access policy where integrated.

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

**Evidence to Capture.** Workflow audit trail; status-to-access test.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l01-003"></a>

### TC-L01-003: Business Owner and Accountable Executive Attribution

| Field | Value |
|---|---|
| **Lifecycle Layer** | L01 Business & Use Cases |
| **Use-Case Domain(s)** | D3 |
| **Control Theme** | GOV: Governance and accountability |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN (policies, accountability and oversight) |

**Risk Addressed.** Systems without a named owner are not maintained, reviewed or switched off.

**Business Scenario.** Governance wants a named business owner and accountable executive on every use case, kept current.

**Technical Scenario.** Test owner assignment, validation against the directory and handling of leavers and role changes.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 10 use cases with owners; directory with 3 leavers and 2 role changes among them; 2 use cases with a shared mailbox as owner.

**Procedure**

1. Assign owners from the directory.
2. Attempt to assign a shared mailbox or non-existent person.
3. Mark owners as leavers in the directory.
4. Check detection and notifications.
5. Check reassignment workflow and its deadline.
6. Report ownerless use cases.
7. Check ownership history.

**Edge Cases / Variants.** Owner on long leave; use case transferred between departments.

**Expected Result.** Invalid owners rejected; leaver detected within the stated time; reassignment tracked to closure; history retained.

**Expected Control Action.** Alert and escalate.

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

**Evidence to Capture.** Owner report; history.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l01-004"></a>

### TC-L01-004: Use-Case to System, Model and Data Traceability

| Field | Value |
|---|---|
| **Lifecycle Layer** | L01 Business & Use Cases |
| **Use-Case Domain(s)** | D3, D4, D6 |
| **Control Theme** | INV: Inventory and classification |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MAP (context and inventory of AI systems) |

**Risk Addressed.** Risk assessment is weak when no one can say which models, datasets and services a use case relies on.

**Business Scenario.** Governance wants a traceable chain from a use case to its components.

**Technical Scenario.** Link five use cases to models, datasets, services and users and test navigation both ways.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 5 use cases; 8 models and services; 6 datasets; 40 links; 2 deliberately orphaned components.

**Procedure**

1. Create the links.
2. Navigate from a use case to its components and back.
3. Change a component and check which use cases are affected.
4. Detect orphaned components.
5. Export the dependency view.
6. Check how links are kept current when systems change.

**Edge Cases / Variants.** Component shared by many use cases; component replaced.

**Expected Result.** Navigation complete in both directions; impact of a component change listed; orphans reported; export available.

**Expected Control Action.** N/A.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Links fed by discovery where available.

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

**Evidence to Capture.** Dependency export; impact report.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l01-005"></a>

### TC-L01-005: Risk Tiering of Use Cases: Criteria and Consistency

| Field | Value |
|---|---|
| **Lifecycle Layer** | L01 Business & Use Cases |
| **Use-Case Domain(s)** | D3, D7 |
| **Control Theme** | RSK: Risk management |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MAP and MANAGE (risk identification and treatment) |

**Risk Addressed.** Tiering that depends on who completes it produces uneven control and unreliable reporting.

**Business Scenario.** Governance wants a defined tiering method that two assessors apply consistently.

**Technical Scenario.** Have two assessors tier the same use cases independently and compare results and rationale capture.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 10 fabricated use cases covering internal productivity, customer-facing assistance, employee screening, credit-style decisioning, code generation, medical-style triage, marketing content, monitoring of staff, translation, and safety-related operations; criteria documented (impact, data sensitivity, autonomy, scale, affected persons).

**Procedure**

1. Record the tiering method and criteria.
2. Assessor A tiers the ten use cases.
3. Assessor B tiers independently.
4. Compare tiers and rationale.
5. Check how the platform records rationale.
6. Change a criterion answer and check recalculation and approvals.
7. Check handling of overrides.

**Edge Cases / Variants.** Use case with mixed purposes; tier changed after deployment.

**Expected Result.** At least 8 of 10 tiers agree between assessors; rationale recorded for every tier; overrides require justification and approval.

**Expected Control Action.** Gate on tier.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Tier feeds control requirements.

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

**Evidence to Capture.** Tiering comparison table.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l01-006"></a>

### TC-L01-006: Screening for Prohibited or Restricted Use Cases

| Field | Value |
|---|---|
| **Lifecycle Layer** | L01 Business & Use Cases |
| **Use-Case Domain(s)** | D3, D7 |
| **Control Theme** | GOV: Governance and accountability |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN (policies, accountability and oversight) |

**Risk Addressed.** Some uses are barred by law, policy or contract and must not reach the build stage.

**Business Scenario.** Governance wants intake questions to catch prohibited and restricted uses early.

**Technical Scenario.** Submit use cases that touch policy-defined restricted categories and test screening.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 8 use cases: 3 clearly in a restricted category defined by the organisation's policy, 2 borderline, 3 acceptable; restricted list entered into the platform (examples: workplace emotion inference, biometric identification, social scoring-style ranking, if the adopted framework or policy restricts them).

**Procedure**

1. Enter the restricted list from the organisation's policy.
2. Submit the 8 use cases.
3. Record screening results.
4. Check escalation for borderline cases.
5. Check that restricted use cases cannot be approved at the normal level.
6. Check audit of any override.

**Edge Cases / Variants.** Use case described in euphemistic terms; use case split to avoid a restriction.

**Expected Result.** All clearly restricted use cases blocked or escalated to the defined authority; borderline cases escalated; acceptable ones pass; overrides audited.

**Expected Control Action.** Block or escalate.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Restricted list maintained centrally.

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

**Evidence to Capture.** Screening results.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l01-007"></a>

### TC-L01-007: Intended Purpose Documentation and Purpose-Drift Detection

| Field | Value |
|---|---|
| **Lifecycle Layer** | L01 Business & Use Cases |
| **Use-Case Domain(s)** | D3, D6 |
| **Control Theme** | PRV: Privacy and data protection principles |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P, A |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MAP and MEASURE (privacy risk examined and managed) |

**Risk Addressed.** Systems drift from their documented purpose, undermining the privacy, risk and legal assumptions made at approval, and purpose limitation is a principle in most data protection frameworks.

**Business Scenario.** Governance wants each use case's intended purpose recorded and departures from it detected and reviewed.

**Technical Scenario.** Record purposes and expected data and user groups for four use cases, then generate usage that departs from them in four ways.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 4 use cases with recorded purposes, expected data categories and expected user groups; usage logs: in-purpose use (control), new user group, new data category, new downstream destination, new geography; 30 days of simulated activity.

**Procedure**

1. Record the purpose, data categories and user groups for each use case.
2. Generate in-purpose usage and confirm no alerts.
3. Introduce each departure one at a time.
4. Record whether and when the platform detects and notifies the owner.
5. Check what the review workflow requires (justify, re-assess, stop).
6. Check evidence of resolution.
7. Check how gradual widening over several weeks is handled.

**Edge Cases / Variants.** Purpose recorded in broad terms such as 'business improvement'; usage widening by 5 percent a week.

**Expected Result.** All 4 departures detected within the stated time and routed to the owner; in-purpose usage produces no alerts; review closed with a recorded decision; gradual widening detected or the limitation documented.

**Expected Control Action.** Alert and require review.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Alerts to owner and GRC tool.

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

**Evidence to Capture.** Detection table; review records.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l01-008"></a>

### TC-L01-008: Reconciliation of Discovered AI Use Against the Registry

| Field | Value |
|---|---|
| **Lifecycle Layer** | L01 Business & Use Cases |
| **Use-Case Domain(s)** | D1, D3 |
| **Control Theme** | INV: Inventory and classification |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, W |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MAP (context and inventory of AI systems) |

**Risk Addressed.** The registry is only as good as its completeness; unregistered use is the real exposure.

**Business Scenario.** Governance wants discovery results reconciled with registered use cases on a schedule.

**Technical Scenario.** Run discovery on a lab environment containing registered and unregistered AI use and compare.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 10 registered use cases; 6 unregistered uses (public tool, scheduled script calling a model API, SaaS AI feature, browser plugin, notebook model, low-code agent); 2 registered use cases with no remaining activity.

**Procedure**

1. Load the registry.
2. Run discovery.
3. Compare registry and discovery.
4. Check the unregistered list for attributes (user, department, data, destination).
5. Convert two unregistered items into registry entries from the finding and check attribute carry-over.
6. Check reporting of registered but inactive entries.
7. Configure recurring reconciliation and owner notification.

**Edge Cases / Variants.** Unregistered use by a contractor; use hidden inside an approved SaaS product.

**Expected Result.** All 6 unregistered uses found; inactive entries reported; conversion keeps discovery attributes; recurring reconciliation and notification configured.

**Expected Control Action.** Alert owners.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Findings feed the registry.

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

**Evidence to Capture.** Reconciliation report.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l01-009"></a>

### TC-L01-009: Business Impact and Criticality Classification

| Field | Value |
|---|---|
| **Lifecycle Layer** | L01 Business & Use Cases |
| **Use-Case Domain(s)** | D3, D7 |
| **Control Theme** | BCP: Resilience and continuity |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MANAGE (response and recovery) |

**Risk Addressed.** Treating every AI service as equally critical misallocates resilience effort and obscures what must be restored first.

**Business Scenario.** Operations wants criticality tied to business processes and recovery targets.

**Technical Scenario.** Classify use cases by impact and link them to processes and recovery objectives.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 6 use cases linked to 4 business processes; recovery time and data-loss targets defined per process; 1 use case supporting 2 processes with different targets.

**Procedure**

1. Record processes and targets.
2. Link use cases to processes.
3. Assign criticality.
4. Check target inheritance, including the dual-process case.
5. Change a process target and check propagation.
6. Report use cases with no recovery target.
7. Export the view for continuity planning.

**Edge Cases / Variants.** Process retired; use case supporting a process owned by a different division.

**Expected Result.** Targets inherited and visible; the stricter target applies in the dual-process case; changes propagate; gaps reported.

**Expected Control Action.** N/A.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Process data from the continuity tool.

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

**Evidence to Capture.** Criticality report.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l01-010"></a>

### TC-L01-010: Impacted Persons and Stakeholder Identification

| Field | Value |
|---|---|
| **Lifecycle Layer** | L01 Business & Use Cases |
| **Use-Case Domain(s)** | D3, D7 |
| **Control Theme** | OVS: Human oversight and transparency |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN and MANAGE (human oversight, transparency) |

**Risk Addressed.** Harm to affected people is easy to miss when the assessment lists only the users of the system.

**Business Scenario.** Governance wants people affected by AI outputs identified and reflected in the risk tier.

**Technical Scenario.** Complete stakeholder sections for five use cases with different affected groups and check prompts, flags and consequences.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 5 use cases: customer service assistant, applicant screening support, employee monitoring analytics, patient-style triage assistant, public information chatbot; fabricated stakeholder descriptions including vulnerable groups.

**Procedure**

1. Complete the stakeholder section for each.
2. Check prompts for groups affected beyond direct users.
3. Check how vulnerable groups (minors, patients, applicants, employees) are flagged.
4. Check the effect on tier and required controls.
5. Check whether consultation or notification requirements are recorded.
6. Export the completed sections.

**Edge Cases / Variants.** Indirectly affected third parties; groups affected only in rare edge cases.

**Expected Result.** Prompts cover affected persons beyond users; vulnerable groups flagged; tier raised or escalated where defined; export complete.

**Expected Control Action.** Escalate.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Export to assessments.

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

**Evidence to Capture.** Completed sections.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l01-011"></a>

### TC-L01-011: Identification of Automated Decisions and Profiling

| Field | Value |
|---|---|
| **Lifecycle Layer** | L01 Business & Use Cases |
| **Use-Case Domain(s)** | D3, D6, D7 |
| **Control Theme** | OVS: Human oversight and transparency |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, A |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN and MANAGE (human oversight, transparency) |

**Risk Addressed.** Many frameworks give individuals rights and require safeguards when decisions about them are automated or based on profiling.

**Business Scenario.** Governance wants decisions affecting individuals identified, flagged and tied to rights handling.

**Technical Scenario.** Register use cases with and without decisions about people and test flags and downstream requirements.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 8 use cases: 3 fully automated decisions with legal or similar effect on individuals, 2 human-reviewed recommendations, 1 routine human decision with AI summary, 2 with no individual decisions.

**Procedure**

1. Complete screening questions for each.
2. Check flags.
3. Check that flagged use cases require additional assessment and an oversight design.
4. Check links to rights handling (explanation, objection, human review).
5. Check registers and reports.
6. Test a case where a human review step is only nominal and see how the platform asks about it.

**Edge Cases / Variants.** Decision support routinely accepted without review; decision made in bulk overnight.

**Expected Result.** All 3 automated cases flagged; additional requirements triggered; rights links created; nominal human review challenged by the questions; reports list flagged cases.

**Expected Control Action.** Gate.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Link to rights workflow.

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

**Evidence to Capture.** Flag report.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l01-012"></a>

### TC-L01-012: Human Oversight Design Recorded and Tested

| Field | Value |
|---|---|
| **Lifecycle Layer** | L01 Business & Use Cases |
| **Use-Case Domain(s)** | D3, D5 |
| **Control Theme** | OVS: Human oversight and transparency |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: W, A |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN and MANAGE (human oversight, transparency) |

**Risk Addressed.** Oversight that exists only on paper fails when it is needed.

**Business Scenario.** Governance wants oversight roles, authority and intervention points defined and exercised.

**Technical Scenario.** Review oversight records for four use cases and test an intervention in the lab.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 4 use cases with oversight descriptions; 1 live intervention test (stop, override or escalate); named overseers with training records.

**Procedure**

1. Review records for roles, authority, training, intervention method and escalation.
2. Check that overseers have the access and information needed to intervene.
3. Test an intervention for one use case and time it.
4. Check logs of the intervention.
5. Check overseer workload assumptions (volume per person).
6. Record gaps and owners.

**Edge Cases / Variants.** Overseer unavailable; intervention needed outside business hours.

**Expected Result.** Overseers named with authority and training; intervention works and is logged within the target time; workload realistic; gaps recorded.

**Expected Control Action.** N/A.

**Expected Record / Log.** Configuration state, record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Logs.

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

**Evidence to Capture.** Test record; workload analysis.

**Reviewer Notes.** Confirm the evidence is taken from the live product. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l01-013"></a>

### TC-L01-013: Use-Case Lifecycle States and Required Controls per State

| Field | Value |
|---|---|
| **Lifecycle Layer** | L01 Business & Use Cases |
| **Use-Case Domain(s)** | D3 |
| **Control Theme** | CHG: Change and lifecycle management |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MANAGE and GOVERN (change and decommissioning) |

**Risk Addressed.** Controls required in production are skipped in pilot, and pilots become production silently.

**Business Scenario.** Governance wants lifecycle states defined with controls required at each.

**Technical Scenario.** Move use cases through states and check gates, skipping and time limits.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 3 use cases; states proposed, pilot, production, suspended, retired; control checklist per state (for example assessment complete, owner assigned, monitoring on, rollback tested).

**Procedure**

1. Define states and required controls.
2. Move the first use case forward through every state.
3. Check gates at each transition.
4. Attempt to skip a state.
5. Check pilot time limits and alerts.
6. Suspend a live use case and check effect on access.
7. Check the audit trail of transitions.

**Edge Cases / Variants.** Pilot extended repeatedly; emergency move to production.

**Expected Result.** Gates enforced; skipping blocked; pilot expiry alerts raised; suspension affects access or the gap is documented; transitions audited.

**Expected Control Action.** Gate.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Status to access policy.

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

**Evidence to Capture.** State history.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l01-014"></a>

### TC-L01-014: Pilot and Proof-of-Concept Guardrails

| Field | Value |
|---|---|
| **Lifecycle Layer** | L01 Business & Use Cases |
| **Use-Case Domain(s)** | D3, D6 |
| **Control Theme** | GOV: Governance and accountability |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN (policies, accountability and oversight) |

**Risk Addressed.** Pilots use real data and open access because they are treated as informal.

**Business Scenario.** Governance wants minimum guardrails for pilots enforced.

**Technical Scenario.** Run two pilots, one with guardrails configured and one without, and attempt out-of-guardrail actions.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 2 pilots; guardrails: approved or synthetic data only, user cap of 20, 90-day limit, no external sharing, mandatory logging; attempts: add 50 users, load a dataset labelled confidential, share a link externally, continue past 90 days.

**Procedure**

1. Define guardrails.
2. Start both pilots.
3. Attempt each out-of-guardrail action in both.
4. Record blocking or alerting.
5. Check expiry behaviour.
6. Check extension approval.
7. Check reporting of pilots near expiry.

**Edge Cases / Variants.** Pilot converted to production without assessment.

**Expected Result.** All attempts blocked or alerted in the guarded pilot; expiry enforced; extension requires approval; near-expiry report produced.

**Expected Control Action.** Block.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Alerts to owner.

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

<a id="tc-l01-015"></a>

### TC-L01-015: Material Change Triggers Re-Assessment

| Field | Value |
|---|---|
| **Lifecycle Layer** | L01 Business & Use Cases |
| **Use-Case Domain(s)** | D3, D4 |
| **Control Theme** | CHG: Change and lifecycle management |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MANAGE and GOVERN (change and decommissioning) |

**Risk Addressed.** Approvals granted once become stale as models, data and users change.

**Business Scenario.** Governance wants material changes to trigger review automatically.

**Technical Scenario.** Change attributes of an approved use case and check which changes trigger review.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 1 approved use case with 5 changes: model version, new data source, new user group, new region, new tool; 3 minor changes (wording, owner phone, report layout).

**Procedure**

1. Define triggers and thresholds.
2. Apply the five material changes.
3. Apply the three minor changes.
4. Check triggers, status changes and notifications.
5. Check effect on production access.
6. Complete re-assessment and re-approve.
7. Check how combined small changes are handled.

**Edge Cases / Variants.** Several minor changes adding up to a material one.

**Expected Result.** All 5 material changes trigger review and none of the minor ones; status shows pending review; approvals recorded; combined small changes detected or limit documented.

**Expected Control Action.** Hold or restrict.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Change events from discovery.

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

<a id="tc-l01-016"></a>

### TC-L01-016: Benefit, Risk and KPI Tracking per Use Case

| Field | Value |
|---|---|
| **Lifecycle Layer** | L01 Business & Use Cases |
| **Use-Case Domain(s)** | D3 |
| **Control Theme** | RSK: Risk management |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Low |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MAP and MANAGE (risk identification and treatment) |

**Risk Addressed.** Without measured value and incident data, use cases persist because nobody asks whether they are worth the risk.

**Business Scenario.** Governance wants benefit measured alongside risk indicators.

**Technical Scenario.** Record KPIs and risk indicators for four use cases and review the dashboards.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 4 use cases with 6 months of simulated KPIs (time saved, error rate, adoption) and incident counts; 1 use case with high risk and low value.

**Procedure**

1. Enter KPIs and link risk indicators.
2. Review the dashboards.
3. Identify the low-value, high-risk case.
4. Check review triggers and thresholds.
5. Check export.
6. Check whether KPIs can be fed automatically.

**Edge Cases / Variants.** KPIs not available for a new use case.

**Expected Result.** Dashboards show benefit and risk together; the flagged case is surfaced; review triggered.

**Expected Control Action.** N/A.

**Expected Record / Log.** Configuration state, record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Data from BI tools.

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

**Evidence to Capture.** Dashboard screenshot.

**Reviewer Notes.** Confirm the evidence is taken from the live product. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l01-017"></a>

### TC-L01-017: Third-Party AI Dependency Recording per Use Case

| Field | Value |
|---|---|
| **Lifecycle Layer** | L01 Business & Use Cases |
| **Use-Case Domain(s)** | D3, D4 |
| **Control Theme** | VND: Third-party and supplier management |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN and MAP (third-party and supply chain risk) |

**Risk Addressed.** A use case that depends on an external model or service inherits that provider's risk, location and contract terms.

**Business Scenario.** Governance wants dependencies recorded and linked to provider assessments.

**Technical Scenario.** Link five use cases to four providers and test the provider-centred view.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 5 use cases; 4 providers (model provider, SaaS vendor, hosting provider, data supplier), 2 shared across use cases; 1 provider flagged high risk during the test.

**Procedure**

1. Record the dependencies.
2. Open the provider-centred view.
3. Mark one provider as high risk.
4. Check the list of affected use cases and notifications to owners.
5. Check how provider sub-processors are recorded.
6. Export the dependency map.

**Edge Cases / Variants.** Provider acquired by another company; provider changes region.

**Expected Result.** Affected use cases listed instantly; owners notified; sub-processors recorded; map exportable.

**Expected Control Action.** N/A.

**Expected Record / Log.** Record with timestamp, actor, record identifier, decision, before and after values and approval reference, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Link to the vendor register.

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

**Evidence to Capture.** Provider impact view.

**Reviewer Notes.** Confirm evidence comes from the live PoC tenant, not vendor-supplied demo data. Record the product version tested and any manual steps needed.

[Back to layer index](#top)

---

<a id="tc-l01-018"></a>

### TC-L01-018: Fallback and Continuity Plans for AI-Dependent Processes

| Field | Value |
|---|---|
| **Lifecycle Layer** | L01 Business & Use Cases |
| **Use-Case Domain(s)** | D3, D7 |
| **Control Theme** | BCP: Resilience and continuity |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MANAGE (response and recovery) |

**Risk Addressed.** Processes that depend on AI need a manual or alternative path when it fails, and it must work.

**Business Scenario.** Operations wants fallback plans recorded and tested.

**Technical Scenario.** Review recorded plans and execute one fallback in the lab.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 3 use cases with fallback plans; 1 simulated outage of the AI service; recovery targets from the business impact record.

**Procedure**

1. Review plans for steps, owners, triggers and targets.
2. Check that plans are linked to the use case record.
3. Simulate the outage.
4. Execute the fallback.
5. Record time to switch and issues.
6. Check review dates.
7. Record corrective actions.

**Edge Cases / Variants.** Fallback depending on staff who are on leave; outage at month end.

**Expected Result.** Plan executed within the target; issues recorded and tracked; reviews current.

**Expected Control Action.** N/A.

**Expected Record / Log.** Configuration state, record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Record or report visible in the governance and compliance workspace within the documented refresh interval.

**Expected Integration Evidence.** Exercise record.

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

**Evidence to Capture.** Exercise notes; timeline.

**Reviewer Notes.** Confirm the evidence is taken from the live product. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l01-019"></a>

### TC-L01-019: Use-Case Retirement and Decommission Evidence

| Field | Value |
|---|---|
| **Lifecycle Layer** | L01 Business & Use Cases |
| **Use-Case Domain(s)** | D3, D7 |
| **Control Theme** | CHG: Change and lifecycle management |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | MANAGE and GOVERN (change and decommissioning) |

**Risk Addressed.** Retired systems keep data, access and cost, and lapses are discovered only during incidents.

**Business Scenario.** Governance wants retirement to remove everything and produce proof.

**Technical Scenario.** Retire two use cases and verify each closure step in the lab.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 2 use cases with models, datasets, accounts, keys, integrations, user notices and logs; retention duties on one dataset.

**Procedure**

1. Start retirement for both.
2. Work through the checklist: access, data, models, keys, integrations, notices, monitoring.
3. Verify each item in the lab environment.
4. Check handling of data that must be retained.
5. Produce closure evidence.
6. Attempt to reactivate a retired use case and check approval requirements.

**Edge Cases / Variants.** Use case referenced by other systems; retention duty conflicting with deletion.

**Expected Result.** All checklist items verified; retained data handled under a stated rule; reactivation requires approval; closure evidence complete.

**Expected Control Action.** Checklist.

**Expected Record / Log.** Configuration state, record or export that supports the claim, with timestamp and the identity of the person who produced it.

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

**Scoring Criteria.** 0 = not demonstrated; 3 = partly shown or shown only from documentation; 5 = shown in the live product with exportable evidence; N/A = capability out of scope by design.

**Pass Criteria.** Expected Result and Expected Control Action are met in full against the requirement recorded in Applicable Requirement, within the vendor's documented SLA, and the evidence under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Expected Result is not met; evidence is missing or not from the live product; the control action does not occur where required; or the applicable requirement and its parameters were not recorded before testing.

**Evidence to Capture.** Closure record.

**Reviewer Notes.** Confirm the evidence is taken from the live product. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l01-020"></a>

### TC-L01-020: Portfolio View and Executive Reporting on Use Cases

| Field | Value |
|---|---|
| **Lifecycle Layer** | L01 Business & Use Cases |
| **Use-Case Domain(s)** | D3, D7 |
| **Control Theme** | GOV: Governance and accountability |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **NIST AI RMF Mapping** | GOVERN (policies, accountability and oversight) |

**Risk Addressed.** Leaders lack a view of how much AI is in use and at what risk.

**Business Scenario.** Leadership wants a portfolio summary that is accurate and explainable.

**Technical Scenario.** Load 30 fabricated use cases and check the reports against known totals.

**Preconditions.** Isolated PoC tenant provisioned; fabricated use cases, policies, records and individuals seeded per [Appendix D](appendix-d-lab-prerequisites.md); test users in the roles named in the case; platform connected to the lab directory with least-privilege test credentials. Written evidence request issued to the vendor before the PoC; sample use cases, policies, registers and records are fabricated; the assessor has copied the applicable requirement text and any numeric parameters (timelines, retention periods, thresholds) from the adopted framework into the Applicable Requirement field before testing.

**Applicable Requirement *(assessor to complete)***

- Framework and clause: `________`
- Requirement text: `________`
- Parameters (timelines, periods, thresholds): `________`

**Test Data.** 30 use cases across 4 tiers, 6 departments and 5 states; calculation sheet.

**Procedure**

1. Load the data.
2. Compare portfolio counts to the calculation sheet.
3. Check drill-down.
4. Check filters by tier, department and state.
5. Schedule a monthly report.
6. Check access control on reports.

**Edge Cases / Variants.** Use cases tagged to several departments.

**Expected Result.** Counts match exactly; drill-down works; schedule and access control work.

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

**Evidence to Capture.** Report sample.

**Reviewer Notes.** Confirm the evidence is taken from the live product. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

