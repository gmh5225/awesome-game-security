---
title: hv-detect
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__hv-detect.md
updated: 2026-08-12
confidence: medium
---

# hv-detect

Research project focused on **hypervisor IDT detections** via **SIDT** / **LIDT** — store interrupt-descriptor-table state, run detection checks inside that environment, then restore everything afterward. Aimed at anti-cheat engineers and defensive security researchers working the `Detection: Hacked Hypervisor` lane. (source: wiki/sources/descriptions/gmh5225__hv-detect.md)

Complements Hyper-V VM environment probes such as [[go-detection-hyper-v]], kernel-mode KPCR/KPRCB Hyper-V guest probes such as [[detection-hyper-v]], multi-technique C++ detectors such as [[hypervisor-detection]], hypervisor VM-detection benchmarking such as [[nohv]], user-mode HV probes such as [[checkhv-um]], and EPT hook detectors such as [[ept-hook-detection]].

## Links

- Repo: https://github.com/gmh5225/hv-detect

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[hypervisor-detection]] · [[nohv]] · [[checkhv-um]] · [[ept-hook-detection]] · [[hv]] · [[hypervisor]] · [[hvci]]
