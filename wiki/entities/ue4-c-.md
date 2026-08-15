---
title: ue4-c-
kind: entity
topics: [game-hacking, windows-kernel, game-engine, anti-cheat]
sources:
  - wiki/sources/descriptions/frankelitoc__UE4-c-.md
updated: 2026-08-15
confidence: medium
---

# ue4-c-

External **Unreal Engine 4** cheat for **Valorant** (README `[External]`; frankelitoc): a **kernel-mode driver** manual-mapped via **EFI** communicates through **IOCTL dispatch hooks**, paired with a **usermode client** that reads game memory through the driver interface. The client renders an **ImGui** overlay on a **DirectX 9** window, uses **ToolHelp32** snapshots for process enumeration, and performs cross-process reads of UE4 **actor** and **player** structures via the driver. (source: wiki/sources/descriptions/frankelitoc__UE4-c-.md)

Sits in the EFI-loaded kernel external lane beside other Valorant out-of-process stacks such as [[valorant-external-source]] and [[valorant-cheat-external]], kernel read drivers such as [[valo-driver]], and UE4 layout research under [[unreal-object-model]] rather than in-process internal bases under [[vanguard]].

## Links

- Repo: https://github.com/frankelitoc/UE4-c-

## Related

[[vanguard]] · [[valorant-external-source]] · [[valorant-cheat-external]] · [[valo-driver]] · [[unreal-object-model]] · [[imgui]] · [[rainbow-efi]] · [[driver-read-write]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/game-engine]]
