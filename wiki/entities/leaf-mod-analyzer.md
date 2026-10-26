---
title: Leaf Mod Analyzer
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gemakfy__leaf-mod-analyzer.md
updated: 2026-10-26
confidence: medium
---

# Leaf Mod Analyzer

**Leaf Mod Analyzer** (gemakfy/leaf-mod-analyzer) is a standalone **Rust** CLI (optional **Python** extension) that statically inspects **Minecraft mod JAR** class bytecode **without a JVM or full decompilation**. A native classfile parser scans single files or batch directories, applies entropy and obfuscation heuristics, and evaluates hits through an extensible **JSON rule engine**. Reporting is tailored to **Fabric**, **Forge**, and **NeoForge** loader layouts. Heuristics flag obfuscation, aggressive renaming, homoglyph identifiers, encrypted string pools, and suspicious bytecode patterns common in cheat clients—aimed at server operators, moderation workflows, and researchers who need fast offline triage of third-party mods. (source: wiki/sources/descriptions/gemakfy__leaf-mod-analyzer.md)

## Capabilities

- **Offline bytecode triage** — parse Java classfiles inside JARs; no runtime execution required.
- **Obfuscation signals** — entropy scoring plus rename/homoglyph/string-pool heuristics.
- **Custom rules** — load rule directories for organization-specific cheat fingerprints.
- **Loader-aware output** — batch scans with reports oriented to common Minecraft mod platforms.

## Positioning

Complements live **hash-whitelist** enforcement such as [[faircount]] and [[katapult-anticheat]] and screenshare-oriented Windows triage such as [[jaranalyzer]] by supporting **pre-admission** or **appeal** review of mod archives on Linux/macOS/Windows CI hosts. Does not replace server-side movement/combat plugins such as [[grim]] or [[lavaguard-ac]].

## Links

- Repo: https://github.com/gemakfy/leaf-mod-analyzer

## Related

[[jaranalyzer]] · [[faircount]] · [[katapult-anticheat]] · [[minecraft-anticheat-list]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
