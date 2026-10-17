---
title: sshserver-magisk
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/Ayoubvvch__sshserver-magisk.md
updated: 2026-10-17
confidence: medium
---

# sshserver-magisk

**Magisk**, **KernelSU**, and **APatch** flashable module that starts a lightweight **Dropbear** SSH and SFTP server on rooted Android from boot—no Termux or separate userland app required. Ships statically compiled arm64 Dropbear and SFTP binaries linked against **musl libc** to avoid Android linker-namespace issues on Android 10 through 15+. Authentication supports **Ed25519** or **RSA** public keys plus **SHA-512** password auth via a systemless generated `passwd` file. (source: wiki/sources/descriptions/Ayoubvvch__sshserver-magisk.md)

The **`sshserverctl`** shell utility manages the daemon; settings live in **`config.env`**. **TCP keepalives** help sessions survive Doze. Magisk **`post-fs-data`** and **`late_start`** service hooks tie installation to module startup. Targets developers and security researchers who need persistent headless root shell and file transfer over the network for mobile debugging, instrumentation, and reverse-engineering workflows. (source: wiki/sources/descriptions/Ayoubvvch__sshserver-magisk.md)

Complements tailnet remote access via [[magisk-tailscaled]] and wireless ADB lanes such as [[nowifi-adb]]—local Dropbear SSH/SFTP without a PC-attached Frida or ADB session.

## Links

- Repo: https://github.com/ayoubvvch/sshserver-magisk [Magisk/KernelSU/APatch module with statically linked Dropbear SSH and SFTP for headless root shell access from boot]

## Related

[[magisk]] · [[kernelsu]] · [[apatch]] · [[magisk-tailscaled]] · [[nowifi-adb]] · [[frida-magisk]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
