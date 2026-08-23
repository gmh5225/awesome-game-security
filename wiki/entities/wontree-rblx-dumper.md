---
title: WonTree RBLX Dumper
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/LyeDevGit__WonTree-RBLX-Dumper.md
updated: 2026-08-23
confidence: medium
---

# WonTree RBLX Dumper

Universal **Roblox** game analysis tool that decompiles reachable scripts and exports structured reports for reverse-engineering a live experience. Written in **Luau** as a single injectable script; runs on UNC-compatible executors (Xeno, Wave, Solara, Delta, Codex) with Rayfield Gen2 UI and a native fallback. (source: wiki/sources/descriptions/LyeDevGit__WonTree-RBLX-Dumper.md)

## Capabilities

- Four-layer decompile pipeline for reachable Luau scripts
- Full client and server instance scanning
- Remote call graphs with optional live `FireServer` / `InvokeServer` logger
- Framework detection and anti-cheat keyword scanning
- Markdown and CSV report export
- Executor noise filtering, graceful handling of protected scripts, configurable script limits and memory caps for large games

Targets game security researchers and reverse engineers who need a practical reference map of a Roblox experience's scripts, remotes, assets, and security-relevant code paths. Pair with [[advanced-anticheat]] and [[shprotect-ac]] for defensive Luau AC context, [[byfron-bypass]] / [[vulkan]] for client anti-tamper RE, and [[roblox-cheats]] for the macOS native client offensive lane.

## Links

- Repo: https://github.com/LyeDevGit/WonTree-RBLX-Dumper

## Related

[[roblox-cheats]] · [[advanced-anticheat]] · [[shprotect-ac]] · [[lua-obfuscator-clyde-protection]] · [[byfron-bypass]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
