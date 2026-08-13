---
title: Driver-read_write
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__Driver-read_write.md
updated: 2026-08-13
confidence: medium
---

# Driver-read_write

Manually mapped kernel read/write driver that hijacks `Beep.sys` `IRP_MJ_DEVICE_CONTROL` to expose memory copy and module-base queries. Swaps dispatch on `\Driver\Beep`, validates user requests, attaches to target processes for direct memory access, and reuses the hooked driver object so the mapped payload can masquerade as a more legitimate kernel module. (source: wiki/sources/descriptions/gmh5225__Driver-read_write.md)

Also includes cleanup for `PiDDBCacheTable` and `MmUnloadedDrivers`, making it both a communication example and a post-mapping trace-reduction reference for vulnerable-driver-based mapping workflows. Primarily useful for Windows kernel researchers studying IRP hijacking, basic process memory primitives, and unsigned-driver-loader artifact cleanup.

## Links

- Repo: https://github.com/gmh5225/Driver-read_write

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[boom]] · [[read-write-driver]] · [[hide-driver-testing]] · [[known-driver-mappers]] · [[ntmemory]]
