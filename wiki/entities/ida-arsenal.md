---
title: IDA Arsenal
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/khalilammarr__ida-arsenal.md
updated: 2026-11-19
confidence: medium
---

# IDA Arsenal

**IDA Arsenal** (khalilammarr/ida-arsenal) is an **IDA Pro 9.1 Python plugin** that keeps symbolic solving, input recovery, crypto triage, and auxiliary RE utilities **inside the IDB workflow**. A **separate backend process** built on **angr** and **Z3** receives find/avoid address or function goals from the UI and recovers **stdin**, **argv**, or **call-site inputs** under length and printable constraints. (source: wiki/sources/descriptions/khalilammarr__ida-arsenal.md)

## Capabilities

- Find/avoid symbolic path solving via angr-backed backend
- Input discovery for stdin, argv, and libc stack call sites
- Import-usage function classification and stripped-binary crypto/hash recognition
- **Z3** / **SMT-LIB** predicate solving tab
- Packer and anti-analysis trait scoring; Frida and GDB helper export
- Go symbol recovery via a small Go helper

## Scope

Primary target: **Linux x86-64 ELF** crackmes, CTF challenges, and malware-style RE, including workflows for **protected game binaries** and **license checks**. (source: wiki/sources/descriptions/khalilammarr__ida-arsenal.md)

## Positioning

Listed under **Cheat → RE Tools**. Complements in-IDA symbolic execution via [[ponce]] and Ghidra-side [[ponce4ghidra]] / [[angry-ghidra]]; pairs with core [[triton]] / angr tooling and CFF recovery via [[idadeflat]].

## Links

- Repo: https://github.com/khalilammarr/ida-arsenal

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ponce]] · [[ponce4ghidra]] · [[angry-ghidra]] · [[idadeflat]] · [[triton]] · [[frida]]