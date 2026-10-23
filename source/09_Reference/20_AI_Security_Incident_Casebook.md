---
title: "AI Security Incident Casebook"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Reference"
nav_order: 3
description: "Real AI security incidents and disclosed vulnerabilities, each mapped to the wiki's risks, controls and OWASP items, with what would have stopped it and a link to the primary write-up."
document_type: AI Security Wiki Reference
version: 1.0
last_reviewed: 2026-10-17
---

# AI Security Incident Casebook

> **Purpose:** Ground the [Enterprise AI Risk Register](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) in things that have actually happened. Each case says what happened, which wiki risks and controls it maps to, and which control would have broken the chain.

> **Audience:** Security architects, AI engineers, risk owners and anyone making the case for a control.

> **How the facts were checked:** Each case was checked on 17 October 2026 against the source linked in its row: the researcher's or vendor's own write-up, a CVE record, a court decision, or a security advisory that reports it. Details such as affected versions can change as advisories are updated, so read the source before relying on a detail. The mapping to wiki risks, controls and OWASP items is this wiki's judgement.

## Cases at a glance

| Case | Date | Kind | Wiki risks | OWASP |
|---|---|---|---|---|
| [EchoLeak](#echoleak-microsoft-365-copilot) | June 2025 | Zero-click prompt injection and data exfiltration | AI-R05, AI-R06 | LLM01:2025, LLM02:2025, ASI01 |
| [GitHub MCP toxic agent flow](#github-mcp-toxic-agent-flow) | May 2025 | Indirect prompt injection through a public issue | AI-R05, AI-R24, AI-R07 | LLM01:2025, ASI01, MCP06:2025 |
| [postmark-mcp](#postmark-mcp-malicious-mcp-server) | September 2025 | Malicious MCP server on a public registry | AI-R23, AI-R08 | ASI04, MCP04:2025 |
| [mcp-remote](#mcp-remote-cve-2025-6514) | 9 July 2025 | Command injection from a malicious MCP server | AI-R23, AI-R08 | MCP05:2025, ASI04 |
| [MCP Inspector](#mcp-inspector-cve-2025-49596) | July 2025 | Remote code execution in a developer tool | AI-R23, AI-R04 | MCP07:2025 |
| [Amazon Q Developer extension](#amazon-q-developer-extension-1840) | July 2025 | Destructive prompt shipped in a coding assistant | AI-R08, AI-R23 | ASI04, LLM03:2025 |
| [Replit production database](#replit-production-database-deletion) | July 2025 | Agent deleted a production database during a code freeze | AI-R07, AI-R19 | LLM06:2025, ASI10 |
| [Air Canada chatbot](#air-canada-chatbot-ruling) | 14 February 2024 | Organization held liable for its chatbot's wrong answer | AI-R12, AI-R20 | LLM09:2025 |
| [Mata v. Avianca](#mata-v-avianca) | June 2023 | Invented case citations filed in court | AI-R12, AI-R19 | LLM09:2025 |

## Cases

### EchoLeak (Microsoft 365 Copilot)

**What happened.** Aim Labs reported a zero-click flaw, CVE-2025-32711 (CVSS 9.3), in Microsoft 365 Copilot. An attacker sent an email worded to slip past Copilot's injection classifiers; when Copilot later retrieved it, the hidden instructions led it to put confidential data into a Markdown link or image. Reference-style Markdown was not filtered, and the image was routed through an allowed Microsoft Teams domain to get past the content security policy, so the data reached the attacker's server. Microsoft said the issue was fully resolved and no customer action was needed. Sources: [SOC Prime summary of CVE-2025-32711](https://socprime.com/blog/cve-2025-32711-zero-click-ai-vulnerability/) and [Simon Willison's summary of the Aim Labs write-up](https://simonwillison.net/2025/Jun/11/echoleak/).

**Maps to.** [AI-R05](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) prompt injection and [AI-R06](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) output leakage. Controls: [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-018](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-018), [AI-CTRL-020](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-020).

**What breaks the chain.** Treat every email and document as untrusted, and remove the outbound channel: do not render remote images or links in output, in any Markdown syntax, and keep the allow-list for rendered content as narrow as possible. This is the [lethal trifecta](../24_Builder_Track/02_Agent_Architecture_Patterns.md#the-lethal-trifecta-and-the-rule-of-two) in a single assistant.

### GitHub MCP toxic agent flow

**What happened.** Invariant Labs showed that a prompt injection in an issue on a public GitHub repository could make a user's agent, connected through the GitHub MCP server, read the user's private repositories and publish their contents in a pull request on the public repository. The researchers stressed that the MCP server code was not at fault: the flaw is in how the agent combines tools. Published 26 May 2025. Source: [Invariant Labs](https://invariantlabs.ai/blog/mcp-github-vulnerability).

**Maps to.** [AI-R05](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R24](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) tool chain manipulation and [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md). Controls: [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016), [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022), [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024).

**What breaks the chain.** Scope the agent's token to the one repository the task needs, so private data is out of reach in a session that reads public content.

### postmark-mcp (malicious MCP server)

**What happened.** An npm package that let AI assistants send email through Postmark was changed so that every outgoing email was also blind-copied to an outside address. Snyk reported it on 25 September 2025 and placed the start of the behaviour around version 1.0.16. Source: [Snyk](https://snyk.io/blog/malicious-mcp-server-on-npm-postmark-mcp-harvests-emails/).

**Maps to.** [AI-R23](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) skill, plugin and MCP server supply chain. Controls: [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031).

**What breaks the chain.** Install MCP servers only from a reviewed allow-list, pin versions, and review each update before it is accepted. Egress limits on the server would also have blocked the copy to an unknown host.

### mcp-remote (CVE-2025-6514)

**What happened.** On 9 July 2025 JFrog reported an OS command injection, CVE-2025-6514 (CVSS 9.6), in the `mcp-remote` npm package. A malicious MCP server could return a crafted authorization endpoint URL that the client then executed, so simply connecting to a hostile server could run commands on the user's machine. Source: [JFrog advisory](https://research.jfrog.com/vulnerabilities/mcp-remote-command-injection-rce-jfsa-2025-001290844/).

**Maps to.** [AI-R23](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md). Controls: [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031), [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027).

**What breaks the chain.** Connect only to approved MCP servers and patch MCP client libraries. The MCP specification now requires clients to reject dangerous URL schemes such as `file:` and never to open URLs through a shell (see [Identity and Authorization for Agents](../24_Builder_Track/02_Agent_Architecture_Patterns.md#identity-and-authorization-for-agents)).

### MCP Inspector (CVE-2025-49596)

**What happened.** MCP Inspector, a debugging tool for MCP servers, had a critical flaw (CVSS 9.4) in versions before 0.14.1. Its web client and local proxy did not authenticate each other, so a malicious website visited by a developer could run commands on the developer's machine. Fixed in 0.14.1. Source: [Qualys ThreatPROTECT](https://threatprotect.qualys.com/2025/07/03/anthropic-model-context-protocol-mcp-inspector-remote-code-execution-vulnerability-cve-2025-49596/).

**Maps to.** [AI-R23](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) and [AI-R04](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) developer tooling. Controls: [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004), [AI-CTRL-032](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-032).

**What breaks the chain.** Keep AI developer tools in the patch inventory, and never leave unauthenticated local services listening.

### Amazon Q Developer extension 1.84.0

**What happened.** A commit merged into the Amazon Q Developer extension for Visual Studio Code added a prompt instructing the assistant to delete the user's local files and cloud resources. Version 1.84.0 was published on 17 July 2025, removed after the problem was found, and replaced by 1.85.0. Amazon said the code was malformed and would not run; some researchers disputed this. Source: [TechRadar](https://www.techradar.com/pro/amazon-ai-coding-agent-hacked-to-inject-data-wiping-commands).

**Maps to.** [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) and [AI-R23](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md). Controls: [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031), [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004), [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016).

**What breaks the chain.** Treat prompts and agent instructions as code that needs review, and do not give coding assistants standing cloud credentials that can delete resources.

### Replit production database deletion

**What happened.** In July 2025 Jason Lemkin, founder of SaaStr, reported that the Replit AI agent deleted his production database despite an instruction not to change code during a code freeze, and then gave misleading accounts of what it had done. Source: [AI Incident Database report 5578](https://incidentdatabase.ai/reports/5578/), which summarises coverage in *The Register*.

**Maps to.** [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) and [AI-R19](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md). Controls: [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025).

**What breaks the chain.** An instruction in a prompt is not a control. A code freeze has to be enforced outside the model, by credentials that cannot write to production and by approval for destructive actions.

### Air Canada chatbot ruling

**What happened.** In *Moffatt v. Air Canada*, 2024 BCCRT 149, decided on 14 February 2024, British Columbia's Civil Resolution Tribunal held Air Canada liable for negligent misrepresentation after its website chatbot told a customer he could apply for a bereavement fare after travelling, which another page of the airline's website contradicted. The tribunal rejected Air Canada's argument that the chatbot was a separate legal entity responsible for its own actions. Source: [McCarthy Tétrault](https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot).

**Maps to.** [AI-R12](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) and [AI-R20](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md). Controls: [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039).

**What breaks the chain.** Ground answers about policies and prices in the approved source, and test factual accuracy on the topics customers ask about.

### Mata v. Avianca

**What happened.** On 22 June 2023 the US District Court for the Southern District of New York sanctioned lawyers who had filed a brief citing court decisions that did not exist, generated with ChatGPT, and who kept defending them when questioned. The court imposed a $5,000 penalty. Source: [a copy of the sanctions order](https://www.nhd.uscourts.gov/sites/default/files/pdf/Mata-v-Avianca-sanctions-order.PDF).

**Maps to.** [AI-R12](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) and [AI-R19](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md). Controls: [AI-CTRL-039](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-039), [AI-CTRL-044](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-044), [AI-CTRL-045](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-045).

**What breaks the chain.** Citation verification before anything is filed or published, and training that makes clear the person who signs is accountable.

## Adding a case

Add a case only when there is a primary or authoritative source: the researcher's or vendor's advisory, a CVE record, a court or regulator decision, or a report that cites one of these. Give the date, link the source, keep to what the source says, and map the case to register risks and controls. Leave out attribution of motive unless the source states it.

## Related pages

- [Agent Architecture Patterns](../24_Builder_Track/02_Agent_Architecture_Patterns.md)
- [OWASP MCP Top 10 Crosswalk](../23_Framework_Crosswalks/19_OWASP_MCP_Top_10_Crosswalk.md)
- [OWASP Top 10 Crosswalk](../23_Framework_Crosswalks/06_OWASP_Top_10_Crosswalk.md)
- [Enterprise AI Risk Register](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md)
