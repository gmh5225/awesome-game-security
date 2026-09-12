---
title: forti-research
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/mein-0__forti-research.md
  - wiki/sources/README-categories.md
updated: 2026-09-12
confidence: medium
---

# forti-research

Proof-of-concept research targeting Fortinet's **`fortimon3_74.sys`** kernel driver, part of FortiClient's anti-exploit minifilter stack. Written in **C**, the PoC connects to the driver's Filter Manager communication port via the Windows Filter Manager API and sends an **unauthenticated 8-byte kill message** to terminate arbitrary processes from kernel mode—without buffer overflows or complex exploitation chains. (source: wiki/sources/descriptions/mein-0__forti-research.md)

Local administrators can terminate **PPL-protected** targets such as Windows Defender and **`lsass.exe`**. The write-up documents additional root causes: missing caller authentication, handle-table misuse that could enable credential theft, and **BYOVD risk** because the driver is Fortinet-signed. Intended for kernel security researchers studying PPL bypass, vulnerable signed-driver abuse, and anti-exploit product security. Listed under README **Cheat** (removed from Vulnerable Driver).

## Attack surface

| Element | Role |
|---------|------|
| **`fortimon3_74.sys`** | FortiClient anti-exploit minifilter backend |
| Filter Manager port | User-mode connect + 8-byte kill message (no auth) |
| Kernel terminate | Force-kill PPL-protected AV/LSA processes |

## Links

- Repo: https://github.com/mein-0/forti-research

## Related

[[byovd]] · [[pplkiller]] · [[phantomkiller]] · [[process-killer-byovd]] · [[driver-communication]] · [[memfilter-fn-driver]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
