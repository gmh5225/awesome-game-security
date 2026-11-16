---
title: HirschgangWare
kind: entity
topics: [dma-attack, game-hacking, graphics-api, windows-kernel]
sources:
  - wiki/sources/descriptions/weikiboy-tech__HirschgangWare.md
updated: 2026-11-16
confidence: medium
---

# HirschgangWare

**HirschgangWare** (weikiboy-tech/HirschgangWare) is an open-source **Windows external cheat for DayZ** that runs on a **separate machine** and reads the Enfusion game process through a **PCIe DMA device** using **PCILeech** and **MemProcFS**, without attaching to or writing memory on the gaming PC. Built in **C++17** with MSVC, **Dear ImGui**, and **DirectX 11**, it drives ESP overlays, a **secondary-monitor radar**, loot discovery, and gameplay assistance from live memory reads only. Input features such as a triggerbot and key handling use external hardware (**kmbox** or **MAKCU**) for [[hardware-input-injection]] so the host mouse chain can stay intact for the game client. The repository documents offset discovery, **kernel-session keyboard state** resolution through VMM APIs, and operational notes for researchers studying external cheating architectures, DMA-based evasion, and related game-security reverse engineering. (source: wiki/sources/descriptions/weikiboy-tech__HirschgangWare.md)

## Research framing

Targets analysts comparing **second-PC DMA** DayZ stacks with same-host externals ([[dayz-esp]] BYOVD kernel reads, [[external-dayz-cheat]] custom driver overlays) under [[battleye]]—not production deployment guidance. (source: wiki/sources/descriptions/weikiboy-tech__HirschgangWare.md)

## Positioning

Listed under README **Cheat** as game:dayz **[DMA External]** beside other DayZ samples ([[dayz-cheat]], [[dayzzz]], [[dayz-mcp]]) but distinct in running all cheat logic and rendering off the target OS with optional HID actuators on a separate input path.

## Links

- Repo: https://github.com/weikiboy-tech/HirschgangWare [Open-source DayZ external DMA cheat: MemProcFS/PCILeech reads, ESP overlay, second-monitor radar, loot filters, and kmbox/MAKCU triggerbot]

## Related

[[dma]] · [[pcileech]] · [[battleye]] · [[world-to-screen]] · [[hardware-input-injection]] · [[dayz-esp]] · [[external-dayz-cheat]] · [[dayz-cheat]] · [[overviews/dma-attack]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]