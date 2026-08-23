---
title: ArcEngine
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/MohitSethi99__ArcEngine.md
updated: 2026-08-23
confidence: medium
---

# ArcEngine

Custom **C++** game engine with an integrated editor and scripting layer. The source tree includes subsystems for rendering, scene management, physics, audio, input, and tooling, plus platform-specific backends and shader assets. Ships a **C#** script core, **premake**-based build setup, vendor dependencies, and a sandbox project for running sample content—aimed at engine architecture experimentation and practical game development prototyping. (source: wiki/sources/descriptions/MohitSethi99__ArcEngine.md)

## Security-relevant surfaces

- **Native C++ + C# scripting** — mixed managed/native engine boundaries expose IL decompilation and native hooking paths typical of hybrid engine stacks.
- **Editor and sandbox tooling** — scene/asset pipelines and sample projects provide concrete targets for studying engine internals and content formats.
- **Rendering backends** — platform-specific render paths and shader assets align with standard [[present-hook]] and graphics API research.

Sits in the Game Engine / source lane beside [[mxengine]], [[lumos]], and [[spartan-engine]]—an OSS custom engine codebase for architecture and tooling study, not a cheat or anti-cheat artifact.

## Links

- Repo: https://github.com/MohitSethi99/ArcEngine

## Related

[[overviews/game-engine]] · [[overviews/graphics-api]] · [[mxengine]] · [[lumos]] · [[spartan-engine]] · [[doriax]] · [[present-hook]]
