---
title: VMProtect
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__VMProtect.md
  - wiki/sources/descriptions/gmh5225__VMP-Vmp3_64bit_disasm-prerelease-.md
  - wiki/sources/descriptions/milk-analyzer__vmpunpack.md
  - wiki/sources/descriptions/tomhamidi97-arch__vmp-devirtualization-lab.md
  - wiki/sources/descriptions/Lucyferek-nunu__vmp-unpacker.md
  - wiki/sources/descriptions/JonathanSalwan__VMProtect-devirtualization.md
updated: 2026-08-24
confidence: medium
---

# VMProtect

**VM-based code obfuscation** that protects programs by translating native logic into bytecode executed on a software virtual machine. The VM simulates a CPU plus basic hardware components—supporting arithmetic, memory read/write, and I/O device interaction—so protected code runs through an emulated execution environment rather than directly on the host processor. Aimed at game-security researchers and reverse engineers studying offensive protection and **Fix VMP** workflows in the cheat / RE tooling lane. (source: wiki/sources/descriptions/gmh5225__VMProtect.md)

Useful as a reference surface for VM virtualization mechanics alongside open engines such as [[cerberus]] (ChaosVm) and [[nocturne]], and as context for Fix VMP tooling such as [[novmpy]], [[rumba]], [[vmprotect-devirtualization]] (experimental dynamic pure-function devirt; Intel Pin trace + Triton symbolic exec + LLVM IR lift for MBA simplification; JonathanSalwan; source: wiki/sources/descriptions/JonathanSalwan__VMProtect-devirtualization.md), [[vmp-vmp3-64bit-disasm-prerelease-]] (VMP3 x64 bytecode disasm; handler decode; gmh5225; source: wiki/sources/descriptions/gmh5225__VMP-Vmp3_64bit-disasm-prerelease-.md), [[vmpunpack]] (Python sogen emulation to OEP; PE rebuild; no devirt; source: wiki/sources/descriptions/milk-analyzer__vmpunpack.md), [[vmpunpacker]], [[vmp-unpacker]] (C++ dynamic unpacker; Win32 debug attach; PEB/ntdll anti-debug bypass; OEP discovery; mutated IAT rebuild; source: wiki/sources/descriptions/Lucyferek-nunu__vmp-unpacker.md), and [[vmp3-utils]]. Educational Android native-library VMP devirtualization lab [[vmp-devirtualization-lab]] (mini-VM + dispatcher/handler recovery + symbolic lifting; tomhamidi97-arch) complements Windows-centric Fix VMP tooling with a reproducible teaching workflow. (source: wiki/sources/descriptions/tomhamidi97-arch__vmp-devirtualization-lab.md)

## Links

- Repo: https://github.com/gmh5225/VMProtect

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[novmpy]] · [[rumba]] · [[vmprotect-devirtualization]] · [[vmp-devirtualization-lab]] · [[vmp-vmp3-64bit-disasm-prerelease-]] · [[vmpunpack]] · [[vmpunpacker]] · [[vmp-unpacker]] · [[vmp3-utils]] · [[cerberus]] · [[nocturne]]
