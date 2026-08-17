---
title: Optick
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/bombomby__optick.md
updated: 2026-08-17
confidence: medium
---

# Optick

**C++ game performance profiler** with a lightweight in-game instrumentation SDK and a **WPF-based GUI viewer**. Captures per-frame **CPU timing**, **GPU events** (D3D12 / Vulkan), **thread scheduling**, **context switches**, and **hardware counters** via **ETW** on Windows. Integrates with **Unreal Engine 4/5**, **Unity**, and custom engines through macros such as `OPTICK_EVENT` / `OPTICK_FRAME`; streams capture data over **TCP** to the viewer. Analysis surfaces include flame graphs, per-thread timelines, call-stack sampling, and frame-comparison views, with optional task-tracker hooks (GitHub, Jira). Aimed at game developers and engine programmers profiling rendering, physics, and gameplay systems to find CPU/GPU bottlenecks — sits in the README **Game Testing** / graphics-performance lane beside in-process profilers such as [[tracy]] and [[orbit]]. (source: wiki/sources/descriptions/bombomby__optick.md)

## Links

- Repo: https://github.com/bombomby/optick

## Related

[[overviews/game-engine]] · [[overviews/graphics-api]] · [[tracy]] · [[orbit]] · [[rprof]]
