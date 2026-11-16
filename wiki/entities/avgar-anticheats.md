---
title: Avgar AntiCheats
kind: entity
topics: [anti-cheat, game-hacking, windows-kernel]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/Werta1z__Avgar-AntiCheats.md
updated: 2026-11-16
confidence: medium
---

# Avgar AntiCheats

Windows-focused **forensic and runtime scanner** for **Minecraft Java screenshare** and integrity checks. PowerShell orchestration loads an inline, multi-threaded **C# engine** at runtime so staff can run deep audits without shipping separate binaries—aimed at server moderators and game-security reviewers needing a fast, zero-dependency local triage workflow during live or post-session investigations. (source: wiki/sources/descriptions/Werta1z__Avgar-AntiCheats.md)

## Runtime memory (javaw.exe)

- **WinAPI memory reads** hunt ghost-client strings, unbacked PE regions, and manual-map style DLL injections in the JVM process.
- Scans **in-memory JAR bytecode** for suspicious patterns—Mixin hooks, reflection around combat/hitbox logic, and related cheat-client artifacts.

## Host artifact correlation

Correlates Windows execution and filesystem traces: **BAM** registry entries, **Prefetch**, execution history, **DNS resolver cache**, and broad filesystem sweeps against large signature lists of known clients, loaders, and trace-cleaning utilities. (source: wiki/sources/descriptions/Werta1z__Avgar-AntiCheats.md)

## Links

- Repo: https://github.com/Werta1z/Avgar-AntiCheats

## Related

[[jvm-inspector]] · [[jaranalyzer]] · [[hapiscanner]] · [[error-pc-check]] · [[screenshare-signatures]] · [[toxido-anticheat]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]