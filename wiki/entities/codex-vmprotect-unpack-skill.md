---
title: codex-vmprotect-unpack-skill
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/UzawaReisaQwQ__codex-vmprotect-unpack-skill.md
updated: 2026-11-12
confidence: medium
---

# codex-vmprotect-unpack-skill

[UzawaReisaQwQ/codex-vmprotect-unpack-skill](https://github.com/UzawaReisaQwQ/codex-vmprotect-unpack-skill) is a **Codex/Claude agent skill** that guides **authorized** analysis and recovery of **VMProtect-protected** native **Windows PE** executables and DLLs. Workflows emphasize **unpacking**—restoring unpacked images, rebuilding import tables, recovering strings, and reasoning about anti-debug and anti-virtualization checks—while **separating unpack success from full devirtualization**. (source: wiki/sources/descriptions/UzawaReisaQwQ__codex-vmprotect-unpack-skill.md)

## Workflow stack

| Component | Role |
|-----------|------|
| **vmp-lazy-unpack** tracer | Core dynamic trace path for lazy unpack recovery |
| **Python helpers** | PE inventory, import-evidence auditing, run comparison, progress logging |
| **Compatibility shims** | x86 and WinStation adjustments when samples require them |

Version-specific reference notes cover roughly **VMProtect 3.5.0 through 3.10.4** on **x64** and selected **x86** builds. A bundled **C++ sample** protected with VMProtect serves as a training target. (source: wiki/sources/descriptions/UzawaReisaQwQ__codex-vmprotect-unpack-skill.md)

## Audience

Reverse engineers and malware or software-protection researchers studying **packer behavior**, anti-tamper schemes, and practical unpacking on Windows—not a one-click generic deobfuscator. (source: wiki/sources/descriptions/UzawaReisaQwQ__codex-vmprotect-unpack-skill.md)

## Positioning

Listed under Cheat **Fix VMP** as an **LLM unpack workflow** beside devirtualization-oriented [[vmprotect-llm-skill]] and automated unpackers ([[vmprotect-unpacker]], [[vmp-unpacker]], [[vmprotect-3-x-emulator-memory-dumper]], [[vmpunpack]]). Pair successful dumps with static/dynamic devirtualizers such as [[novmp]], [[vmplift]], or [[vmp-devirt]] when SDK-virtualized regions remain.

## Links

- Repo: https://github.com/UzawaReisaQwQ/codex-vmprotect-unpack-skill

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[vmprotect]] · [[vmprotect-llm-skill]] · [[kozdbg]] · [[vmprotect-unpacker]] · [[vmp-unpacker]] · [[vmprotect-3-x-emulator-memory-dumper]] · [[mcp-reverse]]
