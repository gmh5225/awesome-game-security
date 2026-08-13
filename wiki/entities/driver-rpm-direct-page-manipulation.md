---
title: Driver-RPM-DirectPageManipulation
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__Driver-RPM-DirectPageManipulation.md
updated: 2026-08-13
confidence: medium
---

# Driver-RPM-DirectPageManipulation

Minimal Windows kernel sample demonstrating cross-process memory read/write by **directly manipulating paging structures** instead of documented copy helpers such as `MmCopyVirtualMemory`. (source: wiki/sources/descriptions/gmh5225__Driver-RPM-DirectPageManipulation.md)

The driver allocates a contiguous page, locates its own PTE, overwrites the page-frame number to remap arbitrary physical pages, then uses manual virtual-to-physical translation to implement process memory copy routines. Sample entry reads target-process module data without standard documented copy APIs. Paged-out memory handling and multithreading are intentionally omitted to keep the logic compact.

Primarily useful for Windows kernel researchers studying PTE rewriting, manual address translation, and page-table-based process memory access.

## Links

- Repo: https://github.com/gmh5225/Driver-RPM-DirectPageManipulation (README tag: read physical memory)

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[readphys]] · [[page-table-injector]] · [[pteditor]] · [[ntmemory]] · [[windows-kernel-pagehook]]
