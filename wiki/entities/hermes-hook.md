---
title: Hermes Hook
kind: entity
topics: [game-hacking, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/winterhafen__hermes-hook.md
updated: 2026-11-07
confidence: medium
---

# Hermes Hook

**Hermes Hook** (winterhafen/hermes-hook) is a cross-platform desktop **memory inspection and hooking workbench** for running games on native **Linux**, **Windows**, and Windows titles under **Wine/Proton**. The stack is primarily **Python** with **JavaScript** hook scripts, using **Frida**, **ptrace**, and **Capstone** for attach, tracing, and disassembly. Features include memory and **pointer scanning**, read/write **watches**, instruction-level hooks that transform values in script, and engine-specific support for **Unity Mono/IL2CPP** and **Unreal Engine** (class catalogs, tracing, method hooks, scripted calls into game code). The tool targets researchers, modders, and reverse engineers on **offline or single-player** analysis, training, and memory-based modding—not online anti-cheat bypass. (source: wiki/sources/descriptions/winterhafen__hermes-hook.md)

README lists it as a **cross-platform Python game memory scanner and hooking workbench** with Unity/IL2CPP and Unreal class browsing, Frida-based Wine/Proton support, pointer scans, and scriptable hooks (Cheat category). (source: wiki/sources/descriptions/winterhafen__hermes-hook.md)

## Links

- Repo: https://github.com/winterhafen/hermes-hook

## Related

[[frida]] · [[grembyte]] · [[frida-orbit-lab]] · [[cheap-engine]] · [[pince]] · [[il2cpp]] · [[dynamic-binary-instrumentation]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
