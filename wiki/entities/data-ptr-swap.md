---
title: .data-ptr-swap
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/xPasters__.data-ptr-swap.md
updated: 2026-07-18
confidence: medium
---

# .data-ptr-swap

C/C++ kernel research sample centered on **`NtSetCompositionSurfaceAnalogExclusive`**—a composition-surface path used to study stealthy cheat / driver communication rather than obvious IOCTL or named-device surfaces. (source: wiki/sources/descriptions/xPasters__.data-ptr-swap.md)

Useful for game-security and reverse-engineering researchers mapping Ring0↔usermode channels that ride Windows composition APIs (adjacent to samples tagged with related composition handles such as [[zero-thread-kernel]]).

## Links

- Repo: https://github.com/xPasters/.data-ptr-swap

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[boom]] · [[zero-thread-kernel]]
