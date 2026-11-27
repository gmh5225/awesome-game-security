---
title: IDA Proofmark
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/bgrubbs1__ida-proofmark.md
  - wiki/sources/README-categories.md
updated: 2026-11-27
confidence: medium
---

# IDA Proofmark

Experimental **IDAPython** plugin for Hex-Rays IDA that binds analyst conclusions to checkable **byte anchors** at the cursor address. Python UI plus a separate core library implements matching logic; each record stores a claim, notes, and up to sixteen evidence bytes in a **JSON sidecar** beside the database without modifying the IDB or using the network. Workflows include capturing conclusions at an address, listing records, verifying them against initialized IDB bytes (with progress and cancellation), comparing prior sidecars when binaries change, and jumping when anchors are unchanged or uniquely relocated. Verification labels each record **unchanged**, **moved candidate**, **ambiguous**, **not found**, or **incomplete** after scanning the open image. (source: wiki/sources/descriptions/bgrubbs1__ida-proofmark.md)

Suited to game-security and malware RE when tracking whether supporting machine code still matches an earlier analysis across client patches or anti-cheat updates. Complements annotation porting via [[oh-my-dump]] and [[ida-migrator]]; pair byte-anchored claim checks with [[research-rigor]] and [[static-runtime-evidence]] on [[overviews/reverse-engineering]].

## Links

- Repo: https://github.com/bgrubbs1/ida-proofmark

## Related

[[oh-my-dump]] · [[ida-migrator]] · [[reverify]] · [[static-runtime-evidence]] · [[research-rigor]] · [[binary-diffing]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]