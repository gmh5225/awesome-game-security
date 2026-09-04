---
title: Pew Game
kind: entity
topics: [anti-cheat, game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/nocoo__pew-game.md
updated: 2026-09-04
confidence: medium
---

# Pew Game

Browser-based pixel-art **twin-stick shooter** inspired by Stardew Valley's Journey of the Prairie King, built as a full-stack web game with an online leaderboard. Implemented in **TypeScript** with Next.js, Bun, and Tailwind CSS; a pure TypeScript canvas engine draws all sprites procedurally without image assets. (source: wiki/sources/descriptions/nocoo__pew-game.md)

Server-side **anti-cheat** issues **HMAC-signed session tokens** at game start and validates score submissions for signature integrity, score/wave/duration plausibility, and replay prevention. SQLite via better-sqlite3 stores leaderboard data; the repo includes extensive unit and end-to-end tests covering gameplay mechanics and anti-cheat validation. Useful as a practical reference for securing client-side browser game scores and protecting online leaderboards from tampering.

## Links

- Repo: https://github.com/nocoo/pew-game

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[ff3mmo]] · [[bevy-personal-test]] · [[javascript-obfuscator]]
