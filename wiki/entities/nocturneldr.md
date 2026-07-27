---
title: NocturneLdr
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/xec412__NocturneLdr.md
updated: 2026-07-27
confidence: medium
---

# NocturneLdr

Research-oriented Windows x64 **shellcode loader** (C++20 + MASM) that aims for clean, fully backed call stacks indistinguishable from legitimate Windows threads under EDR/forensic inspection. CRT-free with PEB-based API resolution via compile-time DJB2 hashing and benign USER32 IAT camouflage. (source: wiki/sources/descriptions/xec412__NocturneLdr.md)

Core technique is **CET-compatible stack spoofing**: inject into a signed module (e.g. `windows.storage.dll`) code cave, register donor unwind metadata (`RtlAddFunctionTable` / inverted function-table collapse) so software stack walks and Intel CET shadow stacks both validate. Also includes Zilean sleep obfuscation (ROP image encrypt + stack duplication), heap masking, and EAF bypass via ntdll gadget reads (`ShieldedRead`). Useful alongside simpler spoof samples such as [[return-address-spoofer]] / [[loudsunrun]] when modeling `Cheat > Spoof Stack` vs `Detection:Spoof Stack` and CET baselines such as [[cet-research]].

## Links

- Repo: https://github.com/xec412/NocturneLdr

## Related

[[return-address-spoofer]] · [[loudsunrun]] · [[cet-research]] · [[scfw]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
