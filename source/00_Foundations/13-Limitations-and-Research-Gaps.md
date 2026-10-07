---
title: "13. Limitations and Research Gaps"
description: "Limitations of the AI Security vs. Security of AI paper and open research problems in agent security, evaluation, provenance and detection."
author: Nachiket Sathaye
parent: "Foundations"
nav_order: 13
document_type: Practitioner Research Paper
---

# 13. Limitations and Research Gaps

## 13.1 Limitations of this paper

1. **It is a synthesis, not an empirical study.** There are no new experiments, datasets or measurements. The two-axis model, maturity model and metric suggestions are the author's constructs and are not validated.
2. **Sources are partly secondary.** Several current-events claims (EU AI Omnibus dates, OWASP agentic and Round-up content, MITRE ATLAS version) rest on web summaries or law-firm commentary, and are labelled **[Reported]**. They should be checked against primary sources before citation.
3. **The field moves quickly.** Attack feasibility, defences, standards and regulation change on a scale of months. The content reflects the state of knowledge around October 2026 and some of it will date.
4. **Terminology is stipulated.** The three-way split in [Page 1](01-Terminology-and-Two-Axis-Model.md) is a convention proposed here. Other authors and standards bodies carve the space differently.
5. **Scope.** It does not cover model-safety alignment in depth, content-moderation policy, or sector-specific regulation beyond the EU Act. UAE sovereignty and data residency are covered separately in the wiki's [sovereignty standard](../04_Domain_Standards/10_Sovereign_AI_UAE_Compliance_and_Data_Residency.md). It does not provide offensive techniques.
6. **Not legal advice.**

## 13.2 Open problems

These are questions where the author sees a gap between practice and evidence. [Analysis]

| Area | Open question |
|---|---|
| **Agent security** | Is there a design pattern that lets an agent process untrusted content and use sensitive tools in one session with a defensible guarantee, rather than relying on separation of sessions? |
| **Evaluation science** | How should "attack success rate" be defined, sampled and reported so numbers are comparable across systems and over time? How do we handle adaptive attackers in routine testing? |
| **Provenance** | What is a practical, widely adopted way to attest where a model's behaviour came from (data, training, fine-tuning) beyond file hashes? |
| **Detection** | What telemetry is both privacy-acceptable and sufficient to detect injection and misuse in production? |
| **Metrics for boards** | Which indicators predict AI-related loss, as opposed to merely recording activity? |
| **Cross-framework mapping** | Can a single machine-readable control mapping be maintained across NIST, ISO, OWASP, ATLAS and the EU Act? |
| **Autonomy governance** | What evidence should justify raising an agent's autonomy level, and how should it be revoked? |

## 13.3 Updating this paper

Treat it as a living document. When a source in [References](References.md) changes (for example a new NIST edition, an OWASP revision or an ATLAS release), update the relevant page and record the revision date on [Home](index.md).
