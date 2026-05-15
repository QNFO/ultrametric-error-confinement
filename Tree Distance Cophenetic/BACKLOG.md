# BACKLOG — Tree Distance Cophenetic

> **Status:** Sprint 1 complete. 0.8.md is publication-ready (all citations verified, reader-tested). Zenodo upload is the natural next action.

## HIGH Priority
- [ ] **Upload 0.8.md to Zenodo** — DOI 10.5281/zenodo.20200828 assigned; requires Zenodo deposit. Blocker: manual action by author.
- [ ] **Fresh-Claude reader test** — Blind testing of 0.8.md with 7-question protocol (§7.4). Subagents unavailable; requires manual fresh Claude session.

## MEDIUM Priority
- [ ] **Design empirical test for triadic rigidity** — Pick one domain (phylogenetics, social networks, linguistics, clustering benchmarks) and design a falsifiable test. This operationalizes the framework's key empirical claim.
- [ ] **Address 4 CGF weaknesses** (§5.2): empirical deficit, physics minority position, citation gap (now resolved), reader accessibility. Most require external research, not document edits.

## LOW Priority
- [ ] **Write accessible introduction** — Standalone version assuming no ultrametrics/cophenetic knowledge. Add glossary of terms.
- [ ] **Add tree structure diagrams** — Visual dendrograms, LCA illustrations, height function schematics for §§1-2.
- [ ] **Package `0.3.py` as standalone Python module** — `pip install`-able Tree class with verification suite.
- [ ] **Explore applications**: phylogenetics, clustering, decision theory, linguistics.

## Completed (Sprint 1 — 2026-05-15)
- [x] Python verification of ultrametric inequality and triadic rigidity → `0.3.py` (70+ checks)
- [x] Math formatting audit (Unicode → LaTeX) → all 7 content files CLEAN
- [x] Document unification → `0.7.md`, then `0.8.md` (publication draft)
- [x] Imported 16 external sources → `src_0.2_*.md`
- [x] All HIGH/MEDIUM/LOW sprint tasks → `0.3.md`–`0.6.md`
- [x] Branch renamed → `feature/tree-distance-cophenetic`
- [x] All 5 citations verified by external search → `[VERIFIED]`
- [x] Reader testing → 12 issues found and fixed (I1-I12)
- [x] All 7 project documentation files updated to final state
- [x] LEARNINGS.md populated with 5 project-specific lessons
