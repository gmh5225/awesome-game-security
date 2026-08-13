---
title: EAC-VmCheck.asm
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__EAC-VmCheck.asm.md
updated: 2026-08-13
confidence: medium
---

# EAC-VmCheck.asm

Tiny assembly extraction of [[easy-anti-cheat]] **virtual-machine detection** logic recovered from `easyanticheat.sys` (gmh5225). The archived README notes it was pulled from the driver's `vm` directory; `vmCheck.asm` exposes a `CheckVM` routine that calls an `ExecVMREAD` helper issuing **VMREAD** and branching on the result to separate VM-found vs VM-not-found paths. Not a framework—value is preserving the exact low-level control flow of EAC's VM detection for offline reanalysis. (source: wiki/sources/descriptions/gmh5225__EAC-VmCheck.asm.md)

Useful alongside driver decompile dumps such as [[easyanticheat-reversing]] and reversed-source archives such as [[eazy-anti-cheat-src]] when studying EAC virtualization checks and VMREAD-based probing. README category: Virtual machine checking.

## Links

- Repo: https://github.com/gmh5225/EAC-VmCheck.asm

## Related

[[easy-anti-cheat]] · [[eac]] · [[easyanticheat-reversing]] · [[eazy-anti-cheat-src]] · [[eac-shellcode-1]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
