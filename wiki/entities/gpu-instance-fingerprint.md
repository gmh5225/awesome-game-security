---
title: GPU Instance Fingerprint
kind: entity
topics: [anti-cheat, game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/divagr18__gpu-instance-fingerprint.md
updated: 2026-11-02
confidence: medium
---

# GPU Instance Fingerprint

**gpu-instance-fingerprint** (divagr18/gpu-instance-fingerprint) is a **research codebase** for telling apart physically identical **NVIDIA GPUs** using only the **numerical results of CUDA work**, without reading serial numbers or relying on timers. (source: wiki/sources/descriptions/divagr18__gpu-instance-fingerprint.md)

## Probes and analysis

- **Active CuPy probe** — fingerprints chips from hardware-decided **atomic contention order** in custom CUDA kernels.
- **Passive PyTorch channel** — `index_add` output can leak the same identity from ordinary framework ops without a dedicated probe kernel.
- **CPU-side Python analysis** — bundled measurement data reproduces separation, forgery, reboot stability, and defense experiments.

Stack: **Python** with CUDA via **CuPy**, optional **PyTorch** probes, plus **Docker** and remote **SSH** helpers for collecting fingerprints across hosts.

## Research audience

Security and anti-cheat researchers studying **GPU instance binding**, **cloud-tenant identification**, **side channels in shared GPU fleets**, and mitigations such as **deterministic PyTorch modes** versus blocking custom kernels.

## Links

- Repo: https://github.com/divagr18/gpu-instance-fingerprint

## Related

[[odzhan-hwid]] · [[filtertap]] · [[concepts/hwid-spoofing]] · [[gpu-inspector]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
