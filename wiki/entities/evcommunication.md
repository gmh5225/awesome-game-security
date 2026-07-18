---
title: EvCommunication
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/weak1337__EvCommunication.md
updated: 2026-07-18
confidence: medium
---

# EvCommunication

Kernel↔usermode communication research sample that signals via Windows named events (`ZwOpenEvent` / `ZwSetEvent` / `ZwWaitForSingleObject`) instead of IOCTL device paths that [[battleye]] / [[easy-anti-cheat]] commonly monitor. (source: wiki/sources/descriptions/weak1337__EvCommunication.md)

The driver hooks `NtTokenManager` (`NtTokenManagerCreateFlipObjectReturnTokenHandle`) as the initial trigger, then runs a shared event loop: usermode signals a request event, the kernel handler performs memory R/W with `MmCopyVirtualMemory`, and completion is signaled on a second event. Useful for studying stealth Ring0↔Ring3 channels adjacent to [[boom]] and [[data-ptr-swap]].

## Links

- Repo: https://github.com/weak1337/EvCommunication

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[boom]] · [[data-ptr-swap]] · [[ntmemory]]
