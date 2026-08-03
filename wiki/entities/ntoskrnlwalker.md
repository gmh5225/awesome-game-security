---
title: ntoskrnlwalker
kind: entity
topics: [windows-kernel, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/jsacco__ntoskrnlwalker.md
updated: 2026-08-02
confidence: medium
---

# ntoskrnlwalker

User-mode tooling to **resolve offsets, ROP gadgets, and symbols from `ntoskrnl`** for a specific Windows build. Speeds up kernel structure navigation, gadget discovery, and offset lookup so cheat / RE workflows spend less time on hardcoded build-specific values. (source: wiki/sources/descriptions/jsacco__ntoskrnlwalker.md)

Complements the manual symbol-walking workflow in [[overviews/windows-kernel]] (dbghelp + Microsoft symbol server, struct field queries, executable-section gadget scans) and bulk PDB prefetch via [[pdblister]]. Embeddable library form: [[ntkernelwalkerlib]] (same dbghelp + executable-section gadget scan lane). Pair with [[ntsleuth]] for usermode syscall-table extraction and [[pdb-rs]] / [[pdb]] for programmatic PDB parsing—not a live kernel debugger.

## Links

- Repo: https://github.com/jsacco/ntoskrnlwalker

## Related

[[ntkernelwalkerlib]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[pdblister]] · [[ntsleuth]] · [[pdb-rs]] · [[pdb]] · [[kpdb]] · [[research-rigor]]
