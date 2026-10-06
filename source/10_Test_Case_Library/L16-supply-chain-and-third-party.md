---
title: "L16 Supply Chain & Third Party"
author: Nachiket Sathaye
parent: "Test Case Library"
nav_order: 19
---

<a id="top"></a>

# L16 Supply Chain & Third Party

**Primary test focus:** AI-BOM, model and package provenance, third-party SaaS AI risk

**Cases:** 26 (TC-L16-001 to TC-L16-026)
> **Safety boundary.** Retrieval, model, training, pipeline and supply chain cases use fabricated corpora and datasets, small lab models, mock hubs and indexes and harmless marker artefacts only (an EICAR-style file that writes a marker, never real malware). Never load untrusted model files outside an isolated sandbox, and never connect the lab to production knowledge sources, models, pipelines, registries or credentials. Cases marked Attestation rest on vendor documents and score below demonstrated evidence.

> **Verify before use.** MITRE ATLAS, OWASP LLM and NIST AI RMF identifiers must be checked against the current published versions. Numeric thresholds are starting values to tune. See the [Reference Index](00-reference-index.md) for field definitions and applicability codes.

## Cases in this layer

| ID | Title | Severity | Method | Domain(s) |
|---|---|---|---|---|
| [TC-L16-001](#tc-l16-001) | AI Bill of Materials Generation | High | Technical | D4, D7 |
| [TC-L16-002](#tc-l16-002) | AI Bill of Materials Format, Export and Vulnerability Linkage | Medium | Evidence | D4, D7 |
| [TC-L16-003](#tc-l16-003) | Model Provenance Verification for Hub-Sourced Models | Critical | Technical | D4 |
| [TC-L16-004](#tc-l16-004) | Malicious or Typosquatted Model and Package Detection | Critical | Technical | D4 |
| [TC-L16-005](#tc-l16-005) | Third-Party Model Repository Scanning at Download | High | Technical | D4 |
| [TC-L16-006](#tc-l16-006) | Known Vulnerabilities in AI Frameworks and Serving Components | High | Technical | D4 |
| [TC-L16-007](#tc-l16-007) | Dependency Confusion and Build-Time Substitution in AI SDKs | High | Technical | D4, D2 |
| [TC-L16-008](#tc-l16-008) | Third-Party SaaS AI Feature and Vendor Risk Assessment | High | Evidence | D1, D7 |
| [TC-L16-009](#tc-l16-009) | Third-Party Assurance Evidence (SOC 2, ISO 27001, ISO/IEC 42001) | Medium | Attestation | D7 |
| [TC-L16-010](#tc-l16-010) | Sub-Processor and Model-Provider Chain Visibility | High | Evidence | D7 |
| [TC-L16-011](#tc-l16-011) | Contractual Data Use, Training Opt-Out and Breach Notification Terms | High | Attestation | D7 |
| [TC-L16-012](#tc-l16-012) | Provider Outage, API Change and Exit Resilience | Medium | Technical | D7 |
| [TC-L16-013](#tc-l16-013) | Provider Model Deprecation and Behaviour Change Monitoring | Medium | Technical | D4 |
| [TC-L16-014](#tc-l16-014) | Open-Source Licence Compliance for Models, Datasets and Code | Medium | Technical | D7 |
| [TC-L16-015](#tc-l16-015) | Agent Framework and SDK Supply Chain Integrity | High | Technical | D5, D4 |
| [TC-L16-016](#tc-l16-016) | Third-Party Prompt and Template Pack Vetting | Medium | Technical | D3 |
| [TC-L16-017](#tc-l16-017) | Container Base Image and GPU Driver Supply Chain | Medium | Technical | D4 |
| [TC-L16-018](#tc-l16-018) | Evaluated Vendor's Own Software Supply Chain and Security Programme | Critical | Attestation | D7 |
| [TC-L16-019](#tc-l16-019) | Vendor Handling of Customer Telemetry and Support Access | Critical | Attestation | D7, D6 |
| [TC-L16-020](#tc-l16-020) | Vendor Continuity, Escrow and Data Return | Medium | Attestation | D7 |
| [TC-L16-021](#tc-l16-021) | Vendor Incident Response and Breach Notification | High | Attestation | D7 |
| [TC-L16-022](#tc-l16-022) | Vendor Patch Cadence and Vulnerability Handling | High | Technical | D7 |
| [TC-L16-023](#tc-l16-023) | Fourth-Party and Concentration Risk Across AI Controls | Medium | Evidence | D7 |
| [TC-L16-024](#tc-l16-024) | Supply Chain Incident Response Exercise | High | Technical | D4, D7 |
| [TC-L16-025](#tc-l16-025) | Right to Audit and Independent Security Testing of the Vendor Platform | High | Attestation | D7 |
| [TC-L16-026](#tc-l16-026) | IDE Extension and AI Plugin Marketplace Vetting | High | Technical | D2, D4 |

---

## Test cases

<a id="tc-l16-001"></a>

### TC-L16-001: AI Bill of Materials Generation

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D4, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |

**Risk Addressed.** Without a bill of materials for models, datasets, prompts, libraries and services, an organisation cannot tell which AI components a vulnerability or recall affects.

**Business Scenario.** Supply chain owners want an AI bill of materials generated automatically for each AI application.

**Technical Scenario.** Generate bills of materials for lab applications with known components and compare content to ground truth.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** 3 applications: a RAG chatbot (hosted model, embedding model, vector store, 20 libraries, prompt templates), a classifier service (self-hosted model, dataset, 30 libraries), an agent (2 models, 4 tools, 2 MCP servers, 25 libraries).

**Procedure**

1. Record ground truth of every component, version, source and licence for each application.
2. Run generation.
3. Compare completeness by component type.
4. Check relationship data (which model uses which dataset, which tool talks to which service).
5. Update one component and regenerate to check version change tracking.
6. Time generation.

**Edge Cases / Variants.** Components loaded dynamically at runtime; hosted model versions not exposed by the provider.

**Expected Detection.** At least 90 percent of components captured per application including models, datasets, prompts and tools; relationships present; version changes reflected; generation completes within the stated time.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Export to a software supply chain or asset system.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Component comparison; relationship graph.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l16-002"></a>

### TC-L16-002: AI Bill of Materials Format, Export and Vulnerability Linkage

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D4, D7 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |

**Risk Addressed.** A bill of materials that cannot be exchanged or linked to vulnerability data has little operational value.

**Business Scenario.** Procurement and security want export in a recognised format and linkage to known issues.

**Technical Scenario.** Export the bills of materials and test import into other tools and linkage to advisories.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** Bills of materials from the previous case; a second tool able to ingest a standard format; 5 seeded component issues from public advisory-style records.

**Procedure**

1. Export in each format the vendor supports (state which, for example CycloneDX ML-BOM or SPDX AI profile, and verify against current specifications).
2. Validate against the format's schema.
3. Import into the second tool.
4. Check that seeded issues are linked to the right components.
5. Check signing or integrity of exports.

**Edge Cases / Variants.** Large exports; partial exports for one application.

**Expected Detection.** Exports validate against the stated schema and import cleanly; at least 4 of 5 seeded issues linked; exports can be signed or hashed.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Import into asset and vulnerability tools.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Validation output; import result.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l16-003"></a>

### TC-L16-003: Model Provenance Verification for Hub-Sourced Models

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |

**Risk Addressed.** Models downloaded from public hubs may be unofficial copies, altered, or published by look-alike accounts.

**Business Scenario.** Security wants publisher and integrity checked before a downloaded model is used.

**Technical Scenario.** Download lab models from a mock hub representing official, look-alike and altered sources.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** 8 models: 3 from official publishers with signatures or hashes, 2 from look-alike publisher names, 2 re-uploaded copies with changed weights, 1 with no publisher metadata.

**Procedure**

1. Set provenance policy.
2. Attempt to download and register each.
3. Record verification outcome.
4. Compare hashes with the official source.
5. Check approval for exceptions.
6. Review events.

**Edge Cases / Variants.** Publisher account renamed; model repository transferred to a new owner.

**Expected Detection.** Look-alike, altered and unknown models blocked or flagged; official models accepted; exceptions audited.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events to SIEM.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Verification table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l16-004"></a>

### TC-L16-004: Malicious or Typosquatted Model and Package Detection

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |

**Risk Addressed.** Attackers publish models and packages with names close to popular ones, relying on mistakes and automated tools.

**Business Scenario.** Developers and platform teams want such names caught at download and install time.

**Technical Scenario.** Attempt to install lab packages and models with names close to popular ones from a mock index.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** 10 mock items: 4 typosquats of well-known AI libraries and models, 2 dependency-confusion names matching internal package names, 2 recently created packages with few downloads, 2 genuine ones; all harmless.

**Procedure**

1. Set policy.
2. Attempt installs from developer workstations and from a build pipeline.
3. Record decisions and reasons.
4. Test an internal package name published to the public index.
5. Check developer messages and override workflow.

**Edge Cases / Variants.** Name differing by one character in a language with similar letters; very new genuine package.

**Expected Detection.** All 8 suspect items blocked or flagged; genuine items allowed; dependency confusion prevented; override audited.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events to SIEM.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Install attempt table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l16-005"></a>

### TC-L16-005: Third-Party Model Repository Scanning at Download

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, E |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |

**Risk Addressed.** Scanning only inside the pipeline misses models pulled directly onto workstations and notebooks.

**Business Scenario.** Security wants scanning at the point of download wherever it occurs.

**Technical Scenario.** Download test models with harmless marker artefacts to different environments.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** 6 models (including 2 with marker payloads); 3 environments: pipeline, notebook server, developer workstation.

**Procedure**

1. Enable download scanning.
2. Download each model in each environment.
3. Record scan and block outcomes.
4. Check scan time for large models.
5. Check handling of models downloaded before scanning was enabled.

**Edge Cases / Variants.** Download over a different protocol; model fetched by code at runtime.

**Expected Detection.** Marker models blocked in all environments; clean models allowed; historical downloads rescanned.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Events to SIEM.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Environment matrix.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l16-006"></a>

### TC-L16-006: Known Vulnerabilities in AI Frameworks and Serving Components

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |

**Risk Addressed.** AI frameworks and inference servers regularly disclose serious vulnerabilities.

**Business Scenario.** Security wants known vulnerabilities in AI components found and prioritised.

**Technical Scenario.** Scan lab environments running seeded older versions of AI frameworks and servers.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** 3 environments; 12 seeded components with known public issues (use only component versions and published identifiers, no exploit code); 6 current versions.

**Procedure**

1. Scan environments.
2. Compare findings with seeded versions.
3. Check prioritisation (exposure, exploitability).
4. Check time between a new advisory entry and detection.
5. Check remediation advice.

**Edge Cases / Variants.** Component present only in a container layer; vendored copies.

**Expected Detection.** At least 11 of 12 seeded components flagged; current versions not flagged; prioritisation reflects exposure; new advisories reflected within the stated time.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to ticketing.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Findings vs seeded list.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l16-007"></a>

### TC-L16-007: Dependency Confusion and Build-Time Substitution in AI SDKs

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D4, D2 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |

**Risk Addressed.** Build systems that prefer public indexes can pull attacker packages with the same name as internal ones.

**Business Scenario.** Engineering wants internal package names protected.

**Technical Scenario.** Simulate dependency confusion in the lab build.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** Internal index; mock public index; 3 internal package names; harmless higher-version packages with the same names on the public index.

**Procedure**

1. Build with default settings.
2. Observe which package is selected.
3. Enable platform protection.
4. Rebuild.
5. Check alerts.
6. Check pinning and hash enforcement.

**Edge Cases / Variants.** Namespaced packages; mirrored indexes.

**Expected Detection.** Public lookalike never selected with protection on; alerts raised; hashes enforced.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Alerts to SIEM.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Build logs.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l16-008"></a>

### TC-L16-008: Third-Party SaaS AI Feature and Vendor Risk Assessment

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D1, D7 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Approved SaaS tools add AI features and sub-processors without a new review.

**Business Scenario.** Procurement wants third-party AI use assessed continuously.

**Technical Scenario.** Register SaaS tools with varied AI features and review the assessment output.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** 10 SaaS applications with differing AI features and data access; vendor questionnaires of varied completeness.

**Procedure**

1. Register.
2. Review assessment output: AI features, data used, model provider, location.
3. Compare with seeded facts.
4. Trigger a change (new AI feature) and check alert.
5. Review risk scoring.

**Edge Cases / Variants.** Features enabled by default; features available only on higher tiers.

**Expected Detection.** At least 8 of 10 correct; change alerted; scoring explained.

**Expected Prevention / Control Action.** Flag.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Export to vendor management.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Assessment table.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l16-009"></a>

### TC-L16-009: Third-Party Assurance Evidence (SOC 2, ISO 27001, ISO/IEC 42001)

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Attestation |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Certificates and reports are only useful if scope, dates and exceptions are read, and some claims cover only part of the service.

**Business Scenario.** Procurement wants assurance evidence collected and checked for scope.

**Technical Scenario.** Request evidence from the vendor and review against the services in scope.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** Vendor-supplied reports and certificates; checklist of scope questions.

**Procedure**

1. Request reports and certificates in writing.
2. Verify issuing body, dates and scope.
3. Check whether the evaluated product and hosting locations are inside scope.
4. Review exceptions and qualified findings.
5. Check bridge letters for gaps.
6. Record anything the vendor cannot provide.

**Edge Cases / Variants.** Report covering a previous product version; certificate scope excluding the AI features.

**Expected Detection.** Current reports covering the evaluated product; exceptions understood; gaps documented; no claim relied on without sight of the document.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Signed written statement from the vendor.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Documents attached to the register.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = no statement; 3 = statement without supporting detail; 5 = statement with technical detail and an offer to demonstrate.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Evidence checklist.

**Reviewer Notes.** Attestation scores below demonstrated evidence. Request a demonstration where possible.

[Back to layer index](#top)

---

<a id="tc-l16-010"></a>

### TC-L16-010: Sub-Processor and Model-Provider Chain Visibility

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Customer data may pass through several parties, including model providers, that the customer never contracted.

**Business Scenario.** Legal and privacy want the full chain known.

**Technical Scenario.** Request and verify the sub-processor and provider list and observe traffic.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** Vendor sub-processor list; lab traffic capture; data flow diagram.

**Procedure**

1. Request the list with locations and purposes.
2. Compare with observed destinations.
3. Check notification process for changes.
4. Check contractual flow-down of obligations.
5. Test an addition of a sub-processor (mock) and the notice period.

**Edge Cases / Variants.** Sub-processors of sub-processors; optional features that add providers.

**Expected Detection.** List matches observed traffic; change notification process documented and tested; flow-down confirmed in writing.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Documents attached.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** List vs capture.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l16-011"></a>

### TC-L16-011: Contractual Data Use, Training Opt-Out and Breach Notification Terms

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Attestation |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Weak terms leave customer data open to retention, training use, slow breach notice and unclear liability, and these are very hard to fix after signature.

**Business Scenario.** Legal and procurement want the vendor's terms checked clause by clause against a written requirements list.

**Technical Scenario.** Review the vendor's draft terms and data processing agreement against a requirements checklist and record the vendor's response to each gap.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** Vendor draft terms and data processing agreement; requirements checklist with 15 items: purpose limitation, no training on customer data, retention limits, deletion on exit, sub-processor approval, audit rights, breach notice within a stated number of hours, data location, liability cap, indemnity for IP claims, security obligations, termination assistance, jurisdiction, change-of-control notice, and flow-down to model providers.

**Procedure**

1. Agree the checklist and the minimum acceptable position for each item with legal.
2. Map every item to a clause reference or mark it absent.
3. Highlight clauses that conflict with the minimum position.
4. Send a written list of requested amendments.
5. Record the vendor's response and the time taken.
6. Have the risk owner sign off any residual gaps.
7. Check that service descriptions and product documentation agree with the terms (for example on training use).

**Edge Cases / Variants.** Terms that differ by region or by product tier; terms incorporated by reference to web pages that can change.

**Expected Detection.** All mandatory items met or formally accepted as exceptions by the risk owner; vendor responds to the amendment list within 10 working days; product documentation consistent with the terms.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Signed written statement from the vendor.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Documents attached to the register.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = no statement; 3 = statement without supporting detail; 5 = statement with technical detail and an offer to demonstrate.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Clause mapping table; amendment log.

**Reviewer Notes.** Attestation scores below demonstrated evidence. Request a demonstration where possible.

[Back to layer index](#top)

---

<a id="tc-l16-012"></a>

### TC-L16-012: Provider Outage, API Change and Exit Resilience

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Dependence on one provider creates availability, price and lock-in risk, and failover paths often break policy.

**Business Scenario.** Operations wants fallback and exit options proven rather than assumed.

**Technical Scenario.** Simulate outage, slow responses and API change against mock providers and review exit arrangements.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** 3 lab applications using a mock primary provider and a mock secondary; scenarios: full outage, partial outage with errors on 30 percent of calls, slow responses at 10 times normal latency, breaking API change, price change notice.

**Procedure**

1. Record normal behaviour and policy settings for each application.
2. Fail the primary completely and record behaviour, user messages and time to fallback.
3. Check that fallback respects data, region and model policy.
4. Introduce partial errors and slow responses and check retries, timeouts and circuit breaking.
5. Introduce a breaking API change and check detection.
6. Review the written exit plan: data return, configuration export, deletion confirmation, transition support.
7. Test export of platform configuration and logs.

**Edge Cases / Variants.** Outage during a policy change; secondary provider degraded at the same time.

**Expected Detection.** Fallback within the stated time and policy-compliant; timeouts and circuit breakers prevent cascading failure; breaking change detected; exit plan complete; export works.

**Expected Prevention / Control Action.** Failover.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Alerts to operations.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Outage timeline; policy check on fallback; export samples.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l16-013"></a>

### TC-L16-013: Provider Model Deprecation and Behaviour Change Monitoring

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, G |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Providers retire or alter models on their own schedule, breaking applications and invalidating security and safety assumptions.

**Business Scenario.** Operations wants early notice, impact mapping and behaviour checks.

**Technical Scenario.** Simulate deprecation notices and behaviour changes through a mock provider and test detection and impact reporting.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** Mock provider feed with 4 announcements (deprecation, price change, new default model, safety policy change); 4 applications using different models; 25 canary prompts.

**Procedure**

1. Map applications to models in the platform.
2. Publish each announcement.
3. Check ingestion and mapping to affected applications and owners.
4. Change mock model behaviour without announcement.
5. Run canaries and check drift alerts.
6. Check the impact report content and ticket creation.
7. Check how long the platform keeps a history of changes.

**Edge Cases / Variants.** Announcement covering a model alias; deprecation with a short notice window.

**Expected Detection.** Announcements mapped to the right applications within 24 hours; silent behaviour change detected by canaries; impact report names owners and deadlines; history retained.

**Expected Prevention / Control Action.** Alert.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Tickets created automatically.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Impact report; canary results.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l16-014"></a>

### TC-L16-014: Open-Source Licence Compliance for Models, Datasets and Code

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Licence obligations differ widely and can bar commercial use, require disclosure or impose behavioural restrictions.

**Business Scenario.** Legal wants conflicts found before deployment.

**Technical Scenario.** Register components with differing licences and test detection, policy and reporting.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** 20 components: 6 permissive, 4 copyleft, 4 with non-commercial terms, 3 with responsible-use restrictions, 3 with unclear or custom terms; 3 intended uses (internal tool, customer product, research).

**Procedure**

1. Define a licence policy by use.
2. Register the components.
3. Check detected licence per component.
4. Attempt to include non-compliant components in each use.
5. Check handling of unclear licences (flag for legal review).
6. Check report content for notices and attribution.
7. Change a licence on a component and check alerting.

**Edge Cases / Variants.** Dual-licensed components; licence differs between model code and weights.

**Expected Detection.** At least 18 of 20 licences identified correctly; non-compliant use blocked or flagged; unclear licences routed to legal; attribution report produced.

**Expected Prevention / Control Action.** Gate.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Report export.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Licence table; policy test results.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l16-015"></a>

### TC-L16-015: Agent Framework and SDK Supply Chain Integrity

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D5, D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |

**Risk Addressed.** Agent frameworks and SDKs update often and run with significant privileges, so a poisoned release has wide reach.

**Business Scenario.** Engineering wants versions pinned, integrity checked and unexpected updates stopped.

**Technical Scenario.** Test version pinning and integrity checking against a mock index with a tampered release.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** 3 agent SDKs; mock index with releases 1.0, 1.1 and a tampered 1.1 with the same version number but different content; 2 applications, one pinned and one using a floating version.

**Procedure**

1. Install release 1.0 and record hashes.
2. Publish the tampered 1.1.
3. Build the pinned application.
4. Build the floating application.
5. Check detection of hash mismatch and unexpected version change.
6. Check alerts and blocking.
7. Review the lock-file and hash-pinning guidance.

**Edge Cases / Variants.** Auto-update in an IDE extension; transitive SDK update.

**Expected Detection.** Tampered release blocked or flagged in both applications; floating versions reported as a finding; hash pinning supported and enforced.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Alerts to SIEM.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Build logs; hash comparison.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l16-016"></a>

### TC-L16-016: Third-Party Prompt and Template Pack Vetting

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D3 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, A |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |

**Risk Addressed.** Downloaded prompt packs and templates can contain hidden instructions, data-collection links or excessive tool permissions.

**Business Scenario.** Governance wants third-party prompt content reviewed before use.

**Technical Scenario.** Import lab prompt packs with seeded issues and review findings.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** 5 packs: clean, hidden instruction at the end of a long template, link that sends conversation data to a lab collector, request for broad tool permissions, text under a restrictive licence.

**Procedure**

1. Define review rules.
2. Import each pack.
3. Review findings and risk rating.
4. Approve the clean pack.
5. Attempt to use a flagged pack in an application.
6. Update an approved pack and check re-review.
7. Check provenance and publisher recording.

**Edge Cases / Variants.** Pack fetched by URL at runtime; pack that changes after approval.

**Expected Detection.** All 4 flawed packs flagged correctly; clean pack approved; use of flagged pack blocked; update triggers re-review.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Report export.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Findings table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l16-017"></a>

### TC-L16-017: Container Base Image and GPU Driver Supply Chain

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |

**Risk Addressed.** GPU drivers and base images are large, privileged and rarely tracked, yet they sit below every model workload.

**Business Scenario.** Platform security wants base components inventoried and patched.

**Technical Scenario.** Scan lab GPU nodes and images with seeded outdated components.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** 2 GPU nodes; 4 images; seeded issues: outdated driver version, outdated base image, unsigned image, image from an unapproved registry, unpatched runtime component, plus current components.

**Procedure**

1. Scan nodes and images.
2. Compare findings with seeded issues.
3. Check patch recommendations.
4. Check admission control for unsigned or unapproved images.
5. Apply an update and rescan.
6. Check how the platform handles kernel-level components it cannot inspect.

**Edge Cases / Variants.** Driver installed by a node bootstrap script; image rebuilt with the same tag.

**Expected Detection.** At least 5 of 6 seeded issues found; unsigned and unapproved images blocked; limits on kernel-level visibility documented.

**Expected Prevention / Control Action.** Block at admission.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Tickets.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Scan results; admission test.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l16-018"></a>

### TC-L16-018: Evaluated Vendor's Own Software Supply Chain and Security Programme

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Attestation |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** A security product with weak internal security is a high-value target with deep access to prompts, data and endpoints.

**Business Scenario.** Procurement wants evidence of the vendor's secure development and supply chain practices before granting that access.

**Technical Scenario.** Request and review the vendor's own supply chain and security evidence and verify what can be verified in the lab.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** Evidence request list: software bill of materials for agent and gateway, recent independent penetration test summary, vulnerability disclosure policy, secure development practices, release signing, update mechanism design, access required by the agent, internal access controls for customer data.

**Procedure**

1. Issue the request list in writing.
2. Review responses for completeness and dates.
3. Verify release signing and checksum publication in the lab.
4. Analyse the agent's update mechanism: channel, integrity checks, rollback.
5. List the privileges and ports the agent and gateway need and compare with the vendor's statement.
6. Check the vendor's public vulnerability history and response times.
7. Score completeness and willingness to share.

**Edge Cases / Variants.** Vendor offers only a summary under non-disclosure; vendor acquired during evaluation.

**Expected Detection.** Bill of materials and recent independent test summary supplied; releases signed and verified; update path integrity-protected; privileges match the statement; disclosure policy published.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Signed written statement from the vendor.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Documents attached.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = no statement; 3 = statement without supporting detail; 5 = statement with technical detail and an offer to demonstrate.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Evidence checklist; signature verification output.

**Reviewer Notes.** Attestation scores below demonstrated evidence. Request a demonstration where possible.

[Back to layer index](#top)

---

<a id="tc-l16-019"></a>

### TC-L16-019: Vendor Handling of Customer Telemetry and Support Access

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D7, D6 |
| **Test Method** | Attestation |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Critical |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage (secondary) |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; GOVERN 1.1 |

**Risk Addressed.** Vendor systems and staff may see prompts, files and metadata through telemetry and support tooling, contrary to residency and confidentiality commitments.

**Business Scenario.** Privacy wants exactly what the vendor can see documented and verified.

**Technical Scenario.** Request documentation and verify telemetry content and support access behaviour in the lab.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** Vendor telemetry documentation; lab traffic capture; telemetry settings; support access process; 10 fabricated sensitive prompts.

**Procedure**

1. Request a table of every telemetry field, purpose, destination and retention.
2. Capture traffic for 24 hours of normal lab use with the fabricated prompts.
3. Compare observed fields with the table.
4. Disable optional telemetry and capture again.
5. Request the support access process: who, from where, approvals, logging, customer visibility.
6. Request a sample support access log.
7. Check masking of sensitive content in support views where demonstrable.

**Edge Cases / Variants.** Crash dumps or diagnostic bundles containing prompt content; telemetry sent during upgrades.

**Expected Detection.** Observed telemetry matches the table; no prompt content leaves except as documented; optional telemetry can be disabled; support access approved, logged and visible to the customer.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Signed written statement from the vendor.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Documents attached.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = no statement; 3 = statement without supporting detail; 5 = statement with technical detail and an offer to demonstrate.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Telemetry comparison; support log sample.

**Reviewer Notes.** Attestation scores below demonstrated evidence. Request a demonstration where possible.

[Back to layer index](#top)

---

<a id="tc-l16-020"></a>

### TC-L16-020: Vendor Continuity, Escrow and Data Return

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Attestation |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Acquisition, failure or exit can leave customers without service, configuration or data.

**Business Scenario.** Procurement wants continuity and exit arrangements evidenced.

**Technical Scenario.** Review continuity evidence and test configuration and data export.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** Vendor continuity statement; escrow or step-in terms if offered; data return process; lab tenant with configuration, policies and logs.

**Procedure**

1. Request continuity, escrow and change-of-control commitments.
2. Review financial stability indicators the vendor provides.
3. Export policies, configuration and logs from the lab tenant.
4. Check format openness and completeness.
5. Request deletion confirmation after export.
6. Review termination assistance and notice periods.

**Edge Cases / Variants.** Export of very large logs; change of control to a competitor.

**Expected Detection.** Export complete in an open format; deletion confirmation process defined; continuity commitments documented.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Signed written statement from the vendor.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Documents attached.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = no statement; 3 = statement without supporting detail; 5 = statement with technical detail and an offer to demonstrate.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Export samples; commitment summary.

**Reviewer Notes.** Attestation scores below demonstrated evidence. Request a demonstration where possible.

[Back to layer index](#top)

---

<a id="tc-l16-021"></a>

### TC-L16-021: Vendor Incident Response and Breach Notification

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Attestation |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Slow or unclear vendor notification extends damage and delays the customer's own regulatory duties.

**Business Scenario.** Security wants clear notification commitments and a tested contact path.

**Technical Scenario.** Review the vendor's incident process and run a notification drill.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** Vendor incident policy and contact list; mock incident notification scenario; customer escalation contacts.

**Procedure**

1. Review the policy for severity levels, notification times and content.
2. Verify contacts are named and available out of hours.
3. Send a mock incident notification request and measure acknowledgement and response time.
4. Request anonymised post-incident reports from the last 2 years.
5. Check how the vendor notifies about incidents at sub-processors.
6. Align with the customer's own notification obligations.

**Edge Cases / Variants.** Incident discovered by the customer first.

**Expected Detection.** Notification commitment within the agreed number of hours; acknowledgement within 1 hour in the drill; post-incident reports provided.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Signed written statement from the vendor.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Documents and contacts attached.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = no statement; 3 = statement without supporting detail; 5 = statement with technical detail and an offer to demonstrate.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Drill timeline.

**Reviewer Notes.** Attestation scores below demonstrated evidence. Request a demonstration where possible.

[Back to layer index](#top)

---

<a id="tc-l16-022"></a>

### TC-L16-022: Vendor Patch Cadence and Vulnerability Handling

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Slow patching of the security product itself leaves defenders exposed.

**Business Scenario.** Security wants evidence of timely patching and safe upgrades.

**Technical Scenario.** Review release history and test an upgrade and rollback in the lab.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** Last 12 months of release notes and advisories; lab deployment on the previous version.

**Procedure**

1. List security fixes and the time from public disclosure or report to fix.
2. Check whether critical fixes were released outside the normal cycle.
3. Upgrade the lab deployment.
4. Check policy and data preserved.
5. Roll back and check state.
6. Check emergency patch distribution and customer notification.

**Edge Cases / Variants.** Emergency patch outside the maintenance window.

**Expected Detection.** Critical fixes released within the stated time; upgrade preserves policy and data; rollback possible; emergency path exists.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Release feed subscription.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Upgrade and rollback log.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l16-023"></a>

### TC-L16-023: Fourth-Party and Concentration Risk Across AI Controls

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Medium |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Several shortlisted tools may depend on the same model provider or cloud, so one failure disables many controls at once.

**Business Scenario.** Risk owners want concentration mapped.

**Technical Scenario.** Collect dependencies for each shortlisted tool and build a concentration map.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** Dependency data for 5 tools, covering hosting provider, model providers, identity provider, telemetry services and sub-processors.

**Procedure**

1. Request dependency data from each vendor.
2. Build the map.
3. Identify shared providers and regions.
4. Score the impact of each provider failing on the full control set.
5. Review mitigations such as local models or alternative providers.

**Edge Cases / Variants.** Dependencies that appear only in failure modes.

**Expected Detection.** Shared dependencies identified; failure impact scored; mitigations recorded.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Diagram attached to the register.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Concentration map.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l16-024"></a>

### TC-L16-024: Supply Chain Incident Response Exercise

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D4, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Teams that have never practised a compromised model or package scenario respond slowly and inconsistently.

**Business Scenario.** Incident response wants the platform tested in a realistic exercise using the bill of materials.

**Technical Scenario.** Run a lab drill with a mock compromised package and a withdrawn model.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** Scenario: a package used by 6 applications is reported malicious; a model used by 2 applications is withdrawn by its publisher; bills of materials loaded for all applications.

**Procedure**

1. Start the clock and announce the scenario.
2. Use the platform to identify affected applications and owners.
3. Block the package and model.
4. Notify owners.
5. Roll back affected applications.
6. Verify no residual use.
7. Produce the incident report and lessons list.

**Edge Cases / Variants.** Scenario starting at night; incomplete bill of materials for one application.

**Expected Detection.** Affected applications identified within 30 minutes; block and rollback executed within 2 hours; owners notified; report produced.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Incident report.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Timeline; report.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l16-025"></a>

### TC-L16-025: Right to Audit and Independent Security Testing of the Vendor Platform

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Attestation |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Without the right to test or audit, customers rely entirely on the vendor's word about its controls.

**Business Scenario.** Procurement wants audit and testing rights written into the agreement.

**Technical Scenario.** Review audit rights and confirm what testing the vendor permits.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Lab environment with mock model hub, mock package index, test applications, fabricated vendor documents and test users; vendor evidence requests issued in writing before testing; no production dependencies or contracts altered.

**Test Data.** Vendor contract; testing rules of engagement; list of permitted activities.

**Procedure**

1. Request audit and testing clauses.
2. Review notice periods, scope, frequency and cost.
3. Confirm whether penetration testing of the tenant is allowed and under what rules.
4. Request recent third-party audit reports.
5. Record any restrictions on publishing findings.
6. Confirm remediation commitments for critical findings.

**Edge Cases / Variants.** Audit rights limited to certificates.

**Expected Detection.** Audit and testing rights granted for the customer or an appointed third party; remediation commitment stated; restrictions documented.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Signed written statement from the vendor.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Documents attached.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = no statement; 3 = statement without supporting detail; 5 = statement with technical detail and an offer to demonstrate.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Clause summary.

**Reviewer Notes.** Attestation scores below demonstrated evidence. Request a demonstration where possible.

[Back to layer index](#top)

---

<a id="tc-l16-026"></a>

### TC-L16-026: IDE Extension and AI Plugin Marketplace Vetting

| Field | Value |
|---|---|
| **Lifecycle Layer** | L16 Supply Chain & Third Party |
| **Use-Case Domain(s)** | D2, D4 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, P |
| **Risk Severity** | High |
| **Quick-Start Scenario** | [AI-POC-ID-004](../06_Testing_and_Assurance/13_AI_Security_PoC_Test_Case_Library.md#ide-ai-test-cases) |
| **MITRE ATLAS Mapping** | AML.T0010 AI Supply Chain Compromise |
| **OWASP LLM / GenAI Mapping** | LLM03:2025 Supply Chain |
| **NIST AI RMF Mapping** | GOVERN 6.1; MAP 4.1 |

**Risk Addressed.** Look-alike or compromised AI extensions in public marketplaces run inside the IDE with access to source code, terminals and credentials.

**Business Scenario.** Security wants extensions vetted before install, with look-alike publishers and risky permissions flagged.

**Technical Scenario.** Offer legitimate, look-alike and over-permissioned test extensions from a mock marketplace and check the vetting results.

**Preconditions.** Isolated PoC lab provisioned; mock model hub, mock package index, test applications and test users seeded per the [Lab Prerequisites appendix](appendix-lab-prerequisites.md); written vendor evidence requests issued before testing; platform connected with least-privilege test credentials. Mock extension marketplace reachable from the test workstations; mock URL endpoint that records requests.

**Test Data.** 8 test extensions: 3 legitimate; 2 look-alike names from different publishers; 1 with a post-install script that calls the mock URL; 1 requesting broad workspace and terminal access without need; 1 legitimate extension whose new version changes publisher.

**Procedure**

1. Request installation of each extension and record the verdict and reason.
2. Install the legitimate ones.
3. Publish the changed-publisher update.
4. Check for an alert on the update.
5. Export the extension risk report.

**Edge Cases / Variants.** Extension installed from a file; extension pack that pulls in others; pre-release channel.

**Expected Detection.** 5 of 5 risky extensions flagged with a reason (publisher mismatch, script behaviour, permissions or ownership change); the 3 legitimate extensions are not flagged.

**Expected Prevention / Control Action.** Risky extensions blocked from install where enforcement is claimed; the changed-publisher update is held for review.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding or inventory entry visible in the supply chain dashboard within the documented refresh interval.

**Expected Integration Evidence.** Verdicts available to endpoint management for enforcement.

**Forensic Evidence.** Component identifier, version, hash, source, publisher, decision and timestamp, plus the vendor evidence received, exportable for audit and incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Verdict table; risk report export; mock URL access log.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---
