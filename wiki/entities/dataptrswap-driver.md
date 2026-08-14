---
title: DataPtrSwap-driver
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__DataPtrSwap-driver.md
updated: 2026-08-14
confidence: medium
---

# DataPtrSwap-driver

Older cheat-driver example using a **data-pointer swap in win32kbase** for KM↔UM communication instead of a conventional device interface. The driver scans win32kbase for the target pointer, attaches to `explorer.exe`, swaps it with a custom `NtSetCompositionSurfaceAnalogExclusive` handler via `InterlockedExchangePointer`, and routes requests through usermode-supplied structures. Also bundles cleanup utilities for `MmUnloadedDrivers` and related loader residue — part comms demo, part anti-forensics helper. (source: wiki/sources/descriptions/gmh5225__DataPtrSwap-driver.md)

Mainly useful for Windows kernel researchers studying data-pointer-swap communication, win32k-based hook placement, and cleanup logic alongside manually mapped cheat drivers — adjacent to [[data-ptr-swap]] (xPasters; same composition-surface syscall), [[custom-data-ptr-swap-sample]], [[driver-read-write]], and [[hide-driver-testing]].

## Links

- Repo: https://github.com/gmh5225/DataPtrSwap-driver

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[data-ptr-swap]] · [[custom-data-ptr-swap-sample]] · [[driver-read-write]] · [[hide-driver-testing]] · [[dataptrhookwin11]]
