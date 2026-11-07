---
title: droid-vm
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/boz700908__droid-vm.md
updated: 2026-11-07
confidence: medium
---

# droid-vm

Runs a **full Android guest** with real **Magisk**, **KernelSU (LKM)**, or **KernelPatch (KPM)** on **stock, non-rooted arm64 phones** by booting a genuine Linux kernel as a **User Mode Linux (UML)** process—not containers or QEMU. Builds on an **Android GKI-based arm64 UML** port with SMP, **ext4/qcow2** root disks, **binder**, and optional framebuffer and **virtio-gpu**; kernel configs enable module loading, **kprobes**, and Magisk-friendly features. Shell scripts and GitHub Actions assemble kernel artifacts and **Alpine-based** root filesystems; **Termux**-oriented launch scripts support on-device testing. Targets mobile security and modding research where analysts need a rooted Android environment **without elevating the host device**, including workflows that depend on real kernel modules and root-style tooling. (source: wiki/sources/descriptions/boz700908__droid-vm.md)

Distinct from hypervisor/QEMU on-phone stacks such as [[droidvm]] (Gunyah + KVM guests; host root required) and container hosts such as [[anbox]] (LXC namespaces on Linux). Sits beside no-root sandbox VMs ([[zn-toolbox]], [[virtualmachine]]) and classic emulator root paths ([[aeroot]], [[rootavd]]) when the goal is **real LKM/Magisk/KPM** inside an isolated guest on an unmodified phone.

## Links

- Repo: https://github.com/boz700908/droid-vm (README: Non-root Android host · UML arm64 guest · Magisk / KernelSU / KernelPatch)

## Related

[[magisk]] · [[kernelsu]] · [[apatch-kpm]] · [[kernelpatch]] · [[termux-app]] · [[droidvm]] · [[anbox]] · [[aeroot]] · [[virtualmachine]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
