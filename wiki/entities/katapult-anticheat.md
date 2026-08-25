---
title: Katapult AntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Gitex68__Katapult-AntiCheat.md
updated: 2026-08-25
confidence: medium
---

# Katapult AntiCheat

Client-server anti-cheat mod for Minecraft **1.21.1** on **NeoForge** that enforces game integrity by validating installed client mods and resource packs against server-side whitelists. Written in Java; computes **SHA-256 checksums** from physical `.jar` and `.zip` files on the client and compares them to hashes generated from server mods and administrator-approved optional client content, disconnecting players who load unapproved or modified files. (source: wiki/sources/descriptions/Gitex68__Katapult-AntiCheat.md)

## Enforcement model

- **Mod checksum validation** — client-side SHA-256 over installed mod JARs matched to server whitelist hashes.
- **Resource pack monitoring** — detects renamed or spoofed packs such as hidden X-ray textures; real-time checks on join and reload.
- **Hot-reloadable configuration** — server-side whitelist regeneration and live re-validation via commands without restart.
- **NeoForge networking** — custom payloads carry checksum results between client and server.
- **Gson whitelist management** — administrator-maintained approved optional client content lists.

Targets Minecraft server operators who need integrity enforcement on **modded NeoForge multiplayer** servers. Complements Fabric hash-list mods such as [[seiun-ac]] and blacklist-oriented Fabric AC such as [[the-dreamers-guards]]; distinct from packet-physics server plugins such as [[grim]] and [[windfall-anticheat]].

## Links

- Repo: https://github.com/Gitex68/Katapult-AntiCheat

## Related

[[seiun-ac]] · [[the-dreamers-guards]] · [[grim]] · [[minecraft-anticheat-list]] · [[epsilon]] · [[lenrete-mod]] · [[jaranalyzer]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
