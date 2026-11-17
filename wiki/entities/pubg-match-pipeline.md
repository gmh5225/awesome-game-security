---
title: pubg-match-pipeline
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/eysang-blip__pubg-match-pipeline.md
  - wiki/sources/README-categories.md
updated: 2026-11-17
confidence: medium
---

# pubg-match-pipeline

**pubg-match-pipeline** (eysang-blip) is a **Python** end-to-end workflow that ingests **PlayerUnknown's Battlegrounds (PUBG)** match telemetry from the **official match API**, loads it into **SQLite**, and exports **prioritized manual anti-cheat review candidates**. Orchestration covers match ID sampling, incremental JSON collection with **rate-limit** handling, deterministic database rebuilds, and a **nine-check validation gate** that blocks downstream analysis when data quality fails. The analytical layer uses **SQL views** to filter squad human players, compute per-match **damage-per-minute z-scores** and **headshot-rate** outliers, and rank suspicious performances—aimed at practitioners who want reproducible, statistics-driven scouting from **public match summaries** rather than in-client telemetry. (source: wiki/sources/descriptions/eysang-blip__pubg-match-pipeline.md)

## Pipeline stages

- **Ingest** — sampled match IDs, incremental API JSON fetch with rate-limit awareness.
- **Persistence** — SQLite with repeatable full rebuild semantics.
- **Quality gate** — nine automated checks; analysis halts on failed data quality.
- **Scoring** — SQL-driven z-score and headshot-rate outlier ranking for analyst queues.

## Positioning

Lightweight **official-API + SQLite** review pipeline for PUBG—complements large-scale batch stacks such as [[pubg-bigdata-analytics]] (PySpark/K-Means) and dedicated-server log classifiers such as [[detect-fps-hackers]]. Statistical ranks are **review hints**, not sanctions—pair exports with [[detector-operations]] and [[research-rigor]] before enforcement. Contrasts with offensive PUBG client samples such as [[pubg-external-cheat]] and CV triggerbot references such as [[yolov5-pubg]]. (source: wiki/sources/descriptions/eysang-blip__pubg-match-pipeline.md)

## Links

- Repo: https://github.com/eysang-blip/pubg-match-pipeline [Python pipeline ingesting PUBG official match API data into SQLite, running nine automated quality checks, and SQL-driven extraction of cheat-review candidates]

## Related

[[pubg-bigdata-analytics]] · [[detect-fps-hackers]] · [[apex-anticheat-lab]] · [[ban-hammer]] · [[battleye]] · [[overviews/anti-cheat]] · [[concepts/ai-aimbot-detection]]