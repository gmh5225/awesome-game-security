---
title: Ghidra VxD Tools
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/andrew-hoffman__ghidra-vxd-tools.md
updated: 2026-08-18
confidence: medium
---

# Ghidra VxD Tools

Ghidra Jython scripts that improve disassembly and annotation of Windows 9x VxD (Virtual Device Driver) binaries. The main script scans for `INT 20h` VxD call sequences, replaces raw bytes with a typed `VxDCall` structure, and adds human-readable labels and comments by decoding VxD and service IDs against a large database derived from VMDisp9x `vmm.h`. It also handles special inline payloads such as debug strings and flag words for common VMM debug services. (source: wiki/sources/descriptions/andrew-hoffman__ghidra-vxd-tools.md)

Written in Jython using the Ghidra API; installs into the Ghidra script manager under the **Windows9x** category. Targets reverse engineers and security researchers analyzing legacy Windows 9x kernel-mode drivers, including historical game protection and anti-cheat components.

## Links

- Repo: https://github.com/andrew-hoffman/ghidra-vxd-tools

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[ghidra]] · [[ghidra-scripts]] · [[winnt5-src-20201004]]
