---
title: esp-killer
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/kroshtan__esp-killer.md
  - wiki/sources/README-categories.md
updated: 2026-09-26
confidence: medium
---

# esp-killer

Server-side **ESP / wallhack detection** for **The Isle: Evrima** multiplayer servers. Python read-only agent polls player positions through the Evrima **RCON** protocol and uploads snapshots to a **FastAPI** backend with SQLite storage and API key management. Flags movement that only makes sense with wallhack vision—heading directly toward distant hidden players or arriving implausibly fast—and alerts admins for human review rather than automatic bans. Because Evrima ships with Easy Anti-Cheat and offers no modding API, the tool never touches the game client. Includes a clean-room RCON client, on-disk upload queue with retry logic, and dev tools (fake RCON server + movement simulator) for pipeline testing. (source: wiki/sources/descriptions/kroshtan__esp-killer.md)

Sits in the **Detection:ESP** lane beside server-side terrain/occlusion mitigations such as [[petal-anti-freecam]] and [[serverguard]], and movement-replay backends such as [[blastscale]].

## Links

- Repo: https://github.com/kroshtan/esp-killer

## Related

[[petal-anti-freecam]] · [[serverguard]] · [[blastscale]] · [[easy-anti-cheat]] · [[overviews/anti-cheat]] · [[concepts/detector-operations]]
