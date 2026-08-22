---
title: DeObfBR
kind: entity
topics: [reverse-engineering, mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/Mrack__DeObfBR.md
updated: 2026-08-22
confidence: medium
---

# DeObfBR

Python tool for deobfuscating **ARM64 branch-obfuscated** code in shared libraries (ELF `.so`). Uses Unicorn CPU emulation with Capstone disassembly, Keystone assembly, and ELF parsing to analyze obfuscated control flow, accept function start/end addresses, process protected regions, and write reconstructed output binaries. Primary use case: reverse engineering and malware or game-protection analysis on Android native libraries. README tags `libtprt.so`. (source: wiki/sources/descriptions/Mrack__DeObfBR.md)

## Links

- Repo: https://github.com/Mrack/DeObfBR

## Related

[[deobf]] · [[dfm-android-unicorn]] · [[memdetection]] · [[control-flow-flattening]] · [[overviews/reverse-engineering]] · [[overviews/mobile-security]]
