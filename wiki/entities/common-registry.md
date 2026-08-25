---
title: Common-Registry
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/EBalloon__Common-Registry.md
updated: 2026-08-25
confidence: medium
---

# Common-Registry

**Common-Registry** (EBalloon) is a **proof-of-concept** for **user-mode ↔ kernel-mode communication through the Windows Registry**. The C++ project pairs a **KMDF driver** with a **user-mode client** and explores **custom process-attach handling** plus related **low-level memory-management** ideas noted by the author. Intended for **Windows internals research** and **anti-cheat bypass experimentation**; README tag `[Registry Callback]`. (source: wiki/sources/descriptions/EBalloon__Common-Registry.md)

Sits in the same **registry-callback** and covert **KM↔UM IPC** lane as [[common-registry-jmp-rcx]], [[boundcallback]], [[evcommunication]], and [[km-um-communication]].

## Links

- Repo: https://github.com/EBalloon/Common-Registry

## Related

[[kernel-callbacks]] · [[common-registry-jmp-rcx]] · [[boundcallback]] · [[evcommunication]] · [[km-um-communication]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
