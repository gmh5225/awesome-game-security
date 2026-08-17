---
title: eac-leak
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/chaeyk__eac-leak.md
updated: 2026-08-17
confidence: medium
---

# eac-leak

Leaked **Easy Anti-Cheat server** implementation (chaeyk; C++; explore anticheat:eac) with **Epic Online Services (EOS)** SDK integration for anti-cheat session management. The codebase includes a deployable server component that handles EOS-backed anti-cheat sessions; operators must replace the bundled EOS application ID before deployment. Useful for researchers studying EAC **server-side architecture** and the game-server ↔ EAC cloud validation protocol—complementing client/driver reversed-source archives such as [[eac-easyanticheat-src-1]] and EOS SDK study bundles such as [[eac]]. (source: wiki/sources/descriptions/chaeyk__eac-leak.md)

## Links

- Repo: https://github.com/chaeyk/eac-leak

## Related

[[easy-anti-cheat]] · [[eac]] · [[eac-easyanticheat-src-1]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
