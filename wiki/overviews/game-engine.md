---
title: Game Engine
kind: overview
topics: [game-engine]
sources:
  - wiki/sources/skills/game-engine.md
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/zompi2__Static-Variables-Obfuscator-UE4.md
  - wiki/sources/descriptions/zinx-YT__Fortnite-Fltokens-and-offsets.md
  - wiki/sources/descriptions/zhitkur__DayZzz.md
  - wiki/sources/descriptions/yucchiy__UniCli.md
  - wiki/sources/descriptions/yring-me__ts-ue4dumper.md
  - wiki/sources/descriptions/yrgo__awesome-educational-games.md
  - wiki/sources/descriptions/yourmnbbn__tiny-csgo-client.md
  - wiki/sources/descriptions/yoshisaac__CounterStrikeSource-Linux-Trainer.md
  - wiki/sources/descriptions/yoshisaac__CounterStrike2-Linux-Cheat.md
  - wiki/sources/descriptions/yinleiCoder__cs2-cheat-cpp.md
  - wiki/sources/descriptions/xvorost__CS-2-Glow.md
  - wiki/sources/descriptions/xkp95175333__Thetan_ArenaSDK.md
updated: 2026-07-17
confidence: high
---




# Game Engine

Engine internals, plugins, detectors, and SDK workflows that underpin modding, reverse engineering, and anti-cheat integration points—especially Unreal, Unity ([[il2cpp]] / Mono), Source, Godot, and custom engines. (source: wiki/sources/skills/game-engine.md)

## Key sub-areas

**Engines:** Unreal (GObjects/GNames/GWorld, Dumper-7/UE4SS), Unity (IL2CPPDumper + metadata, Mono/dnSpy), Source (NetVars / CreateInterface), Godot/Lumix plugins. Editor-side Unity automation such as [[unicli]] (terminal CLI: compile/test/build/inspect; AI-agent ready) sits in Plugins:Unity / Game Develop rather than shipped-binary RE. (source: wiki/sources/descriptions/yucchiy__UniCli.md)

**Security-relevant surfaces:** object models and property offsets, rendering hooks ([[present-hook]]), network replication, engine-specific AC protection categories in the README. UE4 static-variable obfuscation (e.g. [[static-variables-obfuscator-ue4]]) raises the cost of memory scanners like Cheat Engine against non-dynamic game data. (source: wiki/sources/descriptions/zompi2__Static-Variables-Obfuscator-UE4.md) Per-title Unreal dumps such as Fortnite FLTokens/offsets ([[fortnite-fltokens-and-offsets]]) show how quickly build-bound token and offset maps go stale. (source: wiki/sources/descriptions/zinx-YT__Fortnite-Fltokens-and-offsets.md)


**SDK generation:** UE version signatures → dumpers; Unity `global-metadata.dat` + `GameAssembly.dll` / `libil2cpp.so`; Source ClientClass → RecvTable maps. Modular TypeScript/Frida UE4 dumps (e.g. [[ts-ue4dumper]], C++ offset path) sit alongside Dumper-7/UE4SS-style explorers. (source: wiki/sources/descriptions/yring-me__ts-ue4dumper.md) Per-title DayZ SDK/modding workflows (e.g. [[dayzzz]]) sit in the same Cheat SDK CodeGen / overlay lane. (source: wiki/sources/descriptions/zhitkur__DayZzz.md) Source/CS:GO-oriented minimal clients such as [[tiny-csgo-client]] (dedicated-server connect; modding / SDK generation) illustrate the Source-side end of that lane. (source: wiki/sources/descriptions/yourmnbbn__tiny-csgo-client.md) Linux external CS:S trainers such as [[counterstrikesource-linux-trainer]] (movement / info display) sit in the adjacent Source / game:css external lane. (source: wiki/sources/descriptions/yoshisaac__CounterStrikeSource-Linux-Trainer.md) Linux external CS2 memory-analysis cheats such as [[counterstrike2-linux-cheat]] sit in the Source 2 / game:cs2 external lane. (source: wiki/sources/descriptions/yoshisaac__CounterStrike2-Linux-Cheat.md) External CS2 samples such as [[cs2-cheat-cpp]] (rendering / asset pipelines / SDK generation) sit in the same Source 2 / game:cs2 external lane. (source: wiki/sources/descriptions/yinleiCoder__cs2-cheat-cpp.md) External glow ESP such as [[cs-2-glow]] (entity parse / offset management / glow via external memory) also sits in that Source 2 / game:cs2 external lane. (source: wiki/sources/descriptions/xvorost__CS-2-Glow.md) Per-title Thetan Arena SDKs such as [[thetan-arenasdk]] (rendering / audio / physics) sit in the adjacent Cheat SDK / game:thetan lane. (source: wiki/sources/descriptions/xkp95175333__Thetan_ArenaSDK.md)

## Related concepts

[[il2cpp]] · [[present-hook]] · [[frida]] (mobile IL2CPP) · [[ts-ue4dumper]] · [[static-variables-obfuscator-ue4]] · [[fortnite-fltokens-and-offsets]] · [[dayzzz]] · [[tiny-csgo-client]] · [[counterstrikesource-linux-trainer]] · [[counterstrike2-linux-cheat]] · [[cs2-cheat-cpp]] · [[cs-2-glow]] · [[thetan-arenasdk]] · [[unicli]] · [[awesome-educational-games]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]



## README map

`Game Engine` (~140 links: guides, source, Unreal/Unity/Godot/Lumix plugins, detectors). Adjacent: `Game Assets` (~10; UE/glTF + AI sprite/YAML→3D asset pipelines), `Game Hot Patch` (~3; HybridCLR/xLua/InjectFix), `Game Develop` (~176; Guide lists such as [[awesome-educational-games]], MCP server/security + AI Agents), `Game Network` (~25; Guide/Source + JWT/Auth Token + Location/Geocoding), `AI` (~5; local/Claude image→3D, Gaussian splat, 2D sprite-sheet generators for Unity/Unreal/Godot), plus Cheat SDK CodeGen and Anti Cheat `Game Engine Protection:*` subtrees. (source: wiki/sources/README-categories.md) (source: wiki/sources/descriptions/yrgo__awesome-educational-games.md)
