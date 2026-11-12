---
title: SIM Number Setter Pro
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/MayaXDev__SIMNumberSetter-Pro.md
  - wiki/sources/README-categories.md
updated: 2026-11-12
confidence: medium
---

# SIM Number Setter Pro

Open-source Android utility that reads, writes, and programs the subscriber phone number (MSISDN) into SIM **EF_MSISDN** so the device reports a valid number instead of unknown MSISDN. (source: wiki/sources/descriptions/MayaXDev__SIMNumberSetter-Pro.md)

Kotlin/Gradle app for Android API 26–34. Primary path: **LSPosed/Xposed** hooks on `com.android.phone` and the system framework. Fallback: rooted access via telephony providers and shell on **Magisk**, **KernelSU**, or **APatch**. Dual-SIM slot selection, E.164 validation, automatic phone-state permission grants, telephony-stack hot-restart without full reboot, and optional internal telephony stubs for low-level Phone APIs. Targets researchers studying mobile identity, SMS/OTP verification, carrier provisioning, and how rooted or hooked devices alter telephony-reported attributes.

## Links

- Repo: https://github.com/MayaXDev/SIMNumberSetter-Pro (README: rooted Android MSISDN EF_MSISDN programmer via LSPosed hooks or telephony providers; dual-SIM; API 26–34)

## Related

[[swsim]] · [[lsposed-universal-template]] · [[xiaomi-usb-security-bypass]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
