---
title: CSGO-FindMDL
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Kruziikrel1__CSGO-FindMDL.md
updated: 2026-08-23
confidence: medium
---

# CSGO-FindMDL

**CSGO-FindMDL** (Kruziikrel1/CSGO-FindMDL) is an **internal model changer** for **Counter-Strike: Global Offensive** built around a **FindMDL hook**. Implemented as a **C++ DLL**, it bundles hook logic, **interface wrappers**, **offset handling**, and **VMT management** utilities. The repository ships **Visual Studio** project files and follows a typical **injector-driven** workflow for loading into the game process; source layout supports customizing model replacement behavior and asset paths. Primarily intended for **cheat development practice** and **game reverse-engineering research**. (source: wiki/sources/descriptions/Kruziikrel1__CSGO-FindMDL.md)

README category: Model Changer (cheat / game:csgo).

Sits in the cheat / game:csgo lane beside cosmetic-focused internals such as [[csgo-kns]] and [[aqhax-csgo]] (skin changer modules) and scaffold bases such as [[csgo-internal-base]] that teach VMT hook and interface patterns.

## Architecture notes

| Component | Role |
|-----------|------|
| FindMDL hook | Intercepts model lookup to swap player/weapon MDL paths |
| Interface wrappers | Source engine client/engine interface access |
| Offset handling | Patch-driven structure and function resolution |
| VMT utilities | Virtual-method-table hook lifecycle management |

See [[source-netvars]] for offset/interface workflows and [[csgo-cheat-base]] for comparable internal hook scaffolding.

## Links

- Repo: https://github.com/Kruziikrel1/CSGO-FindMDL

## Related

[[csgo-internal-base]] · [[csgo-cheat-base]] · [[csgo-kns]] · [[aqhax-csgo]] · [[digital-sdk]] · [[source-netvars]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
