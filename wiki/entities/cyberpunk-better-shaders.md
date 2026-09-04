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

Cyberpunk 2077 graphics mod that improves path-traced skin via Callisto BRDF diffuse-Fresnel and retroreflection terms plus a reshaped subsurface-scattering blur kernel. Uses a custom **Vulkan implicit layer** (`VkLayer_callisto_spvswap`) to hot-swap SPIR-V path-tracer ray-generation shaders at load time on **Linux via Proton**, identifying modules by embedded DXIL fingerprints; a RED4ext plugin overwrites the runtime SSS diffusion texture through CopyTextureRegion hooks. Ships C/Python/Lua/shell tooling for SPIR-V patching, shader census, A/B testing, and verification. Skin changes gate to engine-classified skin pixels so other materials stay bit-identical at default settings — useful for studying runtime shader interception and BRDF replacement in shipping titles. (source: wiki/sources/descriptions/BlaneC__cyberpunk-better-shaders.md)

## Links

- Repo: https://github.com/blanec/cyberpunk-better-shaders

## Related

[[vocem-overlay]] · [[shader-injector]] · [[game-lag-reducer]] · [[present-hook]] · [[kiero2]] · [[overviews/graphics-api]] · [[overviews/game-engine]]
