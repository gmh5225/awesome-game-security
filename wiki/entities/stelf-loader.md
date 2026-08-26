---
title: stelf-loader
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/DavidBuchanan314__stelf-loader.md
updated: 2026-08-26
confidence: medium
---

# stelf-loader

**stelf-loader** is a research toolchain that converts Linux **x64 ELF executables** into **self-loading shell scripts**. Python tooling plus generated **NASM shellcode** maps executable segments, restores memory protections, and jumps to the original entry point from a script-driven loader path. Output supports compressed payloads, base64 transport, raw entry execution modes, and compact one-liner generation. Primary audience: exploit-development research, payload-delivery experiments, and studying ELF runtime loading behavior under Anti Cheat → Binary Packer / `[ELF]`. (source: wiki/sources/descriptions/DavidBuchanan314__stelf-loader.md)

Differs from full dynamic-linker replacements such as [[sloader]] by wrapping a static ELF in a transportable shell script rather than replacing glibc `ld-linux.so`. Complements in-memory packers such as [[harmless]] and stub-based packers such as [[elfpacker]] with a script-carried loader that reimplements segment mapping and `mprotect` restoration in user-controlled shellcode.

## Links

- Repo: https://github.com/DavidBuchanan314/stelf-loader

## Related

[[sloader]] · [[harmless]] · [[elfpacker]] · [[mojoelf]] · [[elfuck]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
