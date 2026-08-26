---
title: QorTroller
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/ConWan30__QorTroller.md
updated: 2026-08-26
confidence: medium
---

# QorTroller

**Hardware-rooted physical input trust and controller attestation stack** by ConWan30 for verifying that gamepad input comes from a real human player rather than scripts, macros, or spoofed devices. Centers on the **VAPI protocol**, with a DualShock/controller bridge, presence challenges, biometric fusion, and **Proof of Embodied Presence (PoEP)** signals that feed session receipts and match scorecards. (source: wiki/sources/descriptions/ConWan30__QorTroller.md)

## Stack

| Layer | Components |
|-------|------------|
| Bridge / agents | Python agents and bridge services; DualShock/controller bridge |
| Attestation | VAPI protocol; presence challenges; biometric fusion; PoEP |
| Proofs | Circom/Groth16 zero-knowledge circuits for replay and verified-human proofs |
| On-chain | Solidity smart contracts; session receipts and match scorecards |
| Streaming / firmware | Rust w3bstream components; joypad firmware |

Primary use cases: **game security**, **anti-cheat research**, and on-chain attestation of controller identity and live player presence. README tag: *Cryptographic console anti-cheat proving human controller presence via attested inputs and verifiable match receipts*.

## Links

- Repo: https://github.com/ConWan30/QorTroller

## Related

[[hardware-input-injection]] · [[ai-aimbot-detection]] · [[usbmon]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
