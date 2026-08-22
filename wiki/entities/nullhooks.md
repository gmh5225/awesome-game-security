---
title: NullHooks
kind: entity
topics: [game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/NullHooks__NullHooks.md
updated: 2026-08-22
confidence: medium
---

# NullHooks

Learning-focused **internal CS:GO cheat** (NullHooks) implemented in **C++** with a **modular codebase**: gameplay features, **configuration presets**, and supporting utilities commonly used in internal cheat development. The repository documents references and contribution notes. It is marked **inactive** but remains useful for study. Primary use case: educational exploration of **game-hacking architecture** and implementation techniques—not a maintained production cheat. (source: wiki/sources/descriptions/NullHooks__NullHooks.md)

README tags it `[Internal]`. Pair with other Source 1 internal scaffolds when comparing how feature modules, config layers, and hook surfaces are organized across educational codebases.

## Architecture highlights

| Component | Role |
|-----------|------|
| Modular layout | Separates gameplay features, utilities, and shared internal-cheat patterns |
| Configuration presets | Saved toggles/settings typical of internal cheat menus |
| Gameplay features | In-process CS:GO feature modules for architecture study |
| References / notes | Documented learning resources and contribution guidance |

See [[csgo-cheat-base]] and [[csgo-internal-base]] for comparable Source 1 internal scaffolds in the same lane.

## Links

- Repo: https://github.com/NullHooks/NullHooks

## Related

[[overviews/game-hacking]] · [[csgo-cheat-base]] · [[csgo-internal-base]] · [[csgosimple]] · [[solace-csgo]] · [[osiris]] · [[intro-to-gamehacking]]
