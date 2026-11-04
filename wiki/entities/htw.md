---
title: Hack The Web
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Entkenntnis__htw.md
  - wiki/sources/README-categories.md
updated: 2026-11-04
confidence: medium
---

# htw

**Hack The Web** ([Entkenntnis/htw](https://github.com/Entkenntnis/htw)) is the self-hostable source for a browser-based puzzle platform: players work through **web security and hacking-themed challenges** inside an interactive adventure. Operators can run a full web-hacking training site locally or on their own infrastructure. (source: wiki/sources/descriptions/Entkenntnis__htw.md)

## Architecture

| Layer | Role |
|-------|------|
| **Node.js + Express + EJS** | Server-rendered web app and adventure shell |
| **Sequelize** | Database access for progress and content |
| **JWT + cookie sessions** | Authentication alongside **CSRF protection** |
| **Socket.io** | Real-time features during play |
| **In-browser challenge library** | Bundled scripts, quizzes, maps, and editor tooling |
| **Operator secrets file** | Spoiler answers kept separate; populated after solving tasks |

## Audience

Educators, **CTF enthusiasts**, and security learners studying or deploying hands-on **web offensive** practice—not live game anti-cheat or kernel security. Pair with structured curricula such as [[re-dojo]] and [[intro-to-gamehacking]] when routing learners from browser labs to native game RE.

## Links

- Repo: https://github.com/Entkenntnis/htw

## Related

[[re-dojo]] · [[intro-to-gamehacking]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
