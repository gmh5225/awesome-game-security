---
title: OpenGL32 Enhancer
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/ASDAlexander77__opengl32_enhancer.md
  - wiki/sources/README-categories.md
updated: 2026-09-18
confidence: medium
---

# OpenGL32 Enhancer

Drop-in 32-bit `opengl32.dll` proxy for Windows OpenGL games that forwards every call to the real system OpenGL library while hooking `wglSwapBuffers` to run a ReShade-style post-processing chain before each frame is presented. Written in C++ with CMake and OpenGL 4.3 compute shaders; no game source changes or injector required. (source: wiki/sources/descriptions/ASDAlexander77__opengl32_enhancer.md)

## Mechanism

- **Proxy forwarding:** every OpenGL export delegates to the real system `opengl32.dll`.
- **Present hook:** `wglSwapBuffers` intercept runs a configurable effect chain before the frame is shown.

## Effects

FSR upscaling, SMAA/TAA, CAS sharpening, bloom, ACES tone mapping, LUT color grading, SSAO, depth of field, and other filters via `opengl32_enhancer.ini` or an included ImGui config editor. Aimed at players/modders modernizing legacy 32-bit OpenGL titles and researchers studying graphics interception. (source: wiki/sources/descriptions/ASDAlexander77__opengl32_enhancer.md)

## Links

- Repo: https://github.com/ASDAlexander77/opengl32_enhancer

## Related

[[present-hook]] · [[reshade]] · [[dxwrapper]] · [[universalhookx]] · [[overviews/graphics-api]]
