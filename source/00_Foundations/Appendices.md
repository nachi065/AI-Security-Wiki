---
title: "Appendices"
description: "AI security assessment questionnaire, threat-modelling worksheets for assets, attack paths and agents, and control testing procedures."
author: Nachiket Sathaye
parent: "Foundations"
nav_order: 14
document_type: Practitioner Research Paper
---

# Appendices

## Appendix A: AI Security Assessment Questionnaire

### A.1 Governance
- Does the organisation maintain an inventory of material AI systems?
- Is each system assigned an owner and a risk classification?
- Are prohibited uses documented?
- Are suppliers and model providers assessed?
- Are regulatory obligations mapped to controls?
- Are exceptions documented and time-bound?

### A.2 Technical security
- Is model provenance known?
- Are training and inference datasets classified?
- Are secrets excluded from prompts and logs?
- Are model endpoints protected?
- Are tools least-privileged?
- Are agent identities separate from human identities?
- Are retrieval stores access-controlled with end-user entitlements?
- Are model and prompt changes versioned?

### A.3 Assurance
- Are adversarial tests performed before deployment?
- Are prompt injection, data poisoning, model extraction, sensitive-data disclosure and tool misuse tested?
- Are high-impact actions gated?
- Is runtime monitoring enabled?
- Can the system be rapidly disabled or rolled back?
- Are incident-response procedures exercised?

---

## Appendix B: Threat-Modelling Worksheets

### B.1 Asset worksheet
For each system, record: asset name; owner; business purpose; data classes; model provider; model version; application; tools; identities; external dependencies; geographic scope; regulatory classification; maximum credible impact.

### B.2 Attack-path worksheet
For each threat, record: entry point; attacker capability; exploited weakness; affected component; privilege gained; downstream action; security property affected; business impact; existing controls; residual risk; detection opportunities.

### B.3 Agent worksheet
For each agent, record: available tools; permissions; data sources; action types; approval requirements; memory stores; external communications; maximum transaction value; maximum autonomous duration; emergency shutdown mechanism.

---

## Appendix C: Control Testing Procedures

### C.1 Prompt and context testing
Create benign and adversarial test suites covering direct injection, indirect injection, instruction conflict, malicious retrieved content, data-exfiltration attempts and tool manipulation. Measure not only refusal behaviour but whether the system leaks information or performs unauthorised actions. Record model version, configuration and date for every run.

### C.2 Supply-chain testing
Verify artifact provenance, checksums or signatures where supported, dependency versions, model source, dataset origin, licence obligations and update channels. Test whether an unapproved model or package can enter production and whether changes trigger re-evaluation.

### C.3 Incident testing
Conduct tabletop exercises in which a model is suspected of leaking confidential data, an agent performs an unauthorised action, a provider suffers an outage, or a compromised document influences retrieval. Test technical containment, business escalation, communications and recovery.

---

## Appendix D: Glossary

The terms used in this paper are defined in the wiki's [AI Security Glossary and Taxonomy](../09_Reference/18_AI_Security_Glossary_and_Taxonomy.md).
