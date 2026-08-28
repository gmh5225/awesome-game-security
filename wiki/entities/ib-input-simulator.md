---
title: Ib Input Simulator
kind: entity
topics: [game-hacking, windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/Chaoses-Ib__IbInputSimulator.md
updated: 2026-08-28
confidence: medium
---

# Ib Input Simulator

**IbInputSimulator** (Chaoses-Ib) is a Windows input simulation library that sends keyboard and mouse events through **driver-backed** paths instead of standard user-mode APIs. C and C++ components plus AutoHotkey examples expose a unified initialization and send interface across multiple backends: **Logitech software**, **Razer Synapse**, **MouClassInputInjection**, and **DD virtual devices**. Primary use cases are automation, game tooling, and anti-cheat evasion research where `SendInput` and related APIs are blocked or heavily monitored. (source: wiki/sources/descriptions/Chaoses-Ib__IbInputSimulator.md)

## Links

- Repo: https://github.com/Chaoses-Ib/IbInputSimulator

## Related

[[autohotkey-l]] · [[razer-rzctl]] · [[logitech-cve]] · [[mouhid-input-hook]] · [[mouseclassservicecallbacktrick]] · [[hardware-input-injection]] · [[pareidolia-triggerbot]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
