---
title: CodM Dumper
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/Poko-Apps__CodMDumper.md
updated: 2026-08-22
confidence: medium
---

# CodM Dumper

**Call of Duty Mobile IL2CPP dump package** for Android (Poko-Apps). Focuses on extracting **il2cpp binaries and metadata** from the mobile title. Ships primarily as a **release-oriented distribution** with usage documentation rather than a fully exposed source tree. Supports **armv7 and arm64** on **Termux or similar terminals**, producing artifacts such as **`dump.cs`**, **`ida.py`**, and **IDA JSON** data for downstream static analysis. Targets mobile game reverse-engineering workflows; **deprecated by its author**. README lane `[il2cpp dump]`. (source: wiki/sources/descriptions/Poko-Apps__CodMDumper.md)

Complements generic Android IL2CPP dump tooling such as [[il2cppdumper]] and on-device GUI dumpers such as [[il2cppdumpdroidgui]] from the same author. Downstream CODM offensive samples such as [[codm-esp-aimbot-mod-menu]] sit in the title-specific mod-menu lane after metadata recovery.

## Links

- Repo: https://github.com/Poko-Apps/CodMDumper

## Related

[[il2cpp]] · [[il2cppdumper]] · [[il2cppdumpdroidgui]] · [[memkernel]] · [[codm-esp-aimbot-mod-menu]] · [[termux-app]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
