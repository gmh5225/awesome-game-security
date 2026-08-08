---
title: World-to-Screen
kind: concept
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/skills/game-hacking.md
  - wiki/sources/descriptions/microsoft__DirectXMath.md
  - wiki/sources/descriptions/kotae4__lab-esp-and-aimbot.md
  - wiki/sources/descriptions/gmh5225__fortnite-W2S-offset-Fortnite.md
updated: 2026-08-08
confidence: high
---

# World-to-Screen

Project a **3D world-space point** (entity bone, item, waypoint) onto **2D screen pixels** using the active view/projection matrix—core math for ESP boxes, aim FOV checks, and radar overlays. Invalid when the point is behind the camera (`w < threshold`). (source: wiki/sources/skills/game-hacking.md)

## Pipeline

1. Multiply world position by view matrix → clip coordinates `(x, y, w)`.
2. Reject if `w` below near-plane cutoff (behind camera).
3. Perspective divide → NDC `(-1…1)`.
4. Map NDC to pixel space: `screen_x = (width/2) * (ndc_x + 1)`; flip Y for top-left origin.

Matrix layout and row/column convention vary by engine and hook point—verify against the game's `ViewMatrix` / `ViewProjection` dump, not a generic snippet.

## Engine helpers

Cross-engine constexpr libraries such as [[omath]] ship W2S, projectile prediction, and engine-specific camera helpers (Source, Unity, Unreal, Frostbite, etc.). Microsoft's [[directxmath]] supplies SIMD matrix/vector inlines and frustum helpers for DirectX-facing Windows/Xbox code paths. Per-title offset collections such as [[fortnite-w2s-offset-fortnite]] (Fortnite; gmh5225; view/projection and camera offsets for external ESP; cheat / game:fortnite `[Offset]`) document version-specific memory layouts upstream of the projection math. Educational internals with explicit W2S: [[simple-ac-internal-cheat]]. Beginner walkthrough labs such as [[lab-esp-and-aimbot]] (custom 3D target app + external cheat; ESP + aimbot from scratch) teach the same pipeline in a controlled practice environment. (source: wiki/sources/descriptions/kotae4__lab-esp-and-aimbot.md) (source: wiki/sources/descriptions/gmh5225__fortnite-W2S-offset-Fortnite.md)

## Related

[[present-hook]] · [[unreal-object-model]] · [[source-netvars]] · [[omath]] · [[directxmath]] · [[fortnite-w2s-offset-fortnite]] · [[lab-esp-and-aimbot]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
