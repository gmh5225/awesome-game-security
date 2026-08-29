---
title: Source NetVars
kind: concept
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/skills/game-engine.md
  - wiki/sources/descriptions/ikhsanprasetyo__dota2dumped.md
  - wiki/sources/descriptions/guided-hacking__GH-Offset-Dumper.md
  - wiki/sources/descriptions/guided-hacking__GH-Entity-List-Finder.md
  - wiki/sources/descriptions/gmh5225__source-sdk-orangebox.md
  - wiki/sources/descriptions/gmh5225__csso-src.md
  - wiki/sources/descriptions/gmh5225__csgo_sdk.md
  - wiki/sources/descriptions/gmh5225__csgo-sdk.md
  - wiki/sources/descriptions/bloesway__csgo_sdk.md
  - wiki/sources/descriptions/gmh5225__csgo-sdk-improved.md
  - wiki/sources/descriptions/gmh5225__csgo-offsets.md
  - wiki/sources/descriptions/gmh5225__cs2_webradar.md
  - wiki/sources/descriptions/clauadv__cs2_webradar.md
  - wiki/sources/descriptions/gmh5225__cs2_things.md
  - wiki/sources/descriptions/gmh5225__cs2_sdk.md
  - wiki/sources/descriptions/gmh5225__cs2-sdk.md
  - wiki/sources/descriptions/clouddss__cs2-internal-sdk.md
  - wiki/sources/descriptions/gmh5225__cs2-fov-changer.md
  - wiki/sources/descriptions/gmh5225__OffsetStreaming.md
  - wiki/sources/descriptions/gmh5225__DVRT.md
  - wiki/sources/descriptions/frk1__hazedumper.md
  - wiki/sources/descriptions/alliedmodders__hl2sdk.md
  - wiki/sources/descriptions/ValveSoftware__source-sdk-2013.md
  - wiki/sources/descriptions/anarh1st47__Source2Dumps.md
  - wiki/sources/descriptions/dougwithseismic__dezlock-dump.md
  - wiki/sources/descriptions/dhanax26__Apex-Legends-Offset-Dumper.md
  - wiki/sources/descriptions/a2x__cs2-dumper.md
  - wiki/sources/descriptions/designer1337__csgo-cheat-base.md
  - wiki/sources/descriptions/EternityX__DEADCELL-CSGO.md
  - wiki/sources/descriptions/W1lliam1337__digital-sdk.md
  - wiki/sources/descriptions/ProjectBorealis__PBCharacterMovement.md
  - wiki/sources/descriptions/CallumCVM__ValveGen.md
updated: 2026-08-29
confidence: high
---

# Source NetVars

Valve **Source 1** and **Source 2** games expose replicated entity state through **ClientClass → RecvTable → RecvProp** chains and **CreateInterface**-exported engine interfaces. Cheat SDK and offset tooling walks these structures to map class names to network property offsets. (source: wiki/sources/skills/game-engine.md)

## NetVar parsing workflow (Source 1)

1. Locate `CHLClient` and walk the **ClientClass** linked list
2. For each class, enumerate **RecvTable → RecvProp** entries
3. Build offset map: `class name → property name → offset` (e.g. `CCSPlayer → m_iHealth → 0x100`)
4. Tools: auto-updating CS:GO signature/offset dumps such as [[hazedumper]] (frk1; JSON/TOML/YAML/C++/C#/VB; `config.json` byte patterns for `dwClientState`, `dwEntityList`, netvars; cheat / game:csgo [Offset]) (source: wiki/sources/descriptions/frk1__hazedumper.md), runtime signature/netvar dumpers such as [[gh-offset-dumper]] (pattern scan → headers/JSON; Source engine) (source: wiki/sources/descriptions/guided-hacking__GH-Offset-Dumper.md), title-specific Apex Legends live-process dumpers such as [[apex-legends-offset-dumper]] (dhanax26; interfaces, netvars, SwapChain pointers; cheat / game:apex legends `[Offset]`) (source: wiki/sources/descriptions/dhanax26__Apex-Legends-Offset-Dumper.md), maintained headers such as [[offsets]], patch-updated CS:GO offset feeds such as [[csgo-offsets]] (gmh5225; netvar dumps, interface pointers, signature patterns; cheat / game:csgo [Offset]) (source: wiki/sources/descriptions/gmh5225__csgo-offsets.md), automated SDK generators such as [[valvegen]] (CallumCVM; C++; networked class/data-table parse from client metadata → class definitions and offsets; [SDK Generator]) (source: wiki/sources/descriptions/CallumCVM__ValveGen.md), generated SDKs such as [[sdk]] and [[csgo-sdk]] (gmh5225 + bloesway forks; C++; netvar structures / interfaces / signatures plus SDK generation + hooking; bloesway fork emphasizes rendering / networking / animation; cheat / game:csgo [SDK]) (source: wiki/sources/descriptions/gmh5225__csgo-sdk.md) (source: wiki/sources/descriptions/gmh5225__csgo_sdk.md) (source: wiki/sources/descriptions/bloesway__csgo_sdk.md), corrected header trees such as [[csgo-sdk-improved]] (gmh5225; fixed classes, extra interfaces, fuller netvar coverage vs leaked SDKs; cheat / game:csgo [Internal]) (source: wiki/sources/descriptions/gmh5225__csgo-sdk-improved.md), and live offset **streaming** to cheat clients via [[offset-streaming]] (gmh5225; C/C++; Some Tricks / Windows Ring3) (source: wiki/sources/descriptions/gmh5225__OffsetStreaming.md), plus dynamic value resolution tables such as [[dvrt]] (gmh5225; maintain/update offsets at runtime on module load/relocation; cheat [Offset]) (source: wiki/sources/descriptions/gmh5225__DVRT.md)

Source 2 extends the model with schema-driven layouts; generators such as [[source2gen]] and multi-game dumps such as [[source2sdk]] produce C++ class/enum headers from exposed schema. Pre-generated multi-game reference dumps such as [[source2dumps]] (anarh1st47; netvars, interfaces, class IDs; Dota 2, Artifact, HL:Alyx, Sandbox; `[Dump]`) provide static layout listings for offset tracking without running generators. (source: wiki/sources/descriptions/anarh1st47__Source2Dumps.md) Live-process schema + RTTI tools such as [[dezlock-dump]] (Deadlock/CS2/Dota 2; class hierarchies, netvars, interfaces, protobuf, singletons; WebSocket live bridge) extract the same layout artifacts at runtime without offline source2gen. (source: wiki/sources/descriptions/dougwithseismic__dezlock-dump.md) CS2-specific live offset/interface dumpers such as [[cs2-dumper]] (a2x; Rust; memflow on Windows/Linux; C#/C++/Rust/JSON output; cheat / game:cs2 `[Dump]`) automate the same per-patch refresh for CS2 externals and analysts. (source: wiki/sources/descriptions/a2x__cs2-dumper.md)

## Key interfaces (CreateInterface export)

| Interface | Typical use |
|-----------|-------------|
| `IVEngineClient` | Engine client services |
| `IClientEntityList` | `GetClientEntity(index)` entity list; live-process entity-list discovery tools such as [[gh-entity-list-finder]] (x64/x86 scan for likely list addresses) complement signature dumpers (source: wiki/sources/descriptions/guided-hacking__GH-Entity-List-Finder.md) |
| `IEngineTrace` | Ray/world traces |
| `ICvar` | `FindVar("sv_cheats")` and console variables |
| `ISurface` / `IPanel` | Overlay rendering (Source 1 HUD/ESP lane); internal bases such as [[csgo-cheat-base]] wrap these interfaces for DirectX surface drawing and glow ESP (source: wiki/sources/descriptions/designer1337__csgo-cheat-base.md); full-source learning frameworks such as [[deadcell-csgo]] (EternityX; aiming, visuals, config, menu modules; build-from-source CS:GO cheat architecture study) illustrate modular internal feature layout beside scaffold bases (source: wiki/sources/descriptions/EternityX__DEADCELL-CSGO.md); modular scaffolds such as [[digital-sdk]] pair dedicated netvars/rendering modules with CreateMove and Direct3D reset hooks for ESP, chams, and autowall features (source: wiki/sources/descriptions/W1lliam1337__digital-sdk.md) |

Interface vtables and netvar tables drift per game build—verify against the target binary. Pair with [[research-rigor]] when porting offsets across patches.

## Ground-truth sources

UE4 movement plugins such as [[pbcharactermovement]] (ProjectBorealis; recreates HL2/Source bunnyhopping, surfing, strafe boosting, wall strafing, and advanced crouch on `UCharacterMovementComponent`; source + prebuilt binaries) show how classic Source movement mechanics translate to Unreal integration rather than RecvTable offset workflows. (source: wiki/sources/descriptions/ProjectBorealis__PBCharacterMovement.md) Open or leaked trees such as [[source-engine]], AlliedModders HL2 SDK references such as [[hl2sdk]] (alliedmodders; C/C++; client/server/game logic headers + mod/plugin build infrastructure; Half-Life 2 era Source 1 SDK) (source: wiki/sources/descriptions/alliedmodders__hl2sdk.md), official Valve **Source SDK 2013** such as [[source-sdk-2013]] (ValveSoftware; HL2/HL2DM/TF2 game+engine code; VS + Steam Runtime Linux builds; non-commercial mods) (source: wiki/sources/descriptions/ValveSoftware__source-sdk-2013.md), Orange Box SDK trees such as [[source-sdk-orangebox]] (gmh5225; shader/render/driver-oriented Source 1 SDK) (source: wiki/sources/descriptions/gmh5225__source-sdk-orangebox.md), [[cstrike15-src]], and CS:GO mod source trees such as [[csso-src]] (gmh5225; client/server logic, weapons, movement, engine interfaces; CSGO Mod) (source: wiki/sources/descriptions/gmh5225__csso-src.md) help validate ClientClass/RecvTable layouts. CS2 offset dumps such as [[cs2-offsets]] and Dota 2 layout dumps such as [[dota2dumped]] (netvar offsets, interface pointers, class headers after patches) illustrate the Source 2 netvar/entity-layout lane; CS2 research collections such as [[cs2-things]] (gmh5225; VScript; RE structures / offset dumps / SDK snippets / entity layouts / netvars / engine interfaces; cheat / game:cs2) document the same layout artifacts for Source 2 RE; CS2 SDK headers such as [[cs2-sdk]] (gmh5225/cs2_sdk and cs2-sdk forks; C/C++; SDK generation / simplified Source 2 layout; driver / rendering / networking; DX11 + Vulkan; cheat / game:cs2 [SDK]) supply the foundational type system for that lane; reverse-engineered internal SDK headers such as [[cs2-internal-sdk]] (clouddss; C++; class defs, interface pointers, netvar offsets, schema structures; cheat / game:cs2 [Internal]) extend it for in-process hooking; browser radar clients such as [[cs2-webradar]] (gmh5225 and clauadv forks; entity positions via memory analysis for web display; cheat / game:cs2) consume the same artifacts as overlay cheats; CS2 FOV changer samples such as [[cs2-fov-changer]] (gmh5225; hooking / memory analysis; cheat / game:cs2 [FOV changer]) illustrate camera-state manipulation in the same Source 2 layout lane. (source: wiki/sources/descriptions/ikhsanprasetyo__dota2dumped.md) (source: wiki/sources/descriptions/gmh5225__cs2_things.md) (source: wiki/sources/descriptions/gmh5225__cs2_sdk.md) (source: wiki/sources/descriptions/gmh5225__cs2-sdk.md) (source: wiki/sources/descriptions/clouddss__cs2-internal-sdk.md) (source: wiki/sources/descriptions/gmh5225__cs2_webradar.md) (source: wiki/sources/descriptions/clauadv__cs2_webradar.md) (source: wiki/sources/descriptions/gmh5225__cs2-fov-changer.md)

## Related

[[unreal-object-model]] · [[il2cpp]] · [[valvegen]] · [[sdk]] · [[csgo-sdk]] · [[csgo-sdk-improved]] · [[csgo-offsets]] · [[hazedumper]] · [[offsets]] · [[offset-streaming]] · [[dvrt]] · [[gh-offset-dumper]] · [[apex-legends-offset-dumper]] · [[gh-entity-list-finder]] · [[source2gen]] · [[source2sdk]] · [[source2dumps]] · [[dezlock-dump]] · [[cs2-dumper]] · [[dota2dumped]] · [[cs2-offsets]] · [[cs2-sdk]] · [[cs2-internal-sdk]] · [[cs2-things]] · [[cs2-webradar]] · [[cs2-fov-changer]] · [[source-engine]] · [[hl2sdk]] · [[source-sdk-2013]] · [[pbcharactermovement]] · [[source-sdk-orangebox]] · [[cstrike15-src]] · [[csso-src]] · [[csgo-cheat-base]] · [[deadcell-csgo]] · [[csgo-internal-base]] · [[research-rigor]] · [[overviews/game-engine]] · [[overviews/game-hacking]]
