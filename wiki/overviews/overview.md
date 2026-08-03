---
title: Awesome Game Security Overview
kind: overview
topics: [overview]
sources:
  - wiki/sources/skills/overview.md
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/yucchiy__UniCli.md
  - wiki/sources/descriptions/neogeek__get-unity.md
  - wiki/sources/descriptions/nowsprinting__UnityAutomatedQAExamples.md
  - wiki/sources/descriptions/leigest519__OpenGame.md
  - wiki/sources/descriptions/nikaera__Unity-GameCI-Sample.md
  - wiki/sources/descriptions/kvick-games__UnrealMCP.md
  - wiki/sources/descriptions/wondeks__unity-mcp.md
  - wiki/sources/descriptions/justinpbarnett__unity-mcp.md
  - wiki/sources/descriptions/regenrek__deepwiki-mcp.md
  - wiki/sources/descriptions/noopstudios__interactive-feedback-mcp.md
  - wiki/sources/descriptions/n24q02m__better-godot-mcp.md
  - wiki/sources/descriptions/johnhalloran321__mcpSafetyScanner.md
  - wiki/sources/descriptions/yrgo__awesome-educational-games.md
  - wiki/sources/descriptions/michelpereira__awesome-open-source-games.md
  - wiki/sources/descriptions/notpresident35__learn-awesome-gamedev.md
  - wiki/sources/descriptions/killop__anything_about_game.md
  - wiki/sources/descriptions/uNetworking__uWebSockets.md
  - wiki/sources/descriptions/traccar__traccar-geocoder.md
  - wiki/sources/descriptions/topfreegames__pitaya.md
  - wiki/sources/descriptions/ketoo__NoahGameFrame.md
  - wiki/sources/descriptions/socketio__socket.io.md
  - wiki/sources/descriptions/mqttjs__MQTT.js.md
  - wiki/sources/descriptions/mcxiaoke__mqtt.md
  - wiki/sources/descriptions/tomlooman__ue4-tutorials.md
  - wiki/sources/descriptions/revan1611__UE-Interview-Cheat-Sheet.md
  - wiki/sources/descriptions/tomlooman__SimpleFPSTemplate.md
  - wiki/sources/descriptions/tomlooman__EpicSurvivalGame.md
  - wiki/sources/descriptions/tomlooman__ActionRoguelike.md
  - wiki/sources/descriptions/stackOverflower92__FightingGame-UE5.md
  - wiki/sources/descriptions/perfect-hand__ue5-cardgame.md
  - wiki/sources/descriptions/pafuhana1213__VTuberWithUE4.md
  - wiki/sources/descriptions/pafuhana1213__KawaiiPhysics.md
  - wiki/sources/descriptions/ticarpi__jwt_tool.md
  - wiki/sources/descriptions/thomaseichhorn__cs16-client.md
  - wiki/sources/descriptions/solidi__hl-mods.md
  - wiki/sources/descriptions/sxlmnwb__windows-subsystem-linux.md
  - wiki/sources/descriptions/swordjoinmagic__MoBaDemo.md
  - wiki/sources/descriptions/shadirvan__Unity-Cheat-Sheet.md
  - wiki/sources/descriptions/ls361664056__GameAI-paper-list.md
  - wiki/sources/descriptions/lightningpixel__modly.md
  - wiki/sources/descriptions/skywind3000__kcp.md
  - wiki/sources/descriptions/ryanjon2040__UnrealNetworkProfiler.md
  - wiki/sources/descriptions/ryanjon2040__Unreal-Binary-Builder.md
  - wiki/sources/descriptions/sergiovillaverde__win11_apk_installer.md
  - wiki/sources/descriptions/recastnavigation__recastnavigation.md
  - wiki/sources/descriptions/raizam__gamedev_libraries.md
  - wiki/sources/descriptions/ppy__osu.md
  - wiki/sources/descriptions/ppy__osu-framework.md
  - wiki/sources/descriptions/plibither8__2048.cpp.md
  - wiki/sources/descriptions/playgameservices__cpp-android-basic-samples.md
  - wiki/sources/descriptions/nem0__lumixengine_maps.md
updated: 2026-08-03
confidence: high
---


# Awesome Game Security Overview

Curated resource list spanning offensive game hacking and defensive anti-cheat research, with heavy coverage of Windows internals, drivers, DMA, reverse engineering, and engine-specific surfaces. (source: wiki/sources/skills/overview.md)

## What this domain covers

The README organizes ~40 top-level sections: engines/rendering/`Mathematics` (~7; constexpr math/physics for gamedev+cheat)/`Renderer` (~17; incl. ReShade post-processing inject)/`AI` (~5; local desktop image→3D e.g. [[modly]], YAML→GLB factories, 2D sprite sheets; zh game-AI paper list [[gameai-paper-list]])/`Image Codec` (~5; wgpu/Rhai raster editors such as PaintFE), offensive (`Cheat` ~2646 incl. mytechnotalent Rust/Go/embedded RE course lanes + [[gamehacking-cheatsheet]] guide), defensive (`Anti Cheat` ~640 incl. hybrid CS2 judge/honeypot proposals + Minecraft Java/Bedrock anticheat catalog + structured AC/kernel/VT-x/graphics-integrity research index xhscfq/anti-cheat-research-index), platform hardening (`Windows Security Features`), mobile/console/emulator ecosystems (Switch ~7 / Xbox ~8 LLE/HLE + X360/XBE patch + SystemOS kernel exploit / PlayStation ~7 HV+BD-UN-JB RemoteJarLoader / WebKit CSSFontFace / PSFree-Enhanced host / Game Boy ~3 / Nintendo 3DS ~3 incl. Hydr8gon 3Beans full LLE boot + Luma `.3gx` overlays / GameCube·Wii ~1 Rust gecko emulator / Linux Emulator ~1 felix86), and supporting gamedev infrastructure (`Game Develop` ~182 Guide / MCP server/security / AI Agents—e.g. Unity Editor terminal CLI [[unicli]], Unreal MCP [[unreal-mcp]], Unity MCP server [[unity-mcp]], Godot 4.x composite MCP [[better-godot-mcp]], DeepWiki docs MCP [[deepwiki-mcp]], interactive user-feedback MCP [[interactive-feedback-mcp]], educational-games list [[awesome-educational-games]], open-source games collection [[awesome-open-source-games]], gamedev learning mega-list [[learn-awesome-gamedev]], cross-discipline game-development resource index [[anything-about-game]], data-oriented C/C++ gamedev libraries [[gamedev-libraries]], Unity cheat sheet [[unity-cheat-sheet]], UE interview cheat sheet [[ue-interview-cheat-sheet]], UE4 C++ tutorials [[ue4-tutorials]] (audio/physics/animation), UE4 FPS demo [[simple-fps-template]], UE4 FPS course [[epic-survival-game]], UE Roguelike [[action-roguelike]], UE5 fighting game [[fightinggame-ue5]], UE5 card game [[ue5-cardgame]], UE4 VTuber [[vtuber-with-ue4]], UE4/UE5 fake physics [[kawaii-physics]], rewrote CS1.6 client [[cs16-client]], Half-Life/GoldSrc mods [[hl-mods]], Unity MOBA demo [[mobademo]], C# rhythm client [[osu]] on [[osu-framework]], terminal C++ 2048 [[2048-cpp]], Google Play Games C++ SDK samples [[cpp-android-basic-samples]]; `Game Tools`/`Testing`/`CI`/`Manager`). Prefer this wiki for synthesis; fall back to README → descriptions → archives for specific repos. (source: wiki/sources/README-categories.md) (source: wiki/sources/descriptions/yucchiy__UniCli.md) (source: wiki/sources/descriptions/kvick-games__UnrealMCP.md) (source: wiki/sources/descriptions/wondeks__unity-mcp.md) (source: wiki/sources/descriptions/justinpbarnett__unity-mcp.md) (source: wiki/sources/descriptions/n24q02m__better-godot-mcp.md) (source: wiki/sources/descriptions/regenrek__deepwiki-mcp.md) (source: wiki/sources/descriptions/noopstudios__interactive-feedback-mcp.md) (source: wiki/sources/descriptions/yrgo__awesome-educational-games.md) (source: wiki/sources/descriptions/michelpereira__awesome-open-source-games.md) (source: wiki/sources/descriptions/notpresident35__learn-awesome-gamedev.md) (source: wiki/sources/descriptions/killop__anything_about_game.md) (source: wiki/sources/descriptions/raizam__gamedev_libraries.md) (source: wiki/sources/descriptions/shadirvan__Unity-Cheat-Sheet.md) (source: wiki/sources/descriptions/revan1611__UE-Interview-Cheat-Sheet.md) (source: wiki/sources/descriptions/tomlooman__ue4-tutorials.md) (source: wiki/sources/descriptions/tomlooman__SimpleFPSTemplate.md) (source: wiki/sources/descriptions/tomlooman__EpicSurvivalGame.md) (source: wiki/sources/descriptions/tomlooman__ActionRoguelike.md) (source: wiki/sources/descriptions/stackOverflower92__FightingGame-UE5.md) (source: wiki/sources/descriptions/perfect-hand__ue5-cardgame.md) (source: wiki/sources/descriptions/pafuhana1213__VTuberWithUE4.md) (source: wiki/sources/descriptions/pafuhana1213__KawaiiPhysics.md) (source: wiki/sources/descriptions/thomaseichhorn__cs16-client.md) (source: wiki/sources/descriptions/solidi__hl-mods.md) (source: wiki/sources/descriptions/swordjoinmagic__MoBaDemo.md) (source: wiki/sources/descriptions/ppy__osu.md) (source: wiki/sources/descriptions/ppy__osu-framework.md) (source: wiki/sources/descriptions/plibither8__2048.cpp.md) (source: wiki/sources/descriptions/playgameservices__cpp-android-basic-samples.md) (source: wiki/sources/descriptions/lightningpixel__modly.md)

## Skill routing (primary topics)

| Topic | Overview | Typical queries |
|-------|----------|-----------------|
| Anti-cheat | [[overviews/anti-cheat]] | EAC, BattlEye, Vanguard, detection |
| DMA | [[overviews/dma-attack]] | pcileech, FPGA, IOMMU |
| Game engine | [[overviews/game-engine]] | Unreal, Unity IL2CPP, Godot |
| Game hacking | [[overviews/game-hacking]] | memory, injection, overlays |
| Graphics API | [[overviews/graphics-api]] | Present hooks, DXGI, Vulkan |
| Mobile | [[overviews/mobile-security]] | Frida, Magisk, jailbreak |
| Reverse engineering | [[overviews/reverse-engineering]] | IDA, DBI, deobfuscation, MCP RE tools |
| Windows kernel | [[overviews/windows-kernel]] | callbacks, HVCI, PatchGuard |
| Research rigor | [[research-rigor]] | claim validation, citation checks, detector evaluation |
| Project maintenance | (this page) | adding resources, README format, link validation |

Also check `wiki/overviews/<topic>.md` for the matching primary skill topic before deep README or archive dives. (source: wiki/sources/skills/overview.md)

## Answer priority (data layers)

Prefer the [[compiled-wiki]] layer for cross-cutting synthesis; fall back in order when a repo-specific answer is needed: (source: wiki/sources/skills/overview.md)

1. Wiki entity/concept/overview (if present)
2. `description/{owner}/{repo}/description_en.txt` (concise English summary)
3. `archive/{owner}/{repo}.txt` (full code snapshot; avoid for high-level questions)
4. README category entry

Treat README entries, generated descriptions, wiki pages, and archives as **discovery/provenance** layers—not automatic proof of embedded claims. Pair domain skills with [[research-rigor]] for consequential security conclusions.

## Contributing & README format

Each README category uses `## Category Name`, optional `> Subcategory`, and bullet links with full URLs plus `[brief description]`. Before adding entries: check duplicates, verify links, place by primary function, and tag language/platform when helpful (e.g. `[Rust]`, `[Unity]`). Quality bar: actively maintained or historically significant, unique value, prefer original repos over forks unless the fork adds substantial work. (source: wiki/sources/skills/overview.md)

Maintenance scripts under `scripts/`: `generate-toc.py` (TOC generation), `remove-forks.py` (fork cleanup).

## Core concepts

- [[compiled-wiki]], [[research-rigor]] — synthesis layer and evidence discipline
- [[easy-anti-cheat]], [[battleye]], [[vanguard]] — major AC products
- [[dma]], [[iommu]] — external memory access threat/defense
- [[hvci]], [[patchguard]], [[kernel-callbacks]], [[byovd]] — Windows trust stack
- [[present-hook]], [[il2cpp]], [[frida]] — graphics, engines, mobile RE

## README category map (high-signal)

Security-dense sections from the projected category map (40 top-level / ~36 resource cats): **Cheat** (~2646 links), **Anti Cheat** (~640), **DirectX** (~37; D3D12 pixel-shader inject e.g. FF7 Rebirth + cross-API runtime shader capture/flatten) / **OpenGL** (~3) / **Vulkan** (~10; kiero2 cross-platform API locators), **Windows Security Features** (~9), **Some Tricks** (~113), plus engine (`Game Engine` ~154; Unreal/Unity/Godot/Lumix plugins (e.g. OSM map downloader [[lumixengine-maps]]) + detectors; adjacent `Mathematics` ~7 / `PhysX SDK` ~3 / `Renderer` ~17 incl. ReShade) (source: wiki/sources/descriptions/nem0__lumixengine_maps.md), gamedev infra (`Game Develop` ~182 MCP server/security + AI Agents; MCP safety auditing such as [[mcp-safety-scanner]] (agent-driven audit/remediation) (source: wiki/sources/descriptions/johnhalloran321__mcpSafetyScanner.md); `Game Network` ~26 JWT/Auth (e.g. [[jwt-tool]] validate/forge/scan) + Location/Geocoding; reliable-UDP ARQ such as [[kcp]]; WebSocket/HTTP stacks such as [[uwebsockets]]; Node.js/browser event-based real-time stacks such as [[socket-io]]; MQTT v3.1.1 spec reference (Chinese) such as [[mqtt]]; MQTT pub/sub clients such as [[mqtt-js]]; distributed multiplayer server frameworks such as [[pitaya]] / C++ server engines such as [[noahgameframe]]; self-hosted OSM reverse geocoders such as [[traccar-geocoder]]; `AI` (~5) / `Game Assets` (~11; YAML→GLB + AI sprite sheets) / `Image Codec` (~5; [[stb]] + wgpu/Rhai raster editors) / `Game Hot Patch` (~3; HybridCLR/xLua/InjectFix); `Game Tools` ~8 incl. RCE hardening + UE source builders such as [[unreal-binary-builder]] + UE network profilers such as [[unreal-network-profiler]] + Unity download-URL CLI [[get-unity]] (source: wiki/sources/descriptions/neogeek__get-unity.md) + navmesh toolsets such as [[recastnavigation]] (source: wiki/sources/descriptions/recastnavigation__recastnavigation.md); `Game Testing` ~19 (e.g. agentic web-game QA [[opengame]]; Unity automated QA guidebook [[unity-automated-qa-examples]]); `Game CI` ~3 incl. Unity sample [[unity-gameci-sample]] + Epic lore content-addressed VCS; `Game Manager` ~1) (source: wiki/sources/descriptions/leigest519__OpenGame.md) (source: wiki/sources/descriptions/nowsprinting__UnityAutomatedQAExamples.md) (source: wiki/sources/descriptions/nikaera__Unity-GameCI-Sample.md), WSA/emulator lanes (`WSA` ~9 incl. Win11 APK installers such as [[win11-apk-installer]]; `Windows Emulator` ~7 WHP trap-driven guests + hybrid KDemu kernel-driver AC analysis; `Android Emulator` ~9 incl. Snapdragon Droid-VM/Gunyah; `WSL` ~4 incl. [[windows-subsystem-linux]] full Linux-kernel trees; `Linux Emulator` ~1 felix86) (source: wiki/sources/descriptions/sergiovillaverde__win11_apk_installer.md) (source: wiki/sources/descriptions/sxlmnwb__windows-subsystem-linux.md), and console (Switch ~7 / Xbox ~8 LLE/HLE + X360 patch + SystemOS exploit / PlayStation ~7 HV+BD-UN-JB / PSFree-Enhanced / Nintendo 3DS ~3 incl. 3Beans LLE + Luma overlays / GameCube·Wii ~1 gecko / Game Boy ~3) categories. (source: wiki/sources/README-categories.md) (source: wiki/sources/descriptions/uNetworking__uWebSockets.md) (source: wiki/sources/descriptions/socketio__socket.io.md) (source: wiki/sources/descriptions/mqttjs__MQTT.js.md) (source: wiki/sources/descriptions/mcxiaoke__mqtt.md) (source: wiki/sources/descriptions/topfreegames__pitaya.md) (source: wiki/sources/descriptions/ketoo__NoahGameFrame.md) (source: wiki/sources/descriptions/traccar__traccar-geocoder.md) (source: wiki/sources/descriptions/ticarpi__jwt_tool.md) (source: wiki/sources/descriptions/skywind3000__kcp.md) (source: wiki/sources/descriptions/ryanjon2040__UnrealNetworkProfiler.md)
