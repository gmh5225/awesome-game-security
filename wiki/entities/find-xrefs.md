---
title: FindXrefs
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/TheCruZ__FindXrefs.md
updated: 2026-08-20
confidence: medium
---

# FindXrefs

IDA Pro plugin (Python IDAPython) that finds and **materializes cross-references** IDA has not yet created on large binaries—fixing cases where Jump to xref reports no references even though they exist. Scans the full database for RIP-relative and absolute pointer references on x86/x64, with an optional raw relative 32-bit sliding-window mode for non-standard or obfuscated offsets. For each match on undefined bytes, it creates instructions or data offsets so IDA generates the xref automatically. Optional NumPy acceleration speeds byte sweeps roughly fivefold, with regex and loop fallbacks when NumPy is unavailable. (source: wiki/sources/descriptions/TheCruZ__FindXrefs.md)

Aimed at reverse engineers analyzing large game clients, anti-cheat modules, and other binaries where incomplete auto-analysis leaves strings and globals without visible xrefs. Cheat / IDA Plugins lane.

## Links

- Repo: https://github.com/TheCruZ/FindXrefs

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[xrefsext]] · [[ida-find-.data-ptr]] · [[findfunc]] · [[ida-plugins]]
