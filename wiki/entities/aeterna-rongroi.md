---
title: Aeterna-rongroi
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/aeterna__aeterna-rongroi.md
updated: 2026-09-11
confidence: medium
---

# Aeterna-rongroi

**Offline, read-only, open-source PC-check tool** for **FiveM** communities that scans a Windows host for cheat traces and risky machine posture. Presents forensic evidence as **Found**, **NotFound**, or **Unmeasured** results rather than issuing clean or guilty verdicts—supporting player self-checks and admin screenshare sessions with transparent, privacy-conscious inspection. (source: wiki/sources/descriptions/aeterna__aeterna-rongroi.md)

## Architecture

Built primarily in **Rust** with a **Tauri 2** desktop app and **React/TypeScript** UI, plus a **CLI** supporting self-check and screenshare modes with path redaction and consent flows. Detection is driven by an embedded **YAML rules engine** and read-only collectors that inspect artifacts such as **Secure Boot** posture without writing to or networking with the host.

## Audience

Targets **game security staff**, **server moderators**, and **players** who need evidence-oriented FiveM PC checks without opaque auto-ban verdicts.

## Links

- Repo: https://github.com/aeterna/aeterna-rongroi

## Related

[[dead-anticheat]] · [[atomicshieldclient]] · [[irontrace]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
