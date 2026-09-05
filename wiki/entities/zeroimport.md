---
title: ZeroImport
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/1hAck-0__zeroimport.md
  - wiki/sources/README-categories.md
updated: 2026-09-05
confidence: medium
---

# ZeroImport

C++ **Windows kernel driver library** (1hAck-0) that resolves imports at runtime instead of relying on static PE import tables. Hashes export names and walks **ntoskrnl** exports to locate functions and variables such as `MmIsAddressValid` and `PsInitialSystemProcess`. The design minimizes import-table artifacts and avoids embedding cleartext API strings in the compiled driver, with optional caching for performance. Aimed at low-level driver development and security research where stealth and resistance to static analysis matter. Listed under Anti Cheat → Lazy Importer beside [[lazy-importer]], [[kli]], [[noimportz]], and [[rs-ldr]]. (source: wiki/sources/descriptions/1hAck-0__zeroimport.md)

## Mechanism

- **Export resolve:** hash-based export-name lookup against ntoskrnl export directory (not static IAT entries).
- **Symbol coverage:** resolves both functions and exported kernel globals/variables.
- **String hygiene:** avoids cleartext API name strings in the driver image.
- **Performance:** optional resolve cache for repeated lookups.

Complements compile-time kernel lazy-import headers ([[kli]], [[kli-ex]]) and runtime zero-IAT resolver [[noimportz]] (LSTAR→ntoskrnl + `PsLoadedModuleList` walk). Defensive analysts should treat sparse driver IATs combined with ntoskrnl export-table walks and hashed export resolution as potential zero-import lazy-import usage.

## Links

- Repo: https://github.com/1hAck-0/zeroimport

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[lazy-importer]] · [[kli]] · [[kli-ex]] · [[noimportz]] · [[kernelmode-manual-mapping-through-iat]]
