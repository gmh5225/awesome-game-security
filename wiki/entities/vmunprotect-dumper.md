---
title: VMUnprotect.Dumper
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/void-stack__VMUnprotect.Dumper.md
updated: 2026-07-19
confidence: medium
---

# VMUnprotect.Dumper

C# tool that dynamically unpacks .NET assemblies protected by VMProtect so analysts can recover a decrypted executable. Loads the target, forces VMProtect’s static constructor to restore methods in memory, then dumps the runtime PE image with AsmResolver while fixing entry point and PE magic fields. Built for .NET Framework 4.7.2 (AsmResolver + Sharprompt); targets VMProtect 3.7.0 and nearby versions. Aimed at reverse engineers and game-security researchers studying VMProtect-protected .NET binaries. (source: wiki/sources/descriptions/void-stack__VMUnprotect.Dumper.md)

Dump/unpack sibling to [[vmunprotect]] (Harmony method instrumentation / anti-debug). Companion surface to other Cheat → Fix VMP research: runtime PE recovery vs symbolic-exec ([[novmpy]]) or VTIL compile demos ([[vmdevirt-vtil]]).

## Links

- Repo: https://github.com/void-stack/VMUnprotect.Dumper

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[vmunprotect]] · [[novmpy]] · [[vmdevirt-vtil]]
