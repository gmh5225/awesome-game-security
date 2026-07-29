---
title: levo
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/momo5502__levo.md
updated: 2026-07-29
confidence: medium
---

# levo

Experimental ahead-of-time (AOT) binary translator for x86/x64 PE executables: exports control-flow graphs from Ghidra, lifts machine code to LLVM IR (Intel XED disassembly; README also tags Remill lifting), and recompiles to native code with the LLVM backend. Ships a PE mapper plus a runtime that intercepts `kernel32` API calls so translated binaries can execute on the host OS. (source: wiki/sources/descriptions/momo5502__levo.md)

Complements emulation-first Windows PE runners such as [[sogen]] and [[winvisor]] with a lift-and-recompile path for studying closed PE game clients without full instruction emulation.

## Links

- Repo: https://github.com/momo5502/levo (README tag: AOT binary translation — control flow recovery with Ghidra, lifting with Remill, recompilation with LLVM)

## Related

[[sogen]] · [[winvisor]] · [[recompiler]] · [[patch-finder]] · [[vmtrace]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
