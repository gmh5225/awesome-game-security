---
title: NTKernelWalkerLib
kind: entity
topics: [windows-kernel, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/jsacco__NTKernelWalkerLib.md
updated: 2026-08-03
confidence: medium
---

# NTKernelWalkerLib

User-mode **library** for resolving `ntoskrnl` **symbol RVAs**, **struct field offsets**, and **short ROP gadgets** (e.g. `pop rcx ; ret`, `jmp rax`) for a target Windows build. Uses dbghelp against exported symbols from local `ntoskrnl.exe` and an image mapper that scans executable sections for gadget primitives — the embeddable counterpart to standalone tooling like [[ntoskrnlwalker]]. (source: wiki/sources/descriptions/jsacco__NTKernelWalkerLib.md)

Useful for game-security researchers and reverse engineers studying offensive kernel-explorer / cheat workflows who want programmatic offset and gadget resolution without hardcoded build-specific values. Complements [[overviews/windows-kernel]] symbol-walking guidance, bulk PDB prefetch via [[pdblister]], and syscall-table extraction via [[ntsleuth]].

## Links

- Repo: https://github.com/jsacco/NTKernelWalkerLib

## Related

[[ntoskrnlwalker]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[pdblister]] · [[ntsleuth]] · [[pdb-rs]] · [[pdb]] · [[research-rigor]]
