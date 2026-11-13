---
title: Deadline Cheat Test Anticheat
kind: entity
topics: [anti-cheat, game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/BonzeD__deadline_cheat_testAnticheat.md
  - wiki/sources/README-categories.md
updated: 2026-11-13
confidence: medium
---

# Deadline Cheat Test Anticheat

**Deadline Research Client** (BonzeD/deadline_cheat_testAnticheat) is a modular **Roblox Luau** test harness for exploring client-side exploit techniques and validating anti-cheat responses on places you own or are authorized to test—not a production anti-cheat product. (source: wiki/sources/descriptions/BonzeD__deadline_cheat_testAnticheat.md)

## Modules

Optional research modules cover **aim assistance**, **ESP** and skeleton overlays, **movement** and air-jump speed experiments, **trigger bot** behavior, visuals, and narrowly scoped bypass probes such as spoofed **WalkSpeed** reads and suppressed client violation signals.

## Operator surface

A configurable in-game UI with keybinds and **JSON profiles** pairs with **ANTICHEAT_RESEARCH.md** guidance on server-side detection, risks, and test plans rather than shipping enforcement logic.

## Off-platform tests

**Python** and **Lua 5.4** mock runners under `tests/` exercise module logic without a live Roblox session.

## Role

Anti Cheat **Stress Testing** lane for game security researchers, Roblox developers, and red-team evaluation of **client trust boundaries** and **server-authoritative** mitigations. Complements movement-only harnesses such as [[roblox-speed-tester]] and defensive Studio audits such as [[roblox-exploit-auditor]] beside Luau server AC such as [[volcano-ac]] and [[anticheat-dashboard]].

## Links

- Repo: https://github.com/BonzeD/deadline_cheat_testAnticheat

## Related

[[roblox-speed-tester]] · [[roblox-exploit-auditor]] · [[volcano-ac]] · [[anticheat-dashboard]] · [[world-to-screen]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
