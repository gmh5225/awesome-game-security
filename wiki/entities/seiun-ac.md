---
title: Seiun AC
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/clementine44613__seiun-ac.md
updated: 2026-08-19
confidence: medium
---

# Seiun AC

Fabric anti-cheat mod for Minecraft **1.21.11** that enforces client integrity by hashing installed mods and resource packs against server-side whitelists, blacklists, and gray lists when players join. Written in Java for Fabric Loader; uses custom client-server network packets and Mixins to collect mod hashes, detect mid-session resource-pack changes, and kick or warn players on unauthorized or modified clients. (source: wiki/sources/descriptions/clementine44613__seiun-ac.md)

## Enforcement model

- **Hash lists** — server-maintained whitelist, blacklist, and gray-list tiers for mod JARs and resource packs.
- **Join-time verification** — client inventory of mods/packs checked before play proceeds.
- **Mid-session monitoring** — resource-pack changes after join trigger alerts or removal.
- **Operator tooling** — in-game commands to manage lists and reload configuration without restarts.
- **Discord webhooks** — real-time alerts for kicks, warnings, operator-status changes, and violation statistics.

Targets Minecraft server administrators who need client-mod enforcement beyond traditional gameplay packet checks; complements Discord-based whitelisting tools in the same project family. Distinct from packet-physics AC such as [[windfall-anticheatf]] and from passive client monitors such as [[local-anticheat-1-8-9]].

## Links

- Repo: https://github.com/clementine44613/seiun-ac

## Related

[[windfall-anticheatf]] · [[windfall-anticheat]] · [[local-anticheat-1-8-9]] · [[jaranalyzer]] · [[lenrete-mod]] · [[phantom-client]] · [[yuri]] · [[dakotaac]] · [[minecraft-anticheatai]] · [[cklsit-advanced-anticheat]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
