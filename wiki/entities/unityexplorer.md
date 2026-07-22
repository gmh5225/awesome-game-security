---
title: UnityExplorer
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/sinai-dev__UnityExplorer.md
updated: 2026-07-22
confidence: medium
---

# UnityExplorer

Runtime Unity inspector/debugger injectable into games via BepInEx or MelonLoader. Provides a live scene hierarchy, GameObject/Component inspector, C# REPL, mouse/freecam, and clipboard tools for examining and modifying game state at runtime. Uses reflection and [[il2cpp]] unhollowing so it works on both Mono and IL2CPP Unity builds. Aimed at Unity modders, game hackers, and researchers RE’ing Unity titles. (source: wiki/sources/descriptions/sinai-dev__UnityExplorer.md)

Complements offline dump/resolve tooling such as [[il2cpp-resolver]] and [[il2cpp-spy]], and live Frida bridges like [[frida-il2cpp-bridge]], when the goal is in-process hierarchy/REPL inspection rather than static metadata dumps alone. Distinct from editor-side automation such as [[unicli]] / [[unity-mcp]].

## Links

- Repo: https://github.com/sinai-dev/UnityExplorer

## Related

[[il2cpp]] · [[il2cpp-resolver]] · [[il2cpp-spy]] · [[frida-il2cpp-bridge]] · [[unity-vulnerable-entrypoint]] · [[unicli]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
