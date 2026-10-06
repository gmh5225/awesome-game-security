---
title: LeviAntiCheat
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/LiteLDev__LeviAntiCheat.md
  - wiki/sources/README-categories.md
updated: 2026-10-06
confidence: medium
---

# LeviAntiCheat

**Open-source server-side anti-cheat plugin** for **LeviLamina-based Minecraft Bedrock dedicated servers** (LiteLDev/LeviAntiCheat). Implemented in C++, it detects and punishes client cheats and hardens the host against known Bedrock server exploits. (source: wiki/sources/descriptions/LiteLDev__LeviAntiCheat.md)

## Capabilities

| Area | Coverage |
|------|----------|
| World / vision | X-ray vision; obfuscation-based **Anti-Xray** engine with multiple engine modes |
| Movement | Fly and speed hacks |
| Combat | Reach and auto-click abuse |
| Inventory | Invalid inventory item detection |
| Network | Malicious or malformed packet checks |
| Exploit mitigation | Item duplication and crafter crash fixes |
| Moderation | Configurable violation-level punishment with ban and mute commands |
| Operations | Extensive JSON configuration, hot reload, multilingual operator messaging |

## Architecture

| Layer | Role |
|-------|------|
| **Runtime** | C++ LeviLamina plugin loaded on Bedrock dedicated server (BDS) |
| **Detection** | Server-side heuristics and packet sanity checks across movement, combat, inventory, and world interaction |
| **Anti-Xray** | Obfuscation engine with selectable modes to limit ore/block exposure without client mods |
| **Policy** | JSON-driven thresholds, punishments, and localized messages; hot reload without restart |

## Positioning

Listed in the README under **Anti Cheat → Open Source Anti Cheat System** / **game:minecraft**. Sits beside Bedrock prediction plugins such as [[amethyst]] and [[ghost-anticheat]], behavior-pack AC such as [[paradox-anticheat]] and [[blarion-anticheat]], and catalog hubs such as [[minecraft-anticheat-list]].

## Links

- Repo: https://github.com/LiteLDev/LeviAntiCheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[minecraft-anticheat-list]] · [[amethyst]] · [[ghost-anticheat]] · [[paradox-anticheat]] · [[blarion-anticheat]]
