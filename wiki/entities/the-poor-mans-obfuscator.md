---
title: the-poor-mans-obfuscator
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/romainthomas__the-poor-mans-obfuscator.md
updated: 2026-07-24
confidence: medium
---

# the-poor-mans-obfuscator

Lightweight LLVM-based code obfuscator that applies instruction substitution, control-flow flattening, and string encryption as C++ optimization passes on LLVM IR. Language- and architecture-independent via the IR pipeline; integrates into standard build workflows for ELF/Mach-O protection research. Aimed at studying basic obfuscation transformations as compiler passes—not a commercial protector. (source: wiki/sources/descriptions/romainthomas__the-poor-mans-obfuscator.md)

Useful as a minimal OLLVM-style Obfuscation Engine reference alongside fuller pass-plugins such as [[kagura]] and post-compile tools such as [[alcatraz]].

## Links

- Repo: https://github.com/romainthomas/the-poor-mans-obfuscator

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[kagura]] · [[alcatraz]] · [[wprotect]] · [[idadeflat]] · [[deobf]]
