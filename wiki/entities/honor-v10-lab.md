---
title: Honor V10 Lab
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/yingyangdao__honor-v10-lab.md
  - wiki/sources/README-categories.md
updated: 2026-10-24
confidence: medium
---

# Honor V10 Lab

**Honor V10 Lab** (yingyangdao/honor-v10-lab) documents turning a locked **Honor V10 (BKL-AL20) on EMUI 9** into a rooted, always-connected Android lab for development, debugging, and traffic analysis. The write-up captures the full unlock and root path—including **software test point (SWTP) bootloader unlock** without an official Huawei code—and how to work around vendor-specific limits such as rigid **SELinux** and a broken **`frida-server`** workflow on Kirin/Huawei builds. (source: wiki/sources/descriptions/yingyangdao__honor-v10-lab.md)

README category: Cheat / Android Root.

## Lab stack

- **Root / modules:** Magisk 20.1, EdXposed, optional root-hide and ad-blocking modules.
- **Dynamic instrumentation:** **Frida Gadget** injection when attach-mode `frida-server` fails under strict Huawei SELinux (documented pitfall notes).
- **Network analysis:** system CA trust for MITM, Termux **tcpdump** for on-device capture.
- **Host automation:** reusable PowerShell and shell scripts plus a **harness skill** for day-to-day device control.

(source: wiki/sources/descriptions/yingyangdao__honor-v10-lab.md)

## Supporting material

Step-by-step guides, documented pitfalls, **HwOUC** reverse-engineering notes, and automation aimed at mobile security researchers and reverse engineers who need a reproducible Honor/Huawei Kirin test bed for hooking, packet capture, and app behavior analysis—including **game clients** and anti-tamper checks. (source: wiki/sources/descriptions/yingyangdao__honor-v10-lab.md)

## Links

- Repo: https://github.com/yingyangdao/honor-v10-lab

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[kpa-root]] · [[frida]] · [[magisk]] · [[mobile-trust-boundaries]] · [[unity-apk-reverse]]
