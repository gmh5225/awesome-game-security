---
title: memdumper
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/kp7742__MemDumper.md
updated: 2026-08-01
confidence: medium
---

# memdumper

Android memory dumping tool that extracts loaded shared library (`.so`) segments from a target process address space and reconstructs valid ELF binaries with fixed headers for both 32-bit and 64-bit architectures. Reads directly from `/proc/<pid>/mem` without `ptrace`, bypassing basic anti-debugging protections that monitor attach-based debuggers. Sits in the Cheat / Dump lane for offline native `.so` RE in IDA/Ghidra after runtime extraction from packed or protected mobile games. (source: wiki/sources/descriptions/kp7742__MemDumper.md)

## Links

- Repo: https://github.com/kp7742/MemDumper

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ue4dumper]] · [[zygisk-dump-dex]] · [[lldbext-dump]] · [[android-unpacker]] · [[jadx]]
