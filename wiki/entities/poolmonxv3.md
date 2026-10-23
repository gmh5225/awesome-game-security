---
title: PoolMonX v3
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/zodiacon__PoolMonXv3.md
  - wiki/sources/README-categories.md
updated: 2026-10-23
confidence: high
---

# PoolMonX v3

**PoolMonX v3** (zodiacon/PoolMonXv3) is a Windows desktop utility that monitors live kernel **pool allocation tags** and presents paged vs non-paged usage in a sortable list view. (source: wiki/sources/descriptions/zodiacon__PoolMonXv3.md)

## Capabilities

- Polls pool statistics via `NtQuerySystemInformation`; optional WinDbg **`pooltag.txt`** enrichment (source names and tag descriptions).
- Sortable list of paged and non-paged tag usage; quick filtering; pause/resume refresh; color-coded allocation **deltas** between updates; dark mode and toolbar controls.
- Implemented in C++ with Visual Studio, **WTL**, and **WIL** (same Windows Kernel Explorer tooling family as [[dbgprint]] and [[object-explorer]]).

## Use cases

Targets kernel debugging, driver analysis, and low-level Windows security work—e.g. spotting unusual pool consumers tied to drivers or anti-cheat components without a full WinDbg `!pool` session. Complements [[kn-diff-pool]] Big Pool snapshot diffs and [[pooldump]] interactive dumps when triaging manual-map footprints or driver leaks.

## Links

- Repo: https://github.com/zodiacon/PoolMonXv3 (README: GUI monitor for Windows kernel pool allocation tags with filtering, pause/resume, and WinDbg pooltag.txt integration)

## Related

[[kernel-pool-scanning]] · [[kn-diff-pool]] · [[pooldump]] · [[dbgprint]] · [[object-explorer]] · [[overviews/windows-kernel]] · [[research-rigor]]
