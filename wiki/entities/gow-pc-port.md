---
title: God of War PC Port (gow-pc-port)
kind: entity
topics: [reverse-engineering, game-engine, graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/danielalves96__gow-pc-port.md
  - wiki/sources/README-categories.md
updated: 2026-10-31
confidence: medium
---

# God of War PC Port (gow-pc-port)

**gow-pc-port** ([danielalves96/gow-pc-port](https://github.com/danielalves96/gow-pc-port)) is a **native PC port** of **God of War (PlayStation 2, NTSC-U, SCUS-97399)** that lifts retail **MIPS (R5900)** binaries into runnable **native code** through **static recompilation**, not full-system emulation. Users supply **legally obtained disc data**; the repo ships **no bundled game assets**. (source: wiki/sources/descriptions/danielalves96__gow-pc-port.md)

## Recompiler toolchain (Rust)

A **Rust workspace** implements the **MIPS recompiler**, **ELF and R5900** tooling, **parity checks** against reference output, **ISO-based installer** helpers, and developer **validation utilities**. The pipeline covers **function mapping**, **VU1** handling, and **texture-replacement hooks** for studying how commercial PS2 code paths translate to a PC host. (source: wiki/sources/descriptions/danielalves96__gow-pc-port.md)

## Runtime host (C++)

**C++ with CMake** provides the in-process **runtime**, **IOP subsystem**, and **game-specific overrides**. The display path targets **OpenGL** on **Windows and Linux**. PC-side features include a **Tauri + React launcher**, **widescreen** support, and an **in-game cheat menu**—useful for preservation and deep inspection workflows, not live-service anti-cheat bypass. (source: wiki/sources/descriptions/danielalves96__gow-pc-port.md)

## Research use

Targets developers and researchers studying **binary translation**, **legacy console bring-up**, and **deep inspection** of a commercial title’s execution paths when paired with owned disc images. Fits the README **Cheat → Guide / RE Tools** lane beside [[ps2-port-engine]] and [[static-runtime-evidence]]-style lift-vs-runtime labeling. (source: wiki/sources/descriptions/danielalves96__gow-pc-port.md)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/game-engine]] · [[overviews/graphics-api]] · [[ps2-port-engine]] · [[ps2-ida-vu-micro]] · [[vifterpreter]] · [[static-runtime-evidence]]

## Links

- Repo: https://github.com/danielalves96/gow-pc-port
