---
title: PointerGuard
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/charliewolfe__PointerGuard.md
updated: 2026-08-17
confidence: medium
---

# PointerGuard

Windows proof-of-concept for protecting **function pointers** and **vtable entries** against runtime tampering. Monitors critical pointer locations with **hardware breakpoints (HWBP)** or **`PAGE_GUARD`** / **VEH** page-protection mechanisms, detecting when cheats or exploits attempt to redirect execution by overwriting pointers. C/C++ sample aimed at anti-cheat developers and security researchers studying pointer-integrity protection. (source: wiki/sources/descriptions/charliewolfe__PointerGuard.md)

README tag: **VEH + PAGE_GUARD**. Complements broader page-guard libraries such as [[memory-guard]], EAT-focused monitoring such as [[eat-guard]], and offensive Page Guard hook samples such as [[pghooker]].

## Links

- Repo: https://github.com/charliewolfe/PointerGuard

## Related

[[memory-guard]] · [[eat-guard]] · [[pghooker]] · [[veh-printf-hook]] · [[integrity-experiments]] · [[voidmaw]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
