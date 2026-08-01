---
title: plthook
kind: entity
topics: [game-hacking, reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/kubo__plthook.md
updated: 2026-08-01
confidence: medium
---

# plthook

Cross-platform **C library** for hooking dynamically linked functions by modifying **PLT** (Procedure Linkage Table) and **GOT** (Global Offset Table) entries — on Windows, the analogous **IAT** import table. Calls through the import table redirect to user-defined replacement functions without patching function prologues. Supports **ELF**, **Mach-O**, and **PE** binaries on Linux, macOS, and Windows; aimed at security researchers, profiling tool developers, and portable dynamic interception. (source: wiki/sources/descriptions/kubo__plthook.md)

## Links

- Repo: https://github.com/kubo/plthook

## Related

[[detours]] · [[polyhook]] · [[polyhook-2-0]] · [[libmem]] · [[mobile-anti-cheat]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/mobile-security]]
