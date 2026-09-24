---
title: SecurityRiskAndroid
kind: entity
topics: [anti-cheat, mobile-security]
sources:
  - wiki/sources/descriptions/radito__SecurityRiskAndroid.md
  - wiki/sources/README-categories.md
updated: 2026-09-24
confidence: medium
---

# SecurityRiskAndroid

**SecurityRiskAndroid** (radito/SecurityRiskAndroid) is an Android sample application with a JNI native library that implements layered **runtime-risk detection** for tampering, hooking, and root-related threats. Listed under README **Anti Cheat > Detection:Android root**. (source: wiki/sources/descriptions/radito__SecurityRiskAndroid.md)

## Detection signals

Fast synchronous checks and asynchronous deep scans cover Frida and Xposed artifacts, debugger attachment, suspicious memory mappings, ART and package visibility inconsistencies, KernelSU probes, mock-location indicators, and native code integrity via GOT/PLT, PHDR, and disk-versus-memory hash verification.

## Architecture

Java UI plus C JNI native library; optional root-assisted diagnostics; isolated-process comparison via a Messenger-backed service. Built with Gradle, Android Gradle Plugin 8.x, and CMake/NDK. Exposes scored verdicts and detailed field results for studying mobile anti-tamper techniques.

## Links

- Repo: https://github.com/radito/SecurityRiskAndroid

## Related

[[securify]] · [[rootect]] · [[mobile-anti-cheat]] · [[mobile-trust-boundaries]] · [[frida]] · [[overviews/anti-cheat]] · [[overviews/mobile-security]]
