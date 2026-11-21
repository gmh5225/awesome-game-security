---
title: AmongShield
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/AmongShieldServer__AmongShield.md
updated: 2026-11-21
confidence: medium
---

# AmongShield

**AmongShield** is a free community anti-cheat **Among Us** game server. Players join by selecting a custom region (not official NA/EU/Asia) after onboarding via a short PowerShell script that edits `regionInfo.json`, bundled JSON region definitions, and a static HTML setup page with mobile deep links. The playable backend runs on a modified **Impostor** open-source Among Us server; this repository focuses on client region setup and documentation rather than the full server implementation. (source: wiki/sources/descriptions/AmongShieldServer__AmongShield.md)

Server-side protections feed **role-ESP** cheat menus multiple decoy impostors, detect impossible actions and self-advertising cheat menus, kick offenders with lobby chat callouts, and post truthful impostor summaries after each round. Hosts can tune lobby vision via chat commands and use automatic host rotation in public games. Targets PC and mobile players who want vanilla Among Us with stronger resistance to menus such as MalumMenu and Sicko Menu **without** installing game mods or patching client binaries—complementary to BepInEx host/client plugins such as [[among-us-anti-cheat]], [[au-anticheat]], and [[banmod]].

## Defensive surfaces

- **ESP deception** — decoy impostor roles served to role-reveal cheat menus.
- **Behavior validation** — impossible actions and self-advertising menu detection.
- **Enforcement** — kicks with lobby chat announcements.
- **Post-round transparency** — truthful impostor summaries.
- **Host tooling** — lobby vision chat commands; automatic host rotation in public lobbies.

## Links

- Repo: https://github.com/AmongShieldServer/AmongShield

## Related

[[among-us-anti-cheat]] · [[among-us-3d-vr-anticheat]] · [[au-anticheat]] · [[banmod]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]