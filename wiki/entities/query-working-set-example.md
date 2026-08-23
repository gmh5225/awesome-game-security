---
title: QueryWorkingSetExample
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/Midi12__QueryWorkingSetExample.md
updated: 2026-08-23
confidence: medium
---

# QueryWorkingSetExample

C demonstration of a lightweight **anti-tamper** technique based on Windows **working-set metadata**. Uses `QueryWorkingSet` APIs to inspect shared-page state in non-writable regions such as `.text`, revealing debugger **breakpoints** or **protection changes** that alter page attributes during analysis. Ships minimal build files and screenshots contrasting normal versus tampered execution. Aimed at reverse engineers and defenders studying usermode memory-integrity checks without full page-fault monitors. (source: wiki/sources/descriptions/Midi12__QueryWorkingSetExample.md)

Complements page-fault working-set AC PoCs such as [[faultline]] and offensive bypass samples such as [[count-hook]] on the cheat page-protection lane.

## Links

- Repo: https://github.com/Midi12/QueryWorkingSetExample

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[faultline]] · [[count-hook]] · [[integrity-experiments]] · [[memory-guard]]
