---
title: netImgui
kind: entity
topics: [graphics-api, game-engine]
sources:
  - wiki/sources/descriptions/sammyfreg__netImgui.md
updated: 2026-07-23
confidence: medium
---

# netImgui

Dear ImGui remote-access library and application: any Dear ImGui host can take input from a remote PC and forward its UI draw stream (textures, vertices, indices, draw commands) to that remote for display. Aimed at game developers, engine programmers, and graphics researchers—especially Unreal / engine-plugin tooling—rather than Present-hook cheat overlays. (source: wiki/sources/descriptions/sammyfreg__netImgui.md)

Complements in-engine ImGui samples such as [[ue5-with-dear-imgui]] (local UE5 wiring) by moving the ImGui interaction surface off-box. Adjacent graphics-API overlay research ([[present-hook]], [[directxhook]]) is the in-process Present path; this repo is the networked ImGui remoting side of that UI surface.

## Links

- Repo: https://github.com/sammyfreg/netImgui (README: 'Dear Imgui' remote access library and application)

## Related

[[overviews/graphics-api]] · [[overviews/game-engine]] · [[ue5-with-dear-imgui]] · [[present-hook]] · [[directxhook]] · [[tracy]]
