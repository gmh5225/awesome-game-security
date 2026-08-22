---
title: OmegaWare Framework
kind: entity
topics: [game-hacking, graphics-api, game-engine]
sources:
  - wiki/sources/descriptions/Omega172__OmegaWare-Framework.md
updated: 2026-08-22
confidence: medium
---

# OmegaWare Framework

**Windows C++ foundation** (Omega172) for building **injected game modifications** with an in-game **Dear ImGui** overlay menu and developer console. Targets **Unity**, **Unreal Engine**, and other **DirectX-based** games through configurable engine profiles, automatic **D3D11/D3D12** renderer detection, and hooks on the **graphics pipeline** and **window procedure**. A **plugin-style feature system** with auto-registration, **JSON configuration**, localization, memory utilities, and compile-time **CRC64 string hashing** lets developers add modular capabilities without rewriting core injection logic. Built with **Xmake** in a **proxy plus internal DLL** layout for reverse engineers and game-security researchers studying cheat development techniques and anti-cheat countermeasures. (source: wiki/sources/descriptions/Omega172__OmegaWare-Framework.md)

Sits in the general-purpose **internal cheat-framework** lane beside modular backends such as [[blacksun-framework]] and universal graphics hook libs such as [[kiero]] / [[kiero2]].

## Links

- Repo: https://github.com/Omega172/OmegaWare-Framework

## Related

[[kiero]] · [[kiero2]] · [[present-hook]] · [[universal-dear-imgui-hook]] · [[blacksun-framework]] · [[il2cpp]] · [[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/game-engine]]
