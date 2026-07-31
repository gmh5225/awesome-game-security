---
title: dncil
kind: entity
topics: [reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/mandiant__dncil.md
updated: 2026-07-31
confidence: medium
---

# dncil

Python library from Mandiant for disassembling Common Intermediate Language (CIL) in .NET PE binaries. Parses .NET metadata and method bodies into individual CIL instructions with operand resolution, supporting all CIL opcodes and metadata token resolution. Intended for malware analysts and reverse engineers building automated .NET analysis tools or integrating CIL disassembly into YARA rules and detection pipelines. Listed in the README under **For Unity** — useful for programmatic analysis of Mono-era Unity managed assemblies (`Assembly-CSharp.dll`) where GUI decompilers (dnSpy/ILSpy) are insufficient. (source: wiki/sources/descriptions/mandiant__dncil.md)

## Links

- Repo: https://github.com/mandiant/dncil

## Related

[[mono]] · [[il2cpp]] · [[dotx64dbg]] · [[dotniet]] · [[totalpe2]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
