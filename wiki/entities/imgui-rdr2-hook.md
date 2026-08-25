---
title: ImGuiRDR2Hook
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/Halen84__ImGuiRDR2Hook.md
updated: 2026-08-25
confidence: medium
---

# ImGuiRDR2Hook

**ImGuiRDR2Hook** (Halen84/ImGuiRDR2Hook) is a **Red Dead Redemption 2 hook framework** for rendering custom **Dear ImGui** menus through **Vulkan** and **DirectX 12**. Implemented in **C++**, it integrates common hooking components—**MinHook**, **Kiero**, and Dear ImGui—to intercept rendering paths. The codebase provides hook entry points, render routines, configuration handling, and practical notes for stable menu drawing and input behavior. Mainly used for game overlay development, graphics API hooking practice, and game security experimentation. (source: wiki/sources/descriptions/Halen84__ImGuiRDR2Hook.md)

Sits in the dual-backend Present-hook overlay lane beside [[vulkan-hook]], [[universal-dear-imgui-hook]], and [[kisssart-cs2-cheat-base]] as a title-specific RDR2 scaffold combining Kiero API bootstrap with MinHook detours on both Vulkan and DX12 render paths.

## Architecture highlights

| Component | Role |
|-----------|------|
| Kiero | Runtime graphics API detection and method-table hook bootstrap |
| MinHook | Function detours on Present/swap render paths |
| Dear ImGui | In-game overlay menu and debug UI |
| Vulkan + DX12 | Dual-backend render-path interception for RDR2 |
| Config handling | Menu/settings persistence and runtime toggles |
| Input notes | Guidance for stable menu draw and input capture |

See [[present-hook]] for swap-chain Present interception patterns and [[kiero]] for cross-API hook bootstrap.

## Links

- Repo: https://github.com/Halen84/ImGuiRDR2Hook

## Related

[[present-hook]] · [[kiero]] · [[imgui]] · [[vulkan-hook]] · [[universal-dear-imgui-hook]] · [[d3dhook-imgui]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
