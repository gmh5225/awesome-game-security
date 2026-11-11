---
title: ingame_overlay
kind: entity
topics: [graphics-api, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Nemirtingas__ingame_overlay.md
updated: 2026-11-11
confidence: medium
---

# ingame_overlay

**InGameOverlay** (Nemirtingas) is a cross-platform C++ library for drawing custom UI inside third-party applications by hooking their graphics renderers. It targets Windows, Linux, and macOS with OpenGL, Vulkan, DirectX 9–12, and Metal backends, using platform-specific renderer hooks plus a shared API-detection and resource layer—no host source required. The tree is CMake-built with detour-based interception plumbing; example and test targets pair hooks with Dear ImGui for validation. Typical uses: injected DLL or shared-library tooling, runtime visualization, debugging, and game-security or reverse-engineering workflows where overlay UI must composite into an existing frame. (source: wiki/sources/descriptions/Nemirtingas__ingame_overlay.md)

Compared with Windows-centric universal hook bootstrap libraries such as [[kiero]] and address-only locators like [[kiero2]], ingame_overlay emphasizes full cross-platform renderer coverage including Metal and a dedicated overlay/resource stack rather than method-table discovery alone.

## Links

- Repo: https://github.com/nemirtingas/ingame_overlay

## Related

[[present-hook]] · [[kiero]] · [[kiero2]] · [[imgui]] · [[d3dhook-imgui]] · [[universalhookx]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
