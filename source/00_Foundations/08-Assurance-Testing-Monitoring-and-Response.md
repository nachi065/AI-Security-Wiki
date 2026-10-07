---
title: "8. Assurance: Testing, Monitoring and Response"
description: "AI assurance: threat modelling, adversarial testing and red teaming, monitoring and detection, AI incident response and control-effectiveness metrics."
author: Nachiket Sathaye
parent: "Foundations"
nav_order: 8
document_type: Practitioner Research Paper
---

# 8. Assurance: Testing, Monitoring and Response

A statement that an AI system is "secure" has no meaning unless it names the threat model, assets, assumptions, evaluation methods, residual risk and operating environment. This page describes how to produce that evidence.

## 8.1 Threat modelling for AI systems

Conventional methods (STRIDE-style analysis, attack trees, data-flow diagrams) still apply. Extend them with AI-specific assets and paths:

1. **Identify assets** beyond code and data: models, prompts, tool definitions, embeddings, memory, agent identities.
2. **Draw trust boundaries** (see [Page 2](02-AI-System-Boundary-and-Assets.md)).
3. **Enumerate attack paths** from each untrusted input to each privileged action. For every path, record entry point, attacker capability, weakness exploited, privilege gained and detection opportunity.
4. **Write abuse cases** in business terms: "a customer-supplied PDF causes the assistant to email another customer's records".
5. **Score risk** using your existing method, adding an explicit *authority* factor: what can the system do without a human?
6. **Map to shared vocabularies** (OWASP LLM/Agentic IDs [11][12], MITRE ATLAS techniques [14]) so findings are comparable and auditable.

Worksheets are in the [Appendices](Appendices.md).

## 8.2 Testing and red teaming

| Activity | Purpose | Notes |
|---|---|---|
| **Security testing of the application** | Find conventional flaws in the new data flows | API testing, authorisation tests, output-handling tests, dependency scanning |
| **Adversarial evaluation** | Measure resistance to evasion, injection, extraction and leakage | Define attack success explicitly; use realistic, adaptive attackers |
| **Red teaming** | Discover unknown failure modes through creative, goal-driven attack | Scope around business harm, not only policy violations |
| **Continuous evaluation** | Detect regressions when models, prompts, corpora or tools change | Automate; tie results to component versions |

**What to measure.** Do not measure only refusal behaviour. The question is whether the system leaks information or performs an unauthorised action. [Analysis] Test suites should cover: direct injection; indirect injection through each retrieval and tool channel; instruction conflicts; malicious retrieved content; exfiltration attempts; tool manipulation; and cross-tenant access.

**Limits of testing.** Because behaviour is probabilistic, a clean test run is evidence, not proof. Report results as rates over defined test sets with the model version, configuration and date, and treat any single pass as provisional. NIST notes that adversarial ML mitigations are an evolving area [1]. **[Documented]**

## 8.3 Monitoring and detection

**Telemetry to collect** (subject to privacy and legal constraints): authenticated identity; model and prompt version; retrieval sources and their provenance; tool calls with parameters; policy decisions (allow, deny, escalate); output metadata; latency, token and cost usage.

**Detection ideas** [Analysis]:

- Tool calls outside the normal pattern for that agent or task
- Retrieval of documents unrelated to the query, or from unusual sources
- Output containing credential-like strings, internal identifiers or unexpected URLs
- High-volume, systematic querying consistent with model extraction
- Sudden shifts in refusal rate, output length or tool-use distribution after a change upstream
- Repeated approval denials or unusual approval patterns

Feed AI telemetry into existing SIEM/SOAR workflows rather than building a parallel operations stack. Add AI-specific detection content and runbooks.

## 8.4 Incident response and recovery

AI incident categories to plan for: sensitive-data disclosure through a model; unauthorised agent action; prompt-injection compromise; poisoned data or corpus; compromised model or package; credential exposure; provider outage or silent behaviour change; abusive use driving cost or reputational harm.

| Phase | AI-specific considerations |
|---|---|
| **Contain** | Disable the affected tool or agent; revoke its credentials; switch to a known-good model version; isolate the retrieval source; apply rate limits or block patterns |
| **Investigate** | Preserve prompts, retrieved context, tool-call logs, model version and configuration; establish whether the model was the cause, the channel or merely the victim |
| **Eradicate** | Remove poisoned documents; rotate secrets; patch the application path that made the action possible; add detection |
| **Recover** | Roll back to a verified model and corpus; re-run evaluations before re-enabling autonomy; reconcile any actions already taken |
| **Learn** | Update threat models, tests and approval thresholds; record the incident against ATLAS techniques where applicable [14] |

**Exercise it.** Tabletop scenarios: a model is suspected of leaking confidential data; an agent performs an unauthorised action; a provider suffers an outage; a poisoned document influences retrieval. Test technical containment, business escalation, communications and recovery.

## 8.5 Metrics

Metrics should reflect control effectiveness rather than activity volume. Suggested starting set. *Targets are deliberately omitted; set them from your own baseline and risk appetite.* [Analysis]

| Level | Metric | Definition |
|---|---|---|
| Technical | Coverage of AI inventory | AI systems with a named owner and risk rating ÷ AI systems discovered |
| Technical | Injection test success rate | Successful attacks ÷ attacks attempted, per test suite and model version |
| Technical | Privileged-action gating | High-impact tool calls passing through policy enforcement ÷ all high-impact tool calls |
| Technical | Version traceability | Production AI components with recorded provenance ÷ all production AI components |
| Operational | Time to disable | Time from decision to the AI system being stopped or isolated |
| Operational | Time to detect/respond | For AI-related incidents, median time to detect and to contain |
| Operational | Re-evaluation latency | Time from an upstream change to completed security re-evaluation |
| Risk | Residual risk by system | Rating after controls, with accepted exceptions and expiry dates |
| Board | Material AI systems and top risks | Count and heat-map of high-risk systems, open exceptions, and incident trend |
