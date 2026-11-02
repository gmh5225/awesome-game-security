---
title: owlbear
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Brad-Edwards__owlbear.md
updated: 2026-11-02
confidence: medium
---

# owlbear

**owlbear** (Brad-Edwards) is an **educational anti-cheat and endpoint-detection prototype** for **ARM64 Linux** that combines a loadable **kernel module**, **eBPF** programs, and a **userspace daemon** to monitor and protect a target game process. The stack uses kernel **kprobes**, **eBPF LSM hooks** that deny dangerous operations such as **ptrace** and sensitive memory maps, and a daemon with a policy engine, signature scanning, **HMAC-SHA256** code-integrity checks, debugger and **LD_PRELOAD** detection, and process-tree correlation. It ships with a small **ncurses** game target, sample cheat programs to exercise detections, end-to-end verification scripts, optional cloud telemetry, and **Terraform** for Graviton-based dev environments. Primary languages are **C** (kernel, eBPF, daemon, cheats) and **Python** (control scripts). Aimed at researchers learning kernel-level game security—not production deployment. (source: wiki/sources/descriptions/Brad-Edwards__owlbear.md)

Sits in the native Linux open-source AC lane beside [[linux-anticheat]], [[vigil]], and [[tlac-modern-local-anti-cheat-reunioned]], with bundled attack samples for validation rather than live bypass tooling.

## Architecture

1. **Kernel module** (C) — loadable foundation; **kprobes** for instrumentation.
2. **eBPF LSM** — deny ptrace, sensitive **mmap**, and related high-risk kernel paths.
3. **Userspace daemon** (C) — policy engine, signature scan, HMAC-SHA256 integrity, debugger/LD_PRELOAD checks, process-tree correlation.
4. **Lab target** — ncurses game plus external-memory-style sample cheats and verification scripts.

## Stack

**ARM64 Linux** (Graviton-friendly); optional cloud telemetry; Terraform dev environments.

## Status

Educational prototype—research and teaching reference, not production-ready enforcement.

## Links

- Repo: https://github.com/Brad-Edwards/owlbear [Educational ARM64 Linux anti-cheat prototype: kernel module, eBPF LSM hooks, userspace daemon with policy/signature scanning, ncurses game target, and bundled external-memory cheat attack programs for verification]

## Related

[[linux-anticheat]] · [[vigil]] · [[tlac-modern-local-anti-cheat-reunioned]] · [[ac-compat-research]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
