---
title: Minecraft Anti-Cheat (UltraAntiCheat)
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/XuanXuan-ZhengGui__Minecraft-Anti-Cheat.md
updated: 2026-08-19
confidence: medium
---

# Minecraft Anti-Cheat (UltraAntiCheat)

Open-source Minecraft server anti-cheat plugin (**UltraAntiCheat**) for Spigot and Paper **1.13+**. Written in Java 17+ (Maven). Ships thirteen core detection modules covering movement, combat, block, and packet cheating—fly, speed, timer, KillAura, reach, auto-clicker, scaffold, phase, velocity, no-slow, bad packets, ground spoof, and xray. Notable techniques include GCD-based rotation analysis for KillAura and aim assist, physics-based movement simulation with confidence scoring to reduce false positives, and optional **ProtocolLib** packet inspection. Can bridge with other anti-cheats including GrimAC, [[nocheatplus]], Vulcan, Matrix, and Spartan, and offers a browser-based web dashboard for live monitoring. Targets server operators who need configurable alerts, punishments, and multi-check cheat detection. (source: wiki/sources/descriptions/XuanXuan-ZhengGui__Minecraft-Anti-Cheat.md)

## Detection stack

Thirteen configurable movement, combat, block, and packet modules; GCD rotation analysis for combat cheats; physics-based movement simulation with confidence scoring; optional ProtocolLib packet layer; integration bridges to GrimAC, [[nocheatplus]], Vulcan, Matrix, and Spartan; browser web dashboard for live operator monitoring.

## Links

- Repo: https://github.com/XuanXuan-ZhengGui/Minecraft-Anti-Cheat

## Related

[[dakotaac]] · [[windfall-anticheat]] · [[ycbr-anticheat]] · [[cklsit-advanced-anticheat]] · [[minecraft-anticheatai]] · [[nocheatplus]] · [[avaanticheat]] · [[phantom-client]] · [[yuri]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
