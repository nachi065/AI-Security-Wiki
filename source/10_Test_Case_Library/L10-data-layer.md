---
title: "L10 Data Layer"
parent: "Test Case Library"
nav_order: 13
---

<a id="top"></a>

# L10 Data Layer

**Primary test focus:** sensitive-data classification, DLP, lineage, tenant isolation

**Cases:** 30 (TC-L10-001 to TC-L10-030)  |  **Batch:** 2

> **Safety boundary.** Injection and jailbreak cases use benign canary strings and mock tools only. Each case first measures whether the attack succeeds against the unprotected application, so that only effective payloads are scored.

> **Verify before use.** MITRE ATLAS, OWASP LLM and NIST AI RMF identifiers must be checked against the current published versions. Numeric thresholds are starting values to tune. See the [Reference Index](00-reference-index.md) for field definitions and applicability codes.

## Cases in this layer

| ID | Title | Severity | Method | Domain(s) |
|---|---|---|---|---|
| [TC-L10-001](#tc-l10-001) | Sensitive Data Discovery in AI Data Stores | Critical | Technical | D6 |
| [TC-L10-002](#tc-l10-002) | Classification Accuracy on Structured Data | High | Technical | D6 |
| [TC-L10-003](#tc-l10-003) | Classification Accuracy on Unstructured Documents | High | Technical | D6 |
| [TC-L10-004](#tc-l10-004) | Classification of Arabic and Regional-Language Documents | High | Technical | D6, D7 |
| [TC-L10-005](#tc-l10-005) | Label Inheritance to AI Outputs and Derived Data | High | Technical | D6 |
| [TC-L10-006](#tc-l10-006) | Label-Aware Access: AI Cannot Read Beyond User Entitlement | Critical | Technical | D6 |
| [TC-L10-007](#tc-l10-007) | Field-Level Masking and Data Minimisation Before the Model | High | Technical | D6 |
| [TC-L10-008](#tc-l10-008) | Data Lineage: Source to Prompt to Output | High | Evidence | D6 |
| [TC-L10-009](#tc-l10-009) | Lineage for Knowledge Base and Dataset Versions | Medium | Evidence | D6 |
| [TC-L10-010](#tc-l10-010) | Tenant Isolation in Shared AI Data Stores | Critical | Technical | D6, D3 |
| [TC-L10-011](#tc-l10-011) | Tenant Isolation Under Adversarial Probing | Critical | Technical | D6, D3 |
| [TC-L10-012](#tc-l10-012) | Data Residency: Processing Region Enforcement | Critical | Technical | D7 |
| [TC-L10-013](#tc-l10-013) | Data Residency: Logs, Telemetry, Backups and Support Access | Critical | Evidence | D7 |
| [TC-L10-014](#tc-l10-014) | Cross-Border Transfer Detection to Non-Approved Providers | High | Technical | D7, D6 |
| [TC-L10-015](#tc-l10-015) | Encryption and Key Ownership (BYOK and HYOK) | High | Evidence | D7 |
| [TC-L10-016](#tc-l10-016) | Key Rotation and Crypto-Shredding | Medium | Technical | D7 |
| [TC-L10-017](#tc-l10-017) | Dataset Access Control for AI Service Identities | Critical | Technical | D6 |
| [TC-L10-018](#tc-l10-018) | Oversharing Discovery: Data Reachable by AI Assistants Beyond Need | Critical | Technical | D6 |
| [TC-L10-019](#tc-l10-019) | Bulk Data Extraction Through AI Queries | High | Technical | D6 |
| [TC-L10-020](#tc-l10-020) | Retention and Deletion Across the AI Pipeline | High | Evidence | D7, D6 |
| [TC-L10-021](#tc-l10-021) | Erasure Propagation to Vector Stores and Derived Data | High | Technical | D7, D6 |
| [TC-L10-022](#tc-l10-022) | Data Subject Access Request Support | Medium | Evidence | D7, D6 |
| [TC-L10-023](#tc-l10-023) | Production Data in Development and Test AI Environments | High | Technical | D6, D2 |
| [TC-L10-024](#tc-l10-024) | Ingestion Validation for Untrusted Data Sources | High | Technical | D6, D3 |
| [TC-L10-025](#tc-l10-025) | Provider Data-Use Terms: Zero Retention and No Training Verification | Critical | Attestation | D7 |
| [TC-L10-026](#tc-l10-026) | Data Access Forensics: Who Accessed What via AI | High | Technical | D6 |
| [TC-L10-027](#tc-l10-027) | Insider Investigation Workflow and Case Management | Medium | Technical | D6 |
| [TC-L10-028](#tc-l10-028) | Legal Hold and eDiscovery for AI Conversations | Medium | Evidence | D7 |
| [TC-L10-029](#tc-l10-029) | Classification and Label Synchronisation with Enterprise Tools | Medium | Technical | D6 |
| [TC-L10-030](#tc-l10-030) | Leakage Metrics and Regulatory Reporting Evidence | Medium | Evidence | D7 |

---

## Test cases

<a id="tc-l10-001"></a>

### TC-L10-001: Sensitive Data Discovery in AI Data Stores

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P \| Partial: E |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** AI projects copy data into buckets, notebooks, vector stores and shared drives that security has never scanned.

**Business Scenario.** Data owners want to know where sensitive data sits across the stores that feed AI systems.

**Technical Scenario.** Point the platform at a set of test stores containing seeded sensitive records and measure what it finds.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 5 test stores (object storage bucket, file share, relational database, vector store export, notebook folder); 200 seeded records across 6 categories (personal data, financial, health-style, credentials, confidential documents, source code); 200 non-sensitive look-alikes.

**Procedure**

1. Record the seeded ground truth by store and category.
2. Connect the platform to each store using least-privilege read access.
3. Run discovery and record scan time.
4. Compare findings to ground truth to compute recall and precision per store and category.
5. Add 20 new sensitive records to one store and measure time to detection.
6. Check that scanning does not copy data out of the store or retain content.

**Edge Cases / Variants.** Compressed archives; very large files; databases with JSON columns; stores in a different region.

**Expected Detection.** Recall of at least 90 percent and precision of at least 85 percent overall; every store type supported or its absence documented; new records found within the vendor's stated rescan interval; no content retained outside the environment.

**Expected Prevention / Control Action.** N/A (discovery control).

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings exportable to a data catalogue or SIEM.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Ground-truth and findings comparison; scan duration; data-handling statement.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-002"></a>

### TC-L10-002: Classification Accuracy on Structured Data

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** Misclassified columns lead to over- or under-protection of data feeding AI features.

**Business Scenario.** Data governance wants column-level classification validated against a known answer key.

**Technical Scenario.** Run classification on a test database and table set with labelled columns.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 3 tables, 60 columns, 10,000 rows: name, contact, ID numbers, salary, card-like data, free-text notes with embedded personal data, and ordinary business columns; answer key per column.

**Procedure**

1. Seed tables and answer key.
2. Run classification.
3. Compare labels to the answer key at column level.
4. Check confidence scores and sampling method.
5. Review misclassifications for pattern.
6. Obscure column names (col1, col2) and rerun to test content-based detection.

**Edge Cases / Variants.** Columns with mixed content; sparse columns; very wide tables.

**Expected Detection.** At least 90 percent column accuracy with meaningful names and at least 80 percent with obscured names; free-text personal data found in at least 70 percent of notes columns.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Labels exportable to catalogue.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Column accuracy table; confusion list.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-003"></a>

### TC-L10-003: Classification Accuracy on Unstructured Documents

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, E |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** Documents carry the most valuable sensitive content and are what retrieval systems ingest.

**Business Scenario.** Data governance wants document classification tested against a labelled corpus.

**Technical Scenario.** Classify a mixed corpus of fabricated documents with known sensitivity labels.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 300 documents (contracts, HR letters, financial reports, meeting notes, public brochures, source code) with an answer key of 4 levels (Public, Internal, Confidential, Restricted); formats DOCX, PDF, XLSX, TXT.

**Procedure**

1. Load corpus.
2. Run classification.
3. Compare to the answer key.
4. Compute accuracy per level and confusion matrix.
5. Focus on Restricted recall.
6. Review documents classified lower than the key (under-classification) as a separate risk count.

**Edge Cases / Variants.** Documents with a few sensitive lines in a long public text; scanned PDFs.

**Expected Detection.** Restricted recall at least 90 percent; overall accuracy at least 80 percent; under-classification of Confidential or Restricted below 5 percent.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Labels exportable.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Confusion matrix; list of under-classified documents.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-004"></a>

### TC-L10-004: Classification of Arabic and Regional-Language Documents

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D6, D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, E |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** Classification trained on English leaves local-language content unprotected.

**Business Scenario.** Compliance in the GCC wants parity for Arabic and bilingual documents.

**Technical Scenario.** Classify a bilingual corpus with an answer key.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 120 documents: 40 Arabic, 40 English, 40 bilingual, covering the same categories; Arabic-Indic digits in some.

**Procedure**

1. Load corpus.
2. Run classification.
3. Compute accuracy per language set.
4. Check handling of right-to-left layout in PDF and DOCX.
5. Record entity detection for Arabic names and ID numbers.
6. Ask the vendor to tune one miss and measure effort.

**Edge Cases / Variants.** Dialect text; transliterated names.

**Expected Detection.** Arabic and bilingual accuracy within 10 points of English; entity detection for Arabic names at least 80 percent; tuning completed within a working day.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Language shown in findings.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Per-language accuracy table.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-005"></a>

### TC-L10-005: Label Inheritance to AI Outputs and Derived Data

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: A, G, P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** If a summary of a Restricted document is stored as unlabelled text, protection is lost the moment AI touches the data.

**Business Scenario.** Governance wants derived content to inherit the highest sensitivity of its sources.

**Technical Scenario.** Have a test assistant generate summaries and extracts from labelled documents and examine labels on outputs.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 10 documents at differing labels; assistant that summarises one or several; output saved to a store.

**Procedure**

1. Summarise a single Restricted document.
2. Summarise a Public and a Confidential document together.
3. Save outputs.
4. Inspect labels or markings applied.
5. Attempt to share the unlabelled output through a controlled channel and check enforcement.
6. Review audit entries linking output to source labels.

**Edge Cases / Variants.** Outputs pasted into a new document; outputs from different sessions combined.

**Expected Detection.** Output label equals highest source label in at least 9 of 10 cases; sharing blocked or flagged by label; link between output and sources recorded.

**Expected Prevention / Control Action.** Apply or enforce label.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Labels recognised by the enterprise labelling tool.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Output label table; sharing test.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-006"></a>

### TC-L10-006: Label-Aware Access: AI Cannot Read Beyond User Entitlement

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: A, P |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** Assistants that run with broad permissions expose content to users who would be denied direct access.

**Business Scenario.** Security wants the AI to retrieve only what the requesting user may see.

**Technical Scenario.** Ask questions whose answers exist only in documents the user is not entitled to read.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 3 users with different entitlements; 30 documents with access lists; 40 questions answerable only from restricted documents or from permitted ones.

**Procedure**

1. Map document ACLs.
2. Ask all questions as each user.
3. Record whether answers contain restricted content.
4. Check that refusals do not reveal the existence or title of restricted documents.
5. Change a user's access and repeat to test propagation time.

**Edge Cases / Variants.** Nested groups; document with shared link; inherited folder permissions.

**Expected Detection.** Zero restricted content in answers; no document titles leaked in refusals; access change effective within the documented time and no later than 1 hour.

**Expected Prevention / Control Action.** Filter retrieval by entitlement.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** User and document identifiers in logs.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Question and answer table; propagation timing.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-007"></a>

### TC-L10-007: Field-Level Masking and Data Minimisation Before the Model

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** Sending whole records to a model when only a few fields are needed multiplies exposure.

**Business Scenario.** Privacy wants only necessary fields reaching the model.

**Technical Scenario.** Pass records through the platform with field-level policies and inspect what the model receives.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 200 fabricated customer records with 12 fields; 3 use cases needing different fields; mock model that logs input.

**Procedure**

1. Define policies by use case.
2. Send records.
3. Inspect mock model input.
4. Verify unneeded fields removed or masked.
5. Check the response still meets the use case.
6. Change policy and repeat.

**Edge Cases / Variants.** Free-text field containing personal data; nested JSON fields.

**Expected Detection.** Unneeded fields absent from model input in 100 percent of cases; use-case answers still correct in at least 95 percent; policy change effective in under 5 minutes.

**Expected Prevention / Control Action.** Mask or remove fields.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Policy export.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Mock model input captures.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-008"></a>

### TC-L10-008: Data Lineage: Source to Prompt to Output

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D6 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: P, A |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Without lineage, an organisation cannot say which data produced an answer or who was exposed to it.

**Business Scenario.** Audit and investigations want to trace any answer to its sources and any source to its uses.

**Technical Scenario.** Run a set of queries and trace lineage in both directions.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 10 queries over a test knowledge base; 3 source documents later updated.

**Procedure**

1. Run the queries.
2. For three outputs, trace backwards to source documents and versions.
3. For one source, trace forwards to all outputs and users.
4. Update a source and check that lineage shows version change.
5. Export lineage.

**Edge Cases / Variants.** Outputs that combine several sources; deleted source.

**Expected Detection.** Backward and forward trace complete for all tested items; version recorded; export available.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Lineage exportable to catalogue.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Lineage graph screenshots; export.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l10-009"></a>

### TC-L10-009: Lineage for Knowledge Base and Dataset Versions

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D6 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Answers given months ago may need to be explained against the data as it then stood.

**Business Scenario.** Audit wants point-in-time reconstruction of what data an AI system could use.

**Technical Scenario.** Change a test dataset over time and reconstruct its past state.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 1 dataset with 5 monthly versions (simulated); 5 historical queries.

**Procedure**

1. Record version changes.
2. Pick a past date.
3. Ask the platform to show the data scope on that date.
4. Compare with the recorded version.
5. Check retention of version metadata.

**Edge Cases / Variants.** Dataset restored from backup; renamed dataset.

**Expected Detection.** Past state reconstructed correctly for all 5 dates; metadata retained for the stated period.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Exportable timeline.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Timeline export; comparison.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l10-010"></a>

### TC-L10-010: Tenant Isolation in Shared AI Data Stores

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D6, D3 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: A, P |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** Multi-tenant AI services holding data for many customers or business units must keep it strictly separate.

**Business Scenario.** Security wants logical separation proven for storage, indexes and caches.

**Technical Scenario.** Create two tenants with canary data and test separation at each layer.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 2 tenants; 50 canary records each in storage, search index and cache; admin and normal accounts per tenant.

**Procedure**

1. Seed canaries.
2. Query each layer as tenant A for tenant B data.
3. Test with crafted identifiers and wildcard queries.
4. Test admin accounts from one tenant.
5. Review isolation architecture documentation and verify against observations.
6. Check shared cache keys.

**Edge Cases / Variants.** Identifier collisions; tenant deletion and recreation with same name.

**Expected Detection.** Zero cross-tenant canaries returned at any layer; documented isolation model matches observations; attempts logged.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Tenant ID in logs.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Probe results per layer.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-011"></a>

### TC-L10-011: Tenant Isolation Under Adversarial Probing

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D6, D3 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: A, G |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** Attackers will use the AI interface itself to ask for other tenants' information.

**Business Scenario.** Security wants conversational attempts to cross tenant boundaries stopped.

**Technical Scenario.** As a tenant A user, use direct and indirect prompts to retrieve tenant B canary data.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 30 probes: direct ask, impersonation, indirect via summarisation, guessing identifiers, prompt injection asking to ignore tenant filter; tenant B canaries.

**Procedure**

1. Baseline against the unprotected app.
2. Enable the platform.
3. Run probes.
4. Search responses for tenant B canaries.
5. Check events for cross-tenant attempt classification.

**Edge Cases / Variants.** Probes across several turns; probes via document upload.

**Expected Detection.** Zero canaries returned; at least 27 of 30 probes flagged as cross-tenant attempts.

**Expected Prevention / Control Action.** Block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Event type: cross-tenant attempt.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Probe log; canary search.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-012"></a>

### TC-L10-012: Data Residency: Processing Region Enforcement

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Data processed outside the permitted jurisdiction can breach contractual and regulatory commitments.

**Business Scenario.** Compliance wants all processing, including by third-party model providers, kept in approved regions.

**Technical Scenario.** Route requests under region policy and verify where processing occurs.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Endpoints in multiple regions available in the lab or mocked.

**Test Data.** Region policy allowing UAE only; providers with UAE, EU and US endpoints; 20 requests.

**Procedure**

1. Configure the policy.
2. Send requests that would normally route to each region.
3. Capture the actual destination of each.
4. Attempt to override region through headers or model aliases.
5. Check failure behaviour when no permitted endpoint is available.
6. Review logs for region field.

**Edge Cases / Variants.** Failover to another region; provider moves endpoint.

**Expected Detection.** All requests to permitted region only; override attempts blocked; unavailable endpoint causes safe failure rather than fallback; region recorded.

**Expected Prevention / Control Action.** Block or route.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Region field in logs.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Destination capture; override attempts.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-013"></a>

### TC-L10-013: Data Residency: Logs, Telemetry, Backups and Support Access

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Residency promises often cover primary storage but not logs, telemetry, backups or remote support access.

**Business Scenario.** Compliance wants the full data footprint located.

**Technical Scenario.** Inventory every place data or derived data from the platform is stored or accessed.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** Vendor data-flow documents; lab tenant; list of data classes (prompts, responses, metadata, telemetry, diagnostics).

**Procedure**

1. Request a written list of locations by data class.
2. Capture telemetry destinations during use.
3. Review backup location and retention.
4. Ask who can access data for support, from where, and under what approvals.
5. Request a recent access log sample.
6. Compare written statements with observations.

**Edge Cases / Variants.** Sub-processor changes; emergency support from another region.

**Expected Detection.** Statements match observations; no data class stored or accessible outside approved regions without disclosure; support access is logged and approval based.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Evidence documents provided.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Location table; support access sample.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l10-014"></a>

### TC-L10-014: Cross-Border Transfer Detection to Non-Approved Providers

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D7, D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: E, G, P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** Staff and applications may send data to AI services hosted in non-approved jurisdictions.

**Business Scenario.** Compliance wants transfers to unapproved regions or providers detected and controlled.

**Technical Scenario.** Send test traffic to AI services in approved and non-approved jurisdictions.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 6 AI endpoints (mock) labelled by region; synthetic personal data; approved regions list.

**Procedure**

1. Configure approved regions.
2. Send traffic to each endpoint.
3. Check detection and action.
4. Check region determination method (IP, vendor knowledge base, contract data).
5. Test a CDN-fronted endpoint.
6. Review report of transfers by region.

**Edge Cases / Variants.** Provider that changes hosting region; proxy chain.

**Expected Detection.** All non-approved transfers flagged; region determination method stated; CDN case documented; report available.

**Expected Prevention / Control Action.** Block or alert.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Report exportable for compliance.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Transfer report; determination notes.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-015"></a>

### TC-L10-015: Encryption and Key Ownership (BYOK and HYOK)

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Control of encryption keys decides who can read stored AI data, including the vendor's staff.

**Business Scenario.** Security wants customer-held keys where required and strong encryption everywhere.

**Technical Scenario.** Review encryption at rest and in transit and test customer-managed key options.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** Lab tenant; customer-managed key in a test key store; TLS scanner.

**Procedure**

1. Review encryption settings for each data store.
2. Scan endpoints for TLS versions and ciphers.
3. Configure a customer-managed key.
4. Revoke the key and confirm data becomes inaccessible.
5. Restore the key and confirm recovery.
6. Document key hierarchy and who can access keys.

**Edge Cases / Variants.** Key rotation during active use; key store unavailable.

**Expected Detection.** TLS 1.2 or higher only; strong ciphers; revocation makes data unreadable within the documented time; vendor cannot read data without the key.

**Expected Prevention / Control Action.** Key control.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Key usage logs available.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Scan output; revocation test.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l10-016"></a>

### TC-L10-016: Key Rotation and Crypto-Shredding

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Rotation limits exposure from a stolen key, and key destruction is the only reliable way to delete data in some architectures.

**Business Scenario.** Security wants rotation without downtime and verifiable irreversible deletion.

**Technical Scenario.** Rotate keys under load and destroy the key for a test dataset.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 1 test dataset; customer-managed key; background traffic.

**Procedure**

1. Rotate the key during traffic.
2. Record errors and re-encryption time.
3. Create a second dataset with its own key.
4. Destroy that key.
5. Confirm data cannot be recovered including from backups the vendor controls.
6. Review the evidence of destruction.

**Edge Cases / Variants.** Rotation interrupted; destroyed key requested for recovery.

**Expected Detection.** Rotation with no failed requests beyond the documented window; destroyed-key data unrecoverable; evidence of destruction produced.

**Expected Prevention / Control Action.** Key lifecycle control.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Key events logged.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Rotation log; destruction evidence.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-017"></a>

### TC-L10-017: Dataset Access Control for AI Service Identities

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, A |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** AI services and agents often run with powerful service accounts that can read far more than any one task needs.

**Business Scenario.** Security wants AI service identities limited to the datasets they require.

**Technical Scenario.** Review and test permissions of AI service identities across test datasets.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 6 datasets; 3 AI service identities with intended access matrix; test reads and writes.

**Procedure**

1. Document intended access.
2. Extract actual permissions.
3. Compare.
4. Attempt access outside the matrix.
5. Review permissions inherited through groups and roles.
6. Check how the platform shows excessive privilege.

**Edge Cases / Variants.** Cross-account roles; temporary credentials.

**Expected Detection.** Excess permissions identified in all seeded cases; out-of-matrix access denied; privilege findings exportable.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to IAM tooling.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Matrix comparison; denied-access logs.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-018"></a>

### TC-L10-018: Oversharing Discovery: Data Reachable by AI Assistants Beyond Need

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** Productivity assistants surface any content the user technically can read, exposing overshared files.

**Business Scenario.** Security wants overshared sensitive files found before an assistant is switched on.

**Technical Scenario.** Seed overshared files and run the platform's oversharing analysis.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 100 files: 20 sensitive files shared with Everyone or large groups, 20 sensitive files shared correctly, 60 ordinary files; test collaboration tenant.

**Procedure**

1. Seed sharing settings.
2. Run analysis.
3. Compare findings to seeded exposure.
4. Check ranking by sensitivity and audience size.
5. Remediate three items from the platform and verify the change.
6. Re-run to confirm clearance.

**Edge Cases / Variants.** Link-based sharing; guest access; inherited permissions.

**Expected Detection.** At least 18 of 20 overshared sensitive files found; correctly shared files not flagged more than 2 times; remediation works and is logged.

**Expected Prevention / Control Action.** Remediate permissions.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Findings to ticketing.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Findings list; remediation log.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-019"></a>

### TC-L10-019: Bulk Data Extraction Through AI Queries

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: G, A, P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0025 Exfiltration via Cyber Means |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** Attackers and insiders can use an assistant to read and export large volumes of data conversationally.

**Business Scenario.** Security wants unusual volumes of sensitive retrieval detected and limited.

**Technical Scenario.** Run scripted large-volume queries as a normal and as an abusive user.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** Knowledge base of 5,000 fabricated records; normal user profile (5 queries per hour); abusive script (500 queries per hour and requests for lists of all records).

**Procedure**

1. Run normal usage for baseline.
2. Run the abusive script.
3. Record when throttling or alerts start.
4. Check detection of enumeration patterns ('list all', repeated paging).
5. Check what is blocked and what is logged.
6. Check that normal user is unaffected.

**Edge Cases / Variants.** Slow low-volume extraction over days; many users sharing credentials.

**Expected Detection.** Abusive pattern detected within 5 minutes or 100 queries; volume limit enforced; normal user unaffected.

**Expected Prevention / Control Action.** Throttle or block.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Alert to SIEM.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Timeline; alert.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-020"></a>

### TC-L10-020: Retention and Deletion Across the AI Pipeline

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D7, D6 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage (secondary) |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; GOVERN 1.1 |

**Risk Addressed.** Prompts, responses, caches, embeddings and logs each keep copies; deleting one location leaves the rest.

**Business Scenario.** Privacy wants retention and deletion enforced for every store the pipeline writes to.

**Technical Scenario.** Trace one prompt's data through every store and test deletion.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 1 prompt with canary content; stores: conversation history, cache, vector store, logs, analytics, backups.

**Procedure**

1. Send the prompt.
2. List every store holding data from it.
3. Set retention to the shortest period.
4. Wait or backdate.
5. Check each store.
6. Request deletion and confirm completion evidence.
7. Record backup deletion timing.

**Edge Cases / Variants.** Data copied to analytics; data in vendor support tools.

**Expected Detection.** Every store enumerated; deletion complete across all within documented time; backups addressed in writing.

**Expected Prevention / Control Action.** Deletion.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Deletion certificate or log.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Store inventory; deletion evidence.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l10-021"></a>

### TC-L10-021: Erasure Propagation to Vector Stores and Derived Data

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D7, D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: A, P |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage (secondary) |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; GOVERN 1.1 |

**Risk Addressed.** Embeddings and summaries derived from deleted personal data still leak information if left behind.

**Business Scenario.** Privacy wants erasure requests honoured in derived stores.

**Technical Scenario.** Delete a source document and a person's data and check derived stores.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 10 documents about 3 fabricated individuals; vector index; summaries; erasure request for 1 individual and 2 documents.

**Procedure**

1. Ingest and query to confirm retrieval.
2. Delete the documents and the individual.
3. Query again.
4. Inspect the vector store for residual embeddings.
5. Check summaries and caches.
6. Record time to full propagation.

**Edge Cases / Variants.** Embedding of a document chunk that merges two sources.

**Expected Detection.** Deleted content no longer retrievable; embeddings removed or provably unusable; propagation within the documented time.

**Expected Prevention / Control Action.** Deletion.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Erasure log.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Before and after queries; index inspection.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-022"></a>

### TC-L10-022: Data Subject Access Request Support

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D7, D6 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: P, A |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage (secondary) |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; GOVERN 1.1 |

**Risk Addressed.** Regulators expect organisations to locate all personal data on an individual, including in AI systems.

**Business Scenario.** Privacy wants to find all data about a named person across AI stores and outputs.

**Technical Scenario.** Run a subject search across prompts, documents and outputs.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 3 fabricated individuals referenced in 40 items across stores.

**Procedure**

1. Search for each person by name and identifiers.
2. Compare results to the seeded list.
3. Export a report.
4. Check what is excluded by design.
5. Time the process.

**Edge Cases / Variants.** Name variants; person referred to only by pronoun.

**Expected Detection.** At least 90 percent of seeded items found; export produced within an hour; gaps documented.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Report exportable.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Search results; export.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l10-023"></a>

### TC-L10-023: Production Data in Development and Test AI Environments

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D6, D2 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, E |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0057 LLM Data Leakage |
| **OWASP LLM / GenAI Mapping** | LLM02:2025 Sensitive Information Disclosure |
| **NIST AI RMF Mapping** | MEASURE 2.10; MANAGE 2.3 |

**Risk Addressed.** Developers copy production data into AI experiments, bypassing production controls.

**Business Scenario.** Security wants real data detected in non-production environments.

**Technical Scenario.** Seed realistic-looking, flagged production-like records into a dev environment and scan.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** Dev environment with 100 records of which 30 carry a production marker (fabricated signature) and 70 are synthetic.

**Procedure**

1. Scan the environment.
2. Compare findings to seeded markers.
3. Check how the platform distinguishes real from synthetic.
4. Check alerting to the data owner.
5. Test new data arriving later.

**Edge Cases / Variants.** Records re-formatted; data inside notebooks.

**Expected Detection.** At least 27 of 30 marked records found; synthetic records not flagged more than 5 times; owner alerted.

**Expected Prevention / Control Action.** Alert or quarantine.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Alerts to ticketing.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Findings list.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-024"></a>

### TC-L10-024: Ingestion Validation for Untrusted Data Sources

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D6, D3 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, A |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | AML.T0020 Poison Training Data (applied by analogy to stored context, memory and ingested data); verify against current ATLAS |
| **OWASP LLM / GenAI Mapping** | LLM04:2025 Data and Model Poisoning; LLM01:2025 Prompt Injection |
| **NIST AI RMF Mapping** | MAP 2.3; MEASURE 2.7 |

**Risk Addressed.** Data from outside sources entering knowledge bases or datasets can be tampered with or booby-trapped.

**Business Scenario.** Security wants untrusted data validated and quarantined before use.

**Technical Scenario.** Feed a mix of clean and manipulated test files into an ingestion pipeline.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 20 files: 10 clean, 10 manipulated (hidden instructions, corrupted structure, unexpected types, oversized, duplicated content with altered facts).

**Procedure**

1. Configure ingestion with validation.
2. Ingest all 20.
3. Record accepted, quarantined and rejected.
4. Review reasons.
5. Release one quarantined file manually and check audit.

**Edge Cases / Variants.** Valid file from a spoofed source; slow trickle of altered files.

**Expected Detection.** At least 8 of 10 manipulated files quarantined or rejected; clean files accepted; audit records manual releases.

**Expected Prevention / Control Action.** Quarantine.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Quarantine events logged.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Ingestion results.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-025"></a>

### TC-L10-025: Provider Data-Use Terms: Zero Retention and No Training Verification

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Attestation |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Critical |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Data sent to model providers may be retained or used for training unless terms and settings prevent it.

**Business Scenario.** Procurement wants written commitments and technical verification where possible.

**Technical Scenario.** Collect and test the provider terms, settings and any available evidence.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** Contracts and data processing terms of vendor and each model provider; settings screenshots.

**Procedure**

1. Request written statements on retention, human review and training use.
2. Verify settings in the tenant.
3. Send canary content and check provider-side logs where available.
4. Review sub-processor lists.
5. Ask for audit reports covering the claims.
6. Record exceptions such as abuse monitoring.

**Edge Cases / Variants.** Provider changes terms mid-contract.

**Expected Detection.** Written commitments cover retention and training; settings match; audit reports provided; exceptions documented.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Signed written statement from the vendor.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Documents attached to the register.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = no statement; 3 = statement without supporting detail; 5 = statement with technical detail and an offer to demonstrate.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Statements; settings evidence.

**Reviewer Notes.** Attestation scores below demonstrated evidence. Request a demonstration where possible.

[Back to layer index](#top)

---

<a id="tc-l10-026"></a>

### TC-L10-026: Data Access Forensics: Who Accessed What via AI

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | High |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** After an incident, investigators must establish which sensitive data an AI system accessed and for whom.

**Business Scenario.** Investigation wants a reliable record linking user, prompt, retrieved data and output.

**Technical Scenario.** Perform a mock incident and reconstruct events from platform records.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** Scenario: user retrieves 12 canary-labelled documents through an assistant over 2 days; investigator has only platform data.

**Procedure**

1. Run the scenario.
2. Ask the investigator to reconstruct who, what and when.
3. Verify against the scenario script.
4. Check completeness of identity, document IDs and time.
5. Export evidence with integrity protection.
6. Time the reconstruction.

**Edge Cases / Variants.** Access through a shared account; deleted conversations.

**Expected Detection.** Investigator reproduces at least 11 of 12 accesses within 1 hour; exported evidence is tamper-evident.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Evidence export for case tools.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Reconstruction notes.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-027"></a>

### TC-L10-027: Insider Investigation Workflow and Case Management

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, E, G |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Insider data-loss cases need timelines, context and evidence preserved.

**Business Scenario.** Security wants to open, work and close a case from AI-related alerts.

**Technical Scenario.** Create a case from a series of policy events by one test user.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 1 user generating 25 events across 7 days.

**Procedure**

1. Generate the events.
2. Open a case.
3. Build the user timeline.
4. Add notes, attach evidence, assign.
5. Check role separation and privacy controls on viewing identity.
6. Close and export.

**Edge Cases / Variants.** User with legitimate high usage; case spanning several tools.

**Expected Detection.** Timeline accurate; evidence preserved; role-based identity controls applied; case audit trail complete.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Case export or ticket integration.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Case file.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-028"></a>

### TC-L10-028: Legal Hold and eDiscovery for AI Conversations

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: A, P |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** AI conversations may be discoverable, and deletion during legal proceedings creates exposure.

**Business Scenario.** Legal wants holds applied and conversations exportable.

**Technical Scenario.** Place a hold on test users' conversations and attempt deletion.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 3 users; 30 conversations; hold on 1 user.

**Procedure**

1. Apply the hold.
2. Attempt deletion and retention expiry.
3. Search conversations by keyword and date.
4. Export in a standard format.
5. Release the hold and confirm normal rules resume.

**Edge Cases / Variants.** Hold applied after deletion request; multi-user threads.

**Expected Detection.** Held data retained despite deletion and expiry; search and export function; hold actions audited.

**Expected Prevention / Control Action.** Hold.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Export format documented.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Hold audit; export sample.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

<a id="tc-l10-029"></a>

### TC-L10-029: Classification and Label Synchronisation with Enterprise Tools

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D6 |
| **Test Method** | Technical |
| **Vendor Applicability** | Core: P, E, G |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (governance and policy control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | GOVERN 1.1; MANAGE 4.1 |

**Risk Addressed.** Separate classification schemes produce inconsistent protection.

**Business Scenario.** Governance wants labels from the existing labelling and DLP tools respected.

**Technical Scenario.** Connect the platform to the existing labelling solution and test label use.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 50 documents labelled in the enterprise tool; 4 label levels.

**Procedure**

1. Connect integration.
2. Check label import.
3. Edit a label in the source and check propagation time.
4. Use labelled files in AI prompts and check policy reaction.
5. Check behaviour when labels are missing.

**Edge Cases / Variants.** Label downgrade; custom label names.

**Expected Detection.** Labels imported for at least 48 of 50; propagation within 1 hour; policy uses labels; missing label default documented.

**Expected Prevention / Control Action.** Label-based policy.

**Expected Alert / Log.** Log entry with timestamp, user or application identity, device or host, destination, policy or rule matched, action taken and classification, within the vendor's documented SLA.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Integration documented.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = detected or enforced but one or more attribution or evidence fields missing, or SLA exceeded; 5 = fully met with complete evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection and Expected Prevention / Control Action are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Label comparison.

**Reviewer Notes.** Confirm evidence comes from the live PoC environment, not vendor-supplied demo data. Record the build and policy version tested.

[Back to layer index](#top)

---

<a id="tc-l10-030"></a>

### TC-L10-030: Leakage Metrics and Regulatory Reporting Evidence

| Field | Value |
|---|---|
| **Lifecycle Layer** | L10 Data Layer |
| **Use-Case Domain(s)** | D7 |
| **Test Method** | Evidence |
| **Vendor Applicability** | Core: all |
| **Risk Severity** | Medium |
| **Legacy ID** | None (new case) |
| **MITRE ATLAS Mapping** | N/A (operational and monitoring control) |
| **OWASP LLM / GenAI Mapping** | N/A |
| **NIST AI RMF Mapping** | MANAGE 4.1; MEASURE 2.4 |

**Risk Addressed.** Boards and regulators ask for measurable evidence that AI data risk is controlled.

**Business Scenario.** Compliance wants repeatable reports for management and supervisory review.

**Technical Scenario.** Generate reports from test activity and check that they answer typical regulatory questions.

**Preconditions.** Isolated PoC lab provisioned; test data stores, test tenants and fabricated records seeded per [Appendix D](appendix-d-lab-prerequisites.md); platform connected with least-privilege test credentials. Isolated data environment populated only with fabricated records; classification ground truth agreed and signed off before testing; no production data connected.

**Test Data.** 30 days of simulated activity; 10 typical questions (volume of sensitive data blocked, transfers by region, top risk users, exceptions granted, incident times).

**Procedure**

1. Load activity.
2. Run each report.
3. Check answers against the known simulated data.
4. Test scheduling and export.
5. Check report immutability and signing.

**Edge Cases / Variants.** Report across tenants; historic restatement.

**Expected Detection.** At least 9 of 10 questions answerable accurately; scheduling and export available; reports are tamper-evident.

**Expected Prevention / Control Action.** N/A.

**Expected Alert / Log.** Configuration state, audit record or export that supports the claim, with timestamp and the identity of the person who produced it.

**Expected Report / Dashboard Evidence.** Finding visible in the data security or data inventory dashboard within the documented refresh interval.

**Expected Integration Evidence.** Scheduled export.

**Forensic Evidence.** Data object identifier, location, classification, accessing identity, action and timestamp exportable for incident reconstruction.

**Compliance Evidence.** Test execution log and captured evidence retained in the Test Case Execution Register for audit.

**Scoring Criteria.** 0 = not demonstrated; 3 = partially shown or shown only on documentation; 5 = shown in the live product with exportable evidence; N/A = architecture out of scope.

**Pass Criteria.** Expected Detection are met in full within the vendor's documented SLA, and the evidence listed under Evidence to Capture is obtained from the live PoC.

**Fail Criteria.** Any seeded item is missed, the control action does not occur where required, SLA is exceeded, attribution fields are missing, or the result can only be reproduced with vendor-supplied data.

**Evidence to Capture.** Report samples.

**Reviewer Notes.** Confirm the evidence is taken from the live product in the PoC tenant. Documentation alone scores no higher than 3.

[Back to layer index](#top)

---

