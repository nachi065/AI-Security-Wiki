---
title: "L04 Human Interaction Layer"
author: Nachiket Sathaye
parent: "Test Case Library"
nav_order: 7
---

<a id="top"></a>

# L04 Human Interaction Layer

**Primary test focus:** browser/workforce AI, user coaching, approval prompts, multimodal input

**Controls tested:** [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) AI Discovery (12 cases), [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) Policy Enforcement (8 cases), [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002) Prompt Inspection (4 cases), [AI-CTRL-003](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-003) File Upload Protection (3 cases), [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004) IDE AI Governance (3 cases), [AI-CTRL-021](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-021) Multimodal and Voice Input Security (3 cases), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) AI Risk Assessment and Exception Management (3 cases), [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006) Agent Governance (1 case), [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) AI Policy, Roles and Acceptable Use (1 case), [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) Privacy and Regulatory Compliance (1 case), [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity (1 case)

**Cases:** 32 (TC-L04-001 to TC-L04-032)
> **Safety boundary.** All test cases in this layer use synthetic, non-functional or clearly marked test data only. Card numbers must come from published test ranges; keys, identifiers and records must be fabricated.

> **Verify before use.** MITRE ATLAS, OWASP LLM and NIST AI RMF identifiers must be checked against the current published versions. Numeric thresholds are starting values to tune. See the [Reference Index](00-reference-index.md) for field definitions and applicability codes.

## Cases in this layer

| ID | Title | Severity | Method | Domain(s) | Controls |
|---|---|---|---|---|---|
| [TC-L04-001](#tc-l04-001) | Unsanctioned Public AI Web Tool Discovery | Medium | Technical | D1 | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) |
| [TC-L04-002](#tc-l04-002) | AI Browser Extension Discovery | High | Technical | D1 | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) |
| [TC-L04-003](#tc-l04-003) | AI Usage Attribution by Department | High | Technical | D1 | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) |
| [TC-L04-004](#tc-l04-004) | AI Usage Attribution by User Group | Critical | Technical | D1 | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) |
| [TC-L04-005](#tc-l04-005) | AI Usage by Device Type and Management Status | High | Technical | D1 | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) |
| [TC-L04-006](#tc-l04-006) | AI Usage by Network Path | High | Technical | D1 | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) |
| [TC-L04-007](#tc-l04-007) | Discovery from Existing Proxy/SWG Logs | Medium | Technical | D1 | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) |
| [TC-L04-008](#tc-l04-008) | Off-Network Endpoint Usage Reporting | High | Technical | D1 | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) |
| [TC-L04-009](#tc-l04-009) | Personal vs Corporate Account Detection on the Same AI Service | Critical | Technical | D1, D6 | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001), [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) |
| [TC-L04-010](#tc-l04-010) | Native Browser-Embedded AI Assistant Detection | High | Technical | D1 | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) |
| [TC-L04-011](#tc-l04-011) | Real-Time Coaching Banner on Unsanctioned Tool | Medium | Technical | D1 | [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010), [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) |
| [TC-L04-012](#tc-l04-012) | Content-Aware Warning on Sensitive Paste | High | Technical | D1, D6 | [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010), [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002) |
| [TC-L04-013](#tc-l04-013) | Business Justification Workflow (Justify and Proceed) | Medium | Evidence | D1 | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) |
| [TC-L04-014](#tc-l04-014) | Approval Workflow for AI Access Exceptions | High | Evidence | D1 | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) |
| [TC-L04-015](#tc-l04-015) | Time-Bound Exception Expiry Enforcement | Medium | Technical | D1 | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) |
| [TC-L04-016](#tc-l04-016) | Block with Redirect to Sanctioned Alternative | Medium | Technical | D1 | [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) |
| [TC-L04-017](#tc-l04-017) | Sensitive Text Paste into Web AI Prompt: Monitor vs Block | Critical | Technical | D1, D6 | [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002) |
| [TC-L04-018](#tc-l04-018) | File Upload to AI Web Tool: Classified File Detection | Critical | Technical | D1, D6 | [AI-CTRL-003](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-003) |
| [TC-L04-019](#tc-l04-019) | Source Code Snippet Paste or Drag-and-Drop | High | Technical | D1, D2 | [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002), [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004) |
| [TC-L04-020](#tc-l04-020) | Screenshot and Image Upload with Sensitive Content | High | Technical | D1, D6 | [AI-CTRL-021](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-021), [AI-CTRL-003](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-003) |
| [TC-L04-021](#tc-l04-021) | Voice and Audio Input to AI Tools | Medium | Technical | D1 | [AI-CTRL-021](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-021) |
| [TC-L04-022](#tc-l04-022) | Hidden Text and Metadata in Uploaded Documents | High | Technical | D1, D6 | [AI-CTRL-003](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-003), [AI-CTRL-021](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-021) |
| [TC-L04-023](#tc-l04-023) | Browser-Based AI Agent (Computer-Use) Activity Detection | Critical | Technical | D1, D5 | [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006) |
| [TC-L04-024](#tc-l04-024) | Mobile and BYOD AI App Visibility | High | Technical | D1 | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) |
| [TC-L04-025](#tc-l04-025) | Unmanaged Device Access to Sanctioned AI Tools | High | Technical | D1, D6 | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001), [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) |
| [TC-L04-026](#tc-l04-026) | User Risk Scoring from Repeated AI Policy Violations | Medium | Evidence | D1, D6 | [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) |
| [TC-L04-027](#tc-l04-027) | Privacy Controls on User-Level AI Activity Data | High | Evidence | D1, D7 | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) |
| [TC-L04-028](#tc-l04-028) | Arabic and Mixed-Language Prompt Handling | High | Technical | D1, D7 | [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002) |
| [TC-L04-029](#tc-l04-029) | Differential Policy Enforcement by Group | High | Technical | D1 | [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) |
| [TC-L04-030](#tc-l04-030) | Shared or Generic Account Use of AI Tools | Medium | Technical | D1 | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) |
| [TC-L04-031](#tc-l04-031) | IDE Chat Prompt Containing Proprietary Source Code: Monitor vs Block | Critical | Technical | D2, D6 | [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004) |
| [TC-L04-032](#tc-l04-032) | Developer Coaching and Justification Inside the IDE | Medium | Technical | D2 | [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004) |

---

## Test cases

<a id="tc-l04-001"></a>

### TC-L04-001: Unsanctioned Public AI Web Tool Discovery

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, G \| Partial: P |
| **Risk Severity** | Medium |
| **Quick-Start Scenario** | [AI-POC-BR-005](../06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md#browser-ai-test-cases) |
| **MITRE ATLAS Mapping** | N/A (visibility control); Reconnaissance/Discovery context only |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (unmanaged AI components) |
| **NIST AI RMF Mapping** | MAP 1.1; GOVERN 6.1 |
| **Control(s) Tested** | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) AI Discovery |

**Risk Addressed.** Public AI web tools that bypassed procurement and security review are an unmanaged data-exposure surface.

**Business Scenario.** Security must identify which public AI tools staff use that are not on the approved list.

**Technical Scenario.** Test accounts browse to 3 public AI web tools absent from the approved list; the platform must classify each as unsanctioned.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 3 unapproved public AI tools; 5 test accounts; approved-list file loaded in the platform.

**Procedure**

1. Access each tool from a monitored endpoint, 3 times each.
2. Wait for the documented detection SLA.
3. Compare flagged tools against the seeded ground truth.

**Expected Detection.** All 3 tools flagged as unsanctioned on every access, separate from the sanctioned inventory.

**Expected Prevention / Control Action.** Optional warning banner per configured policy.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Unsanctioned list feeds the Shadow AI view and any exportable report.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Alert/inventory export; raw log line per access; timestamp delta between action and detection.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-002"></a>

### TC-L04-002: AI Browser Extension Discovery

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E \| Partial: P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (visibility control); Reconnaissance/Discovery context only |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (unmanaged AI components) |
| **NIST AI RMF Mapping** | MAP 1.1; GOVERN 6.1 |
| **Control(s) Tested** | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) AI Discovery |

**Risk Addressed.** AI browser extensions can read page content, including sensitive data, outside normal DLP visibility.

**Business Scenario.** Security needs a list of AI-related extensions installed across managed browsers, with versions.

**Technical Scenario.** Install 3 test AI extensions (summariser, writing assistant, chat sidebar) on 5 test endpoints and confirm inventory.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 3 test extensions across 5 endpoints; mix of Chrome and Edge profiles.

**Procedure**

1. Install extensions.
2. Run or await discovery.
3. Verify name, version, permissions and endpoint for each install.
4. Remove one extension and confirm the inventory updates.

**Expected Detection.** All 3 extensions detected on all 5 endpoints with correct name, version and requested permissions; removal reflected within SLA.

**Expected Prevention / Control Action.** Ability to flag or block non-approved extensions per policy.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Inventory correlates to MDM/EDR asset records.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Inventory export; permission list screenshot; before/after removal log entries.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-003"></a>

### TC-L04-003: AI Usage Attribution by Department

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, G \| Partial: P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (visibility control); Reconnaissance/Discovery context only |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (unmanaged AI components) |
| **NIST AI RMF Mapping** | MAP 1.1; GOVERN 6.1 |
| **Control(s) Tested** | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) AI Discovery |

**Risk Addressed.** Without a departmental breakdown, AI risk cannot be prioritised or routed to the right business owner.

**Business Scenario.** Business-unit leaders need AI usage by department to focus governance effort.

**Technical Scenario.** 15 test accounts tagged to 3 directory departments generate a known mix of sanctioned and unsanctioned usage.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 15 accounts (5 per department); scripted usage counts per account.

**Procedure**

1. Generate the scripted usage.
2. Pull the departmental report.
3. Compare each department against ground truth.

**Expected Detection.** Departmental counts match ground truth within 5% variance.

**Expected Prevention / Control Action.** N/A (visibility control).

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Departmental data exportable to the executive dashboard or BI tool.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Report export; ground-truth sheet; variance calculation.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-004"></a>

### TC-L04-004: AI Usage Attribution by User Group

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, G \| Partial: P |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | N/A (visibility control); Reconnaissance/Discovery context only |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (unmanaged AI components) |
| **NIST AI RMF Mapping** | MAP 1.1; GOVERN 6.1 |
| **Control(s) Tested** | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) AI Discovery |

**Risk Addressed.** Risk differs sharply between groups (finance, engineering, contractors); group-level visibility enables targeted policy.

**Business Scenario.** Security needs usage segmented by IdP security group and role.

**Technical Scenario.** Test accounts in 2 distinct IdP groups generate usage; the platform must attribute by group membership, including after a group change.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 10 accounts across 2 groups; 1 account moved between groups mid-test.

**Procedure**

1. Generate usage.
2. Pull the group report.
3. Move one account to the other group and repeat.
4. Validate against membership ground truth.

**Expected Detection.** Group counts match ground truth; moved account attributed to the new group for new sessions only.

**Expected Prevention / Control Action.** N/A (visibility control).

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Group data correlates to IAM/IdP group definitions.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Group report before and after the move; IdP membership export.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-005"></a>

### TC-L04-005: AI Usage by Device Type and Management Status

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E \| Partial: G |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (visibility control); Reconnaissance/Discovery context only |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (unmanaged AI components) |
| **NIST AI RMF Mapping** | MAP 1.1; GOVERN 6.1 |
| **Control(s) Tested** | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) AI Discovery |

**Risk Addressed.** Managed laptops, unmanaged personal devices and mobiles carry materially different risk.

**Business Scenario.** Security must tell AI use from managed, unmanaged and mobile devices apart.

**Technical Scenario.** Generate usage from 1 managed laptop, 1 unmanaged laptop and 1 mobile device.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 3 devices with known management status.

**Procedure**

1. Access the same AI tool from each device.
2. Check device type and management flag per session.

**Expected Detection.** Device type and management status correct for all 3 sessions.

**Expected Prevention / Control Action.** N/A (feeds policy decisions elsewhere).

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Attribution correlates with MDM/UEM inventory.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Session records showing device attributes; MDM export.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-006"></a>

### TC-L04-006: AI Usage by Network Path

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E \| Partial: G |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (visibility control); Reconnaissance/Discovery context only |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (unmanaged AI components) |
| **NIST AI RMF Mapping** | MAP 1.1; GOVERN 6.1 |
| **Control(s) Tested** | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) AI Discovery |

**Risk Addressed.** Usage from outside the corporate perimeter may bypass inline controls.

**Business Scenario.** Security must know whether AI use occurs on LAN, VPN or an external network.

**Technical Scenario.** 1 test account uses AI tools over on-premises LAN, corporate VPN and an unmanaged external network.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 1 account; 3 network paths.

**Procedure**

1. Access AI tools over each path.
2. Confirm path attribution per session.

**Expected Detection.** Network path correct for all sessions.

**Expected Prevention / Control Action.** N/A (visibility control).

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Path data correlates to SASE/VPN logs.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Session logs with path field; VPN log extract.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-007"></a>

### TC-L04-007: Discovery from Existing Proxy/SWG Logs

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, P \| Partial: E |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (visibility control); Reconnaissance/Discovery context only |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (unmanaged AI components) |
| **NIST AI RMF Mapping** | MAP 1.1; GOVERN 6.1 |
| **Control(s) Tested** | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) AI Discovery |

**Risk Addressed.** Proxy telemetry already exists; the platform should use it rather than demand a parallel data path.

**Business Scenario.** Security wants AI discovery from current proxy logs without new infrastructure.

**Technical Scenario.** Ingest a proxy log sample containing known AI domains.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** Log sample with 5 known AI-tool domain accesses and 20 unrelated entries.

**Procedure**

1. Ingest the sample.
2. Verify extraction and classification of every AI access.
3. Check that unrelated entries produce no AI findings.

**Expected Detection.** All 5 AI accesses identified and classified; zero false positives from unrelated entries.

**Expected Prevention / Control Action.** N/A (visibility control).

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Confirms ingestion works with no additional agent.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Ingestion job log; classified results; false-positive count.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-008"></a>

### TC-L04-008: Off-Network Endpoint Usage Reporting

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (visibility control); Reconnaissance/Discovery context only |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (unmanaged AI components) |
| **NIST AI RMF Mapping** | MAP 1.1; GOVERN 6.1 |
| **Control(s) Tested** | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) AI Discovery |

**Risk Addressed.** Endpoint-level visibility catches AI use that never crosses a monitored network.

**Business Scenario.** Security wants evidence that agent-based discovery works independent of location and reports on reconnect.

**Technical Scenario.** Use a local AI app on an agent-equipped endpoint while disconnected, then reconnect.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 1 endpoint with agent; 1 local AI application.

**Procedure**

1. Disconnect the endpoint from the corporate network.
2. Use the local AI app.
3. Reconnect and wait for sync.
4. Confirm the offline usage is reported with correct timestamps.

**Expected Detection.** Offline usage reported after reconnect, with original timestamps preserved.

**Expected Prevention / Control Action.** N/A (visibility control).

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Agent telemetry correlates with EDR data.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Agent queue log; reported event with original and received timestamps.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-009"></a>

### TC-L04-009: Personal vs Corporate Account Detection on the Same AI Service

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1, D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, G |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage (secondary) |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; GOVERN 1.1 |
| **Control(s) Tested** | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) AI Discovery; [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) Policy Enforcement |

**Risk Addressed.** Data pasted into a personal tenant of an approved service leaves corporate control even though the service itself is sanctioned.

**Business Scenario.** Security must distinguish corporate-tenant from personal-account use of the same AI service.

**Technical Scenario.** Sign in to one AI service first with a corporate SSO identity, then with a personal account, and submit synthetic data in each.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 1 AI service with enterprise tenant; 1 personal test account; synthetic internal-labelled text.

**Procedure**

1. Use the corporate identity.
2. Use the personal account from the same endpoint.
3. Review tenant/account attribution for each session.

**Expected Detection.** The platform labels the corporate and personal sessions differently and flags the personal one per policy.

**Expected Prevention / Control Action.** Policy can block or warn on personal-account sessions.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Tenant restriction data correlates with IdP and SaaS admin logs.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Two session records with account-type field; policy screenshot.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-010"></a>

### TC-L04-010: Native Browser-Embedded AI Assistant Detection

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E \| Partial: G |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (visibility control); Reconnaissance/Discovery context only |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (unmanaged AI components) |
| **NIST AI RMF Mapping** | MAP 1.1; GOVERN 6.1 |
| **Control(s) Tested** | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) AI Discovery |

**Risk Addressed.** AI assistants built into browsers or operating systems may send page content to a provider without any separate install.

**Business Scenario.** Security must see use of built-in browser or OS AI features.

**Technical Scenario.** Enable the built-in AI assistant in a managed browser and summarise a test page.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 1 browser with built-in AI feature enabled; 1 internal-labelled test page.

**Procedure**

1. Enable the feature.
2. Invoke it on the test page.
3. Check discovery and the policy action.

**Expected Detection.** Feature use is detected and attributed to user and device, or the platform documents it as an unsupported channel.

**Expected Prevention / Control Action.** Ability to disable the feature by policy, or alert on its use.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Browser management policy state correlates with detection.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Detection record or documented limitation; browser policy export.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-011"></a>

### TC-L04-011: Real-Time Coaching Banner on Unsanctioned Tool

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, G |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) Policy Enforcement; [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) AI Policy, Roles and Acceptable Use |

**Risk Addressed.** Users who are told why a tool is risky and where to go instead change behaviour; silent blocking creates workarounds.

**Business Scenario.** Security wants a just-in-time message pointing to the sanctioned alternative.

**Technical Scenario.** Access an unsanctioned tool with coaching enabled and observe the message and click-through.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 2 unsanctioned tools; 1 sanctioned alternative with link; 5 test users.

**Procedure**

1. Configure the coaching message.
2. Access the tool as each user.
3. Check message display, link target and logged user response.

**Expected Detection.** Message shown on every access within seconds, linking to the sanctioned alternative; user action logged.

**Expected Prevention / Control Action.** Coaching without block (warn mode).

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Message content and response logged for reporting.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Screenshot of message; log of user action.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-012"></a>

### TC-L04-012: Content-Aware Warning on Sensitive Paste

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1, D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, G |
| **Risk Severity** | High |
| **Quick-Start Scenario** | [AI-POC-BR-002](../06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md#browser-ai-test-cases) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) Policy Enforcement; [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002) Prompt Inspection |

**Risk Addressed.** Generic warnings are ignored; warnings that name the detected data type are acted on.

**Business Scenario.** Security wants a warning that appears only when sensitive content is pasted into an AI prompt.

**Technical Scenario.** Paste synthetic confidential text into a sanctioned and an unsanctioned AI prompt and observe the warning.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** Synthetic text labelled Confidential; neutral text for control.

**Procedure**

1. Paste neutral text and confirm no warning.
2. Paste the labelled text and confirm a warning naming the data type.
3. Record the user choice.

**Expected Detection.** Warning appears only for the sensitive paste, names the detected category, and logs the user decision.

**Expected Prevention / Control Action.** Warn and allow, or block, per policy.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Event includes classification label and user decision.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Warning screenshot; event log including decision field.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-013"></a>

### TC-L04-013: Business Justification Workflow (Justify and Proceed)

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: E, G |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) AI Risk Assessment and Exception Management; [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) Policy Enforcement |

**Risk Addressed.** Without recorded justification, risk acceptance by individual users is unauditable.

**Business Scenario.** Governance wants users to give a reason when proceeding past a warning, and the reason retained.

**Technical Scenario.** User overrides a warning by entering a justification; the platform stores it with the event.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 3 test users; 3 justification texts including one blank attempt.

**Procedure**

1. Trigger a justify-and-proceed prompt.
2. Submit a reason, then try a blank reason.
3. Retrieve the justification from logs and reports.

**Expected Detection.** Blank reason rejected; entered reasons stored against user, event and time.

**Expected Prevention / Control Action.** Proceed only after valid justification.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Justifications exportable for audit or GRC tooling.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Export of justification records; blank-submit screenshot.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l04-014"></a>

### TC-L04-014: Approval Workflow for AI Access Exceptions

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: E, G \| Partial: P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) AI Risk Assessment and Exception Management |

**Risk Addressed.** Ad-hoc exceptions granted over chat leave no audit trail and are rarely revoked.

**Business Scenario.** Governance wants exception requests routed to a manager or data owner and recorded.

**Technical Scenario.** User requests access to a blocked AI tool; the approver approves or rejects in the workflow.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 2 requests: 1 to approve, 1 to reject; named test approver.

**Procedure**

1. Submit both requests.
2. Approve one and reject one.
3. Re-test access for both users.
4. Review the audit trail.

**Expected Detection.** Approved user gains access, rejected user does not; approver, time and decision logged.

**Expected Prevention / Control Action.** Access changes only after approval.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Workflow integrates with ticketing or IdP approval where supported.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Workflow audit trail export; before/after access test results.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l04-015"></a>

### TC-L04-015: Time-Bound Exception Expiry Enforcement

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, G |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) AI Risk Assessment and Exception Management |

**Risk Addressed.** Permanent exceptions accumulate and silently widen the exposure surface.

**Business Scenario.** Governance wants exceptions to expire automatically.

**Technical Scenario.** Grant a 1-hour exception, use the tool inside the window, then again after expiry.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 1 user; 1 blocked tool; exception of 1 hour.

**Procedure**

1. Grant the exception.
2. Access inside the window.
3. Access after expiry.
4. Check expiry logging.

**Expected Detection.** Access allowed inside the window and blocked after expiry; expiry event logged.

**Expected Prevention / Control Action.** Automatic revoke at expiry.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Expiry events visible in the exception register.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Timestamped access logs either side of expiry.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-016"></a>

### TC-L04-016: Block with Redirect to Sanctioned Alternative

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, G |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) Policy Enforcement |

**Risk Addressed.** Hard blocks without an alternative push users to personal devices.

**Business Scenario.** Security wants blocked users sent to the approved tool.

**Technical Scenario.** Access a blocked public tool and confirm the block page offers the sanctioned alternative.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 1 blocked tool; 1 sanctioned alternative.

**Procedure**

1. Access the blocked tool.
2. Confirm block and redirect link.
3. Follow the link and confirm it opens the sanctioned tool.

**Expected Detection.** Access blocked; redirect link correct and working; block event logged.

**Expected Prevention / Control Action.** Block with redirect.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Block events appear in the Shadow AI report.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Block page screenshot; log entry.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-017"></a>

### TC-L04-017: Sensitive Text Paste into Web AI Prompt: Monitor vs Block

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1, D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, G |
| **Risk Severity** | Critical |
| **Quick-Start Scenario** | [AI-POC-BR-002](../06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md#browser-ai-test-cases) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002) Prompt Inspection |

**Risk Addressed.** Pasted confidential text is the most common route of leakage to public AI tools.

**Business Scenario.** Security wants to compare monitor-only and block outcomes for the same paste.

**Technical Scenario.** Paste synthetic labelled data into a web AI prompt under monitor mode, then enforce mode.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 5 synthetic confidential snippets (customer record, contract clause, HR note, price list, board paragraph).

**Procedure**

1. Run all 5 pastes in monitor mode.
2. Switch to enforce mode and repeat.
3. Compare results.

**Expected Detection.** All 5 snippets detected in both modes; in monitor mode, logged; in enforce mode, blocked.

**Expected Prevention / Control Action.** Block in enforce mode; allow-and-log in monitor mode.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events carry classification and rule that fired.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Event exports for both modes; policy mode screenshot.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-018"></a>

### TC-L04-018: File Upload to AI Web Tool: Classified File Detection

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1, D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, G |
| **Risk Severity** | Critical |
| **Quick-Start Scenario** | [AI-POC-BR-001](../06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md#browser-ai-test-cases), [AI-POC-BR-004](../06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md#browser-ai-test-cases) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-003](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-003) File Upload Protection |

**Risk Addressed.** Uploads move whole documents in one action.

**Business Scenario.** Security wants uploads of labelled files to AI tools detected and controlled.

**Technical Scenario.** Upload files carrying sensitivity labels and fingerprints to a web AI tool.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 4 synthetic files: labelled DOCX, labelled PDF, unlabelled but fingerprinted XLSX, clean TXT.

**Procedure**

1. Upload each file.
2. Compare detection result to expected.
3. Confirm clean file passes.

**Expected Detection.** 3 sensitive files detected and the clean file passes; reason for each decision logged.

**Expected Prevention / Control Action.** Block or warn per policy for sensitive files.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Detection uses labels from the classification platform where integrated.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Per-file event with filename hash, label, action.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-019"></a>

### TC-L04-019: Source Code Snippet Paste or Drag-and-Drop

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1, D2 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, G |
| **Risk Severity** | High |
| **Quick-Start Scenario** | [AI-POC-BR-003](../06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md#browser-ai-test-cases) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002) Prompt Inspection; [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004) IDE AI Governance |

**Risk Addressed.** Source code pasted into public AI tools can expose proprietary logic and embedded secrets.

**Business Scenario.** Security wants code leaving through the browser detected.

**Technical Scenario.** Paste and drag-drop synthetic proprietary code snippets into a web AI prompt.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 3 synthetic code snippets: one with a fake API key, one with an internal hostname, one generic.

**Procedure**

1. Paste each snippet.
2. Drag-drop a code file.
3. Check detection of secret and internal markers.

**Expected Detection.** Snippets with secret and internal markers detected; generic snippet handled per policy; both paste and drag-drop covered.

**Expected Prevention / Control Action.** Block or redact for secret-bearing snippets.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events tagged with repo or project metadata if available.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Event records for each input route.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-020"></a>

### TC-L04-020: Screenshot and Image Upload with Sensitive Content

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1, D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, G \| Partial: A |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-021](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-021) Multimodal and Voice Input Security; [AI-CTRL-003](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-003) File Upload Protection |

**Risk Addressed.** Images bypass text-only DLP; screenshots of dashboards or documents leak data directly.

**Business Scenario.** Security wants image uploads to AI tools inspected for sensitive text.

**Technical Scenario.** Upload synthetic screenshots containing fake customer data to a web AI tool.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 3 images: screenshot with fake Emirates-ID-format number, photographed document, clean image.

**Procedure**

1. Upload each image.
2. Compare detection to expectation.
3. Note processing delay.

**Expected Detection.** Sensitive images detected via OCR or equivalent; clean image passes; delay recorded.

**Expected Prevention / Control Action.** Block or warn per policy.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Event carries detection method (OCR/classifier).

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Event records; processing delay measurements.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-021"></a>

### TC-L04-021: Voice and Audio Input to AI Tools

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1 |
| **Test Method** | Technical |
| **Vendor Applicability** | Partial: E, G \| Core: A |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-021](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-021) Multimodal and Voice Input Security |

**Risk Addressed.** Voice input to AI assistants is rarely covered by prompt-inspection controls.

**Business Scenario.** Security needs to know whether voice-mode AI use is detected or controlled.

**Technical Scenario.** Use voice mode in a test AI assistant, speaking synthetic sensitive phrases.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 1 voice-capable AI tool; 3 scripted spoken phrases.

**Procedure**

1. Use voice mode.
2. Check whether the session is detected.
3. Check whether content inspection occurs or is documented as unsupported.

**Expected Detection.** Session detected and attributed; content inspection either works or the limitation is documented in writing.

**Expected Prevention / Control Action.** Ability to block voice mode by policy.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Detection record or written limitation statement.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Event record; vendor limitation statement if applicable.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-022"></a>

### TC-L04-022: Hidden Text and Metadata in Uploaded Documents

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1, D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, G \| Partial: A |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0051 LLM Prompt Injection |
| **OWASP LLM / GenAI Mapping** | LLM01:2025 Prompt Injection |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-003](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-003) File Upload Protection; [AI-CTRL-021](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-021) Multimodal and Voice Input Security |

**Risk Addressed.** Hidden text, comments and metadata can carry sensitive data or injected instructions that users never see.

**Business Scenario.** Security wants documents inspected beyond visible text.

**Technical Scenario.** Upload documents with sensitive data in hidden text, comments and metadata.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 3 synthetic files: white-on-white text, tracked comment, EXIF metadata.

**Procedure**

1. Upload each file.
2. Check detection for each hiding method.

**Expected Detection.** Hidden sensitive content detected in at least 2 of 3 methods, with gaps documented.

**Expected Prevention / Control Action.** Block or warn per policy.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Event identifies the location of the match.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Event details; documented gap list.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-023"></a>

### TC-L04-023: Browser-Based AI Agent (Computer-Use) Activity Detection

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1, D5 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E \| Partial: G |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | N/A (visibility control); Reconnaissance/Discovery context only |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (unmanaged AI components) |
| **NIST AI RMF Mapping** | MAP 1.1; GOVERN 6.1 |
| **Control(s) Tested** | [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006) Agent Governance |

**Risk Addressed.** Browser agents act with the user's session and can read or submit data without per-step user awareness.

**Business Scenario.** Security must see when an AI agent drives a browser session on a user's behalf.

**Technical Scenario.** Run a test browser agent that fills a form and reads a page in the user's session.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 1 test browser agent; internal test form; 1 test user session.

**Procedure**

1. Start the agent task.
2. Check detection of agent-driven actions versus human actions.
3. Review attribution.

**Expected Detection.** Agent-driven session identified as non-human activity and linked to the user and agent product.

**Expected Prevention / Control Action.** Policy to restrict agent use on sensitive domains.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events link to identity and endpoint records.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Event records distinguishing agent from human actions.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-024"></a>

### TC-L04-024: Mobile and BYOD AI App Visibility

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E (mobile) \| Partial: G, P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (visibility control); Reconnaissance/Discovery context only |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (unmanaged AI components) |
| **NIST AI RMF Mapping** | MAP 1.1; GOVERN 6.1 |
| **Control(s) Tested** | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) AI Discovery |

**Risk Addressed.** Personal and mobile devices are a major route for AI use outside inline controls.

**Business Scenario.** Security wants visibility into AI app use from mobile and BYOD devices.

**Technical Scenario.** Use 3 AI mobile apps on an enrolled and a non-enrolled phone.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 2 phones; 3 AI mobile apps.

**Procedure**

1. Use the apps on each phone.
2. Check which sessions are visible.
3. Document coverage gaps.

**Expected Detection.** Enrolled phone sessions detected; non-enrolled gaps documented in writing.

**Expected Prevention / Control Action.** Per MDM/MAM policy where integrated.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Correlates with MDM/MAM enrolment status.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Event records; written coverage statement.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-025"></a>

### TC-L04-025: Unmanaged Device Access to Sanctioned AI Tools

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1, D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G \| Partial: E |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) AI Discovery; [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) Policy Enforcement |

**Risk Addressed.** Sanctioned AI tools reached from unmanaged devices can let data be copied out of reach of endpoint controls.

**Business Scenario.** Security wants limited or session-controlled access from unmanaged devices.

**Technical Scenario.** Access a sanctioned AI tool from an unmanaged browser and attempt copy, download and upload.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 1 unmanaged device; 1 sanctioned AI tool; synthetic data.

**Procedure**

1. Access the tool.
2. Attempt copy/paste, download and upload.
3. Review which actions are restricted.

**Expected Detection.** Session restrictions apply per policy and are logged; unrestricted actions documented.

**Expected Prevention / Control Action.** Browser isolation, restricted actions or deny per policy.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Device posture signal from IdP or MDM.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Policy screenshot; action-level logs.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-026"></a>

### TC-L04-026: User Risk Scoring from Repeated AI Policy Violations

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1, D6 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: E, G \| Partial: P |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |
| **Control(s) Tested** | [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) Policy Enforcement |

**Risk Addressed.** Repeated risky behaviour by one user is a better signal than any single event.

**Business Scenario.** Security wants users ranked by AI-related risk behaviour.

**Technical Scenario.** Generate repeated violations from 2 test users and a clean baseline from a third.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 3 users; scripted violation counts (10, 3, 0).

**Procedure**

1. Generate events.
2. Open the user risk view.
3. Compare ranking with scripted counts.

**Expected Detection.** Ranking matches the scripted order; scoring factors are visible.

**Expected Prevention / Control Action.** N/A (analytics).

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Risk score exportable to SIEM or insider-risk tooling.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Risk view screenshot; export; factor explanation.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l04-027"></a>

### TC-L04-027: Privacy Controls on User-Level AI Activity Data

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1, D7 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: E, G, P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage (secondary) |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; GOVERN 1.1 |
| **Control(s) Tested** | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) Privacy and Regulatory Compliance |

**Risk Addressed.** Detailed per-user prompt monitoring may breach employment, works-council or UAE privacy expectations if left unrestricted.

**Business Scenario.** Legal and HR want user identities pseudonymised by default and unmasked only for authorised investigators.

**Technical Scenario.** Review user identity handling in dashboards and log exports under two admin roles.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 2 admin roles (analyst, investigator); 5 test users.

**Procedure**

1. View dashboards as analyst.
2. View as investigator.
3. Test the unmask action and its audit log.

**Expected Detection.** Analyst sees pseudonymised users; investigator can unmask with a logged reason.

**Expected Prevention / Control Action.** Role-based unmask control.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Audit entries exportable to SIEM.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Role comparison screenshots; unmask audit log.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l04-028"></a>

### TC-L04-028: Arabic and Mixed-Language Prompt Handling

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, G, A |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002) Prompt Inspection |

**Risk Addressed.** Classifiers trained mainly on English can miss sensitive content in Arabic or mixed-script prompts.

**Business Scenario.** Security needs consistent detection for Arabic and English-Arabic prompts.

**Technical Scenario.** Submit synthetic sensitive content in Arabic, English and mixed text.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 9 prompts: 3 each Arabic, English, mixed; same sensitive categories.

**Procedure**

1. Submit all prompts.
2. Compare detection rates by language.
3. Record misses.

**Expected Detection.** Detection rate in Arabic and mixed text within 10 percentage points of English.

**Expected Prevention / Control Action.** Policy action applies equally across languages.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Event records include detected language.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Per-language detection table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-029"></a>

### TC-L04-029: Differential Policy Enforcement by Group

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, G |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) Policy Enforcement |

**Risk Addressed.** One policy for all staff is either too loose for finance or too tight for marketing.

**Business Scenario.** Governance wants different AI policies per user group.

**Technical Scenario.** Apply a stricter policy to a finance group and a lighter one to a general group, then test the same action.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 2 groups; 1 identical sensitive paste action.

**Procedure**

1. Configure both policies.
2. Run the same action as each user.
3. Check divergent outcomes.

**Expected Detection.** Finance user blocked and general user warned, per configuration; both logged with policy name.

**Expected Prevention / Control Action.** Per-group enforcement.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Group source is the IdP.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Policy configuration and two result records.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-030"></a>

### TC-L04-030: Shared or Generic Account Use of AI Tools

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D1 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, G \| Partial: P |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (visibility control); Reconnaissance/Discovery context only |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (unmanaged AI components) |
| **NIST AI RMF Mapping** | MAP 1.1; GOVERN 6.1 |
| **Control(s) Tested** | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity |

**Risk Addressed.** Shared logins make individual accountability for AI use impossible.

**Business Scenario.** Governance wants to detect AI tools accessed with shared or service-style accounts.

**Technical Scenario.** Two test users sign in to one AI tool using the same shared credential from different devices.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test.

**Test Data.** 1 shared test account; 2 devices; 2 users.

**Procedure**

1. Sign in from both devices.
2. Check whether sessions are attributed to the endpoint user, the shared account, or both.
3. Check for a shared-account flag.

**Expected Detection.** Both sessions attributed to the real endpoint user and flagged as shared-account use.

**Expected Prevention / Control Action.** Alert or block on shared-account use per policy.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Attribution uses endpoint or IdP identity.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Two session records with user and account fields.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-031"></a>

### TC-L04-031: IDE Chat Prompt Containing Proprietary Source Code: Monitor vs Block

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D2, D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, G |
| **Risk Severity** | Critical |
| **Quick-Start Scenario** | [AI-POC-ID-001](../06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md#ide-ai-test-cases) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004) IDE AI Governance |

**Risk Addressed.** Developers paste or attach proprietary code into an IDE assistant chat panel, a channel that browser-focused controls do not see.

**Business Scenario.** Engineering leadership wants assistants allowed for general coding while code from restricted repositories is kept out of prompts.

**Technical Scenario.** From the IDE chat panel, submit synthetic code marked proprietary by paste, by file attachment and by a selection-based action such as explain, under a monitor policy and then a block policy.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test. Two IDE families with an AI assistant extension installed on managed test workstations; fabricated repository tagged restricted.

**Test Data.** 3 synthetic source files carrying a proprietary header and a fingerprinted function; 1 clean open-source file as a control; 2 policies (monitor, block).

**Procedure**

1. Set the monitor policy and submit each proprietary file by paste, by attachment and by selection-based action (9 submissions).
2. Record what is logged for each submission.
3. Switch to the block policy and repeat the 9 submissions.
4. Submit the clean control file under both policies.
5. Check the developer-facing message and the administrator event for each block.

**Edge Cases / Variants.** Code split across several short prompts; inline completion context instead of chat; assistant running in a remote or container workspace.

**Expected Detection.** 9 of 9 proprietary submissions detected in both modes with IDE, extension, user and repository recorded; the control file is not flagged.

**Expected Prevention / Control Action.** Under the block policy the prompt does not leave the workstation or gateway, and the developer sees a reason and a policy reference.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events forwarded to the SIEM with repository and file identifiers.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Event export for all 18 proprietary submissions; block message screenshots; egress capture showing no blocked content was sent.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l04-032"></a>

### TC-L04-032: Developer Coaching and Justification Inside the IDE

| Field | Value |
|---|---|
| **Lifecycle Layer** | L04 Human Interaction Layer |
| **Use-Case Domain(s)** | D2 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004) IDE AI Governance |

**Risk Addressed.** A silent block inside an IDE looks like a tool failure, so developers move to unmanaged tools.

**Business Scenario.** Engineering and security want developers told why an action was stopped and offered a sanctioned route without leaving the editor.

**Technical Scenario.** Trigger warn, justify-and-proceed and block outcomes from inside the IDE and inspect what the developer sees and what is recorded.

**Preconditions.** Isolated PoC lab provisioned; test users, managed and unmanaged test endpoints and synthetic data seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform agent or integration installed for the channel under test. Coaching messages configured with a policy link and a sanctioned alternative; two IDE families with an AI assistant extension.

**Test Data.** 3 policies (warn, justify, block); 3 trigger prompts containing synthetic sensitive markers; 2 IDEs.

**Procedure**

1. Trigger each policy in each IDE (6 triggers).
2. Record where the message appears (chat panel, notification or status bar) and whether it names the policy.
3. Enter a justification and proceed.
4. Confirm the justification text is stored against the event with user and timestamp.
5. Repeat one trigger with the assistant in inline-completion mode.

**Edge Cases / Variants.** Workstation offline; localised message text; repeated triggers in one session.

**Expected Detection.** Each of the 6 triggers produces a visible, readable message in the IDE that names the policy; the justification is captured with user and timestamp.

**Expected Prevention / Control Action.** The block outcome stops the request; the justify outcome releases it only after text is entered.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Event visible in the workforce/Shadow AI dashboard within the documented refresh interval.

**Expected Integration Evidence.** Justifications exportable to ticketing or a GRC tool.

**Forensic Evidence.** Full session metadata (user, device, browser, destination, network path, timestamp and policy decision) exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Screenshot of each message; justification record export.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---
