---
title: Benowin Blanc (bb)
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/cristeigabriela__bb.md
updated: 2026-08-16
confidence: medium
---

# Benowin Blanc (bb)

**Benowin Blanc** parses Windows SDK and community **PHNT** (Process Hacker NT headers) via **libclang** to expose struct layouts, enums, and constants—WinDbg `dt`-like introspection without attaching a debugger. Ships CLI + TUI interfaces and JSON export for scripting. (source: wiki/sources/descriptions/cristeigabriela__bb.md)

PHNT documents internal NT structures Microsoft does not publish; this tool makes those headers queryable offline for game-security researchers and reverse engineers working in cheat / Windows kernel explorer workflows.

## Links

- Repo: https://github.com/cristeigabriela/bb

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[ntoskrnlwalker]] · [[ntkernelwalkerlib]] · [[windiff]] · [[windbg-scripts]] · [[systeminformer]]
