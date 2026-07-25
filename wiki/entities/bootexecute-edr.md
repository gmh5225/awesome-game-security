---
title: BootExecuteEDR
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/rad9800__BootExecuteEDR.md
updated: 2026-07-25
confidence: medium
---

# BootExecuteEDR

Research sample for **bootExecute** EDR bypass: execution that runs in the Windows boot path **before services start**, so EDR/AC user-mode services and many late-load drivers are not yet online. Framed for game-security / RE study of offensive early-boot techniques in the cheat / hide lane. (source: wiki/sources/descriptions/rad9800__BootExecuteEDR.md)

Adjacent early-boot / CI trust research includes [[bootbypass]] (Secure Boot / DSE / HVCI via `SeCiCallbacks`) and EFI pre-kernel mappers such as [[efitool]] / [[xigmapper]]; runtime EDR blind tooling such as [[edrsandblast]] sits later in the boot timeline (callbacks / ETW after kernel is up).

## Links

- Repo: https://github.com/rad9800/BootExecuteEDR

## Related

[[bootbypass]] · [[edrsandblast]] · [[efitool]] · [[xigmapper]] · [[hvci]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
