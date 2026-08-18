---
title: vulkan
kind: entity
topics: [reverse-engineering, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/atrexus__vulkan.md
updated: 2026-08-18
confidence: medium
---

# vulkan

C++ **PE image dumper** for processes protected by **dynamic code encryption** such as **Hyperion** and **Theia** user-mode anti-tamper solutions. Restores encrypted PE images by iteratively resolving **`PAGE_NOACCESS`** pages until the target module decrypts, with configurable decryption-factor thresholds and import resolution support. Tested on Roblox and The Finals; also dumps regular mapped modules from memory. Mainly useful for reverse engineers and game-security researchers studying anti-tamper protections and PE dumping techniques for encrypted executables. (source: wiki/sources/descriptions/atrexus__vulkan.md)

Sits in the anti-tamper PE dump lane beside lightweight RPM dumpers such as [[dumpepe]] and defensive PAGE_NOACCESS simulation such as [[page-no-access-not-byfron]] — specialized for Hyperion/Theia-style lazy decrypt rather than plain OpenProcess reads.

## Links

- Repo: https://github.com/atrexus/vulkan

## Related

[[dumpepe]] · [[page-no-access-not-byfron]] · [[no-access-protection]] · [[no-access-protection-x86]] · [[ksdumper-11]] · [[pereconstruct]] · [[byfron-bypass]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
