---
title: Grembyte
kind: entity
topics: [game-hacking, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/grembyte__grembyte.md
updated: 2026-11-13
confidence: medium
---

# Grembyte

**Grembyte** (grembyte/grembyte) is an **alpha** desktop application for inspecting and manipulating memory in running games on **Linux**, **Windows**, and Windows titles under **Wine** or **Proton**. The stack is primarily **Python** with a **PySide6** UI; it injects **Frida-based JavaScript** into target processes for live memory work. Core features include value **scanning and freezing**, **pointer scans**, read and write **watches**, **JavaScript hooks** on memory writes, **scheduled scripts**, a **headless CLI** launch mode, and **native tracing** plus function monitoring. Engine-specific tooling covers **Unity Mono** and **IL2CPP** and **Unreal Engine** (class and method catalogs, object inspection, method hooks, **GAS** attribute views). The project targets educational use, security research, and **single-player modding**—not online play or anti-cheat evasion. (source: wiki/sources/descriptions/grembyte__grembyte.md)

README lists it as an alpha **desktop memory scanner and hooking workbench** for single-player games on Linux and Windows, with Unity Mono/IL2CPP and Unreal class browsing, Frida hooks, and Wine/Proton support (Cheat category). (source: wiki/sources/descriptions/grembyte__grembyte.md)

## Links

- Repo: https://github.com/grembyte/grembyte

## Related

[[frida]] · [[hermes-hook]] · [[frida-orbit-lab]] · [[pince]] · [[il2cpp]] · [[dynamic-binary-instrumentation]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
