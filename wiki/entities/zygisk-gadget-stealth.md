---
title: zygisk-gadget-stealth
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/hex91__zygisk-gadget-stealth.md
updated: 2026-11-06
confidence: medium
---

# zygisk-gadget-stealth

**Zygisk** root module that **injects the official Frida Gadget** into selected Android apps **without repackaging APKs** and **without ptrace attach**, for long-running, per-app dynamic instrumentation on rooted devices (typical [[magisk]] / Zygisk-compatible stacks). Native code implements memory/path hygiene (e.g. remapping gadget-backed regions in process maps, neutral library and data paths), optional thread-name masking, quieter logging, plus shell install scripts, a **Web management UI**, JS hook examples, and **PC-side Python helpers**. Configuration is plain key-value text (script vs listen modes, per-app whitelists, injection delay, anti-fingerprinting toggles, verification commands). The project pins gadget and tooling to a **specific Frida release** so the host `frida` client matches the injected gadget on **arm64** and **32-bit ARM**. (source: wiki/sources/descriptions/hex91__zygisk-gadget-stealth.md)

Compared with generic gadget injectors such as [[zygisk-frida]] and Rusda-oriented stacks such as [[ksurusda]], this repo foregrounds **reducing obvious Frida/gadget artifacts** in process-visible state. Pair with [[frida]], [[zygisk]], and [[antifrida]] / [[frida-detection]] when reasoning about defender probes vs stealth claims.

## Links

- Repo: https://github.com/hex91/zygisk-gadget-stealth (Zygisk module for per-app Frida Gadget injection with configurable stealth and WebUI status)

## Related

[[frida]] · [[zygisk]] · [[magisk]] · [[zygisk-frida]] · [[ksurusda]] · [[frida-magisk]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[antifrida]] · [[frida-detection]]
