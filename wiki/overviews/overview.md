---
title: Awesome Game Security Overview
kind: overview
topics: [overview]
sources:
  - wiki/sources/skills/overview.md
  - wiki/sources/README-categories.md
updated: 2026-07-17
confidence: high
---

# Awesome Game Security Overview

Curated resource list spanning offensive game hacking and defensive anti-cheat research, with heavy coverage of Windows internals, drivers, DMA, reverse engineering, and engine-specific surfaces. (source: wiki/sources/skills/overview.md)

## What this domain covers

The README organizes ~40 top-level sections: engines/rendering, offensive (`Cheat`), defensive (`Anti Cheat`), platform hardening (`Windows Security Features`), mobile/console/emulator ecosystems, and supporting gamedev infrastructure (including MCP/AI-agent tooling under `Game Develop`). Prefer this wiki for synthesis; fall back to README → descriptions → archives for specific repos.

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

Security-dense sections from the projected category map (40 top-level): **Cheat** (~2540 links), **Anti Cheat** (~590), **DirectX/OpenGL/Vulkan**, **Windows Security Features**, **Some Tricks**, plus engine, WSA/emulator, and console (Switch/Xbox/PlayStation) categories. (source: wiki/sources/README-categories.md)
