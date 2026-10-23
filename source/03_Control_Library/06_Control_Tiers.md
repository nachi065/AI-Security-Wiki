---
title: "Control Tiers"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Control Library"
nav_order: 6
description: "The {{n:controls}} controls split into a Baseline set to put in place first and an Advanced set for higher risk or greater maturity."
document_type: AI Security Wiki Reference
version: 1.0
---

# Control Tiers

Not every organisation needs all {{n:controls}} controls on day one. Each control carries a **Tier** field in the [Control Library](03_AI_Security_Control_Objectives_Library.md). This page is generated from those fields, so it cannot drift from them.

- **Baseline** controls are the ones to have before any AI system, agent or workforce AI use goes into production: know what is running and who owns it, give it identity and least privilege, enforce authority outside the model, keep logs, and be able to respond.
- **Advanced** controls add depth for higher-risk use cases, regulated sectors, model builders and mature programmes: model and pipeline protection, fairness and rights assessment, supply-chain depth, resilience and assurance evidence.

The split is the author's judgement, not a requirement of any framework. A high-risk use case under the [risk tiering](03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011) can need an Advanced control early (for example, impact assessment for a system that decides on people). The ten controls used in the [Builder Track](../24_Builder_Track/01_Secure_Your_First_Agent.md) are all Baseline.

<!-- control-tiers -->
