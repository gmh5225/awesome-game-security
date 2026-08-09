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
updated: 2026-08-09
confidence: high
---

# Source NetVars

Valve **Source 1** and **Source 2** games expose replicated entity state through **ClientClass → RecvTable → RecvProp** chains and **CreateInterface**-exported engine interfaces. Cheat SDK and offset tooling walks these structures to map class names to network property offsets. (source: wiki/sources/skills/game-engine.md)

## NetVar parsing workflow (Source 1)

1. Locate `CHLClient` and walk the **ClientClass** linked list
2. For each class, enumerate **RecvTable → RecvProp** entries
3. Build offset map: `class name → property name → offset` (e.g. `CCSPlayer → m_iHealth → 0x100`)
4. Tools: hazedumper-style dumps, runtime signature/netvar dumpers such as [[gh-offset-dumper]] (pattern scan → headers/JSON; Source engine) (source: wiki/sources/descriptions/guided-hacking__GH-Offset-Dumper.md), maintained headers such as [[offsets]], generated SDKs such as [[sdk]] and [[csgo-sdk]] (gmh5225; C++; netvar structures / interfaces / signatures plus SDK generation + hooking; cheat / game:csgo) (source: wiki/sources/descriptions/gmh5225__csgo-sdk.md) (source: wiki/sources/descriptions/gmh5225__csgo_sdk.md)

Source 2 extends the model with schema-driven layouts; generators such as [[source2gen]] and multi-game dumps such as [[source2sdk]] produce C++ class/enum headers from exposed schema.

## Key interfaces (CreateInterface export)

| Interface | Typical use |
|-----------|-------------|
| `IVEngineClient` | Engine client services |
| `IClientEntityList` | `GetClientEntity(index)` entity list; live-process entity-list discovery tools such as [[gh-entity-list-finder]] (x64/x86 scan for likely list addresses) complement signature dumpers (source: wiki/sources/descriptions/guided-hacking__GH-Entity-List-Finder.md) |
| `IEngineTrace` | Ray/world traces |
| `ICvar` | `FindVar("sv_cheats")` and console variables |
| `ISurface` / `IPanel` | Overlay rendering (Source 1 HUD/ESP lane) |

Interface vtables and netvar tables drift per game build—verify against the target binary. Pair with [[research-rigor]] when porting offsets across patches.

## Ground-truth sources

Open or leaked trees such as [[source-engine]], Orange Box SDK trees such as [[source-sdk-orangebox]] (gmh5225; shader/render/driver-oriented Source 1 SDK) (source: wiki/sources/descriptions/gmh5225__source-sdk-orangebox.md), [[cstrike15-src]], and CS:GO mod source trees such as [[csso-src]] (gmh5225; client/server logic, weapons, movement, engine interfaces; CSGO Mod) (source: wiki/sources/descriptions/gmh5225__csso-src.md) help validate ClientClass/RecvTable layouts. CS2 offset dumps such as [[cs2-offsets]] and Dota 2 layout dumps such as [[dota2dumped]] (netvar offsets, interface pointers, class headers after patches) illustrate the Source 2 netvar/entity-layout lane. (source: wiki/sources/descriptions/ikhsanprasetyo__dota2dumped.md)

## Related

[[unreal-object-model]] · [[il2cpp]] · [[sdk]] · [[csgo-sdk]] · [[offsets]] · [[gh-offset-dumper]] · [[gh-entity-list-finder]] · [[source2gen]] · [[source2sdk]] · [[dota2dumped]] · [[cs2-offsets]] · [[source-engine]] · [[source-sdk-orangebox]] · [[cstrike15-src]] · [[csso-src]] · [[research-rigor]] · [[overviews/game-engine]] · [[overviews/game-hacking]]
