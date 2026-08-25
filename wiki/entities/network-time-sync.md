---
title: NetworkTimeSync
kind: entity
topics: [game-engine]
sources:
  - wiki/sources/descriptions/Erlite__NetworkTimeSync.md
updated: 2026-08-25
confidence: medium
---

# NetworkTimeSync

**NetworkTimeSync** (Erlite/NetworkTimeSync) is an **Unreal Engine plugin** that provides more accurate **server world time synchronization** for multiplayer clients. Implemented in **C++** with **Blueprint-compatible** integration, it exposes synchronized time values to both native code and visual scripting. The plugin is structured for drop-in installation under a project plugins folder and focuses on reducing **time drift** in networked gameplay logic.

Primary audience: multiplayer game developers who need reliable shared clocks for simulation, timed events, and latency-sensitive mechanics—not anti-cheat or reverse-engineering tooling. (source: wiki/sources/descriptions/Erlite__NetworkTimeSync.md)

Sits in the UE **Plugins:Unreal** networking lane beside replication samples such as [[multiplayer-blaster-game]] and network analysis tooling such as [[unreal-network-profiler]].

## Links

- Repo: https://github.com/Erlite/NetworkTimeSync (README: simple UE subsystem for more accurate server world time on clients)

## Related

[[overviews/game-engine]] · [[multiplayer-blaster-game]] · [[unreal-network-profiler]] · [[game-networking-resources]] · [[lightyear]] · [[kcp]]
