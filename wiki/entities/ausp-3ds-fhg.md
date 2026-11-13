---
title: AUSP-3DS-FHG
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/SlabyLol__AUSP-3DS-FHG.md
updated: 2026-11-13
confidence: medium
---

# AUSP-3DS-FHG

**AUSP-3DS** (SlabyLol/AUSP-3DS-FHG) is a drop-in **C library** for **Nintendo 3DS homebrew** titles that detects cheat and plugin loaders **without reading the SD card or filesystem**. At startup it walks process memory through the system memory-query service and matches byte signatures associated with **NTR**, **3GX**, **CTRPluginFramework**, **Luma** plugins, and similar tooling. Integrators optionally treat **Nimbus** and **Pretendo** as benign so online custom-network players are not blocked. A single startup routine drives a **citro2d** splash screen, runs the scan, then shows a configurable warning UI, invokes a custom callback, exits the process, or combines those reactions. Built on **libctru**, **citro2d**, and **citro3d** for lightweight in-process anti-cheat and anti-tamper in homebrew multiplayer. (source: wiki/sources/descriptions/SlabyLol__AUSP-3DS-FHG.md)

README category: Anti Cheat / Nintendo 3DS homebrew.

## Detection model

Memory-only **signature scanning** via the platform memory-query API—no filesystem or SD enumeration—targets known loader and plugin frameworks common on Luma-based 3DS homebrew stacks.

## Integration

One startup entry point: splash → scan → configurable enforcement (UI warning, callback, process exit, or combined reactions).

## Positioning

Defensive counterpart to overlay/cheat authoring in the same console lane as [[ctr-composer]] and [[ocarina-ctr-composer]], beside preservation/emulator work such as [[3beans]] and retail patch research such as [[3ds-game-fixes]]; practices in-process integrity signaling akin to open usermode signature libraries on other platforms (see [[overviews/anti-cheat]]).

## Peers

[[3beans]] · [[3ds-game-fixes]] · [[ctr-composer]] · [[ocarina-ctr-composer]] · [[detector-operations]]

## Links

- GitHub: https://github.com/SlabyLol/AUSP-3DS-FHG
