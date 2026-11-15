---
title: mibox3s-utgard-lpe
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/wuying2021__mibox3s-utgard-lpe.md
updated: 2026-11-15
confidence: medium
---

# mibox3s-utgard-lpe

**Documented local privilege escalation chain** (wuying2021) that elevates an unprivileged **adb shell** on **Xiaomi Mi Box 3S** (Amlogic, **Linux 3.14**) to **root** with **SELinux permissive**. The exploit abuses the **Mali-400 Utgard** GPU driver’s **unvalidated external memory binding** to obtain **arbitrary physical memory writes** through the GPU, patches unused **`sys_call_table`** slots to redirect syscalls into attacker-controlled or resolved kernel helpers, disables SELinux enforcement, and triggers a **coredump handler** to run a root helper script. Implementation is mainly **C** with **aarch64** and **armv7** cross-compiled utilities and shell automation; notes cover **cache coherency**, **ion workarounds**, and **kernel symbol discovery** on locked-down firmware. The chain avoids ROP, heap spray, and a separate CVE—aimed at Android kernel exploitation and **GPU-assisted LPE** on legacy Amlogic set-top boxes. (source: wiki/sources/descriptions/wuying2021__mibox3s-utgard-lpe.md)

Sits beside modern **Mali GPU kernel** privesc research such as [[pixel-gpu-exploit]] and structured Android kernel training [[android-kernel-exploitation]], and contrasts with **io_uring**-focused PoCs such as [[bad-io-uring]].

## Links

- Repo: https://github.com/wuying2021/mibox3s-utgard-lpe [Mali-400 GPU write-back adb→root on Mi Box 3S; Utgard / kernel 3.14]

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[pixel-gpu-exploit]] · [[bad-io-uring]] · [[android-kernel-exploitation]]