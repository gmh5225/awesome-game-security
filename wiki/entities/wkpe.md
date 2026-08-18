---
title: wkpe
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/am0nsec__wkpe.md
updated: 2026-08-18
confidence: medium
---

# wkpe

**Windows kernel programming experiments** packaged as proof-of-concept drivers with companion user-mode tools. Focus is low-level internals—especially **memory manager** behavior—with examples such as **listing process VAD structures**. Implemented in C/C++ with Visual Studio and WDK-style projects; documents strong coupling to specific Windows builds and symbol availability. Intended for educational kernel research and controlled security experimentation, not production deployment. (source: wiki/sources/descriptions/am0nsec__wkpe.md)

README lane: Enumerate VAD.

## Links

- Repo: https://github.com/am0nsec/wkpe

## Related

[[kernel-vad-injector]] · [[modmap]] · [[stealthy-kernelmode-injector]] · [[document]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
