---
title: FFNx
kind: entity
topics: [graphics-api, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/julianxhokaxhiu__FFNx.md
  - wiki/sources/README-categories.md
updated: 2026-11-07
confidence: medium
---

# FFNx

Replacement graphics and modding driver for the Windows releases of **Final Fantasy VII** and **Final Fantasy VIII**, extending the classic FF7 OpenGL patch lineage into a full mod platform. Implemented in C++ with CMake: a shared injected DLL hooks the legacy executables and rebuilds rendering through [[bgfx]], exposing DirectX 11, DirectX 12, Vulkan, and OpenGL backends plus modern audio, input, widescreen, and texture pipelines. Modders and researchers can capture draws with RenderDoc, inspect engine state via ImGui, apply Hext-style binary patches, redirect assets through TOML configuration, and replace hardcoded EXE data, VRAM pages, movies, music, and shaders—including a native speedhack. Useful for studying how commercial legacy titles are extended through injected rendering layers and in-process memory patching. (source: wiki/sources/descriptions/julianxhokaxhiu__FFNx.md)

## Mechanism

- **Injected driver DLL:** shared hook layer replaces the original graphics path with a [[bgfx]]-backed renderer selectable across D3D11/12, Vulkan, and OpenGL.
- **Asset and binary modding:** TOML-driven asset redirection, Hext-style patches, and direct EXE/VRAM/content replacement—not a Present-only overlay cheat framework.
- **Debug surfaces:** ImGui in-game UI and RenderDoc-compatible frame inspection for draw-path RE.

## Security relevance

Reference implementation for multi-backend graphics driver replacement on shipping Win32 game executables—the same class of in-process DLL injection, render-path hooking, and executable memory patching that anti-cheat and integrity tooling must distinguish from benign compatibility mods. (source: wiki/sources/descriptions/julianxhokaxhiu__FFNx.md)

## Links

- Repo: https://github.com/julianxhokaxhiu/FFNx (README: [Graphics driver replacement and modding platform for Final Fantasy VII/VIII])

## Related

[[bgfx]] · [[shader-injector]] · [[dxwrapper]] · [[winehooks]] · [[wiz3d]] · [[draw-call-hook]] · [[present-hook]] · [[imgui]] · [[overviews/graphics-api]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
