---
title: obfuscator
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/es3n1n__obfuscator.md
updated: 2026-08-15
confidence: medium
---

# obfuscator

C++ **x86-64 PE binary obfuscator** that applies multiple transformation passes directly to compiled executables—no source access required. Passes include control-flow flattening, junk-code insertion, instruction mutation, import obfuscation, and anti-disassembly tricks. The tool disassembles PE images, transforms at the binary level, and reassembles output. Aimed at software-protection researchers studying post-compilation obfuscation and binary-level code transformation under Anti Cheat → Obfuscation Engine. (source: wiki/sources/descriptions/es3n1n__obfuscator.md)

Useful as a post-compile PE obfuscation reference alongside mutators such as [[alcatraz]] and [[binprotect]]—not a commercial protector or unpacker.

## Links

- Repo: https://github.com/es3n1n/obfuscator

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[control-flow-flattening]] · [[alcatraz]] · [[binprotect]] · [[perses]] · [[idadeflat]]
