---
title: cs2-p2c-templates
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/ccsimplyspolit__CS2-P2C-TEMPLATES.md
updated: 2026-08-17
confidence: medium
---

# cs2-p2c-templates

**CS2 security-research P2C templates** (ccsimplyspolit) — one-to-one reverse-engineered ports of a VMProtect-protected anti-VAC helper and related injector tooling for studying **VAC Live** and CS2 client internals on insecure local or CTF setups. (source: wiki/sources/descriptions/ccsimplyspolit__CS2-P2C-TEMPLATES.md)

## Core artifacts

- **VacLiveBypass** — C/C++ injected DLL using **MinHook** detours on `CreateMove`, `LevelInit`, and protobuf serialization paths to mutate input-history and view-angle data before wire transmission.
- **Kernel drivers** — server-flag and rank spoofing (Windows kernel).
- **Injector** — multi-method user-mode and kernel injection.
- **Offset pipeline** — depot-aware offset manifests with runtime GitHub offset fetching.
- **Documentation** — VMProtect mechanics, demo analysis; Python demo parsing; Lua reverse-engineering notes.

Built with CMake (C/C++). Intended for anti-cheat research, reverse-engineering education, and bug-bounty-style VAC Live study—not live competitive use.

Complements CS:GO P2C forensics via [[csgo-p2c-dumper]], VAC architecture notes via [[como-funciona-vac]] and [[cs2-anticheat]], kernel VAC bypass research via [[vac-bypass-kernel]], VMProtect study surfaces such as [[vmprotect]], and other CS2 internal samples such as [[cs2internal]] and [[cs2-cheat-base]].

## Links

- Repo: https://github.com/ccsimplyspolit/CS2-P2C-TEMPLATES

## Related

[[csgo-p2c-dumper]] · [[como-funciona-vac]] · [[cs2-anticheat]] · [[vac-bypass-kernel]] · [[vac-bypass]] · [[vmprotect]] · [[cs2internal]] · [[cs2-cheat-base]] · [[cs2-internal-sdk]] · [[cs2-offsets]] · [[ntminhook]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
