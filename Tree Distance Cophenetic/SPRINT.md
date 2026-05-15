# SPRINT — Tree Distance Cophenetic

**Sprint 2:** Publication & Empirical Grounding
**Started:** 2026-05-15
**Branch:** `feature/tree-distance-cophenetic`

## Sprint 2 Tasks

### HIGH Priority
- [ ] **Zenodo upload** — Upload `0.8.md` to Zenodo (DOI: 10.5281/zenodo.20200828). Requires author action (login, deposit).
- [ ] **Fresh-Claude reader test** — Blind testing with 7-question protocol (`0.8.md` §7.4). Critical self-review found I8-I12; blind test may catch more.

### MEDIUM Priority
- [x] **Empirical test design** — 0.9.md + 0.9.py (2026-05-15). Three test proposals (A/B/C). Test B prototype executed: TRI cleanly separates hierarchical (1.000) from non-hierarchical (0.135) structures. All permutation tests $p < 0.001$.
- [ ] **CGF weakness mitigation** (§5.2): Draft plan for addressing empirical deficit (what data would test triadic rigidity?), physics minority position (engage with alternatives?), reader accessibility (glossary?).

### LOW Priority
- [ ] **Accessible introduction** — Write standalone intro assuming no ultrametrics/cophenetic knowledge. Add glossary.
- [ ] **Tree diagrams** — Create visual dendrogram, LCA illustration, height function schematic for §§1-2.
- [ ] **Python package** — Package `0.3.py` as standalone module with `setup.py`.

---

## Sprint 1 — Complete ✅ (2026-05-15)

| Priority | Task | Status |
|:---------|:-----|:-------|
| HIGH | Cophenetic distance definition + example | ✅ `0.3.md` / `0.8.md` §2 |
| HIGH | Ultrametric inequality + triadic rigidity proof | ✅ `0.3.py` — 70+ checks [CODE-EXECUTED] |
| HIGH | Python verification script | ✅ `0.3.py` |
| HIGH | Generative mechanism (Autaxys bridge) | ✅ `0.4.md` / `0.8.md` §3 |
| HIGH | Methodology (5I process) | ✅ `0.5.md` / `0.8.md` §5 |
| HIGH | CGF self-evaluation (4.0/5) | ✅ `0.8.md` §5.2 |
| HIGH | 5 citation verification | ✅ All [VERIFIED] (2026-05-15) |
| MEDIUM | Resolution-dependence bridge | ✅ `0.8.md` §3.1 |
| MEDIUM | Framework positioning vs. alternatives | ✅ `0.8.md` §5.2 |
| MEDIUM | Linguistic bridge | ✅ `0.8.md` §4.1 |
| MEDIUM | 7 objections + counterarguments | ✅ `0.8.md` §6 |
| MEDIUM | Bounded consilience (L1-L8) | ✅ `0.8.md` §4.3 |
| LOW | Epistemological limits | ✅ `0.8.md` §4.2 |
| LOW | Cosmological extension | ✅ `0.8.md` §3.3 |
| — | Document unification (0.3–0.6 → 0.8) | ✅ `0.8.md` |
| — | Math formatting audit | ✅ ALL CLEAN (7 files) |
| — | Reader testing (I1-I12 fixed) | ✅ |
| — | 7 documentation files finalized | ✅ |
| — | Branch renamed | ✅ `feature/tree-distance-cophenetic` |
