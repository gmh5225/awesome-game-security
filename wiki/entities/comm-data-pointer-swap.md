---
title: Comm-Data-Pointer-Swap
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__Comm-Data-Pointer-Swap.md
updated: 2026-08-14
confidence: medium
---

# Comm-Data-Pointer-Swap

Proof-of-concept **kernel communication** sample that swaps an internal **data pointer in a win32k path** instead of exposing a conventional device interface. The driver pattern-scans **win32kbase.sys**, resolves the target qword pointer, attaches to **explorer.exe**, and uses **`InterlockedExchangePointer`** to replace that pointer with a custom handler. User mode resolves **`NtDCompositionSetChildRootVisual`** from **win32u.dll** to trigger the path—a compact **pointer-swap communication through a GUI syscall** rather than a full framework. (source: wiki/sources/descriptions/gmh5225__Comm-Data-Pointer-Swap.md)

Mainly useful for Windows kernel researchers studying **covert driver communication**, **pointer redirection inside GUI subsystems**, and tradeoffs of obvious one-off hook placement — adjacent to [[dataptrswap-driver]] (same win32kbase swap pattern on `NtSetCompositionSurfaceAnalogExclusive`), [[comm-data-ptr-driver]], [[comm-neko-swap]], and [[data-ptr-swap]].

## Links

- Repo: https://github.com/gmh5225/Comm-Data-Pointer-Swap

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[dataptrswap-driver]] · [[comm-data-ptr-driver]] · [[comm-neko-swap]] · [[data-ptr-swap]] · [[driver-communication-list]] · [[win32k-file-collection]]
