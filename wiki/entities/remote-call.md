---
title: RemoteCall
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/1401199262__RemoteCall.md
updated: 2026-09-05
confidence: medium
---

# RemoteCall

**RemoteCall** (1401199262) is a **Windows kernel technique** (C++) that executes **user-mode code in an arbitrary target process**. It **chains a kernel APC with `KeUserModeCallback`**, pivots execution through a **driver I/O routine**, and returns with **controlled context restoration**. The implementation **avoids allocating RWX shellcode memory in the target process** while still enabling callable user-mode execution. Primary use case: **advanced process injection research** and evaluation of **detection trade-offs in game security environments**. Listed under cheat with README tag `[APC Remote Call]`. (source: wiki/sources/descriptions/1401199262__RemoteCall.md)

Extends the **`KeUserModeCallback`** primitive lane beside demos such as [[keusermodecallback]] with a **full kernel-APC injection chain** into arbitrary processes rather than standalone callback-to-MessageBox scaffolding.

## Links

- Repo: https://github.com/1401199262/RemoteCall

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[keusermodecallback]] · [[apc-research]] · [[injdrv]] · [[kinject]] · [[process-injection-techniques]] · [[windows-process-injection]]
