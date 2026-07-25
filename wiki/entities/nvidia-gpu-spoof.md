---
title: Nvidia-GPU-Spoof
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/roomyoni__Nvidia-GPU-Spoof.md
updated: 2026-07-24
confidence: medium
---

# Nvidia-GPU-Spoof

Windows research tool that spoofs **NVIDIA GPU hardware identifiers** used for HWID bans: GPU serials, device IDs, and related fingerprints reported through the NVIDIA driver stack. README focuses on spoofing the NVIDIA GPU UUID by modifying `nvlddmkm.sys`; the description also notes driver-query and registry patches that anti-cheat systems use for hardware fingerprinting. (source: wiki/sources/descriptions/roomyoni__Nvidia-GPU-Spoof.md)

Useful alongside NvAPI GPU serial / board fingerprint tooling such as [[nvidiaapi]], broader HWID spoof samples such as [[hwidspoofer]] / [[spoofer-amidewin]], and Detection:HWID counterparts such as [[detect-tpm-spoofing]] / [[tpm-mmio]].

## Links

- Repo: https://github.com/roomyoni/Nvidia-GPU-Spoof

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[nvidiaapi]] · [[hwidspoofer]] · [[spoofer-amidewin]] · [[detect-tpm-spoofing]]
