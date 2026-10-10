---
title: "L12 Model Layer"
author: Nachiket Sathaye
parent: "Test Case Library"
nav_order: 15
---

<a id="top"></a>

# L12 Model Layer

**Primary test focus:** model theft, extraction, adversarial inputs, model scanning, identity for model access

**Controls tested:** [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) Model Protection (14 cases), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) AI Supply Chain and AI-BOM (6 cases), [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity (5 cases), [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) Least Privilege and Scoped Credentials (5 cases), [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) AI Use-Case Registry and Risk Tiering (2 cases), [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030) ML Pipeline and Model Registry Security (2 cases), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) Adversarial Testing and Continuous Evaluation (2 cases), [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls (2 cases), [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) AI Discovery (1 case), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) Auditability (1 case), [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) Policy Enforcement (1 case), [AI-CTRL-032](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-032) AI Infrastructure Hardening (1 case), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) Output Reliability and Content Safety (1 case), [AI-CTRL-040](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-040) AI Service Resilience and Fail-Safe Operation (1 case)

**Cases:** 31 (TC-L12-001 to TC-L12-031)
> **Safety boundary.** Retrieval, model, training, pipeline and supply chain cases use fabricated corpora and datasets, small lab models, mock hubs and indexes and harmless marker artefacts only (an EICAR-style file that writes a marker, never real malware). Never load untrusted model files outside an isolated sandbox, and never connect the lab to production knowledge sources, models, pipelines, registries or credentials. Cases marked Attestation rest on vendor documents and score below demonstrated evidence.

> **Verify before use.** MITRE ATLAS, OWASP LLM and NIST AI RMF identifiers must be checked against the current published versions. Numeric thresholds are starting values to tune. See the [Reference Index](00-reference-index.md) for field definitions and applicability codes.

## Cases in this layer

| ID | Title | Severity | Method | Domain(s) | Controls |
|---|---|---|---|---|---|
| [TC-L12-001](#tc-l12-001) | Model Inventory and Registry Discovery | High | Technical | D4 | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031), [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) |
| [TC-L12-002](#tc-l12-002) | Model Artefact Scanning: Unsafe Serialisation | Critical | Technical | D4 | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) |
| [TC-L12-003](#tc-l12-003) | Model Scanning: Backdoor and Trojan Indicators | High | Technical | D4 | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) |
| [TC-L12-004](#tc-l12-004) | Model File Format Policy Enforcement | Medium | Technical | D4 | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030) |
| [TC-L12-005](#tc-l12-005) | Model Provenance and Signature Verification | Critical | Technical | D4 | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) |
| [TC-L12-006](#tc-l12-006) | Model Licence and Usage Terms Check | Medium | Evidence | D4 | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) |
| [TC-L12-007](#tc-l12-007) | Model Extraction Attack Detection | High | Technical | D4 | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) |
| [TC-L12-008](#tc-l12-008) | Training Data Extraction and Memorisation Probes | High | Technical | D4, D6 | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) |
| [TC-L12-009](#tc-l12-009) | Model Weights Exfiltration Protection | Critical | Technical | D4, D7 | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) |
| [TC-L12-010](#tc-l12-010) | Adversarial Image Robustness for Vision Models | Medium | Technical | D4 | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) |
| [TC-L12-011](#tc-l12-011) | Adversarial Text Perturbation Robustness for Classifiers | Medium | Technical | D4 | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) |
| [TC-L12-012](#tc-l12-012) | Inference-Time Input Anomaly Detection | Medium | Technical | D4 | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) |
| [TC-L12-013](#tc-l12-013) | Inference Endpoint Authentication, Authorisation and Rate Limiting | Critical | Technical | D4 | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036), [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) |
| [TC-L12-014](#tc-l12-014) | Model-Level Access Control by User, Role and Version | High | Technical | D4 | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) |
| [TC-L12-015](#tc-l12-015) | Model Fingerprinting and Unauthorised Copy Identification | Medium | Technical | D4 | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) |
| [TC-L12-016](#tc-l12-016) | Safety Evaluation Baseline for Deployed Models | High | Technical | D4, D3 | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) |
| [TC-L12-017](#tc-l12-017) | Hallucination and Factuality Evaluation Baseline | Medium | Technical | D4 | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) |
| [TC-L12-018](#tc-l12-018) | Model Version Pinning and Behaviour Drift Detection | High | Technical | D4 | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031), [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) |
| [TC-L12-019](#tc-l12-019) | Model Cards and AI-BOM Completeness | Medium | Evidence | D4, D7 | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) |
| [TC-L12-020](#tc-l12-020) | Model Deployment Configuration Hardening | Medium | Evidence | D4 | [AI-CTRL-032](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-032) |
| [TC-L12-021](#tc-l12-021) | Multi-Model Routing and Fallback Security | High | Technical | D4, D7 | [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010), [AI-CTRL-040](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-040) |
| [TC-L12-022](#tc-l12-022) | Model Resource Exhaustion and Long-Sequence Abuse | Medium | Technical | D4 | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) |
| [TC-L12-023](#tc-l12-023) | Quantised and Converted Model Integrity | Medium | Technical | D4 | [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030) |
| [TC-L12-024](#tc-l12-024) | Model Retirement and Weight Disposal | Low | Evidence | D4, D7 | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) |
| [TC-L12-025](#tc-l12-025) | Model Risk Tiering and Assessment Workflow | Medium | Evidence | D4, D7 | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) |
| [TC-L12-026](#tc-l12-026) | Model Serving Workload Identity and Scoped Access to Weights | Critical | Technical | D4 | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015), [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) |
| [TC-L12-027](#tc-l12-027) | Calling Workload Attribution at Inference Endpoints: No Shared Application Keys | High | Technical | D4 | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) |
| [TC-L12-028](#tc-l12-028) | Privileged Access to Model Weights and the Registry: Just-in-Time and Dual Approval | Critical | Technical | D4, D7 | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016), [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) |
| [TC-L12-029](#tc-l12-029) | Tenant and Owner Isolation for Fine-Tuned Models | Critical | Technical | D4, D7 | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016), [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) |
| [TC-L12-030](#tc-l12-030) | Access Recertification for Model Registry and Serving Entitlements | Medium | Evidence | D4 | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015), [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) |
| [TC-L12-031](#tc-l12-031) | Identity Audit Trail for Model Access: Download, Load and Promotion Events | High | Technical | D4, D7 | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) |

---

## Test cases

<a id="tc-l12-001"></a>

### TC-L12-001: Model Inventory and Registry Discovery

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (visibility control); Reconnaissance/Discovery context only |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (unmanaged AI components) |
| **NIST AI RMF Mapping** | MAP 1.1; GOVERN 6.1 |
| **Control(s) Tested** | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) AI Supply Chain and AI-BOM; [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) AI Discovery |

**Risk Addressed.** Models run in notebooks, containers, cloud services and SaaS; unknown models are unmanaged risk.

**Business Scenario.** Model risk owners want all models listed with source, version, host and owner.

**Technical Scenario.** Deploy a known set of models in different places and compare the inventory.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 10 models: 3 hosted API models, 3 self-hosted open-weight models, 2 fine-tuned models, 1 embedding model, 1 classifier in a notebook.

**Procedure**

1. Record ground truth.
2. Run discovery.
3. Compare.
4. Check attributes: source, version, licence, host, owner, data used.
5. Add a model and time detection.

**Edge Cases / Variants.** Model loaded only at runtime; model with renamed files.

**Expected Detection.** At least 9 of 10 models found; source and version correct for at least 8; new model detected within the stated interval.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Inventory exportable to a model registry or catalogue.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Inventory vs ground truth.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-002"></a>

### TC-L12-002: Model Artefact Scanning: Unsafe Serialisation

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, R |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |
| **Control(s) Tested** | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) Model Protection; [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) AI Supply Chain and AI-BOM |

**Risk Addressed.** Model files in some formats can execute code when loaded.

**Business Scenario.** Security wants unsafe model files caught before they are loaded.

**Technical Scenario.** Scan a set of model files including harmless marker artefacts.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 12 files: 4 in safe tensor format, 4 in a pickle-based format with benign content, 4 pickle-based files containing a harmless marker-writing payload (EICAR-style).

**Procedure**

1. Submit all files to the scanner.
2. Record detection.
3. Attempt to load a flagged file with the gate on and off in an isolated sandbox.
4. Check whether the marker file is created.
5. Check scan time for large files.

**Edge Cases / Variants.** Payload hidden in a nested archive; obfuscated payload.

**Expected Detection.** All 4 marker files flagged; safe files pass; flagged files blocked from loading when the gate is on; scan time reasonable.

**Expected Prevention / Control Action.** Block load.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to registry.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Scan results; sandbox observations.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-003"></a>

### TC-L12-003: Model Scanning: Backdoor and Trojan Indicators

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Partial: P, R |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |
| **Control(s) Tested** | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) Model Protection |

**Risk Addressed.** Backdoored models behave normally until a trigger appears.

**Business Scenario.** Security wants to know what the scanner can and cannot find.

**Technical Scenario.** Test the scanner on models with known benign trigger behaviour.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 3 small test models with an inserted harmless trigger that outputs a marker phrase; 3 clean models.

**Procedure**

1. Submit models.
2. Record findings.
3. Run behavioural probes with and without the trigger.
4. Ask the vendor for detection method and published results.
5. Document limitations.

**Edge Cases / Variants.** Trigger in a language other than English; trigger via image.

**Expected Detection.** Detection rate reported honestly; at least 2 of 3 triggered models flagged or the limitation documented in writing.

**Expected Prevention / Control Action.** Block or flag.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to registry.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Result table; vendor method statement.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-004"></a>

### TC-L12-004: Model File Format Policy Enforcement

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) Model Protection; [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030) ML Pipeline and Model Registry Security |

**Risk Addressed.** Policies banning unsafe formats are useless if not enforced at load and download.

**Business Scenario.** Security wants format policy enforced in pipelines and workstations.

**Technical Scenario.** Try to download and load models in disallowed formats.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 3 formats; 2 locations (pipeline, workstation).

**Procedure**

1. Set policy.
2. Attempt download and load in each location.
3. Check blocks and exceptions.
4. Check exception audit.

**Edge Cases / Variants.** Renamed file extension; archive containing disallowed file.

**Expected Detection.** Disallowed formats blocked in both locations; exceptions audited.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events to SIEM.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Result table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-005"></a>

### TC-L12-005: Model Provenance and Signature Verification

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |
| **Control(s) Tested** | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) AI Supply Chain and AI-BOM |

**Risk Addressed.** A model from an unknown source or modified in transit may not be what it claims to be.

**Business Scenario.** Supply chain owners want origin and integrity verified at load.

**Technical Scenario.** Load signed, unsigned and tampered models.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 3 signed models, 3 unsigned, 3 signed then tampered; trust policy.

**Procedure**

1. Set trust policy.
2. Attempt to load each.
3. Record results.
4. Check how trust anchors are managed.
5. Check logs.

**Edge Cases / Variants.** Expired signing key; key rotation.

**Expected Detection.** Tampered and unsigned models blocked per policy; signed models load; trust management documented.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Verification events.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Load results.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-006"></a>

### TC-L12-006: Model Licence and Usage Terms Check

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) AI Supply Chain and AI-BOM |

**Risk Addressed.** Using models against their licence terms creates legal exposure.

**Business Scenario.** Legal wants licence terms captured and violations flagged.

**Technical Scenario.** Register models with different licences and test policy.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 8 models with different licence types, including non-commercial and restricted-use terms.

**Procedure**

1. Register models.
2. Check licence detection.
3. Set policy (no non-commercial in production).
4. Attempt deployment.
5. Check report.

**Edge Cases / Variants.** Custom licences; licence changes.

**Expected Detection.** Licences correctly identified for at least 7 of 8; policy blocks restricted deployments.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Report export.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Licence table.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l12-007"></a>

### TC-L12-007: Model Extraction Attack Detection

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0024 Exfiltration via AI Inference API (includes model extraction and inversion techniques) |
| **OWASP LLM / GenAI Mapping** | LLM10:2025 Unbounded Consumption; LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.7; MEASURE 2.10 |
| **Control(s) Tested** | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) Model Protection |

**Risk Addressed.** Systematic querying can reproduce a model's behaviour and steal its value.

**Business Scenario.** Model owners want extraction patterns detected and throttled.

**Technical Scenario.** Run a scripted extraction-style query pattern against a protected inference endpoint.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** Inference endpoint; normal profile of 50 queries per user per day; extraction script making 20,000 structured queries.

**Procedure**

1. Run normal use.
2. Run extraction at three speeds.
3. Record detection and action.
4. Check false positives for heavy legitimate users (batch analytics).
5. Check alerts.

**Edge Cases / Variants.** Distributed extraction across accounts.

**Expected Detection.** Extraction detected at fast and medium rates within 15 minutes; slow rate behaviour documented; legitimate heavy user not blocked without review.

**Expected Prevention / Control Action.** Throttle.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Alerts to SIEM.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Detection timeline.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-008"></a>

### TC-L12-008: Training Data Extraction and Memorisation Probes

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4, D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: R \| Partial: G |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0024 Exfiltration via AI Inference API (includes model extraction and inversion techniques) |
| **OWASP LLM / GenAI Mapping** | LLM10:2025 Unbounded Consumption; LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.7; MEASURE 2.10 |
| **Control(s) Tested** | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) Model Protection |

**Risk Addressed.** Models may reproduce training data, including personal data.

**Business Scenario.** Privacy wants memorisation measured and extraction attempts blocked.

**Technical Scenario.** Run probes against a test model fine-tuned on canary content.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** Test model fine-tuned on 50 canary strings; 100 extraction prompts.

**Procedure**

1. Run probes.
2. Count canary reproduction.
3. Enable the platform.
4. Repeat.
5. Compare.
6. Check output filtering.

**Edge Cases / Variants.** Prefix attacks; repeated token attacks.

**Expected Detection.** Canary reproduction rate reported; at least 90 percent of reproductions blocked or masked.

**Expected Prevention / Control Action.** Mask.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events with canary matches.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Probe results.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-009"></a>

### TC-L12-009: Model Weights Exfiltration Protection

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, P |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0024 Exfiltration via AI Inference API (includes model extraction and inversion techniques) |
| **OWASP LLM / GenAI Mapping** | LLM10:2025 Unbounded Consumption; LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.7; MEASURE 2.10 |
| **Control(s) Tested** | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) Model Protection |

**Risk Addressed.** Weights represent the model's whole value and may encode sensitive training data.

**Business Scenario.** Security wants copying of weights outside controlled locations detected and blocked.

**Technical Scenario.** Attempt to copy model files to unauthorised destinations.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** Weights repository; destinations: personal cloud, removable media (lab), unapproved bucket, email; 4 file sizes.

**Procedure**

1. Attempt each copy.
2. Record detection and action.
3. Check classification of model files as sensitive.
4. Check access logs for model storage.

**Edge Cases / Variants.** Copy in split chunks; copy via compressed archive.

**Expected Detection.** All copy attempts blocked or alerted; storage access logged.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events to SIEM.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Attempt table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-010"></a>

### TC-L12-010: Adversarial Image Robustness for Vision Models

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Partial: R |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | AML.T0043 Craft Adversarial Data |
| **OWASP LLM / GenAI Mapping** | N/A (classic model robustness; no direct LLM Top 10 entry) |
| **NIST AI RMF Mapping** | MEASURE 2.5; MEASURE 2.7 |
| **Control(s) Tested** | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) Model Protection |

**Risk Addressed.** Small imperceptible changes can flip a vision model's decision.

**Business Scenario.** Model owners want robustness measured and attacks detected.

**Technical Scenario.** Apply standard perturbation methods to a test classifier and measure.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** Test image classifier; 100 images; perturbation levels low, medium, high; open-source robustness tooling.

**Procedure**

1. Baseline accuracy.
2. Apply perturbations.
3. Measure accuracy drop.
4. Enable the platform's detection.
5. Measure detection rate and false positives on clean images.

**Edge Cases / Variants.** Physical-world style perturbations.

**Expected Detection.** Accuracy loss measured; at least 70 percent of high-level perturbations detected; false positives under 5 percent.

**Expected Prevention / Control Action.** Flag.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings exportable.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Robustness table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-011"></a>

### TC-L12-011: Adversarial Text Perturbation Robustness for Classifiers

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Partial: R, A |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | AML.T0043 Craft Adversarial Data |
| **OWASP LLM / GenAI Mapping** | N/A (classic model robustness; no direct LLM Top 10 entry) |
| **NIST AI RMF Mapping** | MEASURE 2.5; MEASURE 2.7 |
| **Control(s) Tested** | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) Model Protection |

**Risk Addressed.** Small wording changes can flip the decisions of fraud, spam, toxicity or routing classifiers, letting an attacker evade controls the business relies on.

**Business Scenario.** Model owners want to know how easily their text classifiers are fooled and whether the platform detects evasion attempts.

**Technical Scenario.** Perturb inputs to a lab text classifier with realistic evasion techniques and measure decision flips and platform detection.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** Lab classifier (for example a spam or fraud-style model); 200 labelled inputs; 5 perturbation types: character swaps and typos, synonym substitution, homoglyph substitution, inserted benign filler text, and translation round trip.

**Procedure**

1. Measure baseline accuracy on the 200 clean inputs.
2. Apply each perturbation type to all inputs (1,000 variants).
3. Record decision flips by type.
4. Enable the platform's evasion detection.
5. Resend variants and record flags.
6. Send 100 clean inputs written by different people and record false positives.
7. Review explanations given for flags.

**Edge Cases / Variants.** Perturbations in Arabic or mixed script; combined perturbations; adaptive attacker who tunes against the detector.

**Expected Detection.** Flip rate by perturbation type reported; at least 60 percent of flipped variants flagged; false positives on natural variation under 5 percent; explanations name the technique class.

**Expected Prevention / Control Action.** Flag or route to review.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings exportable to model risk records.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Flip-rate table; detection and false-positive counts.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-012"></a>

### TC-L12-012: Inference-Time Input Anomaly Detection

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | AML.T0043 Craft Adversarial Data |
| **OWASP LLM / GenAI Mapping** | N/A (classic model robustness; no direct LLM Top 10 entry) |
| **NIST AI RMF Mapping** | MEASURE 2.5; MEASURE 2.7 |
| **Control(s) Tested** | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) Model Protection |

**Risk Addressed.** Crafted or out-of-distribution inputs are often the first signs of probing, extraction or evasion.

**Business Scenario.** Security wants unusual input patterns to the model flagged before they cause harm.

**Technical Scenario.** Send normal traffic and five classes of anomalous input to a lab inference endpoint and compare detection.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 300 normal inputs; 50 anomalous inputs across five classes: extreme length, unusual character distributions, repeated near-identical queries with small changes (probing), out-of-domain content, and malformed structured inputs.

**Procedure**

1. Run the 300 normal inputs to build a baseline.
2. Send the 50 anomalous inputs in randomised order.
3. Record flags and actions.
4. Review the explanation for each flag.
5. Count false positives on 100 additional normal inputs from different users.
6. Introduce a legitimate new input type (a new product launch) and check how quickly the baseline adapts and whether alerts are raised.

**Edge Cases / Variants.** Slow-and-low probing over days; anomalies from a trusted internal service.

**Expected Detection.** At least 80 percent of anomalous inputs flagged; false positives below 3 percent; explanations name the anomaly class; baseline adapts to the new legitimate input type within the stated period without suppressing true anomalies.

**Expected Prevention / Control Action.** Flag or rate-limit.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Alerts to SIEM.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Detection table by anomaly class.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-013"></a>

### TC-L12-013: Inference Endpoint Authentication, Authorisation and Rate Limiting

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) Model Protection; [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls; [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity |

**Risk Addressed.** Unprotected inference endpoints are easy to abuse, copy, overload or use as a pivot into the network.

**Business Scenario.** Security wants every model endpoint authenticated, scoped and rate limited.

**Technical Scenario.** Test lab inference APIs with no credentials, bad credentials, wrong-scope credentials and abusive volume.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 2 lab inference endpoints (one internal, one exposed to a wider segment); credential sets: valid, expired, revoked, wrong scope, malformed; load script at 10 times normal volume.

**Procedure**

1. Call each endpoint without credentials.
2. Call with each invalid credential type.
3. Call with a valid but wrong-scope credential against another model.
4. Exceed the rate limit from one identity and then from many identities sharing one network address.
5. Check response codes, error messages and information leakage.
6. Check logging of every rejected call.
7. Scan the endpoint for exposed documentation or debug routes.

**Edge Cases / Variants.** Credentials passed in query strings; cross-origin browser calls; endpoint reachable by IP address.

**Expected Detection.** All invalid calls rejected with uninformative errors; wrong-scope access denied; rate limits enforced per identity; every rejection logged with source and credential identifier; no exposed debug routes.

**Expected Prevention / Control Action.** Reject and throttle.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events to SIEM.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Call and response table; log extract; scan output.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-014"></a>

### TC-L12-014: Model-Level Access Control by User, Role and Version

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) Least Privilege and Scoped Credentials |

**Risk Addressed.** Different models and versions carry different data exposure, cost and risk; open access to all of them defeats risk tiering.

**Business Scenario.** Governance wants access defined per model and version and enforced consistently.

**Technical Scenario.** Define a role-by-model matrix and test every combination, including after version change.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 4 models (public, internal, restricted data, experimental), 3 versions of the restricted model, 3 roles, 2 service identities; 40 combinations.

**Procedure**

1. Define the access matrix.
2. Test all 40 combinations and record outcomes.
3. Compare to the matrix.
4. Release a new version of the restricted model and test inherited access.
5. Change one rule and time its effect.
6. Check that deprecated versions can be disabled.
7. Review logs for model, version and identity.

**Edge Cases / Variants.** Model alias names; version pinned in application code; identity belonging to two roles.

**Expected Detection.** All 40 outcomes match; new versions do not inherit broader access than intended; rule change effective in the stated time; deprecated versions blocked.

**Expected Prevention / Control Action.** Allow or deny.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Decision logs to SIEM.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Matrix with expected and actual columns.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-015"></a>

### TC-L12-015: Model Fingerprinting and Unauthorised Copy Identification

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Partial: R, P |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | AML.T0024 Exfiltration via AI Inference API (includes model extraction and inversion techniques) |
| **OWASP LLM / GenAI Mapping** | LLM10:2025 Unbounded Consumption; LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.7; MEASURE 2.10 |
| **Control(s) Tested** | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) Model Protection |

**Risk Addressed.** Without a fingerprint, an owner cannot show that a suspect model derives from its own.

**Business Scenario.** Legal and security want a way to identify unauthorised copies or derivatives with evidence.

**Technical Scenario.** Fingerprint a lab model, create copies and derivatives, and test identification.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 1 owned lab model; copies: exact copy, quantised copy, fine-tuned derivative, distilled student; 3 unrelated models.

**Procedure**

1. Create the fingerprint or watermark using the platform's method.
2. Present each candidate model.
3. Record match results and confidence.
4. Record the number of queries or access needed.
5. Ask the vendor for the false match rate and the attacks known to defeat the method.
6. Review the evidence report format.

**Edge Cases / Variants.** Model with outputs filtered; derivative trained on heavy paraphrase.

**Expected Detection.** Exact and quantised copies identified; fine-tuned derivative identified or limitation documented; unrelated models not matched; vendor states known limits in writing; evidence report usable for escalation.

**Expected Prevention / Control Action.** Alert.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Evidence export.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Match table; evidence report.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-016"></a>

### TC-L12-016: Safety Evaluation Baseline for Deployed Models

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4, D3 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: R \| Partial: G |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (evaluation control) |
| **OWASP LLM / GenAI Mapping** | LLM09:2025 Misinformation; LLM01:2025 Prompt Injection (policy robustness) |
| **NIST AI RMF Mapping** | MEASURE 2.6; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) Adversarial Testing and Continuous Evaluation |

**Risk Addressed.** Models differ in how they handle policy-boundary requests, and tuning or version change can shift behaviour without notice.

**Business Scenario.** Risk owners want a repeatable safety score before go-live and after every change.

**Technical Scenario.** Run an agreed benign test set probing policy boundaries on each model and compare.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 150 benign test prompts across 6 policy categories (for example restricted internal topics, impersonation, privacy requests, unsafe instructions in mild form, bias-sensitive questions, regulated advice); expected behaviour defined per prompt; 3 models.

**Procedure**

1. Agree the expected-behaviour rubric and thresholds.
2. Run the set on each model.
3. Score responses automatically and manually sample 30 for human check.
4. Compare scores to thresholds.
5. Repeat after a system prompt change and after a model version change.
6. Review report content and export format.

**Edge Cases / Variants.** Same set in Arabic; adversarial rewording of prompts.

**Expected Detection.** Scores produced per category and model; automatic scoring agrees with human check on at least 90 percent of the sample; below-threshold models flagged; changes produce a comparison report.

**Expected Prevention / Control Action.** Gate on threshold.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Results export to model risk records.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Score table; human check sample.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-017"></a>

### TC-L12-017: Hallucination and Factuality Evaluation Baseline

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: R \| Partial: A |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (no direct technique) |
| **OWASP LLM / GenAI Mapping** | LLM09:2025 Misinformation |
| **NIST AI RMF Mapping** | MEASURE 2.5; MAP 2.3 |
| **Control(s) Tested** | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) Output Reliability and Content Safety |

**Risk Addressed.** Confident wrong answers cause business, legal and safety harm.

**Business Scenario.** Business owners want factual accuracy and appropriate refusal measured on their own use cases.

**Technical Scenario.** Run a factual question set with reference answers, including unanswerable questions, with and without grounding controls.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 100 answerable questions from the organisation's own fabricated knowledge base; 20 unanswerable questions; 2 models; groundedness control on and off.

**Procedure**

1. Run questions on each model without controls.
2. Score correctness against reference answers.
3. Score refusal behaviour on unanswerable items.
4. Enable groundedness controls and repeat.
5. Compare.
6. Review how the platform flags low-confidence answers to users.

**Edge Cases / Variants.** Questions requiring multi-step reasoning; questions with outdated knowledge.

**Expected Detection.** Accuracy and refusal rates reported; groundedness controls improve at least one metric without reducing the other by more than 5 points; low-confidence flags visible.

**Expected Prevention / Control Action.** Warn or suppress.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Results exportable.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Score table by model and mode.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-018"></a>

### TC-L12-018: Model Version Pinning and Behaviour Drift Detection

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, G |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |
| **Control(s) Tested** | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) AI Supply Chain and AI-BOM; [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) Adversarial Testing and Continuous Evaluation |

**Risk Addressed.** Hosted providers update models silently; behaviour, safety and cost change without a code change on the customer side.

**Business Scenario.** Operations wants version changes and behaviour drift detected quickly.

**Technical Scenario.** Pin versions, then simulate a provider update using a mock provider and monitor canary prompts.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** Mock provider with versions A and B; 30 canary prompts with expected outputs or properties (format, refusal, factual answer); 2 applications.

**Procedure**

1. Pin application to version A and record canary baseline.
2. Switch the mock provider alias to version B without notice.
3. Wait for the next canary run.
4. Check version-change alert and drift score.
5. Check which applications are affected.
6. Roll back and confirm recovery.
7. Review change history.

**Edge Cases / Variants.** Drift that affects only one language; slow drift across several updates.

**Expected Detection.** Version change detected within the canary interval and no later than 24 hours; drift quantified per canary; affected applications listed; rollback works.

**Expected Prevention / Control Action.** Alert or block on unapproved version.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Change events to SIEM.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Canary result table; alert.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-019"></a>

### TC-L12-019: Model Cards and AI-BOM Completeness

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4, D7 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) AI Supply Chain and AI-BOM |

**Risk Addressed.** Missing model documentation blocks risk review, audit and regulatory response.

**Business Scenario.** Governance wants required documentation captured and gaps visible before approval.

**Technical Scenario.** Register models with complete and incomplete documentation and check gap handling.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 8 models: 2 complete, 3 missing intended use and limitations, 2 missing training data summary, 1 missing licence; required field list agreed in advance.

**Procedure**

1. Define required fields (intended use, limitations, training data summary, evaluation results, licence, owner, version, risk tier).
2. Register the models.
3. Review gap reports.
4. Attempt production approval for an incomplete model.
5. Complete the missing fields and re-attempt.
6. Export the documentation set.

**Edge Cases / Variants.** Third-party model with no available card; model updated after approval.

**Expected Detection.** Gaps reported correctly for all 6 incomplete models; approval blocked until fields complete; export available in a structured format.

**Expected Prevention / Control Action.** Gate.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Export for audit.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Gap report; approval attempt record.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l12-020"></a>

### TC-L12-020: Model Deployment Configuration Hardening

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-032](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-032) AI Infrastructure Hardening |

**Risk Addressed.** Default settings for guardrails, tool access, logging and network exposure are often unsafe in production.

**Business Scenario.** Platform owners want a hardening baseline checked and gaps reported.

**Technical Scenario.** Run configuration checks against lab deployments with seeded weak settings.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 5 deployments with 20 seeded weaknesses: guardrails disabled, verbose error output, logging off, public network exposure, no authentication on admin routes, default credentials, unlimited tokens, unrestricted tools, debug mode on, and benign settings.

**Procedure**

1. Record seeded weaknesses.
2. Run checks.
3. Compare findings.
4. Review remediation guidance.
5. Fix five items and rerun to confirm they clear.
6. Check mapping of checks to a recognised benchmark or the vendor's own baseline.

**Edge Cases / Variants.** Settings changed after deployment (configuration drift); settings that differ per environment.

**Expected Detection.** At least 16 of 20 weaknesses detected; benign settings not flagged more than twice; findings clear after remediation; benchmark mapping stated.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to ticketing.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Check results vs seeded list.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l12-021"></a>

### TC-L12-021: Multi-Model Routing and Fallback Security

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-010](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-010) Policy Enforcement; [AI-CTRL-040](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-040) AI Service Resilience and Fail-Safe Operation |

**Risk Addressed.** Failover to a cheaper, weaker or less compliant model can bypass guardrails, residency and licence limits.

**Business Scenario.** Architecture wants fallback paths subject to the same policy as the primary.

**Technical Scenario.** Trigger failover and cost-based routing in a lab router and check policy at each destination.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** Router with a primary and 2 fallback models (one in a non-approved region, one with weaker safety scores, one approved); 30 requests with and without sensitive data.

**Procedure**

1. Run requests under normal routing.
2. Fail the primary.
3. Record where requests go.
4. Check policy decisions on fallback destinations.
5. Send sensitive data during failover.
6. Check alerts and logs.
7. Test cost-based routing rules.

**Edge Cases / Variants.** All approved models unavailable; routing rule edited under load.

**Expected Detection.** Fallbacks to non-approved region or below-threshold safety are blocked; sensitive data does not reach non-approved fallbacks; each routing decision is logged with reason.

**Expected Prevention / Control Action.** Block non-compliant fallback.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events to SIEM.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Routing log; policy decisions.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-022"></a>

### TC-L12-022: Model Resource Exhaustion and Long-Sequence Abuse

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | AML.T0029 Denial of AI Service; AML.T0034 Cost Harvesting |
| **OWASP LLM / GenAI Mapping** | LLM10:2025 Unbounded Consumption |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) AI Cost and Abuse Controls |

**Risk Addressed.** Crafted requests such as very long inputs, repetition and expansion prompts can consume disproportionate compute.

**Business Scenario.** Operations wants costly requests limited without harming legitimate long-document use.

**Technical Scenario.** Send ten request types designed to be expensive and compare cost, latency and platform handling.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** Lab inference endpoint with a mock cost meter; 10 request types: maximum-length input, repeated token input, request for maximum-length output, nested expansion prompts, many parallel requests, large image or file input, recursive tool loop, streaming held open, tiny requests at high rate, and a legitimate 40-page document summary.

**Procedure**

1. Record baseline cost and latency for typical requests.
2. Send each expensive type.
3. Record cost, latency, platform action and user message.
4. Send the legitimate long document.
5. Check per-user and global ceilings.
6. Check alerts and recovery time after a burst.

**Edge Cases / Variants.** Distributed bursts; abuse from an authenticated internal service.

**Expected Detection.** Abusive types limited or throttled before exceeding 10 times typical cost; legitimate long document completes within an agreed ceiling; alerts raised; recovery within the stated time.

**Expected Prevention / Control Action.** Limit.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Cost events to monitoring.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Cost and latency table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-023"></a>

### TC-L12-023: Quantised and Converted Model Integrity

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |
| **Control(s) Tested** | [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030) ML Pipeline and Model Registry Security |

**Risk Addressed.** Conversion and quantisation steps are places where a model can be swapped or altered while keeping a trusted name.

**Business Scenario.** Pipeline owners want provenance preserved through every transformation.

**Technical Scenario.** Convert a signed lab model and verify the chain of provenance, then tamper with the output.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 1 signed model; 2 conversions (format change, quantisation); tampering tests: altered weights file, swapped file with same name, altered metadata.

**Procedure**

1. Record the source hash and signature.
2. Run each conversion in the pipeline.
3. Check whether the platform records the transformation and links source and output.
4. Verify the output signature or attestation.
5. Tamper with the output and attempt to load.
6. Perform a conversion outside the pipeline on a laptop and attempt to register the result.

**Edge Cases / Variants.** Conversion performed by a third party; multiple chained conversions.

**Expected Detection.** Provenance chain recorded for pipeline conversions; tampered output blocked; unrecorded conversions flagged or refused registration.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Records exportable.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Chain record; load attempt results.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-024"></a>

### TC-L12-024: Model Retirement and Weight Disposal

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4, D7 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Low |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) Model Protection; [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) AI Use-Case Registry and Risk Tiering |

**Risk Addressed.** Retired models keep weights, endpoints, keys and access, extending exposure and cost.

**Business Scenario.** Governance wants retirement to remove every trace and produce evidence.

**Technical Scenario.** Retire a lab model and check for residual access and copies.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 2 models with endpoints, API keys, registry entries, cached copies and backups.

**Procedure**

1. Mark one model retired.
2. Check endpoint shutdown, key revocation, registry status and cache clearing.
3. Check access by users who previously used the model.
4. Review backups and retention statement.
5. Request a disposal evidence record.
6. Attempt to redeploy the retired version.

**Edge Cases / Variants.** Model referenced by other applications; model copies on developer laptops.

**Expected Detection.** All endpoints, keys and caches removed; redeploy blocked or requires approval; evidence record produced; backup retention stated.

**Expected Prevention / Control Action.** Remove access.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Evidence export.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Residual access checks; evidence record.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l12-025"></a>

### TC-L12-025: Model Risk Tiering and Assessment Workflow

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4, D7 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) AI Use-Case Registry and Risk Tiering |

**Risk Addressed.** Applying the same scrutiny to every model wastes effort on low risk and under-reviews high risk.

**Business Scenario.** Governance wants assessment depth to follow risk.

**Technical Scenario.** Submit models of different risk through the platform's workflow and check tiering, required assessments and approvals.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 4 models: internal summariser, customer-facing assistant, credit-style decision model, code assistant; scoring inputs (data sensitivity, autonomy, impact, exposure).

**Procedure**

1. Define the tier criteria.
2. Submit each model.
3. Compare assigned tiers with the expected ones.
4. Check required assessments per tier.
5. Complete and approve one.
6. Change a risk input after approval and check re-tiering and re-approval.
7. Check expiry and periodic review reminders.

**Edge Cases / Variants.** Model with mixed use cases; tier override with justification.

**Expected Detection.** At least 3 of 4 tiers match expectation; required assessments differ by tier; changes trigger re-tiering; reviews scheduled.

**Expected Prevention / Control Action.** Gate.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Export to GRC.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Tier table; workflow record.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l12-026"></a>

### TC-L12-026: Model Serving Workload Identity and Scoped Access to Weights

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, P |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0044 Full AI Model Access |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity; [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) Least Privilege and Scoped Credentials |

**Risk Addressed.** A serving process that runs under a broad shared identity can read every model in the store, so one compromised endpoint exposes all weights.

**Business Scenario.** Security wants each serving endpoint to run under its own identity and reach only the model it serves.

**Technical Scenario.** From each lab endpoint, attempt to read its own weights and those of other models.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 3 serving endpoints for 3 models; a weight store holding 5 models; 1 endpoint configured with a shared identity.

**Procedure**

1. List the identity each endpoint runs as.
2. From each endpoint, read its own model's weights and the weights of the other models.
3. Check that the shared identity is flagged.
4. Attempt to write to the weight store from an endpoint.
5. Use an endpoint's identity from outside the serving environment.
6. Trace one weight read back to its endpoint.

**Edge Cases / Variants.** An endpoint that serves two versions of one model; a model loaded from a local cache.

**Expected Detection.** Each endpoint reads only its own model; writes are denied; the shared identity is flagged; the identity cannot be used outside the serving environment.

**Expected Prevention / Control Action.** Allow or deny.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Decision logs to SIEM.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Access matrix; finding for the shared identity; attribution trace.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-027"></a>

### TC-L12-027: Calling Workload Attribution at Inference Endpoints: No Shared Application Keys

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MEASURE 2.8 |
| **Control(s) Tested** | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity |

**Risk Addressed.** When several applications call a model with one key, a misuse or a leak cannot be traced to its source or stopped without stopping them all.

**Business Scenario.** The SOC wants every inference call tied to one application or agent and, where there is one, to the end user.

**Technical Scenario.** Send calls to one endpoint from several applications and agents, two of which share a key.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 1 model endpoint; 4 calling applications and 2 agents; 2 of the applications sharing one key; 60 calls.

**Procedure**

1. Send the 60 calls.
2. Export the call records.
3. Check that each call names one application or agent, and the end user where one exists.
4. Check that the shared key is flagged.
5. Send a call with no workload identity.
6. Revoke one caller's key and check that the other callers are unaffected.

**Edge Cases / Variants.** A batch job calling on behalf of many users; a call routed through a gateway that replaces the caller's identity.

**Expected Detection.** Every call is attributed to one application or agent and, where present, an end user; the shared key is flagged; the call with no workload identity is refused; one key is revoked without affecting other callers.

**Expected Prevention / Control Action.** Block or alert.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Call records to SIEM.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Attribution table; finding for the shared key; revocation result.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-028"></a>

### TC-L12-028: Privileged Access to Model Weights and the Registry: Just-in-Time and Dual Approval

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, P |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0044 Full AI Model Access |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |
| **Control(s) Tested** | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) Least Privilege and Scoped Credentials; [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) Model Protection |

**Risk Addressed.** An administrator with standing access can copy or delete production weights, or change what gets promoted, with no second person involved.

**Business Scenario.** Security wants privileged actions on weights and the registry to need a time-bound grant approved by someone else.

**Technical Scenario.** Request privileged actions on a lab production registry as an administrator, with and without approval.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 2 administrators and 1 approver; a production registry with 3 models; requests to download weights, delete a version and change a promotion rule.

**Procedure**

1. Attempt each of the three actions with no grant.
2. Request a one-hour grant and have the approver approve it.
3. Repeat the three actions under the grant.
4. Have an administrator try to approve their own request.
5. Repeat an action after the grant expires.
6. Check that the session is recorded.

**Edge Cases / Variants.** An emergency request outside working hours; a grant covering one model used against another.

**Expected Detection.** No action succeeds without a grant; each grant is time-bound and approved by a second person; self-approval is refused; access ends when the grant expires; the session is recorded.

**Expected Prevention / Control Action.** Gate.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Grant and session records to SIEM.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Request and approval records; action outcomes; session record.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-029"></a>

### TC-L12-029: Tenant and Owner Isolation for Fine-Tuned Models

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, P |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0024 Exfiltration via AI Inference API |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.7; MEASURE 2.10 |
| **Control(s) Tested** | [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) Least Privilege and Scoped Credentials; [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028) Model Protection |

**Risk Addressed.** A fine-tuned model carries the data it was tuned on, so access by another team or tenant is access to that data.

**Business Scenario.** Data owners want a fine-tuned model reachable only by the team that owns it and by identities it has named.

**Technical Scenario.** Attempt to invoke, download and list three teams' fine-tuned models with each team's identity and a cross-team service identity.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 3 fine-tuned models owned by 3 teams, one tuned on restricted data; 3 team identities and 1 cross-team service identity; 24 access attempts (invoke, download, list and read training metadata).

**Procedure**

1. Record the expected outcome for the 24 attempts.
2. Run the attempts with each identity.
3. Check what each identity sees when it lists models.
4. Check what training metadata each identity can read.
5. Grant the cross-team identity access to one model and repeat.
6. Check that each denied attempt is logged with the owning team.

**Edge Cases / Variants.** A model shared with a second team for evaluation only; a base model common to all three teams.

**Expected Detection.** Each team reaches only its own model; listings show no other team's models or metadata; the cross-team identity is limited to what its grant names; all 24 outcomes match.

**Expected Prevention / Control Action.** Allow or deny.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Decision logs to SIEM.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Access matrix with expected and actual columns; denial log entries.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l12-030"></a>

### TC-L12-030: Access Recertification for Model Registry and Serving Entitlements

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity; [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) Least Privilege and Scoped Credentials |

**Risk Addressed.** Access to the registry and to endpoints builds up as people change role and applications retire, and nobody removes it.

**Business Scenario.** Governance wants entitlements on the registry and on serving endpoints reviewed on a schedule and stale ones removed.

**Technical Scenario.** Seed current and stale entitlements and run a review campaign.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 12 entitlements on the registry and endpoints: 6 current, 3 for people who changed role, 2 for service identities with no owner and 1 for a retired application.

**Procedure**

1. Seed the 12 entitlements.
2. Start a review campaign.
3. Check that each entitlement is listed with its owner and last use.
4. Check which entitlements are flagged as stale.
5. Revoke the flagged entitlements.
6. Check that access is removed and the campaign record is kept.

**Edge Cases / Variants.** A reviewer asked to certify their own access; an entitlement granted through a group.

**Expected Detection.** The campaign lists all 12 entitlements with owner and last use; the 6 stale entitlements are flagged; revocation removes access with evidence; the campaign record is retained.

**Expected Prevention / Control Action.** Revoke.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Export to GRC.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Campaign record; revocation evidence.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l12-031"></a>

### TC-L12-031: Identity Audit Trail for Model Access: Download, Load and Promotion Events

| Field | Value |
|---|---|
| **Lifecycle Layer** | L12 Model Layer |
| **Use-Case Domain(s)** | D4, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MEASURE 2.4; MANAGE 4.1 |
| **Control(s) Tested** | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) Auditability; [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) Human and Agent Identity |

**Risk Addressed.** If nobody can say who downloaded, loaded or promoted a model, a stolen or tampered model cannot be traced.

**Business Scenario.** Audit wants every access to a model recorded with the identity that made it.

**Technical Scenario.** Generate model access events from human and workload identities and inspect the logs.

**Preconditions.** Isolated PoC lab provisioned; lab model hosting, test models, mock registry and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); platform connected to the lab model environment with least-privilege test credentials. Lab model hosting with small open-weight test models, a mock model registry, harmless EICAR-style marker artefacts (a file that only writes a marker file when loaded, never real malware), and test users; no production models connected.

**Test Data.** 10 events across the registry and serving: 3 downloads, 3 loads, 2 promotions, 1 deletion and 1 denied download; a mix of human and workload identities.

**Procedure**

1. Generate the 10 events.
2. Export the logs.
3. Check that each event records the identity, model, version, hash, source address and decision.
4. Check that workload events name the owning team.
5. Check that the denied download is logged.
6. Search for the events in the lab SIEM.

**Edge Cases / Variants.** A download through a mirror or cache; a promotion performed by a pipeline.

**Expected Detection.** All 10 events are logged with identity, model, version, hash, source address and decision; workload events name the owning team; the denied download is logged; the events reach the SIEM.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Model finding or decision visible in the model security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events to SIEM.

**Forensic Evidence.** Model identifier, version, hash, source, requesting identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Event log export; field completeness table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

