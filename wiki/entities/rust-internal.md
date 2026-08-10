---
title: rust-internal
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/gmh5225__rust-internal.md
updated: 2026-08-07
confidence: medium
---

# rust-internal

C++ **internal** cheat framework for Facepunch **Rust**, built around a Horizon core with DirectX 11 rendering and ImGui overlays. Includes memory and map helpers, HDE64 disassembly support, secure string utilities, and Win32 or DX11 ImGui backends for in-process UI and graphics hooks. Framed for game security researchers and reverse engineers studying offensive techniques in the cheat / game:rust lane. (source: wiki/sources/descriptions/gmh5225__rust-internal.md)

Complements the OOP driver/rendering base in [[simple-rust-base]], minimal title-specific source [[simple-rust-hack]], external kernel/RPM + overlay sample [[rust-external-1]], rendering/networking external sample [[rust-external]], and loader-oriented samples such as [[a-pasted-rust-script]] for comparing full in-process DX11/ImGui scaffold layout vs bare cheat sources, out-of-process ESP, and ImGui loaders.

## Links

- Repo: https://github.com/gmh5225/rust-internal

## Related

[[simple-rust-base]] · [[simple-rust-hack]] · [[rust-external-1]] · [[rust-external]] · [[a-pasted-rust-script]] · [[present-hook]] · [[imgui]] · [[easy-anti-cheat]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
