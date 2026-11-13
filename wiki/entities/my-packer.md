---
title: my-packer
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/oldccat66__my-packer.md
updated: 2026-11-13
confidence: medium
---

# my-packer

Windows x64 command-line PE protector (my-vmp) that hardens executables and emits a new protected binary. Protection is driven by TOML project files with optional Lua hooks for compile-time scripting, offering per-procedure modes such as virtualization, mutation, and ultra plus tuning for segments, resources, and imports. Embedded resources can be compressed with LZMA or Zstandard; the toolchain supports licensing parameters, watermarks, build dates, and license-manager configuration. Documented virtualization and kernel-debugger-related options ship with release binaries and `USAGE.md`. Listed under Anti Cheat → Binary Packer (`[PE X64]`); aimed at developers studying client-side obfuscation and anti-tamper hardening on authorized software, including game-security and reverse-engineering defense research. (source: wiki/sources/descriptions/oldccat66__my-packer.md)

Useful as a VMProtect-style x64 PE protection reference alongside [[hm-pe-packer]], [[pe-protector]], and [[atom-pe-packer]]—complement Fix VMP / unpack lanes such as [[vmprotect-unpacker]] and [[codex-vmprotect-unpack-skill]], not a commercial AC product.

## Links

- Repo: https://github.com/oldccat66/my-packer

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[hm-pe-packer]] · [[pe-protector]] · [[atom-pe-packer]] · [[x64-exe-packer]] · [[vmprotect-llm-skill]] · [[codex-vmprotect-unpack-skill]]
