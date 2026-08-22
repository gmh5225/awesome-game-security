---
title: BloodHunt-v1.1
kind: entity
topics: [game-hacking, graphics-api, game-engine]
sources:
  - wiki/sources/descriptions/PhysX1337__BloodHunt-v1.1.md
updated: 2026-08-22
confidence: medium
---

# BloodHunt-v1.1

External **Windows cheat framework** for **Blood Hunt** (PhysX1337). C++ implementation built around out-of-process **memory reading** and **DirectX 9 + ImGui overlay rendering** for an **Unreal Engine** battle-royale target. Features include **ESP**, configurable **aimbot**, **recoil-related** modifications, **hardcoded game offsets**, **actor caching**, and on-screen **menu controls** for feature toggling and tuning. Positioned for cheat prototyping and anti-cheat evasion research. (source: wiki/sources/descriptions/PhysX1337__BloodHunt-v1.1.md)

## Architecture highlights

| Component | Role |
|-----------|------|
| External memory reads | Out-of-process entity/state access |
| Hardcoded offsets | UE actor/layout targeting without live dumper |
| Actor cache | Amortized entity enumeration across frames |
| DX9 + ImGui overlay | Transparent external render + menu UI |
| Feature modules | ESP, aimbot, recoil mods with runtime toggles |

Complements [[bloodhunt-external]] (ZZZ-Monster; DX9 ImGui + mhyprot driver utilities) and [[blood-hunt]] (gmh5225; driver/render/modding) as another Blood Hunt external sample under [[easy-anti-cheat]].

## Links

- Repo: https://github.com/PhysX1337/BloodHunt-v1.1

## Related

[[blood-hunt]] · [[bloodhunt-external]] · [[easy-anti-cheat]] · [[imgui-standalone]] · [[fortnite-external-cheat-source-code]] · [[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/game-engine]]
