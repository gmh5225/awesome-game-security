---
title: D3D12 Hook ImGui
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/DrNseven__D3D12-Hook-ImGui.md
updated: 2026-08-26
confidence: medium
---

# D3D12 Hook ImGui

**D3D12 Hook ImGui** (DrNseven/D3D12-Hook-ImGui) is a **Direct3D 12 hooking sample** that injects a **Dear ImGui** overlay into DX12 games. Implemented in **C++** with DirectX 12 APIs and **MinHook-style function interception**, it demonstrates practical **DLL build and injection flow**, **frame hook setup**, and **real-time menu rendering**. Mainly used for graphics API research, game overlay prototyping, and low-level game instrumentation studies. (source: wiki/sources/descriptions/DrNseven__D3D12-Hook-ImGui.md)

Sits in the DX12-only Present-hook overlay lane beside cross-API starters such as [[universal-dear-imgui-hook]], [[d3dhook-imgui]], and title-specific dual-backend scaffolds such as [[imgui-rdr2-hook]].

## Architecture highlights

| Component | Role |
|-----------|------|
| DirectX 12 | Target graphics API; swap-chain / frame render path |
| MinHook-style detours | Function interception on DX12 Present/frame hooks |
| Dear ImGui | In-game overlay menu and debug UI |
| DLL inject flow | Build, load, and hook lifecycle for in-process overlays |

See [[present-hook]] for swap-chain Present interception patterns and [[kiero]] for cross-API hook bootstrap when titles may use multiple backends.

## Links

- Repo: https://github.com/DrNseven/D3D12-Hook-ImGui

## Related

[[present-hook]] · [[imgui]] · [[d3dhook-imgui]] · [[universal-dear-imgui-hook]] · [[imgui-rdr2-hook]] · [[warzone-internal]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
