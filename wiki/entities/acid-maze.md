---
title: ACID MAZE
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/acidvegas__acid-maze.md
updated: 2026-11-23
confidence: medium
---

# ACID MAZE

**Browser-based retro maze chase arcade** (acidvegas) with original graphics, audio, and multiple play modes in an 80s-cabinet style. The stack pairs a **Python Flask** backend (Gunicorn + gevent) with a **JavaScript** client and a **shared deterministic game core** in `static/core.js`, **SQLite** for scores, and **Docker** packaging that includes **QuickJS** for deployment-side simulation. **Leaderboard integrity** is server-authoritative: the client submits **per-tick input logs**, and the backend **replays** them through the same **fixed-timestep** simulation before accepting a score—rejecting tampered, reused, incomplete, or oversized submissions and applying **per-address rate limits**. **Seeded PRNGs** and **fixed-point** math keep replays reproducible; automated tests cover API replay and cheating scenarios. A practical reference for **web-game score validation** rather than kernel-level anti-cheat. (source: wiki/sources/descriptions/acidvegas__acid-maze.md)

Sits beside server-replay leaderboard references such as [[dmn-minigame]], [[bitgeist]], [[ghostline]], [[breach]], [[pew-game]], and [[cobra-snake]].

## Links

- Repo: https://github.com/acidvegas/acid-maze

## Related

[[dmn-minigame]] · [[bitgeist]] · [[ghostline]] · [[breach]] · [[pew-game]] · [[cobra-snake]] · [[leaderboard]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[concepts/input-provenance]]