---
title: frida-magisk
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/xjoker__frida-magisk.md
updated: 2026-10-17
confidence: medium
---

# frida-magisk

**Magisk** and **KernelSU** flashable module that bundles **official Frida** Android `frida-server` and **Gadget** binaries with a custom **Zygisk**-based native injector. Build tooling downloads upstream Frida assets, **SHA-256-verifies** them, compiles the injector for arm64, arm32, x86, and x86_64, and ships **CI-driven** release ZIPs. (source: wiki/sources/descriptions/xjoker__frida-magisk.md)

Runtime modes include **server-only**, **hybrid** (server + gadget), and **Gadget-only** in-process injection with **per-app package targets**. On-device control uses shell scripts plus an optional **KernelSU WebUI** (JavaScript). An optional **antidetect** flavor renames bundled assets for environments that fingerprint standard Frida layouts. Primary implementation: C++ injector, shell module logic, WebUI JS. Targets Android reverse engineers and game security researchers who need reliable Frida deployment without manual server setup on each device. (source: wiki/sources/descriptions/xjoker__frida-magisk.md)

Contrasts with KernelSU-only supervisors such as [[frida-rs]] (stock server lifecycle) and stealth repacks such as [[magisk-hluda]] / [[florida-zygisk]] — frida-magisk ships **verified upstream** Frida binaries plus Zygisk gadget injection in one module.

## Links

- Repo: https://github.com/xjoker/frida-magisk [Magisk/KernelSU module bundling official Frida server and Gadget plus a Zygisk injector, with scripted builds and on-device WebUI]

## Related

[[frida]] · [[magisk]] · [[kernelsu]] · [[zygisk]] · [[zygisk-frida]] · [[frida-rs]] · [[magisk-hluda]] · [[florida-zygisk]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
