---
title: Cheatguard
kind: entity
topics: [anti-cheat, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/JUS7205__cheatguard.md
updated: 2026-08-24
confidence: medium
---

# Cheatguard

Engine-agnostic **anti-cheat detection toolkit** (Rust) that scans a target process's **loaded modules** and scores how likely cheating software is present. Detection logic lives in a **JSON-driven ruleset**—signatures are data, not hard-coded—with configurable weights for signals such as known cheat names, suspicious module name patterns, unexpected load paths, unsigned modules, and module-count anomalies. On Windows it enumerates modules via **Win32 APIs** and emits a deterministic **0–100 risk score** with **CLEAN**, **SUSPICIOUS**, or **MALICIOUS** verdicts in a JSON report; other platforms return an honest unsupported stub rather than fabricated results. Ships as both a **library** and CLI (`cheatguard scan <pid>`) for blue-team game security research, defensive process-integrity checks, and custom anti-cheat or forensics workflows. (source: wiki/sources/descriptions/JUS7205__cheatguard.md)

Complements educational module-enumeration samples such as [[basic-anti-cheat]], manual-map forensics tools such as [[modfinder]], and live injection scanners such as [[xmalhunter]].

## Links

- Repo: https://github.com/JUS7205/cheatguard

## Related

[[basic-anti-cheat]] · [[modfinder]] · [[betashield]] · [[xmalhunter]] · [[anticheat-poc]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
