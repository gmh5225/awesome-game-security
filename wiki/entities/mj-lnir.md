---
title: Mjölnir (Mj-lnir)
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/nulli83__Mj-lnir.md
updated: 2026-08-07
confidence: medium
---

# Mjölnir (Mj-lnir)

Windows-focused anti-cheat stack that **separates on-machine detection from studio-controlled enforcement**. The client pairs a C++ security core with a Rust agent to audit the game process and gather evidence—module and overlay scanning, debugger detection, memory integrity, hook analysis, injection heuristics, and self-protection—then forwards telemetry over HMAC-secured IPC and optional HTTPS ingest. (source: wiki/sources/descriptions/nulli83__Mj-lnir.md)

A self-hosted Rust server acts as the studio control plane: session scoring, policy, kick/ban decisions, and webhooks into backend ban systems. An optional Tauri dashboard provides local visibility. **Observe-only mode** is the default so operators can investigate before enabling enforcement. Aimed at game studios building or operating their own anti-cheat and incident-response workflows rather than relying on a third-party cloud service—adjacent to OSS skeletons such as [[sentinelac]], server-authoritative stacks such as [[certael]], and evidence-review platforms such as [[ponytail-risk]].

## Links

- Repo: https://github.com/nulli83/Mj-lnir

## Related

[[overviews/anti-cheat]] · [[sentinelac]] · [[certael]] · [[ponytail-risk]] · [[anticheat-poc]] · [[darken-anticheat]]
