---
title: "3. Threat Taxonomy"
description: "AI threat taxonomy by lifecycle stage: poisoning, evasion, prompt injection, extraction and supply chain, mapped to NIST AI 100-2, OWASP and MITRE ATLAS."
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Foundations"
nav_order: 3
document_type: Practitioner Research Paper
---

# 3. Threat Taxonomy

This page organises threats to AI systems by lifecycle stage and cross-references them to NIST's attack classes [1], OWASP's LLM categories [11], and MITRE ATLAS techniques [14]. It is a navigation aid, not a replacement for those sources.

## 3.1 How NIST classifies attacks

NIST AI 100-2e2025, published in March 2025, is a taxonomy and terminology document for adversarial machine learning. The 2025 edition has two taxonomies [1]:

- **Predictive AI** (section 2), with sections on evasion attacks (2.2), poisoning attacks (2.3) and privacy attacks (2.4).
- **Generative AI** (section 3), with sections on supply chain attacks (3.2), direct prompting attacks (3.3), indirect prompt injection (3.4), security of agents (3.5) and benchmarks for AML vulnerabilities (3.6).

In both taxonomies, attacks are classified by the attacker's objective, and each attack class has a stable identifier of the form `NISTAML.0XY`. The objectives are availability violations (NISTAML.01), integrity violations (NISTAML.02), privacy compromises (NISTAML.03), misuse violations (NISTAML.04, generative AI) and supply chain attacks (NISTAML.05). For example, NISTAML.018 is prompt injection and NISTAML.015 is indirect prompt injection. NIST states that it intends to update the report as the field evolves. **[Documented]**

> **Correction (15 October 2026).** An earlier version of this section said that the 2025 edition organises generative AI attacks into "evasion, poisoning, privacy and misuse" classes. That was inaccurate: evasion, poisoning and privacy are the section headings of the predictive AI taxonomy, and both taxonomies classify attacks by attacker objective, as set out above. The section headings and identifiers were checked against the published PDF on 15 October 2026. The [NIST AI 100-2 Crosswalk](../23_Framework_Crosswalks/14_NIST_AI_100_2_Crosswalk.md) maps each identifier to the wiki's controls.

## 3.2 Threats by lifecycle stage

### Training-time

| Threat | Description | Key sources |
|---|---|---|
| **Data poisoning** | Attacker alters training data to degrade a model or install targeted behaviour | Biggio et al. showed poisoning against SVMs in 2012 [19]; Carlini et al. showed web-scale dataset poisoning is practical [25] |
| **Backdoors / trojans** | A hidden trigger causes attacker-chosen behaviour while normal accuracy is preserved | NIST AI 100-2e2025 [1]; OWASP LLM04 [11] |
| **Compromised pre-trained models** | A downloaded model or adapter is already tampered with | See [Page 6](06-Supply-Chain-and-Infrastructure.md) |

**Documented example.** Carlini et al. describe *split-view poisoning* (buying expired domains that host content indexed in datasets such as LAION-400M, so later downloaders receive attacker-controlled content) and *frontrunning poisoning* (editing content just before a predictable snapshot, as with Wikipedia dumps). They report that they could have controlled roughly 0.01% of some datasets for about US$60, and proposed integrity checks and snapshot-timing defences [25]. **[Documented]** *Verify the figures against the paper before quoting them.*

### Inference-time

| Threat | Description | Key sources |
|---|---|---|
| **Evasion / adversarial examples** | Small, crafted perturbations cause misclassification | Goodfellow et al. [16]; Papernot et al. [17]; physical-world examples by Kurakin et al. [18] |
| **Prompt injection (direct)** | User-supplied text overrides intended behaviour | Perez & Ribeiro [22]; OWASP LLM01 [11] |
| **Prompt injection (indirect)** | Instructions hidden in retrieved or third-party content | Greshake et al. [23] |
| **Adversarial suffixes / jailbreaks** | Automatically generated strings that transfer across aligned models | Zou et al. [24] |
| **Resource abuse** | Cost or capacity exhaustion through crafted use | OWASP LLM10 [11] |

### Model-level

| Threat | Description | Key sources |
|---|---|---|
| **Membership inference** | Determining whether a record was in the training set | Shokri et al. [20] |
| **Model extraction** | Reconstructing a model's function through repeated queries to its API | Tramèr et al. [21] |
| **Training-data extraction / leakage** | Eliciting memorised content | NIST AI 100-2e2025 privacy attacks [1]; OWASP LLM02 [11] |
| **System-prompt leakage** | Disclosure of hidden instructions | OWASP LLM07 [11] |

### Application and ecosystem

| Threat | Description | Key sources |
|---|---|---|
| **Insecure output handling** | Model output reaches an interpreter (browser, shell, SQL) unescaped | OWASP LLM05 [11] |
| **Excessive agency** | Over-broad tools, permissions or autonomy | OWASP LLM06 [11]; OWASP Agentic Top 10 [12] |
| **Vector/embedding weaknesses** | Cross-tenant leakage, poisoned retrieval | OWASP LLM08 [11] |
| **Supply-chain compromise** | Malicious packages, models, plugins, datasets | OWASP LLM03 [11]; OWASP Round-up Q1 2026 [13] |
| **Misinformation / over-reliance** | False output acted on without verification | OWASP LLM09 [11] |

## 3.3 What is "new" and what is not

Many of the above are old problems in new forms: supply-chain compromise, injection through an untrusted channel, over-privileged service accounts, side channels. What is genuinely different: [Analysis]

1. **Probabilistic behaviour.** A control can pass a test and fail on a slightly different input. Testing gives evidence, not proof.
2. **Learned, opaque artifacts.** The behaviour of a model cannot be fully audited by reading its source.
3. **Natural-language attack surface.** The input language is also the instruction language.
4. **Behaviour that moves with upstream change.** A provider-side model update can change security-relevant behaviour with no change to your code.

## 3.4 Who attacks AI systems

| Actor | Typical objective | Relevant capability |
|---|---|---|
| Criminal groups | Fraud, extortion, resale of access, abuse of compute | Commodity tooling; abuse of exposed AI endpoints and keys |
| Insiders | Data theft, sabotage, unauthorised model access | Legitimate access to weights, data or prompts |
| Malicious users | Jailbreaking, data extraction, free compute | Direct interaction with the model |
| Supply-chain actors | Persistence at scale via popular packages or models | Control over upstream artifacts |
| Strategic or state-aligned actors | Espionage, model theft, disruption | Resources for sustained, targeted operations |

*[Analysis]. This paper does not attribute specific AI-security incidents to specific actors.*

## 3.5 Mapping to ATLAS

MITRE ATLAS is a knowledge base of adversary tactics and techniques against AI-enabled systems, modelled on the structure of ATT&CK, and maintained with regular content releases [14]. Use it to describe an incident or test case in shared vocabulary. At the time of writing the public data repository shows a content version of 2026.05 and states that ATLAS releases monthly updates [14]. Check atlas.mitre.org for current technique counts and identifiers rather than relying on a figure in this paper.
