---
title: apexbot
kind: entity
topics: [game-hacking]
sources:
  - wiki/sources/descriptions/CasualX__apexbot.md
updated: 2026-08-29
confidence: medium
---

# apexbot

Rust **external Apex Legends cheat framework** designed to embed into a custom memory-access backend rather than ship a fixed driver or overlay stack. Modular features include aim assist with PID smoothing, triggerbot logic, recoil control, ESP overlays, highlights, radar, observer tracking, and automation scripts. The codebase separates game-state parsing, projectile prediction, and offset handling, with tooling to regenerate gamedata from dumped offsets. Aimed at advanced game-security researchers and cheat developers studying external cheat architecture and feature engineering (cheat / game:apex legends [External]). (source: wiki/sources/descriptions/CasualX__apexbot.md)

Sits beside [[apexdream]] from the same CasualX author lane—`apexdream` as a Win32-attached library with pelite-based `apexdumper`, `apexbot` as a backend-embeddable modular framework. Related offset/SDK refresh tooling includes [[apex-legends-offset-dumper]] and [[apex-legends-sdk]].

## Links

- Repo: https://github.com/CasualX/apexbot

## Related

[[apexdream]] · [[apex-legends-offset-dumper]] · [[apex-legends-sdk]] · [[apex-external]] · [[obfstr]] · [[easy-anti-cheat]] · [[overviews/game-hacking]]
