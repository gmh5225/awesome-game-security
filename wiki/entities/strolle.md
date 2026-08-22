---
title: Strolle
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/Patryk27__strolle.md
updated: 2026-08-22
confidence: medium
---

# Strolle

Real-time renderer focused on dynamic global illumination experiments. Implemented in Rust; runs standalone via **wgpu** or integrates as a component in **Bevy**-based projects. Emphasizes modern sampling and lighting techniques such as **ReSTIR** and targets usable performance on consumer GPUs without dedicated ray-tracing hardware. Aimed at graphics programmers and engine researchers prototyping advanced real-time lighting. (source: wiki/sources/descriptions/Patryk27__strolle.md)

Primary use case is rendering research and engine experimentation—not anti-cheat or reverse engineering. Sits beside other Rust wgpu engine surfaces ([[bevy]], [[nightshade]]) as a dynamic-GI / ReSTIR study surface.

## Links

- Repo: https://github.com/Patryk27/strolle (README tag: [Real-time rendering engine])

## Related

[[bevy]] · [[nightshade]] · [[paintfe]] · [[overviews/game-engine]] · [[overviews/graphics-api]]
