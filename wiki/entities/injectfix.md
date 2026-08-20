---
title: InjectFix
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/Tencent__InjectFix.md
updated: 2026-08-20
confidence: medium
---

# InjectFix

Tencent Unity **logic hotfix** framework: patch C# gameplay code at runtime without rebuilding the whole client. Uses IL tooling to inject and route patched logic; targets broad Unity version and platform coverage, including older projects that cannot be heavily refactored. Primary use case is fast bug fixing and controlled hot updates for live Unity games—not an anti-cheat product, but a README **Game Hot Patch** surface relevant to modding and client integrity research. (source: wiki/sources/descriptions/Tencent__InjectFix.md)

Sits beside [[xlua]] (Lua↔C# scripting hotfix) and [[hybridclr]] (IL2CPP hot-update interpreter) in the live-update lane.

## Links

- Repo: https://github.com/Tencent/InjectFix

## Related

[[xlua]] · [[hybridclr]] · [[mono]] · [[il2cpp]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]
