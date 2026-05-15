# SPRINT -- Ultrametric Error Confinement v2

**Sprint:** 2 — General-p Architecture & Higher-Prime Validation
**Start:** 2026-05-16
**Status:** ACTIVE

## Sprint 2 Tasks

| # | Task | Status |
|:--|:-----|:-------|
| 2.1 | General-p tree module (0.10.py) — refactor run_trial/run_experiment to accept p parameter | [x] 2026-05-16 |
| 2.2 | p=5 exhaustive barrier verification (d=1, all 32 patterns) | [x] 2026-05-16 |
| 2.3 | p=5 MC experiments d=2-4 (both bits, 500 trials, LER validation) | [x] 2026-05-16 |
| 2.4 | p=7 exhaustive barrier verification (d=1, all 128 patterns) | [x] 2026-05-16 |
| 2.5 | p=7 MC experiments d=2-3 (both bits, 500 trials, LER validation) | [x] 2026-05-16 |
| 2.6 | Update 0.8.md §3.3 with computational validation data for p=5,7 | [x] 2026-05-16 |
| 2.7 | Classical repetition code baseline comparison | [x] 2026-05-16 |

## Sprint 2 Key Results

- **p=5 symmetry confirmed:** Both bits produce identical LER at all 24 data points
- **p=5 d=4:** ZERO errors at all p_err <= 0.40 (500 trials, 625 leaves, B=81)
- **p=7 symmetry confirmed:** Both bits produce identical LER at all 16 data points  
- **p=7 d=3:** 1 error at p_err=0.40, zero errors at p_err <= 0.35 (500 trials, 343 leaves, B=64)
- **Barrier formula B(d)=ceil(p/2)^d confirmed** for all tested primes
- **Classical baseline:** Classical repetition code has higher absolute barrier (N/2 vs 2^d) and lower LER at matched qubit counts for most regimes. Tree's value is geometric/theoretical, not raw error-correction efficiency (§7.6).
- **Regular p=2:** B(b1)=1 (even worse than strict BT B(b1)=2) — confirmed exhaustively d=1-3

## Sprint 1 (Complete)

| # | Task | Status |
|:--|:-----|:-------|
| 0.x | Phase 0: Setup, git, 7 mandatory docs | DONE |
| 1.x | Phase 1: Ternary tree code (0.1.py) | DONE |
| 2.x | Phase 2: MC experiments d=2..8, both bits | DONE |
| 3.x | Phase 3: Energy barrier verified (exhaustive+constructive) | DONE |
| 4.x | Phase 4: Physical platform scoping (0.6.md) | DONE |
| 5.x | Phase 5: Lean 4 formalization | DEFERRED |
| 6.x | Phase 6: Whitepaper (0.7.md) + Companion Paper (0.8.md) + FAQ (0.9.md) | DONE |
