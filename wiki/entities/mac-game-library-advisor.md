---
title: Mac Game Library Advisor
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/ruodou233__mac-game-library-advisor.md
updated: 2026-11-16
confidence: medium
---

# Mac Game Library Advisor

**Mac Game Library Advisor** (ruodou233/mac-game-library-advisor) is a packaged **Claude/agent skill** that audits an owned **Steam library on macOS** and classifies each title by whether it runs natively, works through a **Wine / Game Porting Toolkit (GPTK)** compatibility layer, is unlikely to work, or lacks reliable public data. It grades real-world performance and mod-framework viability (BepInEx, Workshop, script extenders), and explicitly flags risks from **kernel-level anti-cheat** ([[easy-anti-cheat]], [[battleye]], Vanguard, Ricochet) and third-party launchers that commonly block Wine-style environments. The workflow is defined in Markdown skill instructions plus a distributable `.skill` bundle, and it mandates fresh lookups across AppleGamingWiki, PCGamingWiki, ProtonDB, and community reports rather than static allowlists—aimed at Mac players avoiding wasted setup time and researchers studying how commercial anti-cheat and platform checks interact with compatibility layers on Apple hardware. (source: wiki/sources/descriptions/ruodou233__mac-game-library-advisor.md)

## Research framing

Legitimate **compatibility triage**, not bypass: the skill documents which titles are blocked or degraded by AC and launcher policy under unofficial runtimes, complementing GNU/Linux lanes such as [[proton]] and [[are-we-anti-cheat-yet]] and macOS launchers such as [[obelisk]]. (source: wiki/sources/descriptions/ruodou233__mac-game-library-advisor.md)

## Links

- Repo: https://github.com/ruodou233/mac-game-library-advisor [Claude/agent skill to classify a Steam library on Mac by native play, Wine/GPTK viability, and kernel anti-cheat blockers (EAC, BE, Vanguard)]

## Related

[[easy-anti-cheat]] · [[battleye]] · [[proton]] · [[obelisk]] · [[are-we-anti-cheat-yet]] · [[crossover-patcher]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]