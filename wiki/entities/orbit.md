---
title: Orbit
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/google__orbit.md
updated: 2026-08-07
confidence: medium
---

# Orbit

Standalone **C++ native-application profiler** from Google. Instruments functions **dynamically at runtime** without source changes or recompilation: function timing, call graphs, thread scheduling, context-switch analysis, and memory tracking. **Client–server architecture** supports remote profiling on **Linux** with visualization on **Windows**. Aimed at game developers and system programmers profiling complex native applications and catching performance regressions — sits in the Game Testing / native perf lane beside in-process profilers such as [[tracy]] and [[rprof]]. (source: wiki/sources/descriptions/google__orbit.md)

## Links

- Repo: https://github.com/google/orbit

## Related

[[tracy]] · [[rprof]] · [[overviews/game-engine]]
