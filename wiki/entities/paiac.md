---
title: PaiAC
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Pai100707__PaiAC.md
  - wiki/sources/README-categories.md
updated: 2026-11-13
confidence: medium
---

# PaiAC

**PaiAC** (Pai100707/PaiAC) is a modular **server-side anti-cheat plugin** for **Minecraft Java Edition** aimed at survival, economy, and **crystal or respawn-anchor PvP** networks. Implemented in **Java 21** with Gradle, it targets **Paper** roughly **1.21.1–1.21.11**, with code paths for **Folia** and **Spigot/Bukkit**. (source: wiki/sources/descriptions/Pai100707__PaiAC.md)

README category: Anti Cheat / Open Source Anti Cheat System / game:minecraft.

## Detection surface

Movement checks cover **fly**, **speed**, and **boat-fly**. Combat modules flag **reach**, **kill aura**, and **auto-clicker**. PvP-macro checks include **crystal placement bursts**, **respawn-anchor timing**, **auto-totem**, and **fast experience bottles**. The plugin surfaces native **Paper anti-xray** configuration status rather than reimplementing x-ray detection.

## Evidence and enforcement

**Violation levels** with decay, **SQLite** evidence storage, configurable **punishment ladders** and ban lists, **lag-aware gating**, and an administrative command suite support **detection-first** defaults with optional enforcement.

## Positioning

Crystal/anchor PvP–focused modular Paper-family stack beside open heuristics such as [[h-ac]] and [[novaguard]], alert-first plugins such as [[aegis-ac]], and evidence-oriented operators practicing [[detector-operations]] discipline (stored violation history before auto-sanctions).

## Peers

[[aegis-ac]] · [[h-ac]] · [[novaguard]] · [[argus-ac]] · [[bedrockguard]] · [[minecraft-anticheat-list]] · [[detector-operations]]

## Links

- GitHub: https://github.com/Pai100707/PaiAC
