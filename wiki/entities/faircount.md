---
title: FairCount
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/XuJun05__FairCount.md
  - wiki/sources/README-categories.md
updated: 2026-09-13
confidence: medium
---

# FairCount

Fabric server/client mod that enforces server-side mod and resource-pack whitelists by requiring clients to report loaded mods when joining multiplayer. Written in Java for Fabric Loader and Fabric API; inventories standalone JARs and nested jar-in-jar mods, verifies SHA-256 hashes to detect tampered approved versions, and disconnects players who lack FairCount or carry disallowed client additions. Also monitors external resource packs with whitelist and hash checks, auto-permits Fabric API modules, and exposes admin commands with localized kick messages. (source: wiki/sources/descriptions/XuJun05__FairCount.md)

Targets server administrators needing anti-cheat-style client integrity for competitive PvP, events, and vanilla-fair gameplay. Complements hash-tier mods such as [[seiun-ac]] and NeoForge integrity stacks such as [[katapult-anticheat]]; distinct from packet-physics AC such as [[windfall-anticheatf]] and catalog indexes such as [[minecraft-anticheat-list]].

## Links

- Repo: https://github.com/XuJun05/FairCount

## Related

[[seiun-ac]] · [[katapult-anticheat]] · [[the-dreamers-guards]] · [[crispy-wafer-anti-cheat-assistant-waferaca]] · [[minecraft-anticheat-list]] · [[grim]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
