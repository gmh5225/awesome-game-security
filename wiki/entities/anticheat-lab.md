---
title: Anticheat Lab (Ogonx)
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Ogonx__anticheat-lab.md
  - wiki/sources/README-categories.md
updated: 2026-10-30
confidence: medium
---

# Anticheat Lab (Ogonx)

**Anticheat-lab** (Ogonx/anticheat-lab) is a structured **six-month self-study curriculum** for game anti-cheat: alternating attack and defense on the author’s own deliberately vulnerable game builds and practice binaries rather than live commercial titles. Topics span x64 assembly and C++ memory layout, reverse-engineering tooling, a cheatable multiplayer prototype, server authority, statistical detection, and client-side checks. Early exercises use C++ samples, Compiler Explorer disassembly comparisons, and Visual Studio debugging with stack/register tracing on Windows x64 calling conventions, shadow space, and stack frames. Progress lives in a devlog with monthly exercise folders and write-ups—aimed at developers and security learners who want **VM-only**, ethical low-level game-security foundations. (source: wiki/sources/descriptions/Ogonx__anticheat-lab.md)

## Curriculum arc

- **Foundations:** x64 assembly, C++ memory layout, Windows x64 ABI (shadow space, stack frames).
- **RE tooling:** static/dynamic analysis workflows on practice binaries before touching the game prototype.
- **Prototype loop:** deliberately cheatable multiplayer build → server authority → statistical detection → client-side checks, revisited from both attacker and defender perspectives.

## Early tooling

- **Compiler Explorer:** compare unoptimized vs optimized disassembly for the same C++ samples.
- **Visual Studio debugger:** stack and register tracing while stepping through calling-convention exercises.

## Catalog

Listed under README **Anti Cheat** beside educational guides and behavioral research labs such as [[apex-anticheat-lab]] and [[minecraft-anticheat-docs]]. (source: wiki/sources/README-categories.md)

## Links

- Repo: https://github.com/Ogonx/anticheat-lab

## Related

[[apex-anticheat-lab]] · [[minecraft-anticheat-docs]] · [[intro-to-gamehacking]] · [[re4f]] · [[detector-operations]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
