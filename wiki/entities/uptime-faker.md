---
title: UptimeFaker
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/CookiePLMonster__UptimeFaker.md
updated: 2026-08-26
confidence: medium
---

# UptimeFaker

Windows **timing hook library** by CookiePLMonster that **fakes system uptime values** for testing and compatibility work. Written in **C++** as a **Microsoft Detours**-based plugin, injectable as a DLL or ASI-style module. Redirects multiple timer-related APIs with **INI-configured** behavior, including process-relative time simulation. Primarily used to **diagnose or mitigate game and application bugs** that manifest on **high-uptime systems** — a Game Testing / “Detecting High PC Uptime” lane distinct from Cheat Engine–style speed hacks. (source: wiki/sources/descriptions/CookiePLMonster__UptimeFaker.md)

AC stacks may treat abnormal uptime or timer API tampering as sandbox or tamper signals; [[uptime-faker]] supports controlled reproduction of those conditions for QA and defensive research.

## Links

- Repo: https://github.com/CookiePLMonster/UptimeFaker

## Related

[[detours]] · [[speed-hack]] · [[ce-speed-hack]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
