---
title: FlyingGuys
kind: entity
topics: [game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__FlyingGuys.md
updated: 2026-08-13
confidence: medium
---

# FlyingGuys

**FlyingGuys** is a **Fall Guys** game cheat (gmh5225) combining a **custom kernel driver** for cross-process memory operations, a **KdMapper-based loader**, and a **user-mode client** with **ImGui** overlay rendering. The usermode stack uses **zlib compression** for network data manipulation. (source: wiki/sources/descriptions/gmh5225__FlyingGuys.md)

A fully expanded variant with fly/movement hacks lives in [[flying-guys-fully-modified]].

Sits in the kernel-driver external cheat lane beside KdMapper load research such as [[kdmapper-rs]], ImGui overlay substrates such as [[imgui]], and other gmh5225 KdMapper + ImGui stacks such as [[full-hwid-spoofer-v6]] and [[anti-cheat-amateur]].

## Links

- Repo: https://github.com/gmh5225/FlyingGuys

## Related

[[flying-guys-fully-modified]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[kdmapper-rs]] · [[imgui]] · [[full-hwid-spoofer-v6]] · [[anti-cheat-amateur]]
