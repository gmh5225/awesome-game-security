---
title: win-driver-exp
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Win-Driver-EXP.md
updated: 2026-08-09
confidence: medium
---

# win-driver-exp

Collection of **Windows driver exploits** targeting multiple vulnerable signed drivers for kernel-level access. Provides exploit code that abuses insecure IOCTL interfaces for arbitrary kernel read/write, code execution, and process manipulation. Aimed at [[byovd]] researchers and red-team operators cataloging exploitable Windows kernel drivers. (source: wiki/sources/descriptions/gmh5225__Win-Driver-EXP.md)

README-indexed sample: **`AsUpIO64.sys`** (CVE-2024-33218) — overlaps the ASUS **`AsUpIO.sys`** / **`AsUpIO64.sys`** LOLdriver lane studied by [[imxyvimapper]].

## Links

- Repo: https://github.com/gmh5225/Win-Driver-EXP
- CVE-2024-33218 / `AsUpIO64.sys`: https://github.com/gmh5225/Win-Driver-EXP/tree/main/CVE-2024-33218

## Related

[[byovd]] · [[imxyvimapper]] · [[vdk]] · [[windows-kernel-exploits]] · [[loldrivers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
