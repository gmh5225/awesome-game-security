---
title: HWID Spoofing
kind: concept
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/skills/game-hacking.md
  - wiki/sources/descriptions/SamuelTulach__negativespoofer.md
  - wiki/sources/descriptions/Th3Spl__PerfectSMBios.md
  - wiki/sources/descriptions/gmh5225__HWID-Kernel-Spoofer.md
  - wiki/sources/descriptions/GJR787878__DeviceResetSpoofer.md
updated: 2026-09-09
confidence: medium
---

# HWID Spoofing

Techniques that **replace or mask hardware identifiers** queried by anti-cheat, launcher, or platform ban systems. Spoofing targets the *reported* identity seen by user-mode collectors—not necessarily the underlying firmware or bus topology. A changed serial in one API response does not prove all observers see the same value or that gameplay misconduct occurred. (source: wiki/sources/skills/game-hacking.md)

## Common targets

| Identifier | Typical query path |
|------------|-------------------|
| Disk serial | `IOCTL_STORAGE_QUERY_PROPERTY`, SMART |
| NIC MAC | NDIS `OID_802_3_PERMANENT_ADDRESS` |
| SMBIOS | Motherboard serial, system UUID, BIOS vendor |
| GPU | Registry or NVAPI/ADL serial queries |
| Monitor | EDID display serial |
| Volume | `NtQueryVolumeInformationFile` |
| TPM | Endorsement Key fingerprint |

## Technique classes

- **Filter driver IOCTL interception** — return substituted serial/MAC in driver responses
- **Registry cache patching** — modify cached hardware IDs the OS or AC reads
- **SMBIOS table patching** — edit raw SMBIOS memory region before query
- **NIC driver hook** — replace MAC in NDIS miniport responses
- **Coordinated spoofers** — rotate multiple identifiers together to defeat composite fingerprints

Kernel-mode samples such as [[hwid-kernel-spoofer]] (gmh5225; C/C++; kernel driver development; cheat / HWID) and user-mode/registry-oriented tools such as [[negativespoofer]] (SamuelTulach; C++; cheat / HWID) illustrate common implementation lanes. UEFI pre-boot SMBIOS spoofing such as [[perfectsmbios]] (Th3Spl; UEFI; cheat / HWID) operates before the OS loads. Mobile post-clear identity rotation such as [[device-reset-spoofer]] (GJR787878; Android; cheat / HWID) sits in a parallel mobile ban-evasion lane. (source: wiki/sources/descriptions/gmh5225__HWID-Kernel-Spoofer.md) (source: wiki/sources/descriptions/SamuelTulach__negativespoofer.md) (source: wiki/sources/descriptions/Th3Spl__PerfectSMBios.md) (source: wiki/sources/descriptions/GJR787878__DeviceResetSpoofer.md)

## Defensive limits

- Compare **multiple independent sources** (WMI, driver IOCTL, firmware tables, attestation) before treating a mismatch as spoofing
- Spoofed values may revert after reboot unless firmware or driver persistence is established
- Shared hardware profiles, VMs, and legitimate repair workflows produce overlapping signals
- Pair with [[network-environment-evidence]] for account/device association—not serial substitution alone

## Related

[[network-environment-evidence]] · [[device-reset-spoofer]] · [[hidemyandroid]] · [[byovd]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
