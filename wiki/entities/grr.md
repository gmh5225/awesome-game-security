---
title: GRR Rapid Response
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/google__grr.md
updated: 2026-08-07
confidence: medium
---

# GRR Rapid Response

Python incident-response framework for **remote live forensics** at fleet scale: a central server with a web admin UI and lightweight HTTP client agents on endpoints. Supports forensic artifact collection, file search, live memory extraction, registry dumps, and arbitrary Python-based analysis flows orchestrated across large machine populations — aimed at incident responders, forensic investigators, and SOC teams doing enterprise endpoint triage and evidence collection. (source: wiki/sources/descriptions/google__grr.md)

Complements one-shot triage collectors such as [[dfirtriage]] and offline RAM analysis via [[volatility3]] / [[dumpit-mirror]] in the AC Information System & Forensics lane.

## Links

- Repo: https://github.com/google/grr

## Related

[[dfirtriage]] · [[volatile-data-collector]] · [[volatility3]] · [[dumpit-mirror]] · [[kvcforensic]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
