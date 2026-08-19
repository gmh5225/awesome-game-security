---
title: AutoRE
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/a1ext__auto_re.md
updated: 2026-08-19
confidence: medium
---

# AutoRE

Python **IDA Pro plugin** that accelerates binary triage by automatically renaming dummy functions from imported API calls and jump targets, then tagging functions by behavioral indicators—networking, process injection, crypto, and file activity—with a dedicated tag view. Used in reverse engineering and game security research to prioritize unfamiliar or suspicious logic faster. (source: wiki/sources/descriptions/a1ext__auto_re.md)

Behavioral tagging + API-driven naming—not manual batch rename ([[ida-names]]), instruction-signature library ID ([[renamaida]]), or RTTI class naming ([[pyclassinformer]]). Complements [[autorename]] and [[finger]] in the symbol-recovery / malware-triage lane.

## Links

- Repo: https://github.com/a1ext/auto_re

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[autorename]] · [[renamaida]] · [[ida-names]] · [[list-of-ida-plugins]]
