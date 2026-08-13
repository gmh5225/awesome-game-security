---
title: fortnite-external
kind: entity
topics: [game-hacking, windows-kernel, game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/gmh5225__Fortnite-External.md
updated: 2026-08-13
confidence: medium
---

# fortnite-external

External Fortnite cheat sample (gmh5225; cheat / game:fortnite [External]). Out-of-process architecture depends on a **custom kernel driver** for cross-process memory access. Includes DirectX 9 rendering setup, game offset definitions, and utility functions for reading Unreal Engine data structures externally—useful for studying driver-backed external cheat stacks, UE offset workflows, and legacy D3D9 overlay paths on EAC-protected Fortnite clients. (source: wiki/sources/descriptions/gmh5225__Fortnite-External.md)

Sits beside other external Fortnite samples such as [[fortnite-ud-external]], [[fortnite-external-base-source]], [[fortnite-external-evo-gj]], [[fortnite-voyagertf]], and [[volto-external-spowar-ud-eac-be-fortnite-external-cheat]].

## Links

- Repo: https://github.com/gmh5225/Fortnite-External-Cheat-WinSense-Leak

## Related

[[easy-anti-cheat]] · [[unreal-object-model]] · [[world-to-screen]] · [[present-hook]] · [[fortnite-offsets]] · [[fortnite-ud-external]] · [[fortnite-external-base-source]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]]
