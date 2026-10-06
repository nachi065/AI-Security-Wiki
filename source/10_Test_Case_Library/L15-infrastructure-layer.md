---
title: "L15 Infrastructure Layer"
author: Nachiket Sathaye
parent: "Test Case Library"
nav_order: 18
---

<a id="top"></a>

# L15 Infrastructure Layer

**Primary test focus:** GPU/cluster hardening, secrets, network segmentation, sovereignty of control plane

**Cases:** 20 (TC-L15-001 to TC-L15-020)
> **Safety boundary.** Infrastructure and SOC cases use a lab cluster, mock inference servers, a test cloud account and a lab SIEM and SOAR only. Probe and compromise-simulation scripts are harmless lab tools that only attempt connections and reads of canary resources. Never run them against production systems, and never connect lab alerting to production on-call routing. Cases marked Attestation rest on vendor documents and score below demonstrated evidence.

> **Verify before use.** MITRE ATLAS, OWASP LLM and NIST AI RMF identifiers must be checked against the current published versions. Numeric thresholds are starting values to tune. See the [Reference Index](00-reference-index.md) for field definitions and applicability codes.

## Cases in this layer

| ID | Title | Severity | Method | Domain(s) |
|---|---|---|---|---|
| [TC-L15-001](#tc-l15-001) | AI Infrastructure Asset Discovery | High | Technical | D4, D3 |
| [TC-L15-002](#tc-l15-002) | GPU Cluster Configuration Hardening | High | Technical | D4 |
| [TC-L15-003](#tc-l15-003) | GPU Multi-Tenancy Isolation and Memory Residue | Critical | Technical | D4, D6 |
| [TC-L15-004](#tc-l15-004) | Kubernetes Hardening for AI Workloads | High | Technical | D4, D3 |
| [TC-L15-005](#tc-l15-005) | Inference Server Hardening and Exposure | High | Technical | D3, D4 |
| [TC-L15-006](#tc-l15-006) | Network Segmentation Between AI Zones | Critical | Technical | D3, D7 |
| [TC-L15-007](#tc-l15-007) | Egress Control for AI Workloads | High | Technical | D4, D7 |
| [TC-L15-008](#tc-l15-008) | Lateral Movement Containment from a Compromised Inference Pod | Critical | Technical | D3, D5 |
| [TC-L15-009](#tc-l15-009) | Secrets Management for AI Infrastructure | Critical | Technical | D4 |
| [TC-L15-010](#tc-l15-010) | Cloud IAM Roles for AI Services and Metadata Service Protection | Critical | Technical | D4, D7 |
| [TC-L15-011](#tc-l15-011) | Model and Dataset Storage Security | Critical | Technical | D4, D6 |
| [TC-L15-012](#tc-l15-012) | Encryption and Confidential Computing Evidence | Medium | Evidence | D7 |
| [TC-L15-013](#tc-l15-013) | Control Plane and Data Plane Location Proof (Sovereignty) | Critical | Evidence | D7 |
| [TC-L15-014](#tc-l15-014) | Air-Gapped and On-Premise Operation | High | Technical | D7 |
| [TC-L15-015](#tc-l15-015) | Single-Tenant and Dedicated Deployment Evidence | High | Evidence | D7, D4 |
| [TC-L15-016](#tc-l15-016) | Hardening of the Evaluated Platform's Own Components | Critical | Technical | D7 |
| [TC-L15-017](#tc-l15-017) | Resource Quotas and Noisy-Neighbour Protection on Shared GPU Capacity | Medium | Technical | D4 |
| [TC-L15-018](#tc-l15-018) | Infrastructure Logging and Telemetry Coverage | High | Technical | D4, D7 |
| [TC-L15-019](#tc-l15-019) | Backup, Disaster Recovery and Restoration of AI Services | High | Technical | D3, D7 |
| [TC-L15-020](#tc-l15-020) | Hosting Location and Data Centre Assurance | High | Attestation | D7 |

---

## Test cases

<a id="tc-l15-001"></a>

### TC-L15-001: AI Infrastructure Asset Discovery

| Field | Value |
|---|---|
| **Lifecycle Layer** | L15 Infrastructure Layer |
| **Use-Case Domain(s)** | D4, D3 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (visibility control); Reconnaissance/Discovery context only |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (unmanaged AI components) |
| **NIST AI RMF Mapping** | MAP 1.1; GOVERN 6.1 |

**Risk Addressed.** GPU nodes, inference servers, vector stores and model storage are provisioned by data teams outside normal asset processes, so they escape patching and monitoring.

**Business Scenario.** Infrastructure owners want every component hosting AI workloads inventoried with owner, location and exposure.

**Technical Scenario.** Deploy a known set of AI infrastructure in several places and compare the platform's inventory with ground truth.

**Preconditions.** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab Kubernetes cluster with real or simulated GPU nodes, mock inference servers, a test cloud account with fabricated resources, separate network segments, seeded misconfigurations and test users; no production infrastructure, accounts or data connected.

**Test Data.** 12 assets: 3 GPU nodes (one in a separate cloud account), 2 inference servers, 2 vector stores, 2 model storage buckets, 1 notebook server, 1 orchestration controller, 1 experiment tracker; each tagged with owner, environment and exposure.

**Procedure**

1. Record ground truth: asset, location, owner, exposure, workload.
2. Deploy all assets without registering them.
3. Run discovery across cloud, cluster and network.
4. Compare found assets and attributes.
5. Check classification of exposure (internal, partner, internet).
6. Add two assets later and time detection.
7. Check export to the asset system.

**Edge Cases / Variants.** Assets in an account the platform was not given; short-lived training clusters existing for under an hour.

**Expected Detection.** At least 11 of 12 assets found; owner and exposure correct for at least 9; new assets detected within the stated interval; export maps to the asset system.

**Expected Prevention / Control Action.** N/A (discovery).

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Infrastructure finding visible in the infrastructure security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Inventory to CMDB.

**Forensic Evidence.** Asset identifier, location, configuration state, accessing identity, change or finding and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Inventory vs ground truth; detection delay.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l15-002"></a>

### TC-L15-002: GPU Cluster Configuration Hardening

| Field | Value |
|---|---|
| **Lifecycle Layer** | L15 Infrastructure Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** GPU hosts run privileged drivers and large shared workloads; default settings leave management ports, shared memory and debugging interfaces open.

**Business Scenario.** Platform security wants GPU and cluster configuration checked against a hardening baseline.

**Technical Scenario.** Assess lab GPU nodes and cluster configuration with seeded weaknesses and review findings.

**Preconditions.** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab Kubernetes cluster with real or simulated GPU nodes, mock inference servers, a test cloud account with fabricated resources, separate network segments, seeded misconfigurations and test users; no production infrastructure, accounts or data connected.

**Test Data.** 3 GPU nodes and 1 cluster with 16 seeded weaknesses: exposed device plugin metrics, open management interface, privileged containers with host device access, shared host paths, outdated driver, default credentials on a monitoring tool, debug port open, no node isolation between teams, unencrypted node disks, permissive cluster roles, plus 6 compliant settings.

**Procedure**

1. Record the seeded weaknesses.
2. Run the assessment.
3. Compare findings with ground truth.
4. Check severity ranking and remediation guidance.
5. Remediate five items and rerun.
6. Check which benchmark the checks map to (state it, for example a recognised Kubernetes or cloud benchmark).
7. Check handling of settings the platform cannot see (kernel or firmware level).

**Edge Cases / Variants.** Settings that differ between node pools; configuration changed after the scan.

**Expected Detection.** At least 13 of 16 weaknesses found; compliant settings not flagged more than twice; findings clear after remediation; benchmark mapping stated; blind spots documented.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Infrastructure finding visible in the infrastructure security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to ticketing.

**Forensic Evidence.** Asset identifier, location, configuration state, accessing identity, change or finding and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Findings vs seeded list.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l15-003"></a>

### TC-L15-003: GPU Multi-Tenancy Isolation and Memory Residue

| Field | Value |
|---|---|
| **Lifecycle Layer** | L15 Infrastructure Layer |
| **Use-Case Domain(s)** | D4, D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P \| Partial: R |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** Shared GPUs can leak data between tenants through memory that is not cleared or isolation modes that are weaker than assumed.

**Business Scenario.** Security wants isolation between workloads on shared accelerators demonstrated, not just stated.

**Technical Scenario.** Run two tenants' workloads on shared GPU resources in each sharing mode and probe for residue and interference.

**Preconditions.** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab GPU hardware or documented simulation; probe is lab-only and harmless.

**Test Data.** 2 tenants; sharing modes the vendor or platform supports (dedicated, partitioned, time-sliced); probe workload that writes canary patterns to device memory and a second workload that reads uninitialised device memory (lab only, harmless); noisy workload.

**Procedure**

1. Document the claimed isolation for each mode.
2. Run tenant A's workload writing a canary pattern.
3. Terminate it and start tenant B's probe immediately.
4. Search B's memory reads for the canary.
5. Repeat for each mode.
6. Run the noisy workload and measure effect on the other tenant's latency.
7. Check platform findings and recommendations on sharing modes.

**Edge Cases / Variants.** Memory not cleared after crash; containers sharing a driver version with a known issue.

**Expected Detection.** No canary visible across tenants in any mode the platform allows for sensitive workloads; weaker modes reported with risk statements; interference measured and reported.

**Expected Prevention / Control Action.** Restrict sharing by policy.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Infrastructure finding visible in the infrastructure security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to ticketing.

**Forensic Evidence.** Asset identifier, location, configuration state, accessing identity, change or finding and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Probe results per mode; latency table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l15-004"></a>

### TC-L15-004: Kubernetes Hardening for AI Workloads

| Field | Value |
|---|---|
| **Lifecycle Layer** | L15 Infrastructure Layer |
| **Use-Case Domain(s)** | D4, D3 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** AI jobs often run with broad cluster roles, host access and unrestricted networking for convenience.

**Business Scenario.** Platform owners want pod security, RBAC and admission rules applied to AI namespaces.

**Technical Scenario.** Scan and test lab namespaces with seeded poor settings, then enforce policy.

**Preconditions.** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab Kubernetes cluster with real or simulated GPU nodes, mock inference servers, a test cloud account with fabricated resources, separate network segments, seeded misconfigurations and test users; no production infrastructure, accounts or data connected.

**Test Data.** 3 namespaces (training, inference, shared tools); 20 workloads; seeded issues: privileged pods, host network, service account with cluster-admin, no resource limits, secrets as environment variables, unrestricted network policy, images from public registries, writable root file systems.

**Procedure**

1. Scan namespaces.
2. Compare findings with seeded issues.
3. Enable enforcement rules.
4. Redeploy the 20 workloads.
5. Record rejections and developer messages.
6. Request an exception and check approval and expiry.
7. Check drift detection after a manual change.

**Edge Cases / Variants.** Operators with privileged access making manual changes; third-party operators installed by Helm.

**Expected Detection.** At least 7 of 8 issue types found; non-compliant workloads rejected with clear reasons; exceptions time-limited; manual changes detected within the stated interval.

**Expected Prevention / Control Action.** Reject at admission.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Infrastructure finding visible in the infrastructure security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events to SIEM.

**Forensic Evidence.** Asset identifier, location, configuration state, accessing identity, change or finding and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Findings; admission outcomes.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l15-005"></a>

### TC-L15-005: Inference Server Hardening and Exposure

| Field | Value |
|---|---|
| **Lifecycle Layer** | L15 Infrastructure Layer |
| **Use-Case Domain(s)** | D3, D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0049 Exploit Public-Facing Application (where exposed); general cloud and infrastructure controls apply |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (infrastructure components) |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Inference servers ship with open admin interfaces, verbose errors and default ports that are easy to find and abuse.

**Business Scenario.** Security wants inference servers hardened and unexposed admin functions found.

**Technical Scenario.** Assess lab inference servers with seeded exposure and configuration weaknesses.

**Preconditions.** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab Kubernetes cluster with real or simulated GPU nodes, mock inference servers, a test cloud account with fabricated resources, separate network segments, seeded misconfigurations and test users; no production infrastructure, accounts or data connected.

**Test Data.** 3 mock inference servers with 12 seeded weaknesses: unauthenticated admin endpoint, debug routes, verbose stack traces, default ports exposed to wider segment, permissive cross-origin settings, no TLS on internal calls, unlimited request size, no rate limit, outdated version, model listing exposed, metrics endpoint with prompt samples, plus secure controls.

**Procedure**

1. Scan the servers.
2. Compare findings with ground truth.
3. Check ranking by exposure.
4. Check guidance.
5. Apply fixes to four items and rescan.
6. Test whether the platform shows the metrics endpoint content risk.
7. Check scan impact on server performance.

**Edge Cases / Variants.** Server behind an ingress that hides some routes; server updated between scans.

**Expected Detection.** At least 10 of 12 weaknesses found; fixes verified; metrics exposure of prompt content identified; scan causes no outage.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Infrastructure finding visible in the infrastructure security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to ticketing.

**Forensic Evidence.** Asset identifier, location, configuration state, accessing identity, change or finding and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Findings vs seeded list.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l15-006"></a>

### TC-L15-006: Network Segmentation Between AI Zones

| Field | Value |
|---|---|
| **Lifecycle Layer** | L15 Infrastructure Layer |
| **Use-Case Domain(s)** | D3, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, G |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0049 Exploit Public-Facing Application (where exposed); general cloud and infrastructure controls apply |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (infrastructure components) |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** A flat network lets a compromised notebook reach production data, model storage and management planes.

**Business Scenario.** Network security wants training, inference, data, management and developer zones separated by enforced rules.

**Technical Scenario.** Map zones, test cross-zone connections and compare with the intended policy.

**Preconditions.** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab Kubernetes cluster with real or simulated GPU nodes, mock inference servers, a test cloud account with fabricated resources, separate network segments, seeded misconfigurations and test users; no production infrastructure, accounts or data connected.

**Test Data.** 5 zones with a written allow matrix (training to data store allowed, inference to data store read-only, developer to management blocked, internet to inference only via gateway, management to all with MFA); test hosts in each zone; 25 intended connection tests.

**Procedure**

1. Load the intended matrix.
2. Test the 25 connections by attempting them.
3. Compare actual to intended.
4. Check how the platform reports violations.
5. Fix one violation and verify.
6. Introduce a new rule and check change detection.
7. Check visualisation of actual flows.

**Edge Cases / Variants.** Connections via a shared jump host; temporary firewall rule left open.

**Expected Detection.** At least 24 of 25 outcomes match the intended policy; violations reported with source, destination and port; rule change detected.

**Expected Prevention / Control Action.** N/A (assessment), or block where the platform enforces.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Infrastructure finding visible in the infrastructure security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to network security tools.

**Forensic Evidence.** Asset identifier, location, configuration state, accessing identity, change or finding and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Connection test matrix.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l15-007"></a>

### TC-L15-007: Egress Control for AI Workloads

| Field | Value |
|---|---|
| **Lifecycle Layer** | L15 Infrastructure Layer |
| **Use-Case Domain(s)** | D4, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, G, E |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0049 Exploit Public-Facing Application (where exposed); general cloud and infrastructure controls apply |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (infrastructure components) |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Training and inference jobs with unrestricted internet access can pull untrusted code and send data out.

**Business Scenario.** Security wants outbound destinations allowed per workload.

**Technical Scenario.** Run lab workloads that attempt outbound connections and test enforcement and visibility.

**Preconditions.** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab Kubernetes cluster with real or simulated GPU nodes, mock inference servers, a test cloud account with fabricated resources, separate network segments, seeded misconfigurations and test users; no production infrastructure, accounts or data connected.

**Test Data.** 3 workloads (training, inference, agent); allow-lists of 3 destinations each; 20 attempted connections: allowed hosts, public package index, unlisted storage bucket, raw IP, DNS tunnelling-style long queries (lab only), metadata service, other tenants' endpoints.

**Procedure**

1. Set policy.
2. Run the 20 attempts per workload.
3. Record decisions.
4. Check DNS handling.
5. Add and remove an allowed destination and check effect time.
6. Check alerts and logs.
7. Check behaviour when the control component fails.

**Edge Cases / Variants.** Allowed destination redirecting elsewhere; traffic over a non-standard port.

**Expected Detection.** All out-of-policy attempts blocked or alerted; allowed destinations work; DNS abuse patterns detected; change effective within 5 minutes; failure mode documented.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Infrastructure finding visible in the infrastructure security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events to SIEM.

**Forensic Evidence.** Asset identifier, location, configuration state, accessing identity, change or finding and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Attempt matrix.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l15-008"></a>

### TC-L15-008: Lateral Movement Containment from a Compromised Inference Pod

| Field | Value |
|---|---|
| **Lifecycle Layer** | L15 Infrastructure Layer |
| **Use-Case Domain(s)** | D3, D5 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, G |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0049 Exploit Public-Facing Application (where exposed); general cloud and infrastructure controls apply |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (infrastructure components) |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** A foothold in one inference container should not give reach to storage, other models or management APIs.

**Business Scenario.** Security wants blast radius limited and compromise detected.

**Technical Scenario.** Simulate a compromised inference pod using harmless lab probes that attempt common post-compromise actions.

**Preconditions.** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Probes are harmless lab scripts that only attempt connections and reads of canary resources.

**Test Data.** 1 inference pod; probes: read mounted secrets, query cloud metadata service, scan internal ports, call the cluster API, read other namespaces, write to the model bucket, reach the vector store; detection rules active.

**Procedure**

1. Baseline: run probes with controls off and record reach.
2. Enable controls.
3. Run probes again.
4. Record blocked actions and alerts.
5. Check time to detection.
6. Check containment actions offered (isolate pod, revoke token).
7. Review the evidence available for investigation.

**Edge Cases / Variants.** Pod with a mounted cloud credential; probe running slowly over hours.

**Expected Detection.** At least 6 of 7 probes blocked or detected; alerts within 5 minutes; isolation action available; evidence sufficient to reconstruct probes.

**Expected Prevention / Control Action.** Block; isolate.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Infrastructure finding visible in the infrastructure security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Alerts to SIEM and SOAR.

**Forensic Evidence.** Asset identifier, location, configuration state, accessing identity, change or finding and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Probe result table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l15-009"></a>

### TC-L15-009: Secrets Management for AI Infrastructure

| Field | Value |
|---|---|
| **Lifecycle Layer** | L15 Infrastructure Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0055 Unsecured Credentials |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** Secrets in images, environment variables and configuration maps are readable by anyone who can read the workload.

**Business Scenario.** Security wants secrets fetched from a vault and never baked in.

**Technical Scenario.** Seed secrets across lab infrastructure and test discovery and vault adoption.

**Preconditions.** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab Kubernetes cluster with real or simulated GPU nodes, mock inference servers, a test cloud account with fabricated resources, separate network segments, seeded misconfigurations and test users; no production infrastructure, accounts or data connected.

**Test Data.** 15 fabricated secrets across image layers, environment variables, config maps, node files, pipeline variables and notebook files; vault with 3 secrets properly referenced.

**Procedure**

1. Seed secrets.
2. Run detection across infrastructure.
3. Compare to ground truth.
4. Check rotation guidance.
5. Migrate two secrets to the vault and rerun.
6. Check vault access logging and policies.
7. Check detection of secrets in running process memory or logs if offered.

**Edge Cases / Variants.** Secrets in build cache; secrets in crash dumps.

**Expected Detection.** At least 13 of 15 secrets found; findings clear after migration; vault access logged and least-privilege.

**Expected Prevention / Control Action.** Alert.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Infrastructure finding visible in the infrastructure security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to ticketing.

**Forensic Evidence.** Asset identifier, location, configuration state, accessing identity, change or finding and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Detection table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l15-010"></a>

### TC-L15-010: Cloud IAM Roles for AI Services and Metadata Service Protection

| Field | Value |
|---|---|
| **Lifecycle Layer** | L15 Infrastructure Layer |
| **Use-Case Domain(s)** | D4, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** Over-permissive cloud roles on AI services let a small compromise become an account-wide one.

**Business Scenario.** Cloud security wants AI service roles minimal and metadata credentials protected.

**Technical Scenario.** Review roles attached to lab AI services and test misuse paths.

**Preconditions.** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab Kubernetes cluster with real or simulated GPU nodes, mock inference servers, a test cloud account with fabricated resources, separate network segments, seeded misconfigurations and test users; no production infrastructure, accounts or data connected.

**Test Data.** 6 roles: broad administrator, storage full access, read-only data, model deployment only, unused role with wildcard permissions, cross-account trust; metadata service with and without hardening.

**Procedure**

1. Extract roles and permissions.
2. Compare to need.
3. Flag over-permission and unused permissions.
4. Attempt to read credentials from the metadata service inside a pod.
5. Check protection (session tokens, restricted hops).
6. Reduce one role and verify service still works.
7. Check cross-account trust findings.

**Edge Cases / Variants.** Roles assumed through chains; permissions granted by tag conditions.

**Expected Detection.** Over-permissive roles identified for all seeded cases; metadata exposure found or blocked; reduced role works; trust findings correct.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Infrastructure finding visible in the infrastructure security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to ticketing.

**Forensic Evidence.** Asset identifier, location, configuration state, accessing identity, change or finding and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Permission analysis; metadata test.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l15-011"></a>

### TC-L15-011: Model and Dataset Storage Security

| Field | Value |
|---|---|
| **Lifecycle Layer** | L15 Infrastructure Layer |
| **Use-Case Domain(s)** | D4, D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** Public or weakly protected buckets holding models and datasets are among the most common AI exposures.

**Business Scenario.** Security wants model and dataset storage checked for exposure, encryption and versioning.

**Technical Scenario.** Assess lab storage with seeded weaknesses.

**Preconditions.** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab Kubernetes cluster with real or simulated GPU nodes, mock inference servers, a test cloud account with fabricated resources, separate network segments, seeded misconfigurations and test users; no production infrastructure, accounts or data connected.

**Test Data.** 6 buckets or shares with 14 seeded issues: public read, public write, no encryption, weak policy with wildcard principal, no versioning, no access logging, no object lock, cross-account access, signed URLs with long expiry, no lifecycle rules, plus compliant settings.

**Procedure**

1. Run assessment.
2. Compare with seeded issues.
3. Test unauthenticated access from outside the account.
4. Check findings priority.
5. Remediate three and rerun.
6. Check detection of new public exposure after a change.

**Edge Cases / Variants.** Signed URL shared externally; replication to another region.

**Expected Detection.** At least 12 of 14 issues found; public exposure ranked highest; new exposure detected within the stated interval.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Infrastructure finding visible in the infrastructure security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to ticketing.

**Forensic Evidence.** Asset identifier, location, configuration state, accessing identity, change or finding and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Findings vs seeded list.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l15-012"></a>

### TC-L15-012: Encryption and Confidential Computing Evidence

| Field | Value |
|---|---|
| **Lifecycle Layer** | L15 Infrastructure Layer |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Encryption claims often cover storage but not memory, backups or in-use data.

**Business Scenario.** Security wants the coverage of encryption stated precisely and verified where possible.

**Technical Scenario.** Review encryption coverage and any confidential computing support for lab workloads.

**Preconditions.** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab Kubernetes cluster with real or simulated GPU nodes, mock inference servers, a test cloud account with fabricated resources, separate network segments, seeded misconfigurations and test users; no production infrastructure, accounts or data connected.

**Test Data.** Lab workloads; encryption settings for disks, buckets, backups and network; vendor statements on in-use protection.

**Procedure**

1. Request a coverage table for data at rest, in transit and in use.
2. Verify disk, bucket and backup settings in the lab.
3. Scan TLS versions and ciphers.
4. If confidential computing is claimed, request attestation evidence and verify.
5. Record gaps.
6. Review key custody for each layer.

**Edge Cases / Variants.** Backups in another region; third-party managed services.

**Expected Detection.** Coverage table matches observed settings; TLS 1.2 or higher only; attestation evidence provided if claimed; gaps documented.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Infrastructure finding visible in the infrastructure security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Documents attached.

**Forensic Evidence.** Asset identifier, location, configuration state, accessing identity, change or finding and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Settings and scan output.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l15-013"></a>

### TC-L15-013: Control Plane and Data Plane Location Proof (Sovereignty)

| Field | Value |
|---|---|
| **Lifecycle Layer** | L15 Infrastructure Layer |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Sovereignty claims about in-country control are meaningless if management, telemetry or licensing functions depend on services outside the jurisdiction.

**Business Scenario.** Sovereignty and compliance reviewers need the physical and logical location of every plane proven.

**Technical Scenario.** Trace management, data and telemetry paths with network capture and cloud region evidence.

**Preconditions.** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab Kubernetes cluster with real or simulated GPU nodes, mock inference servers, a test cloud account with fabricated resources, separate network segments, seeded misconfigurations and test users; no production infrastructure, accounts or data connected.

**Test Data.** Deployed platform in the lab; capture tooling; list of platform components with claimed locations; data classes (prompts, metadata, telemetry, licence checks, updates).

**Procedure**

1. Request a written table of components, locations and operators.
2. Capture all traffic for 48 hours including idle periods and an upgrade.
3. Resolve destinations to operators and regions.
4. Compare with the table.
5. Block all non-approved regions and verify continued operation.
6. Check who holds administrative credentials for each plane and from where they connect.
7. Review contractual statements.

**Edge Cases / Variants.** Licence checks and update endpoints; support access from another country.

**Expected Detection.** No component or data class depends on a non-approved region; operation continues with non-approved regions blocked; administrative access locations documented; written table matches observations.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Infrastructure finding visible in the infrastructure security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Documents attached.

**Forensic Evidence.** Asset identifier, location, configuration state, accessing identity, change or finding and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Capture analysis; region resolution table.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l15-014"></a>

### TC-L15-014: Air-Gapped and On-Premise Operation

| Field | Value |
|---|---|
| **Lifecycle Layer** | L15 Infrastructure Layer |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Products described as on-premise often need cloud services for licensing, updates, model downloads or classification.

**Business Scenario.** Operations in restricted environments need proof the product works without internet.

**Technical Scenario.** Deploy the platform in an isolated lab segment with no internet access and run the full test set.

**Preconditions.** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab Kubernetes cluster with real or simulated GPU nodes, mock inference servers, a test cloud account with fabricated resources, separate network segments, seeded misconfigurations and test users; no production infrastructure, accounts or data connected.

**Test Data.** Isolated segment; offline update media; standard test set of 40 prompts and events; offline licence mechanism.

**Procedure**

1. Deploy with no internet.
2. Run the standard test set.
3. Record functions that fail or degrade.
4. Apply an offline update.
5. Check licence validation offline.
6. Check threat content updates offline and their delay.
7. Check log and evidence export offline.

**Edge Cases / Variants.** Licence expiry during offline period; time synchronisation drift.

**Expected Detection.** All claimed core functions work offline; degraded functions documented; offline update and licence work; content update path defined.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Infrastructure finding visible in the infrastructure security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Offline export works.

**Forensic Evidence.** Asset identifier, location, configuration state, accessing identity, change or finding and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Function table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l15-015"></a>

### TC-L15-015: Single-Tenant and Dedicated Deployment Evidence

| Field | Value |
|---|---|
| **Lifecycle Layer** | L15 Infrastructure Layer |
| **Use-Case Domain(s)** | D7, D4 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** Shared platforms increase the chance of cross-customer exposure and complicate residency commitments.

**Business Scenario.** Risk owners want dedicated options and isolation shown.

**Technical Scenario.** Review tenancy models and test isolation where a shared option is in scope.

**Preconditions.** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab Kubernetes cluster with real or simulated GPU nodes, mock inference servers, a test cloud account with fabricated resources, separate network segments, seeded misconfigurations and test users; no production infrastructure, accounts or data connected.

**Test Data.** Vendor tenancy documentation; lab tenants in each available model.

**Procedure**

1. Request a description of each tenancy model.
2. Compare with deployment in the lab.
3. Check network, storage and compute separation.
4. Check customer-held key options per model.
5. Test administrative separation between tenants.
6. Review incident history involving tenancy.

**Edge Cases / Variants.** Dedicated compute with shared control plane.

**Expected Detection.** Tenancy model matches documentation; isolation verified at network, storage and compute levels; incident history disclosed.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Infrastructure finding visible in the infrastructure security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Documents attached.

**Forensic Evidence.** Asset identifier, location, configuration state, accessing identity, change or finding and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Verification notes.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l15-016"></a>

### TC-L15-016: Hardening of the Evaluated Platform's Own Components

| Field | Value |
|---|---|
| **Lifecycle Layer** | L15 Infrastructure Layer |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0049 Exploit Public-Facing Application (where exposed); general cloud and infrastructure controls apply |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (infrastructure components) |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** The security platform's agents, gateways and console hold privileged access to traffic and data, and are themselves attack targets.

**Business Scenario.** Security wants the vendor's own components assessed like any other critical system.

**Technical Scenario.** Deploy the platform in the lab and assess each component with network, configuration and credential checks.

**Preconditions.** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab Kubernetes cluster with real or simulated GPU nodes, mock inference servers, a test cloud account with fabricated resources, separate network segments, seeded misconfigurations and test users; no production infrastructure, accounts or data connected.

**Test Data.** Deployed agent, gateway and management console; scanning tools approved for the lab; benchmark checklist.

**Procedure**

1. Port scan and service enumeration of each component.
2. TLS and cipher scan.
3. Check default credentials and password policy.
4. Check administrative interface exposure and MFA.
5. Check privileges the agent runs with and files it writes.
6. Check log content for secrets.
7. Check operating system hardening of appliances.
8. Report findings by severity.

**Edge Cases / Variants.** Appliance images with outdated components; debugging interfaces enabled by default.

**Expected Detection.** No critical or high findings left open without a vendor commitment; no default credentials; MFA available for administrators; agent privileges match documentation.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Infrastructure finding visible in the infrastructure security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to the vendor with deadlines.

**Forensic Evidence.** Asset identifier, location, configuration state, accessing identity, change or finding and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Scan outputs; findings list.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l15-017"></a>

### TC-L15-017: Resource Quotas and Noisy-Neighbour Protection on Shared GPU Capacity

| Field | Value |
|---|---|
| **Lifecycle Layer** | L15 Infrastructure Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | AML.T0029 Denial of AI Service; AML.T0034 Cost Harvesting |
| **OWASP LLM / GenAI Mapping** | LLM10:2025 Unbounded Consumption |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 4.1 |

**Risk Addressed.** One team can monopolise scarce GPU capacity or starve production inference.

**Business Scenario.** Operations wants quotas and priorities enforced.

**Technical Scenario.** Run competing workloads under quotas and measure fairness and protection of production inference.

**Preconditions.** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab Kubernetes cluster with real or simulated GPU nodes, mock inference servers, a test cloud account with fabricated resources, separate network segments, seeded misconfigurations and test users; no production infrastructure, accounts or data connected.

**Test Data.** Cluster with 8 GPU units; 3 teams with quotas; production inference service; 4 batch training jobs including one oversized.

**Procedure**

1. Set quotas and priorities.
2. Run the jobs.
3. Record allocation.
4. Submit an oversized job.
5. Measure production inference latency during contention.
6. Check preemption and alerts.
7. Check quota change audit.

**Edge Cases / Variants.** Burst credits; job priority changes mid-run.

**Expected Detection.** Quotas enforced; production latency within limit during contention; oversized job rejected or queued; alerts raised.

**Expected Prevention / Control Action.** Enforce quota.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Infrastructure finding visible in the infrastructure security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Metrics to monitoring.

**Forensic Evidence.** Asset identifier, location, configuration state, accessing identity, change or finding and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Allocation and latency table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l15-018"></a>

### TC-L15-018: Infrastructure Logging and Telemetry Coverage

| Field | Value |
|---|---|
| **Lifecycle Layer** | L15 Infrastructure Layer |
| **Use-Case Domain(s)** | D4, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, G |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Gaps in cluster, GPU, storage and network logging leave incidents unexplained.

**Business Scenario.** SOC wants required log sources present, complete and timely.

**Technical Scenario.** Generate known activity in lab infrastructure and check that every expected log source records it.

**Preconditions.** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab Kubernetes cluster with real or simulated GPU nodes, mock inference servers, a test cloud account with fabricated resources, separate network segments, seeded misconfigurations and test users; no production infrastructure, accounts or data connected.

**Test Data.** 8 activities: login to the cluster, role change, secret read, model file download, storage policy change, GPU job start, network policy change, admin API call; 10 log sources.

**Procedure**

1. List expected log sources and fields.
2. Perform each activity.
3. Check for a corresponding record in each source.
4. Check timestamps and identities.
5. Identify missing sources.
6. Check delivery delay to the SIEM.
7. Check retention settings.

**Edge Cases / Variants.** Activities performed through automation accounts; logging disabled by an attacker.

**Expected Detection.** At least 7 of 8 activities recorded with identity and time; delay under 5 minutes; gaps reported by the platform.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Infrastructure finding visible in the infrastructure security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Delivery to SIEM.

**Forensic Evidence.** Asset identifier, location, configuration state, accessing identity, change or finding and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Coverage table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l15-019"></a>

### TC-L15-019: Backup, Disaster Recovery and Restoration of AI Services

| Field | Value |
|---|---|
| **Lifecycle Layer** | L15 Infrastructure Layer |
| **Use-Case Domain(s)** | D3, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Models, vector stores, prompts and policies may be unrecoverable or restore to an insecure state.

**Business Scenario.** Resilience owners want recovery objectives met and restored services secure.

**Technical Scenario.** Back up and restore a lab AI service including model, index, configuration and policies.

**Preconditions.** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab Kubernetes cluster with real or simulated GPU nodes, mock inference servers, a test cloud account with fabricated resources, separate network segments, seeded misconfigurations and test users; no production infrastructure, accounts or data connected.

**Test Data.** 1 AI application with model weights, vector store of 1,000 chunks, prompt templates, platform policies and access rules; recovery targets for time and data loss.

**Procedure**

1. Take backups.
2. Destroy the primary environment.
3. Restore.
4. Measure recovery time and data loss.
5. Check that access controls, keys and policies are restored correctly.
6. Check that restored secrets are rotated or protected.
7. Test restoration in a second region if relevant to the residency policy.

**Edge Cases / Variants.** Partial restore; restore during a policy change.

**Expected Detection.** Targets met; access controls identical after restore; no data restored outside permitted regions; backups encrypted.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Infrastructure finding visible in the infrastructure security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Backup logs.

**Forensic Evidence.** Asset identifier, location, configuration state, accessing identity, change or finding and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Recovery timeline; post-restore checks.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l15-020"></a>

### TC-L15-020: Hosting Location and Data Centre Assurance

| Field | Value |
|---|---|
| **Lifecycle Layer** | L15 Infrastructure Layer |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Attestation |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Residency and resilience promises depend on where infrastructure physically sits, who operates it and what assurance covers the facility.

**Business Scenario.** Compliance wants hosting locations, operators and facility assurance evidenced for every component that touches customer data.

**Technical Scenario.** Request and review hosting and facility evidence for each platform component and compare with observed network destinations.

**Preconditions.** Isolated PoC lab provisioned; lab cluster with real or simulated GPU nodes, mock inference servers, test cloud account, network segments and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab Kubernetes cluster with real or simulated GPU nodes, mock inference servers, a test cloud account with fabricated resources, separate network segments, seeded misconfigurations and test users; no production infrastructure, accounts or data connected.

**Test Data.** List of platform components and hosting providers; facility certifications and audit reports; observed destination and region data from the lab; requirements checklist (country, operator, certification, resilience tier, physical access controls, sub-contractors).

**Procedure**

1. Request in writing, for each component, the country, city, operator, facility and sub-contractors.
2. Request facility certifications and audit reports, and check scope and dates.
3. Compare with the lab capture of real destinations.
4. Check whether disaster recovery sites stay inside the permitted country.
5. Check notification commitments for hosting changes.
6. Record anything the vendor cannot evidence.

**Edge Cases / Variants.** Hosting provider acquired or changed during the contract; managed services whose locations the vendor cannot confirm.

**Expected Detection.** Locations and operators documented for every component; reports current and in scope; DR sites inside the permitted country; observed destinations match; change notification committed.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Signed written statement from the vendor.

**Expected Report / Dashboard Evidence.** Infrastructure finding visible in the infrastructure security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Documents attached to the register.

**Forensic Evidence.** Asset identifier, location, configuration state, accessing identity, change or finding and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = no statement; 3 = statement without supporting detail; 5 = statement with technical detail and an offer to demonstrate.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Evidence checklist; destination comparison.

**Reviewer Notes.** Attestation scores below demonstrated evidence. Request a demonstration where possible.

[Back to layer index](#top)

---

