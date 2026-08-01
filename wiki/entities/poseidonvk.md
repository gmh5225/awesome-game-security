---
title: PoseidonVK
kind: entity
topics: [game-engine, graphics-api, reverse-engineering]
sources:
  - wiki/sources/descriptions/koosoli__PoseidonVK.md
updated: 2026-08-01
confidence: medium
---

# PoseidonVK

Community continuation of Bohemia Interactive's GPL source release for *Arma: Cold War Assault Remastered*, built around the Poseidon (CWR) game engine. Primarily modern C++20 with CMake; ships a dedicated Vulkan graphics backend alongside OpenGL and OpenAL Soft audio via SDL3. Includes format tooling and libFuzzer harnesses for classic Bohemia asset and script formats (PBO, P3D, PAA, SQF, network message decoding), plus a Blender P3D importer and developer studio apps; some supporting services and integration harnesses are written in Rust. Primary use case: remastering and studying the Operation Flashpoint / Cold War Assault engine for modding, portability, reverse engineering, and game-format security research. (source: wiki/sources/descriptions/koosoli__PoseidonVK.md)

Distinct from [[poseidon]] (kernel auxiliary-counter KM↔UM channel research).

## Links

- Repo: https://github.com/koosoli/PoseidonVK (README: [Vulkan modernization fork of the Poseidon/CWR-CE engine (Arma: Cold War Assault)])

## Related

[[overviews/game-engine]] · [[overviews/graphics-api]] · [[overviews/reverse-engineering]] · [[vk-engine]] · [[liblava]] · [[storm-engine]]
