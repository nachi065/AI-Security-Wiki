---
title: "Brazil Regulatory Crosswalk"
author: Nachiket Sathaye
parent: "Brazil AI Compliance"
nav_order: 3
description: "Brazilian instruments mapped one per row to AI security controls, with verification status. Also available as a CSV file."
document_type: AI Security Wiki Reference
version: 1.0
last_reviewed: 2026-10-22
---

# Brazil Regulatory Crosswalk

> **Verification required.** Claims on this page about Brazilian law were compiled on 7 October 2026 from secondary web sources and from memory of the law. On 22 October 2026, rows BR1 were checked against the primary text on the issuing bodies' own sites (the Senate and Chamber of Deputies bill records) and are tagged [Verified]. Every other claim is tagged [Reported], [Recalled], [Conflict] or [Unverified] as explained on the [section home page](index.md). Check the primary text before relying on any of them. This is not legal advice.

One row per instrument in the [Brazil AI Regulatory Hub](01_Brazil_AI_Regulatory_Hub.md), with the wiki controls that relate to it and its verification status. The last column is empty until a row has been confirmed against the primary text; record the primary URL and the date you retrieved it there.

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
| BR1 | PL 2338/2023 (AI bill) | Proposed | Pending; Senate approved 10 Dec 2024; awaiting committee opinion in the Chamber as at 2 Sep 2026 | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011); [AI-CTRL-037](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-037); [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | Verified | Chamber text, once the rapporteur files an opinion | [Senado Federal: PL 2338/2023 record](https://www25.senado.leg.br/web/atividade/materias/-/materia/157233/pdf); [Camara dos Deputados: PL 2338/2023 tramitacao](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2487262), retrieved 22 Oct 2026 (Senate approved the substitute on 10 Dec 2024; the Chamber page shows "Aguardando Parecer do(a) Relator(a) na Comissao Especial", no amendments and no entry after 2 Sep 2026) |
| BR2 | LGPD (Law 13.709/2018) | Binding law | Binding. Lei 15.352/2026 (25 Feb 2026) made the ANPD a special-regime agency (Agencia Nacional de Protecao de Dados) linked to the Ministry of Justice; Art. 20 not amended | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013); [AI-CTRL-007](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-007); [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017); [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035) | Recalled | LGPD text and Art. 20 wording (the planalto LGPD page could not be read automatically); ANPD rules on Art. 20 | [Planalto: Lei 15.352 de 25 de fevereiro de 2026](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/L15352.htm), retrieved 22 Oct 2026 (the amending law was read; the LGPD itself was not, so the tag stays Recalled) |
| BR3 | ANPD and sector regulators advancing AI regulation | Context | Regulator activity. ANPD: AI and data protection regulatory sandbox (testing methodology 19 Aug 2026); AI a priority theme for 2026-27 (Resolucao CD/ANPD 30/2025); enforces duties of language-model and chatbot providers towards minors (Decreto 12.880/2026, Art. 11) | [AI-CTRL-013](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-013); [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012) | Verified | Sector regulators (no primary BCB or CMN AI rule found); Lei 15.487/2026 (AI and sexual violence against children) not read | [ANPD: Mapa de Temas Prioritarios 2026-2027 (24 Dec 2025)](https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-publica-mapa-de-temas-prioritarios-para-o-bienio-2026-2027-e-atualiza-agenda-regulatoria-2025-2026); [ANPD: sandbox testing methodology (19 Aug 2026)](https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-publica-metodologia-de-testagem-do-sandbox-regulatorio-em-inteligencia-artificial-e-protecao-de-dados); [Planalto: Decreto 12.880 de 18 de marco de 2026](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/decreto/d12880.htm), retrieved 22 Oct 2026 |
| BR4 | Consumer Defence Code and sector rules (finance, health) | Binding law | Binding. Decreto 13.135/2026 (customer service, published 13 Oct 2026, in force 2 Nov 2026 under Art. 25) allows automated and AI systems only if the consumer can choose real-time service by a person (Art. 3 para 3) | [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014); [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039) | Recalled | Consumer Defence Code (Law 8.078/1990) text; finance and health sector rules | [Planalto: Decreto 13.135 de 9 de outubro de 2026](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/decreto/d13135.htm), retrieved 22 Oct 2026 (the decree revokes Decreto 11.034/2022; Art. 25 sets entry into force 20 days after publication, and 2 Nov 2026 is this wiki's count; the Code itself was not read, so the tag stays Recalled) |
