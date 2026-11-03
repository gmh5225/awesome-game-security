---
title: Ocean Anti-Cheat Analysis
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/fluxolex__ocean-anticheat-analysis.md
  - wiki/sources/README-categories.md
updated: 2026-11-03
confidence: medium
---

# Ocean Anti-Cheat Analysis

**ocean-anticheat-analysis** (fluxolex/ocean-anticheat-analysis) publishes a long-form static reverse-engineering study of the Ocean Anti-Cheat Windows client (`ocean.exe`) used in Minecraft and FiveM community screenshare workflows. The work unpacks a Go binary protected with VMProtect and garble using Unicorn-based unpacking, Python API stubs, and large-scale Ghidra decompilation without executing the sample on a live system. (source: wiki/sources/descriptions/fluxolex__ocean-anticheat-analysis.md)

## Documented surfaces

- Sixteen client–server channels, weak protocol protections (CryptoJS password encryption, redirect URL signing, detection keys from server-time sine sums)
- **OceanGraper** kernel driver behavior, data exfiltration paths, and privacy-policy claims versus observed telemetry

## Role in the README map

Listed under **Anti Cheat** beside consensual screenshare tooling such as [[hapiscanner]], [[error-pc-check]], and [[dexcheck]] for evidence-oriented third-party AC client RE.

## Links

- Repo: https://github.com/fluxolex/ocean-anticheat-analysis

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[hapiscanner]] · [[dexcheck]] · [[screenshare-signatures]] · [[research-rigor]]
