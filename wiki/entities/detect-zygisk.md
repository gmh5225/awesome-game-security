---
title: DetectZygisk
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/apkunpacker__DetectZygisk.md
updated: 2026-08-18
confidence: medium
---

# DetectZygisk

Android proof-of-concept for identifying **Zygisk-style process injection**. Detection logic is implemented in C++ and JNI: fork a child process, attach with `ptrace`, and read `PTRACE_GETEVENTMSG` artifacts to infer Zygisk specialization behavior. Ships a sample APK and runtime logs demonstrating detection across several Zygisk forks while baseline implementations may differ. Primarily useful for mobile anti-cheat and root-detection researchers studying runtime integrity checks against early zygote injection. (source: wiki/sources/descriptions/apkunpacker__DetectZygisk.md)

Sits in the Anti Cheat Zygisk / instrumentation-detection lane beside the apkunpacker detector collection [[magisk-detection]] (archive of root/Magisk POC APKs including Zygisk checks), package-presence probes such as [[root-app-detector]], and native Frida instrumentation checks such as [[detect-frida]]—opposite early-load modding modules documented under [[zygisk]] (DEX dump, ImGui menus, Frida gadget injectors).

## Links

- Repo: https://github.com/apkunpacker/DetectZygisk

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[zygisk]] · [[magisk-detection]] · [[root-app-detector]] · [[detect-frida]] · [[detection]] · [[magisk]]
