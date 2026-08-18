---
title: exe_packer
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/andrew9382__exe_packer.md
updated: 2026-08-18
confidence: medium
---

# exe_packer

C/C++ Windows executable packer that rebuilds PE files with a custom unpacking stub. Compresses the original binary with Huffman coding, stores the payload in a dedicated section, and emits a loader-oriented image. The stub resolves low-level NTDLL and KERNEL32 APIs, decrypts import-name data, maps sections, applies relocations, fixes imports, and jumps to the original entry point. Visual Studio projects target both x86 and x64 PE internals—aimed at reverse-engineering research, packer analysis, and understanding anti-analysis loaders in game security contexts. (source: wiki/sources/descriptions/andrew9382__exe_packer.md)

Useful as an educational x86/x64 PE packer reference alongside [[pe-packer]], [[x64-exe-packer]], and [[pepacker]]—not a full unpacker or commercial protector.

## Links

- Repo: https://github.com/andrew9382/exe_packer

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[pe-packer]] · [[x64-exe-packer]] · [[pepacker]] · [[atom-pe-packer]] · [[packer-tutorial]] · [[unpacker]] · [[awesome-executable-packing]]
