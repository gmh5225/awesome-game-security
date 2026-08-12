---
title: Kernel-VAD-Injector
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__Kernel-VAD-Injector.md
updated: 2026-08-12
confidence: medium
---

# Kernel-VAD-Injector

Unsigned-driver-assisted **DLL injector** that conceals its staging region by manipulating **VADs** and **PTEs** instead of relying on ordinary user-mode allocations alone. The driver communicates through a **PatchGuard-safe `xKdEnumerateDebuggingDevices` hook**, traps a user thread in kernel, and runs a command loop supporting read, write, allocate memory, spoof PTE, allocate VAD, and remove VAD requests. Internally it pattern-finds `MiAllocateVad`, `MiInsertVad`, and `MiInsertVadCharges` inside ntoskrnl, uses `KeStackAttachProcess` around memory operations, and removes the VAD node again after mapping so the injected region is less visible to `NtQueryVirtualMemory` and similar checks. Mainly useful for Windows kernel researchers studying manual mapping with VAD tree abuse, executable-page concealment, and driver-based post-injection cleanup. (source: wiki/sources/descriptions/gmh5225__Kernel-VAD-Injector.md)

README lane: Hide VAD.

## Links

- Repo: https://github.com/gmh5225/Kernel-VAD-Injector

## Related

[[page-table-injector]] · [[kernelmode-manual-mapping-through-iat]] · [[memory-relocalloc]] · [[wizard-loader]] · [[battleye-region-walking]] · [[system-thread-finder]] · [[patchguard]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
