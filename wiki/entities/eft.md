---
title: eft
kind: entity
topics: [game-hacking, game-engine, graphics-api, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/Splitx12__eft.md
updated: 2026-08-20
confidence: medium
---

# eft

**eft** (Splitx12/eft) is a C++ **internal** cheat implementation for **Escape From Tarkov** with assembly helpers. It implements Unity object access, world and entity traversal, and in-game rendering utilities. Feature modules include ESP-style visuals, extraction-status display, aim-assist-related targeting logic, and configurable menu controls. The repository documents Win10 **`KeUserModeCallBack`** usage in `usercallback.h` as part of win32k GUI-subsystem callback research. Intended for advanced cheat-development study of Unity-based shooter memory structures and runtime manipulation on BattlEye-protected clients. (source: wiki/sources/descriptions/Splitx12__eft.md)

Sits in the in-process Unity internal lane beside modular C++ internals such as [[eft-tarkov-internal-cheat]], rendering scaffolds such as [[eft-internal]] and [[simple-eft-base]], Mono method-hooking samples such as [[eft-monoeft]], and external DMA/radar stacks such as [[meatyeftrelease]] and [[eft-external]].

## Links

- Repo: https://github.com/Splitx12/eft
- KeUserModeCallBack Win10 reference: https://github.com/Splitx12/eft/blob/834064aacaab7353173e36acc15933a3cf9289b3/eft/usercallback.h#L50

## Related

[[battleye]] · [[il2cpp]] · [[world-to-screen]] · [[present-hook]] · [[eft-tarkov-internal-cheat]] · [[eft-internal]] · [[simple-eft-base]] · [[eft-monoeft]] · [[meatyeftrelease]] · [[eft-external]] · [[escapefromtarkov-trainer]] · [[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/windows-kernel]]
