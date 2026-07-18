---
title: Alcatraz
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/weak1337__Alcatraz.md
updated: 2026-07-18
confidence: medium
---

# Alcatraz

x64 PE binary obfuscator with an ImGui GUI. Applies instruction mutation (MOV/ADD/LEA equivalents), control-flow flattening (dispatcher state machines), anti-disassembly junk, IAT obfuscation, and custom entry-point redirection. Built on Zydis + AsmJit; parses PE sections and PDB symbols, transforms at instruction level, and reassembles while preserving relocations/imports. Aimed at PE-level obfuscation research and AC binary-protection evaluation under Anti Cheat → Obfuscation Engine / Anti Disassembly. (source: wiki/sources/descriptions/weak1337__Alcatraz.md)

Useful as a post-compile PE obfuscation reference alongside packers and compile-time libraries—not a commercial protector or unpacker.

## Links

- Repo: https://github.com/weak1337/Alcatraz

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[wprotect]] · [[obfusk8]] · [[shredder-rs]] · [[2pack]] · [[idadeflat]]
