---
title: FlowGraph
kind: entity
topics: [game-engine]
sources:
  - wiki/sources/descriptions/MothCocoon__FlowGraph.md
updated: 2026-08-22
confidence: medium
---

# FlowGraph

Unreal Engine plugin providing a **design-agnostic event-flow graph system** for gameplay and narrative scripting. Implemented primarily in C++ with editor integration; emphasizes async node execution, custom pin layouts, and visual debugging. The architecture lets teams author reusable game-specific nodes and extend editor behavior without rewriting core graph logic—aimed at structured storytelling and gameplay flow authoring in Unreal projects, not anti-cheat or reverse-engineering work. (source: wiki/sources/descriptions/MothCocoon__FlowGraph.md)

Sits in the Game Engine Plugins:Unreal lane beside other graph-oriented editor plugins: [[generic-graph]] targets reusable graph data structures for tooling pipelines, while [[simple-quest]] narrows visual graph authoring to questline progression with runtime components and save/load.

## Links

- Repo: https://github.com/MothCocoon/FlowGraph (README: design-agnostic node system for scripting game flow in Unreal Engine)

## Related

[[overviews/game-engine]] · [[generic-graph]] · [[simple-quest]] · [[luamachine]] · [[automation-examples]] · [[unreal-engine-guide]]
