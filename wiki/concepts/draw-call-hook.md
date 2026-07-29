---
title: Draw Call Hook
kind: concept
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/skills/graphics-api.md
updated: 2026-07-29
confidence: medium
---

# Draw Call Hook

Intercepting **draw submission** or **shader/pipeline state** instead of (or in addition to) the Present path—used for wallhack, chams, and render-debug research. Hook targets vary by API and engine render graph. (source: wiki/sources/skills/graphics-api.md)

## Hook targets

| API | Common intercepts |
|-----|-------------------|
| DirectX 11 | `ID3D11DeviceContext::Draw`, `DrawIndexed`; `OMSetDepthStencilState`, pixel-shader bind |
| DirectX 12 | Command-list recording hooks before `ExecuteCommandLists` |
| OpenGL | `glDrawElements`, `glDrawArrays`; legacy `glBegin`/`glEnd` |
| Vulkan | `vkCmdDraw`, `vkCmdDrawIndexed`; render-pass / pipeline bind |

Present-only overlays ([[present-hook]]) draw on top of the finished frame; draw-call hooks **modify what the game renders** (depth test off, replacement shaders).

## Wallhack and chams patterns

- **Depth disable** — `OMSetDepthStencilState` with depth test off so geometry draws through walls.
- **Shader replacement** — pixel shader returns flat team colors (chams) or semi-transparent tint.
- **Cross-API shader tooling** — README DirectX lane includes D3D12 injectors and cross-API runtime shader capture/flatten/replace for research on live pipelines.

Engine-specific samples often combine draw hooks with SDK offsets ([[battlefield-1-internal]], [[csgo-bot]] OpenGL/shader lane).

## Detection surface

Modified pipeline state, unexpected shader bytecode, draw-count anomalies, and integrity checks on device/context vtables overlap with [[present-hook]] detection. AC **Screenshot** and **Detection:ESP** lanes may correlate visual evidence with hook artifacts.

## Related

[[present-hook]] · [[world-to-screen]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
