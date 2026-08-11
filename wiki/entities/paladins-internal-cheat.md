---
title: paladins-internal-cheat
kind: entity
topics: [game-hacking, windows-kernel, graphics-api]
sources:
  - wiki/sources/descriptions/gmh5225__Paladins-internal-Cheat.md
updated: 2026-08-11
confidence: medium
---

# paladins-internal-cheat

**Paladins** internal cheat source (gmh5225) originally built as a private hack, later refactored to use **Mhyprot** (`mhyprot2.sys`) as the kernel access backend — a custom driver is optional but recommended. The overlay targets **borderless windowed** mode and does not work in fullscreen. Framed for game security researchers and reverse engineers studying in-process offensive techniques in the cheat / game:paladins lane. (source: wiki/sources/descriptions/gmh5225__Paladins-internal-Cheat.md)

Illustrates how [[byovd]] primitives from the miHoYo **`mhyprot2.sys`** family ([[mhyprot2]], [[evil-mhyprot-cli]]) can be wired into title-specific internal cheat stacks instead of a bespoke kernel driver. Complements other gmh5225 FPS internals such as [[warzone-internal-cheat]] and [[r6s-internal-cheat]] for comparing overlay and driver-backend choices across titles.

## Links

- Repo: https://github.com/gmh5225/Paladins-internal-Cheat

## Related

[[mhyprot2]] · [[evil-mhyprot-cli]] · [[byovd]] · [[warzone-internal-cheat]] · [[r6s-internal-cheat]] · [[present-hook]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]]
