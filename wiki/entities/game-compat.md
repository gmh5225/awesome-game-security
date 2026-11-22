---
title: Game Compat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/miyu-agent__game-compat.md
updated: 2026-11-22
confidence: medium
---

# Game Compat

**Game-compat** (miyu-agent/game-compat) is a **Miyu agent skill package** plus a **Python 3** command-line tool that answers whether a PC game runs on **GNU/Linux** (including **Steam Deck**) and **Apple Silicon Macs**. The CLI resolves titles by **Steam App ID** or name (including **Chinese** store strings), fetches compatibility signals in **parallel** using only the **standard library**, and can filter Mac results by chip and emit **JSON** for automation. Aggregated sources include **ProtonDB** player reports, [[are-we-anti-cheat-yet]] anti-cheat status, caniplayonlinux verdicts, Valve **Steam Deck** verification, and **MacGamingDB** data on native play, CrossOver, and Parallels. It targets gamers planning Linux or Mac installs and anyone who needs quick, sourced answers about Proton compatibility and whether anti-cheat blocks online play on non-Windows platforms. (source: wiki/sources/descriptions/miyu-agent__game-compat.md)

## Research framing

Legitimate **compatibility and AC-status triage**, not bypass: the skill and CLI surface public verdict layers—Proton fit, Deck verification, and whether kernel anti-cheat blocks unofficial platforms—complementing desktop planners such as [[rigcheck]], macOS library skills such as [[mac-game-library-advisor]], and launchers such as [[pointblank-linux]] and [[proton]]. (source: wiki/sources/descriptions/miyu-agent__game-compat.md)

## Links

- Repo: https://github.com/miyu-agent/game-compat [Agent skill and CLI aggregating ProtonDB, AreWeAntiCheatYet, caniplayonlinux, Steam Deck verification, and MacGamingDB for Linux/Mac playability and anti-cheat status]

## Related

[[are-we-anti-cheat-yet]] · [[proton]] · [[rigcheck]] · [[mac-game-library-advisor]] · [[pointblank-linux]] · [[ferret]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]