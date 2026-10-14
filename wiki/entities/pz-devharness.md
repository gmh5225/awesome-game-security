---
title: PZ DevHarness
kind: entity
topics: [game-engine]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/CalebFenton__PZ_DevHarness.md
updated: 2026-10-14
confidence: medium
---

# PZ DevHarness

**PZ_DevHarness** (CalebFenton) is an automated **Project Zomboid Build 42** mod test harness that runs in-game integration tests headlessly with CI-friendly pass/fail exit codes. Short **Lua** tests queue player-like timed actions and assert outcomes; per-test world resets, recorded undos, and leak checks isolate failures. Bash orchestration launches debug clients in throwaway profiles; Java reflection launchers start client and dedicated server in-process, auto-dismiss loading screens, and accelerate startup without patching game files. Covers single-player and local dedicated-server multiplayer with DESYNC reporting when client/server tiles disagree and server-load validation scripts. (source: wiki/sources/descriptions/CalebFenton__PZ_DevHarness.md)

README category: Game Testing (in-game mod integration / CI).

Adjacent to Kenshi file-based automation [[kenshi-automation-harness]], UE Gauntlet plugin [[ue4-test-automation]], and Unity mobile QA examples [[games-test-automation-example]].

## Links

- Repo: https://github.com/CalebFenton/PZ_DevHarness

## See also

[[kenshi-automation-harness]] · [[ue4-test-automation]] · [[games-test-automation-example]] · [[overviews/game-engine]] · [[overviews/overview]]
