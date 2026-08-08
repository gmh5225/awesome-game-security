---
title: kur
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__kur.md
updated: 2026-08-08
confidence: medium
---

# kur

C/C++ Windows kernel utility that obtains ring-0 access through a vulnerable signed driver or custom kernel interface. README lists **`echo_driver.sys`** as the BYOVD backend; the tool exposes kernel read/write, process manipulation, and driver-loading primitives commonly used in game-security and kernel-access research. (source: wiki/sources/descriptions/gmh5225__kur.md)

Sits in the same [[byovd]] access-primitives lane as [[vdk]], [[kdu]], and [[lenovo-mapper]].

## Links

- Repo: https://github.com/gmh5225/kur

## Related

[[byovd]] · [[vdk]] · [[kdu]] · [[lenovo-mapper]] · [[loldrivers]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
