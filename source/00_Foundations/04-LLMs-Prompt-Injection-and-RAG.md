---
title: "4. LLMs, Prompt Injection and RAG"
description: "LLM attack surface, direct and indirect prompt injection, RAG access control and hallucination as a security risk, against the OWASP LLM Top 10 2025."
author: Nachiket Sathaye
parent: "Foundations"
nav_order: 4
document_type: Practitioner Research Paper
---

# 4. LLMs, Prompt Injection and RAG

## 4.1 The LLM attack surface

An LLM application exposes several surfaces that conventional applications do not: the prompt (user, system and developer text), the context window (retrieved documents, tool results, conversation memory), the output (which may be rendered, executed or acted on), and the model itself (extractable, manipulable, version-dependent). OWASP's 2025 Top 10 for LLM Applications is the most widely used catalogue of the resulting risks [11]:

| ID | Category |
|---|---|
| LLM01 | Prompt Injection |
| LLM02 | Sensitive Information Disclosure |
| LLM03 | Supply Chain |
| LLM04 | Data and Model Poisoning |
| LLM05 | Improper Output Handling |
| LLM06 | Excessive Agency |
| LLM07 | System Prompt Leakage |
| LLM08 | Vector and Embedding Weaknesses |
| LLM09 | Misinformation |
| LLM10 | Unbounded Consumption |

## 4.2 Prompt injection

**Direct injection** is user-supplied text that overrides or subverts intended behaviour. It was characterised early as *goal hijacking* and *prompt leaking* [22]. Automated methods can generate adversarial suffixes that transferred across several aligned models in the original study [24].

**Indirect injection** places instructions in content the application will retrieve or process later: a web page, email, document, calendar invite, code comment or tool result. Greshake et al. demonstrated data theft, fraud, malware distribution, intrusion, content manipulation and availability attacks against synthetic applications and real systems [23]. The user never types the malicious text, so input filters at the user boundary do not see it.

### Why filtering alone is not enough

To the author's knowledge, no published defence reliably separates instructions from data inside a model's context. Classifiers and delimiters reduce attack success but do not provide a security guarantee, and adaptive attackers can often work around fixed defences. [Analysis, consistent with the adversarial ML literature on adaptive attacks; the reader should check recent evaluations of any specific defence.]

### Mitigation architecture

Because the model cannot be relied on to resist injection, design so that a successful injection has limited consequence:

1. **Constrain what the model can do.** Give each task the narrowest tool set and data scope it needs.
2. **Enforce authorisation outside the model.** The tool gateway checks the *user's* entitlements, not the model's request.
3. **Separate privileged and unprivileged contexts.** Do not let the same model session both read untrusted content and hold high-privilege credentials or tools.
4. **Gate irreversible or high-impact actions** behind human approval or deterministic policy.
5. **Treat output as untrusted.** Encode and validate it before it reaches a browser, shell, query engine or downstream API.
6. **Limit exfiltration channels.** Restrict outbound network access, rendered links and image fetches from model-generated content.
7. **Log and monitor** prompts, retrieved sources, tool calls and policy decisions with enough fidelity to reconstruct an incident.

*[Analysis]; items 1 to 5 correspond to controls recommended against OWASP LLM01, LLM05 and LLM06 [11].*

## 4.3 Retrieval-augmented generation (RAG)

RAG adds a retrieval layer between the user and the model. It improves relevance and keeps sensitive knowledge out of model weights, but it creates new trust questions.

| Risk | Mechanism | Mitigation |
|---|---|---|
| **Cross-user data leakage** | The index contains documents the requesting user is not entitled to read | Enforce document-level ACLs at query time using the *end user's* identity; do not rely on the model to withhold content |
| **Document poisoning** | An attacker with write access to any indexed source plants content, including hidden instructions | Control and monitor write paths into the corpus; track source and ingestion time; quarantine untrusted sources |
| **Indirect injection via retrieved text** | Retrieved passage carries instructions (see §4.2) | Treat retrieved text as untrusted data; limit tools available in the same session |
| **Embedding weaknesses** | Embeddings may leak information about source text; multi-tenant indices may mix data | Tenant isolation; access control on the vector store; evaluate inversion risk for sensitive data (OWASP LLM08) [11] |
| **Weak provenance** | Users cannot tell where an answer came from | Return citations to source documents with identifiers, and make those verifiable |

*[Analysis], structured against OWASP LLM08 [11].*

**Design rule.** Authorisation should be applied twice: once to decide which chunks may be retrieved for this user, and again to decide what the downstream session may do with them.

## 4.4 Hallucination as a security risk

Misinformation (LLM09) is treated by OWASP as a security-relevant category [11]. Where fabricated output feeds a decision or an automated step, it becomes an integrity problem. Examples to test for: invented references in a compliance report, invented API or package names in generated code, wrong remediation advice accepted by a junior analyst. In the package case, an attacker could register a plausible fabricated name and wait. [Analysis; this paper cites no measured prevalence figure and deliberately makes no quantitative claim here.]

Mitigations: ground answers in retrievable sources, validate machine-generated identifiers (packages, URLs, CVE IDs) against authoritative registries before use, and require human review where an error would be costly.

## 4.5 Content and policy controls

Input/output filters, moderation models and refusal training reduce misuse, but they are *probabilistic* controls. Use them as one layer, measure their performance against your own threat cases, and never rely on them as the sole barrier protecting a sensitive action. [Analysis]
