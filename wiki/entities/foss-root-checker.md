---
title: FOSS Root Checker
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/Chill-Astro__FOSS-Root-Checker.md
updated: 2026-11-16
confidence: medium
---

# FOSS Root Checker

**FOSS Root Checker** (Chill-Astro) is an open-source **Android app** that audits **superuser access** and **BusyBox** on rooted or modified devices. Built with **Kotlin** and **Jetpack Compose** (Material theming), it ships **official** and **offline** APK variants—integrated self-updater versus a network-free build. The app scans **more than forty** system paths for root traces, runs live checks such as `su -c id` for privilege confirmation, and targets **Magisk**, **KernelSU**, **APatch**, and legacy rooting setups on **Android 7+**. Aimed at mobile security researchers and power users who want a transparent, low-footprint root-state auditor; useful reference when studying how games and anti-cheat stacks probe compromised Android environments. (source: wiki/sources/descriptions/Chill-Astro__FOSS-Root-Checker.md)

Complements broader offline inspectors such as [[advanced-root-checker]] and modular probe cards in [[duck-detector-refactoring]]—opposite hide frameworks [[magisk]], [[kernelsu]], and [[apatch]].

## Links

- Repo: https://github.com/Chill-Astro/FOSS-Root-Checker

## Related

[[overviews/mobile-security]] · [[mobile-anti-cheat]] · [[advanced-root-checker]] · [[duck-detector-refactoring]] · [[litmus]] · [[magisk]] · [[kernelsu]] · [[apatch]]