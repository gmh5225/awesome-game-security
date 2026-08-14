---
title: cs2-cheat
kind: entity
topics: [game-hacking, graphics-api, game-engine]
sources:
  - wiki/sources/descriptions/tiansongyu__cs2_cheat.md
  - wiki/sources/descriptions/gmh5225__CS2-Cheat.md
updated: 2026-08-14
confidence: medium
---

# cs2-cheat

Two Counter-Strike 2 cheat projects share this name in the curated list—one external educational ESP sample and one internal Source 2 SDK implementation.

## tiansongyu/cs2_cheat

Educational Counter-Strike 2 external ESP / cheat learning project (C++). Uses SDL2 + ImGui for overlay UI, Windows process memory reads, and generated offsets (e.g. cs2-dumper) with hourly CI offset updates. Features include box/skeleton ESP, health/weapon displays, aimbot, triggerbot, radar, anti-flash, and bomb timer; intended for offline insecure-mode study of memory structures, process I/O, and graphics overlays—not online play. (source: wiki/sources/descriptions/tiansongyu__cs2_cheat.md)

## gmh5225/CS2-Cheat

Internal Counter-Strike 2 cheat implementation (gmh5225) with gameplay modification features built on the **Source 2 engine SDK**. Modules include **ESP**, **aimbot**, and miscellaneous hacks—useful for researchers studying in-process CS2 cheat architecture and Source 2 SDK consumption beside samples such as [[asphyxia-cs2]] and [[cs2-internal]]. (source: wiki/sources/descriptions/gmh5225__CS2-Cheat.md)

## Links

- Repo (tiansongyu): https://github.com/tiansongyu/cs2_cheat
- Repo (gmh5225): https://github.com/gmh5225/CS2-Cheat

## Related

[[overviews/game-hacking]] · [[overviews/game-engine]] · [[overviews/graphics-api]] · [[cs2-cheat-base]] · [[cs2-cheat-cpp]] · [[cs2-external-cheat]] · [[cs2-internal]] · [[asphyxia-cs2]] · [[cs2-sdk]] · [[cs-2-glow]] · [[proext]] · [[counterstrike2-linux-cheat]] · [[cs2-offsets]] · [[present-hook]]
