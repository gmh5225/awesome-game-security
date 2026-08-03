---
title: EtwTi-FluctuationMonitor
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/jdu2600__EtwTi-FluctuationMonitor.md
updated: 2026-08-03
confidence: medium
---

# EtwTi-FluctuationMonitor

Windows tool that monitors ETW Threat Intelligence (EtwTi) provider registration fluctuations to detect tampering with security products. It watches for changes in EtwTi callback registrations that indicate an attacker is removing or patching ETW-based monitoring — a common EDR evasion technique. The C implementation emits real-time alerts on callback manipulation. (source: wiki/sources/descriptions/jdu2600__EtwTi-FluctuationMonitor.md)

Aimed at defensive security researchers and EDR developers building tamper detection for ETW-based telemetry. Complements bypass samples such as [[disable-threat-tracing]] and [[telemetry-sourcerer]] on the blind side, and ThreatIntel consumers such as [[tietwagent]] on the consume side.

## Links

- Repo: https://github.com/jdu2600/EtwTi-FluctuationMonitor

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[etw-threat-intelligence]] · [[etw-watcher]] · [[etw-explorer]] · [[tietwagent]] · [[disable-threat-tracing]]
