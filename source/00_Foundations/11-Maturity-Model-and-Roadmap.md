---
title: "11. Maturity Model and Roadmap"
description: "AI security maturity levels with typical evidence, and a roadmap from the first 30 days to 24 months."
author: Nachiket Sathaye
parent: "Foundations"
nav_order: 11
document_type: Practitioner Research Paper
---

# 11. Maturity Model and Roadmap

*This model is the author's own construct and has not been validated empirically. Use it as a conversation tool, not a benchmark.* [Analysis]

## 11.1 Five-level maturity model

The levels are those of the wiki's [AI Security Maturity Model](../01_Strategy_and_Market/01_AI_Security_Market_and_Technology_Landscape_Expanded.md#8-ai-security-maturity-model), so the whole wiki uses one scale. This page adds the evidence that shows a level has been reached.

| Level | Name | Characteristics | Typical evidence |
|---|---|---|---|
| 1 | **Ad Hoc** | AI use is ad hoc and largely unknown to security; no inventory, policy or security review; reliance on vendor claims | None, or informal |
| 2 | **Discovered** | The main AI tools and systems are visible and inventoried; usage patterns are reported | Inventory, usage reports |
| 3 | **Governed** | Acceptable-use policy, intake, data-handling rules, named owners and vendor review are in place; a standard process exists for threat modelling and release of AI systems | Policy, approval records, threat models, vendor assessments |
| 4 | **Protected** | Runtime, IDE, RAG and agent controls are implemented to architecture patterns; agent permissions are documented; telemetry feeds detection | Architecture standards, permission maps, control configuration, logs |
| 5 | **Optimized** | Regular adversarial testing and continuous evaluation; metrics reported; exercises held; findings, incidents and supplier changes alter controls quickly | Test reports, dashboards, exercise records, change history linked to incidents and research |

## 11.2 Roadmap

### First 30 days: see and stop the obvious

- Discover AI in use (sanctioned and unsanctioned), including AI features inside SaaS.
- Publish an interim acceptable-use rule: what data may be sent to which tools.
- Identify AI systems with write access to anything (agents, automations) and list their credentials.
- Remove secrets from prompts, shared notebooks and configuration.
- Name an accountable owner for AI security.

### By day 90: foundation

- Establish the AI inventory and a risk-tiering scheme.
- Define a minimum security baseline: identity, logging, data classification, approved providers.
- Introduce threat modelling for new AI use cases.
- Put a gateway or policy layer in front of model and tool access for the highest-risk systems.
- Draft AI-specific incident playbooks and run one tabletop.

### By month 6: programme

- Build repeatable evaluation and red-teaming for high-tier systems; connect results to release gates.
- Integrate AI telemetry into the SOC; add detection content.
- Add supply-chain controls: approved model/package sources, pinning, re-evaluation on change.
- Align governance to a chosen framework (for example ISO/IEC 42001 or NIST AI RMF) and begin collecting audit evidence [3][4].
- Map regulatory obligations (including the EU AI Act where relevant) to controls [7][8].

### 12 to 24 months: measured and optimized

- Report the metrics on [Page 8](08-Assurance-Testing-Monitoring-and-Response.md) to executive and board level.
- Continuously evaluate high-tier systems; automate re-testing on upstream change.
- Review autonomy limits against incident and test data; raise or lower them deliberately.
- Independent assurance (internal audit or external) of the AI security programme.
