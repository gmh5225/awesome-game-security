---
title: vanguard-import-resolver
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__VanguardImportResolver.md
updated: 2026-08-09
confidence: medium
---

# vanguard-import-resolver

**Vanguard kernel import resolver** (gmh5225). Resolves **protected import function addresses** used internally by Riot Vanguard's kernel driver (`vgk.sys`): documents the driver's import-resolution mechanism and provides utilities to analyze which kernel functions Vanguard calls. README tag: `[Resolve vgk's protected imports]`. Aimed at anti-cheat researchers reverse engineering Vanguard kernel-driver internals and import protection. (source: wiki/sources/descriptions/gmh5225__VanguardImportResolver.md)

Sits beside [[augur-riot]] in the Vanguard kernel RE lane, but as **runtime/offline import address resolution** for protected `vgk` imports rather than RITO streamed-module → PE reconstruction. Complements [[vgk-illegal-pf-logger]] and [[val-exception-handler]] for static analysis of Vanguard's kernel surface under [[vanguard]].

## Links

- Repo: https://github.com/gmh5225/VanguardImportResolver

## Related

[[vanguard]] · [[augur-riot]] · [[vgk-illegal-pf-logger]] · [[val-exception-handler]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
