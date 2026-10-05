---
title: "L14 MLOps / LLMOps Layer"
parent: "Test Case Library"
nav_order: 17
---

<a id="top"></a>

# L14 MLOps / LLMOps Layer

**Primary test focus:** pipeline and registry security, CI/CD gates, artifact signing

**Cases:** 20 (TC-L14-001 to TC-L14-020)  |  **Batch:** 4

> **Safety boundary.** Retrieval, model, training, pipeline and supply chain cases use fabricated corpora and datasets, small lab models, mock hubs and indexes and harmless marker artefacts only (an EICAR-style file that writes a marker, never real malware). Never load untrusted model files outside an isolated sandbox, and never connect the lab to production knowledge sources, models, pipelines, registries or credentials. Cases marked Attestation rest on vendor documents and score below demonstrated evidence.

> **Verify before use.** MITRE ATLAS, OWASP LLM and NIST AI RMF identifiers must be checked against the current published versions. Numeric thresholds are starting values to tune. See the [Reference Index](00-reference-index.md) for field definitions and applicability codes.

## Cases in this layer

| ID | Title | Severity | Method | Domain(s) |
|---|---|---|---|---|
| [TC-L14-001](#tc-l14-001) | AI Pipeline and LLMOps Tool Inventory | High | Technical | D4, D2 |
| [TC-L14-002](#tc-l14-002) | CI/CD Security Gates for AI Releases | Critical | Technical | D4, D2 |
| [TC-L14-003](#tc-l14-003) | Artefact Signing and Verification (Models, Containers, Prompts) | Critical | Technical | D4 |
| [TC-L14-004](#tc-l14-004) | Model Registry Access Control and Immutability | High | Technical | D4 |
| [TC-L14-005](#tc-l14-005) | Prompts and Configuration as Code: Review and Version Control | High | Technical | D4, D2 |
| [TC-L14-006](#tc-l14-006) | Secrets in Pipelines, Notebooks and Experiment Logs | Critical | Technical | D4, D2 |
| [TC-L14-007](#tc-l14-007) | Notebook Server Security | High | Technical | D4 |
| [TC-L14-008](#tc-l14-008) | Pipeline Runner Least Privilege | High | Technical | D4 |
| [TC-L14-009](#tc-l14-009) | Dependency Scanning for ML Libraries and Serving Images | High | Technical | D4 |
| [TC-L14-010](#tc-l14-010) | Container Image and Runtime Configuration Scanning for Model Serving | High | Technical | D4 |
| [TC-L14-011](#tc-l14-011) | Infrastructure-as-Code Scanning for AI Infrastructure | Medium | Technical | D4 |
| [TC-L14-012](#tc-l14-012) | Promotion Workflow Across Environments | High | Technical | D4 |
| [TC-L14-013](#tc-l14-013) | Rollback and Emergency Model Disable | Critical | Technical | D4, D5 |
| [TC-L14-014](#tc-l14-014) | Feature Store and Data Pipeline Integrity | Medium | Technical | D4, D6 |
| [TC-L14-015](#tc-l14-015) | Experiment Tracking Data Leakage | Medium | Technical | D6, D4 |
| [TC-L14-016](#tc-l14-016) | Post-Deployment Monitoring Coverage and Drift Signals | Medium | Technical | D4 |
| [TC-L14-017](#tc-l14-017) | Evaluation Harness and Test Set Integrity | Medium | Technical | D4 |
| [TC-L14-018](#tc-l14-018) | Shadow Deployments and Unregistered Model Endpoints | High | Technical | D4, D3 |
| [TC-L14-019](#tc-l14-019) | Pipeline Audit Trail and Change Attribution | High | Technical | D4, D7 |
| [TC-L14-020](#tc-l14-020) | Policy-as-Code Admission Control for AI Workloads | High | Technical | D4, D7 |

---

## Test cases

<a id="tc-l14-001"></a>

### TC-L14-001: AI Pipeline and LLMOps Tool Inventory

| Field | Value |
|---|---|
| **Lifecycle Layer** | L14 MLOps / LLMOps Layer |
| **Use-Case Domain(s)** | D4, D2 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (visibility control); Reconnaissance/Discovery context only |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (unmanaged AI components) |
| **NIST AI RMF Mapping** | MAP 1.1; GOVERN 6.1 |

**Risk Addressed.** ML pipelines, notebooks, orchestrators and prompt-management tools are set up by data teams outside normal engineering inventory.

**Business Scenario.** Platform security wants every pipeline and LLMOps component listed with owner, permissions and connected assets.

**Technical Scenario.** Stand up a known set of pipeline components and compare the platform's inventory with ground truth.

**Preconditions.** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.

**Test Data.** 10 components: 2 CI/CD pipelines for models, 2 orchestrated training pipelines, 2 notebook servers, 1 experiment tracker, 1 prompt-management tool, 1 feature store, 1 serving platform; each with a service account.

**Procedure**

1. Record ground truth: component, owner, service account, connected registries and data stores.
2. Deploy all components.
3. Run discovery.
4. Compare found components and links.
5. Check service account privilege reporting.
6. Add a component later and time detection.

**Edge Cases / Variants.** Notebook server run on a developer laptop; pipeline defined only in a personal repository.

**Expected Detection.** At least 9 of 10 components found; owner and service account correct for 8; registry and data store links correct for 7; new component detected within the stated interval.

**Expected Prevention / Control Action.** N/A (discovery).

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or decision visible in the pipeline security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Inventory export to the CMDB.

**Forensic Evidence.** Pipeline, stage, artefact identifier and hash, actor, approval reference, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Inventory vs ground truth.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l14-002"></a>

### TC-L14-002: CI/CD Security Gates for AI Releases

| Field | Value |
|---|---|
| **Lifecycle Layer** | L14 MLOps / LLMOps Layer |
| **Use-Case Domain(s)** | D4, D2 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, R |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Models and prompts promoted without security testing carry unknown weaknesses straight to production.

**Business Scenario.** Release owners want automated AI-specific security checks to block unsafe releases.

**Technical Scenario.** Add the platform's checks to a lab release pipeline and push releases with and without seeded issues.

**Preconditions.** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.

**Test Data.** 1 pipeline with stages build, test, scan, approve, deploy; 6 candidate releases: clean, unsafe model file, prompt with embedded secret, failed safety evaluation, failed injection test, unsigned artefact.

**Procedure**

1. Configure gates and thresholds.
2. Push each release.
3. Record the stage and reason for each block.
4. Push the clean release.
5. Measure added pipeline time.
6. Attempt to bypass a gate by editing the pipeline file and record the control response.
7. Review the gate report.

**Edge Cases / Variants.** Gate skipped by an administrator; check results older than the artefact.

**Expected Detection.** All 5 flawed releases blocked at the correct stage; clean release passes; pipeline time increase within agreed limit (for example 10 minutes); gate bypass detected or prevented.

**Expected Prevention / Control Action.** Block deployment.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or decision visible in the pipeline security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Gate results to the CI system and ticketing.

**Forensic Evidence.** Pipeline, stage, artefact identifier and hash, actor, approval reference, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Release outcome table; pipeline logs.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l14-003"></a>

### TC-L14-003: Artefact Signing and Verification (Models, Containers, Prompts)

| Field | Value |
|---|---|
| **Lifecycle Layer** | L14 MLOps / LLMOps Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |

**Risk Addressed.** Unsigned artefacts can be swapped between build and deploy without anyone noticing.

**Business Scenario.** Security wants every promoted artefact signed and verified at deploy time.

**Technical Scenario.** Sign artefacts in the pipeline and test deployment of valid, unsigned, tampered and wrongly signed artefacts.

**Preconditions.** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.

**Test Data.** 4 artefact types (model, container image, prompt template, configuration); 4 conditions each (valid, unsigned, tampered after signing, signed by an untrusted key).

**Procedure**

1. Configure signing and a verification policy.
2. Sign and deploy valid artefacts.
3. Attempt each failing condition for every artefact type (12 attempts).
4. Check admission decisions and logs.
5. Rotate the signing key and re-verify.
6. Check key custody and access.

**Edge Cases / Variants.** Signature present but certificate expired; rollback to an older signed artefact.

**Expected Detection.** All 12 failing deployments rejected; valid ones accepted; key rotation handled without outage; keys held in a managed store.

**Expected Prevention / Control Action.** Reject.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or decision visible in the pipeline security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Admission events to SIEM.

**Forensic Evidence.** Pipeline, stage, artefact identifier and hash, actor, approval reference, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Admission decision table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l14-004"></a>

### TC-L14-004: Model Registry Access Control and Immutability

| Field | Value |
|---|---|
| **Lifecycle Layer** | L14 MLOps / LLMOps Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** A writable registry lets anyone replace a production model or change its metadata.

**Business Scenario.** Platform owners want promotion rights limited and released versions immutable.

**Technical Scenario.** Test registry roles and attempt to modify released versions.

**Preconditions.** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.

**Test Data.** Registry with 3 roles (contributor, approver, admin); 5 models; released versions v1 and v2.

**Procedure**

1. Attempt uploads, promotions and deletions by each role.
2. Attempt to overwrite a released version.
3. Attempt to change metadata (owner, stage, licence).
4. Check approval requirements.
5. Check audit entries.
6. Check service account permissions used by pipelines.

**Edge Cases / Variants.** Direct storage access bypassing the registry.

**Expected Detection.** Released versions cannot be overwritten; promotion needs an approver; every change attributed; pipeline accounts limited to required actions.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or decision visible in the pipeline security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Audit export to SIEM.

**Forensic Evidence.** Pipeline, stage, artefact identifier and hash, actor, approval reference, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Role and action matrix.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l14-005"></a>

### TC-L14-005: Prompts and Configuration as Code: Review and Version Control

| Field | Value |
|---|---|
| **Lifecycle Layer** | L14 MLOps / LLMOps Layer |
| **Use-Case Domain(s)** | D4, D2 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, A |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Prompts and settings edited in production consoles change behaviour with no review or history.

**Business Scenario.** Engineering wants prompts treated as code with review, versioning and rollback.

**Technical Scenario.** Change prompts through the console and the repository and compare controls.

**Preconditions.** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.

**Test Data.** 3 applications; production prompt console; repository-based prompt workflow; 8 prompt changes including 2 containing a secret and 2 that weaken a safety rule.

**Procedure**

1. Make changes through the console.
2. Make changes through the repository with review.
3. Check detection of console drift versus repository.
4. Check scanning of prompt changes for secrets and weakened rules.
5. Roll back one change.
6. Check change history and attribution.

**Edge Cases / Variants.** Emergency edit during an incident; change made by an automation account.

**Expected Detection.** Console drift detected; secret and weakened-rule changes flagged in at least 3 of 4 cases; rollback works; history complete.

**Expected Prevention / Control Action.** Alert or block on drift.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or decision visible in the pipeline security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Change events.

**Forensic Evidence.** Pipeline, stage, artefact identifier and hash, actor, approval reference, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Change table; drift report.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l14-006"></a>

### TC-L14-006: Secrets in Pipelines, Notebooks and Experiment Logs

| Field | Value |
|---|---|
| **Lifecycle Layer** | L14 MLOps / LLMOps Layer |
| **Use-Case Domain(s)** | D4, D2 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0055 Unsecured Credentials |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** Tokens and keys end up in notebooks, pipeline variables and experiment logs that many people can read.

**Business Scenario.** Security wants secrets found and replaced by vault references.

**Technical Scenario.** Seed secrets in several pipeline locations and run detection.

**Preconditions.** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.

**Test Data.** 12 fabricated secrets distributed across notebook cells and outputs, pipeline variables, repository history, experiment tracker parameters, container build logs; 12 high-entropy but harmless strings.

**Procedure**

1. Seed secrets.
2. Run detection across all locations.
3. Compare to ground truth.
4. Check masking in the UI.
5. Check recommendations (vault reference, rotation).
6. Remove a secret and check the finding clears.
7. Check history scanning.

**Edge Cases / Variants.** Secret in a deleted commit; secret in a base64 configuration blob.

**Expected Detection.** At least 10 of 12 found; no more than 3 harmless strings flagged; secrets masked in views; findings clear after remediation.

**Expected Prevention / Control Action.** Alert; block commit.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or decision visible in the pipeline security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to ticketing.

**Forensic Evidence.** Pipeline, stage, artefact identifier and hash, actor, approval reference, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Detection table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l14-007"></a>

### TC-L14-007: Notebook Server Security

| Field | Value |
|---|---|
| **Lifecycle Layer** | L14 MLOps / LLMOps Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Notebook servers often run with open ports, shared tokens and broad cloud permissions.

**Business Scenario.** Platform security wants notebook servers hardened and monitored.

**Technical Scenario.** Assess lab notebook servers with seeded weaknesses.

**Preconditions.** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.

**Test Data.** 3 notebook servers with 10 weaknesses: no authentication, token in URL, public exposure, root execution, broad cloud role, outputs containing data, no idle shutdown, shared kernels, unrestricted internet, unencrypted disk.

**Procedure**

1. Run assessment.
2. Compare to seeded list.
3. Review risk ranking.
4. Remediate three items and rerun.
5. Check checks against a benchmark.

**Edge Cases / Variants.** Server started by a user through a self-service portal.

**Expected Detection.** At least 8 of 10 weaknesses found; remediation verified on rerun; ranking puts exposure and no authentication first.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or decision visible in the pipeline security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to ticketing.

**Forensic Evidence.** Pipeline, stage, artefact identifier and hash, actor, approval reference, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Check results.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l14-008"></a>

### TC-L14-008: Pipeline Runner Least Privilege

| Field | Value |
|---|---|
| **Lifecycle Layer** | L14 MLOps / LLMOps Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0012 Valid Accounts |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** A compromised pipeline step with broad credentials can read data, push models and reach production.

**Business Scenario.** Security wants pipeline identities scoped per stage.

**Technical Scenario.** Review and test the permissions of pipeline stages.

**Preconditions.** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.

**Test Data.** Pipeline with 5 stages; one shared broad service account versus per-stage accounts; attempted out-of-scope actions per stage.

**Procedure**

1. Extract effective permissions per stage.
2. Compare with need.
3. Attempt out-of-scope actions (build stage writing to production registry, test stage reading production data).
4. Check findings and recommendations.
5. Apply scoped accounts and retest.

**Edge Cases / Variants.** Pipelines triggered by pull requests from forks.

**Expected Detection.** Over-privilege identified for all seeded stages; out-of-scope actions blocked after scoping; recommendations specific.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or decision visible in the pipeline security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to ticketing.

**Forensic Evidence.** Pipeline, stage, artefact identifier and hash, actor, approval reference, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Permission matrix; attempt results.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l14-009"></a>

### TC-L14-009: Dependency Scanning for ML Libraries and Serving Images

| Field | Value |
|---|---|
| **Lifecycle Layer** | L14 MLOps / LLMOps Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |

**Risk Addressed.** ML stacks have deep dependency trees and large images with known vulnerabilities.

**Business Scenario.** Security wants vulnerable and suspicious dependencies found before deployment.

**Technical Scenario.** Scan lab training and serving environments with seeded vulnerable packages.

**Preconditions.** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.

**Test Data.** 2 environments; 15 seeded issues: known vulnerable ML framework versions, a vulnerable serving library, a typosquat-style package name (harmless), an unpinned dependency, an abandoned package, a package with a changed maintainer, plus clean packages.

**Procedure**

1. Scan both environments.
2. Compare findings with seeded issues.
3. Check severity and fix versions.
4. Check reachability analysis if offered.
5. Check blocking on critical findings in the pipeline.
6. Check software bill of materials output.

**Edge Cases / Variants.** Transitive dependency three levels deep; dependency pulled at runtime.

**Expected Detection.** At least 13 of 15 issues found; severity and fix guidance correct; critical findings can block builds; bill of materials exportable.

**Expected Prevention / Control Action.** Block critical.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or decision visible in the pipeline security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to ticketing and the bill of materials store.

**Forensic Evidence.** Pipeline, stage, artefact identifier and hash, actor, approval reference, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Findings vs seeded list.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l14-010"></a>

### TC-L14-010: Container Image and Runtime Configuration Scanning for Model Serving

| Field | Value |
|---|---|
| **Lifecycle Layer** | L14 MLOps / LLMOps Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |

**Risk Addressed.** Serving containers often run as root with excess capabilities and secrets baked into layers.

**Business Scenario.** Platform security wants image and runtime issues found and enforced.

**Technical Scenario.** Scan lab serving images and a test cluster.

**Preconditions.** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.

**Test Data.** 3 images and 1 cluster namespace; seeded issues: root user, secret in layer, outdated base image, privileged container, host path mount, no resource limits, open admin port, no read-only root file system.

**Procedure**

1. Scan images.
2. Scan cluster configuration.
3. Compare findings.
4. Deploy a non-compliant workload with admission control on.
5. Check blocking.
6. Fix and redeploy.

**Edge Cases / Variants.** Image rebuilt with same tag; init containers.

**Expected Detection.** At least 7 of 8 issues found; non-compliant workload blocked; compliant workload deployed.

**Expected Prevention / Control Action.** Block at admission.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or decision visible in the pipeline security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings and admission events to SIEM.

**Forensic Evidence.** Pipeline, stage, artefact identifier and hash, actor, approval reference, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Findings; admission test.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l14-011"></a>

### TC-L14-011: Infrastructure-as-Code Scanning for AI Infrastructure

| Field | Value |
|---|---|
| **Lifecycle Layer** | L14 MLOps / LLMOps Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Misconfigurations in templates for GPU clusters, vector stores and storage are replicated at scale.

**Business Scenario.** Platform security wants misconfigurations caught in code review.

**Technical Scenario.** Scan lab templates with seeded errors.

**Preconditions.** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.

**Test Data.** 4 templates with 14 seeded misconfigurations: public storage, unencrypted volume, open security group, wide IAM role, no logging, public vector store endpoint, disabled TLS, default passwords, missing tags, and clean controls.

**Procedure**

1. Scan templates.
2. Compare to seeded list.
3. Check pull-request feedback.
4. Block merge on critical findings.
5. Fix and rescan.
6. Check policy as code customisation.

**Edge Cases / Variants.** Module sourced from a public registry.

**Expected Detection.** At least 12 of 14 found; critical findings block merge; custom policy added within an hour.

**Expected Prevention / Control Action.** Block merge.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or decision visible in the pipeline security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to code review.

**Forensic Evidence.** Pipeline, stage, artefact identifier and hash, actor, approval reference, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Findings vs seeded list.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l14-012"></a>

### TC-L14-012: Promotion Workflow Across Environments

| Field | Value |
|---|---|
| **Lifecycle Layer** | L14 MLOps / LLMOps Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Skipping staging, or promoting without approval, sends untested models to production.

**Business Scenario.** Release owners want enforced promotion stages and approvals.

**Technical Scenario.** Attempt direct and staged promotions.

**Preconditions.** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.

**Test Data.** 3 environments; 3 roles; 5 promotion attempts including direct to production and approval by the author.

**Procedure**

1. Configure rules.
2. Attempt each promotion.
3. Check blocks and approvals.
4. Check segregation of duties.
5. Check audit trail.
6. Test emergency promotion procedure and its logging.

**Edge Cases / Variants.** Promotion by an automation account.

**Expected Detection.** Direct promotions blocked; author cannot approve own change; emergency path logged and reviewed.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or decision visible in the pipeline security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Audit export.

**Forensic Evidence.** Pipeline, stage, artefact identifier and hash, actor, approval reference, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Attempt table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l14-013"></a>

### TC-L14-013: Rollback and Emergency Model Disable

| Field | Value |
|---|---|
| **Lifecycle Layer** | L14 MLOps / LLMOps Layer |
| **Use-Case Domain(s)** | D4, D5 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, G |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0053 LLM Plugin Compromise |
| **OWASP LLM / GenAI Mapping** | LLM06:2025 Excessive Agency |
| **NIST AI RMF Mapping** | MEASURE 2.7; MANAGE 2.3 |

**Risk Addressed.** When a model misbehaves, teams must be able to disable it or return to a known good version fast.

**Business Scenario.** Incident response wants a tested, quick path to disable or roll back.

**Technical Scenario.** Trigger rollback and emergency disable for a running lab model.

**Preconditions.** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.

**Test Data.** 1 serving deployment with versions v1 (good) and v2 (faulty); traffic generator; 2 dependent applications.

**Procedure**

1. Deploy v2.
2. Trigger rollback.
3. Measure time to full effect.
4. Trigger emergency disable and measure.
5. Check dependent application behaviour and messages.
6. Check audit record.
7. Check required approvals during emergencies.

**Edge Cases / Variants.** Rollback during a data schema change; rollback when v1 is no longer available.

**Expected Detection.** Rollback effective within the stated time and no later than 5 minutes; disable stops traffic within 1 minute; dependent applications fail safely; audit complete.

**Expected Prevention / Control Action.** Rollback or disable.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or decision visible in the pipeline security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events to SIEM and chat.

**Forensic Evidence.** Pipeline, stage, artefact identifier and hash, actor, approval reference, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Timeline.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l14-014"></a>

### TC-L14-014: Feature Store and Data Pipeline Integrity

| Field | Value |
|---|---|
| **Lifecycle Layer** | L14 MLOps / LLMOps Layer |
| **Use-Case Domain(s)** | D4, D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0020 Poison Training Data (applied by analogy to stored context, memory and ingested data); verify against current ATLAS |
| **OWASP LLM / GenAI Mapping** | LLM04:2025 Data and Model Poisoning; LLM01:2025 Prompt Injection |
| **NIST AI RMF Mapping** | MAP 2.3; MEASURE 2.7 |

**Risk Addressed.** Tampered, stale or re-sourced features silently change model predictions without any change to the model.

**Business Scenario.** Data engineers want changes to feature pipelines detected, approved and traceable to affected models.

**Technical Scenario.** Alter features and transformations in a lab feature pipeline and test detection, approval control and lineage.

**Preconditions.** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.

**Test Data.** 1 feature store with 5 feature pipelines feeding 2 models; alterations: changed transformation code, altered stored values, schema change, stale refresh (no update for 48 simulated hours), unexpected new data source.

**Procedure**

1. Record baselines for code hashes, value distributions, schemas and refresh times.
2. Apply each alteration separately.
3. Record detection, time and alert content.
4. Check whether pipeline changes require approval and who can approve.
5. Check lineage showing which models and applications consume the altered feature.
6. Revert and confirm the alert clears.

**Edge Cases / Variants.** Gradual drift in values; change by an authorised user with a wrong parameter.

**Expected Detection.** At least 4 of 5 alterations detected within the stated interval; affected models listed; unapproved changes blocked or flagged; alerts clear after reversion.

**Expected Prevention / Control Action.** Alert or block change.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or decision visible in the pipeline security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Alerts to SIEM and data engineering chat.

**Forensic Evidence.** Pipeline, stage, artefact identifier and hash, actor, approval reference, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Detection table; lineage view.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l14-015"></a>

### TC-L14-015: Experiment Tracking Data Leakage

| Field | Value |
|---|---|
| **Lifecycle Layer** | L14 MLOps / LLMOps Layer |
| **Use-Case Domain(s)** | D6, D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** Experiment tools log prompts, outputs, sample rows and artefacts that nobody classifies, and are often visible to many users.

**Business Scenario.** Privacy wants sensitive content in tracking tools found and restricted.

**Technical Scenario.** Run lab experiments that log sensitive data and scan the tracker.

**Preconditions.** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.

**Test Data.** 3 experiments logging prompts, model outputs, sample dataset rows and attached files; 40 fabricated sensitive items (personal data, secrets, confidential markers) spread across parameters, metrics notes, artefacts and comments.

**Procedure**

1. Run the experiments.
2. Scan the tracker.
3. Compare findings with ground truth by location.
4. Check access control on runs and projects.
5. Apply retention and deletion to one project and verify.
6. Check sharing links and external exposure.
7. Check whether masking can be applied at logging time.

**Edge Cases / Variants.** Large artefacts such as model checkpoints containing data; runs imported from another tool.

**Expected Detection.** At least 36 of 40 items found; access limited to the project team; deletion complete; sharing links reported; masking available or absence documented.

**Expected Prevention / Control Action.** Mask or delete.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or decision visible in the pipeline security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to data owners.

**Forensic Evidence.** Pipeline, stage, artefact identifier and hash, actor, approval reference, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Detection table by location.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l14-016"></a>

### TC-L14-016: Post-Deployment Monitoring Coverage and Drift Signals

| Field | Value |
|---|---|
| **Lifecycle Layer** | L14 MLOps / LLMOps Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, G |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Deployments without monitoring hooks cannot show drift, misuse or degradation.

**Business Scenario.** Operations wants monitoring present on every deployment and its signals reaching the security tools.

**Technical Scenario.** Deploy models with and without monitoring and compare coverage and detection.

**Preconditions.** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.

**Test Data.** 6 deployments, 3 with monitoring hooks and 3 without; simulated input drift, output drift and anomalous traffic.

**Procedure**

1. Run a coverage check.
2. Generate each condition against all deployments.
3. Record detection in monitored deployments.
4. Check gap reports for unmonitored ones.
5. Add monitoring to one and rerun.
6. Check routing of alerts to the SOC and ownership of the response.

**Edge Cases / Variants.** Batch models; deployments behind several routers.

**Expected Detection.** Coverage gaps reported accurately; drift and anomalies detected where monitored; alerts reach the right owner within the stated time.

**Expected Prevention / Control Action.** Alert.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or decision visible in the pipeline security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Metrics and alerts to monitoring tools.

**Forensic Evidence.** Pipeline, stage, artefact identifier and hash, actor, approval reference, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Coverage report; detection table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l14-017"></a>

### TC-L14-017: Evaluation Harness and Test Set Integrity

| Field | Value |
|---|---|
| **Lifecycle Layer** | L14 MLOps / LLMOps Layer |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0020 Poison Training Data (applied by analogy to stored context, memory and ingested data); verify against current ATLAS |
| **OWASP LLM / GenAI Mapping** | LLM04:2025 Data and Model Poisoning; LLM01:2025 Prompt Injection |
| **NIST AI RMF Mapping** | MAP 2.3; MEASURE 2.7 |

**Risk Addressed.** Tampered or leaked evaluation sets make unsafe models look safe.

**Business Scenario.** Model risk owners want evaluation data protected, versioned and kept apart from training data.

**Technical Scenario.** Alter and leak evaluation data in the lab and test detection.

**Preconditions.** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.

**Test Data.** 3 evaluation sets (safety, accuracy, injection robustness) of 100 items each; alterations: remove 20 hardest items, add 15 items that overlap training data, change 10 expected answers; access list with 6 users.

**Procedure**

1. Record hashes, versions and access list.
2. Apply the alterations separately.
3. Check detection and alert content.
4. Check overlap detection between evaluation and training data.
5. Check access logging and restrictions.
6. Check that a model promotion gate uses only the approved version of each set.

**Edge Cases / Variants.** Evaluation set copied into a notebook; set updated by an authorised user without review.

**Expected Detection.** All three alteration types detected; overlap found for at least 12 of 15 items; evaluation set access limited and logged; promotion gate uses approved versions only.

**Expected Prevention / Control Action.** Alert or block promotion.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or decision visible in the pipeline security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Alerts.

**Forensic Evidence.** Pipeline, stage, artefact identifier and hash, actor, approval reference, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Detection table; gate test.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l14-018"></a>

### TC-L14-018: Shadow Deployments and Unregistered Model Endpoints

| Field | Value |
|---|---|
| **Lifecycle Layer** | L14 MLOps / LLMOps Layer |
| **Use-Case Domain(s)** | D4, D3 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, G |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (visibility control); Reconnaissance/Discovery context only |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain (unmanaged AI components) |
| **NIST AI RMF Mapping** | MAP 1.1; GOVERN 6.1 |

**Risk Addressed.** Models served outside the registry bypass every release control, scanning and monitoring step.

**Business Scenario.** Security wants unregistered endpoints found and brought under control.

**Technical Scenario.** Start unregistered endpoints in several places and test discovery and ownership resolution.

**Preconditions.** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.

**Test Data.** 4 endpoints: registered, unregistered internal, unregistered exposed to a wider segment, endpoint in a personal cloud account reachable from a managed device; 20 minutes of traffic on each.

**Procedure**

1. Start the endpoints.
2. Run discovery using network, cloud and traffic signals.
3. Compare with ground truth.
4. Check ownership resolution (account, user, project).
5. Register one endpoint and check status change.
6. Check alert routing for exposed endpoints.

**Edge Cases / Variants.** Endpoint behind a gateway; endpoint with a generic name; endpoint started for under an hour.

**Expected Detection.** All 3 unregistered endpoints found; owner resolved for at least 2; status updates after registration; exposed endpoint prioritised.

**Expected Prevention / Control Action.** Alert.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or decision visible in the pipeline security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to ticketing.

**Forensic Evidence.** Pipeline, stage, artefact identifier and hash, actor, approval reference, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Discovery results.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l14-019"></a>

### TC-L14-019: Pipeline Audit Trail and Change Attribution

| Field | Value |
|---|---|
| **Lifecycle Layer** | L14 MLOps / LLMOps Layer |
| **Use-Case Domain(s)** | D4, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Investigators need to know who changed what in a pipeline, when, and with what approval.

**Business Scenario.** Audit wants complete, tamper-evident pipeline records.

**Technical Scenario.** Make a series of changes across pipeline, registry and configuration and reconstruct them from platform records alone.

**Preconditions.** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.

**Test Data.** 12 changes by 3 users and 2 service accounts across pipeline definitions, registry entries, prompts, access rules and secrets references; 1 change made through an emergency procedure.

**Procedure**

1. Make the changes.
2. Ask an investigator to reconstruct who did what, when, and why using only platform records.
3. Check before and after values and approval references.
4. Attempt to modify or delete audit records.
5. Check time synchronisation.
6. Export records and check format.

**Edge Cases / Variants.** Changes made by automation on behalf of a user; changes across two tools with different clocks.

**Expected Detection.** At least 11 of 12 changes reconstructed; emergency change flagged; audit records protected; export in a standard format.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or decision visible in the pipeline security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Export to SIEM.

**Forensic Evidence.** Pipeline, stage, artefact identifier and hash, actor, approval reference, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Reconstruction notes.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l14-020"></a>

### TC-L14-020: Policy-as-Code Admission Control for AI Workloads

| Field | Value |
|---|---|
| **Lifecycle Layer** | L14 MLOps / LLMOps Layer |
| **Use-Case Domain(s)** | D4, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Written standards fail unless the cluster refuses non-compliant workloads at deployment.

**Business Scenario.** Platform owners want AI-specific rules enforced automatically.

**Technical Scenario.** Write and test admission rules against compliant and non-compliant workloads in the lab cluster.

**Preconditions.** Isolated PoC lab provisioned; lab CI/CD runner, mock registries, notebook server, test cluster and test users seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Lab MLOps environment with a CI/CD runner, mock model and container registries, notebook server, small training and serving pipeline, test Kubernetes cluster and test users; no production pipelines, registries or credentials connected.

**Test Data.** 10 rules: approved registries only, signed models, GPU quotas, resource limits, required ownership labels, no privileged containers, approved regions, required monitoring sidecar, no secrets in environment variables, approved network policies; 20 workloads (10 compliant, 10 breaking one rule each).

**Procedure**

1. Load the rules.
2. Deploy all 20 workloads.
3. Record admission outcomes and the messages shown to developers.
4. Update one rule and test the new behaviour.
5. Request a time-limited exception and check approval and expiry.
6. Check reporting on rejected deployments.
7. Check rule versioning in version control.

**Edge Cases / Variants.** Workloads created by operators with high privileges; rule conflicts between two policies.

**Expected Detection.** All 10 non-compliant workloads rejected with clear reasons; all compliant admitted; exceptions audited and expire; rules versioned.

**Expected Prevention / Control Action.** Reject.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or decision visible in the pipeline security dashboard within the documented refresh interval.

**Expected Integration Evidence.** Admission events to SIEM.

**Forensic Evidence.** Pipeline, stage, artefact identifier and hash, actor, approval reference, decision and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Admission table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

