---
title: NoScreen
kind: entity
topics: [windows-kernel, graphics-api, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/KANKOSHEV__NoScreen.md
updated: 2026-08-24
confidence: medium
---

# NoScreen

**Kernel-assisted window protection** tool intended to **prevent screen capture** (KANKOSHEV). Provides behavior similar to **display affinity** protection (`SetWindowDisplayAffinity` / `WDA_EXCLUDEFROMCAPTURE`) while trying to reduce straightforward **user-mode detection vectors**. Uses a **custom kernel driver** and **device interface** so protection can be applied without modifying target process memory directly. Primary contexts: privacy, anti-capture, and game anti-cheat research—not a maintained commercial product. (source: wiki/sources/descriptions/KANKOSHEV__NoScreen.md)

README lane: Hide Window.

## Links

- Repo: https://github.com/KANKOSHEV/NoScreen

## Related

[[wda-monitor-trick]] · [[disablenvidiascreenshot]] · [[anti-screenshot-capture]] · [[face-injector-v2]] · [[overviews/graphics-api]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
