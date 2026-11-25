---
title: Ab1BaS GameCheck
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/ab1bas0__Ab1BaS-GameCheck.md
updated: 2026-11-25
confidence: medium
---

# Ab1BaS GameCheck

Pair of read-only Windows **PowerShell** diagnostics (ab1bas0) for gaming crashes, freezes, bugchecks, and anti-cheat launch failures. No administrator rights, no system modifications, and no network I/O; reports are sanitized and copied to the desktop and clipboard for support handoff. (source: wiki/sources/descriptions/ab1bas0__Ab1BaS-GameCheck.md)

## Scripts

**Game stability** — Windows event logs, GPU drivers, memory, page file, Visual C++ and .NET runtimes, overlays, and recent bugcheck or driver-reset events.

**Anti-cheat compatibility** — Boot mode, Secure Boot, TPM, kernel isolation (VBS/HVCI), anti-cheat service status, known conflicting software, and blocked drivers from logs for **FACEIT**, Riot **Vanguard**, **Easy Anti-Cheat**, and **BattlEye**.

## Audience

Players, technicians, and sellers who need quick, transparent system snapshots for game security and stability troubleshooting—not AC bypass or exploit development.

## Positioning

Complements gamer-oriented platform-trust diagnostics such as [[securebootcheck]] and tournament pre-play verifiers such as [[kevar-integrity-checker]], with broader crash/stability context and multi-vendor AC service visibility.

## Links

- Repo: https://github.com/ab1bas0/ab1bas-gamecheck

## Related

[[easy-anti-cheat]] · [[vanguard]] · [[battleye]] · [[hvci]] · [[securebootcheck]] · [[kevar-integrity-checker]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]