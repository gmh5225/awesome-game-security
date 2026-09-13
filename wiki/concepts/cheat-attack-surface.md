---
title: Cheat Attack Surface
kind: concept
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/skills/game-hacking.md
updated: 2026-09-13
confidence: high
---

# Cheat Attack Surface

Analytical taxonomy of **what an attacker observes or controls**, the **required capability**, the **trust boundary crossed**, and where defenders have **evidence or authority**. Capabilities combine freely—they do not form a mandatory escalation ladder. (source: wiki/sources/skills/game-hacking.md)

## Threat families

| Family and goal | Necessary capability or failed boundary | Defender observations and controls | Counterexample or coverage limit |
|---|---|---|---|
| Client-state observation | Access to relevant client-resident data | Minimize unnecessary replication; correlate host and process evidence | Read-only access can affect fairness without changing memory |
| State manipulation | Modify local/submitted state plus insufficient authoritative validation | Validate consequential actions and state transitions on the server | Prediction, rollback, latency, and game bugs can resemble anomalies |
| Process injection or unauthorized code modification | Path enabling foreign code or modification in the process | Module/code provenance, integrity findings, source of execution | Legitimate instrumentation and plugins can produce similar artifacts |
| Privileged driver/interface abuse | Reachable privileged interface and permissions or a flaw exposing sensitive operations | Driver inventory, interface authorization, input validation, active policy | Signature validity does not establish safe functionality |
| Hardware DMA observation or modification | DMA-capable requester and accessible mappings | Device isolation, mapping policy, platform evidence | Control scope depends on topology, driver, firmware, and OS state |
| Host-mediated remote acquisition | Host acquisition access plus a transport path | Acquisition component provenance and appropriate host/device evidence | Remote analysis does not turn CPU/kernel acquisition into hardware DMA |
| Graphics modification or overlay abuse | Access to rendering state or a composition surface | Distinguish application, presentation, compositor, and capture evidence | Recording tools and accessibility overlays are legitimate controls |
| Visual automation | Available frames and a decision mechanism | Evaluate gameplay behavior and any available capture context | Need not create a game-memory access artifact |
| Input automation | Input-producing path accepted by the application | Correlate device context, [[input-provenance]], and longitudinal behavior | Accessibility tools, remappers, and device sharing are benign alternatives |
| Protocol or business-rule abuse | Server accepts untrusted requests or client assertions beyond intended authority | Validate authorization, state, ordering, and replay-sensitive actions | Retries and reordering are normal and require protocol-aware interpretation |

Primary-source review: 2026-09-09. Named README tools are **versioned threat-model examples**, not guarantees that every game exposes each surface or that a tool implements it. (source: wiki/sources/skills/game-hacking.md)

## Documented boundaries

In server-authoritative designs, authoritative server state, replicated client state, prediction, and presentation are distinct—investigate who validates each consequential action; do not assume a local change affects authoritative state. Raw Input can distinguish source devices of the same type but is not authentication of human intent; `SendInput` has documented integrity-level restrictions. Driver threat models must include interface access control and what privileged operations an interface exposes—a trusted signature cannot substitute for authorization or correct validation.

Cross-route: [[memory-acquisition-path]] for acquisition/transport, [[overviews/graphics-api]] for rendering observations, [[overviews/game-engine]] for engine authority, [[network-environment-evidence]] for restriction evidence, [[research-rigor]] for validity of implementation or detection claims.

## Write a useful attack description

For a selected family, explain the **objective**, **prerequisite capability**, **exposed resource**, **trust boundary**, **possible effect**, and **available evidence**. Then state which control prevents the behavior, which observation only detects a symptom, which legitimate uses resemble it, and what current evidence cannot settle. Identify the source and version supporting each concrete assertion.

Do not substitute tool names or invisibility claims for a mechanism. A clean module list does not prove a clean host; an ordinary-looking HID report does not prove human origin; a suspicious artifact does not by itself prove cheating. Detector effectiveness requires representative evaluation, not merely that one synthetic sample triggers a rule.

## Related

[[memory-acquisition-path]] · [[input-provenance]] · [[driver-communication]] · [[world-to-screen]] · [[hardware-input-injection]] · [[research-rigor]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
