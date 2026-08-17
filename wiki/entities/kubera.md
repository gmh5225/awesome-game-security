---
title: KUBERA
kind: entity
topics: [reverse-engineering, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/binsnake__KUBERA.md
updated: 2026-08-17
confidence: medium
---

# KUBERA

**KUBERA** is a **platform-independent x86 environment emulator** for **Windows user-mode and kernel-mode binaries**, designed for research. It targets game-security researchers and reverse engineers studying offensive techniques in the **cheat / dynamic binary instrumentation** space — useful for sandboxed PE and driver analysis without a full Windows host. (source: wiki/sources/descriptions/binsnake__KUBERA.md)

Spans both usermode PE and kernel-driver emulation — distinct from WHP-hosted [[winvisor]], Unicorn peers such as [[emulator]] / [[sogen]], and RING3 driver sandboxes such as [[kace]] that focus on kernel drivers only. Complements binsnake ARM64 decode tooling such as [[farm64]] on the instruction-analysis side.

## Links

- Repo: https://github.com/binsnake/KUBERA

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[dynamic-binary-instrumentation]] · [[winvisor]] · [[kace]] · [[emulator]] · [[farm64]]
