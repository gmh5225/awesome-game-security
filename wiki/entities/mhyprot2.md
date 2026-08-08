---
title: mhyprot2
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__mhyprot2.md
updated: 2026-08-08
confidence: medium
---

# mhyprot2

Research tool documenting and exploiting miHoYo **`mhyprot2.sys`** — the signed Genshin Impact anti-cheat kernel driver — as a [[byovd]] primitive. The driver's IOCTL interface exposes kernel read/write and process-termination capabilities abusable from an unprivileged user process for kernel-level operations. Aimed at BYOVD and anti-cheat researchers studying vulnerable game AC driver surfaces. (source: wiki/sources/descriptions/gmh5225__mhyprot2.md)

Complements [[mhydeath]] (same author's BYOVD exploit lane) and [[evil-mhyprot-cli]] (CLI PoC for the same driver family); contrasts with [[mhynot2]], which studies circumvention of the driver's load requirement rather than IOCTL abuse.

## Links

- Repo: https://github.com/gmh5225/mhyprot2

## Related

[[byovd]] · [[mhydeath]] · [[evil-mhyprot-cli]] · [[mhynot2]] · [[loldrivers]] · [[physmem-drivers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
