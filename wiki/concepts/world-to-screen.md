---
title: World-to-Screen
kind: concept
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/skills/game-hacking.md
  - wiki/sources/descriptions/microsoft__DirectXMath.md
  - wiki/sources/descriptions/kotae4__lab-esp-and-aimbot.md
  - wiki/sources/descriptions/gmh5225__fortnite-W2S-offset-Fortnite.md
  - wiki/sources/descriptions/gmh5225__Call-Of-Duty-Warzone-Hack-Esp-Slient-Aimbot-Internal-Unlock-ALL.md
  - wiki/sources/descriptions/gmh5225__Call-Of-Duty-Vanguard-Hack-Esp-AImbot-Unlock-All.md
  - wiki/sources/descriptions/dword64__Ow-FOV.md
  - wiki/sources/descriptions/codereversing__hl2esp.md
  - wiki/sources/descriptions/Zetolac__FortniteExternalW2S.md
  - wiki/sources/descriptions/NullTerminatorr__NullBase.md
  - wiki/sources/descriptions/DrNseven__D3D11-Worldtoscreen-Finder.md
updated: 2026-08-26
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

Cross-engine constexpr libraries such as [[omath]] ship W2S, projectile prediction, and engine-specific camera helpers (Source, Unity, Unreal, Frostbite, etc.). Microsoft's [[directxmath]] supplies SIMD matrix/vector inlines and frustum helpers for DirectX-facing Windows/Xbox code paths. Per-title offset collections such as [[fortnite-w2s-offset-fortnite]] (Fortnite; gmh5225; view/projection and camera offsets for external ESP; cheat / game:fortnite `[Offset]`) document version-specific memory layouts upstream of the projection math. External W2S PoCs such as [[fortnite-external-w2s]] (Zetolac; C++; reads/decrypts camera POV from process memory; matrix construction + perspective projection for ESP overlays; cheat / game:fortnite) demonstrate the full external projection pipeline beside offset-only references. (source: wiki/sources/descriptions/Zetolac__FortniteExternalW2S.md) External title samples such as [[call-of-duty-warzone-hack-esp-slient-aimbot-internal-unlock-all]] (COD Warzone; C# Win32 RPM + user32 overlay ESP; gmh5225) and [[call-of-duty-vanguard-hack-esp-aimbot-unlock-all]] (COD Vanguard/Warzone; Win32 RPM + DirectX overlay ESP; gmh5225) apply the same projection math through out-of-process memory reads rather than in-engine hooks. Title-specific FOV manipulation such as [[ow-fov]] (Overwatch; dword64; injected DLL; cheat / game:overwatch [FOV]) alters the effective camera frustum that upstream W2S and aim-FOV boundary checks assume. (source: wiki/sources/descriptions/dword64__Ow-FOV.md) Educational internals with explicit W2S: [[simple-ac-internal-cheat]]. Source 1 Half-Life 2 hook-based ESP such as [[hl2esp]] (codereversing; C/C++; cheat / game:half-life 2) applies the same view-matrix projection through in-process Source client hooks. (source: wiki/sources/descriptions/codereversing__hl2esp.md) Beginner walkthrough labs such as [[lab-esp-and-aimbot]] (custom 3D target app + external cheat; ESP + aimbot from scratch) teach the same pipeline in a controlled practice environment. (source: wiki/sources/descriptions/kotae4__lab-esp-and-aimbot.md) Readable beginner cheat bases such as [[nullbase]] (NullTerminatorr; C++; memory helpers, entity/local-player abstractions, math + W2S building blocks; Visual Studio layout for framework-structure teaching) illustrate W2S in a minimal extensible scaffold. (source: wiki/sources/descriptions/NullTerminatorr__NullBase.md) In-process DX11 W2S discovery tools such as [[d3d11-worldtoscreen-finder]] (DrNseven; C++; MinHook + ImGui overlay; brute-forces matrix/constant-buffer combinations; draws model-position text and logs matched targets; bootstraps ESP/aim visual experiments) help locate usable projection math when view-matrix offsets are unknown. (source: wiki/sources/descriptions/DrNseven__D3D11-Worldtoscreen-Finder.md) (source: wiki/sources/descriptions/gmh5225__fortnite-W2S-offset-Fortnite.md) (source: wiki/sources/descriptions/gmh5225__Call-Of-Duty-Warzone-Hack-Esp-Slient-Aimbot-Internal-Unlock-ALL.md) (source: wiki/sources/descriptions/gmh5225__Call-Of-Duty-Vanguard-Hack-Esp-AImbot-Unlock-All.md)

## Related

[[present-hook]] · [[unreal-object-model]] · [[source-netvars]] · [[omath]] · [[directxmath]] · [[fortnite-w2s-offset-fortnite]] · [[fortnite-external-w2s]] · [[ow-fov]] · [[hl2esp]] · [[call-of-duty-vanguard-hack-esp-aimbot-unlock-all]] · [[call-of-duty-warzone-hack-esp-slient-aimbot-internal-unlock-all]] · [[lab-esp-and-aimbot]] · [[nullbase]] · [[d3d11-worldtoscreen-finder]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
