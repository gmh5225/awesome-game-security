---
title: irql
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/naorhaziz__irql.md
updated: 2026-07-28
confidence: medium
---

# irql

Rust workspace for **compile-time IRQL safety** in Windows kernel drivers: core IRQL abstractions plus `irql_alloc` pool-backed `Box`/`Vec` and related helpers so KM Rust code allocates and uses data structures only at legal IRQL levels. Useful for kernel developers and game-security researchers writing Ring0 drivers in Rust without classic NonPaged/Paged pool IRQL bugs. (source: wiki/sources/descriptions/naorhaziz__irql.md)

## Links

- Repo: https://github.com/naorhaziz/irql

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[document]] · [[wdutf]] · [[ksocket]]
