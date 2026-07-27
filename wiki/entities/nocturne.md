---
title: Nocturne
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/nodiuus__nocturne.md
updated: 2026-07-27
confidence: medium
---

# Nocturne

Bin2bin **x86-64 PE code virtualizer / binary rewriter** that translates native instructions into custom VM bytecode. Features polymorphic handlers (30+), junk-code insertion, register mapping, PDB-guided function selection, SDK markers for protected regions, and PE section rewriting. Aimed at obfuscation-engine / anti-disassembly research under Anti Cheat → Obfuscation Engine. (source: wiki/sources/descriptions/nodiuus__nocturne.md)

Useful as an open virtualization-obfuscation reference alongside PE mutators such as [[alcatraz]] and commercial-style protectors such as [[vxlang-page]] — distinct from the unrelated shellcode loader [[nocturneldr]].

## Links

- Repo: https://github.com/nodiuus/nocturne

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[alcatraz]] · [[vxlang-page]] · [[wprotect]] · [[novmpy]] · [[vmpunpacker]]
