---
title: import-kallsyms
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/XMCVE__import-kallsyms.md
updated: 2026-08-19
confidence: medium
---

# import-kallsyms

IDA Pro plugin (Python; XMCVE; cheat / IDA Plugins) that imports **Linux kernel symbols** from a **kallsyms dump** into the current IDA database. Maps symbol names and addresses into the disassembler so stripped or partially symbolized kernel images regain navigable function and data labels. Restores symbol context to speed static analysis for kernel reverse engineers and vulnerability researchers. (source: wiki/sources/descriptions/XMCVE__import-kallsyms.md)

Complements live `/proc/kallsyms` rename via [[ida-kallsyms-symbol-renamer]] and offline symbol recovery via [[vmlinux-to-elf]] when working from a saved kallsyms text dump rather than a live host.

## Links

- Repo: https://github.com/XMCVE/import-kallsyms

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-kallsyms-symbol-renamer]] · [[vmlinux-to-elf]] · [[idaplugins]]
