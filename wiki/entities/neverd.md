---
title: NeverD
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/NeverSight__NeverD.md
updated: 2026-08-22
confidence: medium
---

# NeverD

**Native binary analysis and decompilation engine** from NeverSight that performs **one-to-one instruction-level lifting** of compiled executables with the goal of full semantic fidelity. Written primarily in **C++20** and exposed through a pure **C API** (`libneverd`), it loads **PE**, **ELF**, and **Mach-O** binaries across **x86-64**, **i386**, **AArch64**, and **ARM32**, decoding with **Capstone** and lifting through a four-stage IR pipeline built on a custom **LLVM** fork. A single pipeline supports lifting to **LLVM IR**, decompiling to structured **C**, or rewriting machine code in place; **strict mode** rejects unsupported instructions rather than silently guessing. The toolkit includes a unified CLI for disassembly, CFG analysis, signature matching, and binary patching, plus plugin support and **JSON-oriented output** suited to automation and AI-assisted reverse engineering workflows. Targets researchers, integrators, and security practitioners analyzing native code for malware triage, vulnerability research, and game or anti-cheat reverse engineering. (source: wiki/sources/descriptions/NeverSight__NeverD.md)

Complements Ghidra-derived peers [[enigma]] and [[kuna]] by offering a Capstone→LLVM lifting stack with in-place binary rewrite and embeddable `libneverd` for pipelines that need deterministic IR or structured C without a JVM. Bundled in [[re-harness]] as a Hex-Rays fallback lift→O3→redecompile path for LLM-assisted PE static analysis.

## Links

- Repo: https://github.com/NeverSight/NeverD

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[enigma]] · [[kuna]] · [[retdec]] · [[ida2llvm]] · [[re-harness]] · [[decbench]] · [[hyperion-disassembler]]
