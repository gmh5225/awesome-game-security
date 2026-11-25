---
title: rea-games
kind: entity
topics: [reverse-engineering, game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/erkamyaman__rea-games.md
updated: 2026-11-25
confidence: medium
---

# rea-games

**rea-games** ([erkamyaman/rea-games](https://github.com/erkamyaman/rea-games)) is a framework for reverse-engineering open-source game behavior and proving that clean-room reimplementations match the original. A dependency-free **Node.js** CLI records unmodified originals by controlling clocks and randomness, captures inputs, random-number tapes, and per-step game state, and documents rules in per-game **behavior specs**. Rebuilt ports in web JavaScript, **Rust** with Bevy, or headless **Godot** GDScript replay recorded cases and must produce identical traces through a shared **JSON verify** protocol. Shipped verified examples include 2048, Chrome Dino, Canvas Bird, and a falling-blocks game; the **GAME.md** workflow supports agent-driven addition of games and engine ports. Listed under **Cheat / Guide** for behavioral-equivalence study without copying original assets or code. (source: wiki/sources/descriptions/erkamyaman__rea-games.md)

## Workflow

| Stage | Role |
|-------|------|
| **Record** | Node CLI fixes time/RNG; saves inputs, RNG tapes, per-step state |
| **Spec** | Per-game behavior specs document inferred rules |
| **Port** | Clean-room rebuild in JS, Rust/Bevy, or headless Godot |
| **Verify** | Shared JSON protocol checks frame-by-frame behavioral parity |

## Positioning

Complements memory-cheat and disassembler lanes: targets **logic recovery and equivalence proof** on small open web games rather than protected commercial clients. Pair [[research-rigor]] when treating specs as ground truth. Contrasts with agent orchestrators such as [[harness-for-rea]] and [[apex-re]] (binary/MCP RE) and with curriculum labs such as [[re-dojo]] (offline C++ crackmes). (source: wiki/sources/descriptions/erkamyaman__rea-games.md)

## Links

- Repo: https://github.com/erkamyaman/rea-games

## Related

[[re-dojo]] · [[harness-for-rea]] · [[apex-re]] · [[rea-atlas]] · [[research-rigor]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/game-engine]]