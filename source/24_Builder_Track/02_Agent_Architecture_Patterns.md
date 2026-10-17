---
title: "Agent Architecture Patterns"
author: Nachiket Sathaye
parent: "Builder Track"
nav_order: 2
description: "Design-level defences for agents: the lethal trifecta and the Agents Rule of Two, six design patterns that contain prompt injection, identity and authorization standards for agents and MCP, tracing, and an architect's review checklist."
document_type: AI Security Wiki Reference
version: 1.0
last_reviewed: 2026-10-17
---

# Agent Architecture Patterns

> **Purpose:** Give architects the design decisions that make an agent safe even when the model is fooled. [Secure Your First Agent](01_Secure_Your_First_Agent.md) gives ten controls with code; this page explains how to arrange an agent so those controls have something to hold.

> **Audience:** Security architects, AI platform engineers and reviewers of agent designs.

> **How the facts were checked:** Each named pattern, rule and standard links to its primary source, read on 17 October 2026. How they map to wiki controls is this wiki's judgement.

## The starting point: the model is not a security boundary

A language model cannot reliably tell instructions from data, so any rule that depends on the model obeying it ("never reveal X", "only call tools this user may use") can be talked around. Put every authorization decision in deterministic code that uses the authenticated user's identity, have the model propose actions as structured calls, and validate them before they run ([B5](01_Secure_Your_First_Agent.md#b5-validate-every-argument-outside-the-model), [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022)). Assume the system prompt will leak, and keep secrets out of it.

The [Replit case](../09_Reference/20_AI_Security_Incident_Casebook.md#replit-production-database-deletion) shows the failure: a code freeze stated in conversation was not enforced anywhere the model could not override.

## The lethal trifecta and the Rule of Two

Simon Willison's ["lethal trifecta"](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) (16 June 2025) names three capabilities that together let an attacker steal data through prompt injection:

1. Access to private data.
2. Exposure to untrusted content: anything an attacker can get in front of the model, such as web pages, inbound email, tickets, documents or tool output.
3. The ability to communicate externally, in any way that can carry data out (sending email, HTTP requests, rendering a remote image or link, posting a comment or pull request).

Meta's ["Agents Rule of Two"](https://ai.meta.com/blog/practical-ai-agent-security/) (31 October 2025) states a related rule. In a single session an agent should have no more than two of: processing untrustworthy inputs, access to sensitive systems or private data, and the ability to change state or communicate externally. If a task needs all three, the agent should not run autonomously; it needs human approval or another reliable check.

**How to use it in a review.** For each agent and each session, mark which of the three it has. If it has all three, remove one or add a gate:

| Remove | How |
|---|---|
| Private data | Scope credentials to the data this task needs ([AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016)); for example one repository per session, as in the [GitHub MCP case](../09_Reference/20_AI_Security_Incident_Casebook.md#github-mcp-toxic-agent-flow). |
| Untrusted content | Split reading untrusted content into a separate agent or step with no access to private data (see the patterns below). |
| External communication | Allow-list egress ([B8](01_Secure_Your_First_Agent.md#b8-limit-egress-to-named-hosts)), turn off rendering of remote images and links, and remove send, post and forward tools the task does not need. |
| None of them | Require approval showing the exact action, not the agent's summary of it ([B6](01_Secure_Your_First_Agent.md#b6-gate-sensitive-actions-behind-approval)). |

Question A6 in the [AI Use-Case Risk Triage](../02_Risk_Management/02F_AI_Use_Case_Risk_Triage.md) asks this at intake.

## Design patterns that contain prompt injection

The paper [*Design Patterns for Securing LLM Agents against Prompt Injections*](https://arxiv.org/abs/2506.08837) (Beurer-Kellner and others, 2025) describes six patterns. Each gives up some flexibility so that injected text cannot change what the agent does.

| Pattern | How it works | Good fit |
|---|---|---|
| Action-Selector | The model only chooses from a fixed set of actions, and the results never go back into its context. | Front-ends that route requests to known operations. |
| Plan-Then-Execute | The agent fixes its plan of tool calls from the trusted request before it reads untrusted content. Injected text can change data, not which actions run. | Tasks whose steps are known in advance, such as "summarise this ticket and draft a reply". |
| LLM Map-Reduce | Each untrusted item is processed by a separate, isolated model call with constrained output, and a safe step combines the results. | Processing many documents or emails. |
| Dual LLM | A privileged model plans and uses tools but never sees untrusted text; a quarantined model reads untrusted text but has no tools. Results pass between them as references or validated structured data. | Assistants that must act on content from outside. |
| Code-Then-Execute | The model writes a program that calls tools, and the program then runs over untrusted data. Google DeepMind's [CaMeL](https://simonwillison.net/2025/Apr/11/camel/) extends this with capability tags on data and an interpreter that blocks flows that break policy. | Complex tasks where a plan can be expressed as code. |
| Context-Minimization | Content that has served its purpose is removed from the context so it cannot influence later steps. | Long conversations that mix trusted and untrusted input. |

None of these is free: they reduce what the agent can do. Choose the least restrictive pattern that breaks the trifecta for the task, and keep the deterministic controls in [Secure Your First Agent](01_Secure_Your_First_Agent.md) behind it.

## Treat everything in the context as untrusted

User prompts, retrieved chunks, tool results, tool descriptions, memory entries, other agents' messages and the model's own earlier output can all carry instructions. Label each item with its source and trust level, strip hidden text (zero-width characters, white-on-white text, HTML comments) on the way in, and validate output against a strict schema before anything downstream uses it ([AI-CTRL-020](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-020)). Content does not become trusted because a trusted tool fetched it.

## Identity and authorization for agents

An agent without its own identity cannot be given least privilege, audited or revoked ([B2](01_Secure_Your_First_Agent.md#b2-give-it-its-own-identity), [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015)). These standards implement it:

| Need | Standard | What it does |
|---|---|---|
| Act for a user without borrowing their credentials | [OAuth 2.0 Token Exchange, RFC 8693](https://www.rfc-editor.org/rfc/rfc8693) | Defines delegation, in which the agent keeps its own identity and acts for the user (recorded in the token's `act` claim), so downstream systems see both and can enforce the user's permissions. This is the main treatment for AI-R46. |
| Make a token useless anywhere else | [Resource Indicators for OAuth 2.0, RFC 8707](https://www.rfc-editor.org/rfc/rfc8707) | Lets the client name the service a token is for, so the authorization server can restrict the token to that service. |
| Make a stolen token hard to use | [DPoP, RFC 9449](https://www.rfc-editor.org/rfc/rfc9449), or mutual TLS | Binds access and refresh tokens to a key pair the client holds, so a stolen token is useless without the private key. |
| Give each workload an identity | Workload identity from the platform, or [SPIFFE](https://spiffe.io/) | Replaces shared API keys with short-lived, attested identities. |

**MCP servers.** The MCP specification's [security best practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) (version 2025-11-25, read on 17 October 2026) say that MCP servers must not accept any token that was not explicitly issued for that server, so token passthrough is forbidden. They also require clients to accept only `https` authorization URLs (or `http` for local development), to reject schemes such as `javascript:` and `file:`, and never to open URLs through a shell, which is the class of flaw in the [mcp-remote case](../09_Reference/20_AI_Security_Incident_Casebook.md#mcp-remote-cve-2025-6514). They recommend starting with minimal scopes and asking for more only when a privileged operation is first attempted.

Keep credentials out of the model's context: tools fetch secrets from a vault when they run ([AI-R22](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md)).

## Tracing and shutdown

Trace every step: the prompt, the IDs of retrieved content, the model and version, each tool call with its arguments and result, each approval decision, and the identity of the agent and the user behind every action ([B10](01_Secure_Your_First_Agent.md#b10-log-every-decision-in-a-tamper-evident-trace), [AI-CTRL-008](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-008)). OpenTelemetry publishes [semantic conventions for generative AI](https://github.com/open-telemetry/semantic-conventions-genai) so these traces can join existing monitoring pipelines. They are at the Development stability level, which means names can change between releases, so check their status before depending on them.

Signals worth alerting on include unusual sequences of tool calls, sudden growth in token use, new outbound domains, repeated denied actions and retrieval much broader than usual. Telling sanctioned agent activity from an attack is itself a risk ([AI-R45](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md)). Shutdown must work in seconds: per-agent and per-tool disable switches, central token revocation, and circuit breakers that pause an agent after repeated policy violations or a cost threshold ([B9](01_Secure_Your_First_Agent.md#b9-cap-the-blast-radius-and-keep-a-kill-switch), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025)).

## Architect's review checklist

Use these questions on any agent, LLM application or MCP design. A "no" or "don't know" is a finding.

1. **Trifecta.** Does any single agent or session have private data, untrusted input and an outbound channel? If so, what gates it?
2. **Where authorization happens.** Is every authorization decision made outside the model, using the end user's identity?
3. **Context trust map.** Can you list every source that enters the context and its trust level?
4. **Tools.** For each tool, is the scope as narrow as possible, is there a named approver, and is its definition pinned?
5. **Identity.** Does each agent have its own identity, and do downstream systems see the user it acts for?
6. **Blast radius.** If this agent were fully compromised, what is the worst outcome, and can it be made smaller?
7. **Human approval.** Do approvers see the real action (amount, recipient, command), and is the number of approvals low enough that people still read them?
8. **Execution.** Does generated code run in a sandbox with no standing secrets and restricted egress?
9. **Memory and retrieval.** Are writes validated, scoped to the user and tenant, and reversible?
10. **Detection and response.** Can you trace any action from end to end, and stop the agent within a minute?
11. **Supply chain.** Are models, prompts, MCP servers and dependencies inventoried, pinned and verified?
12. **Testing.** Do automated adversarial and regression tests gate every change to the model, prompt or tools?

## Exercises

1. **Trifecta audit.** Take a developer's coding agent connected to a source repository, a database and a chat tool. Mark which of the three capabilities each connection gives, then design two alternatives that each remove one, and compare what each costs the developer.
2. **Policy writing.** For a customer-support agent that can issue refunds, write the policy in plain language and then in your policy engine's language: refund limits, allowed email domains and approval tiers.
3. **Threat model.** Apply STRIDE, or an agent-specific method such as the Cloud Security Alliance's [MAESTRO](https://cloudsecurityalliance.org/articles/agentic-ai-threat-modeling-framework-maestro), to the same agent, and map each threat to an OWASP item and a wiki control.
4. **Incident drill.** An MCP server you use changes a tool description after approval. Write the detection signal, the containment steps and the recovery plan, and compare them with [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024).

## Related pages

- [Secure Your First Agent: Ten Controls With Code](01_Secure_Your_First_Agent.md)
- [AI Security Incident Casebook](../09_Reference/20_AI_Security_Incident_Casebook.md)
- [OWASP MCP Top 10 Crosswalk](../23_Framework_Crosswalks/19_OWASP_MCP_Top_10_Crosswalk.md)
- [Agents, Identity and Excessive Agency](../00_Foundations/05-Agents-Identity-and-Excessive-Agency.md)
