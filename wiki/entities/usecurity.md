---
title: USecurity
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/ls9512__USecurity.md
updated: 2026-07-31
confidence: medium
---

# USecurity

Unity security component for runtime client data protection. Encrypts commonly used scalar and structured data types at runtime, wraps `PlayerPrefs` persistence with storage encryption, and exposes a quick-call API for encrypt/decrypt using common algorithms. Aimed at anti-cheat engineers and defensive researchers building Unity client hardening in the README `Game Engine Protection:Unity` lane—raising the cost of trivial memory scans and plaintext preference tampering opposite [[il2cpp]] / Mono RE tooling. (source: wiki/sources/descriptions/ls9512__USecurity.md)

Complements other Unity-side protection samples such as [[free-rasp-unity-poc]] (mobile RASP) and [[com-sipvlib-anticheat]] (integrity heuristics) rather than kernel or server-authoritative stacks like [[certael]].

## Links

- Repo: https://github.com/ls9512/USecurity

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[il2cpp]] · [[free-rasp-unity-poc]] · [[com-sipvlib-anticheat]]
