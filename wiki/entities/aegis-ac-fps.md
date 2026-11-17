---
title: Aegis AC (FPS)
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/phugiadang12__aegis-ac.md
  - wiki/sources/README-categories.md
updated: 2026-11-17
confidence: medium
---

# Aegis AC (FPS)

**Aegis AC** (phugiadang12/aegis-ac; not [[aegis-ac]] Paper Minecraft AegisAC) is a **server-side behavioural anti-cheat stack for multiplayer FPS** games. It scores players from **telemetry the game server already emits**—no client drivers or cross-process memory reads. (source: wiki/sources/descriptions/phugiadang12__aegis-ac.md)

README category: Anti Cheat / Open Source Anti Cheat System.

Repository: [phugiadang12/aegis-ac](https://github.com/phugiadang12/aegis-ac).

## Architecture

Three Python packages—**collector**, **detection**, and **soc-agent**—plus a **TypeScript/React** operations dashboard. A **FastAPI** collector ingests **UDP and HTTP JSONL** events into **SQLite**. An explainable rule engine scores turn rate, hit rate, headshot rate, and **honeypot interactions** against synthetic cheat simulators. A **Claude-powered SOC analyst** triages alerts into case reports for human approval before **delayed ban waves** and Discord notifications. (source: wiki/sources/descriptions/phugiadang12__aegis-ac.md)

## Detection signals

Rule scores derive from server-emitted combat/movement telemetry only—no kernel driver or client memory probe. **Honeypot** entities and synthetic cheat simulators supply red-team labels without distributing real cheat binaries. Enforcement is staged: analyst-approved case reports precede batched ban waves, aligned with human-in-the-loop ops in [[detector-operations]]. (source: wiki/sources/descriptions/phugiadang12__aegis-ac.md)

## Research framing

Privacy-preserving server-only detection, red-team simulation without shipping real cheats, and an end-to-end pipeline from ingestion through enforcement—pairs [[detector-operations]] staged sanction patterns and [[ai-aimbot-detection]] server-telemetry ML lanes; compare offline log pipelines such as [[detect-fps-hackers]] and prototype review queues such as [[aimguard]].

## Related

[[aegis-ac]] (Minecraft) · [[aegis-ac-cs2]] · [[aimguard]] · [[detect-fps-hackers]] · [[anti-cheat]] · [[overviews/anti-cheat]]