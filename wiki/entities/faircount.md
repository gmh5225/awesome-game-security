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

Fabric server/client mod that enforces server-side mod and resource-pack whitelists by requiring clients to report loaded mods when joining multiplayer. Written in Java for Fabric Loader and Fabric API. (source: wiki/sources/descriptions/XuJun05__FairCount.md)

## Enforcement model

- **Join-time mod inventory** — clients report standalone JARs and nested jar-in-jar mods loaded in Fabric.
- **SHA-256 hash verification** — compares client mod hashes against server whitelists to detect tampered approved versions.
- **Resource-pack monitoring** — external resource packs subject to the same whitelist and hash checks as mods.
- **Fabric API auto-permit** — Fabric API modules are automatically allowed without manual whitelist entries.
- **Disconnect policy** — kicks clients missing FairCount or carrying disallowed client additions; localized kick messages and admin commands for operators.

Targets server administrators needing anti-cheat-style client integrity for competitive PvP, events, and vanilla-fair gameplay. Complements hash-tier mods such as [[seiun-ac]] and NeoForge integrity stacks such as [[katapult-anticheat]]; distinct from packet-physics AC such as [[windfall-anticheatf]] and catalog indexes such as [[minecraft-anticheat-list]].

## Links

- Repo: https://github.com/XuJun05/FairCount

## Related

[[seiun-ac]] · [[katapult-anticheat]] · [[the-dreamers-guards]] · [[crispy-wafer-anti-cheat-assistant-waferaca]] · [[minecraft-anticheat-list]] · [[grim]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
