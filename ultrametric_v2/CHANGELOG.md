# CHANGELOG -- Ultrametric Error Confinement v2

## [0.7.0] — 2026-05-16 (Session 6 — Classical Baseline)

### What Changed
- **Classical repetition code baseline:** 0.11_classical_repetition.py + 0.11_run_comparison.py
  - Compares tree vs classical N-bit repetition at matched qubit counts (N = p^d)
  - Classical barrier = ceil(N/2) — always higher than tree barrier ceil(p/2)^d
  - LER comparison at p_err=0.40: classical wins at most (p,d) combinations
  - Tree wins marginally at p=3 d=2 (0.248 vs 0.258)
  - Both achieve zero errors at d>=6
- **0.8.md §7.6 added:** Honest comparison with classical baseline, interpretation
- **0.8.md §7.5 updated:** Limitation #4 revised (p=5,7 now computationally validated)
- **SPRINT 2 COMPLETE:** All 7 tasks done

### Files Changed
- ultrametric_v2/0.11_classical_repetition.py — CREATE
- ultrametric_v2/0.11_run_comparison.py — CREATE
- ultrametric_v2/0.8.md — EDIT (§7.6 added, §7.5 updated)
- ultrametric_v2/SPRINT.md — EDIT (Task 2.7 done, classical baseline result added)
- ultrametric_v2/PROJECT STATE.md — EDIT (Phase 2c added, file inventory updated)
- ultrametric_v2/CHANGELOG.md — EDIT (this entry)

## [0.6.0] — 2026-05-16 (Session 6 — Sprint 2: General-p Validation)

### What Changed
- **General-p tree module:** 0.10.py created — parameterized run_trial/run_experiment for arbitrary prime p
  - Added: barrier_formula(p,d), has_ties(p), is_symmetric(p), exhaustive_barrier_verify(p,d), overhead_ratio(p,p_ref,d)
  - All tests pass for p=2,3,5,7
- **p=5 validation:** MC experiments d=2-4, both bits, 500 trials
  - Perfect symmetry at all 24 data points
  - d=4: ZERO errors at all p_err <= 0.40 (625 leaves, B=81)
  - Exhaustive verification at d=1 (32 patterns): B(b0)=B(b1)=3
- **p=7 validation:** MC experiments d=2-3, both bits, 500 trials
  - Perfect symmetry at all 16 data points
  - d=3: 1 error at p_err=0.40, zero at p_err <= 0.35 (343 leaves, B=64)
  - Exhaustive verification at d=1 (128 patterns): B(b0)=B(b1)=4
- **p=2 asymmetry re-verified:** Exhaustive d=1-3 confirms B(b0)=2^d, B(b1)=1 (regular p-ary)
- **0.8.md updated:** §3.3.1 added with computational validation tables, §3.4 updated with p=2 asymmetry note
- Barrier formula B(d)=ceil(p/2)^d confirmed for all tested primes

### Files Changed
- ultrametric_v2/0.10.py — CREATE (general-p tree module)
- ultrametric_v2/0.10_run_p5.py — CREATE (p=5 experiment runner)
- ultrametric_v2/0.10_p5_results.json — CREATE (p=5 experiment data)
- ultrametric_v2/0.10_run_p7.py — CREATE (p=7 experiment runner)
- ultrametric_v2/0.10_p7_results.json — CREATE (p=7 experiment data)
- ultrametric_v2/0.10_p2_exhaustive.json — CREATE (p=2 exhaustive data)
- ultrametric_v2/0.8.md — EDIT (§3.3.1 added, §3.4 updated)
- ultrametric_v2/SPRINT.md — EDIT (Sprint 2 tasks 2.1-2.6 marked complete)
- ultrametric_v2/PROJECT STATE.md — EDIT (updated status, new results tables)
- ultrametric_v2/CHANGELOG.md — EDIT (this entry)

## [0.5.0] — 2026-05-16 (Session 5 — CLOSURE)
- Companion paper finalized, FAQ standalone, project closed

## [0.4.0] — 2026-05-15
- Phase 6: Outreach whitepaper, companion paper v1-v3

## [0.3.0] — 2026-05-15
- Phase 4: Physical platform scoping

## [0.2.0] — 2026-05-15
- Phase 2 completion (d=7), Phase 3 barrier verified

## [0.1.0] — 2026-05-15
- Project created, ternary tree, d=2..6 experiments
