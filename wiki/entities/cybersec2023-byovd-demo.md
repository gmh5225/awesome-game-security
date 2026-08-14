---
title: CYBERSEC 2023 BYOVD Demo
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__CYBERSEC2023-BYOVD-Demo.md
updated: 2026-08-14
confidence: medium
---

# CYBERSEC 2023 BYOVD Demo

CYBERSEC 2023 Taiwan conference demonstration of a full **Bring Your Own Vulnerable Driver ([[byovd]])** chain. The sample abuses MSI Afterburner's white-signed **`RTCore64.sys`** to obtain kernel read/write, nullifies the **DSE** flag, loads an unsigned malicious driver, then disables **360 Total Security** `ObRegisterCallbacks` and process notify callbacks to enable arbitrary process manipulation. (source: wiki/sources/descriptions/gmh5225__CYBERSEC2023-BYOVD-Demo.md)

Useful for kernel researchers studying conference-grade BYOVD chains that combine DSE bypass, unsigned driver load, and AC/security callback blinding. Sits in the same **`RTCore64.sys`** lane as [[rtcore64-vulnerability]] and [[pplkiller]]; callback-removal steps overlap [[ps-notif-routine-unloader]], [[bustercall]], and [[edrsandblast]].

## Links

- Repo: https://github.com/gmh5225/CYBERSEC2023-BYOVD-Demo [RTCore64.sys]

## Related

[[byovd]] · [[kernel-callbacks]] · [[rtcore64-vulnerability]] · [[pplkiller]] · [[ps-notif-routine-unloader]] · [[hitcon-2023-demo-cve-2023-20562]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
