---
title: Architectography
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Architectography__Architectography.md
updated: 2026-11-20
confidence: medium
---

# Architectography

**Architectography** (Architectography/Architectography) is a **Windows desktop launcher and control panel** (Python + PyWebView) for quickly auditing a host for third-party or unauthorized software. It provides one-click download and launch of common forensic and system utilities—**Everything**, NirSoft viewers (Prefetch, USB, browser history, jump lists, user assist), **Process Hacker**, **JournalTrace**, and **System Informer**—plus live process enumeration via **psutil** with search and filtering on executable, library names, and paths. Hardware and OS summaries and shortcuts to online malware and URL analysis services sit in the same GUI hub. Investigators, anti-cheat staff, and security analysts can use it when screening player PCs or tournament machines for cheats, injectors, and other unwanted programs without assembling separate toolchains manually. (source: wiki/sources/descriptions/Architectography__Architectography.md)

## Stack

- **Shell** — Python + PyWebView graphical hub; orchestrates external utilities rather than replacing them.
- **Artifact lane** — NirSoft prefetch/USB/browser/jump-list/user-assist viewers; JournalTrace; Everything indexing.
- **Live lane** — psutil process inventory with path/name filters; Process Hacker / System Informer launchers.

## Positioning

Complements integrated scanners such as [[custos]] and [[eagle-eye]] and read-only probe scripts such as [[dexcheck]] by **aggregating launcher shortcuts** for familiar DFIR/sysinternals-style tooling during cheat-software triage (Anti Cheat / Guide).

## Links

- Repo: https://github.com/Architectography/Architectography

## Related

[[custos]] · [[dexcheck]] · [[anticheat-scanner]] · [[dfirtriage]] · [[windows-forensic-artifacts]] · [[overviews/anti-cheat]] · [[concepts/detector-operations]]