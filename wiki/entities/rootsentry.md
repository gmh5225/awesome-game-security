---
title: RootSentry
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/cognis-digital__rootsentry.md
updated: 2026-08-20
confidence: medium
---

# RootSentry

Zero-dependency Python mobile runtime-integrity framework that scores on-device telemetry against a catalog of compromise indicators and returns a weighted posture verdict from TRUSTED through CRITICAL. Matches evidence snapshots for root and jailbreak artifacts, emulator fingerprints, hooking frameworks such as [[frida]] and Xposed, and tamper signals on Android and iOS. Ships a CLI and library for single-device evaluation, fleet-scale cohort analysis, and MITRE ATT&CK for Mobile technique mapping, plus reference Kotlin and Swift collectors and polyglot example detectors. Intended for defensive RASP-style self-protection, backend attestation pipelines, and authorized security assessments where apps must detect compromised or instrumented runtimes before allowing high-risk actions. (source: wiki/sources/descriptions/cognis-digital__rootsentry.md)

Sits in the mobile RASP / integrity lane alongside [[device-trust]], [[risk-engine]], [[droidshield]], and the freeRASP family—opposite root frameworks [[magisk]] / [[kernelsu]] and instrumentation tooling [[frida]] / [[xposed-module-kit]].

## Links

- Repo: https://github.com/cognis-digital/rootsentry

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[device-trust]] · [[risk-engine]] · [[droidshield]] · [[frida-detection]] · [[android-emulator-detection]] · [[detection]] · [[magisk]] · [[frida]]
