---
title: taskbarhero-bot
kind: entity
topics: [game-hacking, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/matheusbranhann__taskbarhero-bot.md
updated: 2026-08-11
confidence: medium
---

# taskbarhero-bot

Windows **trainer and automation bot** for the Unity **IL2CPP** game TaskbarHero, delivered as a self-contained C#/.NET 10 application with a WPF dashboard. Attaches to the running game process and uses batch memory reads, AOB scanning, and IL2CPP offset resolution to read and modify save data, stats, inventory, runes, and stage progression. (source: wiki/sources/descriptions/matheusbranhann__taskbarhero-bot.md)

Key capabilities include **ACTk** (Anti-Cheat Toolkit) bypass, god mode and stat editing, **ObscuredInt** read/write, and scripted automations (auto-boxing, auto-stash, auto-fuse, auto-restart after crashes). Also provides Steam Community Market price lookup with optional OCR overlay, build-hash-based offset caching, and a headless core library testable from a CLI harness.

Useful for reverse engineers and game-security researchers studying Unity IL2CPP external memory editing, client-side protection bypass, and external trainer architecture.

## Links

- Repo: https://github.com/matheusbranhann/taskbarhero-bot

## Related

[[il2cpp]] · [[unity202x-externalresolve]] · [[yae-achievement]] · [[escapefromtarkov-trainer]] · [[overviews/game-hacking]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]
