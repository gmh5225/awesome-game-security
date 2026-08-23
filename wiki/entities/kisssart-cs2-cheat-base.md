---
title: kisssart-cs2-cheat-base
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/KisSsArt__CS2-Cheat-Base.md
updated: 2026-08-23
confidence: medium
---

# kisssart-cs2-cheat-base

C++ **internal Counter-Strike 2 cheat base** from KisSsArt, built as a Windows **DirectX injectable DLL**. Provides hook and rendering infrastructure with configurable gameplay modules such as **ESP** and **bunny hop**, integrating **Dear ImGui**, **[[kiero]]** for graphics API hooking, and **JSON-based configuration**. The documented build targets Visual Studio x64 release output with **manual-map style injection**. Intended as a starter framework for cheat development and practical game security research. (source: wiki/sources/descriptions/KisSsArt__CS2-Cheat-Base.md)

README tags it `[Internal]`. Slug disambiguated from [[cs2-cheat-base]] (gmh5225 fork of the same repo name).

## Architecture highlights

| Component | Role |
|-----------|------|
| Injectable DLL | In-process CS2 modification scaffold |
| [[kiero]] | DirectX graphics API hook bootstrap |
| ImGui | In-game overlay menu and debug UI |
| Hook infrastructure | Function interception for gameplay modules |
| JSON config | Feature toggles and settings persistence |
| ESP / bunny hop | Example configurable gameplay modules |
| Manual-map injection | Documented load path for the release DLL |

See [[cs2-cheat-base]] for the gmh5225 SDK-structure scaffold, [[cstrike2-hack]] for a Rust modular internal base, and [[asphyxia-cs2]] for a feature-complete open-source internal sample.

## Links

- Repo: https://github.com/KisSsArt/CS2-Cheat-Base

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[cs2-cheat-base]] · [[cstrike2-hack]] · [[asphyxia-cs2]] · [[kiero]] · [[present-hook]] · [[windows-dll-injector]] · [[cs2-internal-sdk]]
