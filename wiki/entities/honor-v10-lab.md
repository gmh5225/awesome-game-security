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

**Honor V10 Lab** (yingyangdao/honor-v10-lab) documents turning a locked **Honor V10 (BKL-AL20) on EMUI 9** into a rooted, always-connected Android lab for development, debugging, and traffic analysis. The write-up covers software test point (SWTP) bootloader unlock without an official code, Magisk 20.1, EdXposed, and a **Frida Gadget** workflow that works around Huawei-specific SELinux limits where `frida-server` fails. (source: wiki/sources/descriptions/yingyangdao__honor-v10-lab.md)

README category: Cheat / Android Root.

## Lab stack

System CA trust for MITM, Termux **tcpdump**, optional root-hide and ad-blocking modules, HwOUC reverse-engineering notes, and reusable PowerShell/shell automation plus a harness skill for day-to-day device control. Aimed at mobile security researchers and reverse engineers who need a reproducible Honor/Huawei Kirin test bed for hooking, packet capture, and app behavior analysis—including game clients and anti-tamper checks.

## Links

- Repo: https://github.com/yingyangdao/honor-v10-lab

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[kpa-root]] · [[frida]] · [[magisk]] · [[mobile-trust-boundaries]] · [[unity-apk-reverse]]
