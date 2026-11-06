---
title: WilonityLoader
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/WilonityGames__WilonityLoader.md
updated: 2026-11-06
confidence: medium
---

# WilonityLoader

**WilonityLoader** (WilonityGames) is framed in its description projection as a **unified Windows client** for **injecting third-party cheat modules** into many **multiplayer** titles under a **subscription/license** model: fast **hot-injection** into running games, large **per-game module** sets (e.g. aim assistance and ESP), **hardware-ID–bound** licensing with periodic resets, and **rapid turnaround** after anti-cheat **signature** changes. The repo root is described as a **C++20 CMake** project named **Osiris** (optional ASM) plus a **packaged Electron-style** application bundle and **Node** lockfiles for the UI; docs target **Windows with administrator rights** and a supported **.NET Framework** runtime, with install guidance that mentions disabling **real-time antivirus** during setup—useful for studying **adversarial loader delivery**, **identity binding**, and **client-side evasion** narratives, not as proof of any live bypass. (source: wiki/sources/descriptions/WilonityGames__WilonityLoader.md)

README tags it as a Windows cheat loader citing **kernel/driver bypass**, **HWID spoofing**, and an **undetected injector stack** for many multiplayer titles—compare other licensed / HWID-gated loaders such as [[cyber-ant-loader]], [[codm-cheat]], and manual-map injector research such as [[wizard-loader]].

## Links

- Repo: https://github.com/WilonityGames/WilonityLoader

## Related

[[cyber-ant-loader]] · [[codm-cheat]] · [[wizard-loader]] · [[hwid-spoofing]] · [[stack-spoofing]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
