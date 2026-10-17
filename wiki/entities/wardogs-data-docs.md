---
title: Wardogs Data Docs
kind: entity
topics: [game-engine, reverse-engineering, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Kiyogitpy__wardogs-data-docs.md
updated: 2026-10-17
confidence: medium
---

# Wardogs Data Docs

**Defensive-research reference corpus** for the Wardogs multiplayer shooter on **Unreal Engine 5.7** (Kiyogitpy). The repo pairs a **Jekyll** static documentation site with large **cooked data exports**: JSON datasets for gameplay tags, weapons, projectiles, vehicles, player input, rewards, and related curves under a mirrored content tree. Markdown design notes cover combat and damage pipelines, gameplay effects, AI, progression, and feature-level behavior including **aim assist**, **teamkill tracking**, and **account watermarking**. Python helpers generate or link tables for infantry damage, vehicles, and zone rewards; small JavaScript assets support browsing. The collection also ships **UEDumper**-derived C++ SDK output and mappings, cross-linked with the prose docs under a **responsible disclosure** framing. Listed under cheat / Defensive-research Wardogs reference. (source: wiki/sources/descriptions/Kiyogitpy__wardogs-data-docs.md)

Authoritative **ground-truth mechanics reference** for analysts studying balance, reverse engineering, and game-security or anti-cheat design—not a cheat or bypass tool. Complements generic UE dumpers such as [[zircon-ue-dumper]] and [[uedumper]] with title-specific exported config and design documentation.

## Audience

Researchers and analysts who need structured Wardogs mechanics data for RE, balance study, and defensive integrity work without relying on live client extraction alone. (source: wiki/sources/descriptions/Kiyogitpy__wardogs-data-docs.md)

## Links

- Repo: https://github.com/Kiyogitpy/wardogs-data-docs

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[unreal-object-model]] · [[zircon-ue-dumper]] · [[uedumper]] · [[corner-culling]]
