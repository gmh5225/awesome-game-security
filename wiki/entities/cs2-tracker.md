---
title: cs2-tracker
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/LooperSalty__cs2-tracker.md
updated: 2026-08-23
confidence: medium
---

# cs2-tracker

Windows **Counter-Strike 2** application that combines lifetime player statistics, live match tracking, and an **explainable heuristic anti-cheat analysis engine**. Written primarily in Python with a local **FastAPI** REST API, **SQLite** storage, and optional Qt desktop and web interfaces. (source: wiki/sources/descriptions/LooperSalty__cs2-tracker.md)

## Data sources

Ingests **public Steam Web API** data and official **Game State Integration (GSI)** feeds rather than reading game memory or injecting code—keeping the tool in an observable-data, non-invasive lane.

## Suspicion engine

Roughly **thirty detectors** span aim, weapons, account metadata, live behavior, consistency, progression drift, and ban history. Players receive **0–100 suspicion scores** with Bayesian smoothing and multi-signal corroboration so analysts can see which signals contributed.

## Overlay

A native **C++ in-game overlay** can display live scores and per-player risk during matches.

## Audience

Targets competitive players, analysts, and game-security researchers who want **transparent, statistical cheat-risk assessment** from observable data instead of client-side enforcement.

## Positioning

Complements server-side heuristic plugins such as [[osanticheat]] and community moderation tools such as [[cs2-calladmin]], but runs locally for players and reviewers. Sits opposite memory-reading CS2 cheat stacks such as [[cs2-webradar]] and [[cs2-external-cheat]].

## Links

- Repo: https://github.com/LooperSalty/cs2-tracker

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[osanticheat]] · [[cs2ac]] · [[cs2-calladmin]] · [[aimbot-detection-prototype]] · [[cs2-hybrid-anticheat-proposal]] · [[alibi]] · [[cs2-anticheat]]
