---
title: nbridge_fix
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/Puureastar__nbridge_fix.md
updated: 2026-11-08
confidence: medium
---

# nbridge_fix

**Magisk module** (Magisk 26+, Android 10+ with APEX-based ART) that lets **ijiami-hardened** apps launch on a real rooted phone instead of self-terminating after a false **emulator / native-bridge** environment detection. At boot the module’s `service.sh` uses **busybox** `mount`, **nsenter**, zygote mount-namespace entry, **`--make-rprivate`** propagation control, and SELinux labeling on the bind source to overlay a **zero-byte placeholder** on ART’s **`libnativebridge.so`** inside the **zygote mount namespace**. The packer’s **mmap size check** on that path then fails while the real library stays intact in the **init** namespace. No APK patching, root hiding, or in-process Frida hooks—only namespace-scoped filesystem deception aimed at commercial Chinese packer **inline-svc** environment probes that outlast ordinary root-hide or dynamic instrumentation. (source: wiki/sources/descriptions/Puureastar__nbridge_fix.md)

Complements static unpack via [[kavanoz]] and packer ID via [[apkid]]; sits beside [[magisk]] module workflows and emulator-detection research lanes ([[anti-emulator]], [[mobile-anti-cheat]]) when runtime launch is blocked before dynamic analysis.

## Links

- Repo: https://github.com/puureastar/nbridge_fix

## Related

[[magisk]] · [[kavanoz]] · [[apkid]] · [[anti-emulator]] · [[mobile-anti-cheat]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
