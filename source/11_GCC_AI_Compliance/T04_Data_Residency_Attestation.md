---
title: "T04 Data Residency and Sovereignty Attestation"
author: Nachiket Sathaye
parent: "GCC AI Compliance"
nav_order: 12
description: "Fill-in attestation of where each AI data component is stored and processed, the transfers involved and who signs for them."
document_type: AI Security Wiki Reference
version: 1.0
---

# T04 Data Residency and Sovereignty Attestation

> **Verification required.** This is a working template, not a regulator-approved form. Where it names a regional instrument, the claim comes from secondary sources and is a pointer to check, not a confirmed legal requirement. This is not legal advice.

<!-- -->

> **How to use:** This is a blank form. Copy it and fill in the empty cells and blanks for your system. To copy it, follow the "Suggest an edit to this page" link in the footer to reach its Markdown source.

Wiki control: [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007). The signer attests to facts of configuration, not to legal compliance. Legal review of transfers is separate.

| Field | Entry |
|---|---|
| System / use-case ID | |
| Attestation date | |
| Valid until (re-attest on change or at 12 months) | |
| Signer (name, role) | |

## 1. Data inventory by location

| Data component | Description | Country | Provider and region | Legal entity | Encrypted (Y/N) | Key holder |
|---|---|---|---|---|---|---|
| Training data | | | | | | |
| Fine-tuning data | | | | | | |
| Prompts and inputs | | | | | | |
| Model inference compute | | | | | | |
| Outputs | | | | | | |
| Embeddings / vector store | | | | | | |
| Application logs | | | | | | |
| Telemetry / monitoring | | | | | | |
| Backups and snapshots | | | | | | |
| Support and admin access (location of staff) | | | | | | |
| Sub-processors | | | | | | |

## 2. Transfers

| Flow | From | To | Personal data? | Mechanism / basis (per legal advice) | Approved by |
|---|---|---|---|---|---|

## 3. Attestations (tick if true; explain exceptions)

- [ ] All components above are at the stated locations
- [ ] No component is replicated outside the stated locations
- [ ] Vendor staff outside the approved countries cannot access data, or access is logged and approved
- [ ] Customer data is not used for vendor model training
- [ ] Deletion removes data from backups within ______ days
- [ ] Configuration evidence attached (exports, screenshots, region settings)

Exceptions and compensating controls:

## 4. Regional checks (confirm from primary text; do not rely on this list)

| Jurisdiction | Question for counsel |
|---|---|
| UAE mainland | Transfer conditions under PDPL; sector localisation rules |
| DIFC / ADGM | Transfer rules under free-zone regulations |
| Saudi Arabia | PDPL transfer conditions; NCA, NDMO, SAMA localisation overlays [Reported, verify] |
| Qatar | PDPPL transfer rules; QCB expectations |
| Bahrain, Oman | PDPL transfer provisions; Oman amendments pending [Reported] |

## 5. Sign-off

Signer: ______ Date: ______  Reviewed by (privacy/security): ______ Date: ______
