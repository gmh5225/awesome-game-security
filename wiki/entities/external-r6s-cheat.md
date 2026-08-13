---
title: External-R6S-Cheat
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel, game-engine]
sources:
  - wiki/sources/descriptions/gmh5225__External-R6S-Cheat.md
updated: 2026-08-13
confidence: medium
---

# External-R6S-Cheat

**Rainbow Six Siege (R6S) external cheat** (gmh5225) that operates outside the game process. Uses **shared memory communication with a kernel driver** and reads game entities, player positions, and rendering data externally through a **mapped memory section** to drive **ESP** and **aimbot** features—avoiding in-process injection into the [[battleye]]-protected client. (source: wiki/sources/descriptions/gmh5225__External-R6S-Cheat.md)

Complements other gmh5225 R6 externals such as [[r6s-external-v2]] (kernel driver or handle elevation for RPM), [[rainbow-six-siege-rs6-external-esp-aimbot-hack-cheat]] (WndProc-only input hook), and [[r6-external]] for comparing shared-memory KM↔UM driver channels vs handle elevation or minimal user-mode input paths.

## Links

- Repo: https://github.com/gmh5225/External-R6S-Cheat

## Related

[[battleye]] · [[unreal-object-model]] · [[world-to-screen]] · [[r6-external]] · [[r6s-external-v2]] · [[rainbow-six-siege-rs6-external-esp-aimbot-hack-cheat]] · [[r6s-internal-cheat]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
