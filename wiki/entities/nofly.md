---
title: NoFly
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/getawife__nofly.md
updated: 2026-09-27
confidence: medium
---

# NoFly

**NoFly** (getawife/nofly) is a **fly-hack detection plugin** for **Paper 1.21.x** Minecraft servers. Written in Java, it combines synchronous player movement analysis with **PacketEvents** packet sanity checks to detect unauthorized flight without client mods or memory inspection. (source: wiki/sources/descriptions/getawife__nofly.md)

README category: Anti Cheat / game:minecraft.

## Detection surface

- Tracks vertical and horizontal air movement; simulates expected **gravity**.
- Configurable buffers and leniency flag hovering, sustained ascent, and glide-like cheating.
- Exempts legitimate states: creative mode, vehicles, elytra, potion effects.
- PacketEvents layer adds packet-sanity cross-checks on server-received movement data.

## Enforcement

When violation buffers accumulate, the plugin can:

- Alert staff
- Log flags to disk
- Apply **setbacks** that rubber-band players to their last valid position

## Positioning

Lightweight, **fly-focused** server-side AC—not a general exploit-prevention suite. Sits in the Paper **1.21.x** movement-heuristic lane beside modular plugins such as [[h-ac]] and [[bs-anticheat]], and physics-prediction AC such as [[grim]], for administrators who want narrow fly detection rather than full combat/world coverage.

## Peers

[[grim]] · [[h-ac]] · [[bs-anticheat]] · [[antiguard]] · [[thorium-minecraft-plugin]] · [[minecraft-anticheat-list]]

## Links

- Repo: https://github.com/getawife/nofly

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[detector-operations]]
