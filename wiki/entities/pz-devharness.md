---
title: PZ DevHarness
kind: entity
topics: [game-engine]
sources:
  - wiki/sources/descriptions/CalebFenton__PZ_DevHarness.md
  - wiki/sources/README-categories.md
updated: 2026-10-14
confidence: high
---

# PZ DevHarness

**PZ_DevHarness** (CalebFenton) is an automated **Project Zomboid Build 42** mod test harness that runs in-game integration tests headlessly with CI-friendly pass/fail exit codes. Targets mod developers who want fast, repeatable integration tests instead of clicking through vanilla debug unit-test menus. (source: wiki/sources/descriptions/CalebFenton__PZ_DevHarness.md)

README category: Game Testing (in-game mod integration / CI).

## Test model

Tests are short **Lua** scripts that queue player-like timed actions and assert outcomes afterward. Isolation uses per-test world resets, recorded **undo** steps, and leak checks on the world around the character. One command drives the suite and returns pass/fail exit codes suited to CI pipelines. (source: wiki/sources/descriptions/CalebFenton__PZ_DevHarness.md)

## Launch stack

**Bash** scripts orchestrate debug launches in isolated throwaway profiles. Small **Java** launchers start the client and dedicated server in-process, use **reflection** to auto-dismiss the loading screen, and accelerate startup without patching game files. (source: wiki/sources/descriptions/CalebFenton__PZ_DevHarness.md)

## Multiplayer and validation

Covers single-player and local dedicated-server multiplayer: helpers keep client and server state aligned, **DESYNC** reporting when tiles disagree, and server-load validation scripts. (source: wiki/sources/descriptions/CalebFenton__PZ_DevHarness.md)

Adjacent to Kenshi file-based automation [[kenshi-automation-harness]], UE Gauntlet plugin [[ue4-test-automation]], and Unity mobile QA examples [[games-test-automation-example]].

## Links

- Repo: https://github.com/CalebFenton/PZ_DevHarness

## See also

[[kenshi-automation-harness]] · [[ue4-test-automation]] · [[games-test-automation-example]] · [[overviews/game-engine]] · [[overviews/overview]]
