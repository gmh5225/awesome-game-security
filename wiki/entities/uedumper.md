---
title: UEDumper
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Spuckwaffel__UEDumper.md
updated: 2026-08-20
confidence: medium
---

# UEDumper

**All-in-one Unreal Engine dumper and live memory editor** (Spuckwaffel; C++). Supports UE **4.19 through 5.3.0** with SDK generation, structure dumping, and runtime browsing utilities. ImGui-based UI with components for object management, type generation, and engine-version-specific handling—useful for Unreal game reverse engineering and game-security research workflows. Listed under cheat / SDK Dump for UE 4.19–5.2. (source: wiki/sources/descriptions/Spuckwaffel__UEDumper.md)

Sits in the Unreal SDK-generation lane beside inject dumpers (Dumper-7 / [[re-ue4ss]]), runtime reflection generators such as [[ue4genny]], version-targeted UE4 dumpers such as [[shh0yauedumper]], the separately maintained [[ezfndev-uedumper]] (EZFNDEV; injection-based SDK output with automated offset finding; same repo name), external pattern-scan dumpers such as [[unrealdumper-4-25]], and live explorers—all feeding the same [[unreal-object-model]] research surface.

## Links

- Repo: https://github.com/Spuckwaffel/UEDumper

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[unreal-object-model]] · [[ezfndev-uedumper]] · [[shh0yauedumper]] · [[ue4genny]] · [[unrealdumper-4-25]] · [[re-ue4ss]] · [[ts-ue4dumper]] · [[patternsleuth]]
