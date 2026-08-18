---
title: CaptureEngine
kind: entity
topics: [graphics-api, anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/aufkrawall__capture-engine.md
updated: 2026-08-18
confidence: medium
---

# CaptureEngine

Windows game capture, recording, on-screen overlays, graphics overrides, and frame pacing tool. C++ core with Python build system. Records video and multiple audio sources to Matroska via **Windows Graphics Capture**, **DXGI Desktop Duplication**, or an injected API-aware hook path intercepting D3D9 through D3D12, Vulkan, OpenGL, and DXVK. Hardware encoding via NVENC, AMD AMF, Intel Quick Sync, and Media Foundation; HDR-aware overlays with DLSS/FSR frame-generation integration; NVIDIA Reflex-based FPS limiting; per-application profiles for V-Sync, anisotropic filtering, and DLSS overrides. Documents explicit **anti-cheat safety boundaries** between non-injected capture modes and injected hook features—relevant for game security research, graphics API reverse engineering, and controlled single-player capture workflows. (source: wiki/sources/descriptions/aufkrawall__capture-engine.md)

## Capture modes

| Mode | Inject? | Notes |
|------|---------|-------|
| Windows Graphics Capture | No | Compositor-backed window/monitor capture |
| DXGI Desktop Duplication | No | Full desktop duplication path |
| API-aware hook | Yes | D3D9–D3D12, Vulkan, OpenGL, DXVK intercept for in-process frame access |

## Links

- Repo: https://github.com/aufkrawall/capture-engine

## Related

[[obs-game-capture]] · [[present-hook]] · [[reshade]] · [[screencapture]] · [[windows-desktop-duplication-sample]] · [[dxgicaptureapplication]] · [[anti-screenshot-capture]] · [[overviews/graphics-api]] · [[overviews/anti-cheat]]
