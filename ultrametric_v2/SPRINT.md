# SPRINT -- Ultrametric Error Confinement v2

**Sprint:** 3 — Correlated Noise & Advanced Encoding
**Start:** 2026-05-16
**Status:** ACTIVE

## Sprint 3 Tasks

| # | Task | Status |
|:--|:-----|:-------|
| 3.1 | Correlated noise model — spatially clustered bit-flip errors | [x] 2026-05-16 |
| 3.2 | Tree vs classical comparison under correlated noise | [x] 2026-05-16 |
| 3.3 | Multi-bit logical encoding (one bit per subtree) | [ ] |
| 3.4 | Update 0.8.md with correlated noise results | [x] 2026-05-16 |

## Sprint 3 Key Results (so far)

- **Correlated noise model:** Two-stage process — i.i.d. baseline + neighbor-flip correlation
- **Tree advantage confirmed:** Under correlated noise, tree LER < classical LER at high $p_{\text{corr}}$
- **Three scaling trends:** Higher $p_{\text{corr}}$, higher $d$, higher $p$ all favor the tree
- **Mechanism:** Hierarchical voting contains clustered errors within subtrees
- **0.8.md §7.6.1 added** with crossover tables and physical interpretation

## Sprint 2 (Complete)

| # | Task | Status |
|:--|:-----|:-------|
| 2.1 | General-p tree module (0.10.py) | [x] 2026-05-16 |
| 2.2 | p=5 exhaustive barrier verification (d=1) | [x] 2026-05-16 |
| 2.3 | p=5 MC experiments d=2-4 | [x] 2026-05-16 |
| 2.4 | p=7 exhaustive barrier verification (d=1) | [x] 2026-05-16 |
| 2.5 | p=7 MC experiments d=2-3 | [x] 2026-05-16 |
| 2.6 | Update 0.8.md §3.3 with validation data | [x] 2026-05-16 |
| 2.7 | Classical repetition code baseline | [x] 2026-05-16 |

## Sprint 1 (Complete)

All phases done. See earlier entries.
