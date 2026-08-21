---
title: Vesta
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/Read1dno__vesta.md
updated: 2026-08-21
confidence: medium
---

# Vesta

**Feature-complete external Counter-Strike 2 cheat** from Read1dno. Implemented in **C++23** for **Windows x64**, it runs entirely outside the game process with **no code injection** and **no kernel drivers**. Live game state is read through standard process memory APIs; ESP, chams, and menus render via a **DirectX 11 overlay**; player input is sent through the external Windows input gateway. (source: wiki/sources/descriptions/Read1dno__vesta.md)

## Architecture highlights

| Component | Role |
|-----------|------|
| Process memory APIs | Out-of-process RPM for CS2 client state reconstruction |
| DirectX 11 overlay | ESP, chams, and in-game menu rendering |
| External input gateway | Aimbot/triggerbot input without in-process hooks |
| Combat simulation | Ballistics, penetration, and collision models for aim and visualization |
| Lua 5.4 scripting API | Sandboxed extensions (e.g. web-based radar) |
| Feature modules | Aimbot, triggerbot, player/world ESP, grenade prediction, in-game radar |

Positioned for game security researchers studying **external cheat architectures**, **anti-cheat evasion tradeoffs**, and **CS2 client state reconstruction**. Sits beside full-stack DX11 externals such as [[cs2-external-cheat]], [[cs2-ext]], and [[titled-gui-cs2]], and ImGui framework samples such as [[tkazer-cs2-external]]. The optional Lua-driven web radar path complements browser-radar stacks such as [[cs2-webradar]].

## Links

- Repo: https://github.com/Read1dno/vesta

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[cs2-external-cheat]] · [[cs2-ext]] · [[titled-gui-cs2]] · [[tkazer-cs2-external]] · [[cs2-webradar]] · [[cs2-offsets]] · [[world-to-screen]] · [[hardware-input-injection]]
