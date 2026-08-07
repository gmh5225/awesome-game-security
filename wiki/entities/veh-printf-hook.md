---
title: veh-printf-hook
kind: entity
topics: [reverse-engineering, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__veh-printf-hook.md
updated: 2026-08-07
confidence: medium
---

# veh-printf-hook

Demonstration of **VEH + `PAGE_GUARD`** to hook `printf` and similar output functions without patching target bytes. Sets page guards on the function memory, catches the resulting exception in a Vectored Exception Handler, and redirects execution to custom logging or filtering code—a non-invasive interception technique for security researchers studying VEH-based function hooks. (source: wiki/sources/descriptions/gmh5225__veh-printf-hook.md)

Pairs with related `PAGE_GUARD` / VEH hook samples such as [[pghooker]] (general Page Guard hook research), [[voidmaw]] (code-hiding), and [[cpp-veh-dbi]] (VEH-based lightweight DBI).

## Links

- Repo: https://github.com/gmh5225/veh-printf-hook (README tag: VEH + PAGE_GUARD)

## Related

[[pghooker]] · [[voidmaw]] · [[cpp-veh-dbi]] · [[veh-hide-memory]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
