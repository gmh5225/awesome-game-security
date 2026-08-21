---
title: raybot-zero
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/R4YVEN__raybot-zero.md
updated: 2026-08-21
confidence: medium
---

# raybot-zero

**Kernel-mode CS:GO cheat** that runs core logic **without a traditional user-mode controller**. Combines a **C++ Windows driver** with a small **C# loader** and implements triggerbot, bunnyhop, glow visuals, and **kernel-level key-state reading**. Uses game offsets and low-level memory routines to interact with player entities and engine data. Targets cheat development research and kernel anti-cheat evasion experimentation. (source: wiki/sources/descriptions/R4YVEN__raybot-zero.md)

Sits beside other full-kernel or driver-centric CS:GO samples such as [[csgo-full-kernel]] (KMDF; memory, draw, input in Ring0), [[kernel-csgo]] (hook-based KM↔UM comm), and [[garhal-csgo]] (IOCTL usermode controller + planned kernel overlay).

## Links

- Repo: https://github.com/R4YVEN/raybot-zero

## Related

[[csgo-full-kernel]] · [[kernel-csgo]] · [[garhal-csgo]] · [[ec]] · [[csgo-cheat-external]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
