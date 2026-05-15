# BACKLOG — Tree Distance Cophenetic

> **Status:** Project near-complete. 0.8.md is the definitive publication draft. Only citation verification and reader testing remain.

## HIGH Priority (BLOCKED — Requires External Search)
- [~] **Verify 5 academic citations** — Execute Search Request Manifest (0.8.md §7.2):
  - R1: Sokal & Rohlf (1962), *Taxon*, 11(2), 33–40
  - R2: Sneath & Sokal (1973), *Numerical Taxonomy*, W. H. Freeman
  - R3: Page & Wootters (1983), *Physical Review D*, 27(12), 2885
  - R4: DeWitt (1967), *Physical Review*, 160(5), 1113
  - R5: Hartigan (1967), *JASA*, 62(320), 1140–1158
  - **Blocker:** No web search capability in this environment. Requires manual execution.

## MEDIUM Priority
- [ ] **Reader test 0.8.md** — Manual fresh-Claude session with 7-question protocol (0.8.md §7.4). Subagents unavailable in this environment.
- [ ] **Upload to Zenodo** — 0.8.md has DOI 10.5281/zenodo.20200828; needs actual Zenodo deposit.

## LOW Priority
- [ ] Add diagrams/visualizations of tree structures (dendrograms, LCA illustrations)
- [ ] Create standalone Python package from `0.3.py` (Tree class + verification)
- [ ] Explore applications: phylogenetics, clustering, decision theory
- [ ] Cross-reference with `_shared/CROSS-PROJECT-LEARNINGS.md`

## Completed (Archived)
- [x] Python verification of ultrametric inequality and triadic rigidity → `0.3.py` (70+ checks)
- [x] Math formatting audit (Unicode → LaTeX) → all 7 content files CLEAN
- [x] Document unification → `0.7.md`, then `0.8.md` (publication draft)
- [x] Imported 16 external sources → `src_0.2_*.md`
- [x] All HIGH/MEDIUM/LOW sprint tasks → `0.3.md`–`0.6.md`
