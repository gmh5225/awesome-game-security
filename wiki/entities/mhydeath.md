---
title: mhydeath
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__mhydeath.md
updated: 2026-08-08
confidence: medium
---

# mhydeath

BYOVD research tool that exploits miHoYo **`mhyprot2.sys`** — the signed Genshin Impact anti-cheat kernel driver — for arbitrary kernel operations. Vulnerabilities in the driver's IOCTL interface let unprivileged user processes read/write kernel memory and terminate processes, yielding system-level access via a game AC driver surface. Aimed at BYOVD researchers studying weaponized anti-cheat driver flaws. (source: wiki/sources/descriptions/gmh5225__mhydeath.md)

Complements [[mhyprot2]] (same author's IOCTL documentation/exploit lane) and [[evil-mhyprot-cli]] (CLI PoC for the same driver family); contrasts with [[mhynot2]], which studies circumvention of the driver's load requirement rather than IOCTL abuse.

## Links

- Repo: https://github.com/gmh5225/mhydeath

## Related

[[byovd]] · [[mhyprot2]] · [[evil-mhyprot-cli]] · [[mhynot2]] · [[loldrivers]] · [[physmem-drivers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
