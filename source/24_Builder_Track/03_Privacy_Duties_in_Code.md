---
title: "Privacy Duties in Code: Consent, Rights, Retention and Children's Data"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Builder Track"
nav_order: 3
description: "Working, tested code for the privacy duties an AI product carries under India's DPDP Act: consent per purpose and notice version, access, correction, erasure, grievance and nomination, retention with advance notice, children's data, and log redaction with keyed pseudonyms."
document_type: AI Security Wiki Reference
version: 1.0
last_reviewed: 2026-10-23
---

# Privacy Duties in Code: Consent, Rights, Retention and Children's Data

> **Purpose:** Show how the duties of a data fiduciary under India's Digital Personal Data Protection Act 2023 (DPDP) become code in an AI product, with a small reference implementation that runs and has tests.

> **Audience:** AI product developers, privacy engineers and application security engineers. The [India section](../17_India_AI_Compliance/index.md) covers the law; this page covers the build.

> **How to use:** Read the duty table, run the tests in the [`code/`](code/) folder, then copy the patterns into your own stack. Set the time limits from the text of the law and rules that apply to you. Then prove the build with the test cases at the end.

> **Verification required.** This is engineering guidance, not legal advice. Using this code does not make a system compliant with the DPDP Act or any other law. The Act's section numbers below were checked against the Act on 23 October 2026. The numbers from the DPDP Rules 2025 were read from the Hindi text only and are tagged accordingly. Most of the Rules apply from about 13 May 2027 (see the [India hub](../17_India_AI_Compliance/01_India_AI_Regulatory_Hub.md), row IN2).

## The one idea

A privacy duty that lives only in a policy is not done. Each duty needs one place in the code that enforces it, and a record that proves it was done. The pattern is the same as for agents: decide outside the model, from a declared policy, and log the decision. Here the declared policy is a **data map**: one file that says which fields are personal, the purposes each serves and how long it is kept. Storage, logging, retention and the [pipeline checks](04_Developer_Pipeline_Checks.md) all read the same file, so they cannot disagree.

## Duties, code and tests

| Duty | DPDP Act 2023 | What the code does | Where in the code | Prove it with |
|---|---|---|---|---|
| Notice before or with the consent request | s.5(1) | Consent is stored with the version of the notice shown; a new version needs new consent | `ConsentLedger.grant`, `allows` | [TC-L03-003](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-003) |
| Consent for a specified purpose, withdrawable as easily as given | s.6(1), s.6(4) | Refuses generic purposes and purposes not in the data map; withdrawal is one call | `ConsentLedger.grant`, `withdraw` | [TC-L03-004](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-004) |
| Stop processing after withdrawal | s.6(6) | `allows` returns false once withdrawn; check it before every use, including calls to a model | `ConsentLedger.allows` | [TC-L03-004](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-004) |
| Prove that notice was given and consent obtained | s.6(10) | Every grant and withdrawal goes to the hash-chained audit log | `AuditLog` from [`guard.py`](code/guard.py) | [TC-L17-004](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-004) |
| Reasonable security safeguards | s.8(5) | Personal fields are replaced by keyed pseudonyms before they reach a log; unclassified fields are refused | `RedactingLogger`, `Pseudonymiser` | [TC-L10-007](../10_Test_Case_Library/L10-data-layer.md#tc-l10-007), [TC-L17-005](../10_Test_Case_Library/L17-monitoring-detection-and-response.md#tc-l17-005) |
| Erase when consent is withdrawn or the purpose is no longer served, unless a law requires keeping it | s.8(7) | Data falls due when no purpose it serves still has consent, or after the retention period of inactivity; legal holds block erasure | `RetentionRunner`, `Store.legal_holds` | [TC-L03-016](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-016) |
| Purpose deemed no longer served after a period without contact | s.8(8) | Inactivity is measured from the last time the person approached you or used a right | `Store.last_seen`, `RightsDesk._seen` | No case yet |
| Grievance redressal mechanism | s.8(10), s.13 | Each grievance gets a ticket with a due date; overdue tickets are listed | `RightsDesk.grievance`, `overdue` | [TC-L03-009](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-009) |
| Verifiable parental consent before processing a child's data | s.9(1); "child" is under 18, s.2(f) | No processing of a child's data without a recorded parental verification; an unknown age is treated as a child | `ChildrenGate.check` | [TC-L03-017](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-017) |
| No tracking, behavioural monitoring or targeted advertising directed at children | s.9(3) | These uses are refused for children whatever the consent | `BARRED_FOR_CHILDREN` | [TC-L03-017](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-017) |
| Summary of personal data and processing, and who it was shared with | s.11(1) | Returns the data held, the purposes, the consented purposes and the processors that received each category | `RightsDesk.access` | [TC-L03-005](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-005) |
| Correction, completion, updating and erasure | s.12 | Correction and erasure, each logged; erasure respects legal holds | `RightsDesk.correct`, `erase` | [TC-L03-006](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-006), [TC-L03-007](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-007) |
| Nominate someone to exercise rights on death or incapacity | s.14 | Records the nominee and checks it before a nominee acts | `RightsDesk.nominate`, `may_act_for` | No case yet |
| Cross-border transfer | s.16 | Not enforced in code here: the data map lists each processor and its country so the transfer register can be built from it | `privacy_map.json` | [TC-L03-012](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-012) |

Section references were checked against the Act text published by MeitY, read on 23 October 2026 [Verified]. Two points that often go wrong in other material: the Act has **no "sensitive personal data" category** (it was in earlier bills), and section 7's legitimate uses contain **no general contract ground** of the kind the GDPR has. Do not build a "contract" basis into a DPDP consent model.

## The time limits are parameters

The Act leaves several time limits to the Rules. The code takes them as settings, because they must come from the text that applies to you and from the date each rule takes effect.

| Setting | Value read from the DPDP Rules 2025 | Tag |
|---|---|---|
| `RetentionRunner(notice_hours=...)`: advance notice before erasure for lack of contact | At least 48 hours (Rule 8(2)) | [Reported]: read from the Hindi text, English text not read |
| Retention period for some classes of data fiduciary | Three years from last contact for the classes in the Third Schedule (Rule 8(1)) | [Reported]: read from the Hindi text; the Schedule lists specific classes, so check whether you are one |
| `RightsDesk(response_days=...)`: grievance response time | Not more than ninety days (Rule 14(3)) | [Unverified]: the extracted Hindi text is garbled at the number |
| Minimum retention of logs for security incidents | One year (Rule 6) | [Reported]: read from the Hindi text |
| Detailed breach report to the Board | A number of hours after becoming aware (Rule 7(2)(b)) | [Unverified]: the number was not legible; the [India hub](../17_India_AI_Compliance/01_India_AI_Regulatory_Hub.md) lists it as open |

Read the English text of the Rules before setting any of these. A shorter internal target than the legal limit is usually wise.

## The data map

[`privacy_map.json`](code/privacy_map.json) declares each category of data, its sensitivity, its fields, the purposes it serves and its retention period, and the processors that receive it. The code refuses to store or log a field that is not in the map, because an unclassified field is how personal data usually ends up in a log or a prompt.

## Consent that records the notice version

<!-- excerpt: privacy.py -->
```python
    def grant(self, principal: str, purpose: str, notice_version: str, now: float | None = None) -> None:
        if purpose.strip().lower() in GENERIC_PURPOSES or purpose not in self.map.purposes():
            raise ConsentError(f"purpose '{purpose}' is not a specific purpose in the data map")
        if not notice_version:
            raise ConsentError("record the version of the notice shown")
        now = time.time() if now is None else now
        self._consents[(principal, purpose)] = Consent(purpose, notice_version, now)
        self.audit.write(action="consent.grant", principal=principal, purpose=purpose, notice=notice_version)
```

Check `allows(principal, purpose, notice_version)` before every use of the data, including before it is sent to a model or written to an agent's memory. Withdrawal must stop all of these, not only the user interface.

## Retention with advance notice

The runner is meant to run daily. It sends a notice before erasing, and does nothing if the person comes back in the notice window:

<!-- excerpt: privacy.py -->
```python
            if reason is None or principal in self.store.legal_holds:
                self.pending.pop(principal, None)
            elif sent is None:
                self.pending[principal] = now
                self.notify(principal, reason, now + self.notice_hours * 3600)
                self.audit.write(action="retention.notice", principal=principal, reason=reason)
            elif self.store.last_seen.get(principal, 0) > sent:
                self.pending.pop(principal)   # the person came back: the purpose is still served
            elif now - sent >= self.notice_hours * 3600:
                self.desk.erase(principal, now, reason=reason)
                self.pending.pop(principal)
                erased.append(principal)
```

In an AI system, erasure must reach every copy: the database, search indexes and vector stores, caches, agent memory, evaluation sets and logs that hold content. [TC-L07-045](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-045) tests agent memory, and [TC-L03-007](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-007) tests the other AI stores. Data already used to train or fine-tune a model cannot be erased by deleting a row; record that limit in the notice and the impact assessment.

## Children's data

<!-- excerpt: privacy.py -->
```python
    def check(self, principal: str, age: int | None, use: str) -> bool:
        child = age is None or age < self.adult_age   # unknown age is treated as a child
        if not child:
            return True
        ok = use not in BARRED_FOR_CHILDREN and principal in self._parental
        self.audit.write(action="children.check", principal=principal, use=use, allowed=ok)
        return ok
```

The gate checks that a parental verification happened. How the parent is verified, and the classes of data fiduciary and purposes that the Rules exempt, are outside this code.

## Logs without personal data

A plain hash of an email address or phone number is not a pseudonym: anyone can hash likely values and compare. The logger uses a keyed HMAC instead, with the key kept apart from the logs:

<!-- excerpt: privacy.py -->
```python
    def token(self, value: object) -> str:
        return "p_" + hmac.new(self._key, str(value).encode(), hashlib.sha256).hexdigest()[:24]
```

Use internal identifiers, not email addresses, as the `principal` in every call, so that the audit trail itself holds no contact data.

## Run it

```sh
cd source/24_Builder_Track/code
python3 -m unittest -v test_privacy
```

The tests cover consent and withdrawal, the access summary, correction, erasure under a legal hold, grievance due dates, nomination, retention by withdrawal and by inactivity, cancelling erasure when the person returns, the children's gate, and keyed redaction. The [Builder Track tests workflow](https://github.com/nachi065/AI-Security-Wiki/blob/main/.github/workflows/builder-tests.yml) runs them on every change to this section.

## Limits of this reference

- It holds data in memory. In production each duty sits on your database, identity system and job scheduler; keep the same decision points.
- It does not verify a parent, run a consent manager, file a breach report or handle the exemptions in the Act and the Rules.
- Erasure here is one store. Your erasure has to reach every copy, as described above.
- Other laws differ. The GDPR, for example, has special categories and a contract basis. Use the [Privacy Law Crosswalk](../23_Framework_Crosswalks/13_Privacy_Law_Crosswalk.md) before reusing this code elsewhere.

## Related pages

- [India AI Regulatory Hub](../17_India_AI_Compliance/01_India_AI_Regulatory_Hub.md) and [IN-T1 DPDP AI Processing Record, Notice and Consent](../17_India_AI_Compliance/IN-T1_DPDP_AI_Processing_Record_and_Notice.md)
- [Developer Pipeline Checks](04_Developer_Pipeline_Checks.md), which reads the same data map
- [AI Impact Assessment template](../25_Templates/09_AI_Impact_Assessment_Template.md), which records the data, purposes and safeguards this page puts into code
- [Privacy and Regulatory Compliance (AI-CTRL-013)](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) and [Data Protection in AI Pipelines (AI-CTRL-017)](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017)
