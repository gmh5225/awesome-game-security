---
title: Awesome Game Security Overview
kind: overview
topics: [overview]
sources:
  - wiki/sources/skills/overview.md
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/yucchiy__UniCli.md
  - wiki/sources/descriptions/wondeks__unity-mcp.md
  - wiki/sources/descriptions/yrgo__awesome-educational-games.md
  - wiki/sources/descriptions/uNetworking__uWebSockets.md
  - wiki/sources/descriptions/traccar__traccar-geocoder.md
  - wiki/sources/descriptions/topfreegames__pitaya.md
updated: 2026-07-20
confidence: high
---


# Awesome Game Security Overview

Curated resource list spanning offensive game hacking and defensive anti-cheat research, with heavy coverage of Windows internals, drivers, DMA, reverse engineering, and engine-specific surfaces. (source: wiki/sources/skills/overview.md)

## What this domain covers

The README organizes ~40 top-level sections: engines/rendering/`Mathematics` (~7; constexpr math/physics for gamedev+cheat)/`AI` asset tooling, offensive (`Cheat` ~2556), defensive (`Anti Cheat` ~597), platform hardening (`Windows Security Features`), mobile/console/emulator ecosystems (Switch ~7 / Xbox ~7 / PlayStation ~5 HV+BD-JB / Game Boy ~3 / 3DS LLE / GameCube·Wii), and supporting gamedev infrastructure (`Game Develop` Guide / MCP / AI Agents—e.g. Unity Editor terminal CLI [[unicli]], Unity MCP server [[unity-mcp]], educational-games list [[awesome-educational-games]]; `Game Tools`/`Testing`/`CI`/`Manager`). Prefer this wiki for synthesis; fall back to README → descriptions → archives for specific repos. (source: wiki/sources/README-categories.md) (source: wiki/sources/descriptions/yucchiy__UniCli.md) (source: wiki/sources/descriptions/wondeks__unity-mcp.md) (source: wiki/sources/descriptions/yrgo__awesome-educational-games.md)

## Skill routing (primary topics)

| Topic | Overview | Typical queries |
|-------|----------|-----------------|
| Anti-cheat | [[overviews/anti-cheat]] | EAC, BattlEye, Vanguard, detection |
| DMA | [[overviews/dma-attack]] | pcileech, FPGA, IOMMU |
| Game engine | [[overviews/game-engine]] | Unreal, Unity IL2CPP, Godot |
| Game hacking | [[overviews/game-hacking]] | memory, injection, overlays |
| Graphics API | [[overviews/graphics-api]] | Present hooks, DXGI, Vulkan |
| Mobile | [[overviews/mobile-security]] | Frida, Magisk, jailbreak |
| Reverse engineering | [[overviews/reverse-engineering]] | IDA, DBI, deobfuscation |
| Windows kernel | [[overviews/windows-kernel]] | callbacks, HVCI, PatchGuard |

## Core concepts

- [[easy-anti-cheat]], [[battleye]], [[vanguard]] — major AC products
- [[dma]], [[iommu]] — external memory access threat/defense
- [[hvci]], [[patchguard]], [[kernel-callbacks]], [[byovd]] — Windows trust stack
- [[present-hook]], [[il2cpp]], [[frida]] — graphics, engines, mobile RE

## README category map (high-signal)

Security-dense sections from the projected category map (40 top-level / ~36 resource cats): **Cheat** (~2556 links), **Anti Cheat** (~597), **DirectX** (~33) / OpenGL / Vulkan, **Windows Security Features** (~9), **Some Tricks** (~113), plus engine (`Game Engine` ~142; Unreal/Unity/Godot/Lumix plugins + detectors; adjacent `Mathematics` ~7 / `PhysX SDK` ~3 / `Renderer` ~16), gamedev infra (`Game Develop` ~177 MCP/AI Agents; `Game Network` ~25 JWT/Auth + Location/Geocoding; WebSocket/HTTP stacks such as [[uwebsockets]]; distributed multiplayer server frameworks such as [[pitaya]]; self-hosted OSM reverse geocoders such as [[traccar-geocoder]]; `AI`/`Game Assets`/`Image Codec` image→3D/mesh/splat/sprite + wgpu raster editors; `Game Tools` ~8 incl. RCE hardening; `Game Testing` ~19; `Game CI` ~3 incl. content-addressed game VCS; `Game Manager` ~1), WSA/emulator lanes (`Windows Emulator` ~7 hybrid kernel-driver AC analysis; `WSL` ~4), and console (Switch/Xbox/PlayStation HV+BD-JB / 3DS LLE / GameCube·Wii / Game Boy) categories. (source: wiki/sources/README-categories.md) (source: wiki/sources/descriptions/uNetworking__uWebSockets.md) (source: wiki/sources/descriptions/topfreegames__pitaya.md) (source: wiki/sources/descriptions/traccar__traccar-geocoder.md)
