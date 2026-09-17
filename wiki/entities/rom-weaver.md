---
title: rom-weaver
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/rom-weaver__rom-weaver.md
updated: 2026-09-17
confidence: medium
---

# rom-weaver

Local-first toolkit for **ROM images and disc formats** from rom-weaver. (source: wiki/sources/descriptions/rom-weaver__rom-weaver.md)

## Capabilities

- Shared Rust core as native CLI and threaded WASM inside an offline React PWA — files stay on the user's machine.
- Inspect, extract, compress, apply, and create patches across 21 formats (IPS, BPS, UPS, xdelta/VCDIFF, PPF, Dreamcast DCP).
- Container handling for ZIP, 7z, CHD, RVZ, and other archive/disc image types.
- Checksum verification with header repair, ordered multi-patch chains, cheat-code baking, trim/restore, offline save editing, and shareable workflow bundles.

## Use cases

Aimed at retro game modders, ROM hackers, and preservationists needing end-to-end patch, verify, and repack pipelines without cloud uploads. Retro-console RE lane beside [[openfpga-gbc-cheats-ui]] cheat deployment and [[bizhawk]] RAM-search workflows — not a live-game memory cheat.

## Links

- Repo: https://github.com/rom-weaver/rom-weaver

## Related

[[openfpga-gbc-cheats-ui]] · [[bizhawk]] · [[pc-wackywheels-doc]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
