---
title: memdbg
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/dbcyyds__MemDbg.md
updated: 2026-08-16
confidence: medium
---

# memdbg

**MemDbg** is a Cheat Engine–style memory debugger for rooted **Android aarch64** devices. It ships as a single deployable ELF binary that combines a **Vulkan** fullscreen overlay with **Dear ImGui**, a native root memory engine, and embedded **Lua 5.4** scripting. Written primarily in C++, it targets security researchers, reverse engineers, and game modders who need deep in-process inspection and automation on Android under root or **Termux**. (source: wiki/sources/descriptions/dbcyyds__MemDbg.md)

Core capabilities include process attach, multi-type memory scanning, pointer and structure analysis, hex browsing, hardware and software breakpoints, speedhack, Auto Assemble, and trainer-style cheat tables with value freezing. The tool also offers disassembly, watchpoints, remote calls, shared-object injection, hotkeys, and an on-screen soft keyboard for touch interaction.

Sits in the Cheat Android Memory Explorer / memory-scanner lane beside lightweight scanners such as [[cheap-engine]] and CLI tools such as [[mypower]], but with a fuller CE-like debugger surface (breakpoints, disassembly, Lua automation, Vulkan overlay UI).

## Links

- Repo: https://github.com/dbcyyds/MemDbg

## Related

[[cheap-engine]] · [[mypower]] · [[termux-app]] · [[android-mem-edit]] · [[root-socket-kit]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
