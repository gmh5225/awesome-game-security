---
title: NoVmp
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/can1357__NoVmp.md
updated: 2026-08-17
confidence: medium
---

# NoVmp

C++ static devirtualizer for VMProtect x64 3.x PE binaries. Scans for VMENTER-style control transfers, models VMProtect VM architecture and opcodes, and lifts virtualized handlers into VTIL (VTIL-Core) for deobfuscation and optimization. Builds with CMake or Visual Studio; depends on VTIL-Core (Capstone, Keystone) and linux-pe for PE parsing. CLI can target specific VMs, override image base, strip constant obfuscation, and optionally attempt experimental recompilation. Aimed at reverse engineers and game-security researchers undoing VMProtect-style code virtualization. (source: wiki/sources/descriptions/can1357__NoVmp.md)

Companion surface to [[novmpy]] (Python/Triton symbolic handler recovery) and [[vmdevirt-vtil]] (VTIL compile demo): production-oriented static lift via VTIL rather than trace/symbolic exec or broken compile paths.

## Links

- Repo: https://github.com/can1357/NoVmp

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[novmpy]] · [[vmdevirt-vtil]] · [[rumba]] · [[vmattack]] · [[vmprotect]]
