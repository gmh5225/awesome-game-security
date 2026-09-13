---
title: Frame Observation Boundary
kind: concept
topics: [graphics-api, anti-cheat, game-hacking]
sources:
  - wiki/sources/skills/graphics-api.md
updated: 2026-09-13
confidence: high
---

# Frame Observation Boundary

Discipline for interpreting graphics, overlay, and screenshot evidence: record the observation layer and baseline dimensions **before** naming a hook, cheat, or anti-cheat mechanism. Pair with [[research-rigor]] when a README sample or capture artifact is treated as proof. (source: wiki/sources/skills/graphics-api.md)

## Baseline before interpretation

Record for every rendering or capture claim:

| Dimension | Why it matters |
|-----------|----------------|
| Graphics API and backend | DX9–12, OpenGL, Vulkan, translation layers (DXVK, Wine) change hook points |
| Driver and compositor | DWM, flip model, DirectFlip, Independent Flip, HDR/SDR alter what a capture sees |
| Capture path | Game inject, Desktop Duplication, PrintWindow, Present hook, GPU readback, NVIDIA scanout |
| Synchronization model | Frame discard, vsync, staging/readback timing affect stale or black frames |
| Tool and version | OBS mode, AC module, profiler, or debugger version changes artifacts |

Black, missing, or stale frames have multiple benign explanations—they are not sufficient evidence of concealment without a controlled comparison. (source: wiki/sources/skills/graphics-api.md)

## Layer separation

Do not treat these as interchangeable copies of the same image:

```
Application render targets
  → presentation queues / swap-chain Present
    → compositor output (DWM, flip model)
      → physical display output
        → captured image (screenshot, OBS, AI pipeline)
```

Each step can drop, reorder, or transform content under documented platform behavior. Route hook-specific questions to [[present-hook]] or [[draw-call-hook]]; capture-contract questions to [[anti-screenshot-capture]] or [[obs-game-capture]].

## Capability classification

Classify claims by required capability before attribution:

| Class | Example | Evidence focus |
|-------|---------|----------------|
| In-process graphics change | Present hook, draw-call chams, shader inject | Module provenance, vtable/state integrity, frame debugger |
| Separate-process overlay | Layered HWND, DWM draw, Steam/NVIDIA hijack | Window affinity, composition surface, ETW/GDI signals |
| Frame access for analysis | OBS Game Capture, DDA, AC screenshot | Active capture API, inject footprint, readback bandwidth |

Include **counterexamples**: legitimate streaming (OBS), accessibility overlays, vendor tools (GeForce Experience, Steam), debug visualization, and post-processing injectors such as [[reshade]].

## Capture vs enforcement

**Observed capture behavior** (a PNG, OBS hook DLL, staging texture pattern) is collection evidence. **Assumed anti-cheat enforcement** (ban, flag, staff review) requires the detector's configured path, policy, and corroboration—do not infer enforcement scope from a single screenshot or hook artifact alone. Scheduled snapshots cover their acquisition intervals; intermittent absence does not establish session-wide absence.

## Coverage matrix (owned samples)

For owned applications or lab repros, document: API, OS/driver build, windowed vs exclusive fullscreen, presentation model, monitor count, capture backend, cursor handling, and timestamps. Use known-content controls to distinguish capture failure, protected content, output selection, and actual rendering differences.

## Related

[[present-hook]] · [[draw-call-hook]] · [[anti-screenshot-capture]] · [[obs-game-capture]] · [[world-to-screen]] · [[cheat-attack-surface]] · [[research-rigor]] · [[overviews/graphics-api]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
