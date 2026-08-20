---
title: Shared FlushFileBuffers Communication
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/UCFoxi__Shared-FlushFileBuffers-Communication.md
updated: 2026-08-20
confidence: medium
---

# Shared FlushFileBuffers Communication

Kernel-to-user communication sample (UCFoxi) that uses a **shared buffer** and **`FlushFileBuffers`-triggered IRP handling** as the command path. The driver hooks **`IRP_MJ_FLUSH_BUFFERS`** to process requests on demand instead of relying on a persistent worker thread. Split into C++ kernel and user-mode components built with Visual Studio. Useful for researching stealthier driver communication patterns in game security and anti-cheat bypass experiments. (source: wiki/sources/descriptions/UCFoxi__Shared-FlushFileBuffers-Communication.md)

## Links

- Repo: https://github.com/UCFoxi/Shared-FlushFileBuffers-Communication

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[ucfoxi-shared-flushfilebuffers-communication-update]] · [[kernel-payload-comms]] · [[gina-public]] · [[evcommunication]] · [[km-um-communication]]
