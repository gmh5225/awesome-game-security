---
title: ChompChomp.io
kind: entity
topics: [anti-cheat, game-hacking, game-server-security]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/multiplayeragent__chompchomp-io.md
updated: 2026-10-29
confidence: medium
---

# ChompChomp.io

Browser multiplayer **slither-style .io** arena where armed snakes fight with guns, power-ups, and combat mechanics in a shared arena. Full **JavaScript** stack: canvas client with prediction and interpolation, shared simulation rules in `sim.js`, authoritative room logic bundled via Node `build.js`, plus HTML/CSS shell. **Multiplayer Agent** deployment: server-authoritative rooms at **20 ticks/s**—clients submit only validated **steer, boost, and fire** inputs while the server simulates movement, pickups, bullets, collisions, scores, and persisted stats. Documented anti-cheat design; useful as a **netcode reference** and end-to-end example of trustworthy browser multiplayer without operating your own game server. (source: wiki/sources/descriptions/multiplayeragent__chompchomp-io.md) (source: wiki/sources/README-categories.md)

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[cobra-snake]] · [[input-provenance]] · [[detector-operations]] · [[shinobix]] · [[ghostline]]
