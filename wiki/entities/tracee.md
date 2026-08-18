---
title: tracee
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/aquasecurity__tracee.md
updated: 2026-08-18
confidence: medium
---

# tracee

Aqua Security **Linux runtime security and observability** platform built on **eBPF event collection**. Implemented primarily in Go; combines low-level kernel telemetry with higher-level detections for suspicious behavioral patterns. Includes container and Kubernetes deployment paths, extensive detection content, and production-scale monitoring tooling aimed at cloud and host security teams performing threat detection, incident response, and runtime forensics. Also referenced for compatible **Android/GKI** eBPF attach when BTF, SELinux, and lockdown permit. (source: wiki/sources/descriptions/aquasecurity__tracee.md)

Sits beside mobile eBPF tracers such as [[btrace]], [[peetch]], and [[android-ebpf]], and enterprise host telemetry platforms such as [[wazuh]].

## Links

- Repo: https://github.com/aquasecurity/tracee

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[btrace]] · [[peetch]] · [[android-ebpf]] · [[wazuh]]
