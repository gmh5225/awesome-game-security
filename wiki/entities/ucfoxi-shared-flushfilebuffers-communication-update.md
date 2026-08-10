---
title: UCFoxi Shared FlushFileBuffers Communication Update
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__UCFoxi-Shared-FlushFileBuffers-Communication-Update.md
updated: 2026-08-10
confidence: medium
---

# UCFoxi Shared FlushFileBuffers Communication Update

Kernel and usermode communication sample (gmh5225) that repurposes **`IRP_MJ_FLUSH_BUFFERS`** on `\Driver\PEAUTH` as the trigger while request payloads live in a **shared user buffer**. On driver entry it resolves the target driver object, swaps `MajorFunction[IRP_MJ_FLUSH_BUFFERS]` via `InterlockedExchangePointer`, and reloads the shared-buffer pointer plus client PID from registry values under `\Registry\Machine\SOFTWARE\ucflash`. The hook copies a `REQUEST_DATA` block with `MmCopyVirtualMemory`, rotates a magic value to keep the session synchronized, and dispatches read, write, protect, alloc, free, module, and main-base operations through helper callbacks backed by physical-memory access code. Useful for Windows kernel researchers comparing alternative driver communication channels based on hijacked IRP paths, registry-seeded shared buffers, and lightweight kernel memory services. (source: wiki/sources/descriptions/gmh5225__UCFoxi-Shared-FlushFileBuffers-Communication-Update.md)

## Links

- Repo: https://github.com/gmh5225/UCFoxi-Shared-FlushFileBuffers-Communication-Update

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[kernel-payload-comms]] · [[gina-public]] · [[evcommunication]] · [[custom-data-ptr-swap-sample]]
