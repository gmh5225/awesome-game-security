---
title: cfgdump
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/JKornev__cfgdump.md
updated: 2026-08-24
confidence: medium
---

# cfgdump

**WinDbg extension** for inspecting **Control Flow Guard (CFG) coverage** in a process address space (JKornev). The C++ implementation provides commands to **print CFG maps**, **query specific address ranges**, and **list protected regions**—helping analysts see which memory areas are guarded by CFG bits and how those protections are laid out. Useful for **exploit development research**, **binary hardening validation**, and **low-level Windows debugging** workflows. (source: wiki/sources/descriptions/JKornev__cfgdump.md)

Complements defensive CFG bitmap inconsistency scanners such as [[cfg-find-hidden-shellcode]] on the detection side and live-debugger XFG visualization such as [[x64dbg-xfg-marker]] when studying forward-edge control-flow integrity metadata.

## Links

- Repo: https://github.com/JKornev/cfgdump

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[cfg-find-hidden-shellcode]] · [[x64dbg-xfg-marker]] · [[cet-research]] · [[hidden]] · [[awesome-windbg-extensions]]
