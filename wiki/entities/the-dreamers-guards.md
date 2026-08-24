---
title: The Dreamers Guards
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/IamFriendly0242u__The-Dreamers-Guards.md
updated: 2026-08-24
confidence: medium
---

# The Dreamers Guards

Fabric mod providing client-side and server-side anti-cheat protection for Minecraft multiplayer servers. Written in Java; validates client integrity at join through encrypted custom network payloads and scans installed mods against a blacklist of known cheat clients and exploit utilities. The server enforces infractions with a progressive four-phase suspension system, anti-evasion checks to stop logout bypasses, and operator commands for manual kicks, bans, pardons, and trust management. Security events and enforcement actions can be forwarded to Discord via webhook integration. Targets Fabric server administrators who need automated cheat detection, mod verification, and gameplay integrity enforcement on public or private multiplayer worlds. (source: wiki/sources/descriptions/IamFriendly0242u__The-Dreamers-Guards.md)

## Enforcement model

- **Join-time integrity** — encrypted custom network payloads verify client state before play proceeds.
- **Mod blacklist scanning** — installed mods checked against known cheat clients and exploit utilities.
- **Progressive punishments** — four-phase suspension ladder for repeated infractions.
- **Anti-evasion** — logout-bypass checks to prevent punishment dodging.
- **Operator tooling** — manual kick, ban, pardon, and trust-management commands.
- **Discord webhooks** — security events and enforcement actions forwarded for staff alerting.

Combines client-mod verification with server-side enforcement; complements hash-list integrity mods such as [[seiun-ac]] and packet-physics Fabric AC such as [[windfall-anticheatf]].

## Links

- Repo: https://github.com/IamFriendly0242u/The-Dreamers-Guards

## Related

[[seiun-ac]] · [[windfall-anticheatf]] · [[windfall-anticheat]] · [[jaranalyzer]] · [[lenrete-mod]] · [[local-anticheat-1-8-9]] · [[minecraft-anticheat-list]] · [[dakotaac]] · [[minecraft-anti-cheat]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
