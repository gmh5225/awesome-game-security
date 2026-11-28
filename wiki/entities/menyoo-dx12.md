---
title: Menyoo DX12
kind: entity
topics: [graphics-api, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/joeplenty__menyoo-dx12.md
updated: 2026-11-28
confidence: medium
---

# Menyoo DX12

**Menyoo DX12** (joeplenty/menyoo-dx12) is a pure **Rust** in-game mod menu and trainer overlay that composites a full Menyoo-style interface onto a **DirectX 12** swapchain, aimed at **GTA** titles on modern DXGI/D3D12 hosts. It ships a built-in **software rasterizer** for 1080p UI, a single-pass fullscreen-triangle upload path, floating preview cards, a real-time Post-FX studio, and procedural WinMM audio without external GUI crates. Runtime behavior is driven by an external **Schema v11.0** `rvas.json` with hot-reloadable RVAs, optional x64 callsite hooking, and JSON persistence for outfits, vehicles, and Spooner scenes instead of hardcoded binary offsets in the library. The stack targets Windows 10/11 mod developers, graphics integrators, and reverse engineers who study DXGI overlay injection, trainer frameworks, and cleanroom schema-based game scripting. (source: wiki/sources/descriptions/joeplenty__menyoo-dx12.md)

Compared with ImGui-on-Present scaffolds such as [[d3d12-hook-imgui]], Menyoo DX12 keeps UI rasterization in-process without Dear ImGui and decouples game version drift through an external RVA schema rather than embedded offsets.

## Architecture highlights

| Component | Role |
|-----------|------|
| D3D12 / DXGI swapchain | Present-path compositing target for trainer UI |
| Software rasterizer | 1080p Menyoo-style UI without external GUI dependencies |
| Schema v11.0 `rvas.json` | Hot-reloadable RVAs; optional x64 callsite hooks |
| JSON persistence | Outfits, vehicles, Object Spooner scenes |
| WinMM audio | Procedural UI audio without extra crates |

See [[present-hook]] for swap-chain overlay patterns and [[gta-5-trainer-menu-base]] for DX11/ImGui GTA trainer menu plumbing.

## Links

- Repo: https://github.com/joeplenty/menyoo-dx12

## Related

[[present-hook]] · [[d3d12-hook-imgui]] · [[ingame-overlay]] · [[gta-5-trainer-menu-base]] · [[yimmenu]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]