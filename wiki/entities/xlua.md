---
title: xLua
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/Tencent__xLua.md
updated: 2026-08-20
confidence: medium
---

# xLua

Tencent **Lua ↔ C#** bridge for Unity, .NET, and Mono: two-way interop, runtime **hotfix** hooks, generated binding code, and GC-oriented performance options across C#, Lua, and native runtime pieces on multi-platform game clients. Teams use it for flexible gameplay scripting and live logic updates without frequent full client rebuilds—not an anti-cheat product, but a README **Game Hot Patch** / Unity scripting surface relevant to modding and client integrity research. (source: wiki/sources/descriptions/Tencent__xLua.md)

Sits beside [[hybridclr]] (IL2CPP hot-update interpreter) and [[injectfix]] (Unity C# logic hotfix) in the live-update lane; contrasts with Unreal-side Lua plugins such as [[luamachine]] and [[re-ue4ss]].

## Links

- Repo: https://github.com/Tencent/xLua

## Related

[[hybridclr]] · [[injectfix]] · [[luamachine]] · [[mono]] · [[il2cpp]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]
