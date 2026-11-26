---
title: Orchard Obliterator
kind: entity
topics: [anti-cheat, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/flowerkitties__Orchard-Obliterator.md
updated: 2026-11-26
confidence: medium
---

# Orchard Obliterator

Windows **console scanner** that **detects, reports on, and optionally neutralizes** the **Orchard** Minecraft Java cheat client—including obfuscated **Nitro** builds. Written in **C#** for **.NET Framework**; ships embedded **signature rules** matching JAR contents, Mixin hooks, stealth/combat behaviors, in-process memory strings, and related telemetry artifacts. Targets multiplayer **Minecraft integrity**, client-side cheat hunting, and staff moderation on Windows hosts. (source: wiki/sources/descriptions/flowerkitties__Orchard-Obliterator.md)

## Scan surfaces

- Enumerates running **Java** and **Fabric** game processes; inspects loaded modules and process memory when permitted.
- Walks Minecraft **game and mods folders**; optional deep **drive sweeps** with **USN journal** and **Prefetch** forensics when run **elevated**.

## Operator actions

- Generate **forensic reports**, terminate affected games, **quarantine** suspicious archives, or run **guard mode** that watches folders and new Java processes.

## Links

- Repo: https://github.com/flowerkitties/Orchard-Obliterator

## Related

[[avgar-anticheats]] · [[jvm-inspector]] · [[jaranalyzer]] · [[hapiscanner]] · [[screenshare-signatures]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]