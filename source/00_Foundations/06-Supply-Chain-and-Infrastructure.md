---
title: "6. Supply Chain and Infrastructure"
description: "AI supply chain and infrastructure security: models, datasets, packages, tool servers, provenance, AI bill of materials, GPUs, cloud and secrets."
author: Nachiket Sathaye
parent: "Foundations"
nav_order: 6
document_type: Practitioner Research Paper
---

# 6. Supply Chain and Infrastructure

## 6.1 The AI supply chain is wider than the software supply chain

Organisations consume foundation models and hosted APIs, fine-tuned adapters, open-source frameworks, datasets, embedding models, vector stores, evaluation tools, agent frameworks, plugins and tool servers, and GPU and cloud infrastructure. Foundation models in particular concentrate capability into reusable artifacts; a single model may sit beneath thousands of downstream applications, creating concentration risk [26]. The security boundary is distributed across suppliers and cannot be reduced to the organisation's own code. OWASP lists supply chain as LLM03 [11] and, for agents, ASI04 [12]; ENISA's 2020 threat-landscape report already emphasised the supply chain as a significant dimension of AI cybersecurity [9]. **[Documented]**

| Component | Typical risks | Controls |
|---|---|---|
| **Third-party models and adapters** | Tampered weights; backdoors; unclear training data; unannounced version change | Source from trusted registries; verify hashes/signatures where offered; pin versions; re-evaluate on every change |
| **Model file formats** | Some serialisation formats can execute code on load | Prefer formats that do not execute code on load; scan artifacts; load in isolated environments *(verify current guidance for each format in use)* |
| **Datasets** | Poisoning; unlicensed or sensitive content; link-rot hijack | Record provenance and hashes; integrity-check downloads; review licences [25] |
| **Open-source packages and frameworks** | Malicious or compromised releases; typosquatting; vulnerable dependencies | Pin and lock dependencies; internal mirror; SCA scanning; review new dependencies |
| **Plugins / tool servers** | Over-privileged or malicious tools; description-based injection | Allow-list; review permissions; run isolated; monitor calls |
| **Hosted model providers** | Data retention; behaviour change; outage; provider incident | Contractual terms; data-handling review; fallback plan; monitoring for behavioural drift |

*[Analysis], with sources as cited.*

**Reported incidents.** The OWASP Round-up for Q1 2026 describes malicious package updates in AI-related tooling and the rapid weaponisation of leaked artifacts among its incidents [13]. **[Reported]** *Read the primary report for incident specifics; this paper does not restate them.*

## 6.2 Provenance, signing and an AI bill of materials

Practical goals: know exactly which model, dataset, prompt, adapter and package versions are running in each environment; be able to prove they match what was approved; and be able to answer "are we affected?" within hours when an upstream component is disclosed as compromised.

Recommended minimum record per AI system: model name, provider, version/hash; dataset sources and snapshots; fine-tuning lineage; framework and package versions; prompt and policy versions; tool definitions; evaluation results tied to those versions. Machine-readable inventories exist in SBOM tooling and may be extended to ML artifacts; *check the current capabilities of your chosen format before committing to it.* [Analysis]

**Change control.** Treat a model, prompt, retrieval-corpus or policy change as a release. A control that passed at deployment may not hold after a provider-side model update. Re-run security evaluations whenever any upstream component changes.

## 6.3 Infrastructure and cloud

Most infrastructure risk in AI systems is conventional risk at a higher stakes level: GPUs and accelerators are expensive and attractive for abuse; model weights and datasets are large, valuable files; clusters often have broad internal permissions to move data; and notebooks and experiment tooling are frequently less hardened than production. [Analysis]

| Area | Concerns | Controls |
|---|---|---|
| **GPU / accelerator hosts** | Resource hijacking; driver and firmware vulnerabilities; shared-tenant isolation | Patch management; tenant isolation; usage quotas and anomaly alerts |
| **Containers and orchestration** | Over-privileged pods; exposed dashboards and APIs; image provenance | Hardened base images; least-privilege runtime; admission control; network policies |
| **Storage** | Open buckets; unencrypted weights and datasets; over-broad access | Encryption; strict IAM; access logging; separate environments |
| **Cloud AI platforms** | Privilege abuse via default service roles | Review default roles on managed AI services; the Q1 2026 Round-up reports cloud privilege-abuse issues affecting managed AI platforms [13] **[Reported]** |
| **Secrets** | Keys in notebooks, repos, prompts, CI logs | Central secrets management; scanning; short-lived credentials |
