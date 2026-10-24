---
title: "AI Security Audit and Evidence Checklist"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Testing and Assurance"
nav_order: 2
document_type: AI Security Wiki Reference
version: 1.1
---

# AI Security Audit and Evidence Checklist

> **Purpose:** Define the audit evidence, test procedure, owner and review frequency for each of the {{n:controls}} controls in the [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md), and the ISO/IEC 42001 management system evidence an AI audit also needs.

> **Audience:** Audit teams, governance teams, control owners, security engineering.

> **Run the audit in the workbook.** The [AI Security Audit and Evidence Checklist Template (.xlsx)](../25_Templates/05_AI_Security_Audit_and_Evidence_Checklist_Template.md) holds every control on this page with columns for sample size, result and evidence status, plus the GCC and EU checklists, a findings log and an exception register.

## How to use this page

1. **Set the scope.** List the AI systems in scope from the use-case registry ([AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011)) and select the controls that apply to them. Use the control tier to decide what a first audit covers.
2. **Request the evidence** in the Evidence Required column from the Evidence Owner, with a due date.
3. **Test design, then operation.** Check that the control as designed meets its objective, then follow the Audit Test Procedure over the evidence period using the [sampling guidance](#evidence-period-and-sampling) below.
4. **Check the evidence** against the [evidence quality criteria](#evidence-quality-criteria).
5. **Record the result** on the T08 scale used across the wiki: Effective (E), Partially effective (P), Ineffective (I) or Not tested (N, with the reason).
6. **Raise a finding** for every P or I result in the [findings log](#findings-log-fields), and record approved deviations in the [exception register](#exception-register-fields).

## Evidence by control

The tables are generated from the [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md) each time the site is built, one table per control family. To change a row, edit the control; this page follows on the next build. The Evidence Owner is the library's Control Owner.

<!-- audit-evidence -->

## Evidence period and sampling

Test each control in two steps:

- **Design:** walk one example through the control and confirm that, as built, it meets the control objective. A control that fails design is Ineffective; do not sample its operation.
- **Operation:** confirm that the control worked throughout the evidence period. For a first audit, choose a period that covers at least one full cycle of the control's review frequency. For a surveillance audit, the period is the time since the last audit.

Sample sizes below are common audit practice, not a requirement of any standard. The audit plan sets the final numbers and records why.

| How often the control operates | Suggested sample over the period |
|---|---|
| Annually or less often | 1 |
| Quarterly | 2 |
| Monthly | 2 to 3 |
| Weekly | 5 to 10 |
| Daily | 20 to 40 |
| Many times a day | 25 to 60 |
| Automated, configured once | 1, plus evidence that the configuration did not change during the period (change records or configuration history) |

Draw the sample from the full population in the system of record, such as the SIEM, the policy engine log or the registry, and not from a list the control owner prepares.

## Evidence Quality Criteria

Evidence should be:

- **Exportable.** It can leave the source system in a readable format.
- **Timestamped.** Each item shows when the event happened and when the evidence was collected.
- **Attributable** to user, device, application or agent where applicable.
- **Linked to a policy or control ID.**
- **Retained** according to approved retention requirements.
- **Sufficient** for incident reconstruction and audit sampling.
- **Complete.** The population it is drawn from is the whole population. Reconcile counts against the source, for example events in the SIEM against events at the AI gateway ([AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-009](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009)).
- **Reliable.** Prefer evidence the system generates over evidence a person prepares. Accept a screenshot only when it shows the date, the system and the context, and corroborate it with a log or configuration export.
- **Tamper-evident.** Logs and governance records are protected from silent change, for example with write-once storage, hashes or a change history ([AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038)).
- **Current.** Collected within the evidence period, with its collection date recorded.
- **Protected.** AI evidence often contains prompts, uploaded files, retrieved documents and model output, and with them personal data, secrets and confidential material. Share the minimum needed, redact or pseudonymize content the test does not need, restrict access to the audit team, and apply a retention period to the evidence pack itself ([AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017)).

## Findings Log Fields

```markdown
Finding ID:
Control ID:
AI System / Vendor:
Test Result: (P or I)
Description:
Root Cause:
Risk ID: (from the Enterprise AI Risk Register)
Severity:
Remediation Owner:
Due Date:
Status:
Closure Verified By:
Verification Date:
```

A finding is closed only after someone other than the remediation owner has verified the fix ([AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038)).

## Exception Register Fields

```markdown
Exception ID:
Control ID:
Risk ID: (from the Enterprise AI Risk Register)
AI System / Vendor:
Reason for Exception:
Residual Risk Rating:
Compensating Control:
Compensating Control Evidence:
Business Owner:
Risk Owner:
Approved By:
Approval Authority: (the level allowed to accept this rating of risk)
Approval Date:
Expiry Date:
Renewal Count:
Linked Finding ID:
Review Status:
```

Track exceptions with an expiry date and treat repeated renewals as a signal that the risk should be treated, not accepted again ([AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037)).

## ISO/IEC 42001 Management System Evidence

A certification audit against ISO/IEC 42001 tests the management system before it samples controls. The table lists the clauses and the evidence to prepare. "Cited by" lists the controls whose library entry cites the clause; "Related evidence" lists controls whose evidence helps but which do not cite it.

> **Verify before use.** Clause numbers and titles follow the structure of ISO/IEC 42001:2023. Titles the control library already cites were taken from it; the others were written from the structure of the standard and were not checked against a copy. Check them against your own copy before quoting them in an audit.

| ISO/IEC 42001 clause | Evidence to prepare | Cited by | Related evidence |
|---|---|---|---|
| 4.1 Understanding the organization and its context; 4.2 Understanding the needs and expectations of interested parties | Record of internal and external issues, interested parties and their requirements, including regulators and the organization's role for each AI system (for example provider or deployer). | [AI-CTRL-043](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-043) | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) |
| 4.3 Determining the scope of the AI management system | Scope statement naming the AI systems, activities, sites and exclusions, with the reason for each exclusion. It must match the systems in the registry. | None | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) |
| 5.1 Leadership and commitment; 5.2 AI policy; 5.3 Roles, responsibilities and authorities | Approved AI policy with review date, record of top management approval, and named roles with their authority. | None | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) |
| 6.1.2 AI risk assessment; 6.1.3 AI risk treatment | AI risk register, risk criteria, treatment plans and risk acceptance records. Clause 6.1.3 also requires a statement of applicability: each Annex A control, whether it is included, why, and its implementation status. The [ISO/IEC 42001 Crosswalk](../23_Framework_Crosswalks/05_ISO_IEC_42001_Crosswalk.md) shows which wiki controls support each Annex A control. | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) | [AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033) |
| 6.1.4 AI system impact assessment | Completed impact assessments for in-scope AI systems, with approvals dated before go-live. | None | [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042), [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) |
| 6.2 AI objectives and planning to achieve them | Measurable AI objectives with owners, targets, resources, deadlines and progress records. No wiki control covers this yet. | None | None |
| 7.2 Competence; 7.3 Awareness | Competence requirements by role, training and completion records, effectiveness checks. | [AI-CTRL-044](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-044) | [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045) |
| 7.5 Documented information | Document control: approved, versioned documents with owners and a change history. | None | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) |
| 8.1 Operational planning and control; 8.2 AI risk assessment; 8.3 AI risk treatment; 8.4 AI system impact assessment | Records showing that risk and impact assessments are rerun at planned intervals and on significant change, and that release gates are applied. | None | [AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033), [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037), [AI-CTRL-042](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-042) |
| 9.1 Monitoring, measurement, analysis and evaluation | Control effectiveness results and the measures behind them. | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) |
| 9.2 Internal audit | Internal audit programme, audit reports, and evidence that auditors were independent of the area they audited. | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | None |
| 9.3 Management review | Minutes of management reviews with their inputs, decisions and actions. | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | None |
| 10.1 Continual improvement; 10.2 Nonconformity and corrective action | Findings log with root cause, corrective action and verified closure. | [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037) |

## Preparing for ISO/IEC 42001 Certification

Certification bodies that certify AI management systems against ISO/IEC 42001 work to ISO/IEC 42006:2025, which adds AI-specific requirements to ISO/IEC 17021-1. Knowing what it asks of them helps you prepare. The clause numbers and headings below were checked against the publisher's contents preview on 15 October 2026; the clause text was not read.

| ISO/IEC 42006 clause | What it means for the organization being audited | Wiki evidence to prepare |
|---|---|---|
| 7.1.3 Specific technical competence requirements | Expect auditors, or technical experts with them, who can examine AI-specific controls, not only management-system documents. | The evidence in the tables above, by control |
| 8.4.2 Access to the documentation of the organization | Agree in advance how auditors will see confidential material such as model documentation and test results. | Evidence packs ([AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038)) |
| 9.1.3 Scope of certification | The certificate states which AI systems and activities are in scope. Make sure the scope matches the AI systems you actually run. | AI use-case registry ([AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011)) |
| 9.1.4 Determining audit time, and Annex A (normative) Audit time | Audit effort depends on the AI management system's scope. A secondary source reports that the factors include the number of AI systems, high-risk uses and third-party AI; check this against the standard. | Registry counts by risk tier; vendor AI list ([AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014)) |
| 9.6 Maintaining certification | Surveillance audits sample controls between certification cycles, so evidence must stay current. | Review dates in the control library; [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) |

When you rely on a supplier's ISO/IEC 42001 certificate, ask which AI systems it covers and which body issued it. See the [AI Security Vendor Evaluation Master Framework](../05_Vendor_Evaluation/11_AI_Security_Vendor_Evaluation_Master_Framework.md) and the [ISO/IEC AI Standards Crosswalk](../23_Framework_Crosswalks/15_ISO_IEC_AI_Standards_Crosswalk.md).

## Related pages

- [AI Security Audit and Evidence Checklist Template (.xlsx)](../25_Templates/05_AI_Security_Audit_and_Evidence_Checklist_Template.md)
- [AI Security Requirements Traceability Matrix Template (.xlsx)](../25_Templates/12_AI_Security_Requirements_Traceability_Matrix_Template.md), for a review of one system before it goes live
- [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md)
- [Risk, Control and Test Traceability](../02_Risk_Management/02G_Risk_Control_Test_Traceability.md)
- [GCC T08 AI Audit Checklist](../11_GCC_AI_Compliance/T08_Audit_Checklist.md) and [GCC Evidence Register](../11_GCC_AI_Compliance/08_Evidence_Register.md)
- [EU T08 AI Audit Checklist](../12_EU_AI_Compliance/T08_Audit_Checklist.md) and [EU Evidence Register](../12_EU_AI_Compliance/08_Evidence_Register.md)
- [ISO/IEC 42001 Crosswalk](../23_Framework_Crosswalks/05_ISO_IEC_42001_Crosswalk.md)
- [AI Security PoC Test Case Library](13_AI_Security_PoC_Test_Case_Library.md)
