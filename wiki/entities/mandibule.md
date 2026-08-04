---
title: mandibule
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/ixty__mandibule.md
updated: 2026-08-04
confidence: medium
---

# mandibule

Linux **ptrace** process injector that loads and runs arbitrary **ELF** binaries inside a live target process. The C codebase includes a minimal C runtime (**icrt**) with raw syscall wrappers, ELF loading and relocation, fake stack construction, and shellcode argument passing for position-independent injection payloads — aimed at Linux security researchers studying ptrace injection and runtime ELF loading. (source: wiki/sources/descriptions/ixty__mandibule.md)

Contrasts with Windows injection collections such as [[windows-process-injection]] and Android attach-and-inject tooling such as [[android-ptrace-injector]]; complements Linux live-memory workflows ([[pince]], [[procmap]]) and Wine-focused [[ptrace-read-teb]].

## Links

- Repo: https://github.com/ixty/mandibule

## Related

[[windows-process-injection]] · [[android-ptrace-injector]] · [[ptrace-read-teb]] · [[pince]] · [[procmap]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
