---
title: FaceOff
kind: entity
topics: [game-hacking, windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/REDLANTERNDEV__FaceOff.md
  - wiki/sources/README-categories.md
updated: 2026-10-31
confidence: high
---

# FaceOff

**FaceOff** (redlanterndev/faceoff) is a portable **Windows** utility that disables FACEIT's kernel anti-cheat when you are not playing and re-enables it before the next match. It targets competitive **FPS** players (notably **CS2** on FACEIT) and security-conscious users who want to limit always-on kernel anti-cheat exposure without uninstalling the client. (source: wiki/sources/descriptions/REDLANTERNDEV__FaceOff.md)

README category: **Explore AntiCheat System:FACEIT** / Cheat.

## Components toggled

The tool coordinates **`FACEIT_AC.sys`**, the **FACEITService** Windows service, and related FACEIT client processes, persisting original driver/service settings locally before applying off/on states. (source: wiki/sources/descriptions/REDLANTERNDEV__FaceOff.md)

## Boot-time driver constraint

FACEIT only accepts its kernel driver when loaded at **boot**, so enable/disable flows require **administrator elevation** and a documented **system restart**; the WPF UI and CLI walk through that reboot cycle. (source: wiki/sources/descriptions/REDLANTERNDEV__FaceOff.md)

## Delivery

Implemented in **C#** as a WPF desktop app with a small **CLI**; equivalent **batch scripts** provide the same toggle behavior without running the compiled executable. (source: wiki/sources/descriptions/REDLANTERNDEV__FaceOff.md)

## Positioning

Operational **kernel AC exposure management** between match sessions—not an in-match bypass. Contrasts with offensive FACEIT research such as [[ec-pro-lan]] and sits beside [[anti-cheat-toggle]] lab tooling and platform-trust dual-boot notes ([[omarchy-boot-manager]]) on [[overviews/anti-cheat]].

## Links

- Repo: https://github.com/redlanterndev/faceoff

## Related

[[ec-pro-lan]] · [[anti-cheat-toggle]] · [[omarchy-boot-manager]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
