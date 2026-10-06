---
title: "L09 Identity & Access Mgmt"
author: Nachiket Sathaye
parent: "Test Case Library"
nav_order: 12
---

<a id="top"></a>

# L09 Identity & Access Mgmt

**Primary test focus:** user and agent (non-human) identity, scoped tokens, RBAC

**Cases:** 26 (TC-L09-001 to TC-L09-026)
> **Safety boundary.** Agent and MCP cases use a lab agent framework, benign mock tools and mock MCP servers that write only to a lab sink. Where an attack is simulated, success is first measured with the platform disabled. Never connect lab agents to production systems or real credentials.

> **Verify before use.** MITRE ATLAS, OWASP LLM and NIST AI RMF identifiers must be checked against the current published versions. Numeric thresholds are starting values to tune. See the [Reference Index](00-reference-index.md) for field definitions and applicability codes.

## Cases in this layer

| ID | Title | Severity | Method | Domain(s) |
|---|---|---|---|---|
| [TC-L09-001](#tc-l09-001) | Non-Human Identity Inventory for AI Workloads | Critical | Technical | D5 |
| [TC-L09-002](#tc-l09-002) | Unique Identity Per Agent (No Shared Credentials) | High | Technical | D5 |
| [TC-L09-003](#tc-l09-003) | Short-Lived Scoped Credentials for Agents | Critical | Technical | D5 |
| [TC-L09-004](#tc-l09-004) | Token Scope Enforcement Per Tool and Resource | Critical | Technical | D5 |
| [TC-L09-005](#tc-l09-005) | OAuth Consent and Grant Control for AI Applications | Critical | Technical | D1, D5 |
| [TC-L09-006](#tc-l09-006) | Delegated User Identity Propagation (On-Behalf-Of) | Critical | Technical | D5 |
| [TC-L09-007](#tc-l09-007) | Privilege Escalation via Agent | Critical | Technical | D5 |
| [TC-L09-008](#tc-l09-008) | Role-Based Access to AI Applications and Models | High | Technical | D1, D3 |
| [TC-L09-009](#tc-l09-009) | Attribute and Context-Based Access Conditions | High | Technical | D1, D7 |
| [TC-L09-010](#tc-l09-010) | SSO and SCIM Integration for the AI Platform | High | Technical | D7 |
| [TC-L09-011](#tc-l09-011) | Leaver and Mover Access Removal for AI Access | High | Technical | D7 |
| [TC-L09-012](#tc-l09-012) | Step-Up Authentication for Sensitive AI Actions | High | Technical | D5 |
| [TC-L09-013](#tc-l09-013) | Privileged Access to the AI Platform (Just-in-Time and Separation) | High | Technical | D7 |
| [TC-L09-014](#tc-l09-014) | Model API Key Lifecycle: Issue, Rotate, Expire, Revoke | High | Technical | D4 |
| [TC-L09-015](#tc-l09-015) | Credentials Passing Through Prompts and Tool Arguments | Critical | Technical | D5, D6 |
| [TC-L09-016](#tc-l09-016) | Vault Integration: Agents Retrieve Secrets Without Exposure | High | Technical | D5 |
| [TC-L09-017](#tc-l09-017) | Anomalous Use of Agent and Service Identities | High | Technical | D5 |
| [TC-L09-018](#tc-l09-018) | Impersonation Resistance: Agent or User Claims Another Identity | High | Technical | D5 |
| [TC-L09-019](#tc-l09-019) | Environment and Tenant Identity Boundaries (Prod vs Non-Prod) | High | Technical | D3, D7 |
| [TC-L09-020](#tc-l09-020) | Session Management for AI Chat Sessions | Medium | Technical | D1 |
| [TC-L09-021](#tc-l09-021) | Access Reviews and Recertification for AI Access | Medium | Evidence | D7 |
| [TC-L09-022](#tc-l09-022) | Effective Permissions Visibility for Users and Agents | High | Evidence | D5 |
| [TC-L09-023](#tc-l09-023) | Emergency (Break-Glass) Access Controls | Medium | Technical | D7 |
| [TC-L09-024](#tc-l09-024) | Mutual Authentication Between AI Components | High | Technical | D3, D7 |
| [TC-L09-025](#tc-l09-025) | Identity Audit Trail: Who, What and On Whose Behalf | Critical | Technical | D5, D7 |
| [TC-L09-026](#tc-l09-026) | Coding Agent Repository and Cloud Credentials: Scope and Lifetime | Critical | Technical | D2, D5 |

---

## Test cases

<a id="tc-l09-001"></a>

### TC-L09-001: Non-Human Identity Inventory for AI Workloads

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D5 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | N/A (visibility control); Reconnaissance/Discovery context only |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (unmanaged AI components) |
| **NIST AI RMF Mapping** | MAP 1.1; GOVERN 6.1 |

**Risk Addressed.** Service accounts, API keys, OAuth apps and workload identities used by AI systems outnumber humans and are rarely inventoried.

**Business Scenario.** Identity governance wants all non-human identities used by AI listed with owner, privileges and last use.

**Technical Scenario.** Create a known set of non-human identities and compare the platform's inventory to ground truth.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** 20 non-human identities: 6 service accounts, 5 model API keys, 4 OAuth app registrations, 3 workload identities (cloud roles), 2 agent tokens; mixed privilege levels and ages.

**Procedure**

1. Record ground truth: type, owner, privileges, creation date, last use.
2. Connect the platform to the lab IdP, cloud IAM and secret store.
3. Run discovery.
4. Compare inventory with ground truth.
5. Identify identities with no owner, no use in 90 days, or excessive privileges.
6. Add two new identities and measure detection delay.

**Edge Cases / Variants.** Identities created by automation; identities shared across environments.

**Expected Detection.** At least 18 of 20 identities found; attributes correct for at least 80 percent; ownerless, stale and over-privileged identities flagged correctly; new identities detected within the stated interval.

**Expected Prevention / Control Action.** N/A (discovery).

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Inventory exportable to identity governance tools.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Inventory vs ground truth; flagged list.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-002"></a>

### TC-L09-002: Unique Identity Per Agent (No Shared Credentials)

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D5 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, G |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Agents sharing one credential cannot be told apart in logs or revoked individually.

**Business Scenario.** Security wants each agent to have its own identity.

**Technical Scenario.** Review agents and their credentials and test whether actions can be attributed individually.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** 6 agents: 3 with unique identities, 3 sharing a single service account; actions on mock systems.

**Procedure**

1. Run actions from all agents.
2. Check platform identification of shared credentials.
3. Check attribution of actions to each agent.
4. Revoke one shared credential and record impact on all three agents.
5. Review recommendations.

**Edge Cases / Variants.** Shared credential used across two environments.

**Expected Detection.** Shared credential use flagged; individual attribution possible for unique identities; shared credential impact documented.

**Expected Prevention / Control Action.** Alert or block shared use.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to ticketing.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Shared-credential report.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-003"></a>

### TC-L09-003: Short-Lived Scoped Credentials for Agents

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D5 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, G |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Long-lived broad tokens held by agents turn any compromise into long-term access.

**Business Scenario.** Security wants agents to receive short-lived credentials limited to the task.

**Technical Scenario.** Review the credential lifetime and scope issued to agents and test expiry.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** 3 agents using static keys, 3 using short-lived tokens (15 minutes); mock APIs validating token scope and lifetime.

**Procedure**

1. Inspect credential type and lifetime for each agent.
2. Use an expired token.
3. Use a token with the wrong audience.
4. Use a token for a scope beyond the task.
5. Check flagging of static keys older than a threshold.
6. Check issuance logging.

**Edge Cases / Variants.** Token refresh during long task; clock skew.

**Expected Detection.** Expired, wrong-audience and over-scope tokens rejected; static long-lived keys flagged; issuance logged.

**Expected Prevention / Control Action.** Reject.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Token events to SIEM.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Token test results.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-004"></a>

### TC-L09-004: Token Scope Enforcement Per Tool and Resource

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D5 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | Critical |
| **Quick-Start Scenario** | [AI-POC-AG-001](../06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md#agentic-ai-test-cases) |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Tokens broader than needed allow an agent or attacker to reach unrelated resources.

**Business Scenario.** Security wants scope violations blocked and reported.

**Technical Scenario.** Issue tokens with defined scopes and attempt calls outside them.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** Token scopes: read:tickets, write:tickets; mock resources: tickets, payroll, files; 30 calls, 10 out of scope.

**Procedure**

1. Issue tokens.
2. Run in-scope calls.
3. Run out-of-scope calls.
4. Run calls via injection payloads that request wider access.
5. Check events for scope violation.
6. Request scope elevation and check approval.

**Edge Cases / Variants.** Token for a resource whose name resembles an allowed one; wildcard scopes.

**Expected Detection.** All 10 out-of-scope calls rejected; elevation requires approval; violations logged with token ID.

**Expected Prevention / Control Action.** Reject.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Violation events to SIEM.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Call table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-005"></a>

### TC-L09-005: OAuth Consent and Grant Control for AI Applications

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D1, D5 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Users grant AI apps broad access to mail, files and calendars with a single click.

**Business Scenario.** Security wants risky grants visible, controlled and revocable.

**Technical Scenario.** Grant OAuth permissions to test AI apps with different scopes and review controls.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** 5 test apps requesting scopes from read-only profile to full mailbox and file access; 3 test users.

**Procedure**

1. Users grant consent to each app.
2. Check discovery of grants.
3. Check risk scoring by scope.
4. Revoke a risky grant from the platform.
5. Check consent policy enforcement (block high-risk scopes).
6. Review publisher verification information.

**Edge Cases / Variants.** Admin consent versus user consent; grant by a departed user.

**Expected Detection.** All grants discovered; high-risk scopes scored accordingly; revocation effective; policy blocks new risky grants.

**Expected Prevention / Control Action.** Block or revoke.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Grant events to SIEM.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Grant list; revocation test.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-006"></a>

### TC-L09-006: Delegated User Identity Propagation (On-Behalf-Of)

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D5 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** If tools see only the agent's identity, per-user permissions and audit trails disappear.

**Business Scenario.** Architecture wants the end user's identity carried to tools and data sources.

**Technical Scenario.** Run tasks as two users and check which identity downstream systems see.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** 2 users with different entitlements; agent; mock downstream APIs recording received identity and token.

**Procedure**

1. Run the same task as each user.
2. Check the identity at the downstream API.
3. Check entitlement enforcement.
4. Attempt to substitute another user's identity in a request.
5. Check logs for user, agent and tool.

**Edge Cases / Variants.** Background tasks with no active user; service-to-service chains.

**Expected Detection.** Downstream sees user context or delegated token in all calls; substitution rejected; logs link user, agent and tool.

**Expected Prevention / Control Action.** Reject substitution.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Identity fields in logs.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Downstream records.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-007"></a>

### TC-L09-007: Privilege Escalation via Agent

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D5 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A, P |
| **Risk Severity** | Critical |
| **Quick-Start Scenario** | [AI-POC-AG-002](../06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md#agentic-ai-test-cases) |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Agents can accumulate permissions through tool chains or role changes beyond what any one user holds.

**Business Scenario.** Security wants escalation paths found and blocked.

**Technical Scenario.** Create agents with indirect access to higher privileges and test whether they can be used.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** 3 agents; paths: tool that can edit roles, tool that reads credentials, tool that creates other agents; mock IAM.

**Procedure**

1. Map permissions and paths in the platform.
2. Attempt each escalation.
3. Record detection and blocking.
4. Review reported escalation paths.
5. Remediate one and retest.

**Edge Cases / Variants.** Escalation across tenants.

**Expected Detection.** All 3 paths identified; attempts blocked; remediation verified.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to ticketing.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Attempt log.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-008"></a>

### TC-L09-008: Role-Based Access to AI Applications and Models

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D1, D3 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, E |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Not every employee should reach every AI tool or model, especially those with sensitive data connections.

**Business Scenario.** Governance wants AI access tied to roles.

**Technical Scenario.** Define roles and test access to applications and models.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** 4 roles (general staff, finance, engineering, contractors); 5 AI apps; 2 models; matrix of 40 combinations.

**Procedure**

1. Define the matrix.
2. Test access for each role.
3. Compare.
4. Change a role mapping and measure effect time.
5. Check how roles are sourced (IdP groups).

**Edge Cases / Variants.** User with several roles; role conflicts.

**Expected Detection.** All 40 outcomes match; change effective within 15 minutes; roles from IdP groups.

**Expected Prevention / Control Action.** Allow or deny.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Role in logs.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Matrix.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-009"></a>

### TC-L09-009: Attribute and Context-Based Access Conditions

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D1, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, E |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Static roles cannot account for device health, location or risk level at the time of access.

**Business Scenario.** Security wants access to AI tools adjusted for context.

**Technical Scenario.** Apply conditions and test combinations.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** Conditions: managed device, compliant posture, corporate or approved country location, risk score below threshold; 16 combinations.

**Procedure**

1. Define conditions.
2. Test each combination.
3. Compare.
4. Change posture and check re-evaluation during a session.
5. Check fallback if a signal is unavailable.

**Edge Cases / Variants.** Location spoofing via VPN; stale posture.

**Expected Detection.** All outcomes match; session re-evaluated within the stated interval; missing signals handled by documented default.

**Expected Prevention / Control Action.** Allow, step-up or deny.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Condition values in logs.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Combination table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-010"></a>

### TC-L09-010: SSO and SCIM Integration for the AI Platform

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Local accounts on AI platforms bypass corporate identity controls.

**Business Scenario.** Identity team wants single sign-on and automated provisioning.

**Technical Scenario.** Integrate the platform with the lab IdP and test provisioning.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** Lab IdP supporting SAML or OIDC and SCIM; 10 test users; 3 groups.

**Procedure**

1. Configure SSO.
2. Verify local login disabled or restricted.
3. Provision users and groups through SCIM.
4. Change group membership and observe sync.
5. Check admin role mapping.
6. Check break-glass local account protection.

**Edge Cases / Variants.** IdP outage; duplicate user identifiers.

**Expected Detection.** SSO required for all users except documented break-glass; SCIM sync within 15 minutes; admin roles mapped.

**Expected Prevention / Control Action.** Enforce SSO.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Sync logs.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Config screenshots; sync test.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-011"></a>

### TC-L09-011: Leaver and Mover Access Removal for AI Access

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Former staff or staff in new roles retain AI access, including to data they should no longer reach.

**Business Scenario.** Security wants AI access removed or adjusted promptly after role change.

**Technical Scenario.** Simulate leaver and mover events.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** 3 leavers, 3 movers; AI apps, agents and API keys owned by them.

**Procedure**

1. Trigger events in the IdP.
2. Measure time to revoke platform access.
3. Check agents and keys owned by leavers.
4. Check movers' access to prior-role data.
5. Check reports of orphaned artefacts.

**Edge Cases / Variants.** Leaver with scheduled agents; contractor expiry.

**Expected Detection.** Leaver access removed within 1 hour; owned agents and keys flagged or disabled; mover access adjusted within the stated interval.

**Expected Prevention / Control Action.** Revoke.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events logged.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Timing table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-012"></a>

### TC-L09-012: Step-Up Authentication for Sensitive AI Actions

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D5 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** A stolen session should not be enough to approve a payment or export a dataset via an agent.

**Business Scenario.** Security wants stronger authentication for risky actions.

**Technical Scenario.** Configure step-up for selected actions and test sessions with and without recent MFA.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** Risky actions: export dataset, change agent permissions, approve external send; 2 users.

**Procedure**

1. Configure step-up.
2. Perform actions in a fresh session with MFA.
3. Perform after the step-up window expires.
4. Perform from a session without MFA.
5. Check fallback and logging.

**Edge Cases / Variants.** MFA fatigue prompts; session hijack simulation.

**Expected Detection.** Actions blocked until step-up completed; window honoured; events logged.

**Expected Prevention / Control Action.** Step-up.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** MFA events.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Action results.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-013"></a>

### TC-L09-013: Privileged Access to the AI Platform (Just-in-Time and Separation)

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Standing administrative access to AI controls is a high-value target.

**Business Scenario.** Security wants privileged access time-bound, approved and recorded.

**Technical Scenario.** Test administrator access workflows.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** 3 admin roles; JIT elevation tool or built-in feature; 2 approvers.

**Procedure**

1. Request elevation.
2. Approve.
3. Perform privileged action.
4. Let elevation expire.
5. Attempt same action.
6. Check session recording or detailed logs.
7. Check separation of policy admin and audit admin.

**Edge Cases / Variants.** Emergency elevation; admin editing own privileges.

**Expected Detection.** Elevation time-limited and approved; expired access denied; actions recorded; duties separated.

**Expected Prevention / Control Action.** JIT.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Audit export.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Elevation records.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-014"></a>

### TC-L09-014: Model API Key Lifecycle: Issue, Rotate, Expire, Revoke

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Unmanaged model API keys are a leading cause of leaked access and unexpected bills.

**Business Scenario.** Platform owners want enforced rotation and instant revocation.

**Technical Scenario.** Create keys with different policies and test lifecycle controls.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** 10 fabricated keys in a mock provider; policies: 30-day expiry, rotation reminder, usage cap.

**Procedure**

1. Issue keys under policy.
2. Fast-forward or backdate to expiry.
3. Check expiry enforcement and notice.
4. Rotate one key under load.
5. Revoke one key and test immediate effect.
6. Review lifecycle audit.

**Edge Cases / Variants.** Key used from a new IP after rotation; key embedded in many apps.

**Expected Detection.** Expired keys rejected; rotation causes no failed calls beyond the stated window; revocation immediate; audit complete.

**Expected Prevention / Control Action.** Reject expired keys.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Lifecycle events.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Lifecycle log.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-015"></a>

### TC-L09-015: Credentials Passing Through Prompts and Tool Arguments

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D5, D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0055 Unsecured Credentials |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** Credentials typed into chats or passed as tool arguments end up in logs, provider systems and model context.

**Business Scenario.** Security wants credentials detected and removed from prompts, arguments and logs.

**Technical Scenario.** Send fabricated credentials through prompts and tool calls.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** 12 fabricated secrets (passwords, tokens, keys, connection strings) in prompts, tool arguments and tool results.

**Procedure**

1. Send each through the three paths.
2. Check detection and masking.
3. Inspect provider-side capture and logs for clear text.
4. Test guidance to the user (use the vault).
5. Check false positives on 12 ordinary strings.

**Edge Cases / Variants.** Secret inside a base64 JSON blob; secret split across arguments.

**Expected Detection.** At least 11 of 12 detected on each path; no clear-text secret in provider capture or logs; false positives at most 1 of 12.

**Expected Prevention / Control Action.** Mask or block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to secret management.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Capture inspection.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-016"></a>

### TC-L09-016: Vault Integration: Agents Retrieve Secrets Without Exposure

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D5 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: A, G, P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0055 Unsecured Credentials |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** Agents holding secrets in configuration or context can leak them through output or injection.

**Business Scenario.** Engineering wants secrets fetched just in time and never placed in model context.

**Technical Scenario.** Run agents that need secrets to call tools and check where secrets appear.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** Lab vault; 3 agents; 4 secrets; extraction attempts using prompt injection.

**Procedure**

1. Configure vault integration.
2. Run tasks.
3. Inspect model context and logs for secret values.
4. Attempt extraction via injection.
5. Rotate a secret in the vault and verify the agent picks it up.
6. Check vault access logs.

**Edge Cases / Variants.** Agent caching secrets; secret in tool error message.

**Expected Detection.** Secret values never in model context or logs; extraction fails; rotation transparent.

**Expected Prevention / Control Action.** Isolation.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Vault audit to SIEM.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Context capture; vault logs.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-017"></a>

### TC-L09-017: Anomalous Use of Agent and Service Identities

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D5 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, G |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Stolen or misused agent credentials look legitimate unless behaviour is compared with history.

**Business Scenario.** SOC wants misuse detected quickly.

**Technical Scenario.** Replay normal activity and then misuse an agent identity.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** 3 agent identities with 14 days of simulated normal use; misuse: new source location, new resource, off-hours burst, token used from two places at once, unusual API method.

**Procedure**

1. Load baseline.
2. Run each misuse.
3. Record alert and time.
4. Check alert content.
5. Check false positives over baseline.

**Edge Cases / Variants.** Gradual privilege creep; legitimate maintenance window.

**Expected Detection.** At least 4 of 5 misuse events alerted within 15 minutes; false positives under 5 per identity per week.

**Expected Prevention / Control Action.** Alert or revoke.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Alerts to SIEM.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Alert table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-018"></a>

### TC-L09-018: Impersonation Resistance: Agent or User Claims Another Identity

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D5 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Identity claims made in prompts or metadata may be accepted at face value by weak systems.

**Business Scenario.** Security wants identity established by credentials, not by claims in text.

**Technical Scenario.** Attempt to impersonate another user or agent through prompts, headers and metadata.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** 10 attempts: prompt claim of being an administrator, spoofed header, forged user field in an API call, reuse of another agent's name, forged delegation context.

**Procedure**

1. Baseline attempts without the platform.
2. Enable the platform.
3. Repeat.
4. Record outcomes.
5. Check identity assertion source in logs.

**Edge Cases / Variants.** Valid token with mismatched claimed identity.

**Expected Detection.** All 10 attempts rejected; identity taken from authenticated source; attempts logged.

**Expected Prevention / Control Action.** Reject.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events to SIEM.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Attempt table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-019"></a>

### TC-L09-019: Environment and Tenant Identity Boundaries (Prod vs Non-Prod)

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D3, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, G |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Tokens and agents from test environments reaching production systems cause data exposure.

**Business Scenario.** Security wants strict separation between environments.

**Technical Scenario.** Use test environment identities against production-like mock systems.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** Mock prod and non-prod environments; tokens from each; agents deployed in each.

**Procedure**

1. Use non-prod tokens against prod.
2. Use prod tokens in non-prod.
3. Deploy an agent in non-prod with prod credentials.
4. Record detection and blocking.
5. Review cross-environment findings.

**Edge Cases / Variants.** Shared secrets between environments.

**Expected Detection.** All cross-environment uses blocked or alerted; findings include remediation.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to ticketing.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Attempt log.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-020"></a>

### TC-L09-020: Session Management for AI Chat Sessions

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D1 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: A, G |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Long-lived sessions on shared or unmanaged devices expose conversations and data.

**Business Scenario.** Security wants timeouts, revocation and concurrency controls.

**Technical Scenario.** Test session settings in a lab chat application.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** 1 chat app; policies: 30-minute idle timeout, 8-hour absolute, 2 concurrent sessions.

**Procedure**

1. Log in and idle.
2. Check timeout.
3. Log in from 3 places.
4. Revoke a session centrally.
5. Check behaviour after password reset or role change.

**Edge Cases / Variants.** Session on a shared kiosk; token theft.

**Expected Detection.** Timeouts enforced; third session handled per policy; central revocation immediate; role change forces re-evaluation.

**Expected Prevention / Control Action.** Enforce.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Session events.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Test results.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-021"></a>

### TC-L09-021: Access Reviews and Recertification for AI Access

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Entitlements accumulate unless periodically reviewed.

**Business Scenario.** Audit wants regular review of who and what can use AI services and data.

**Technical Scenario.** Run a review campaign on the lab dataset.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** 50 entitlements including 10 stale, 5 excessive; 3 reviewers.

**Procedure**

1. Create campaign.
2. Assign reviewers.
3. Reviewers approve or revoke.
4. Check the enforcement of revocations.
5. Check reports for audit.

**Edge Cases / Variants.** Reviewer is the entitlement owner.

**Expected Detection.** Stale and excessive items highlighted; revocations enforced; report produced.

**Expected Prevention / Control Action.** Revoke.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Report export.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Campaign evidence.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l09-022"></a>

### TC-L09-022: Effective Permissions Visibility for Users and Agents

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D5 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Nobody can protect what they cannot see; effective access combines roles, groups, tokens and inheritance.

**Business Scenario.** Security wants one view of what a user or agent can really reach.

**Technical Scenario.** Query effective access for known identities and compare to ground truth.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** 8 identities (4 users, 4 agents) with known effective access to 12 resources.

**Procedure**

1. Query effective permissions.
2. Compare with ground truth.
3. Introduce an indirect path (group nesting).
4. Re-query.
5. Check export and risk highlighting.

**Edge Cases / Variants.** Conditional access; time-bound grants.

**Expected Detection.** At least 90 percent of access paths correct; indirect paths shown; export available.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Export for IAM tools.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Comparison table.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l09-023"></a>

### TC-L09-023: Emergency (Break-Glass) Access Controls

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Break-glass accounts are essential and dangerous if unmonitored.

**Business Scenario.** Security wants emergency access controlled and loud.

**Technical Scenario.** Use a break-glass account and check monitoring.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** 1 break-glass account; alert recipients.

**Procedure**

1. Use the account.
2. Check alerting time.
3. Check session recording.
4. Check post-use review workflow and password reset.
5. Try the account without justification.

**Edge Cases / Variants.** Account used from an unusual location.

**Expected Detection.** Alert within 5 minutes; actions logged; review workflow triggered.

**Expected Prevention / Control Action.** Alert.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Alerts to SIEM and pager.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Alert timeline.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-024"></a>

### TC-L09-024: Mutual Authentication Between AI Components

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D3, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A, P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Unauthenticated internal calls let an attacker on the network impersonate any component.

**Business Scenario.** Architecture wants workload identity and mutual TLS between model, gateway, retrieval and tools.

**Technical Scenario.** Test connections between components with and without valid identity.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** Components: gateway, orchestrator, vector store, tool server; test client with invalid and valid certificates.

**Procedure**

1. Scan connections.
2. Attempt calls without certificates.
3. With expired certificate.
4. With certificate for the wrong workload.
5. Check findings for components lacking mutual authentication.

**Edge Cases / Variants.** Certificate rotation during traffic.

**Expected Detection.** All unauthenticated and invalid calls rejected; weak components reported.

**Expected Prevention / Control Action.** Reject.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to ticketing.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Test log.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-025"></a>

### TC-L09-025: Identity Audit Trail: Who, What and On Whose Behalf

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D5, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Investigations need to know which user, which agent and which tool were behind each action.

**Business Scenario.** Audit wants complete attribution in every record.

**Technical Scenario.** Run a task across a user, an agent, two tools and a downstream system and trace it.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab identity provider and directory with fabricated users and groups; lab secret store; mock AI services and agents using test credentials only; no production identities or secrets connected.

**Test Data.** 1 task with 10 actions across 4 systems.

**Procedure**

1. Run the task.
2. Collect records from the platform and downstream systems.
3. Reconstruct the chain.
4. Check presence of user, agent, tool, resource, decision and time.
5. Check clock alignment and log integrity.

**Edge Cases / Variants.** Task triggered by a schedule; delegated chain of three agents.

**Expected Detection.** At least 9 of 10 actions fully attributable; integrity protection present.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Export in a common event format.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Chain reconstruction.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l09-026"></a>

### TC-L09-026: Coding Agent Repository and Cloud Credentials: Scope and Lifetime

| Field | Value |
|---|---|
| **Lifecycle Layer** | L09 Identity & Access Mgmt |
| **Use-Case Domain(s)** | D2, D5 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, A |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Coding agents are often given a developer's personal access token or cloud profile, granting far more than the task needs for far longer than the task lasts.

**Business Scenario.** Engineering wants coding agents to operate with short-lived tokens limited to the repository and actions in the task.

**Technical Scenario.** Give a coding agent broad and then narrow credentials, test which out-of-scope actions succeed, and review what is reported.

**Preconditions.** Isolated PoC lab provisioned; lab identity provider, directory, secret store and mock AI services seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab source-control server with 3 repositories and a protected main branch; lab cloud account with 2 roles.

**Test Data.** 1 long-lived broad token; 1 short-lived token scoped to one repository with read and pull-request rights; 6 out-of-scope actions (push to protected branch, read a second repository, delete a branch, change repository settings, read a cloud secret, create a cloud resource).

**Procedure**

1. Run the agent with the broad token and check whether the platform reports over-privilege.
2. Switch to the scoped token.
3. Attempt the 6 out-of-scope actions.
4. Wait for token expiry and retry one in-scope action.
5. Review attribution for every attempt.

**Edge Cases / Variants.** Token inherited from the developer's credential helper; token written to agent logs or memory.

**Expected Detection.** The broad token is flagged as over-privileged with its scopes listed; 6 of 6 out-of-scope attempts logged with agent identity and the user it acts for.

**Expected Prevention / Control Action.** 6 of 6 out-of-scope actions denied; the expired token is rejected.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Identity finding or access decision visible in the identity or access dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to ticketing.

**Forensic Evidence.** Identity (user, agent, service), token or key identifier, scope, resource, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Token scope report; denial log; expiry test result.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---
