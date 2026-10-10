---
title: pubg-bigdata-analytics
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/README-categories.md
updated: 2026-10-10
confidence: low
---

# pubg-bigdata-analytics

**pubg-bigdata-analytics** (ahuhu789) is a **big-data analytics pipeline** for **PlayerUnknown's Battlegrounds (PUBG)** match telemetry: ingest large public match datasets, preprocess and feature-engineer player behavior in **Apache Spark (PySpark)**, cluster statistically unusual profiles with **K-Means**, apply **rule-based esports physics checks**, persist query-oriented aggregates in **Apache Cassandra**, and visualize results in a **Streamlit** dashboard. README category: Anti Cheat — offline batch anomaly research, not a live game-server AC product. (source: wiki/sources/README-categories.md)

## Positioning

Batch statistical cheat-signal research on historical match rows—beside demo-telemetry ML such as [[cs2guard]] and [[yaacs-anticheat]], server-log evidence pipelines such as [[detect-fps-hackers]], and offensive PUBG CV samples such as [[yolov5-pubg]]. Pair cluster outputs and rule flags with [[detector-operations]] human-review discipline before treating scores as sanctions.

## Related

[[ai-aimbot-detection]] · [[cs2guard]] · [[yaacs-anticheat]] · [[detect-fps-hackers]] · [[overviews/anti-cheat]]

## Links

- Upstream: https://github.com/ahuhu789/pubg-bigdata-analytics
