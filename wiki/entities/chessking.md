---
title: Chess King
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/web-coder-lab__chessking.md
updated: 2026-08-14
confidence: medium
---

# Chess King

Full-stack **multiplayer chess platform** (web-coder-lab) with ranked and casual matchmaking, real-time WebSocket gameplay, and an integrated virtual economy (wallets, shops, inventory, gifts). The **Rust** backend (Axum, SQLx, SQLite) implements a layered **server-side anti-cheat** system: risk scoring, ban escalation, device fingerprinting, match integrity checks, IP reputation tracking, and chess-themed CAPTCHA step-up authentication. A React/Vite frontend serves players; an admin security dashboard monitors risk tiers, security events, and pending review queues. The codebase also documents application-level firewalling, rate limiting, JWT authentication, probe blocking, and structured security logging alongside **shakmaty** for authoritative move validation. Serves as an educational reference for designing, implementing, and auditing anti-cheat and account-abuse defenses in online competitive games. (source: wiki/sources/descriptions/web-coder-lab__chessking.md)

## Anti-cheat surface

- **Risk scoring** with tiered ban escalation
- **Device fingerprinting** and **IP reputation** for account-abuse signals
- **Match integrity** via server-side chess engine validation (shakmaty)
- **Chess-themed CAPTCHA** step-up under elevated risk
- **Admin dashboard** for security events and manual review queues

Complements other educational server-authoritative stacks such as [[certael]] and beginner Windows samples such as [[basic-anti-cheat]] — application-layer defenses rather than kernel AC.

## Links

- Repo: https://github.com/web-coder-lab/chessking

## Related

[[overviews/anti-cheat]] · [[certael]] · [[basic-anti-cheat]] · [[ff3mmo]] · [[ponytail-risk]]
