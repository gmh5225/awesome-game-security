---
title: vanguardtrace
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/armvirus__VanguardTrace.md
updated: 2026-08-18
confidence: medium
---

# vanguardtrace

**Vanguard encrypted-import research tool** (armvirus). Windows kernel research project for analyzing and intercepting **encrypted imports** in Vanguard's kernel driver (`vgk.sys`): signature-scan to locate the encrypted import table, decrypt target entries, and re-encrypt pointers when patching hooks. Sample hook flow tracks calls such as `CiCheckSignedFile` and recovers import offsets from `vgk.sys`. README tag: `[Decrypting and intercepting encrypted imports of Vanguards Kernel Driver]`. Intended for reverse engineering and anti-cheat internals research, not general application development. (source: wiki/sources/descriptions/armvirus__VanguardTrace.md)

Sits beside [[vanguard-import-resolver]] and [[augur-riot]] in the Vanguard kernel RE lane, but focused on **runtime decrypt → hook → re-encrypt** of the driver's encrypted import table rather than static protected-import address resolution or streamed-module PE reconstruction. Complements [[vgk-illegal-pf-logger]] and [[val-exception-handler]] for studying which kernel APIs Vanguard invokes under [[vanguard]].

## Links

- Repo: https://github.com/armvirus/VanguardTrace

## Related

[[vanguard]] · [[vanguard-import-resolver]] · [[augur-riot]] · [[vgk-illegal-pf-logger]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
