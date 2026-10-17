---
title: Astral AntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/tahad4492-svg__Astral-AntiCheat.md
updated: 2026-10-17
confidence: medium
---

# Astral AntiCheat

**Astral AntiCheat** (tahad4492-svg/Astral-AntiCheat) is a **Paper 1.21.11** Java plugin that detects and mitigates cheating and automation on Minecraft multiplayer servers. Built with **Maven** and **Java 21**, it rebuilds **vanilla movement physics** from per-tick client data and **ClientTickEndEvent**, analyzes **packet ordering** for silent rotations and hotbar swaps, and runs **lag-compensated combat** checks (reach, auras, aim, and related exploits). (source: wiki/sources/descriptions/tahad4492-svg__Astral-AntiCheat.md)

README category: Anti Cheat / game:minecraft.

## Detection surface

Coverage spans movement, world interaction, player packets, and macros (auto-clickers, silent hotbar swaps). Built-in **minigame handling** reduces false positives from teleports, rides, and launch mechanics.

## Enforcement and ops

**Configurable block mode** cancels illegal actions and **setbacks** players rather than default auto-kick or auto-ban. Staff get compact grouped alerts, detailed logs, commands, and a monitoring GUI; operators can run **watch-only alerts** or configure punishments.

## Engineering

Includes **simulation tests** that exercise known cheat-client behavior—aimed at server operators who want server-side game security rather than kernel-level anti-cheat.

## Positioning

Paper **1.21.11** **movement-replay** stack beside open-source simulators such as [[grim]] and alert-first event plugins such as [[aegis-ac]], with setback-first enforcement similar to modular Bukkit-family plugins such as [[argus-ac]].

## Peers

[[grim]] · [[aegis-ac]] · [[argus-ac]] · [[h-ac]] · [[novaguard]] · [[minecraft-anticheat-list]] · [[overviews/anti-cheat]]

## Links

- GitHub: https://github.com/tahad4492-svg/Astral-AntiCheat
