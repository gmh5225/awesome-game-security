---
title: r69-driver
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__r69-driver.md
updated: 2026-08-07
confidence: medium
---

# r69-driver

Compact Windows kernel communication library that routes read, write, and process-query requests through **HalPrivateDispatchTable** hooks instead of a conventional device object. The driver replaces `HalTimerQueryAuxiliaryCounterFrequency` with a handler that pulls a `c_packet` from the caller trap frame, decodes `read_process_memory`, `write_process_memory`, and `query_process_data` requests, and services them by translating target virtual addresses to physical pages from the process CR3. A second hook on `HalClearLastBranchRecordStack` refreshes DirectoryTableBase from the current CR3; the user-mode `c_r69` wrapper exposes the path via `NtQueryAuxiliaryCounterFrequency` and can attach to a target process by name. Mainly useful for studying syscall-adjacent communication, HalPrivateDispatchTable abuse, and physical-memory-backed process access without a standard IOCTL interface. (source: wiki/sources/descriptions/gmh5225__r69-driver.md)

## Links

- Repo: https://github.com/gmh5225/r69-driver

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[poseidon]] · [[gina-public]] · [[read-write-driver]] · [[ntmemory]] · [[valo-driver]]
