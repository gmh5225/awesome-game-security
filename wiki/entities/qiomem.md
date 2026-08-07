---
title: qiomem
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__qiomem.md
updated: 2026-08-07
confidence: medium
---

# qiomem

BYOVD research PoC exploiting the Qualcomm **QCI0701** ACPI driver **`QIOMem.sys`**. The tool registers a virtual software device and issues IOCTLs through the signed driver to obtain physical memory read/write primitives—typical ring-0 building blocks for unsigned driver load, kernel structure patching, or anti-cheat bypass research on Qualcomm ACPI-equipped hosts. (source: wiki/sources/descriptions/gmh5225__qiomem.md)

## Links

- Repo: https://github.com/gmh5225/qiomem

## Related

[[byovd]] · [[physmem-drivers]] · [[s4killer]] · [[razer-rzctl]] · [[vdk]] · [[loldrivers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
