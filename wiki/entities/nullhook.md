---
title: NullHook
kind: entity
topics: [game-hacking, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/NullTerminatorr__NullHook.md
updated: 2026-08-22
confidence: medium
---

# NullHook

Tutorial-oriented **Windows game-hacking** sample (NullTerminatorr) that combines **user-mode and kernel-mode** components in a split Visual Studio solution: a **driver project** plus a **userland client**. The C/C++ codebase demonstrates **memory and hook-related workflows** across ring boundaries. Practical setups load the driver through **external manual mapping** rather than conventional signed-driver installation. Primary use case: educational research into **kernel-assisted cheat development** techniques. (source: wiki/sources/descriptions/NullTerminatorr__NullHook.md)

README lane: **`NtDxgkGetTrackedWorkloadStatistics`** — dxgkrnl graphics-syscall hook channel for covert KM↔UM communication (same family as [[kernel-cheat-for-directx3d]] and [[comm-im-miraclela]]).

Complements other NullTerminatorr educational samples such as [[thread-hijacking-injector]] (compact user-mode injection PoC) when studying split driver/client architecture.

## Links

- Repo: https://github.com/NullTerminatorr/NullHook

## Related

[[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[kernel-cheat-for-directx3d]] · [[thread-hijacking-injector]] · [[kdmapper]] · [[windows-kernel-pagehook]]
