---
title: imgui_club
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/ocornut__imgui_club.md
updated: 2026-07-27
confidence: medium
---

# imgui_club

Official Dear ImGui small-extension kit (C++): a mini hexadecimal memory editor (keyboard nav, read-only mode, ASCII/HexII views, address jump, range highlight, custom R/W handlers), a multi-context compositor (z-order / input routing / drag-and-drop across ImGui contexts), and a threaded rendering helper that snapshots `ImDrawData` for deferred draw. Aimed at game developers, tool authors, and reverse engineers building in-game debug UIs and memory inspection. (source: wiki/sources/descriptions/ocornut__imgui_club.md)

Complements in-engine ImGui wiring such as [[ue5-with-dear-imgui]] and remote remoting [[netimgui]]; cheat-side Present-hook overlays ([[present-hook]], [[directxhook]], [[dx11-basehook]]) reuse the same ImGui surface for menus rather than this official extension kit.

## Links

- Repo: https://github.com/ocornut/imgui_club (README: Official Dear ImGui extensions including a hex memory editor widget)

## Related

[[overviews/graphics-api]] · [[overviews/game-hacking]] · [[netimgui]] · [[ue5-with-dear-imgui]] · [[present-hook]] · [[directxhook]] · [[dx11-basehook]]
