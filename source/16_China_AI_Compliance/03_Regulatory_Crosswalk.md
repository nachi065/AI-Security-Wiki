---
title: "China Regulatory Crosswalk"
author: Nachiket Sathaye
parent: "China AI Compliance"
nav_order: 3
description: "Chinese instruments mapped one per row to AI security controls, with verification status. Also available as a CSV file."
document_type: AI Security Wiki Reference
version: 1.0
last_reviewed: 2026-10-22
---

# China Regulatory Crosswalk

> **Verification required.** Claims on this page about Chinese law were compiled on 7 October 2026 from secondary web sources and from memory of the law. On 22 October 2026, rows CN1, CN2, CN3 and CN4 were checked against the primary text on the issuing bodies' own sites (the Cyberspace Administration of China, the State Council policy library and the national standards system) and are tagged [Verified]. Every other claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

One row per instrument in the [China AI Regulatory Hub](01_China_AI_Regulatory_Hub.md), with the wiki controls that relate to it and its verification status. The last column is empty until a row has been confirmed against the primary text; record the primary URL and the date you retrieved it there.

The same data is available as a CSV file for GRC tooling: [crosswalk.csv](data/crosswalk.csv).

**Legal force** sorts each row under one of seven labels, so that law is not mistaken for guidance or for a voluntary framework. The label is this wiki's reading of the sources and carries the same verification caveat as the rest of the row.

| Label | Meaning |
|---|---|
| Binding law | Enacted law or regulation that applies generally in the jurisdiction, including provisions that start on a later date. |
| Binding in scope | Binding only on a sector, a free zone, a state or province, or public bodies. |
| Guidance | Published by a government or regulator, and not binding in itself. |
| Voluntary | A standard, code or framework that an organization chooses to adopt. |
| Proposed | A bill, draft or consultation, or a proposal that lapsed. It is not law. |
| Context | A policy, authority, programme or summary row that sets no rule. |
| Unclear | The sources used do not settle whether it binds. |

| ID | Instrument | Legal force | Type / status | Wiki controls | Verification tag | To verify | Primary URL and retrieval date |
|---|---|---|---|---|---|---|---|
| CN1 | Interim Measures for the Management of Generative AI Services (2023) | Binding law | Binding administrative measures | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013); [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039); [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | Verified | Nothing outstanding | [State Council policy library: 生成式人工智能服务管理暂行办法 (CAC and six other bodies, Order No. 15)](https://www.gov.cn/zhengce/zhengceku/202307/content_6891752.htm), retrieved 22 Oct 2026 (effective 15 Aug 2023; Art. 17 requires a security assessment and algorithm filing only for services with public-opinion or social-mobilisation attributes; no numeric threshold) |
| CN2 | Provisions on Algorithm Recommendation (2022) | Binding law | Binding | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011); [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039); [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | Verified | Nothing outstanding | [CAC: 互联网信息服务算法推荐管理规定 (Order No. 9)](https://www.cac.gov.cn/2022-01/04/c_1642894606364259.htm), retrieved 22 Oct 2026 (effective 1 Mar 2022; filing within 10 working days of starting the service (Art. 24)) |
| CN3 | Provisions on Deep Synthesis (2023) | Binding law | Binding | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | Verified | Nothing outstanding | [CAC: 互联网信息服务深度合成管理规定 (Order No. 12)](https://www.cac.gov.cn/2022-12/11/c_1672221949354811.htm), retrieved 22 Oct 2026 (effective 10 Jan 2023; scope in Art. 2, definition in Art. 23) |
| CN4 | Measures for labelling AI-generated content; mandatory standard GB 45438-2025 | Binding law | Binding; effective 1 Sep 2025 | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | Verified | Nothing outstanding | [CAC: 人工智能生成合成内容标识办法 (CAC, MIIT, MPS and NRTA)](https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm); [SAMR national standards system: GB 45438-2025](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=F32EA2A561F1886CD8D606513512D547), retrieved 22 Oct 2026 (the measures and the standard both take effect 1 Sep 2025; Art. 11 of the measures refers to mandatory national standards without naming GB 45438) |
| CN5 | AI ethics review measures | Binding law | Effective March 2026 | [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012); [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037); [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | Reported | Official title; scope |  |
| CN6 | Rules for anthropomorphic (emotional companion) AI services | Binding law | Effective July 2026 | [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039); [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | Reported | Official title; scope |  |
| CN7 | Cybersecurity Law (2025 amendment with AI provisions); Data Security Law; PIPL | Binding law | Binding | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005); [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013); [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007); [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Reported | Amendment effective date; transfer mechanisms |  |
| CN8 | Comprehensive AI law | Proposed | In 2026 legislative work plan; not enacted | None | Reported | Draft text |  |
| CN9 | Regulators: CAC, MIIT, SAMR, MPS | Context | Authorities | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013) | Reported | Contact points |  |
