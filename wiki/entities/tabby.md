---
title: tabby
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/cocomelonc__tabby.md
updated: 2026-08-17
confidence: medium
---

# tabby

Minimal **position-independent shellcode micro-framework** for Windows x64 that lets developers write shellcode in **C** (not hand-written assembly) and compile on **Linux** with mingw-w64 and NASM into a flat raw `.bin` ready for process injection. Output has no PE header, import table, or CRT; APIs resolve at runtime via PEB and export-table walks keyed by **FNV-1a hashes**. **Indirect NT syscalls** jump into ntdll gadgets so call stacks look legitimate to call-stack-aware EDR/AC products. Designed as a teaching scaffold for ethical malware development and offensive security training—base-address recovery, hash-based API resolution, and SSN extraction are exposed in roughly 500 lines of readable C and assembly. (source: wiki/sources/descriptions/cocomelonc__tabby.md)

Complements other Windows shellcode build frameworks such as [[scfw]] and [[shellcode-factory]], object-to-shellcode tooling such as [[obj2shellcode]], and indirect-syscall loaders such as [[tartarus-tp-alloc-inject]]. Cross-links [[stack-spoofing]] and [[windows-process-injection]] for call-stack and injection context.

## Links

- Repo: https://github.com/cocomelonc/tabby

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[scfw]] · [[shellcode-factory]] · [[obj2shellcode]] · [[tartarus-tp-alloc-inject]] · [[stack-spoofing]] · [[windows-process-injection]]
