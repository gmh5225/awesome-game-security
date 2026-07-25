---
title: Smep-Bypass
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/r0keb__Smep-Bypass.md
updated: 2026-07-25
confidence: medium
---

# Smep-Bypass

Windows kernel PoC for bypassing SMEP (Supervisor Mode Execution Prevention). SMEP blocks the kernel from executing user-mode pages; this research shows disabling it via CR4 manipulation through ROP chains or vulnerable-driver primitives so kernel mode can run user-space shellcode. Aimed at kernel-exploitation researchers studying hardware security-feature bypasses. (source: wiki/sources/descriptions/r0keb__Smep-Bypass.md)

## Links

- Repo: https://github.com/r0keb/Smep-Bypass

## Related

[[byovd]] · [[hvci]] · [[windows-kernel-exploits]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
