---
title: CS2 Hybrid Anti-Cheat Proposal
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/mishka-sit2002__CS2-Hybrid-AntiCheat-Proposal.md
updated: 2026-07-29
confidence: medium
---

# CS2 Hybrid Anti-Cheat Proposal

Technical **proposal and Python proof-of-concept** for a Counter-Strike 2 hybrid anti-cheat that pairs automated detection with a community **Overwatch-style review pipeline**. Intended for game-security researchers, AC designers, and CS2 developers evaluating scalable hybrid detection plus human adjudication. (source: wiki/sources/descriptions/mishka-sit2002__CS2-Hybrid-AntiCheat-Proposal.md)

## Design highlights

- **Dual lane:** VAC Live–style machine-learning signals alongside Overwatch 2.0–style peer review.
- **Glicko-2 judge ratings:** weighted voting so accurate reviewers carry more influence and bot farms are harder to abuse.
- **Honeypot entities:** invisible server-side bait for deterministic aimbot and wallhack proof.
- **Shadow monitoring:** observe flagged players across two to three matches before enforcement to cut false positives.
- **Esports pro handling:** special-case workflow for professional accounts.
- **Bonus sketch:** Source 2 fall-damage fix using vertical height delta instead of air time (engine-adjacent note in the same repo).

## Links

- Repo: https://github.com/mishka-sit2002/CS2-Hybrid-AntiCheat-Proposal

## Related

[[overviews/anti-cheat]] · [[ai-aimbot-detection]] · [[waldo]] · [[aimbot-detection-prototype]] · [[no-mercy]] · [[certael]]
