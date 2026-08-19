---
title: ghidra-nativeaot
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Washi1337__ghidra-nativeaot.md
updated: 2026-08-19
confidence: medium
---

# ghidra-nativeaot

**ghidra-nativeaot** (Washi1337) is a **Ghidra analyzer and UI plugin** for reverse engineering **.NET Native AOT** binaries (.NET 8+), especially when symbols are missing and FunctionID databases are hard to build. Implemented mainly in **Java** as a Ghidra extension, it reconstructs **full type hierarchies** from method tables, annotates **frozen objects** such as string literals, and detects **vtable redirections**. It locates **ReadyToRun metadata** via symbols or heuristic signature scanning so analysts can recover structure from stripped Native AOT executables. An interactive **metadata browser** and **refactoring engine** support renaming virtual methods and related symbols. Primary use cases are malware analysis, CTF challenges, and security research on Native AOT programs in Ghidra. (source: wiki/sources/descriptions/Washi1337__ghidra-nativeaot.md)

Complements IDA-side Native AOT recovery such as [[dotniet]] and Ghidra language-specific plugins such as [[delphiresym]] and [[ghidra-cpp-class-analyzer]] when targets compile managed .NET to ahead-of-time native code instead of conventional IL assemblies.

## Links

- Repo: https://github.com/Washi1337/ghidra-nativeaot

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[dotniet]] · [[delphiresym]] · [[ghidra-cpp-class-analyzer]] · [[research-rigor]]
