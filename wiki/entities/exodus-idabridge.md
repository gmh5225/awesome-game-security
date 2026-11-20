---
title: Exodus IdaBridge
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/elgroovy__exodus-idabridge.md
updated: 2026-11-20
confidence: medium
---

# Exodus IdaBridge

**IdaBridge** is an **Exodus emulator** extension that connects **IDA Pro** to a live **Sega Mega Drive** session so analysts can debug emulated ROM execution from the disassembler. (source: wiki/sources/descriptions/elgroovy__exodus-idabridge.md)

It implements the **gRPC** debugger protocol from **smd_ida_tools2** and pairs with the existing **Gensida** IDA plugin, replacing the older Gens backend with Exodus. Exposed facilities include **68000** and **VDP** state, memory read/write, **DMA** visibility, breakpoints and watchpoints, stepping, call stacks, and execution tracing for code discovery in IDA. (source: wiki/sources/descriptions/elgroovy__exodus-idabridge.md)

Built in **C++** for Windows as a Visual Studio plugin with **gRPC** and Protocol Buffers via **vcpkg**. Targets reverse engineers and researchers analyzing Mega Drive games in a **cycle-accurate** emulator—not live anti-cheat surfaces.

README category: **Cheat → RE Tools** — emulator-backed IDA live-debug bridge for 16-bit console ROM RE.

## Links

- Repo: https://github.com/elgroovy/exodus-idabridge

## Related

[[ida-bochs-windows]] · [[ida-vmware-windows-gdb]] · [[idacode]] · [[saturnkit]] · [[menace-reverse-engineering]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]