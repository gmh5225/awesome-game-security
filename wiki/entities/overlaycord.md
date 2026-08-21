---
title: OverlayCord
kind: entity
topics: [graphics-api, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/SamuelTulach__OverlayCord.md
updated: 2026-08-21
confidence: medium
---

# OverlayCord

**OverlayCord** (SamuelTulach) is a C++ **proof-of-concept** that hijacks Discord's internal **game overlay pipeline** from an **external process**. It demonstrates **framebuffer-sharing abuse** to render through Discord's trusted overlay path without modifying Discord files, injecting Discord modules, or installing API hooks. The sample ships reusable overlay code plus example integration for drawing via that pipeline. Primary use is **game security and anti-cheat research** on overlay trust boundaries and detection blind spots. README category: cheat / [Discord]. (source: wiki/sources/descriptions/SamuelTulach__OverlayCord.md)

Contrasts with hook-based Discord overlay samples such as [[discord-overlay-hook]] (in-process DX11 hooking) by staying fully external and hook-free while still reusing Discord's composited overlay surface.

## Links

- Repo: https://github.com/SamuelTulach/OverlayCord

## Related

[[discord-overlay-hook]] · [[steam-overlay-x64]] · [[nvidia-overlay-hijack]] · [[window-hijack-overlay]] · [[overviews/graphics-api]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
