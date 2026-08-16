---
title: anubis
kind: entity
topics: [game-hacking, game-engine, anti-cheat]
sources:
  - wiki/sources/descriptions/danielkrupinski__Anubis.md
updated: 2026-08-16
confidence: medium
---

# anubis

Linux-native **CS:GO internal cheat** in C++ from danielkrupinski. Injects into the game process and provides ESP, aimbot, and related features via **Source engine SDK** interaction—hooking client-side rendering and game event processing. Contrasts with the same author's Windows-centric [[osiris]] by demonstrating Source 1 internal cheat techniques adapted for Linux. Aimed at game-security researchers studying Linux-based game cheat implementations and Source engine internals on non-Windows platforms—not a production cheat guide. (source: wiki/sources/descriptions/danielkrupinski__Anubis.md)

## Architecture highlights

| Component | Role |
|-----------|------|
| Process injection | In-process load into the CS:GO client on Linux |
| Source SDK | Engine/client interface interaction for game state |
| Rendering hooks | Client-side draw path for ESP visuals |
| Game events | Hooked event processing for aimbot and combat features |
| Platform | Linux-only internal implementation |

See [[source-netvars]] for netvar/interface layout work; [[gamesneeze]] and [[csgo-linux-cheat-sdk]] for other Linux CS:GO offensive research lanes; [[osiris]] and [[goesp]] for the same author's Windows/cross-platform CS:GO references.

## Links

- Repo: https://github.com/danielkrupinski/Anubis

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[source-netvars]] · [[osiris]] · [[goesp]] · [[gamesneeze]] · [[csgo-linux-cheat-sdk]] · [[csgo-internal-base]]
