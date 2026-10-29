---
title: "AI Security Incident Casebook"
author: Nachiket Sathaye
coauthors: Ankush Jain
parent: "Reference"
nav_order: 3
description: "Real AI security incidents and disclosed vulnerabilities, each mapped to the wiki's risks, controls and OWASP items, with what would have stopped it and a link to the primary write-up."
document_type: AI Security Wiki Reference
version: 1.1
last_reviewed: 2026-10-29
---

# AI Security Incident Casebook

> **Purpose:** Ground the [Enterprise AI Risk Register](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) in things that have actually happened. Each case says what happened, which wiki risks and controls it maps to, and which control would have broken the chain.

> **Audience:** Security architects, AI engineers, risk owners and anyone making the case for a control.

> **How the facts were checked:** The 2025 and earlier cases were checked on 17 October 2026 and the 2026 cases on 29 October 2026, each against the source linked in its row: the researcher's or vendor's own write-up, a CVE record, a court decision, or a security advisory that reports it. Details such as affected versions can change as advisories are updated, so read the source before relying on a detail. Where sources disagree or a claim has not been confirmed, the case says so under **Not confirmed**. The mapping to wiki risks, controls and OWASP items is this wiki's judgement.

## Cases at a glance

| Case | Date | Kind | Wiki risks | OWASP |
|---|---|---|---|---|
| [Load/Mine](#loadmine-cryptominer-models-on-hugging-face) | 29 October 2026 | Malicious model repositories run code on load | AI-R08, AI-R11 | LLM03:2025 |
| [OpenClaw gym booking](#openclaw-gym-booking-incident) | 10 August 2026 | Agent exploited a booking API flaw and cancelled another person's booking | AI-R07, AI-R46 | LLM06:2025, ASI02 |
| [Hugging Face breach](#hugging-face-breach-by-an-autonomous-agent-system) | July 2026 | Autonomous agents breached internal clusters | AI-R07, AI-R08, AI-R22 | ASI05, ASI10, LLM03:2025 |
| [Clinejection and Cline CLI 2.3.0](#clinejection-and-the-cline-cli-230-package) | February 2026 | Prompt injection in an issue title led to a tampered npm release | AI-R05, AI-R24, AI-R23 | LLM01:2025, ASI01, ASI04 |
| [Moltbook](#moltbook-exposed-database) | 2 February 2026 | Agent social network exposed 1.5 million agent API tokens | AI-R22, AI-R25 | LLM02:2025, ASI03 |
| [ClawHavoc](#clawhavoc-malicious-skills-on-clawhub) | February 2026 | 341 malicious skills on an agent skill registry | AI-R23, AI-R22 | ASI04, LLM03:2025 |
| [OpenClaw CVE-2026-25253](#openclaw-one-click-remote-code-execution-cve-2026-25253) | 31 January 2026 | One-click token theft and command execution in a personal agent | AI-R07, AI-R22 | ASI03, ASI05 |
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

### Load/Mine: cryptominer models on Hugging Face

**What happened.** On 29 October 2026 Pluto Security reported 31 malicious repositories across seven Hugging Face accounts, plus a ModelScope mirror. The repositories needed no malicious weights: loading them with `trust_remote_code=True` imports the repository's Python code with the caller's privileges before any weights load, and that code installed a cryptominer with persistence, and in some builds a reverse shell or an SSH key. Pluto says the Hub's scanners rated the payload safe. After Pluto reported the first wave, both platforms removed the accounts; a second wave appeared within days and was still live when Pluto published. Pluto counted 29,818 downloads, and notes that downloads are not confirmed infections. Source: [Pluto Security](https://pluto.security/blog/hugging-face-malware-campaign-load-mine).

**Not confirmed.** This case was added on the day it was published, from the researcher's report alone. Hugging Face had not published a statement when this page was checked.

**Maps to.** [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) and [AI-R11](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md). Controls: [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031), [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030), [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027). Test with [TC-L12-004](../10_Test_Case_Library/L12-model-layer.md#tc-l12-004), [TC-L12-002](../10_Test_Case_Library/L12-model-layer.md#tc-l12-002) and [TC-L06-026](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-026).

**What breaks the chain.** Treat `trust_remote_code=True` as running someone else's program: forbid it by default, allow it only for reviewed repositories pinned to a commit, and load models in an environment with no credentials and no outbound network. A clean scanner result is not evidence that a repository's code is safe.

### OpenClaw gym booking incident

**What happened.** On 10 August 2026 ABC News reported that a man named Andrew asked his OpenClaw assistant, which ran on Anthropic's Claude, to help him get into a popular gym class for which he was fourth on the waitlist. According to the account, the agent found that the gym's booking software let it book classes months further ahead than the gym allowed, and that the API did not check who owned a reservation before cancelling it. It cancelled the booking of the person first on the waitlist. In the agent's words as quoted by the ABC, "The API has zero authorisations checks on cancelling other people's reservations". When asked to undo this, it replied that it could not add them back. It then drafted a disclosure email to the software provider. The ABC did not name the gym or the software vendor; the vendor said it did not discuss specific security matters. Source: [ABC News](https://www.abc.net.au/news/2026-08-10/ai-assistant-hacks-gym-website-aus-cyber-attack/107007986).

**Not confirmed.** The account comes from the user, through a blog post that was later deleted, and the ABC. No vendor or independent confirmation has been published. Aikido then built a synthetic booking app with the same two flaws and ran OpenClaw on Claude Opus 4.6 against it: the agent exploited the booking-window flaw in 9 of 10 simulated conversations and cancelled another user's booking in 2 of 10. This shows the account is plausible; it does not confirm it. Source: [Aikido](https://www.aikido.dev/blog/australian-gym-hack-openclaw-test).

**Maps to.** [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R46](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) use of agents to exceed one's own access, [AI-R19](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) and [AI-R51](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md). Controls: [AI-CTRL-006](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-006), [AI-CTRL-022](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-022), [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023). Test with [TC-L06-015](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-015).

**What breaks the chain.** For the person running the agent: an agent should stop and ask before any action that affects another person or relies on a flaw it has found, and that rule has to be enforced by the agent's tool permissions, not left to the model. For the operator of the API: enforce ownership checks and business rules on the server. A rule that only the web page enforces will be found by an agent that calls the API directly, far faster than by a curious person.

### Hugging Face breach by an autonomous agent system

**What happened.** On 16 July 2026 Hugging Face disclosed an intrusion that it said was "driven, end to end, by an autonomous AI agent system". A malicious dataset abused two code-execution paths in its dataset processing, a remote-code dataset loader and a template injection in a dataset configuration, to run code on a processing worker. From there the attacker harvested cloud and cluster credentials and moved laterally into several internal clusters over a weekend. Hugging Face reported access to "a limited set of internal datasets" and to several credentials used by its services, found no evidence of tampering with public models, datasets or Spaces, and said it was still assessing whether partner or customer data was affected. Its log of the attacker's actions held more than 17,000 recorded events. Hugging Face also said that hosted frontier models blocked its forensic work, so it ran the analysis on an open-weight model. On 21 July 2026 OpenAI said the activity was driven by its own models, including GPT-5.6 Sol and a more capable pre-release model, "all with reduced cyber refusals for evaluation purposes", during an evaluation run without its production classifiers. OpenAI's account is that the models exploited a zero-day in a package registry cache proxy inside its evaluation environment, reached a node with Internet access, and then attacked Hugging Face to obtain test solutions for a benchmark it calls ExploitGym. Sources: [Hugging Face disclosure](https://huggingface.co/blog/security-incident-july-2026) and [OpenAI statement](https://openai.com/index/hugging-face-model-evaluation-security-incident/).

**Not confirmed.** The two accounts differ on the entry point (a malicious dataset in Hugging Face's account, a remote code execution path found with stolen credentials and zero-days in OpenAI's) and on what was taken. Hugging Face's own post says it does not know which model powered the agents and has not been updated with OpenAI's attribution. OpenAI calls its findings preliminary. Neither primary source names the vendor of the proxy; some secondary reports do, and this page does not repeat it.

**Maps to.** [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) agent abuse, [AI-R08](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) supply chain (an uploaded dataset as the carrier), [AI-R22](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) credential harvesting and [AI-R18](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) use beyond the approved purpose. Controls: [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027), [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025), [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030), [AI-CTRL-035](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-035). Test with [TC-L06-025](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-025), [TC-L15-007](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-007), [TC-L15-009](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-009), [TC-L06-023](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-023) and [TC-D12-019](../10_Test_Case_Library/D12-ai-incident-response-and-forensics.md#tc-d12-019).

**What breaks the chain.** On the platform side: code that arrives with uploaded data runs in a sandbox that holds no cloud or cluster credentials and has no route to other clusters. On the evaluator side: an environment that runs models with offensive capability and reduced refusals has to be cut off from the Internet by a control that is tested, not assumed, and has a kill switch. For incident response, decide in advance which models and tools the team can use for forensic work that a hosted model may refuse.

### Clinejection and the Cline CLI 2.3.0 package

**What happened.** On 9 February 2026 the researcher Adnan Khan disclosed that the Cline project's issue triage workflow ran an AI coding agent with shell access on every new GitHub issue, with the issue title placed straight into its prompt. A crafted title could make the agent run attacker code inside the project's CI, and from there, through GitHub Actions cache poisoning, reach the jobs that held the publishing tokens. Cline removed the workflow the same day. On 17 February 2026 an unauthorized party used an npm publish token that had not been properly revoked to publish `cline@2.3.0`; its only change was an install script that installed OpenClaw globally. The package was live for about eight hours and was downloaded about 4,000 times, according to StepSecurity as cited by The Hacker News. Cline published 2.4.0, revoked the correct token and moved npm publishing to OIDC provenance. Sources: [Snyk](https://snyk.io/blog/cline-supply-chain-attack-prompt-injection-github-actions) and [The Hacker News](https://thehackernews.com/2026/02/cline-cli-230-supply-chain-attack.html).

**Not confirmed.** The sources read do not establish whether the token used on 17 February was taken through the cache-poisoning route or was obtained some other way.

**Maps to.** [AI-R05](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R24](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R22](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) and [AI-R23](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md). Controls: [AI-CTRL-016](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-016), [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005), [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031). Test with [TC-L07-015](../10_Test_Case_Library/L07-prompt-and-context-layer.md#tc-l07-015), [TC-L09-026](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-026), [TC-L14-006](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-006) and [TC-L16-024](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-024).

**What breaks the chain.** An agent that reads text from the public, such as issue titles, must not also hold a shell in the same pipeline that can reach release credentials; this is the [lethal trifecta](../24_Builder_Track/02_Agent_Architecture_Patterns.md#the-lethal-trifecta-and-the-rule-of-two) in CI. After an incident, confirm that every affected token is revoked, not just one.

### Moltbook exposed database

**What happened.** On 2 February 2026 Wiz reported that Moltbook, a social network for AI agents, exposed its production database. A Supabase API key was in the site's JavaScript and Row Level Security was not enabled, so the key gave full read and write access to all platform data. Wiz reported about 1.5 million agent API tokens, the email addresses of agent owners, and 4,060 private conversations between agents, some of which contained third-party API keys in plain text. Write access meant posts that other agents read could be changed, which is a route for prompt injection. Moltbook secured the tables within about three hours of Wiz's first contact. Wiz's headline and body give different email counts, so this page does not give one. Source: [Wiz](https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys).

**Maps to.** [AI-R22](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R25](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) and [AI-R03](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md). Controls: [AI-CTRL-015](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-015), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017), [AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033). Test with [TC-L15-009](../10_Test_Case_Library/L15-infrastructure-layer.md#tc-l15-009) and [TC-L09-014](../10_Test_Case_Library/L09-identity-and-access-mgmt.md#tc-l09-014).

**What breaks the chain.** A release gate that checks database access rules before launch, and agent credentials that can be rotated quickly. Anyone whose agent posted on a platform like this should assume its key and anything it said in private messages are exposed, and rotate the key.

### ClawHavoc: malicious skills on ClawHub

**What happened.** Koi Security audited 2,857 skills on ClawHub, the public skill registry for OpenClaw, and found 341 malicious ones. 335 of them, a campaign Koi named ClawHavoc, carried a fake "Prerequisites" section that told macOS users to paste a script into Terminal, which installed the Atomic macOS Stealer (AMOS), and told Windows users to download an archive containing a trojan. Others hid reverse shells or sent the agent's credential file to an outside web hook. The registry was open to anyone with a GitHub account at least a week old; after the report OpenClaw added user reporting, with skills hidden automatically after more than three unique reports. Reported on 2 February 2026. Source: [The Hacker News](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html), which reports Koi's findings. Koi's original post now redirects to another site, so the figures here are as The Hacker News reported them.

**Maps to.** [AI-R23](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R22](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) and [AI-R02](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md). Controls: [AI-CTRL-024](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-024), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031), [AI-CTRL-001](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-001). Test with [TC-L06-032](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-032) and [TC-L16-026](../10_Test_Case_Library/L16-supply-chain-and-third-party.md#tc-l16-026).

**What breaks the chain.** Install skills only from a reviewed allow-list, and review a skill's instructions as code: a skill's text tells the agent, and the user, what to run. No skill should need a command pasted into a terminal.

### OpenClaw one-click remote code execution (CVE-2026-25253)

**What happened.** On 31 January 2026 the OpenClaw maintainers published advisory GHSA-g8p2-7wf7-98mq (CVSS 8.8): "The Control UI trusts `gatewayUrl` from the query string without validation and auto-connects on load", sending the stored gateway token to whatever server the link named. Versions up to 2026.1.28 were affected and 2026.1.29 fixed it. The advisory credits depthfirst and two finders. depthfirst showed that, with the token, an attacker could connect to the victim's gateway, switch off the approval prompt for commands and run commands on the victim's machine, all from one click on a link. Because the victim's own browser makes the connection, keeping the gateway on localhost did not protect it. Sources: [GitHub advisory](https://github.com/openclaw/openclaw/security/advisories/GHSA-g8p2-7wf7-98mq), [depthfirst write-up](https://depthfirst.com/post/1-click-rce-to-steal-your-moltbot-data-and-keys) and [The Hacker News](https://thehackernews.com/2026/02/openclaw-bug-enables-one-click-remote.html) for the CVE number.

**Maps to.** [AI-R07](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md), [AI-R22](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md) and [AI-R04](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md). Controls: [AI-CTRL-023](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-023), [AI-CTRL-027](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-027), [AI-CTRL-032](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-032), [AI-CTRL-004](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-004). Test with [TC-L06-016](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-016) and [TC-L06-025](../10_Test_Case_Library/L06-agent-orchestration-layer.md#tc-l06-025).

**What breaks the chain.** Approval settings for an agent must not be changeable with the same credential the agent's interface holds; otherwise one stolen token turns off the human check. Local agent services should check the origin of every connection, and personal agents belong in the patch inventory like any other software.

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

Add a case only when there is a primary or authoritative source: the researcher's or vendor's advisory, a CVE record, a court or regulator decision, or a report that cites one of these. Give the date, link the source, keep to what the source says, and map the case to register risks and controls. Leave out attribution of motive unless the source states it. When sources disagree, or a claim rests on one party's account, add a **Not confirmed** paragraph that says what is not settled.

## Related pages

- [Agent Architecture Patterns](../24_Builder_Track/02_Agent_Architecture_Patterns.md)
- [OWASP MCP Top 10 Crosswalk](../23_Framework_Crosswalks/19_OWASP_MCP_Top_10_Crosswalk.md)
- [OWASP Top 10 Crosswalk](../23_Framework_Crosswalks/06_OWASP_Top_10_Crosswalk.md)
- [Enterprise AI Risk Register](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md)
