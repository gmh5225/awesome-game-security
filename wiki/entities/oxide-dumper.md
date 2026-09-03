---
title: oxide-dumper
kind: entity
topics: [game-hacking, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/LabGuy94__OxideDumper.md
updated: 2026-08-23
confidence: medium
---

# oxide-dumper

Automated offset pipeline for **Facepunch Rust** (LabGuy94; cheat `[Auto Dump]`). Python scripts orchestrate **SteamCMD** game fetch, **[[il2cppdumper]]** processing, and **GitHub Actions** CI to regenerate offset definitions after patches. Exports reusable **C++ header** output instead of relying on manual one-off reverse-engineering steps each update. Intended for game security researchers and tooling maintainers who track Rust's frequent update cadence. (source: wiki/sources/descriptions/LabGuy94__OxideDumper.md)

Complements canonical [[il2cppdumper]] static dumps, C++ multi-format pipelines such as [[rust-auto-dumper]], and per-title automated offset refreshers such as [[cs2-dumper]]; downstream Facepunch Rust cheat and AC research samples such as [[lord-abbot-rust-external-cheat]], [[rust-external]], and [[rustsecure-re]] consume similar offset/header workflows.

## Links

- Repo: https://github.com/LabGuy94/OxideDumper

## Related

[[il2cpp]] · [[il2cppdumper]] · [[rust-auto-dumper]] · [[cs2-dumper]] · [[lord-abbot-rust-external-cheat]] · [[rust-external]] · [[rustsecure-re]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
