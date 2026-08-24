---
title: Pointer Lab
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/HeathHowren__Pointer-Lab.md
updated: 2026-08-24
confidence: medium
---

# Pointer Lab

**Pointer Lab** (HeathHowren/Pointer-Lab) is a Windows x64 user-mode memory research tool that attaches to running 64-bit processes to scan memory, track addresses, and read, write, freeze, disassemble, and patch them. Built in C++20 with a Dear ImGui dockspace interface, it targets reverse engineering practice, CTF work, and authorized inspection of your own software or single-player games—not stealth or online anti-cheat evasion. (source: wiki/sources/descriptions/HeathHowren__Pointer-Lab.md)

## Capabilities

- Multi-type memory scanner with wildcard byte patterns
- Multi-level pointer chain finder that survives ASLR
- Live hex memory viewing
- Zydis-based disassembly and Keystone-based assembly with safe NOP-padded patching
- Repeatable software breakpoints
- DLL injection helpers behind confirmation dialogs
- Embedded Lua 5.4 scripting console (UI-thread isolated) for automating scans and memory operations
- `.iretable` project files to persist address lists and pointer chains across sessions

## Links

- Repo: https://github.com/HeathHowren/Pointer-Lab

## Related

[[cheat-engine]] · [[mhsx]] · [[intro-to-gamehacking]] · [[x64dbg]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
