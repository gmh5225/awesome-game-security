---
title: hayday-bot
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/AshrafMorningstar__hayday-bot.md
updated: 2026-09-10
confidence: medium
---

# hayday-bot

**hayday-bot** (AshrafMorningstar) — in-memory automation suite for the **Hay Day** mobile game that harvests, replants, and sells crops by calling internal game functions instead of screen capture or click macros. (source: wiki/sources/descriptions/AshrafMorningstar__hayday-bot.md)

## Architecture

- **Python** — deployment and control orchestration
- **Frida JavaScript** — runtime hooks on guest ARM64 `libg.so` under LDPlayer 9 / Houdini translation
- **TypeScript** — anti-telemetry modules blocking behavioral AC reporting
- **Native C++** — in-process memory manipulation engine

## Anti-tamper and evasion

- **Promon SHIELD** — bypass via patched Frida gadget injection
- **Quago** — behavioral anti-cheat telemetry blocked at runtime
- **Emulator/root hide** — runtime hooks plus device fingerprint spoofing to mask LDPlayer and root artifacts

## Reverse-engineering utilities

Ships helpers for analyzing `libg.so`, patching gadgets, and probing JNI and native method registration—aimed at researchers studying mobile game automation, anti-cheat evasion, and dynamic instrumentation of protected **Supercell** titles.

## Links

- Repo: https://github.com/AshrafMorningstar/hayday-bot [Frida-based Hay Day automation with guest ARM64 libg.so hooking on LDPlayer/Houdini and Promon SHIELD/Quago anti-cheat bypass]

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[frida]] · [[mobile-anti-cheat]] · [[frida-find-jni-native-methods]] · [[root-detection-low-level]] · [[research-rigor]]
