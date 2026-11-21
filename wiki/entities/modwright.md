---
title: modwright
kind: entity
topics: [game-hacking, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/m4bwav__modwright.md
updated: 2026-11-21
confidence: medium
---

# modwright

**Claude Code plugin and Python CLI** (m4bwav) for controlled, verifiable PC game modding. The stdlib `mw.py` workflow scans game installs to detect engine/runtime (Unity Mono or IL2CPP, Unreal, Godot, GameMaker, Source, and others), installed mod loaders, and anti-cheat markers such as [[easy-anti-cheat]], BattlEye, and [[vanguard]]—halting with a dedicated exit code when anti-cheat is present instead of suggesting injection or online cheats. (source: wiki/sources/descriptions/m4bwav__modwright.md)

## Workflow

Backs up saves and targeted files with SHA-256 manifests for restore and verification. Validates that mods actually loaded by parsing [[bepinex]], MelonLoader, [[re-ue4ss]], and related loader logs. Can prepare Steam Workshop VDF or Thunderstore packaging metadata without uploading. Emphasizes decompiling before naming patch targets, offline or single-player modding, and repeatable automation for mod authors and security-conscious players who need engine and anti-cheat awareness during legitimate mod development.

## Links

- Repo: https://github.com/m4bwav/modwright

## Related

[[reverse-this]] · [[universal-modder]] · [[bepinex]] · [[il2cpp]] · [[re-ue4ss]] · [[overviews/game-hacking]] · [[overviews/game-engine]] · [[anticheat-lab-senolbasyigit]]