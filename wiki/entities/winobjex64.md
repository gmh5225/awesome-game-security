---
title: WinObjEx64
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/hfiref0x__WinObjEx64.md
updated: 2026-08-05
confidence: medium
---

# WinObjEx64

Advanced Windows utility for exploring the **Object Manager** namespace—directories, symbolic links, sections, and other kernel object types—with optional editing of object-related security descriptors. Administrative privileges are required to view much of the namespace and to modify object security information. (source: wiki/sources/descriptions/hfiref0x__WinObjEx64.md)

Primarily useful for **anti-cheat engineers** and **defensive security researchers** working in the anti-cheat / Windows Ring0 [[kernel-callbacks]] lane. The README highlights **Enumerate Callback** support (`extrasCallbacks.c`) for inspecting registered notify routines alongside namespace exploration. (source: wiki/sources/descriptions/hfiref0x__WinObjEx64.md)

Complements defensive inspection GUIs such as [[openark]] and offensive callback enumeration drivers such as [[bustercall]] on the same callback / object surfaces.

## Links

- Repo: https://github.com/hfiref0x/WinObjEx64
- Enumerate Callback: https://github.com/hfiref0x/WinObjEx64/blob/7284d711b2eeebfd965713fc79353b9b76e23083/Source/WinObjEx64/extras/extrasCallbacks.c#L117

## Related

[[kernel-callbacks]] · [[openark]] · [[bustercall]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
