---
title: ADB Debug Detect Checker
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/fiord__ADB-Debug-Detect-Checker.md
updated: 2026-08-15
confidence: medium
---

# ADB Debug Detect Checker

Android **Java** sample app that checks whether **ADB debugging is available** on the device—i.e., whether the environment is in a state where debugging via ADB is possible. Aimed at **anti-cheat engineers** and **defensive security researchers** studying Android **anti-debugging** and developer-options / USB-debug signals that mobile AC and RASP stacks often fold into debugger or tamper heuristics. (source: wiki/sources/descriptions/fiord__ADB-Debug-Detect-Checker.md)

Useful as a compact reference implementation for **ADB-detection** probes beside broader Android anti-debug samples such as [[antidebugandmemorydump]] and client RASP SDKs that include debugger callbacks (e.g. [[free-rasp-android]], [[droidshield]]).

## Links

- Repo: https://github.com/fiord/ADB-Debug-Detect-Checker

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[antidebugandmemorydump]] · [[anti-debugging]] · [[lamda]] · [[adb-file-manager]]
