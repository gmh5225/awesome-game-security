---
title: pubg-bigdata-analytics
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/ahuhu789__pubg-bigdata-analytics.md
  - wiki/sources/README-categories.md
updated: 2026-10-10
confidence: medium
---

# pubg-bigdata-analytics

**pubg-bigdata-analytics** (ahuhu789) is an end-to-end **big-data pipeline** for **PlayerUnknown's Battlegrounds (PUBG)** match records: ingest large-scale public match telemetry, cleanse and analyze player behavior with **PySpark** (Spark SQL match analytics, **MLlib K-Means** clustering), combine unsupervised anomaly scores with **game-physics rule checks** (extreme headshot rates, implausible movement), persist **Apache Parquet** outputs and load query-oriented aggregates into **Apache Cassandra** (optional **Docker Compose** stack), and expose ranked anomaly alerts with explanations via a **Streamlit** dashboard (infrastructure status, match analytics, lookup by match or player id). Targets researchers exploring **server-side or offline** cheat detection, unsupervised anomaly scoring, and big-data tooling for competitive-shooter telemetry—not live client enforcement. (source: wiki/sources/descriptions/ahuhu789__pubg-bigdata-analytics.md)

## Capabilities

- **Ingest & cleanse** — PySpark preprocessing on large PUBG match datasets.
- **Match analytics** — Spark SQL aggregations over player and match dimensions.
- **Anomaly scoring** — K-Means clustering plus rule-based esports physics flags.
- **Storage** — Parquet for processed results; Cassandra for query-oriented access.
- **Operations UI** — Streamlit dashboard for alerts, explanations, and id lookup.

## Positioning

Batch statistical cheat-signal research on historical match rows—beside demo-telemetry ML such as [[cs2guard]] and [[yaacs-anticheat]], server-log evidence pipelines such as [[detect-fps-hackers]], and offensive PUBG CV samples such as [[yolov5-pubg]]. Pair cluster outputs and rule flags with [[detector-operations]] human-review discipline before treating scores as sanctions.

## Related

[[ai-aimbot-detection]] · [[cs2guard]] · [[yaacs-anticheat]] · [[detect-fps-hackers]] · [[overviews/anti-cheat]]

## Links

- Upstream: https://github.com/ahuhu789/pubg-bigdata-analytics
