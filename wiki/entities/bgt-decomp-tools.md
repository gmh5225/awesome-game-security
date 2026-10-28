---
title: bgt-decomp-tools
kind: entity
topics: [reverse-engineering, game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/KamiKitsune420__bgt-decomp-tools.md
  - wiki/sources/README-categories.md
updated: 2026-10-28
confidence: medium
---

# bgt-decomp-tools

Python toolkit (KamiKitsune420) to recover **AngelScript** source structure, bytecode, strings, and asset packs from Windows executables built with the **BlastBay Gaming Toolkit (BGT)** or its open-source successor **NVGT**—common hosts for blind/accessible audio games. The goal is **title-agnostic, reproducible decompilation** of stock BGT/NVGT binaries without per-game manual RE. (source: wiki/sources/descriptions/KamiKitsune420__bgt-decomp-tools.md)

## Extraction pipeline

Automated chain from shipped PEs:

1. **PE overlay** discovery and parsing.
2. **AES-256-CBC** decryption and **LZ77** decompression of embedded packs.
3. **Disassembly and lift** of AngelScript modules via engine-specific readers that **trial-decrypt** and apply **self-verifying format checks** to adapt when pack layouts differ.

Companion modules cover **NVGT** decompilation and library recovery, **UPX** runtime unpacking for opcode-table extraction, optional **Ghidra headless** workflows to extend readers from shipped binaries, and both **CLI** and **screen-reader-friendly GUI** entry points.

## Audience and scope

Targets reverse engineers, accessibility-game researchers, and preservationists studying proprietary script hosts—not live anti-cheat bypass tooling. Listed under **Cheat** / RE Tools beside bytecode and script decompilers such as [[luadecompiler]] and engine-specific decomp tracks like [[fs15-reconstruction]].

## Links

- Repo: https://github.com/KamiKitsune420/bgt-decomp-tools

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[static-runtime-evidence]] · [[ghidra]] · [[luadecompiler]] · [[fs15-reconstruction]]
