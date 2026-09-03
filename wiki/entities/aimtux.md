---
title: aimtux
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/AimTuxOfficial__AimTux.md
updated: 2026-09-03
confidence: medium
---

# aimtux

Linux **internal cheat framework** for **Counter-Strike: Global Offensive** (AimTuxOfficial). C++ codebase with build scripts, injection helpers, and configuration handling for deploying a feature-rich in-game module. Workflow relies on common Linux tooling—**CMake** builds, **GDB-based injection**, and user-managed config directories for runtime customization. Primary use case is game-hacking research to study internal cheat architecture and client-side manipulation techniques on non-Windows Source 1 hosts—not a maintained production cheat. (source: wiki/sources/descriptions/AimTuxOfficial__AimTux.md)

README tags it `[Linux]`. Treat as a fuller Linux internal CS:GO framework reference beside lighter SDK scaffolds.

## Architecture highlights

| Component | Role |
|-----------|------|
| CMake build | Standard Linux compile and packaging workflow |
| GDB injection | Debugger-assisted load into the CS:GO client process |
| Config directories | User-managed runtime customization paths |
| Internal module | In-process feature deployment and client manipulation |

See [[anubis]] and [[csgo-linux-cheat-sdk]] for other Linux CS:GO internal/SDK research lanes; [[ghinterfacescsgo]] for minimal interface/hook scaffolding on Linux.

## Links

- Repo: https://github.com/AimTuxOfficial/AimTux

## Related

[[overviews/game-hacking]] · [[source-netvars]] · [[anubis]] · [[csgo-linux-cheat-sdk]] · [[ghinterfacescsgo]] · [[gamesneeze]] · [[osiris]] · [[csgo-internal-base]]
