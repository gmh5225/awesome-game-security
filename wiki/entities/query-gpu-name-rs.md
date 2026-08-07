---
title: query-gpu-name-rs
kind: entity
topics: [anti-cheat, graphics-api]
sources:
  - wiki/sources/descriptions/gmh5225__query-gpu-name-rs.md
updated: 2026-08-07
confidence: medium
---

# query-gpu-name-rs

Rust utility for querying **GPU display names on Windows**. Aimed at anti-cheat engineers and defensive security researchers in the Detection:HWID lane who need adapter name strings as a hardware fingerprint signal. (source: wiki/sources/descriptions/gmh5225__query-gpu-name-rs.md)

Complements cross-platform inventory libraries such as [[hwinfo]], WMI hardware CLIs such as [[windows-hardware-info]], and NvAPI GPU serial/board fingerprint tooling such as [[nvidiaapi]]; sits opposite offensive GPU spoof samples such as [[nvidia-gpu-spoof]] / [[hwidspoofer]].

## Links

- Repo: https://github.com/gmh5225/query-gpu-name-rs

## Related

[[overviews/anti-cheat]] · [[overviews/graphics-api]] · [[hwinfo]] · [[windows-hardware-info]] · [[nvidiaapi]] · [[hwid-checker-mg]] · [[hwidspoofer]]
