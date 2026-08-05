---
title: PE-sieve
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/hasherezade__pe-sieve.md
updated: 2026-08-05
confidence: medium
---

# PE-sieve

Lightweight Windows engine that scans **one process at a time** to detect in-memory malware and injection artifacts, and to **collect potentially malicious material** for follow-on analysis. Aimed at anti-cheat engineers and defensive security researchers in the `Detection:hook` lane — the core library behind live scanners such as [[xmalhunter]] (libpeconv integration) and complementary to hook/patch tooling such as [[hookhunter]] and [[hook-buster]]. (source: wiki/sources/descriptions/hasherezade__pe-sieve.md)

## Links

- Repo: https://github.com/hasherezade/pe-sieve

## Related

[[xmalhunter]] · [[hookhunter]] · [[hook-buster]] · [[patch-finder]] · [[faultline]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
