---
title: PACC (Professional Anti-Cheat Client)
kind: entity
topics: [anti-cheat, game-hacking, mobile-security]
sources:
  - wiki/sources/descriptions/EPOTATOTV__PACC4_0.md
updated: 2026-09-12
confidence: medium
---

# PACC (Professional Anti-Cheat Client)

**PACC** is a player-side anti-cheat platform for Minecraft **Bedrock** and **Java** editions that combines on-device detection with a separate **PTV** control and administration backend. It inspects local signals such as memory tampering, running processes and modules, and input or USB/HID devices, then logs findings, triggers full-screen red-screen warnings, and supports remote admin inspection and evidence collection without integrating game-server ban systems. (source: wiki/sources/descriptions/EPOTATOTV__PACC4_0.md)

## Detection and enforcement model

- **On-device signals** — memory tampering, process/module enumeration, USB/HID input-device inspection.
- **Behavioral scoring** — Python AI scoring layer for cheat-pattern analysis.
- **Operator response** — encrypted event logging, full-screen red-screen warnings, remote admin review and forensic evidence collection.
- **Isolated backend** — PTV admin stack is separate from game servers; no built-in server ban integration.

## Stack and platforms

- **Services** — Java and Spring Boot backend; React and TypeScript admin frontend.
- **Event pipeline** — Rust pipeline with cryptographic signing and encrypted persistence.
- **Native probes** — kernel or agent modules on **Windows**, **Linux**, **Android**, **iOS**, and **HarmonyOS**.

Targets Minecraft communities and operators who want client-resident cheat deterrence, behavioral analysis, and forensic auditing while keeping management infrastructure isolated from game servers. Complements server-side physics AC such as [[grim]], Forge peer-mod visibility such as [[crispy-wafer-anti-cheat-assistant-waferaca]], and QA clients such as [[anticheat-qa]].

## Links

- Repo: https://github.com/EPOTATOTV/PACC4_0

## Related

[[crispy-wafer-anti-cheat-assistant-waferaca]] · [[katapult-anticheat]] · [[local-anticheat-1-8-9]] · [[anticheat-qa]] · [[grim]] · [[minecraft-anticheat-list]] · [[ai-aimbot-detection]] · [[input-provenance]] · [[mobile-anti-cheat]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
