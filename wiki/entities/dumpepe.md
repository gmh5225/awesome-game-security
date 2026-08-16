---
title: DumpPE
kind: entity
topics: [reverse-engineering, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/d35ha__DumpPE.md
updated: 2026-08-16
confidence: medium
---

# DumpPE

Lightweight command-line **PE dumper** that reads a mapped PE image from a remote process via `OpenProcess` / `ReadProcessMemory`, parses DOS and NT headers to derive full image size from `SizeOfImage`, and writes the complete in-memory PE dump to disk—including all sections. Accepts a PID, hex base address, and output filename; supports both 32-bit and 64-bit targets. Mainly useful for reverse engineers and game-security researchers dumping **packed or protected executables** from memory after runtime unpack, for static analysis in IDA/Ghidra. (source: wiki/sources/descriptions/d35ha__DumpPE.md)

Sits in the usermode RPM dump lane beside kernel-mode dumpers such as [[ksdumper-11]] and title-specific PE reconstruction tools such as [[league-dumper]]—minimal CLI surface without import reconstruction or AC-specific module discovery.

## Links

- Repo: https://github.com/d35ha/DumpPE

## Related

[[ksdumper-11]] · [[league-dumper]] · [[pereconstruct]] · [[umpmlib]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
