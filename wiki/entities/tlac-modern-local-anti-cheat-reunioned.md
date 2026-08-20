---
title: TLAC (Modern Local Anti-Cheat Reunioned)
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/TuncorReUnion__TLAC-MODERN-LOCAL-ANTI-CHEAT-REUNIONED.md
updated: 2026-08-20
confidence: medium
---

# TLAC (Modern Local Anti-Cheat Reunioned)

**TLAC** (TuncorReUnion) — lightweight, MIT-licensed **open-source local anti-cheat for Linux** that keeps enforcement on-device without cloud dependency. Written mainly in **Rust**, with **C** for optional eBPF probes and a kernel module, plus **Python** scripts to train an **ONNX** behavioral anomaly model. Core capabilities include wildcard memory signature scanning, SHA256 self-integrity checks, hardware ID bans, and a **Tokio**-based local IPC server. Optional eBPF tracepoints watch suspicious `open`, `exec`, `ptrace`, and `clone` activity; behavioral anomaly detection aims to catch unknown cheats. Targets Linux game security use cases, including **Steam Deck**, for developers and operators who want a transparent anti-cheat stack. (source: wiki/sources/descriptions/TuncorReUnion__TLAC-MODERN-LOCAL-ANTI-CHEAT-REUNIONED.md)

Sits in the native Linux open-source AC lane beside GNU/Linux Proton/Wine compatibility references such as [[aclist-github-io]] and upstream [[proton]], and complements eBPF security telemetry such as [[tracee]] and [[rootkit-detection-ebpf-time-trace]].

## Links

- Repo: https://github.com/TuncorReUnion/TLAC-MODERN-LOCAL-ANTI-CHEAT-REUNIONED [Linux user-space anti-cheat with eBPF, signature scanning, HWID bans, and AI anomaly detection]

## Related

[[proton]] · [[aclist-github-io]] · [[tracee]] · [[rootkit-detection-ebpf-time-trace]] · [[fastdbg]] · [[rebirth-guard]] · [[anti-cheat]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
