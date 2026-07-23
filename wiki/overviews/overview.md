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
  - wiki/sources/descriptions/socketio__socket.io.md
  - wiki/sources/descriptions/tomlooman__ue4-tutorials.md
  - wiki/sources/descriptions/tomlooman__SimpleFPSTemplate.md
  - wiki/sources/descriptions/tomlooman__EpicSurvivalGame.md
  - wiki/sources/descriptions/tomlooman__ActionRoguelike.md
  - wiki/sources/descriptions/stackOverflower92__FightingGame-UE5.md
  - wiki/sources/descriptions/ticarpi__jwt_tool.md
  - wiki/sources/descriptions/thomaseichhorn__cs16-client.md
  - wiki/sources/descriptions/solidi__hl-mods.md
  - wiki/sources/descriptions/sxlmnwb__windows-subsystem-linux.md
  - wiki/sources/descriptions/swordjoinmagic__MoBaDemo.md
  - wiki/sources/descriptions/shadirvan__Unity-Cheat-Sheet.md
  - wiki/sources/descriptions/skywind3000__kcp.md
  - wiki/sources/descriptions/sergiovillaverde__win11_apk_installer.md
updated: 2026-07-23
confidence: high
---


# Awesome Game Security Overview

Curated resource list spanning offensive game hacking and defensive anti-cheat research, with heavy coverage of Windows internals, drivers, DMA, reverse engineering, and engine-specific surfaces. (source: wiki/sources/skills/overview.md)

## What this domain covers

The README organizes ~40 top-level sections: engines/rendering/`Mathematics` (~7; constexpr math/physics for gamedev+cheat)/`Renderer` (~17)/`AI` asset tooling, offensive (`Cheat` ~2573), defensive (`Anti Cheat` ~607), platform hardening (`Windows Security Features`), mobile/console/emulator ecosystems (Switch ~7 / Xbox ~7 / PlayStation ~5 HV+BD-JB RemoteJarLoader / Game Boy ~3 / 3DS LLE / GameCube·Wii / Linux Emulator ~1), and supporting gamedev infrastructure (`Game Develop` Guide / MCP server/security / AI Agents—e.g. Unity Editor terminal CLI [[unicli]], Unity MCP server [[unity-mcp]], educational-games list [[awesome-educational-games]], Unity cheat sheet [[unity-cheat-sheet]], UE4 C++ tutorials [[ue4-tutorials]] (audio/physics/animation), UE4 FPS demo [[simple-fps-template]], UE4 FPS course [[epic-survival-game]], UE Roguelike [[action-roguelike]], UE5 fighting game [[fightinggame-ue5]], rewrote CS1.6 client [[cs16-client]], Half-Life/GoldSrc mods [[hl-mods]], Unity MOBA demo [[mobademo]]; `Game Tools`/`Testing`/`CI`/`Manager`). Prefer this wiki for synthesis; fall back to README → descriptions → archives for specific repos. (source: wiki/sources/README-categories.md) (source: wiki/sources/descriptions/yucchiy__UniCli.md) (source: wiki/sources/descriptions/wondeks__unity-mcp.md) (source: wiki/sources/descriptions/yrgo__awesome-educational-games.md) (source: wiki/sources/descriptions/shadirvan__Unity-Cheat-Sheet.md) (source: wiki/sources/descriptions/tomlooman__ue4-tutorials.md) (source: wiki/sources/descriptions/tomlooman__SimpleFPSTemplate.md) (source: wiki/sources/descriptions/tomlooman__EpicSurvivalGame.md) (source: wiki/sources/descriptions/tomlooman__ActionRoguelike.md) (source: wiki/sources/descriptions/stackOverflower92__FightingGame-UE5.md) (source: wiki/sources/descriptions/thomaseichhorn__cs16-client.md) (source: wiki/sources/descriptions/solidi__hl-mods.md) (source: wiki/sources/descriptions/swordjoinmagic__MoBaDemo.md)

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

Security-dense sections from the projected category map (40 top-level / ~36 resource cats): **Cheat** (~2573 links), **Anti Cheat** (~607), **DirectX** (~34) / OpenGL / Vulkan, **Windows Security Features** (~9), **Some Tricks** (~113), plus engine (`Game Engine` ~144; Unreal/Unity/Godot/Lumix plugins + detectors; adjacent `Mathematics` ~7 / `PhysX SDK` ~3 / `Renderer` ~17), gamedev infra (`Game Develop` ~179 MCP server/security + AI Agents; `Game Network` ~26 JWT/Auth (e.g. [[jwt-tool]] validate/forge/scan) + Location/Geocoding; reliable-UDP ARQ such as [[kcp]]; WebSocket/HTTP stacks such as [[uwebsockets]]; Node.js/browser event-based real-time stacks such as [[socket-io]]; distributed multiplayer server frameworks such as [[pitaya]]; self-hosted OSM reverse geocoders such as [[traccar-geocoder]]; `AI`/`Game Assets`/`Image Codec` image→3D/mesh/splat/sprite + wgpu raster editors; `Game Tools` ~8 incl. RCE hardening; `Game Testing` ~19; `Game CI` ~3 incl. content-addressed game VCS; `Game Manager` ~1), WSA/emulator lanes (`WSA` ~9 incl. Win11 APK installers such as [[win11-apk-installer]]; `Windows Emulator` ~7 hybrid kernel-driver AC analysis; `WSL` ~4 incl. [[windows-subsystem-linux]] full Linux-kernel trees; `Linux Emulator` ~1) (source: wiki/sources/descriptions/sergiovillaverde__win11_apk_installer.md) (source: wiki/sources/descriptions/sxlmnwb__windows-subsystem-linux.md), and console (Switch/Xbox/PlayStation HV+BD-JB RemoteJarLoader / 3DS LLE / GameCube·Wii / Game Boy) categories. (source: wiki/sources/README-categories.md) (source: wiki/sources/descriptions/uNetworking__uWebSockets.md) (source: wiki/sources/descriptions/socketio__socket.io.md) (source: wiki/sources/descriptions/topfreegames__pitaya.md) (source: wiki/sources/descriptions/traccar__traccar-geocoder.md) (source: wiki/sources/descriptions/ticarpi__jwt_tool.md) (source: wiki/sources/descriptions/skywind3000__kcp.md)
