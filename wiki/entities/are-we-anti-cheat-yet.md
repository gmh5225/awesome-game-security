---
title: Are We Anti-Cheat Yet
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/AreWeAntiCheatYet__AreWeAntiCheatYet.md
updated: 2026-09-15
confidence: medium
---

# Are We Anti-Cheat Yet

**Are We Anti-Cheat Yet** is a community-maintained website that tracks which PC games support anti-cheat on **GNU/Linux**, **Proton**, and **Wine**. Game data lives in a **JSON catalog** and is published as a statically generated **Next.js** site with searchable table and card views, dedicated game pages, status breakdowns, update timelines, and an **RSS** feed. Each title is classified by Linux anti-cheat readiness (**supported**, **running**, **planned**, **broken**, or **denied**) and lists deployed anti-cheat systems such as **Easy Anti-Cheat** and **BattlEye**. Built with **TypeScript**, **React**, and **Mantine**, it gives Linux gamers and **Steam Deck** users a transparent reference for online play compatibility and developer commitments, without promoting bypass techniques. (source: wiki/sources/descriptions/AreWeAntiCheatYet__AreWeAntiCheatYet.md)

Complements manually verified references such as [[aclist-github-io]] and macOS CrossOver patchers such as [[crossover-patcher]] in the platform-support lane; relates to official Valve [[proton]] compatibility work. Upstream architecture feasibility research such as [[ac-compat-research]] (vendor-agnostic Linux kernel AC hosting study; LSM/signing/isolation/ABI; non-virtualized design dossier) addresses why certain titles remain blocked beyond Proton/Wine runtime gaps. (source: wiki/sources/descriptions/IZxMD__ac-compat-research.md)

## Links

- Site: https://areweanticheatyet.com
- Repo: https://github.com/AreWeAntiCheatYet/AreWeAntiCheatYet

## Related

[[aclist-github-io]] · [[ac-compat-research]] · [[crossover-patcher]] · [[proton]] · [[concepts/easy-anti-cheat]] · [[concepts/battleye]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
