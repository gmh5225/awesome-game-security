---
title: rust-auto-dumper
kind: entity
topics: [game-hacking, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/Akandesh__rust-auto-dumper.md
updated: 2026-09-03
confidence: medium
---

# rust-auto-dumper

**C++ auto-dumping and parsing pipeline** for **Facepunch Rust** (Akandesh; cheat `[Auto Dump]` / game:rust). Monitors **Steam build IDs**, executes dump scripts, and parses generated `dump.cs` and script data with **regex-based extraction**. Emits structured outputs—**JSON**, **C++ headers**, and **C# constants**, including variants for **encrypted fields**—so tooling maintainers can keep synchronized Rust offset data in multiple formats after patches. Used by game security researchers and downstream cheat/AC tooling developers. (source: wiki/sources/descriptions/Akandesh__rust-auto-dumper.md)

Complements Python/CI pipelines such as [[oxide-dumper]] and canonical [[il2cppdumper]] static dumps; downstream Facepunch Rust samples such as [[lord-abbot-rust-external-cheat]], [[rust-dma-cheat]], and [[rustsecure-re]] consume similar offset/header workflows.

## Links

- Repo: https://github.com/Akandesh/rust-auto-dumper

## Related

[[oxide-dumper]] · [[il2cpp]] · [[il2cppdumper]] · [[cs2-dumper]] · [[lord-abbot-rust-external-cheat]] · [[rust-dma-cheat]] · [[rustsecure-re]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
