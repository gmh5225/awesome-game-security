---
title: UbuRoot
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/reinanbr__uburoot.md
updated: 2026-11-16
confidence: medium
---

# UbuRoot

**UbuRoot** (reinanbr) is an **Android app** that downloads the official **Ubuntu Base arm64** image and runs a full **Linux userspace in a native chroot** on **rooted** hardware. The UI is **Kotlin** with **Gradle**; mount, install, and integration logic lives in **POSIX shell scripts** driven through **libsu** against **Magisk**, **KernelSU**, or **APatch**. It exposes a real **PTY terminal**, **apt-based** package management, **bind mounts** into phone storage and system partitions, wrappers for Android tooling, and **opt-in kernel and hardware access** with reversible changes for low-level device work. The project targets **mobile security research**, **penetration testing**, and **reverse engineering** on custom ROMs, with documentation aimed at **NetHunter-style platform parity** rather than emulated userspace. (source: wiki/sources/descriptions/reinanbr__uburoot.md)

Contrasts with emulated guest Android VMs such as [[virtualmachine]] by providing a **real arm64 Linux rootfs** beside the host Android kernel; complements libsu rooted utilities such as [[file-explorer]] and [[kernel-loader]].

## Links

- Repo: https://github.com/reinanbr/uburoot

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[magisk]] · [[kernelsu]] · [[apatch]] · [[virtualmachine]] · [[android-security-wizard]] · [[awesome-android-security]] · [[foss-root-checker]]