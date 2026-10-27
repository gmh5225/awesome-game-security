---
title: ReaperPy
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Ston3dd__ReaperPy.md
  - wiki/sources/README-categories.md
updated: 2026-10-27
confidence: high
---

# ReaperPy

**ReaperPy** (Ston3dd/ReaperPy) is a Python desktop toolkit that connects to a jailbroken **PlayStation 5** over the network through the **ps5debug-NG** payload, offering Cheat Engine–style memory scanning, patching, and debugging from a PC on the same LAN. (source: wiki/sources/descriptions/Ston3dd__ReaperPy.md)

README category: **PlayStation** (live console memory RE / trainer workflow).

## Prerequisites

Requires a **jailbroken PS5** with the **ps5debug-NG** payload active and a desktop client on the **same network** as the console. (source: wiki/sources/descriptions/Ston3dd__ReaperPy.md)

## Capabilities

- Byte patches and **x86-64 code caves** assembled with Keystone; pointer scanning; hardware watchpoints; live hex and Capstone disassembly views.
- **Undo journal** for memory writes.
- **Unreal Engine** and **Unity IL2CPP** workflows: live object browsing, SDK-driven cheat menus, static helpers consuming dumper output.
- Scriptable **ps5 API** for automation; import/export of **GoldHEN** and **etaHEN** cheat formats (JSON, SHN, encrypted MC4). (source: wiki/sources/descriptions/Ston3dd__ReaperPy.md)

## Scope

Targets researchers and mod authors who need deep in-process inspection, trainer development, and **offline single-player** experimentation on **their own hardware**—not online anti-cheat bypass research. (source: wiki/sources/descriptions/Ston3dd__ReaperPy.md)

## Links

- Repo: https://github.com/Ston3dd/ReaperPy
- Related: [[niak-ps5]] (homebrew library shell), [[nines]] (remote ELF inject), [[cheatrunner-patches]] (Title-ID XML patches), [[ps5-linux-loader]], [[ida-ps5-elf-plugin]]
