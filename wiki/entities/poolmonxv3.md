---
title: PoolMonX v3
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/zodiacon__PoolMonXv3.md
  - wiki/sources/README-categories.md
updated: 2026-10-23
confidence: medium
---

# PoolMonX v3

**PoolMonX v3** (zodiacon/PoolMonXv3) is a Windows desktop utility that monitors live kernel **pool allocation tags** and presents paged vs non-paged usage in a sortable list view. Data comes from `NtQuerySystemInformation`, with optional enrichment from WinDbg’s `pooltag.txt` (source names and descriptions). The UI supports filtering, pause/resume refresh, color-coded deltas between updates, dark mode, and toolbar controls. (source: wiki/sources/descriptions/zodiacon__PoolMonXv3.md)

Use it beside [[kn-diff-pool]] Big Pool snapshot diffs and [[pooldump]] interactive dumps when triaging unusual pool consumers (drivers, manual-map footprints, anti-cheat components) without a full kernel debugger session. Same maintainer lane as [[dbgprint]] and [[object-explorer]] Windows Kernel Explorer tooling.

## Links

- Repo: https://github.com/zodiacon/PoolMonXv3 (README: GUI monitor for Windows kernel pool allocation tags with filtering, pause/resume, and WinDbg pooltag.txt integration)

## Related

[[kernel-pool-scanning]] · [[kn-diff-pool]] · [[pooldump]] · [[dbgprint]] · [[overviews/windows-kernel]] · [[research-rigor]]
