---
title: be-injector
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/Compiled-Code__be-injector.md
updated: 2026-08-27
confidence: medium
---

# be-injector

**be-injector** (Compiled-Code/be-injector) is a Windows **injection proof of concept** in C++ that **patches signed module code through physical memory mapping** to avoid **copy-on-write (COW) artifacts**. The design modifies pages before normal module mapping behavior diverges, aiming to evade common anti-cheat integrity assumptions around loaded modules — including **thread monitoring**, **API-call scrutiny**, and **signature-based scans**. Primary use case: low-level **anti-cheat bypass** and **detection-resilience** research, not a maintained product. README category: cheat / Attack COW. (source: wiki/sources/descriptions/Compiled-Code__be-injector.md)

Sits in the **physical-memory / COW-evasion injection** lane beside kernel-assisted mappers such as [[kernel-eac-be-injector]] and page-table manipulation injectors such as [[page-table-injector]], but focuses on pre-mapping physical patches to signed modules rather than manual-map DLL staging alone.

## Links

- Repo: https://github.com/Compiled-Code/be-injector

## Related

[[eac-mapper]] · [[kernel-eac-be-injector]] · [[page-table-injector]] · [[ntmemory]] · [[easy-anti-cheat]] · [[battleye]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
