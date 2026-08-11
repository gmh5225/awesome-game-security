---
title: OBS Game Capture
kind: concept
topics: [graphics-api, game-hacking, anti-cheat]
sources:
  - wiki/sources/skills/graphics-api.md
  - wiki/sources/descriptions/gmh5225__OBS-graphics-hook32-Hook.md
  - wiki/sources/descriptions/gmh5225__OBS-Hook.md
updated: 2026-08-11
confidence: medium
---

# OBS Game Capture

OBS Studio frame-acquisition modes and their **security-research relevance**: legitimate streaming, accessibility overlays, and **AI visual cheat pipelines** that reuse capture instead of game-memory reads. Implementation varies by OBS version, Windows build, graphics API, and source settings—identify the active backend before inferring artifacts. (source: wiki/sources/skills/graphics-api.md)

## Capture modes

| Mode | Mechanism | Inject? | Typical use |
|------|-----------|---------|-------------|
| **Game Capture** | OBS graphics-hook DLL in game process; API-specific present/capture intercept; often shared GPU textures | Yes (OBS hook) | Low-latency pre-composition game frames |
| **Window Capture** | WGC, BitBlt, or version-specific window backend | Usually no | Window/composited path; occlusion/HDR behavior varies |
| **Display Capture** | Desktop Duplication or WGC on monitor output | No | Full monitor; no per-process hook |
| **Virtual Camera** | Exports captured frames as a camera device | Depends on upstream source | Downstream AI, streaming, or second process |

Game Capture hook modules and shared-handle traffic are **observable** but also normal for streamers—correlate with plugin provenance, inference load, and input behavior ([[ai-aimbot-detection]]).

## AI visual pipeline (latency-critical)

Typical single-PC path:

```
Game render → Present/backbuffer copy → shared GPU texture
→ staging readback (Map/Unmap) → CPU frame buffer
→ ROI crop (e.g. 640×640) → inference (CUDA/TensorRT/DirectML)
→ mouse command → [[hardware-input-injection]]
```

**OBS plugin form factor** — AI as an OBS video filter (`obs_source_frame` callback) runs inference in-process and may emit HID via hardware devices; appears as “OBS running a filter.”

**Dual-machine** — Game PC OBS → NDI or capture card → cheat PC inference → network to KMBox on game PC; end-to-end latency depends on encode, buffer, and sync—measure percentiles on the deployed setup, not fixed budgets.

Corpus adjacency: [[input-overlay]] (OBS Keyboard Mapper plugin), [[present-hook]] (backbuffer copy alternative to OBS hook). OBS graphics-hook hijack samples such as [[obs-graphics-hook32-hook]] (gmh5225; 32-bit OBS hook inject; pointer-replacement technique) and [[obs-hook]] (gmh5225; hijack OBS Game Capture hook DLL to inject custom draw calls through OBS's trusted pipeline—no separate overlay HWND; AC whitelist research) illustrate offensive reuse of the same Game Capture hook surface researchers already monitor for `obs-graphics-hook64.dll`. (source: wiki/sources/descriptions/gmh5225__OBS-graphics-hook32-Hook.md) (source: wiki/sources/descriptions/gmh5225__OBS-Hook.md)

## Detection-relevant signals (non-proof)

- `obs-graphics-hook64.dll` in game process module list
- Present detour or repeated staging/readback patterns
- DXGI shared handles from game to external process
- `Processing.NDI.Lib.*.dll`, virtual camera drivers (`obs-virtualcam`)
- Sustained GPU→CPU copy bandwidth anomalies

Treat as **collection signals** requiring behavioral and contextual corroboration.

## Related

[[anti-screenshot-capture]] · [[present-hook]] · [[obs-graphics-hook32-hook]] · [[obs-hook]] · [[ai-aimbot-detection]] · [[hardware-input-injection]] · [[overviews/graphics-api]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
