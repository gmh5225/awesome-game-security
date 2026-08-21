---
title: UnSign
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/SV-Foster__UnSign.md
updated: 2026-08-21
confidence: medium
---

# UnSign

Command-line utility that removes Authenticode signatures from Windows PE/COFF executables (EXE, DLL, SYS). Implemented in C with 32-bit and 64-bit builds plus Visual Studio project files. Strips signature-related data and handles PE header edge cases that can block clean re-signing workflows. Aimed at reverse engineering, malware analysis, and software security testing that needs unsigned binary manipulation. (source: wiki/sources/descriptions/SV-Foster__UnSign.md)

Complements the signature-transplant lane ([[sigthief]], [[stealing-signatures]], [[signature-kid]]) by removing existing `WIN_CERTIFICATE` / security-directory blobs instead of copying or forging them—useful when analysts need a truly unsigned baseline before patch-and-resign or verifier testing.

## Links

- Repo: https://github.com/SV-Foster/UnSign

## Related

[[sigthief]] · [[stealing-signatures]] · [[sigflip]] · [[pesign-analyzer]] · [[pedigest]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
