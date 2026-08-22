---
title: Il2CppDumper
kind: entity
topics: [game-engine, reverse-engineering, game-hacking, mobile-security]
sources:
  - wiki/sources/descriptions/Perfare__Il2CppDumper.md
updated: 2026-08-22
confidence: high
---

# Il2CppDumper

Canonical C# [[il2cpp]] reverse-engineering utility for Unity IL2CPP binaries and metadata. Parses IL2CPP executables plus `global-metadata.dat` across ELF, Mach-O, PE, NSO, and WASM on a broad range of Unity versions. Reconstructs dummy DLL metadata and emits analyst outputs — `dump.cs`, structure headers, and helper scripts for IDA, Ghidra, and Binary Ninja — for static analysis and protection research. README lane `[Il2Cpp Dump]`. (source: wiki/sources/descriptions/Perfare__Il2CppDumper.md)

Upstream for many forks and adaptations including [[il2cppdumpdroidgui]], [[il2cpp-pdb]], [[il2cppdumper-yuanshen]], and [[zygisk-il2cppdumper]] (same Perfare author). Complements cross-platform [[il2cpp-inspector]] and live harvesters such as [[frida-il2cpp-bridge]]; Android-native static fork [[il2cppdumper-kp7742]] targets mobile `.so` workflows.

## Links

- Repo: https://github.com/Perfare/Il2CppDumper

## Related

[[il2cpp]] · [[il2cpp-inspector]] · [[il2cpp-pdb]] · [[il2cppdumpdroidgui]] · [[zygisk-il2cppdumper]] · [[il2cppdumper-kp7742]] · [[frida-il2cpp-bridge]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[overviews/mobile-security]]
