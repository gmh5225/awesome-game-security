---
title: DelphiHelper
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/eset__DelphiHelper.md
updated: 2026-08-15
confidence: medium
---

# DelphiHelper

**DelphiHelper** (eset) is tooling to **help analyze x86/x86_64 binaries written in Delphi** (Object Pascal). It targets game-security researchers and reverse engineers working in the **cheat / IDA Plugins** lane when clients, launchers, or legacy tooling ship as Delphi PEs rather than C/C++ or .NET. Running the setup script requires **`py7zr`** (`pip install py7zr`). (source: wiki/sources/descriptions/eset__DelphiHelper.md)

Complements Delphi-adjacent cheat/RE workflows such as [[ce-remap-plugin]] (Delphi Cheat Engine plugin), runtime event-name recovery via [[ida-for-delphi]], and unpackers with Delphi OEP heuristics such as [[magicmida-rs]] when static IDA analysis needs Delphi-specific structure recovery.

## Links

- Repo: https://github.com/eset/DelphiHelper

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ce-remap-plugin]] · [[magicmida-rs]] · [[ida-pro-mcp]] · [[awesome-ida-x64-olly-plugin]]
