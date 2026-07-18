---
title: KernelResearchKit
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/wesmar__KernelResearchKit.md
updated: 2026-07-18
confidence: medium
---

# KernelResearchKit

Windows 11 kernel research framework bundling boot-time DSE bypass, CI patching, and unsigned-driver load paths (manual map, IRP hijack, [[byovd]]). On 25H2 it surgically patches `SeCiCallbacks` via the native subsystem, with anti-loop protection and a dual-path architecture for early-phase unsigned-driver research. (source: wiki/sources/descriptions/wesmar__KernelResearchKit.md)

Same-author lane as [[kvc]] (`g_CiOptions` / `SeCiCallbacks` loaders): here the focus is a broader toolkit (boot bypass + multiple map methods) rather than a single DSE/PP controller.

## Links

- Repo: https://github.com/wesmar/KernelResearchKit

## Related

[[kvc]] · [[byovd]] · [[lsass-extend-mapper]] · [[hvci]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
