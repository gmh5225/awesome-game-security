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

**fpsdet** (Nimdy/detect-FPS-hackers) is a **server-side anti-cheat evidence engine** for first-person shooters. It ingests **JSON combat and movement logs** from a dedicated game server, scores each player against game rules, human baselines, and client visibility limits, and produces **case files for manual review** rather than automatic bans. Written in plain **Python 3.11+** with no runtime dependencies. (source: wiki/sources/descriptions/Nimdy__detect-FPS-hackers.md)

README category: Anti Cheat / Open Source Anti Cheat System.

## Pipeline

CLI stages cover ingest, baseline building, scoring, and dashboard generation. JSON schemas, game profiles, and example emitters ship for **Unity**, **Unreal**, and **Godot**.

## Check families

- **Gear violations** — speed, fire rate, recoil manipulation
- **Statistical outliers** — ranked human cohort baselines
- **Information-theoretic signals** — hidden tracking, wire-versus-picture aim
- **Cross-account patterns** — shared humanizer signatures

Synthetic demo populations, an offline operations review board, optional AI triage briefs, and Grafana/Kibana/Splunk mappings support indie studios and community server operators.

## Positioning

Server-log-based FPS cheat evidence without client installs—beside demo-telemetry research such as [[yaacs-anticheat]], behavioral labs such as [[apex-anticheat-lab]], and offline review pipelines such as [[cs2-overwatch]].

## Links

- Repo: https://github.com/Nimdy/detect-FPS-hackers

## Related

[[apex-anticheat-lab]] · [[yaacs-anticheat]] · [[cs2-overwatch]] · [[cs2guard]] · [[concepts/detector-operations]] · [[overviews/anti-cheat]]
