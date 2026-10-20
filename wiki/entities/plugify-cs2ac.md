---
title: plugify-cs2ac
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/ViTaminza__plugify-cs2ac.md
  - wiki/sources/README-categories.md
updated: 2026-10-20
confidence: medium
---

# plugify-cs2ac

**Plugify / s2sdk port** of [[cs2ac]] for Counter-Strike 2 dedicated servers. Rewritten from the original Metamod:Source plugin while preserving server-side behavioral coverage over user commands, movement, aim, shots, input history, and client settings. (source: wiki/sources/descriptions/ViTaminza__plugify-cs2ac.md)

## Detection stack

- **Polyhook detours** on gamedata-resolved `libserver.so` routines for usercmd and movement data
- **s2sdk hooks** for game events, net messages, client cvars, and schema access
- Broad cheat-class coverage: aimbots, triggerbots, movement exploits, invalid cvars, and related anomalies (plus fork-specific telemetry modes)

## Enforcement

Optional `admin_system` bans, configurable kick commands, JSONL detection logs, Discord webhooks, and localization.

Targets CS2 server operators who want **server-authoritative** anti-cheat on hosts they control—the same lane as [[cs2ac]], [[sac-the-server-anticheat]], and [[cs2-anticheat-by-chmonya]], not client kernel products such as [[easy-anti-cheat]] or [[vanguard]].

## Links

- Repo: https://github.com/ViTaminza/plugify-cs2ac

## Related

[[cs2ac]] · [[sac-the-server-anticheat]] · [[cs2-anticheat-by-chmonya]] · [[anticheatsystem]] · [[overviews/anti-cheat]] · [[ai-aimbot-detection]]
