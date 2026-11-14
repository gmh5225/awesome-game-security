---
title: PerfOverlay Supreme
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/TheBlackSide243__perfoverlay-supreme.md
updated: 2026-11-14
confidence: medium
---

# PerfOverlay Supreme

**PerfOverlay Supreme** (TheBlackSide243) is a single-exe Windows 10/11 in-game performance overlay that reports FPS, frame time, frametime lows, and CPU, GPU, RAM, and system sensor metrics above running games **without injecting into game processes**. C++/CMake/MSVC implementation: frame timing from **Windows ETW Present events**, rendering via a separate click-through overlay using Direct3D 11, DirectComposition, and Direct2D. Features include per-game auto-detection and profiles, an RTSS-style layout editor, import/render of RivaTuner OverlayEditor presets, and optional sensor feeds from NVML, performance counters, HWiNFO, or LibreHardwareMonitor. Audience: PC gamers, benchmarkers, and anyone studying overlay techniques on public APIs rather than Present hooks—relevant when judging anti-cheat compatibility on competitive titles. README **DirectX / Overlay** category. (source: wiki/sources/descriptions/TheBlackSide243__perfoverlay-supreme.md)

Compared with injected OSD tools such as [[push]] or universal hook libraries such as [[ingame-overlay]], PerfOverlay Supreme keeps game address space untouched and observes frames through ETW, closer in telemetry spirit to [[presentmon]] but with an integrated RTSS-like HUD stack.

## Links

- Repo: https://github.com/TheBlackSide243/perfoverlay-supreme

## Related

[[presentmon]] · [[push]] · [[ingame-overlay]] · [[present-hook]] · [[frame-observation-boundary]] · [[overviews/graphics-api]] · [[overviews/anti-cheat]]