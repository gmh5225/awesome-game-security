---
title: xigmapper
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/xtremegamer1__xigmapper.md
updated: 2026-07-17
confidence: medium
---

# xigmapper

EFI manual-map research project for loading an unsigned driver payload during the UEFI/boot path, before normal Windows driver discovery. Aimed at game-security / RE study of cheat ↔ EFI driver techniques rather than production use. (source: wiki/sources/descriptions/xtremegamer1__xigmapper.md)

Constraint called out for [[vanguard]] research: the driver image must **not** live on USB — Windows discovers USB devices after Vanguard’s early load, so a USB-hosted payload arrives too late relative to boot-start AC visibility. (source: wiki/sources/descriptions/xtremegamer1__xigmapper.md)

## Links

- Repo: https://github.com/xtremegamer1/xigmapper

## Related

[[vanguard]] · [[lsass-extend-mapper]] · [[revert-mapper]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
