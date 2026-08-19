---
title: MemoryGuard
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__MemoryGuard.md
updated: 2026-08-11
confidence: medium
---

# MemoryGuard

Windows memory-protection library from gmh5225 that detects and prevents unauthorized in-process memory modifications. Monitors critical regions with **`PAGE_GUARD`**, **VEH** handlers, or periodic integrity checks; can alert or revert tampering from cheats or debuggers. README tag: **VEH + PAGE_GUARD**; aimed at anti-cheat developers and software-protection engineers implementing runtime memory-integrity monitoring (`Anti Cheat` → Page Protection / `Detection:Memory Integrity`). (source: wiki/sources/descriptions/gmh5225__MemoryGuard.md)

Complements header-only experiment corpora such as [[integrity-experiments]], PE section checksum library [[integrity]] (afulsamet; periodic non-writable section hash re-check), pointer/vtable integrity PoCs such as [[pointer-guard]], VEH + page-protection samples such as [[voidmaw]] and [[no-access-protection]], and Byfron-style PoCs such as [[page-no-access-not-byfron]].

## Links

- Repo: https://github.com/gmh5225/MemoryGuard

## Related

[[integrity-experiments]] · [[integrity]] · [[pointer-guard]] · [[voidmaw]] · [[no-access-protection]] · [[page-no-access-not-byfron]] · [[veh-hide-memory]] · [[pghooker]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
