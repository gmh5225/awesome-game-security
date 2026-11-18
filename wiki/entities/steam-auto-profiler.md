---
title: Steam Auto-Profiler
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Renaus-FI__steam-auto-profiler.md
updated: 2026-11-18
confidence: medium
---

# Steam Auto-Profiler

**Steam Auto-Profiler** (Renaus-FI/steam-auto-profiler) is a **Bash** pre-launch orchestrator for **Steam on Linux**, aimed at **Wayland** desktops (KDE, GNOME). It inspects the local Steam install, library manifests, and installed game directories to assign each title one of four **launch profiles**: competitive anti-cheat, native FSR, legacy upscaler, or a standard low-latency default. Classification mixes known competitive **AppIDs** with **filesystem signatures** for runtimes such as [[easy-anti-cheat]], [[battleye]], and related anti-cheat libraries. Applied defaults include disabling optional upscaler bridges when anti-cheat is present and enabling an optional online network profile. Companion tooling syncs Steam **launch options** in `localconfig`, wraps the game command for orchestrated launches, and can apply session-level network tuning **without** bundling overlays or injection libraries. The project targets Linux gamers and security-minded users who want predictable **Proton** behavior around anti-cheat and upscaler stacks, and doubles as a reference for **heuristic anti-cheat presence checks** driving launch policy on open platforms—not bypass or cheat tooling. (source: wiki/sources/descriptions/Renaus-FI__steam-auto-profiler.md)

## Profile model

- **Competitive anti-cheat** — EAC/BattlEye-style signatures or curated competitive AppIDs; conservative graphics and upscaler defaults.
- **Native FSR** / **legacy upscaler** — FSR-capable or older upscaler paths when no AC constraints apply.
- **Low-latency default** — baseline Wayland/Proton launch when no special stack is detected.

## Research framing

Defensive **launch-policy automation**: offline inventory + signature heuristics → safe Proton/Wayland defaults. Complements library-planning tools such as [[rigcheck]] and compatibility catalogs such as [[are-we-anti-cheat-yet]]; contrast with Windows rendering-stack triage such as [[game-api-detector]]. (source: wiki/sources/descriptions/Renaus-FI__steam-auto-profiler.md)

## Links

- Repo: https://github.com/Renaus-FI/steam-auto-profiler [Bash tooling that classifies Steam AppIDs (including competitive anti-cheat titles) and applies safe Proton/Wayland launch profiles on Linux]

## Related

[[rigcheck]] · [[are-we-anti-cheat-yet]] · [[game-api-detector]] · [[easy-anti-cheat]] · [[battleye]] · [[overviews/anti-cheat]]