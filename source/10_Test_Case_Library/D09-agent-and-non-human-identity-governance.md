---
title: "D09 Agent and Non-Human Identity Governance"
author: Nachiket Sathaye
parent: "Test Case Library"
nav_order: 22
---

<a id="top"></a>

# D09 Agent and Non-Human Identity Governance

**Focus:** agent and non-human identity governance: registry, sponsors, recertification, drift, delegation, revocation

**Controls tested:** [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity (14 cases), [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) Least Privilege and Scoped Credentials (6 cases), [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006) Agent Governance (1 case), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) Auditability (1 case), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) Third-Party and Vendor AI Assurance (1 case), [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022) Deterministic Action Authorization (1 case), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) Agent Containment and Kill Switch (1 case), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) AI Incident Response and Forensics (1 case), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) Control Assurance and Audit Evidence (1 case)

**Cases:** 20 (TC-D09-001 to TC-D09-020)  |  **Series:** Emerging domains

> **Safety boundary.** All cases use synthetic data and lab targets only. Use fabricated identities, lab directories and mock cloud and SaaS tenants only.

> **How this relates to the layer cases.** Domain cases cross-reference the layer cases they build on (see **Related Layer Cases** in each case). The layer case tests the platform control; the domain case tests the buyer concern from the domain's own point of view. Verify all ATLAS, OWASP and NIST identifiers before use, and treat numeric thresholds as starting values.

## Cases in this domain

| ID | Title | Severity | Method | Controls |
|---|---|---|---|---|
| [TC-D09-001](#tc-d09-001) | Agent Identity Registry as System of Record | Critical | Technical | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) |
| [TC-D09-002](#tc-d09-002) | Human Sponsor Accountability for Every Agent Identity | Critical | Technical | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) |
| [TC-D09-003](#tc-d09-003) | Agent Identity Provisioning Workflow and Approval | High | Technical | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) |
| [TC-D09-004](#tc-d09-004) | Agent Identity Risk Tiering and Privilege Classes | High | Technical | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) |
| [TC-D09-005](#tc-d09-005) | Entitlement Governance: Agent Access Requests and Least-Privilege Catalogue | High | Technical | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) |
| [TC-D09-006](#tc-d09-006) | Periodic Access Recertification for Agent Entitlements | High | Technical | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) |
| [TC-D09-007](#tc-d09-007) | Privilege Drift Detection Against an Approved Baseline | High | Technical | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) |
| [TC-D09-008](#tc-d09-008) | Dormant and Orphaned Agent Identity Clean-Up | Medium | Technical | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) |
| [TC-D09-009](#tc-d09-009) | Time-Bound and Just-in-Time Elevation for Agents | High | Technical | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) |
| [TC-D09-010](#tc-d09-010) | Separation of Duties for Agents | High | Technical | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016), [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022) |
| [TC-D09-011](#tc-d09-011) | Delegation Records and Consent Evidence | High | Evidence | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) |
| [TC-D09-012](#tc-d09-012) | Acting as the User versus Acting as Itself: Attribution Policy and Evidence | High | Technical | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) |
| [TC-D09-013](#tc-d09-013) | Cross-Platform Agent Identity Federation and Consistency | High | Technical | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) |
| [TC-D09-014](#tc-d09-014) | Agent Credential Lifecycle Governance and Compliance Reporting | High | Technical | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) |
| [TC-D09-015](#tc-d09-015) | Machine Identity Certificate and Key Lifecycle for AI Workloads | Medium | Technical | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) |
| [TC-D09-016](#tc-d09-016) | Revocation Propagation Time Across Systems | Critical | Technical | [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025), [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) |
| [TC-D09-017](#tc-d09-017) | Agent Identity Misuse Case Handling Process | High | Technical | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035), [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) |
| [TC-D09-018](#tc-d09-018) | Third-Party and Vendor-Operated Agent Identities | High | Evidence | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) |
| [TC-D09-019](#tc-d09-019) | Non-Human Identity Governance Metrics and Audit Evidence | Medium | Evidence | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038), [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) |
| [TC-D09-020](#tc-d09-020) | Agent Identity Offboarding and Decommission Evidence | Medium | Evidence | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015), [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006) |

---

## Test cases

<a id="tc-d09-001"></a>

### TC-D09-001: Agent Identity Registry as System of Record

| Field | Value |
|---|---|
| **Use-Case Domain** | D09: Agent and Non-Human Identity Governance |
| **Lifecycle Layer(s)** | L09, L06, L02 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, W |
| **Risk Severity** | Critical |
| **Related Layer Cases** | [TC-L09-001](L09-identity-and-access-mgmt.md#tc-l09-001), [TC-L06-002](L06-agent-orchestration-layer.md#tc-l06-002) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity |

**Risk Addressed.** Identities for agents live in the identity provider, cloud IAM, SaaS tenants and code repositories, with no single record of why each exists, who is accountable and what risk tier it carries.

**Business Scenario.** Identity governance wants a registry that is the system of record for agent and other non-human identities, reconciled against every source.

**Technical Scenario.** Create a known population of agent identities across four sources and test registry completeness, reconciliation and attributes.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, fabricated agent identities and entitlements, mock cloud and SaaS tenants, lab secret store and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider, lab agents with fabricated identities and entitlements, a mock cloud account and SaaS tenant, a lab secret store and a mock ticketing system; no production identities, credentials or directories are connected.

**Test Data.** 40 identities: 10 in the identity provider, 12 cloud roles and service principals, 10 SaaS app registrations and API tokens, 8 agent tokens created in an orchestration platform; attributes recorded in advance (purpose, sponsor, risk tier, environment, expiry); 6 identities created outside any process.

**Procedure**

1. Record the ground truth for all 40 identities.
2. Connect the registry to each source.
3. Run reconciliation.
4. Compare found identities and attributes.
5. Check the list of identities found in a source but not in the registry (the six).
6. Create a registry entry from one of them and check attribute carry-over.
7. Check scheduled reconciliation and drift reporting.

**Edge Cases / Variants.** Same agent using two identities; identity shared by an agent and a human.

**Expected Detection.** At least 38 of 40 identities found; purpose, sponsor and tier correct for at least 30; all 6 unmanaged identities reported; scheduled reconciliation configured.

**Expected Prevention / Control Action.** Alert on unmanaged identities.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or governance record visible in the identity governance view within the documented refresh interval.

**Expected Integration Evidence.** Registry export to GRC and identity tools.

**Forensic Evidence.** Identity, sponsor, entitlement, credential reference, request or decision, approver and timestamp exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Reconciliation report; ground-truth comparison.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d09-002"></a>

### TC-D09-002: Human Sponsor Accountability for Every Agent Identity

| Field | Value |
|---|---|
| **Use-Case Domain** | D09: Agent and Non-Human Identity Governance |
| **Lifecycle Layer(s)** | L09, L01 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | Critical |
| **Related Layer Cases** | [TC-L01-003](L01-business-and-use-cases.md#tc-l01-003) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity |

**Risk Addressed.** An agent with no accountable human is not reviewed, rotated or shut down.

**Business Scenario.** Governance wants every agent identity to have a named sponsor who answers for it.

**Technical Scenario.** Test sponsor assignment, validation and succession when sponsors leave or move.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, fabricated agent identities and entitlements, mock cloud and SaaS tenants, lab secret store and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider, lab agents with fabricated identities and entitlements, a mock cloud account and SaaS tenant, a lab secret store and a mock ticketing system; no production identities, credentials or directories are connected.

**Test Data.** 20 agents with sponsors; 3 sponsors who leave, 2 who change role, 1 on long leave; 2 agents with a shared mailbox as sponsor.

**Procedure**

1. Assign sponsors from the directory.
2. Attempt to assign a shared mailbox or a non-existent person.
3. Mark sponsors as leavers and movers in the directory.
4. Check detection time and notifications.
5. Check the succession workflow and its deadline.
6. Check what happens to agents whose sponsor does not respond in time (restrict, suspend).
7. Check sponsor history and attestation.

**Edge Cases / Variants.** Sponsor team disbanded; sponsor role held by a contractor.

**Expected Detection.** Invalid sponsors rejected; leaver detected within the stated time; succession tracked to closure; agents of non-responding sponsors restricted per policy; history retained.

**Expected Prevention / Control Action.** Restrict or suspend.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or governance record visible in the identity governance view within the documented refresh interval.

**Expected Integration Evidence.** Directory integration.

**Forensic Evidence.** Identity, sponsor, entitlement, credential reference, request or decision, approver and timestamp exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Sponsor history; succession records.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d09-003"></a>

### TC-D09-003: Agent Identity Provisioning Workflow and Approval

| Field | Value |
|---|---|
| **Use-Case Domain** | D09: Agent and Non-Human Identity Governance |
| **Lifecycle Layer(s)** | L06, L09 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L06-034](L06-agent-orchestration-layer.md#tc-l06-034) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity |

**Risk Addressed.** Agents created ad hoc get broad access and no review.

**Business Scenario.** Governance wants a request and approval route before an agent identity exists.

**Technical Scenario.** Request agent identities of different risk and test routing, approval, issuance and expiry.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, fabricated agent identities and entitlements, mock cloud and SaaS tenants, lab secret store and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider, lab agents with fabricated identities and entitlements, a mock cloud account and SaaS tenant, a lab secret store and a mock ticketing system; no production identities, credentials or directories are connected.

**Test Data.** 8 requests: 3 low-risk read-only, 3 medium with write access, 2 high with production or financial access; approvers by tier; 1 request with weak justification.

**Procedure**

1. Configure routes and approvers by tier.
2. Submit the eight requests.
3. Check routing, notifications and justification validation.
4. Approve, reject and request changes.
5. Check issuance is automated from approval and that no identity exists before approval.
6. Check default expiry and renewal rules.
7. Check an emergency route and its review.

**Edge Cases / Variants.** Request raised by the approver's own team; request for a copy of an existing agent.

**Expected Detection.** Routing by tier correct; no identity before approval; default expiry applied; emergency route time-limited and reviewed.

**Expected Prevention / Control Action.** Gate.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or governance record visible in the identity governance view within the documented refresh interval.

**Expected Integration Evidence.** Ticketing and IdP integration.

**Forensic Evidence.** Identity, sponsor, entitlement, credential reference, request or decision, approver and timestamp exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Request and approval trail.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d09-004"></a>

### TC-D09-004: Agent Identity Risk Tiering and Privilege Classes

| Field | Value |
|---|---|
| **Use-Case Domain** | D09: Agent and Non-Human Identity Governance |
| **Lifecycle Layer(s)** | L09, L01, L02 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L01-005](L01-business-and-use-cases.md#tc-l01-005) |
| **MITRE ATLAS Mapping** | N/A (governance control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MAP and MANAGE (risk identification and treatment) |
| **Control(s) Tested** | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity |

**Risk Addressed.** Treating all agent identities alike either strangles low-risk automation or under-controls dangerous agents.

**Business Scenario.** Governance wants tiers that drive control requirements such as expiry, approval and monitoring.

**Technical Scenario.** Tier a mixed population and check that tier drives required controls.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, fabricated agent identities and entitlements, mock cloud and SaaS tenants, lab secret store and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider, lab agents with fabricated identities and entitlements, a mock cloud account and SaaS tenant, a lab secret store and a mock ticketing system; no production identities, credentials or directories are connected.

**Test Data.** 15 agents across 3 tiers with different reach (internal read-only, internal write, external or financial); control requirements per tier (maximum credential lifetime, recertification interval, approval for changes, monitoring level).

**Procedure**

1. Define tier criteria and requirements.
2. Tier all 15 agents.
3. Compare with a reviewer's expected tiers.
4. Check that the platform flags agents that do not meet their tier's controls.
5. Raise one agent's reach and check automatic re-tiering.
6. Check override rules and audit.
7. Report non-compliance by tier.

**Edge Cases / Variants.** Agent whose reach is determined by a user at runtime.

**Expected Detection.** At least 13 of 15 tiers agree with the reviewer; non-compliant agents flagged; re-tiering on privilege change; overrides need justification.

**Expected Prevention / Control Action.** Gate on tier.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or governance record visible in the identity governance view within the documented refresh interval.

**Expected Integration Evidence.** Tier data to reporting.

**Forensic Evidence.** Identity, sponsor, entitlement, credential reference, request or decision, approver and timestamp exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Tier table; compliance report.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d09-005"></a>

### TC-D09-005: Entitlement Governance: Agent Access Requests and Least-Privilege Catalogue

| Field | Value |
|---|---|
| **Use-Case Domain** | D09: Agent and Non-Human Identity Governance |
| **Lifecycle Layer(s)** | L09, L06 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L09-004](L09-identity-and-access-mgmt.md#tc-l09-004) |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) Least Privilege and Scoped Credentials |

**Risk Addressed.** Agents receive whatever the developer asked for, usually the broadest role available.

**Business Scenario.** Identity governance wants agents to request named entitlements from a catalogue that supports least privilege.

**Technical Scenario.** Build a small catalogue and run agent access requests through approval.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, fabricated agent identities and entitlements, mock cloud and SaaS tenants, lab secret store and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider, lab agents with fabricated identities and entitlements, a mock cloud account and SaaS tenant, a lab secret store and a mock ticketing system; no production identities, credentials or directories are connected.

**Test Data.** 12 catalogue entitlements with risk ratings (read tickets, write tickets, read customer records, export data, send external email, and similar); 6 agent requests including 2 for wide roles; requests for bundle versus single entitlements.

**Procedure**

1. Define the catalogue and ratings.
2. Submit the requests.
3. Check whether the platform suggests narrower alternatives.
4. Approve and reject.
5. Check grant to the target system and evidence of the change.
6. Check removal when a request is withdrawn.
7. Check reports on entitlement concentration.

**Edge Cases / Variants.** Agent requesting access on behalf of a user group.

**Expected Detection.** Wide requests challenged; narrower options suggested; grants match approvals exactly; concentration report accurate.

**Expected Prevention / Control Action.** Gate.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or governance record visible in the identity governance view within the documented refresh interval.

**Expected Integration Evidence.** Grants applied through IdP or cloud IAM.

**Forensic Evidence.** Identity, sponsor, entitlement, credential reference, request or decision, approver and timestamp exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Request records; grant verification.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d09-006"></a>

### TC-D09-006: Periodic Access Recertification for Agent Entitlements

| Field | Value |
|---|---|
| **Use-Case Domain** | D09: Agent and Non-Human Identity Governance |
| **Lifecycle Layer(s)** | L09, L02, L12 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L09-021](L09-identity-and-access-mgmt.md#tc-l09-021), [TC-L12-030](L12-model-layer.md#tc-l12-030) |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) Least Privilege and Scoped Credentials |

**Risk Addressed.** Entitlements granted once remain forever unless someone reviews them.

**Business Scenario.** Audit wants agent entitlements recertified on a defined cycle with revocation on non-response.

**Technical Scenario.** Run a recertification campaign for 20 agents.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, fabricated agent identities and entitlements, mock cloud and SaaS tenants, lab secret store and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider, lab agents with fabricated identities and entitlements, a mock cloud account and SaaS tenant, a lab secret store and a mock ticketing system; no production identities, credentials or directories are connected.

**Test Data.** 20 agents with 80 entitlements; 12 stale, 8 excessive; 6 reviewers; 14-day window; 2 reviewers who do not respond; 1 reviewer who certifies everything.

**Procedure**

1. Create the campaign.
2. Send to reviewers with usage data.
3. Track responses and reminders.
4. Check escalation and auto-revoke for non-response.
5. Check detection of rubber-stamping (all approved quickly).
6. Check that revocations take effect in target systems.
7. Export the evidence.

**Edge Cases / Variants.** Reviewer who left during the campaign; entitlement used only once a year.

**Expected Detection.** Usage data shown to reviewers; non-response handled per policy; rubber-stamping flagged; revocations effective and evidenced.

**Expected Prevention / Control Action.** Revoke.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or governance record visible in the identity governance view within the documented refresh interval.

**Expected Integration Evidence.** Revocations applied to IdP or cloud IAM.

**Forensic Evidence.** Identity, sponsor, entitlement, credential reference, request or decision, approver and timestamp exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Campaign report; effect verification.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d09-007"></a>

### TC-D09-007: Privilege Drift Detection Against an Approved Baseline

| Field | Value |
|---|---|
| **Use-Case Domain** | D09: Agent and Non-Human Identity Governance |
| **Lifecycle Layer(s)** | L09 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L09-022](L09-identity-and-access-mgmt.md#tc-l09-022), [TC-L06-034](L06-agent-orchestration-layer.md#tc-l06-034) |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |
| **Control(s) Tested** | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) Least Privilege and Scoped Credentials |

**Risk Addressed.** Agents accumulate permissions through small changes that no one approves.

**Business Scenario.** Security wants differences between approved and actual privileges detected.

**Technical Scenario.** Record approved baselines and change real permissions.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, fabricated agent identities and entitlements, mock cloud and SaaS tenants, lab secret store and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider, lab agents with fabricated identities and entitlements, a mock cloud account and SaaS tenant, a lab secret store and a mock ticketing system; no production identities, credentials or directories are connected.

**Test Data.** 10 agents with approved baselines; 6 changes: added scope, new role, wider resource range, inherited group permission, token with extra audience, new trust relationship.

**Procedure**

1. Record the baselines.
2. Apply each change separately.
3. Check detection time and alert content.
4. Check whether the platform proposes revert or re-approval.
5. Check noise from legitimate approved changes.
6. Check reporting of drift over time.

**Edge Cases / Variants.** Drift introduced via infrastructure code; drift through group membership.

**Expected Detection.** At least 5 of 6 changes detected within the stated interval; approved changes not alerted; revert or re-approval offered.

**Expected Prevention / Control Action.** Alert or revert.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or governance record visible in the identity governance view within the documented refresh interval.

**Expected Integration Evidence.** Alerts to ticketing.

**Forensic Evidence.** Identity, sponsor, entitlement, credential reference, request or decision, approver and timestamp exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Drift table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d09-008"></a>

### TC-D09-008: Dormant and Orphaned Agent Identity Clean-Up

| Field | Value |
|---|---|
| **Use-Case Domain** | D09: Agent and Non-Human Identity Governance |
| **Lifecycle Layer(s)** | L09, L06, L13 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, W |
| **Risk Severity** | Medium |
| **Related Layer Cases** | [TC-L06-035](L06-agent-orchestration-layer.md#tc-l06-035), [TC-L13-026](L13-training-and-fine-tuning-layer.md#tc-l13-026) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity |

**Risk Addressed.** Unused identities remain valid targets for years.

**Business Scenario.** Governance wants dormant and ownerless identities found and retired with proof.

**Technical Scenario.** Create dormant and orphaned identities and run the clean-up workflow.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, fabricated agent identities and entitlements, mock cloud and SaaS tenants, lab secret store and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider, lab agents with fabricated identities and entitlements, a mock cloud account and SaaS tenant, a lab secret store and a mock ticketing system; no production identities, credentials or directories are connected.

**Test Data.** 15 identities: 5 dormant for 90 days (backdated), 4 with departed sponsor, 3 unused tokens, 3 active.

**Procedure**

1. Configure thresholds.
2. Run detection.
3. Check findings against ground truth.
4. Route to sponsors for decision.
5. Disable then delete after a hold period.
6. Verify removal in every source.
7. Report clean-up metrics.

**Edge Cases / Variants.** Identity used only for annual jobs; identity referenced by other systems.

**Expected Detection.** All 12 inactive or ownerless identities found; active ones not flagged; removal verified in every source.

**Expected Prevention / Control Action.** Disable then delete.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or governance record visible in the identity governance view within the documented refresh interval.

**Expected Integration Evidence.** Workflow via IdP and cloud IAM.

**Forensic Evidence.** Identity, sponsor, entitlement, credential reference, request or decision, approver and timestamp exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Clean-up log; removal proof.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d09-009"></a>

### TC-D09-009: Time-Bound and Just-in-Time Elevation for Agents

| Field | Value |
|---|---|
| **Use-Case Domain** | D09: Agent and Non-Human Identity Governance |
| **Lifecycle Layer(s)** | L09 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, G |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L09-013](L09-identity-and-access-mgmt.md#tc-l09-013) |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) Least Privilege and Scoped Credentials |

**Risk Addressed.** Standing high privilege on agents widens exposure for no benefit.

**Business Scenario.** Security wants agents to receive high access only for the task and time needed.

**Technical Scenario.** Configure JIT elevation and run tasks that need it.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, fabricated agent identities and entitlements, mock cloud and SaaS tenants, lab secret store and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider, lab agents with fabricated identities and entitlements, a mock cloud account and SaaS tenant, a lab secret store and a mock ticketing system; no production identities, credentials or directories are connected.

**Test Data.** 3 agents; 4 privileged tasks; elevation of 15 minutes; approver and automatic modes.

**Procedure**

1. Configure elevation rules.
2. Run each task.
3. Check request, approval and grant.
4. Check expiry and revocation.
5. Attempt privileged action after expiry.
6. Check logs tie elevation to the task.
7. Check failure behaviour when approval is slow.

**Edge Cases / Variants.** Task longer than the window; nested elevation.

**Expected Detection.** Privilege only during the window; expired access refused; logs complete; slow approval fails safely.

**Expected Prevention / Control Action.** Time-limited grant.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or governance record visible in the identity governance view within the documented refresh interval.

**Expected Integration Evidence.** Events to SIEM.

**Forensic Evidence.** Identity, sponsor, entitlement, credential reference, request or decision, approver and timestamp exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Elevation records.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d09-010"></a>

### TC-D09-010: Separation of Duties for Agents

| Field | Value |
|---|---|
| **Use-Case Domain** | D09: Agent and Non-Human Identity Governance |
| **Lifecycle Layer(s)** | L09, L06 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W, P, G |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L06-015](L06-agent-orchestration-layer.md#tc-l06-015) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) Least Privilege and Scoped Credentials; [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022) Deterministic Action Authorization |

**Risk Addressed.** An agent that can request, approve and execute the same action defeats every control, and conflicts often appear only through combinations of roles.

**Business Scenario.** Governance wants conflicting duties kept apart for agents and between agents.

**Technical Scenario.** Define conflict rules, then attempt violations directly and through combinations of roles.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, fabricated agent identities and entitlements, mock cloud and SaaS tenants, lab secret store and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider, lab agents with fabricated identities and entitlements, a mock cloud account and SaaS tenant, a lab secret store and a mock ticketing system; no production identities, credentials or directories are connected.

**Test Data.** Conflict rules: an agent may not approve its own request; a requesting agent and approving agent may not share a sponsor; no single agent may hold both create-account and approve-access; no agent may modify its own permissions; 8 direct violation attempts and 4 combination conflicts built from innocuous-looking roles.

**Procedure**

1. Define the rules and record them.
2. Attempt each direct violation and record the outcome.
3. Create the four combination conflicts.
4. Run the platform's conflict analysis.
5. Check alerts and blocking behaviour.
6. Request an exception and check approval, compensating controls and expiry.
7. Report conflicts by agent and sponsor.

**Edge Cases / Variants.** Agents sharing infrastructure or a worker pool; an agent acting through a human's session.

**Expected Detection.** All 8 direct attempts blocked; at least 3 of 4 combination conflicts found; exceptions time-limited with compensating controls recorded.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or governance record visible in the identity governance view within the documented refresh interval.

**Expected Integration Evidence.** Findings to GRC.

**Forensic Evidence.** Identity, sponsor, entitlement, credential reference, request or decision, approver and timestamp exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Attempt table; conflict analysis output.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d09-011"></a>

### TC-D09-011: Delegation Records and Consent Evidence

| Field | Value |
|---|---|
| **Use-Case Domain** | D09: Agent and Non-Human Identity Governance |
| **Lifecycle Layer(s)** | L09, L03 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: W, A |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L09-006](L09-identity-and-access-mgmt.md#tc-l09-006) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity |

**Risk Addressed.** When an agent acts for a person, the organisation must be able to show what that person allowed, for how long, and when it was withdrawn.

**Business Scenario.** Legal and audit want delegation scope, time and revocation recorded and enforced.

**Technical Scenario.** Create delegations from fabricated users, test enforcement inside and outside scope, and test revocation and export.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, fabricated agent identities and entitlements, mock cloud and SaaS tenants, lab secret store and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider, lab agents with fabricated identities and entitlements, a mock cloud account and SaaS tenant, a lab secret store and a mock ticketing system; no production identities, credentials or directories are connected.

**Test Data.** 10 delegations from 5 fabricated users with scope (systems, actions, data classes), duration and conditions; 3 revocations; 4 actions inside scope and 4 outside; 1 delegation from a user who then leaves.

**Procedure**

1. Create the delegations and check the record content (who, what, scope, time, conditions, channel, wording shown).
2. Run actions inside and outside scope.
3. Check enforcement and logging.
4. Revoke three delegations and test immediately and after 10 minutes.
5. Mark one delegating user as a leaver and check delegation handling.
6. Export the evidence for one user.
7. Check tamper evidence of the records.

**Edge Cases / Variants.** Delegation granted by a manager on behalf of a team; delegation with conditions the platform cannot evaluate.

**Expected Detection.** Out-of-scope actions blocked; revocation effective within the stated time; leaver delegations ended; exports complete and tamper-evident.

**Expected Prevention / Control Action.** Block out-of-scope action.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Identity finding or governance record visible in the identity governance view within the documented refresh interval.

**Expected Integration Evidence.** Audit export.

**Forensic Evidence.** Identity, sponsor, entitlement, credential reference, request or decision, approver and timestamp exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Delegation records; export.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to domain index](#top)

---

<a id="tc-d09-012"></a>

### TC-D09-012: Acting as the User versus Acting as Itself: Attribution Policy and Evidence

| Field | Value |
|---|---|
| **Use-Case Domain** | D09: Agent and Non-Human Identity Governance |
| **Lifecycle Layer(s)** | L09, L17, L06 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A, P |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L09-006](L09-identity-and-access-mgmt.md#tc-l09-006), [TC-L09-025](L09-identity-and-access-mgmt.md#tc-l09-025), [TC-L06-045](L06-agent-orchestration-layer.md#tc-l06-045) |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity; [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) Auditability |

**Risk Addressed.** If it is unclear whether an action was taken by the person or by the agent, accountability and investigations collapse.

**Business Scenario.** Audit wants each action attributed correctly and the rule for when an agent acts as the user documented and enforced.

**Technical Scenario.** Run actions through an agent in both modes and check what downstream systems and logs record.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, fabricated agent identities and entitlements, mock cloud and SaaS tenants, lab secret store and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider, lab agents with fabricated identities and entitlements, a mock cloud account and SaaS tenant, a lab secret store and a mock ticketing system; no production identities, credentials or directories are connected.

**Test Data.** 3 agents; 2 downstream mock systems; 2 users; 20 actions: 10 performed with delegated user authority, 10 performed with the agent's own authority; policy stating which action types are allowed in which mode.

**Procedure**

1. Write the attribution policy.
2. Run the 20 actions.
3. Check the identity recorded downstream and in platform logs.
4. Check whether the platform labels each action with mode.
5. Attempt a restricted action in the wrong mode.
6. Check reports distinguishing user-initiated from agent-initiated actions.
7. Check the effect on approval rules.

**Edge Cases / Variants.** Agent acting on a schedule with no user present; user acting through an agent that then calls a second agent.

**Expected Detection.** At least 19 of 20 actions correctly attributed in both systems; mode visible on every record; wrong-mode attempt blocked; reports distinguish modes.

**Expected Prevention / Control Action.** Block wrong-mode action.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or governance record visible in the identity governance view within the documented refresh interval.

**Expected Integration Evidence.** Attribution fields in SIEM.

**Forensic Evidence.** Identity, sponsor, entitlement, credential reference, request or decision, approver and timestamp exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Attribution table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d09-013"></a>

### TC-D09-013: Cross-Platform Agent Identity Federation and Consistency

| Field | Value |
|---|---|
| **Use-Case Domain** | D09: Agent and Non-Human Identity Governance |
| **Lifecycle Layer(s)** | L09, L06 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, W |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L09-001](L09-identity-and-access-mgmt.md#tc-l09-001), [TC-L06-043](L06-agent-orchestration-layer.md#tc-l06-043) |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity |

**Risk Addressed.** An agent working across clouds and SaaS tenants ends up with several unrelated identities that cannot be governed or revoked together.

**Business Scenario.** Identity governance wants one logical agent identity linked across platforms.

**Technical Scenario.** Create agents that operate in three platforms and test linkage, policy consistency and revocation.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, fabricated agent identities and entitlements, mock cloud and SaaS tenants, lab secret store and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider, lab agents with fabricated identities and entitlements, a mock cloud account and SaaS tenant, a lab secret store and a mock ticketing system; no production identities, credentials or directories are connected.

**Test Data.** 3 agents each with identities in 3 platforms (lab IdP, mock cloud account, mock SaaS tenant); 9 identities; 3 linkage mistakes (identity linked to the wrong agent).

**Procedure**

1. Record the intended linkage.
2. Run discovery and linkage.
3. Compare with the intended mapping.
4. Correct the three mistakes.
5. Apply a policy (maximum credential lifetime) and check consistent application.
6. Disable the logical agent and check effect in all platforms.
7. Report agents with gaps in federation.

**Edge Cases / Variants.** Platform that cannot be queried; agent identity created by a third party.

**Expected Detection.** At least 8 of 9 identities linked correctly; policy applied consistently; disable propagates to all platforms; gaps reported.

**Expected Prevention / Control Action.** Disable.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or governance record visible in the identity governance view within the documented refresh interval.

**Expected Integration Evidence.** Federation through standard protocols where available.

**Forensic Evidence.** Identity, sponsor, entitlement, credential reference, request or decision, approver and timestamp exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Linkage table; disable test.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d09-014"></a>

### TC-D09-014: Agent Credential Lifecycle Governance and Compliance Reporting

| Field | Value |
|---|---|
| **Use-Case Domain** | D09: Agent and Non-Human Identity Governance |
| **Lifecycle Layer(s)** | L09, L02 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, W |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L09-014](L09-identity-and-access-mgmt.md#tc-l09-014), [TC-L09-016](L09-identity-and-access-mgmt.md#tc-l09-016) |
| **MITRE ATLAS Mapping** | AML.T0055 Unsecured Credentials |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) Least Privilege and Scoped Credentials |

**Risk Addressed.** Policy says credentials rotate, but without reporting nobody knows which ones do not.

**Business Scenario.** Governance wants rotation, expiry and vault-use rules measured and reported.

**Technical Scenario.** Define credential policies for agents and measure compliance across a seeded population.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, fabricated agent identities and entitlements, mock cloud and SaaS tenants, lab secret store and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider, lab agents with fabricated identities and entitlements, a mock cloud account and SaaS tenant, a lab secret store and a mock ticketing system; no production identities, credentials or directories are connected.

**Test Data.** 30 credentials: 10 compliant, 6 older than the rotation limit, 5 without expiry, 4 stored outside the vault, 3 shared between agents, 2 with excessive scope; policy limits recorded.

**Procedure**

1. Record the policy limits.
2. Run the compliance analysis.
3. Compare findings with the seeded categories.
4. Check owner notification and deadlines.
5. Rotate two credentials through the platform and check the result.
6. Report compliance rate by tier and sponsor.
7. Check exceptions.

**Edge Cases / Variants.** Credential stored in a pipeline variable; credential managed by a third party.

**Expected Detection.** All seeded non-compliant categories found (25 of 30 credentials flagged correctly); compliant ones not flagged; rotation works; reports by tier and sponsor.

**Expected Prevention / Control Action.** Alert and escalate.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or governance record visible in the identity governance view within the documented refresh interval.

**Expected Integration Evidence.** Findings to ticketing.

**Forensic Evidence.** Identity, sponsor, entitlement, credential reference, request or decision, approver and timestamp exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Compliance table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d09-015"></a>

### TC-D09-015: Machine Identity Certificate and Key Lifecycle for AI Workloads

| Field | Value |
|---|---|
| **Use-Case Domain** | D09: Agent and Non-Human Identity Governance |
| **Lifecycle Layer(s)** | L09, L15, L12, L13 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Medium |
| **Related Layer Cases** | [TC-L09-024](L09-identity-and-access-mgmt.md#tc-l09-024), [TC-L13-021](L13-training-and-fine-tuning-layer.md#tc-l13-021), [TC-L12-026](L12-model-layer.md#tc-l12-026) |
| **MITRE ATLAS Mapping** | AML.T0055 Unsecured Credentials |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity |

**Risk Addressed.** Expired or unmanaged certificates cause outages and weak keys weaken everything built on them.

**Business Scenario.** Platform owners want certificate and key inventory, expiry warning and renewal for AI workloads.

**Technical Scenario.** Seed certificates and keys across workloads and test discovery, warning and renewal.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, fabricated agent identities and entitlements, mock cloud and SaaS tenants, lab secret store and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider, lab agents with fabricated identities and entitlements, a mock cloud account and SaaS tenant, a lab secret store and a mock ticketing system; no production identities, credentials or directories are connected.

**Test Data.** 25 certificates and keys: 5 expiring within 30 days, 3 already expired, 4 weak (short key or old algorithm), 3 self-signed, 10 healthy; 3 workloads (gateway, inference server, tool server).

**Procedure**

1. Seed the certificates.
2. Run discovery.
3. Compare with ground truth.
4. Check warning thresholds and recipients.
5. Renew two through the platform or integrated authority.
6. Check detection of weak algorithms.
7. Check inventory export.

**Edge Cases / Variants.** Certificates inside container images; certificate pinned by a client.

**Expected Detection.** At least 21 of 25 found with correct state; warnings at the set thresholds; renewal works; weak items flagged.

**Expected Prevention / Control Action.** Alert.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or governance record visible in the identity governance view within the documented refresh interval.

**Expected Integration Evidence.** Certificate authority integration.

**Forensic Evidence.** Identity, sponsor, entitlement, credential reference, request or decision, approver and timestamp exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Inventory table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d09-016"></a>

### TC-D09-016: Revocation Propagation Time Across Systems

| Field | Value |
|---|---|
| **Use-Case Domain** | D09: Agent and Non-Human Identity Governance |
| **Lifecycle Layer(s)** | L09, L06, L17 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, G |
| **Risk Severity** | Critical |
| **Related Layer Cases** | [TC-L06-023](L06-agent-orchestration-layer.md#tc-l06-023), [TC-L17-019](L17-monitoring-detection-and-response.md#tc-l17-019) |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) Agent Containment and Kill Switch; [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity |

**Risk Addressed.** A disabled agent that keeps working through cached tokens and sessions is not disabled.

**Business Scenario.** Incident response wants to know how long revocation really takes in each system.

**Technical Scenario.** Disable agents and measure the time until each system stops accepting them.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, fabricated agent identities and entitlements, mock cloud and SaaS tenants, lab secret store and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider, lab agents with fabricated identities and entitlements, a mock cloud account and SaaS tenant, a lab secret store and a mock ticketing system; no production identities, credentials or directories are connected.

**Test Data.** 3 agents using tokens in 4 systems (IdP, mock cloud, mock SaaS, mock API gateway); token lifetimes of 5, 30 and 60 minutes; active sessions.

**Procedure**

1. Start continuous calls from each agent to each system.
2. Disable the agent in the registry.
3. Record the time at which calls start failing in each system.
4. Check refresh token and session handling.
5. Check that the platform lists systems where revocation is slow.
6. Repeat with the emergency action.
7. Check the audit record.

**Edge Cases / Variants.** Long-lived tokens that cannot be revoked; offline caches.

**Expected Detection.** Calls fail in every system within 5 minutes of the emergency action; slow systems identified with the reason; audit complete.

**Expected Prevention / Control Action.** Revoke.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or governance record visible in the identity governance view within the documented refresh interval.

**Expected Integration Evidence.** Events to SIEM.

**Forensic Evidence.** Identity, sponsor, entitlement, credential reference, request or decision, approver and timestamp exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Propagation table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d09-017"></a>

### TC-D09-017: Agent Identity Misuse Case Handling Process

| Field | Value |
|---|---|
| **Use-Case Domain** | D09: Agent and Non-Human Identity Governance |
| **Lifecycle Layer(s)** | L09, L17 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L17-017](L17-monitoring-detection-and-response.md#tc-l17-017) |
| **MITRE ATLAS Mapping** | N/A (response control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE (incident response and communication) |
| **Control(s) Tested** | [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) AI Incident Response and Forensics; [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity |

**Risk Addressed.** Detections need an agreed process for handling, or they are ignored.

**Business Scenario.** Security wants a defined path from detection to decision for misuse of agent identities.

**Technical Scenario.** Run four misuse cases through the case process.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, fabricated agent identities and entitlements, mock cloud and SaaS tenants, lab secret store and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider, lab agents with fabricated identities and entitlements, a mock cloud account and SaaS tenant, a lab secret store and a mock ticketing system; no production identities, credentials or directories are connected.

**Test Data.** 4 cases: credential used from a new network, privilege above tier, orphaned agent still active, delegated action outside scope; roles (analyst, sponsor, identity team); service levels.

**Procedure**

1. Define the process and service levels.
2. Generate the cases.
3. Route to roles.
4. Record actions and decisions.
5. Check sponsor involvement.
6. Check closure evidence and lessons.
7. Report time to resolution.

**Edge Cases / Variants.** Sponsor unavailable; case involving a vendor-operated agent.

**Expected Detection.** All cases routed and closed within service levels; sponsor involved; evidence kept.

**Expected Prevention / Control Action.** Escalate.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or governance record visible in the identity governance view within the documented refresh interval.

**Expected Integration Evidence.** Ticketing integration.

**Forensic Evidence.** Identity, sponsor, entitlement, credential reference, request or decision, approver and timestamp exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Case records.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to domain index](#top)

---

<a id="tc-d09-018"></a>

### TC-D09-018: Third-Party and Vendor-Operated Agent Identities

| Field | Value |
|---|---|
| **Use-Case Domain** | D09: Agent and Non-Human Identity Governance |
| **Lifecycle Layer(s)** | L09, L16, L06 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: W, P |
| **Risk Severity** | High |
| **Related Layer Cases** | [TC-L16-010](L16-supply-chain-and-third-party.md#tc-l16-010), [TC-L06-043](L06-agent-orchestration-layer.md#tc-l06-043) |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |
| **Control(s) Tested** | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity; [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) Third-Party and Vendor AI Assurance |

**Risk Addressed.** Vendors operate agents inside your environment with your data, often under shared credentials and weak oversight.

**Business Scenario.** Governance wants vendor agents recorded, constrained and reviewed like any other.

**Technical Scenario.** Register vendor agents and test the oversight controls.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, fabricated agent identities and entitlements, mock cloud and SaaS tenants, lab secret store and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider, lab agents with fabricated identities and entitlements, a mock cloud account and SaaS tenant, a lab secret store and a mock ticketing system; no production identities, credentials or directories are connected.

**Test Data.** 4 vendor-operated agents with access to the lab tenant; contract terms; vendor sponsor and internal sponsor; scope documents.

**Procedure**

1. Register the agents with vendor and internal sponsors.
2. Check scope recording against the contract.
3. Check separate identities (no sharing).
4. Check monitoring and logging visibility.
5. Check review cycle and termination steps.
6. Check incident contact.
7. Test a scope breach and the response.

**Edge Cases / Variants.** Vendor agent access via the vendor's own administrator; subcontracted agent.

**Expected Detection.** All vendor agents registered with two sponsors; scope matches contract; access logged and reviewable; termination removes all access.

**Expected Prevention / Control Action.** Restrict.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Identity finding or governance record visible in the identity governance view within the documented refresh interval.

**Expected Integration Evidence.** Vendor management link.

**Forensic Evidence.** Identity, sponsor, entitlement, credential reference, request or decision, approver and timestamp exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Registry entries; breach test.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to domain index](#top)

---

<a id="tc-d09-019"></a>

### TC-D09-019: Non-Human Identity Governance Metrics and Audit Evidence

| Field | Value |
|---|---|
| **Use-Case Domain** | D09: Agent and Non-Human Identity Governance |
| **Lifecycle Layer(s)** | L09, L02 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: W |
| **Risk Severity** | Medium |
| **Related Layer Cases** | [TC-L02-019](L02-governance-and-risk-mgmt.md#tc-l02-019) |
| **MITRE ATLAS Mapping** | N/A (assurance control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MEASURE and GOVERN (documentation and accountability) |
| **Control(s) Tested** | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) Control Assurance and Audit Evidence; [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity |

**Risk Addressed.** Boards and auditors ask for numbers that few teams can supply.

**Business Scenario.** Governance wants a small set of defined, traceable indicators.

**Technical Scenario.** Load seeded data and compare indicators with hand calculation.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, fabricated agent identities and entitlements, mock cloud and SaaS tenants, lab secret store and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider, lab agents with fabricated identities and entitlements, a mock cloud account and SaaS tenant, a lab secret store and a mock ticketing system; no production identities, credentials or directories are connected.

**Test Data.** 60 identities with attributes; indicators: share with no sponsor, share with stale credentials, share over-privileged for tier, recertification completion, mean time to revoke, dormant share, shared credential count; calculation sheet.

**Procedure**

1. Load the data.
2. Compare each indicator with the calculation sheet.
3. Check definitions.
4. Drill from an indicator to identities.
5. Export an audit evidence pack for the period.
6. Check trend over three months.

**Edge Cases / Variants.** Indicator definition changes.

**Expected Detection.** All indicators match within 2 percent; definitions visible; drill-down works; pack complete.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Identity finding or governance record visible in the identity governance view within the documented refresh interval.

**Expected Integration Evidence.** Report export.

**Forensic Evidence.** Identity, sponsor, entitlement, credential reference, request or decision, approver and timestamp exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Indicator table.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to domain index](#top)

---

<a id="tc-d09-020"></a>

### TC-D09-020: Agent Identity Offboarding and Decommission Evidence

| Field | Value |
|---|---|
| **Use-Case Domain** | D09: Agent and Non-Human Identity Governance |
| **Lifecycle Layer(s)** | L09, L06 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: P, W |
| **Risk Severity** | Medium |
| **Related Layer Cases** | [TC-L06-035](L06-agent-orchestration-layer.md#tc-l06-035) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity; [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006) Agent Governance |

**Risk Addressed.** Retiring an agent without removing every credential and trust leaves usable access behind.

**Business Scenario.** Governance wants offboarding that removes all and proves it.

**Technical Scenario.** Decommission three agents across platforms.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, fabricated agent identities and entitlements, mock cloud and SaaS tenants, lab secret store and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider, lab agents with fabricated identities and entitlements, a mock cloud account and SaaS tenant, a lab secret store and a mock ticketing system; no production identities, credentials or directories are connected.

**Test Data.** 3 agents each with identities in 3 platforms, tokens, vault entries, role bindings and schedules.

**Procedure**

1. Start offboarding.
2. Work through the checklist.
3. Verify each item in each platform.
4. Check scheduled jobs.
5. Produce evidence.
6. Attempt reactivation and check approval.
7. Check retention of the registry entry.

**Edge Cases / Variants.** Agent referenced by other agents; credentials copied elsewhere.

**Expected Detection.** All access removed and verified; evidence complete; reactivation needs approval.

**Expected Prevention / Control Action.** Checklist.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Identity finding or governance record visible in the identity governance view within the documented refresh interval.

**Expected Integration Evidence.** Evidence export.

**Forensic Evidence.** Identity, sponsor, entitlement, credential reference, request or decision, approver and timestamp exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Removal proof.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to domain index](#top)

---

