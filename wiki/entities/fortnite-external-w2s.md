---
title: fortnite-external-w2s
kind: entity
topics: [game-hacking, graphics-api, game-engine]
sources:
  - wiki/sources/descriptions/Zetolac__FortniteExternalW2S.md
updated: 2026-08-19
confidence: medium
---

# fortnite-external-w2s

C++ **proof of concept** for external **world-to-screen (W2S)** math in Fortnite (Zetolac; cheat / game:fortnite). Reads and decrypts camera/viewpoint data from process memory, then converts 3D world positions to 2D screen coordinates via matrix construction, axis transformation, and perspective projection—the same pipeline used by external ESP overlays. Intended as a foundation for external visualization tooling in game-hacking research rather than a full cheat stack. (source: wiki/sources/descriptions/Zetolac__FortniteExternalW2S.md)

Complements offset-only references such as [[fortnite-w2s-offset-fortnite]] and camera-cache samples such as [[fortnite-camera-cache-pov]] by demonstrating runnable external W2S math; pairs with [[fortnite-offsets-and-sigs]] from the same maintainer for offset/signature maintenance workflows.

## Links

- Repo: https://github.com/Zetolac/FortniteExternalW2S

## Related

[[world-to-screen]] · [[fortnite-w2s-offset-fortnite]] · [[fortnite-camera-cache-pov]] · [[fortnite-offsets-and-sigs]] · [[fortnite-external-cheat-base]] · [[unreal-object-model]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
