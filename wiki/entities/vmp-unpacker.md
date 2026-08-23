---
title: vmp-unpacker
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Lucyferek-nunu__vmp-unpacker.md
updated: 2026-08-23
confidence: medium
---

# vmp-unpacker

Windows **C++ dynamic unpacker** for VMProtect-protected PE executables and DLLs. Launches or attaches to a protected process under the Win32 debugger API, bypasses common VMProtect anti-debug checks by patching the PEB and hooking ntdll routines, and discovers the original entry point (OEP) via text-section guards, timed snapshots, or manual triggers. After suspending the process, it dumps decrypted memory to a new PE file, reconstructs standard and mutated IAT call sites, and can resolve obfuscated imports dynamically or via passive attach without debugger APIs. Aimed at reverse engineers and security researchers analyzing VMProtect-packed software, including games and other protected binaries. (source: wiki/sources/descriptions/Lucyferek-nunu__vmp-unpacker.md)

Complements LZMA-based static unpack via [[vmpunpacker]], Python sogen emulation via [[vmpunpack]], and Go static rebuild via [[vmpstatic]] by offering debugger-driven OEP discovery with PEB/ntdll anti-debug bypass and mutated IAT reconstruction. Pair unpacked output with Fix VMP devirt tooling such as [[novmpy]], [[titan]], or [[vmp-vmp3-64bit-disasm-prerelease-]] when virtualized functions remain.

## Links

- Repo: https://github.com/Lucyferek-nunu/vmp-unpacker

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[vmprotect]] · [[vmpunpacker]] · [[vmpunpack]] · [[vmpstatic]] · [[unpacker]] · [[vmpimportfixer]]
