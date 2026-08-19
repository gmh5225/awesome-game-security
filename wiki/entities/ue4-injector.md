---
title: UE4Injector
kind: entity
topics: [game-hacking, game-engine, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Zebratic__UE4Injector.md
updated: 2026-08-19
confidence: medium
---

# UE4Injector

Proof-of-concept **C++ injector** that demonstrates a **Unreal Engine 4 vulnerability** for loading **shellcode or DLL payloads** into target game processes. Ships as a Visual Studio project with command-line usage, build guidance, and notes on **privilege requirements** and deployment. The repository documents the injection workflow and frames the code as **legacy research** that may still affect **unpatched UE4 titles**—primarily for security research into UE4 process-injection vectors and their **anti-cheat implications**. (source: wiki/sources/descriptions/Zebratic__UE4Injector.md)

Contrasts with general Windows injection catalogs such as [[windows-process-injection]], training injectors such as [[guided-hacking-injector]], and UE SDK/dumper workflows that assume conventional in-process tooling such as [[unrealdumper-4-25]] and [[ue4genny]].

## Links

- Repo: https://github.com/Zebratic/UE4Injector

## Related

[[overviews/game-hacking]] · [[overviews/game-engine]] · [[unreal-object-model]] · [[windows-process-injection]] · [[guided-hacking-injector]] · [[injectors]] · [[the-perfect-injector]]
