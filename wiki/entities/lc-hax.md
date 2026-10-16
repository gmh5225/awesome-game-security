---
title: lc-hax
kind: entity
topics: [game-hacking, game-engine, anti-cheat]
sources:
  - wiki/sources/descriptions/winstxnhdw__lc-hax.md
updated: 2026-10-16
confidence: medium
---

# lc-hax

Portable **Windows internal mod** for **Lethal Company** (Unity **Mono**). A **CLI launcher** injects a **C# assembly** into the game process and exposes a large set of always-on mods plus **chat-triggered commands**, built on **.NET** with runtime **Harmony-style patches**, helper modules for players and enemies, and optional **Roslyn source analysers** that validate command definitions. Capabilities include ESP, anti-kick, god mode, noclip, enemy possession, infinite resources, lobby and connection manipulation, and host-only privileged controls, with private command input and keyboard binds for toggles and teleportation. (source: wiki/sources/descriptions/winstxnhdw__lc-hax.md)

Useful for studying **Unity Mono managed injection**, **client-side trust boundaries** on co-op networking, and how feature-rich internal cheats structure patches, commands, and maintenance (CI/docs) outside canonical [[bepinex]] plugin hosts—alongside Mono-era samples such as [[escapefromtarkov-trainer]] and IL2CPP in-process menus such as [[devour-menu]].

## Architecture

| Component | Role |
|-----------|------|
| CLI launcher | Injects managed assembly into the game process |
| Harmony-style patches | Runtime IL hooks for gameplay and networking |
| Command modules | Always-on mods + chat-triggered commands |
| Roslyn analysers | Optional compile-time validation of command definitions |
| Player/enemy helpers | Shared modules for entity manipulation features |

## Links

- Repo: https://github.com/winstxnhdw/lc-hax

## Related

[[bepinex]] · [[monohook]] · [[dnspy]] · [[devour-menu]] · [[escapefromtarkov-trainer]] · [[il2cpp]] · [[overviews/game-hacking]] · [[overviews/game-engine]] · [[overviews/anti-cheat]]
