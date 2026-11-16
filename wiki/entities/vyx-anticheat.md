---
title: VyxAntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/elijoewashacked-pixel__VyxAntiCheat.md
  - wiki/sources/README-categories.md
updated: 2026-11-16
confidence: medium
---

# VyxAntiCheat (VyxAC)

**VyxAC** (elijoewashacked-pixel/VyxAntiCheat) is an open-source Minecraft server anti-cheat plugin for **Spigot**, **Paper**, and **Purpur** (**Paper 1.20+**) that prioritizes **low false-positive bans** through review-first workflows and corroborated evidence. It is implemented in **Java** (JDK 17+, Maven) and targets multiplayer administrators who want a self-hosted, highly tunable AC without relying on external packet-hook libraries by default. (source: wiki/sources/descriptions/elijoewashacked-pixel__VyxAntiCheat.md)

## Detection stack

Roughly **forty-seven** Bukkit event–based checks span combat, movement, inventory and world interaction, and coarse packet or timing heuristics.

A lightweight statistical **“mini AI”** scores click rhythm, aim, and reaction patterns against the server’s clean-player baseline under a strict CPU time budget—on-server statistical scoring, not a remote inference API.

Punishment logic can require **multiple corroborating checks**, **ping and TPS guards**, and **grace periods** during teleports, lag, and vehicles.

## Operator tooling

Operators configure checks via **YAML** and in-game commands, including a customize GUI, violation profiles, and optional **staff review buttons** before kicks or bans.

## Links

- Repo: https://github.com/elijoewashacked-pixel/VyxAntiCheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[detector-operations]] · [[ai-aimbot-detection]] · [[powerac]] · [[civ-anticheat]] · [[anticheatplus]] · [[bs-anticheat]]