# CHANGELOG — Tree Distance Cophenetic

## 2026-05-15 — Mathematical formalization

### What Changed
- **Created:** `0.3.md` — Mathematical Formalization of the Cophenetic Distance Framework. Contains formal definitions, worked dendrogram example with distance matrix, proof of ultrametric inequality from tree LCA property, derivation of triadic rigidity, binary decomposition theorem, gauge invariance discussion, and information-theoretic interpretation.
- **Created:** `0.3.py` — Companion Python verification script with `Tree` class, all-pairs distance computation, ultrametric/triadic rigidity verification on 4-item and 6-item dendrograms, and Euclidean counterexample.
- **Reviewed:** Additional releases (`2025/08/`, `2025/11/`) and archive. Found new convergence points (C8-C12) including resolution-dependence bridge (tree depth = epsilon parameter in Illusion of Time). Archive limited — no cophenetic/ultrametric content found, confirming framework novelty.

### Key Findings
- Cophenetic distance on rooted trees with monotone heights always satisfies ultrametric inequality (proven from LCA property)
- Triadic rigidity is a necessary consequence — all triangles are acute isosceles
- Binary decomposition theorem confirms yes/no as atomic operation of hierarchical organization
- Gauge invariance: branching order is invariant; specific numerical distances are conventional

### Files Changed
- `0.3.md` (new), `0.3.py` (new), `SPRINT.md` (edit), `CHANGELOG.md` (edit), `PROJECT STATE.md` (edit)

### Git
- Branch: `feature/ultrametric-v2-ternary-tree`
- Commit: `7a7dc78`

---

## 2026-05-14 (Second session)

### What Changed
- **Imported:** 16 release documents from `G:\My Drive\Obsidian\releases\2025\00\` as `src_0.2_*.md` for cross-reference review.
- **Launched:** 3 parallel subagents for cross-reference synthesis, gap analysis, and reader testing of `0.1.1.md`.
- **Created:** `0.2.md` — Subagent Review Synthesis aggregating all findings.
- **Updated:** `PROJECT STATE.md`, `SPRINT.md`, `CHANGELOG.md` with review results and next steps.

### Key Findings
- Tree Distance Cophenetic provides mathematical skeleton for philosophical body of existing releases
- 7 convergence points, 5 tensions, 9 extensions identified
- 11 missing elements, 8 unique contributions, 9 recommended additions
- Reader testing: document assumes too much prior knowledge, no cophenetic distance definition, no examples, no citations

### Files Changed
- `src_0.2_*.md` (16 new), `0.2.md` (new), `PROJECT STATE.md` (edit), `SPRINT.md` (edit), `CHANGELOG.md` (edit), `_scan_dirs.py` (new), `_import_sources.py` (new)

### Git
- Branch: `feature/pii-scrub-github`
- Commits: `f6c54ff`, `93195f3`, `94964d2`, `2f6451d`, `645d8e9`, `488bf8b`

---

## 2026-05-14 (First session)
- **Created:** `README.md`, `PROJECT STATE.md`, `SPRINT.md`, `CHANGELOG.md`, `BACKLOG.md`, `LEARNINGS.md`, `DECISIONS.md` — Initial project documentation setup. Agent session start.
