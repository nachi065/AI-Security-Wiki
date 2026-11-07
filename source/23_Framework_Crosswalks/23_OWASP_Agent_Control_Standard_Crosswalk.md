---
title: "OWASP Agent Control Standard Crosswalk"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Framework Crosswalks"
nav_order: 23
description: "The OWASP Agent Control Standard, a wire protocol for agent runtime enforcement, placed against the wiki's controls: which control each ACS hook enforces, what each conformance profile needs, and what ACS deliberately leaves to the deployment."
document_type: AI Security Wiki Reference
version: 1.0
last_reviewed: 2026-11-07
---

# OWASP Agent Control Standard Crosswalk

> **Purpose:** Let a team adopting the Agent Control Standard see which wiki controls each of its enforcement points carries, and what the standard expects the deployment to supply for itself.

> **Audience:** AI platform engineers, security architecture, agent developers, application security.

> **Using the two together:** ACS gives you the places to enforce. This wiki gives you what to enforce there.

## Read this before using the page

The Agent Control Standard is not a control framework and does not read like the other pages in this section. It has no numbered control catalogue, no requirements of the form "the organisation shall", and nothing to score an audit against. It is a JSON-RPC wire protocol between an agent and a policy enforcement point, and it says of itself that it "does not define what policies to enforce".

That makes the usual crosswalk direction wrong. The other pages in this section take a framework's items and find the wiki controls that answer them. Here there are no items to answer. What ACS gives instead is a standard set of **places** where a decision can be taken, and a standard record of what was decided. So this page runs the mapping the other way: for each ACS enforcement point, which wiki control supplies the policy that belongs there.

Four things about its status matter before anyone plans around it.

- **It is pre-1.0.** The specification is version `v0.1.0`; the latest release when this page was written was `0.1.4`, dated 16 October 2026. Version `v0.2.0` is targeted for March 2027 and no v1.0 date has been set. Pre-1.0 releases may change the mandatory baseline in a patch version, and the schemas change in place at the same addresses, so pin a commit rather than a version when you depend on it.
- **Nobody verifies a conformance claim.** Profiles are self-declared on the wire at the handshake. Version 0.1.0 ships no conformance test suite, no registry of conformant implementations and no body to arbitrate a disputed claim. A declared profile is a statement of intent, not evidence, and [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014) still applies to any vendor who claims one.
- **The defaults fail open.** `on_decision_failure` defaults to `proceed`, and the startup posture when the handshake itself fails also defaults to `proceed`. A policy point that crashes, hangs or is unreachable therefore stops governing while the agent keeps acting. The standard states this plainly and describes the effect as converting control into audit. Any deployment that relies on ACS for enforcement should set the deny posture explicitly; see [AI-CTRL-040](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-040).
- **A conformance claim covers the wire format only.** The standard says a permissive policy point is "a conformant but permissive deployment, not a violation", and that ACS-Core does not assert the audit chain is tamper-evident against a compromised policy point. So a claim tells a reviewer that the messages are well formed, and nothing about how strict the policies behind them are.

The mapping below is this wiki's judgement and has not been reviewed by OWASP. Identifiers, method names and profile names were read from the project's own repository and documentation site on 7 November 2026; see reference [28] in the [Foundations references](../00_Foundations/References.md). The OWASP lists of agentic and LLM risks are in the [OWASP Top 10 Crosswalk](06_OWASP_Top_10_Crosswalk.md), and the Model Context Protocol list is in the [OWASP MCP Top 10 Crosswalk](19_OWASP_MCP_Top_10_Crosswalk.md).

## How ACS is put together

Two parties sit on the wire. The **Observed Agent** is the system being watched. The **Guardian Agent** is the policy enforcement point, and it runs a deterministic policy layer first, with an optional model-based layer that is never shown the policy source. The agent itself is required to have no knowledge of the hooks, and provenance must be populated outside the model's output path, so neither can be talked out of firing by the content the agent is processing.

The standard has three pillars.

| Pillar | What it standardises | The wiki's nearest concern |
|---|---|---|
| **Instrument** | The lifecycle hooks where a decision can be taken, and the five verdicts available | [Deterministic Action Authorization](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022) |
| **Trace** | Deterministic event emission, mapped to OpenTelemetry semantic conventions and OCSF 1.9.0 event classes | [Auditability](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) and [SOC Integration](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009) |
| **Inspect** | An Agent Bill of Materials of the components an agent uses, serialised to CycloneDX 1.6, SPDX 3.0 or SWID | [AI Supply Chain and AI-BOM](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) |

The five verdicts a Guardian may return are `ALLOW`, `DENY`, `MODIFY`, `ASK` and `DEFER`. Four must be supported; `MODIFY` is optional, and a Guardian that cannot use it has to substitute a `DENY` and say why. `ASK` routes the decision to a named approver, which is the wire-level form of [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023). `DEFER` carries its own timeout, and its default on timeout is `deny`, which is the opposite of the fail-open default that applies when the channel breaks.

## Enforcement points to wiki controls

Nineteen lifecycle hooks and three further methods make up the control surface. Fourteen of the nineteen can carry a decision; five are audit only. The column that matters for planning is the last one: what the deployment has to decide for itself once the hook is wired up.

**Mandatory in ACS-Core** marks the hooks a deployment must emit to claim the baseline profile at all.

| ACS method | Fires | Decisions | Wiki controls that supply the policy | What ACS leaves to you |
|---|---|---|---|---|
| `sessionStart` | Session start, before any content enters. Mandatory in ACS-Core | ALLOW, DENY | [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006), [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015) | Which sessions to refuse, and the identity the agent must present |
| `agentTrigger` | External activation: user message, schedule, external event, inbound agent call. Mandatory in ACS-Core as an alternative to `userMessage` | ALLOW, DENY, MODIFY | [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006), [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002) | Which trigger types are allowed to start an agent unattended |
| `userMessage` | User input, before it reaches the agent's reasoning context. Mandatory in ACS-Core as an alternative to `agentTrigger` | ALLOW, DENY, MODIFY | [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002), [AI-CTRL-021](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-021) | What to look for in the input and what to redact |
| `turnStart`, `turnEnd` | Turn boundaries, so per-turn limits are computable rather than guessed | `turnStart` only | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) | The per-turn budget and what to do when it is reached |
| `toolCallRequest` | Before a tool runs. Mandatory in ACS-Core | ALLOW, DENY, MODIFY, ASK, DEFER | [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022), [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023) | The whole authorisation decision: which caller, which tool, which arguments |
| `toolCallResult` | After a tool runs, before the agent reads the result. Mandatory in ACS-Core | ALLOW, DENY, MODIFY | [AI-CTRL-020](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-020), [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005) | How to treat tool output as untrusted, and what to strip |
| `knowledgeRetrieval` | Retrieval from a knowledge source, before results enter context | ALLOW, DENY, MODIFY | [AI-CTRL-018](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-018), [AI-CTRL-019](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-019) | Whether this user may read these documents, enforced on the user's identity |
| `memoryContextRetrieval` | Memory read into working context | ALLOW, DENY, MODIFY | [AI-CTRL-026](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-026), [AI-CTRL-018](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-018) | Memory scoping between users, sessions and tenants |
| `memoryStore` | Memory write. The standard calls this the sink for cross-session influence | ALLOW, DENY, MODIFY | [AI-CTRL-026](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-026), [AI-CTRL-019](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-019) | What may be written to memory, and at which scope |
| `agentResponse` | Agent output, before it reaches the user or a peer. Mandatory in ACS-Core | ALLOW, DENY, MODIFY | [AI-CTRL-020](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-020), [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) | Output encoding, leak detection and what the user is told |
| `preCompact` | Before the context window is compacted. The standard names compaction as where provenance is laundered | ALLOW, DENY | [AI-CTRL-026](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-026) | Whether to refuse a compaction that would merge across a trust boundary |
| `postCompact` | After compaction, carrying the new summary's lineage. `DENY` is not legal here | MODIFY only | [AI-CTRL-026](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-026), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) | Nothing to decide; this is where you check the lineage the framework wrote |
| `subagentStart` | A subagent is spawned in process. Mandatory in ACS-Core for subagent-capable clients | ALLOW, DENY | [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006), [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) | Whether a child may hold authority the parent was not granted |
| `subagentStop` | A subagent ends | Audit only | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) | Nothing to decide |
| `skillRegister` | A skill enters the available set, with its definition, digest and declared capabilities visible | ALLOW, DENY | [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) | The vetting decision, and whether declared capabilities match what the skill composes |
| `skillLoad` | A registered skill activates in a session | ALLOW, DENY | [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024) | Whether this activation traces back to an approved definition and digest |
| `skillUnload` | A skill leaves the active set | Audit only | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) | Nothing to decide |
| `sessionEnd` | Session ends and the audit chain is sealed. Mandatory in ACS-Core | Audit only | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) | Reading the per-class count of decision failures, which is how you learn enforcement lapsed |
| `agbom/snapshot` | Once per session, before any content-bearing hook | ALLOW, DENY | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031), [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) | Which components are banned, and what an unexpected one means |
| `agbom/changed` | A component is added, removed or changed mid-session | ALLOW, DENY | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031), [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024) | Whether a hot swap mid-session is allowed at all |
| `protocols/MCP/*` | MCP traffic wrapped in the ACS envelope. Mandatory for any deployment whose sessions involve MCP | Yes, and audited | [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024), [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005) | The MCP policy itself. The standard calls `resources/read` the canonical prompt-injection ingress |
| `system/ping` | Liveness probe. Always allowed, outside the audit chain | None | [AI-CTRL-040](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-040) | The standard warns a successful ping does not prove enforcement is healthy; monitor decision failures instead |

`protocols/A2A/*` is reserved for version 0.2, so agent-to-agent traffic across a network boundary is not covered. The wiki's controls for it stand on their own until then; see [Agentic AI Security and Tool Governance](../04_Domain_Standards/09_Agentic_AI_Security_and_Tool_Governance.md).

## Conformance profiles to wiki controls

Seven profiles are declared at the handshake. `acs-core` is the mandatory floor and the other six layer on it independently, except `acs-inspect-dynamic`, which extends `acs-inspect`. The right-hand column is the wiki control a reviewer should ask for evidence against when a vendor or a team claims the profile.

| Profile | What claiming it commits you to | Wiki controls that evidence it |
|---|---|---|
| `acs-core` | Handshake, signed envelopes, the minimum hook set, four verdicts, session context with a rolling hash chain, replay rejection, honouring decisions, declared liveness, and wrapped MCP where MCP is in play | [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022), [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008) |
| `acs-trace` | An OpenTelemetry or OCSF event for every supported step, with the decision, its reasoning and provenance carried onto it | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-009](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009) |
| `acs-inspect` | A component inventory at session start, serialised to CycloneDX, SPDX or SWID on request | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031), [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001) |
| `acs-inspect-dynamic` | The same, plus an event on every mid-session component change, written into the audit chain | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031), [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024) |
| `acs-provenance` | A provenance object on every data-bearing field in every hook, produced deterministically rather than by the model. Partial population is non-conformant | [AI-CTRL-026](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-026), [AI-CTRL-019](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-019) |
| `acs-crypto` | Post-quantum signatures, at least `ML-DSA-65`, giving non-repudiation the shared-secret baseline cannot | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-032](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-032) |
| `acs-audit` | A hash of the request content on every chain entry, so the chain commits to what was asked and not only that something was asked | [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035), [AI-CTRL-038](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-038) |

ACS-Core explicitly does not require provenance objects, trace emission, a component inventory, asymmetric signatures or request hashing. A deployment can be fully conformant with none of them, so "ACS conformant" on its own tells a reviewer very little. Ask which profiles.

The project publishes a one-page conformance claim template whose cells are limited to `EXERCISED`, `NOT CLAIMED` and `NOT ESTABLISHED`, with reason codes for each. It is the closest thing the standard has to an assessment instrument, and a completed one is reasonable evidence to request under [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014).

## Where the two overlap and where each stands alone

| | ACS | This wiki |
|---|---|---|
| Where a decision is taken | Standardises 22 named points on the wire | Names the control objective but not the hook |
| What the decision is | Deliberately out of scope | The substance of the {{n:controls}} controls |
| Audit record | A hash-chained session record with mappings to OpenTelemetry and OCSF | Says what to log and keep, not the schema |
| Component inventory | A schema and three serialisations | Requires an AI-BOM, no format mandated |
| Human approval | A wire primitive with an authenticated approver | An approval gate with an accountable owner |
| Governance, risk tiering, procurement, training | Not in scope | [AI-CTRL-011](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-011), [AI-CTRL-012](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-012), [AI-CTRL-014](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-014), [AI-CTRL-044](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-044) |
| Testing that enforcement holds | No test suite in v0.1.0 | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) and the [Test Case Library](../10_Test_Case_Library/index.md) |
| Model and training-data concerns | Not in scope | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029), [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030) |

Three wiki controls have no counterpart in ACS at all and are worth naming, because a team that adopts ACS may assume otherwise. [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) covers containment and a kill switch: ACS can deny the next decision-eligible hook, but it defines no way to stop a session already in flight, and mid-flight attachment of a Guardian is undefined in version 0.1. [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027) covers execution isolation, which is a property of where the code runs and not of the wire. And multi-tenancy is a reserved field with no isolation rules in version 0.1, so tenant separation rests entirely on [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) and [AI-CTRL-018](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-018).

## What ACS says about the agentic risk list

The standard publishes one mapping of its own, from its mechanisms to the OWASP Top 10 for Agentic Applications. It appears in the project's FAQ, which states that it is non-normative and that the specification governs where the two disagree, and it describes itself as "mechanism-to-control, not promise-to-eliminate". The table below is this wiki's summary of which ACS mechanism that mapping names, next to the wiki controls the [OWASP Top 10 Crosswalk](06_OWASP_Top_10_Crosswalk.md) already records for the same risk.

| Agentic risk | The ACS mechanism its own mapping names | Wiki controls |
|---|---|---|
| ASI01 Agent Goal Hijack | Intent fixed at session start and immutable to the model, extended only through an approved `ASK` | [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022) |
| ASI02 Tool Misuse and Exploitation | `toolCallRequest` before every outward action, with argument rewriting where `MODIFY` is supported | [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022), [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024) |
| ASI03 Identity and Privilege Abuse | Per-session signing keys, replay rejection, and denial of a subagent spawn that would widen authority | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015), [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016) |
| ASI04 Agentic Supply Chain Vulnerabilities | The component inventory, decision-eligible component changes, and skill vetting on definition and digest | [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031), [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024) |
| ASI05 Unexpected Code Execution | Shell, process and code actions must cross `toolCallRequest` even when the tool registry does not model them | [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027), [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022) |
| ASI06 Memory and Context Poisoning | Memory reads and writes gated, with lineage carried and compaction bound to what it compacted | [AI-CTRL-026](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-026), [AI-CTRL-019](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-019) |
| ASI07 Insecure Inter-Agent Communication | In-process spawning crosses a decision point; signed envelopes with replay rejection. Network A2A waits for v0.2 | [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015), [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006) |
| ASI08 Cascading Failures | A denial at the spawn boundary stops a cascade; parent and child references preserve the path | [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025), [AI-CTRL-040](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-040) |
| ASI09 Human-Agent Trust Exploitation | `ASK` as a wire primitive with an authenticated approver, and `agentResponse` gating output | [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045) |
| ASI10 Rogue Agents | Handshake identity, a component baseline, and continuous hook traffic that makes behaviour observable | [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001), [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006) |

The standard publishes no mapping to the OWASP Top 10 for LLM Applications. It also states that it does not prevent prompt injection, and that what it offers against that class is deviation detection after the fact rather than prevention. Treat [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005) and [AI-CTRL-002](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-002) as unaffected by adopting it.

## If you are adopting it

The order below reflects what the standard makes mandatory and where its defaults need overriding, not a maturity model of its own; ACS defines none.

1. Set the fail-closed posture before anything else. Both the decision-failure default and the handshake-failure default are permissive out of the box, and an unreachable policy point otherwise degrades to an audit log without saying so.
2. Claim `acs-core` and wire `toolCallRequest` first. It is the point the standard calls central, and it is where [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022) lands. Make sure filesystem, network and process actions fire it even when the tool registry does not call them tools.
3. Wrap MCP if MCP is anywhere in the session. It is mandatory in the baseline for those deployments, and without it the ingress the standard names as the main injection route is unmediated.
4. Add `acs-trace` next if you have a SOC. The OCSF class mappings are what make agent decisions legible to existing tooling, which is [AI-CTRL-009](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-009).
5. Measure enforcement by its failures. The per-class count of decision failures at session end is the honest measure of how often enforcement lapsed, and the standard warns that a healthy liveness probe does not mean a healthy enforcement path.
6. Test the enforcement path yourself. There is no conformance suite, so the evidence that a hook actually denies comes from [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) and the agent cases in the [Test Case Library](../10_Test_Case_Library/index.md).

## Attribution

The Agent Control Standard is published by the OWASP GenAI Security Project, with code and schemas under the Apache License 2.0 and prose documentation under CC BY-SA 4.0. This page cites method names, profile names and structure only, and paraphrases requirements rather than reproducing specification text. Check the project's licensing before reusing its wording.

## Related pages

- [OWASP Top 10 Crosswalk](06_OWASP_Top_10_Crosswalk.md)
- [OWASP MCP Top 10 Crosswalk](19_OWASP_MCP_Top_10_Crosswalk.md)
- [Agentic AI Security and Tool Governance](../04_Domain_Standards/09_Agentic_AI_Security_and_Tool_Governance.md)
- [Agent Architecture Patterns](../24_Builder_Track/02_Agent_Architecture_Patterns.md)
- [Secure Your First Agent](../24_Builder_Track/01_Secure_Your_First_Agent.md)
- [AI Security Control Objectives Library](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md)
