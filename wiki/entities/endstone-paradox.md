---
title: Endstone Paradox
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/TheNINJALLO__endstone-paradox.md
  - wiki/sources/README-categories.md
updated: 2026-11-03
confidence: medium
---

# Endstone Paradox

**endstone-paradox** (TheNINJALLO/endstone-paradox) is a native **C++23** anti-cheat and server administration plugin for **Minecraft Bedrock Dedicated Servers** on the **Endstone** modding platform. The loadable native library ships **54 modular checks** for combat and movement cheats, griefing, duping, packet abuse, and related Bedrock client exploits, backed by a violation engine, SQLite persistence, and staff moderation commands. The stack integrates Endstone event and packet hooks with bedrock-protocol decoding, TOML configuration, optional local web admin UI, Discord notifications, and evidence replay tooling; an older Python implementation remains in-tree for reference only. (source: wiki/sources/descriptions/TheNINJALLO__endstone-paradox.md)

Distinct from behavior-pack [[paradox-anticheat]] (Visual1mpact Script API on Realms/BDS)—this is the **Endstone native** production operator lane beside [[levi-anticheat]], [[ghost-anticheat]], and [[bedrockguard]].

## Audience

Bedrock **server operators** and **anti-cheat developers** who need production-oriented monitoring, enforcement, and operational controls on Endstone-hosted worlds—not generic reverse-engineering or client-mod tooling. (source: wiki/sources/descriptions/TheNINJALLO__endstone-paradox.md)

## Surfaces

| Component | Role |
|-----------|------|
| **Platform** | Endstone BDS native plugin (C++23) |
| **Detection** | ~54 movement/combat/grief/dup/packet modules |
| **Enforcement** | Violation engine, SQLite, staff commands |
| **Ops** | TOML config, web admin UI, Discord, replay tooling |

## Links

- Repo: https://github.com/TheNINJALLO/endstone-paradox

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[paradox-anticheat]] · [[levi-anticheat]] · [[bedrockguard]] · [[ghost-anticheat]] · [[minecraft-anticheat-list]]
