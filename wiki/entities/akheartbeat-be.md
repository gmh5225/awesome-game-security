---
title: AkHeartbeat-BE
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/AkitaYui__AkHeartbeat-BE.md
updated: 2026-09-03
confidence: medium
---

# AkHeartbeat-BE

External **C++** tool for **Grand Theft Auto V Enhanced** that provides a **D3D11 overlay menu** and live game memory manipulation while **[[battleye]]** is disabled or bypassed. Runs as a **separate process** without injecting into the game, using **ReadProcessMemory** / **WriteProcessMemory** together with **AOB pattern scanning** to resolve world pointers, script globals, session state, and BattlEye-related flags. Feature modules include stat, script global, and script local editors, teleportation helpers, and runtime patches that neutralize BattlEye detection routines. Documentation maps the **user-mode BE client** and **BEDaisy** kernel driver architecture—aimed at game security researchers and reverse engineers studying BattlEye integration, external cheat design, and anti-cheat bypass techniques in Rockstar titles. (source: wiki/sources/descriptions/AkitaYui__AkHeartbeat-BE.md)

Contrasts with below-OS DMA stacks such as [[gta5-dma-cheat]] and in-process ScriptHookV mod menus such as [[phake]] by staying user-mode external with RPM/WPM and overlay rendering; complements BE client RE samples such as [[beclient]] and [[battleye-re]] with title-specific GTA5 Enhanced heartbeat/bypass documentation.

## Links

- Repo: https://github.com/AkitaYui/AkHeartbeat-BE
- README tag: GTA5 Enhanced BE heartbeat bypass: client–driver RE notes, AOB scan, external D3D11 overlay menu

## Related

[[battleye]] · [[gta5-dma-cheat]] · [[phake]] · [[grandtheftautov-cheat]] · [[gta-5-sigs-1.59]] · [[beclient]] · [[battleye-re]] · [[bedaisy-reversal]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
