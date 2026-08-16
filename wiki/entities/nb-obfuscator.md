---
title: nb_obfuscator
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/cxxrev0to1dev__nb_obfuscator.md
updated: 2026-08-16
confidence: medium
---

# nb_obfuscator

**nb_obfuscator** is a Win32/x64 PE obfuscation framework (Visual Studio solution; C/C++) listed under Anti Cheat → Obfuscation Engine. It disassembles target binaries with Capstone and udis86, applies polymorphic stub / dead-code generation (PSC-Engine integration), and rewrites PE images for anti-RE and signature-evasion research. Mainly useful for anti-cheat engineers and defensive security researchers evaluating obfuscation-engine techniques. (source: wiki/sources/descriptions/cxxrev0to1dev__nb_obfuscator.md)

Useful as a post-compile Windows PE obfuscation reference alongside mutation/CFF tools such as [[alcatraz]] and import-target misdirection such as [[call-obfuscator]] — not a commercial protector or deobfuscator.

## Links

- Repo: https://github.com/cxxrev0to1dev/nb_obfuscator (README: win32/x64 obfuscate framework)

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[alcatraz]] · [[call-obfuscator]] · [[wprotect]] · [[obfuscator]]
