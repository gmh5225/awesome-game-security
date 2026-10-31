---
title: Anticheat Lab (senolbasyigit)
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/senolbasyigit__anticheat-lab.md
  - wiki/sources/README-categories.md
updated: 2026-10-31
confidence: high
---

# Anticheat Lab (senolbasyigit)

**Anticheat-lab** (senolbasyigit/anticheat-lab) is a **Claude Code skill** and Python toolkit for tamper-testing your own game builds before release by scanning process memory for exposed values such as health, ammo, or currency, then documenting findings with server-side defense recommendations and regression tests. It implements a Cheat Engine-style workflow on Windows through scan, next-scan filtering, and read/write helpers backed by a **devbuild.json** SHA-256 guard that only permits work on verified developer executables you own. A separate RPA mode automates third-party Windows applications via exports, APIs, or UI Automation with **pywinauto** without reading their memory. Reference guides cover defense priorities from server authority and delta validation through telemetry and integrity signals, with client obfuscation as a secondary measure. Aimed at game developers and security-minded teams who want to harden releases against memory editing and structure anti-cheat validation before shipping. (source: wiki/sources/descriptions/senolbasyigit__anticheat-lab.md)

## Capabilities

- Windows **scan → next-scan filter → read/write** workflow on attached processes (CE-style value hunting)
- **devbuild.json** SHA-256 allowlist so memory work runs only on verified developer executables the team owns
- Structured reports pairing exposed client values with **server-side validation fixes** and **regression tests**
- **Claude Code skill** wrapping the Python scripts for agent-guided audit loops
- Optional **RPA mode** (exports, APIs, UI Automation via pywinauto) for third-party Windows apps—no process memory reads

## Defense guidance

Bundled reference material ranks mitigations: **server authority** and **delta/rate validation** first, then **telemetry** and **integrity signals**; **client obfuscation** is documented as secondary hardening—not a substitute for authoritative gameplay state. (source: wiki/sources/descriptions/senolbasyigit__anticheat-lab.md)

## Distinction

Not to be confused with [[anticheat-lab]] (Ogonx)—six-month VM self-study on deliberately vulnerable multiplayer builds. This repo targets **pre-ship memory exposure audits** on owned dev binaries plus optional RPA automation.

## Positioning

Listed under README **Anti Cheat → Open Source Anti Cheat System**. Complements general memory tooling such as [[pymemory-editor]] and [[cheat-engine]] with a **defensive pre-release audit** workflow; pairs with server-side QA clients such as [[anticheat-qa]] and educational curricula such as [[anticheat-lab]] (Ogonx). (source: wiki/sources/README-categories.md)

## Links

- Repo: https://github.com/senolbasyigit/anticheat-lab

## Related

[[anticheat-lab]] · [[anticheat-qa]] · [[pymemory-editor]] · [[detector-operations]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
