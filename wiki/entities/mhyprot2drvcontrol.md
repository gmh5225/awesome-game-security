---
title: mhyprot2drvcontrol
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Mhyprot2DrvControl.md
updated: 2026-08-11
confidence: medium
---

# mhyprot2drvcontrol

C++ **control library** for miHoYo **`mhyprot2.sys`** — the signed Genshin Impact anti-cheat kernel driver — that wraps its vulnerable IOCTL interface into a convenient user-mode API. Exposes process memory read/write, module enumeration, and process termination through a reusable class interface for [[byovd]] researchers building on `mhyprot2` as a kernel access primitive. (source: wiki/sources/descriptions/gmh5225__Mhyprot2DrvControl.md)

Complements [[mhyprot2]] (same driver's IOCTL documentation/exploit lane), [[evil-mhyprot-cli]] (CLI service front end), and [[mhydeath]] (alternate BYOVD PoC). Downstream integrations such as [[paladins-internal-cheat]] optionally wire the same **Mhyprot** backend into title-internal cheat stacks instead of a bespoke kernel driver.

## Links

- Repo: https://github.com/gmh5225/Mhyprot2DrvControl

## Related

[[byovd]] · [[mhyprot2]] · [[mhydeath]] · [[evil-mhyprot-cli]] · [[paladins-internal-cheat]] · [[loldrivers]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
