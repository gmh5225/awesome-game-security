---
title: Echinoidea
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/M3351AN__Echinoidea.md
updated: 2026-08-23
confidence: medium
---

# Echinoidea

**Lightweight open-source external CS:GO cheat** from **M3351AN**, implemented primarily in **C#**. It bundles bunnyhop, overlay ESP, and trigger-bot behavior behind an offset-driven workflow and discusses **anti-cheat risk** for public builds. Primary research value: educational experimentation with **external cheat design** and **VAC-era detection tradeoffs**, especially reducing obvious **write-based detection signals** compared with heavier external frameworks. README **External C#** tag. (source: wiki/sources/descriptions/M3351AN__Echinoidea.md)

Sits in the lightweight usermode external CS:GO lane beside [[csgo-external-esp]], [[csgo-external-cheat]], and [[csgo-external-ahk-hack]], and beside same-author kernel-assisted CS2 samples such as [[samidare]] and [[ukia-rpm]].

## Architecture highlights

| Component | Role |
|-----------|------|
| Offset-driven reads | Game structure / field bootstrap for entity and view data |
| Overlay ESP | External on-screen entity visualization |
| Bunnyhop / trigger bot | Movement and input-assisted combat automation |
| Write-signal awareness | Design notes on minimizing obvious memory-write fingerprints |

## Links

- Repo: https://github.com/M3351AN/Echinoidea (README: External C#)

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[csgo-external-esp]] · [[csgo-external-cheat]] · [[csgo-external-ahk-hack]] · [[csgo-offsets]] · [[astra]] · [[heck-csgo-external]] · [[world-to-screen]] · [[samidare]] · [[ukia-rpm]]
