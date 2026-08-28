---
title: UCMiraka-ValorantExternal
kind: entity
topics: [game-hacking, windows-kernel, anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/Chase1803__UCMiraka-ValorantExternal.md
updated: 2026-08-28
confidence: medium
---

# UCMiraka-ValorantExternal

**UCMiraka-ValorantExternal** (Chase1803/UCMiraka-ValorantExternal) is a C++ **proof-of-concept external framework** for reading Valorant game memory via a paired **kernel driver** and **user-mode client**. The kernel component hooks a **win32k** function — **NtUserGetPointerProprietaryId** — to receive custom request packets and exposes operations such as **process memory reads** and **PML4-related data retrieval**. The user component locates the game process, initializes the driver channel, and repeatedly reads core Unreal pointers such as **UWorld**, **ULevel**, and **GameState**. Framed for low-level game hacking and anti-cheat research focused on **driver communication** and **external data extraction** under [[vanguard]]. (source: wiki/sources/descriptions/Chase1803__UCMiraka-ValorantExternal.md)

Sits in the win32k covert-comms external lane beside [[ntuserupdatewindowtrackinginfo]] and [[kernel-eac-be-comm]], and in the Valorant out-of-process lane beside [[valorant-external-source]], [[valo-driver]], and [[phoenix-valorant-cheat]].

## Architecture

| Layer | Role |
|-------|------|
| Kernel driver | Hooks win32k **NtUserGetPointerProprietaryId**; custom request packets for memory R/W and PML4-related retrieval |
| User-mode client | Process discovery; driver channel init; repeated UE pointer reads (UWorld, ULevel, GameState) |

## Links

- Repo: https://github.com/Chase1803/UCMiraka-ValorantExternal

## Related

[[vanguard]] · [[ntuserupdatewindowtrackinginfo]] · [[kernel-eac-be-comm]] · [[win32khooker]] · [[km-um-communication]] · [[valorant-external-source]] · [[valo-driver]] · [[phoenix-valorant-cheat]] · [[unreal-object-model]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
