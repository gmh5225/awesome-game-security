---
title: DelphiReSym
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/WenzWenzWenz__DelphiReSym.md
updated: 2026-08-19
confidence: medium
---

# DelphiReSym

**DelphiReSym** (WenzWenzWenz) is a **Ghidra-oriented Delphi symbol recovery tool** for reverse engineers. Implemented as a **Python script for pyghidra**, it reconstructs **qualified function signatures**, **parameter metadata**, and **virtual-table context** from embedded Delphi compiler metadata, then maps results into **Ghidra data types**. Targets a wide range of modern Delphi versions. Primary use cases are **malware** and **legacy software** RE where recovering semantic names accelerates analysis—also relevant when game clients, launchers, or cheat tooling ship as Delphi PEs. (source: wiki/sources/descriptions/WenzWenzWenz__DelphiReSym.md)

Complements IDA-side Delphi analysis such as [[delphi-helper]] and Ghidra automation such as [[ghidra-scripts]] and [[better-string-analyzer]] when static Ghidra workflows need Object Pascal symbol context instead of raw addresses.

## Links

- Repo: https://github.com/WenzWenzWenz/DelphiReSym

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[delphi-helper]] · [[ce-remap-plugin]] · [[magicmida-rs]] · [[research-rigor]]
