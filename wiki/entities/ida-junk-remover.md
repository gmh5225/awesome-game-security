---
title: IDA Junk Remover
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/b2tmy__ida-junk-remover.md
updated: 2026-11-23
confidence: medium
---

# IDA Junk Remover

**IDA Junk Remover** (b2tmy) is a single-file **Python IDAPython** plugin for **IDA Pro 7.4–9.x** that automatically detects and repairs **junk-code obfuscation** that breaks disassembly and **Hex-Rays** decompilation on **x86** code. It recognizes patterns such as jumps landing inside another instruction, overlapping instructions, dead self-jumps, constant-folded conditional branches, and call-pop EIP tricks, with optional **dry-run preview** before applying fixes. Repairs undefine bogus bytes and rebuild analysis in the **IDB** rather than patching the on-disk binary; an optional mode can rewrite constant-condition jumps in the database. Mock-based unit tests and a demo sample generator support validation without a live IDA session. Aimed at reverse engineers and malware or game-security analysts working through packer-style byte-level obfuscation on protected executables. (source: wiki/sources/descriptions/b2tmy__ida-junk-remover.md)

Complements CFG-oriented IDA deobfuscation such as [[idadeflat]] and in-debugger disassembly cleanup such as [[codecleaner]]—focused on **byte-level junk** that corrupts linear disassembly rather than CFF deflattening or trace-call noise cleanup via [[ida-wpp-remover]].

## Links

- Repo: https://github.com/b2tmy/ida-junk-remover

## Related

[[idadeflat]] · [[codecleaner]] · [[ida-wpp-remover]] · [[d810]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]