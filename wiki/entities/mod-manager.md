---
title: mod-manager
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/B6sse__modManager.md
updated: 2026-10-19
confidence: medium
---

# mod-manager

**Axon** (Basses Mod Manager; B6sse/modManager) is a Windows desktop mod manager for **Star Wars Battlefront (2015)**. Players pick from a **fixed, pre-installed** set of **SHA-256–verified, community-approved** mods; the manager writes **launch metadata** and starts the game so bundled **Auric** (loader DLL beside the executable) applies **Frosty-style `.fbmod`** packages **in memory at startup**—no on-disk game patches. Stack: **C# WPF** on **.NET Framework 4.8**, **Inno Setup** installer with bundled prerequisites. The UI deliberately omits custom import/removal so competitive or private-server organizers can enforce mod integrity; repo docs cover the memory-loading pipeline and **CI** gates that ship only public Auric builds—useful for studying **controlled client-side mod injection** and fair-play mod tooling. (source: wiki/sources/descriptions/B6sse__modManager.md)

## Links

- Repo: https://github.com/B6sse/modManager

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[rearguard]] · [[rce-shield]] · [[dot-server-security]] · [[research-rigor]]
