---
title: mf_antiesp
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/MitologicoDev__mf_antiesp.md
  - wiki/sources/README-categories.md
updated: 2026-10-25
confidence: high
---

# mf_antiesp

**FiveM AntiESP** (MitologicoDev/mf_antiesp) is a free, standalone **client-side** CitizenFX resource for GTA V FiveM that mitigates wallhack-style ESP by hiding other players from the local client when they are occluded behind geometry, so cheat overlays cannot draw enemy models through walls until those players would legitimately be visible again. (source: wiki/sources/descriptions/MitologicoDev__mf_antiesp.md)

README category: Anti Cheat / Detection:ESP.

## Mechanism

The resource periodically scans on-screen player peds and uses native occlusion checks such as **`IsEntityOccluded`** and **`WouldEntityBeOccluded`**, then applies **`NetworkConcealPlayer`** so concealed players are not available to ESP overlays while occluded. (source: wiki/sources/descriptions/MitologicoDev__mf_antiesp.md)

## Stack and deployment

Implemented in **Lua** with a standard **fxmanifest**; requires **no framework** and no server-side configuration—operators drop the resource into the server bundle as a client resource. Scan and reveal intervals are tunable via **`config.lua`** for performance versus responsiveness trade-offs. (source: wiki/sources/descriptions/MitologicoDev__mf_antiesp.md)

## Positioning

Targets **server operators** and anti-cheat workflows on roleplay or multiplayer hosts. It is **client-only** and meant to **complement** full anticheat (e.g. server-side Lua such as [[dead-anticheat]]) rather than replace kernel or server enforcement; test carefully because concealment can conflict with other scripts that manage player visibility, instances, or routing buckets. (source: wiki/sources/descriptions/MitologicoDev__mf_antiesp.md)

## Links

- Repo: https://github.com/MitologicoDev/mf_antiesp

## Related

[[dead-anticheat]] · [[esp-killer]] · [[petal-anti-freecam]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
