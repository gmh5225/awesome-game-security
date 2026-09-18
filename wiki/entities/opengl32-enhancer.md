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

Drop-in 32-bit `opengl32.dll` proxy for Windows OpenGL games that forwards every call to the real system OpenGL library while hooking `wglSwapBuffers` to run a ReShade-style post-processing chain before each frame is presented. Written in C++ with OpenGL 4.3 compute shaders; supports FSR upscaling, SMAA/TAA, CAS sharpening, bloom, ACES tone mapping, LUT grading, SSAO, depth of field, and other filters via `opengl32_enhancer.ini` or an ImGui config editor—without modifying game source or using an injector. Useful for graphics interception, reverse engineering, and legacy OpenGL enhancement research. (source: wiki/sources/descriptions/ASDAlexander77__opengl32_enhancer.md)

## Links

- Repo: https://github.com/ASDAlexander77/opengl32_enhancer

## Related

[[present-hook]] · [[reshade]] · [[universalhookx]] · [[overviews/graphics-api]]
