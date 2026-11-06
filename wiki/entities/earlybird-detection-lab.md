---
title: Early Bird Detection Lab
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/jfisay__earlybird-detection-lab.md
updated: 2026-11-06
confidence: medium
---

# Early Bird Detection Lab

Windows **detection engineering lab** (jfisay) that walks through **Early Bird** queued-user APC injection into a **suspended** host process (MITRE **T1055.004**), pairs a small C injector with **Sliver** C2 shellcode into a system binary such as `RuntimeBroker.exe`, and records what **Sysmon** and **Microsoft Defender** (including cloud protection) actually surface. Documentation compares observed events to expected signals, calls out configuration-driven coverage gaps, and discusses why raw shellcode and pre–entry-point execution can slip past common layers—useful context for blue teams tuning rules beside classic remote-thread / WPM narratives. (source: wiki/sources/descriptions/jfisay__earlybird-detection-lab.md)

README lane: isolated-lab **Early Bird APC** + enterprise telemetry/AV evaluation (Sysmon/Defender).

Pairs with defender coursework such as [[process-injection-detection-lab]] (Sysmon T1055 write-thread focus) and detection corpora such as [[process-injection-techniques]]; differs by exercising **suspended-process + APC queue** timing and C2-delivered shellcode in a lab VM.

## Links

- Repo: https://github.com/jfisay/earlybird-detection-lab

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[process-injection-detection-lab]] · [[process-injection-techniques]] · [[windows-process-injection]]
