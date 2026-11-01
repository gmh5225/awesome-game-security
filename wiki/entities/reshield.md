---
title: ReShield
kind: entity
topics: [reverse-engineering, game-hacking, game-engine, mobile-security]
sources:
  - wiki/sources/descriptions/swimchicken777__reshield.md
  - wiki/sources/README-categories.md
updated: 2026-11-01
confidence: medium
---

# ReShield

**ReShield** (swimchicken777; pre-release) is a **security scanner for shipped game and application builds**. It inspects packaged artifacts, explains in plain language where logic and assets can be copied or recovered, and suggests fixes—aimed at **game developers** and release engineers hardening clients before players or attackers (including **AI-assisted RE** workflows) extract combat formulas, secrets, or other sensitive client-side logic. (source: wiki/sources/descriptions/swimchicken777__reshield.md)

## Implementation

- **Python 3.11+** standalone **CLI** and **agent skill** for Claude Code and Codex.
- **Platform adapters:** Unity (Mono and IL2CPP), Unreal, Godot, web/Electron, Android, iOS, .NET, and native **PE**, **ELF**, and **Mach-O** binaries.

## Detection and reporting

Findings include readable scripts and metadata, shipped **source maps**, **debug symbols**, leaked API and private keys, and related misconfigurations. Exposure is scored on an **L0–L5** protection scale. Reports can export **SARIF** tagged with **OWASP MASWE** for CI pipelines. (source: wiki/sources/descriptions/swimchicken777__reshield.md)

## Positioning

Defensive **pre-release audit** beside author-side hardening such as [[anti-reverse-engineer-anything]] and offensive agent RE stacks cataloged in [[awesome-ai-reverse-engineering]]. Complements [[static-runtime-evidence]] by scoring what actually ships in build artifacts rather than runtime-only observation.

## Links

- Repo: https://github.com/swimchicken777/reshield

## Related

[[anti-reverse-engineer-anything]] · [[reverify]] · [[awesome-ai-reverse-engineering]] · [[binary-evidence]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/game-engine]]
