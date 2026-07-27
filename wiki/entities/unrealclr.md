---
title: UnrealCLR
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/nxrighthere__UnrealCLR.md
updated: 2026-07-27
confidence: medium
---

# UnrealCLR

Unreal Engine plugin that embeds the .NET runtime (CoreCLR) so gameplay logic can be written in C#. Exposes .NET bindings for UE4/UE5 actors, components, input, physics, rendering, and Blueprints, with interop to native C++—aimed at UE developers preferring C# for game logic, not a cheat or anti-cheat artifact. (source: wiki/sources/descriptions/nxrighthere__UnrealCLR.md)

Sits beside other Unreal plugin / scripting samples ([[luamachine]], [[ue5-with-dear-imgui]], [[houdini-engine-for-unreal]]): LuaMachine is the Lua gameplay bridge; this repo is the CoreCLR / .NET 6 managed-scripting bridge in the Plugins:Unreal lane. Distinct from [[unrealsharp]] (SDK View explorer in the Cheat lane).

## Links

- Repo: https://github.com/nxrighthere/UnrealCLR (README: Unreal Engine .NET 6 integration)

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[luamachine]] · [[unrealsharp]] · [[ue5-with-dear-imgui]] · [[houdini-engine-for-unreal]] · [[stride]] · [[flatredball]]
