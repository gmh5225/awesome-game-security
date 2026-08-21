---
title: ue4-processevent-intercept
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Skengdo__ue4-processevent-intercept.md
updated: 2026-08-21
confidence: medium
---

# ue4-processevent-intercept

**ue4-processevent-intercept** (Skengdo/ue4-processevent-intercept) is a compact **C++ library** for intercepting Unreal Engine 4 **ProcessEvent** calls on selected game objects. It uses **VMT shadowing** instead of direct vtable patching, and its hook lifecycle is designed to be **reapplied as objects are recreated**. The included example demonstrates capturing and modifying **gameplay-related function calls** at runtime. Primary use case: **UE4 reverse engineering** and **internal instrumentation** for game security research. (source: wiki/sources/descriptions/Skengdo__ue4-processevent-intercept.md)

Sits in the UE4 in-process dispatch hook lane beside render-hook scaffolds such as [[ue4-base]], SDK generators such as [[ue4genny]], and live modding stacks such as [[re-ue4ss]].

## Links

- Repo: https://github.com/Skengdo/ue4-processevent-intercept

## Related

[[unreal-object-model]] · [[ue4-base]] · [[ue4genny]] · [[re-ue4ss]] · [[fortnite-virtual-offsets]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
