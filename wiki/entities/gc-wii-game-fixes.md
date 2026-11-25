---
title: GameCube and Wii Game Fixes
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/simplysanatori__gc-wii-game-fixes.md
updated: 2026-11-25
confidence: medium
---

# GameCube and Wii Game Fixes

Curated **Dolphin-oriented catalog** of widescreen patches, cheats, graphics fixes, Riivolution mods, and HD texture packs for retail GameCube and Wii titles. Each game is described in structured **JSON entry files** keyed by six-character disc IDs; a **Python build script** validates entries and emits machine-readable catalogs for apps or installers. Entries cover **Gecko, Action Replay, and on-frame codes**, built-in Dolphin INI settings, and remote download metadata for third-party textures from GitHub, GameBanana, and other hosts **without rehosting copyrighted assets**. The project emphasizes author attribution, revision-specific codes, and emulation-focused improvements (widescreen, framerate, compatibility workarounds) for preservation-minded players and reverse engineers applying per-game patches in Dolphin—not commercial anti-cheat or live online security. (source: wiki/sources/descriptions/simplysanatori__gc-wii-game-fixes.md) (source: wiki/sources/README-categories.md)

Sits in the README **GameCube/Wii** lane (~2 entries with ioncodes/[[gecko]] GB/GBC emulator miscategorized there) and parallels simplysanatori [[3ds-game-fixes]] for structured retail fix metadata.

## Catalog model

Per-title JSON records aggregate cheat families, Dolphin game INI tweaks, Riivolution mod pointers, and texture-pack URLs; the build pipeline checks schema consistency before publishing catalogs consumable by frontends. (source: wiki/sources/descriptions/simplysanatori__gc-wii-game-fixes.md)

## Links

- Repo: https://github.com/simplysanatori/gc-wii-game-fixes

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[3ds-game-fixes]] · [[gecko]] · [[rom-weaver]]