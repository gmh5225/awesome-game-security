---
title: Anti-Cheat Observatory
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/ANTI-CHEAT-OBSERVATORY__ANTI-CHEAT-OBSERVATORY.github.io.md
  - wiki/sources/README-categories.md
updated: 2026-10-27
confidence: high
---

# Anti-Cheat Observatory

**Anti-Cheat Observatory** (ANTI-CHEAT-OBSERVATORY) is a static reference site that catalogs commercial anti-cheat systems and public research about them using **version-scoped, source-backed claims** rather than informal articles or bypass headlines. (source: wiki/sources/descriptions/ANTI-CHEAT-OBSERVATORY__ANTI-CHEAT-OBSERVATORY.github.io.md)

Built with **Astro** and **TypeScript**; curated knowledge lives in Git-backed JSON with schema validation; published as a searchable static site (**Pagefind**) on GitHub Pages.

## Content model

- **System dossiers** and **mechanism worksheets** for major products and their kernel/client boundaries.
- **Build comparisons** and **relationship graphs** linking products, mechanisms, and public research.
- **Discovery pipeline** that polls approved RSS, GitHub, and document sources while keeping **provenance**, **review activity**, and **claim state** separate—unreviewed feeds are not promoted to verified findings.
- Node.js maintenance scripts validate cross-references, import editorial proposals, and sync metadata. (source: wiki/sources/descriptions/ANTI-CHEAT-OBSERVATORY__ANTI-CHEAT-OBSERVATORY.github.io.md)

## Audience and scope

Targets game security researchers, anti-cheat analysts, and reverse engineers who need an evidence-oriented map of products such as [[battleye]], [[easy-anti-cheat]], [[vanguard]], and related enforcement boundaries—not runtime detection or bypass tooling.

Complements structured link indexes such as [[anti-cheat-research-index]] and Linux hosting feasibility notes such as [[ac-compat-research]] in the Guide / Analysis Framework lane.

## README placement

Listed under **Anti Cheat** (Guide / catalog lane). (source: wiki/sources/README-categories.md)

## Links

- Repo: https://github.com/ANTI-CHEAT-OBSERVATORY/ANTI-CHEAT-OBSERVATORY.github.io

## Related

- [[overviews/anti-cheat]] — detection methodology and product boundaries
- [[research-rigor]] — claim provenance and dispute handling discipline
