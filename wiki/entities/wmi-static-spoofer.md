---
title: wmi-static-spoofer
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Alex3434__wmi-static-spoofer.md
updated: 2026-09-02
confidence: medium
---

# wmi-static-spoofer

**wmi-static-spoofer** (Alex3434) is a Windows **kernel-mode proof of concept** for **statically spoofing hardware serial information** exposed through **WMI** and related query paths. Instead of installing long-lived dispatch or callback hooks, the driver applies **direct memory manipulation** and **registry updates**, then can **unload** once identifiers are rewritten. The implementation supports **configurable offsets** and **randomized serial generation** for testing different hardware profiles. It is mainly used for **HWID evasion research** against anti-cheat and licensing telemetry. (source: wiki/sources/descriptions/Alex3434__wmi-static-spoofer.md)

Distinct from persistent hook-based kernel HWID spoofers such as [[easy-hwid-spoofer]] and [[hwid-kernel-spoofer]] — emphasizes one-shot WMI-path identifier patching without leaving hook dependencies. Complements hook-minimal storage/SMBIOS rewriters such as [[mutante]] by targeting the **WMI inventory surface** that defensive tools like [[windows-hardware-info]] enumerate.

## Links

- Repo: https://github.com/Alex3434/wmi-static-spoofer

## Related

[[mutante]] · [[easy-hwid-spoofer]] · [[hwid-kernel-spoofer]] · [[skotschia-hwid-spoofer]] · [[windows-hardware-info]] · [[hwid-checker-mg]] · [[hwid-spoofer-eac]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
