# CHANGELOG

> **Purpose:** Versioned record of all project changes.

---

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
