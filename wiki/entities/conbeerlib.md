---
title: ConBeerLib
kind: entity
topics: [anti-cheat, mobile-security]
sources:
  - wiki/sources/descriptions/su-vikas__conbeerlib.md
updated: 2026-07-21
confidence: medium
---

# ConBeerLib

C/Python library for detecting **container and virtualization** environments from within a Linux (incl. Android) process. Probes Docker, LXC, Kubernetes, WSL, and broader VM indicators via cgroup hierarchies, filesystem markers, environment variables, and hardware characteristics so apps can tell where they are running. Aimed at security researchers and developers implementing environment detection for anti-analysis or deployment awareness. (source: wiki/sources/descriptions/su-vikas__conbeerlib.md)

README lane: Android library for detecting Android virtual containers — sits with `Detection:Virtual Environments` alongside sandbox/VE demos such as [[anticuckoo]], curated anti-virt lists such as [[awesome-anti-virtualization]], and mobile RASP/emulator signals such as [[droidshield]].

## Links

- Repo: https://github.com/su-vikas/conbeerlib (README tag: Android virtual containers)

## Related

[[overviews/anti-cheat]] · [[overviews/mobile-security]] · [[anticuckoo]] · [[awesome-anti-virtualization]] · [[droidshield]] · [[windows-subsystem-linux]]
