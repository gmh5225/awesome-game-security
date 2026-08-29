---
title: VMProtect Dumper
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/whoamicrash__VMProtectDumper.md
updated: 2026-08-29
confidence: medium
---

# VMProtect Dumper

Standalone **Windows console utility** (pure C, WinAPI only) that unpacks **VMProtect-protected PE files** — EXE, DLL, OCX, and CPL — from **live process memory** into analysis-ready dumps. Polls for section decryption, reconstructs the original entry point and import address table via thunk following and API hooks, and harvests dynamically allocated executable memory regions outside the original image layout. Supports drag-and-drop operation, dropper and DLL loading modes, optional **[[pe-sieve]]** integration, IOC string extraction, anti-analysis countermeasures, and packages artifacts into a password-protected archive for safe handling. Targets malware analysts, reverse engineers, and incident responders who need unpacked images for static analysis in IDA or Ghidra. (source: wiki/sources/descriptions/whoamicrash__VMProtectDumper.md)

Memory-first unpack sibling to debugger-driven [[vmp-unpacker]], Python sogen emulation via [[vmpunpack]], and .NET runtime dump via [[vmunprotect-dumper]]. Pair output with Fix VMP devirt tooling such as [[novmpy]], [[vmplift]], or [[vmprotect-devirtualization]] when virtualized handlers remain.

## Links

- Repo: https://github.com/whoamicrash/VMProtectDumper

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[vmprotect]] · [[vmp-unpacker]] · [[vmpunpack]] · [[vmunprotect-dumper]] · [[pe-sieve]] · [[dumpepe]] · [[unpacker]]
