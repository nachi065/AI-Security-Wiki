---
title: "10. AI for Security and AI-Enabled Threats"
description: "AI for security and AI-enabled threats: SOC copilots as AI systems needing protection, and how AI changes phishing, reconnaissance and exploit timelines."
author: Nachiket Sathaye
parent: "Foundations"
nav_order: 10
document_type: Practitioner Research Paper
---

# 10. AI for Security and AI-Enabled Threats

The other two meanings of "AI security" from [Page 1](01-Terminology-and-Two-Axis-Model.md) are covered here.

## 10.1 AI for security (defensive use)

Common uses: SOC alert triage and summarisation, threat-intelligence synthesis, detection-rule drafting, malware and script analysis, vulnerability triage, code review, phishing analysis, incident reporting.

**The central point of this paper applies directly: a security tool built on AI is itself an AI system.** A SOC copilot ingests untrusted data (logs, emails, malware strings, ticket text), holds privileged access (EDR actions, ticket systems, identity platforms) and produces output analysts may trust. It therefore has the same exposure as any agent: injected instructions in a log line, over-privileged integrations, wrong output acted on. [Analysis]

| Use | Benefit | Specific risk | Control |
|---|---|---|---|
| Alert triage | Faster prioritisation | Missed true positives; attacker-crafted content steering the summary | Sample audits; keep the original evidence one click away |
| Detection engineering | Faster rule drafting | Plausible but wrong logic | Test against known-good and known-bad data before deployment |
| Automated response | Speed | Wrong or injected action | Bounded actions, reversibility, approval for disruptive steps |
| Threat-intel summarisation | Reduced reading load | Fabricated attribution or indicators | Require source links; verify indicators |
| Code and vulnerability analysis | Coverage | False confidence | Human review; independent scanners |

**Operating rules.** Human oversight proportional to impact; bounded autonomy; validation against ground truth; full audit logs; and the AI-for-security system itself in scope for the controls in Pages 2–9.

## 10.2 AI-enabled threats against conventional security

AI lowers the cost of several attacker activities. The OWASP Q1 2026 Round-up reports that attackers have used AI tooling for automated reconnaissance and exploit development, compressing timelines and increasing scale [13] **[Reported]**. Areas defenders should plan for: [Analysis]

| Area | Change | Defender response |
|---|---|---|
| **Phishing and social engineering** | Fluent, personalised, multilingual content at low cost; voice and video impersonation | Strong authentication that does not depend on recognising a message; out-of-band verification for payments and credential changes; training that does not rely on spotting poor grammar |
| **Reconnaissance** | Faster synthesis of public information about targets | Reduce exposed information; monitor for enumeration |
| **Exploit and malware development** | Assistance in understanding and adapting known techniques | Faster patching of exposed systems; behaviour-based detection; defence in depth |
| **Scale and persistence** | More attempts, more variants | Rate limits, anomaly detection, automation on the defence side |

**This paper does not provide offensive techniques.** The defensive conclusion is that AI does not change the fundamentals (patching, identity, segmentation, logging, backup, tested response), but it shrinks the time defenders have to apply them. Foundational controls remain necessary and should be treated as a first priority, not replaced by AI-specific ones.
