---
title: ZeroHVCI
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__ZeroHVCI.md
updated: 2026-08-09
confidence: medium
---

# ZeroHVCI

Windows HVCI (Hypervisor-Protected Code Integrity) bypass proof of concept aimed at executing unsigned kernel code despite Hyper-V enforcing code integrity at the hypervisor level. Demonstrates circumvention techniques such as HVCI policy edge cases and [[byovd]]-style abuse of vulnerable signed drivers — framed for kernel security researchers studying Memory Integrity bypass and virtualization-based security limitations. (source: wiki/sources/descriptions/gmh5225__ZeroHVCI.md)

Adjacent to early-boot / CI-path bypass kits such as [[bootbypass]], CI.dll hook PoCs such as [[dse-hook]], and PFN-swap HVCI research such as [[bustercall]] — here the focus is direct HVCI circumvention rather than boot-manager patching, DSE-only hooks, or callback/PFN manipulation alone.

## Links

- Repo: https://github.com/gmh5225/ZeroHVCI

## Related

[[hvci]] · [[byovd]] · [[bootbypass]] · [[dse-hook]] · [[bustercall]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
