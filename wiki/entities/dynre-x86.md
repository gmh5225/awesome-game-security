---
title: dynre-x86
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/aroxby__dynre-x86.md
updated: 2026-08-18
confidence: medium
---

# dynre-x86

Early experimental C++ codebase for learning **dynamic recompilation** on x86. Uses the **Zydis** disassembly library to decode instruction streams, print mnemonics, and inspect operand details. Includes Makefile and Dockerfile build setup plus helper tables for register-name mapping. Targets educational reverse-engineering practice for instruction decoding and binary-translation pipeline study—not a production JIT or emulator. (source: wiki/sources/descriptions/aroxby__dynre-x86.md)

Sits upstream of full translators such as [[levo]] and console recompilers such as [[recompiler]] as a minimal decode-and-inspect stepping stone in the x86 binary-translation lane.

## Links

- Repo: https://github.com/aroxby/dynre-x86

## Related

[[levo]] · [[recompiler]] · [[ispras-qemu]] · [[kn-live-dbg]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
