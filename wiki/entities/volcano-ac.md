---
title: VolcanoAC
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/theo926__VolcanoAC.md
  - wiki/sources/README-categories.md
updated: 2026-09-17
confidence: medium
---

# VolcanoAC

Open-source **server-side anti-cheat** for **Roblox** games, written in **Luau** and aimed at lightweight protection against client-side movement cheats. (source: wiki/sources/descriptions/theo926__VolcanoAC.md)

## Detection surface

Per-frame character monitoring on the game server using raycasts and physics-state checks. Covers speed hacks, fly hacks, noclip, and fake seated states with configurable thresholds.

## Enforcement

Enforces walk-speed, air-time, and collision limits. Violations trigger **lag-backs** that snap players to their last valid position; repeat offenders are kicked.

## Deployment

Includes a loadstring-based loader for remote updates. Targets Roblox developers who need practical server-authoritative mitigation where native client AC is limited — the same Luau server model as [[encryptic-roblox-anti-cheat]], [[shprotect-ac]], and [[advanced-anticheat]].

## Links

- Repo: https://github.com/theo926/VolcanoAC

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[encryptic-roblox-anti-cheat]] · [[shprotect-ac]] · [[advanced-anticheat]] · [[rustblox]] · [[byfron-bypass]] · [[wontree-rblx-dumper]]
