---
title: Medal Overlay Framework
kind: entity
topics: [graphics-api, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/NotExenis__Medal-Overlay-Framework.md
updated: 2026-11-26
confidence: medium
---

# Medal Overlay Framework

Medal Overlay Framework (MOF) is a stealth in-game overlay stack that routes custom drawing through Medal.tv’s **whitelisted** Electron capture overlay so visuals can appear to anti-cheat as part of Medal itself. A Node.js patcher modifies Medal’s application package to inject a bridge with a **named-pipe** server; **Python** and **C++** SDKs connect and send JSON draw commands executed on the overlay canvas via injected JavaScript and a .NET helper. Primitives and widgets include ESP boxes, crosshairs, snap lines, skeleton rendering, gradients, animations, layered compositing, and a tabbed menu with toggles and sliders. Stealth-oriented choices include hardware-derived pipe names, innocuous files inside the asar archive, obfuscated globals, and cleanup of legacy patches. Targets game security researchers and overlay authors studying trusted third-party capture overlays as rendering surfaces against [[easy-anti-cheat]], [[battleye]], [[vanguard]], and similar protections. (source: wiki/sources/descriptions/NotExenis__Medal-Overlay-Framework.md)

## Links

- Repo: https://github.com/NotExenis/Medal-Overlay-Framework

## Related

[[discord-overlay-hook]] · [[overlaycord]] · [[nvidia-overlay-hijack]] · [[steam-hook-render-poc]] · [[present-hook]] · [[overviews/graphics-api]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]