---
title: detect-FPS-hackers (fpsdet)
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Nimdy__detect-FPS-hackers.md
  - wiki/sources/README-categories.md
updated: 2026-10-03
confidence: medium
---

# detect-FPS-hackers (fpsdet)

**fpsdet** (Nimdy/detect-FPS-hackers) is a **server-side anti-cheat evidence engine** for first-person shooters. It ingests **JSON combat and movement logs** from a dedicated game server, scores each player against game rules, human baselines, and **client visibility limits**, and produces **case files for manual review** rather than automatic bans. Written in plain **Python 3.11+** with no runtime dependencies. Targets indie and small studios, community server operators, and teams building game-security workflows without client installs. (source: wiki/sources/descriptions/Nimdy__detect-FPS-hackers.md)

README category: Anti Cheat / Open Source Anti Cheat System.

## Detection surface

- **Gear violations** — speed, fire rate, and recoil manipulation against authoritative server rules.
- **Statistical outliers** — ranked human cohort baselines for population- and skill-matched reference distributions.
- **Information-theoretic signals** — hidden tracking and wire-versus-picture aim patterns from server-side observables.
- **Cross-account patterns** — shared humanizer signatures across linked accounts.

JSON schemas, game profiles, and example emitters ship for **Unity**, **Unreal**, and **Godot** dedicated-server integrations.

## Operations

CLI stages cover **ingest**, **baseline building**, **scoring**, and **dashboard generation**. Synthetic demo populations support threshold calibration; an **offline operations review board** and optional **AI triage briefs** route case files to human reviewers. Grafana, Kibana, and Splunk mappings help teams wire outputs into existing SIEM workflows. Pair baseline cohorts and scoring thresholds with [[detector-operations]] shadow/canary practices before treating case outputs as sanction evidence.

## Positioning

Server-log-based FPS cheat evidence without client installs—beside demo-telemetry research such as [[yaacs-anticheat]], behavioral labs such as [[apex-anticheat-lab]], and offline review pipelines such as [[cs2-overwatch]].

## Peers

[[apex-anticheat-lab]] · [[yaacs-anticheat]] · [[cs2-overwatch]] · [[cs2guard]] · [[esp-killer]]

## Links

- Repo: https://github.com/Nimdy/detect-FPS-hackers

## Related

[[concepts/detector-operations]] · [[concepts/ai-aimbot-detection]] · [[overviews/anti-cheat]]
