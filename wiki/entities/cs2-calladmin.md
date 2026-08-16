---
title: CallAdmin (cs2-calladmin)
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/cs2-server-plugins__cs2-calladmin.md
updated: 2026-08-16
confidence: medium
---

# CallAdmin (cs2-calladmin)

**In-game player reporting system** for Counter-Strike 2 dedicated servers on the **ModSharp** framework. Players flag suspected cheaters and rule-breakers from chat; admins claim, handle, or dismiss reports through a structured workflow. (source: wiki/sources/descriptions/cs2-server-plugins__cs2-calladmin.md)

## Architecture

Written in C# as a modular plugin suite: core commands and report lifecycle logic are separated from optional database and Discord notification modules. A public API lets other server plugins subscribe to report events or drive reports programmatically.

## Persistence and notifications

Reports persist via **LiteDB**, **MySQL**, or **PostgreSQL**. An optional Discord module posts webhook embeds that update in place as report status changes.

## Anti-abuse and moderation

Includes cooldowns, duplicate detection, auto-close timers, and configurable report reasons. Can integrate with an in-game admin panel for moderation actions.

Targets CS2 server operators who need lightweight, extensible tooling to collect and triage player misconduct reports—especially suspected cheating—as part of server-side moderation beside automated detection such as [[cs2ac]].

## Links

- Repo: https://github.com/cs2-server-plugins/cs2-calladmin

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[cs2ac]] · [[cs2kac]] · [[7dtd-anticheatmod]] · [[cs2-hybrid-anticheat-proposal]]
