# CHANGELOG

> **Purpose:** Versioned record of all project changes.

---

## [v1.2.1] — 2026-05-12 — Zenodo DOI Correction

### Completed

| Item | Description |
|:-----|:------------|
| DOI correction | Replaced arXiv placeholder with Zenodo DOI `10.5281/zenodo.20134944` in header and footer |
| Docs updated | SPRINT.md, BACKLOG.md, PROJECT STATE.md, DECISIONS.md — removed arXiv references, marked P4 (Zenodo) complete |

### Files Changed

| File | Change |
|:-----|:-------|
| papers/ultrametric-error-confinement.md | EDIT — arXiv → Zenodo DOI |
| SPRINT.md | EDIT — removed P4 (arXiv), marked P4 (Zenodo) complete, added P5 (Promote) |
| BACKLOG.md | EDIT — same as SPRINT |
| PROJECT STATE.md | EDIT — publication status, known issues |
| DECISIONS.md | EDIT — D3 updated to Zenodo-only |

## [v1.2] — 2026-05-12 — Paper Polish & Plot Fix (P3 + P7)

### Completed

| Item | Description |
|:-----|:------------|
| P7: Plot fix | Fixed column name mismatch in `plots.py` — `"min_flips"` → `"barrier"`, `"theoretical"` key resolved |
| P3: Paper polish | Added arXiv placeholder, version/commit metadata to header. Strengthened reproducibility footer. Fixed ref [12] title. |
| Unicode math scan | Paper passes scan — no bare Unicode math characters in mathematical contexts |
| Paper quality scan | 3,877 words, 19 refs, 6 sections, no formatting errors detected |
| Plot verified | experiment_0b energy barrier plot now generates correctly |

### Files Changed

| File | Change |
|:-----|:-------|
| simulations/plots.py | EDIT — fixed column name mismatch in plot_energy_barrier |
| papers/ultrametric-error-confinement.md | EDIT — header metadata, reproducibility footer, ref [12] title |
| SPRINT.md | EDIT — marked P3, P7 complete |
| CHANGELOG.md | EDIT — added v1.2 entry |

## [v1.1] — 2026-05-12 — Project Audit & Cleanup

### Completed

| Item | Description |
|:-----|:------------|
| Experiment verification | Both 0A (error confinement) and 0B (energy barrier) reproduce expected results |
| __pycache__ removed | Compiled Python cache removed from git tracking. .gitignore verified. |
| Nested directory removed | simulations/simulations/plots/ deleted — leftover from path bug |
| Docs rewritten | PROJECT STATE.md expanded to comprehensive handoff document (8 sections). SPRINT.md updated with verified completions and re-prioritized backlog. |

### Files Changed

| File | Change |
|:-----|:-------|
| simulations/__pycache__/ (5 files) | DELETE — removed from tracking |
| simulations/simulations/plots/exp0a_error_confinement.png | DELETE — nested directory cleanup |
| PROJECT STATE.md | EDIT — comprehensive rewrite (v1.0 -> v1.1) |
| SPRINT.md | EDIT — updated completions, re-prioritized backlog |

---

## [v1.0] — 2026-05-12 — Project Extraction from QWAV

### Source
Extracted from QWAV ultrametric quantum computing project.

### Files Imported
- papers/ultrametric-error-confinement.md — arXiv-ready paper (6 sections, 19 refs)
- simulations/ (11 files) — Full Tier 0 simulation suite

### Project Infrastructure Created
- 7 project docs (README, PROJECT STATE, SPRINT, CHANGELOG, BACKLOG, LEARNINGS, DECISIONS)
- .gitignore
