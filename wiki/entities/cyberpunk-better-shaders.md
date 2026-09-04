---
title: Cyberpunk Better Shaders (Callisto SSS)
kind: entity
topics: [graphics-api, game-engine]
sources:
  - wiki/sources/descriptions/BlaneC__cyberpunk-better-shaders.md
  - wiki/sources/README-categories.md
updated: 2026-09-04
confidence: medium
---

# Cyberpunk Better Shaders (Callisto SSS)

**Callisto SSS** is a Cyberpunk 2077 graphics mod that improves path-traced skin rendering. It targets graphics modders and researchers studying real-time rendering pipelines, runtime shader interception, and BRDF replacement—not anti-cheat or security tooling. (source: wiki/sources/descriptions/BlaneC__cyberpunk-better-shaders.md)

## Rendering changes

Injects Callisto BRDF diffuse-Fresnel and retroreflection terms and replaces the engine subsurface-scattering blur kernel with a reshaped profile. Skin changes gate to engine-classified skin pixels so other materials remain bit-identical to vanilla at default settings. (source: wiki/sources/descriptions/BlaneC__cyberpunk-better-shaders.md)

## Mechanism

Two complementary hook paths:

1. **Vulkan implicit layer** (`VkLayer_callisto_spvswap`) — hot-swaps SPIR-V path-tracer ray-generation shaders at load time on **Linux via Proton**, identifying modules by embedded DXIL fingerprints.
2. **RED4ext plugin** — overwrites the runtime SSS diffusion texture through `CopyTextureRegion` hooks.

(source: wiki/sources/descriptions/BlaneC__cyberpunk-better-shaders.md)

## Toolchain

Ships a large reverse-engineering and development toolchain in C, Python, Lua, and shell scripts for SPIR-V patching, shader census, A/B testing, and verification workflows. (source: wiki/sources/descriptions/BlaneC__cyberpunk-better-shaders.md)

## Links

- Repo: https://github.com/blanec/cyberpunk-better-shaders

## Related

[[vocem-overlay]] · [[shader-injector]] · [[game-lag-reducer]] · [[present-hook]] · [[kiero2]] · [[overviews/graphics-api]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]
