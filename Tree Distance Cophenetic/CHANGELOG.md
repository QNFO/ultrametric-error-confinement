# CHANGELOG — Tree Distance Cophenetic

## 2026-05-15 — Bridges and Self-Evaluation

### What Changed
- **Created:** `0.4.md` — Bridges: Resolution-Dependence and Generative Mechanism. Maps tree depth to Illusion of Time's ε parameter, resolves static/dynamic tension (T1) via block universe reconciliation, integrates Autaxys as symmetry-breaking mechanism.
- **Created:** `0.5.md` — Methodology and CGF Self-Evaluation. Documents 5I Process application with iteration history, scores framework 4.0/5 across Logical (4.3), Evidential (3.3), Scientific (4.2), Generativity (4.2) dimensions. Includes framework comparison table.
- **Updated:** SPRINT.md, CHANGELOG.md, PROJECT STATE.md

### Key Findings
- Resolution-dependence bridge is the strongest convergence (C12): tree depth = ε; cophenetic distance = resolution threshold; root = coarsest ε (Big Bang)
- Static/dynamic tension resolved: tree = completed output (block universe); Autaxys = the process (traversal). Same object, different standpoints — Page-Wootters applied to ontology
- Framework strong on mathematical precision (4.3/5) and generativity (4.2/5); weak on empirical evidence (3.3/5)
- CGF identifies 4 weaknesses: empirical deficit, physics minority position, citation gap, reader accessibility

### Git
- Branch: `feature/ultrametric-v2-ternary-tree`
- Commits: `8f1132f` (0.4.md), `e2c9de4` (0.5.md)

---

## 2026-05-15 — Verification Complete & Content Review

### What Changed
- **Executed:** `0.3.py` — All 70+ mathematical checks passed `[CODE-EXECUTED]`:
  - 4-item dendrogram: 12 ultrametric + 4 triadic rigidity = all passed
  - 6-item dendrogram: 60 ultrametric + 20 triadic rigidity = all passed
  - Euclidean counterexample: triadic rigidity confirmed to FAIL (expected)
- **Fixed:** Unicode emoji encoding issues in `0.3.py` for Windows CP1252 compatibility
- **Fixed:** Typo in `0.3.md` §3.3 (A,A,C → A,B,C)
- **Updated:** `0.3.md` §7 — replaced "[VERIFICATION PENDING]" with executed results table and 6-item distance matrix
- **Updated:** `0.3.md` status from "Draft" to "Verified"
- **Audit:** Math formatting scan — PASSED (zero bare Unicode math outside code/math blocks)
- **Cleaned:** Removed temporary audit scripts `_audit_math.py`, `_audit_math2.py`

### Git
- Branch: `feature/ultrametric-v2-ternary-tree`
- Commits: `f405190` (0.3.py fix), `cce7f41` (0.3.md fixes)

---

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
