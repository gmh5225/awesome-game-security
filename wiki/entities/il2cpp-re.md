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

Frida-based **iOS** tool that extracts a **deobfuscated IL2CPP global-metadata header** from a running Unity app on jailbroken devices, producing output suitable for [[il2cppdumper]] and similar reverse-engineering workflows. A Python controller spawns the target by bundle ID and injects JavaScript agents that hook `il2cpp_init` inside UnityFramework to capture the clean header after runtime deobfuscation (verified by `0xFAB11BAF` magic). The default v4 agent tries offset-based hooks when provided and falls back to Stalker-driven register scanning when offsets are stale. (source: wiki/sources/descriptions/ndhn27__il2cpp-re.md)

Listed in the README under **Cheat → Frida** / Unity IL2CPP metadata lanes beside static dumpers and mobile Frida bridges.

## Links

- Repo: https://github.com/ndhn27/il2cpp-re

## Related

[[il2cpp]] · [[il2cppdumper]] · [[frida]] · [[bagbak]] · [[frida-il2cpp-bridge]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]
