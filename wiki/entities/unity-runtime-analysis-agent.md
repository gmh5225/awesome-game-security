---
title: Unity Runtime Analysis Agent
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/RectangleEquals__UnityRuntimeAnalysisAgent.md
updated: 2026-09-29
confidence: medium
---

# Unity Runtime Analysis Agent

**Unity Runtime Analysis Agent** (RectangleEquals/UnityRuntimeAnalysisAgent) is a **BepInEx** plugin that runs inside **Unity Mono** games on Windows and exposes a local API for observing—and, with explicit permission, modifying—a live session. Written in C#, it targets game security researchers, mod developers, and reverse engineers who need programmatic runtime access to shipped Unity titles. (source: wiki/sources/descriptions/RectangleEquals__UnityRuntimeAnalysisAgent.md)

README category: Cheat / BepInEx. Runtime half of the **UnityLudometryMCP** stack; pairs with companion tools such as AgentConsole and the UnityLudometryMCP server over authenticated local transport.

## Introspection

Deep runtime analysis includes managed assembly and IL inspection, cross-references, scene and **GameObject** hierarchy walks, and live object queries. (source: wiki/sources/descriptions/RectangleEquals__UnityRuntimeAnalysisAgent.md)

## Control and safety

Communication is limited to authenticated **local named pipes** or **loopback TCP**. Default mode is **read-only**; **Full** mode permits audited state changes. An in-game overlay logs activity and supports an emergency stop. (source: wiki/sources/descriptions/RectangleEquals__UnityRuntimeAnalysisAgent.md)

## Positioning

Complements GUI runtime inspectors such as [[unityexplorer]] and editor-side MCP bridges such as [[unity-mcp]] by exposing a machine-facing API for agents and scripts. Mono-only today—distinct from [[il2cpp]] dump/resolve workflows and IL2CPP-focused BepInEx plugins such as [[bepinex-il2cppbase]]. Loads through [[bepinex]] like other in-process Unity research plugins.

## Links

- Repo: https://github.com/RectangleEquals/UnityRuntimeAnalysisAgent

## Related

[[bepinex]] · [[unityexplorer]] · [[unity-mcp]] · [[il2cpp]] · [[ceasta]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
