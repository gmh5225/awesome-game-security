---
title: il2cpp-re
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/ndhn27__il2cpp-re.md
updated: 2026-09-16
confidence: medium
---

# il2cpp-re

Frida-based **iOS** tool that extracts a **deobfuscated IL2CPP global-metadata header** from a running Unity app on jailbroken devices, producing output suitable for [[il2cppdumper]] and similar reverse-engineering workflows. A Python controller spawns the target by bundle ID and injects JavaScript Frida agents that hook `il2cpp_init` inside UnityFramework to capture the clean header after runtime deobfuscation, verified by the standard `0xFAB11BAF` magic. (source: wiki/sources/descriptions/ndhn27__il2cpp-re.md)

## How it works

- **Controller:** Python spawns the app by bundle ID and loads Frida JavaScript agents.
- **Hook point:** `il2cpp_init` in UnityFramework — metadata is captured after runtime deobfuscation, not from obfuscated on-disk blobs.
- **v4 (default):** Adaptive offset-based hook when an offset is provided; automatic fallback to Stalker-driven dynamic register scan when the offset is missing or stale.
- **Legacy agents:** v2 (scan-only) and v3 (offset-only) for older or specialized workflows.
- **Scope:** Read-only header extraction — does not modify application state. Aimed at researchers analyzing IL2CPP internals and metadata layout on iOS games and apps they are authorized to test.

Listed in the README under **Cheat → Frida** / Unity IL2CPP metadata lanes beside static dumpers and mobile Frida bridges such as [[frida-il2cpp-bridge]].

## Links

- Repo: https://github.com/ndhn27/il2cpp-re

## Related

[[il2cpp]] · [[il2cppdumper]] · [[frida]] · [[bagbak]] · [[frida-il2cpp-bridge]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]
