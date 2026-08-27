---
title: IDA-For-Delphi
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Coldzer0__IDA-For-Delphi.md
updated: 2026-08-27
confidence: medium
---

# IDA-For-Delphi

**IDAPython script** (Coldzer0) that **recovers Delphi function names** from **event constructor patterns** during reverse engineering. Written in Python for **IDA Pro** with **64-bit** support. Intended to run in a **live debugging session** so symbols resolve from runtime context—useful when static metadata is sparse but event wiring is visible at runtime. Targets analysts reversing **Delphi binaries** in malware analysis, legacy software RE, and game clients or cheat tooling shipped as Object Pascal PEs. (source: wiki/sources/descriptions/Coldzer0__IDA-For-Delphi.md)

Complements metadata-driven recovery such as [[delphi-helper]] (IDA) and [[delphiresym]] (Ghidra) when event-handler naming must be inferred from runtime constructor patterns rather than embedded compiler symbols.

## Links

- Repo: https://github.com/Coldzer0/IDA-For-Delphi

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[delphi-helper]] · [[delphiresym]] · [[luadecompiler]] · [[ce-remap-plugin]] · [[magicmida-rs]]
