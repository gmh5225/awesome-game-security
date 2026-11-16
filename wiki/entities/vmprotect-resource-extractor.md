---
title: VMProtect Resource Extractor
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ivanpotatoes__VMProtect-Resource-Extractor.md
updated: 2026-11-16
confidence: medium
---

# VMProtect Resource Extractor

**VMProtect resource recovery** tooling that locates VMProtect’s encrypted PE resource table, derives the protection key, and dumps embedded resources from protected **EXE** and **DLL** images without an unprotected copy or fixed addresses. Ships three workflows: a C++ static **command-line** tool for on-disk images; a **Unicorn**-based emulator (bundled Python, Capstone, instruction-budget limits) when resources appear only after startup code runs in packed binaries; and an **x64dbg plugin** that scans live process memory after unpacking. Output is numbered binary blobs plus a manifest listing type, name, language, size, and RVA per resource. Targets reverse engineers and malware analysts on VMProtect **3.3.x–3.10.x** resource protection in game and application security research. (source: wiki/sources/descriptions/ivanpotatoes__VMProtect-Resource-Extractor.md)

Complements full-image unpackers such as [[vmprotect-unpacker]], [[vmprotect-dumper]], and [[vmprotect-3-x-emulator-memory-dumper]] when icons, dialogs, embedded configs, or other PE resources stay encrypted on disk. Pairs the author’s x64dbg anti-analysis plugins [[kozdbg]] and [[kozvm]] for live debugging of protected builds.

## Links

- Repo: https://github.com/ivanpotatoes/VMProtect-Resource-Extractor (README tag: static, Unicorn emulation, x64dbg plugin; manifest output)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[vmprotect]] · [[x64dbg]] · [[kozdbg]] · [[kozvm]] · [[vmprotect-unpacker]] · [[vmprotect-dumper]] · [[vmprotect-3-x-emulator-memory-dumper]]