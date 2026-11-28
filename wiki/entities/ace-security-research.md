---
title: ace-security-research
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Leeksov__ace-security-research.md
updated: 2026-11-28
confidence: medium
---

# ace-security-research

Structured **authorized security assessment** of Tencent **ACE (Anti-Cheat Expert)** **developer console** infrastructure at `intl.anticheatexpert.com`, including related **CDN**, **auth**, and **ibox** microservice boundaries. Documents confirmed and blocked findings—**IDOR** exposure of game SDK secret keys and admin metadata, unauthenticated CDN payloads, **OAuth** misconfigurations, and additional console/backend weaknesses—with reproduction steps and impact analysis. (source: wiki/sources/descriptions/Leeksov__ace-security-research.md)

## Tooling and datasets

Python utilities automate **gateway health** monitoring, **game ID** enumeration, **IDOR** scanning, and **CDN channel** discovery. JSON datasets and markdown appendices map services, channels, and attack surfaces for researchers studying commercial anti-cheat **control planes** and responsible disclosure workflows—not client-side `libanogs` RE or kernel driver dumps.

Listed in the README under **Explore AntiCheat System:ACE** as an authorized console/CDN/backend assessment with recon scripts.

Complements client-side and on-host Tencent ACE dossiers such as [[anticheatexpert]], [[ff-ace-anticheat-analysis]], and [[sgame-ace-analysis]], and other Leeksov defensive maps such as [[rustsecure-re]] and [[roblox-ios-research]].

## Links

- Repo: https://github.com/Leeksov/ace-security-research

## Related

[[anticheatexpert]] · [[ff-ace-anticheat-analysis]] · [[sgame-ace-analysis]] · [[starrail-ace-b]] · [[rustsecure-re]] · [[roblox-ios-research]] · [[research-rigor]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]