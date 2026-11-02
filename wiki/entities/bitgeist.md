---
title: Bitgeist
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/kyzoeth__bitgeist.md
updated: 2026-11-02
confidence: medium
---

# Bitgeist

**Bitgeist** (kyzoeth/bitgeist) is a **browser-based retro speedrun arena**: short sprints against up to ten ghost replays, instant save-state retries, and shareable one-on-one dare links. The client runs **multi-console Libretro WebAssembly cores** (NES, SNES, Genesis, Game Boy, GBA) at 60 FPS and reads live player position, camera, and finish state from **emulated system RAM** without patching ROMs. Ghost leaderboards persist in **SQLite** with skill-bracketed matchmaking; user-supplied cartridges stay in **IndexedDB** on the device only. (source: wiki/sources/descriptions/kyzoeth__bitgeist.md)

## Integrity model

- **60 Hz run-length-encoded joypad logs** — primary submitted evidence for each run.
- **Game-specific movement rules** — correlates inputs with mechanics such as wall climbs and air dashes before accepting finishes.
- **Deterministic WASM replay** — headless worker re-simulates submitted logs; mismatches against emulated RAM telemetry reject tampered leaderboards.

Stack: **TypeScript** and **Next.js** on the server with Node SQLite APIs. Useful for studying **client-side emulation telemetry**, competitive replay validation, and lightweight browser-hosted anti-cheat patterns—adjacent to Wasm replay-verified platforms such as [[magnetite]] and [[bevy-personal-test]], and browser score-integrity references such as [[chompchomp-io]] and [[cobra-snake]].

## Links

- Repo: https://github.com/kyzoeth/bitgeist

## Related

[[magnetite]] · [[bevy-personal-test]] · [[ghostline]] · [[chompchomp-io]] · [[concepts/input-provenance]] · [[overviews/anti-cheat]]
