# CHANGELOG -- Ultrametric Error Confinement v2

## [1.0.0] — 2026-05-16 — PROJECT COMPLETE

### Final Status
**All 7 sprints delivered. All BACKLOG P1 items complete. Project ready for publication and outreach.**

### Cumulative Deliverables (26 files)
- 8 Python modules (`0.1.py` through `0.16_qec_concatenation.py`)
- 8 data files (JSON results for $p=3$, $p=5$, $p=7$, $p=2$ exhaustive, correlated noise, $q$-ary, QEC concatenation)
- 6 runner scripts
- 7 documentation files (`0.6.md` through `0.9.md`, `0.17_hardware_specs.md`, `0.18_progress_report.md`, `README.md`)
- 7 mandatory project management files (`PROJECT STATE.md`, `SPRINT.md`, `CHANGELOG.md`, `BACKLOG.md`, `LEARNINGS.md`, `DECISIONS.md`, `.gitignore`)

### Eight Novel Findings Beyond Original Paper [1]
1. $p=5,7$ symmetric — barrier formula $\lceil p/2 \rceil^d$ confirmed computationally
2. Classical repetition beats tree at i.i.d. noise (honest baseline)
3. Tree beats classical under correlated noise (first practical advantage — hierarchical voting contains clustered errors)
4. Multi-bit encoding scales throughput ($7.29\times$ at 9 bits, independence verified)
5. $q$-ary scatter achieves 48× LER reduction at zero additional qubit cost (alkali/alkaline-earth hyperfine levels)
6. Balanced trees optimal under i.i.d. noise (dynamic restructuring provides no benefit)
7. QEC concatenation is redundant (tree IS already a hierarchical repetition code)
8. Hardware prototype: 40 atoms, $d=3$, existing neutral atom platforms, no modifications required

### Total Computational Footprint
- ~260,000 Monte Carlo trials
- 4,500+ lines of Python (standard library only, seed=42)
- Exhaustive enumeration up to $2^9 = 512$ patterns ($p=3$, $d=2$)
- Constructive barrier proof through $d=15$
- Deepest depth: $d=8$ (6,561 leaves, $p=3$)
- Highest prime: $p=7$ ($d=3$, 343 leaves)
- Largest $q$: $q=10$ ($d=4$, 81 leaves)

---

## [0.9.0] — 2026-05-16 — q-ary Generalization (Sprint 4)
Created `0.14_qary.py`, `0.14_qary_results.json`, `0.14_run_qary_comparison.py`. q-ary alphabet generalization with plurality voting. Random-scatter mechanism: errors divide across $q-1$ wrong symbols. $q=3$: 48× LER reduction vs binary at zero qubit cost. $q=5$: zero errors at all tested depths. Added §7.7 to `0.8.md`.

## [0.8.0] — 2026-05-16 — Correlated Noise (Sprint 3)
Created `0.12_correlated_noise.py`, `0.12_correlated_results.json`, `0.12_run_correlated_comparison.py`. Two-stage correlated noise model (i.i.d. baseline + neighbor-flip). Tree vs classical under correlated noise: tree wins at high $p_{\text{corr}}$. Added §7.6.1 to `0.8.md`.

## [0.7.0] — 2026-05-16 — Classical Baseline (Sprint 2, Task 2.7)
Created `0.11_classical_repetition.py`, `0.11_run_comparison.py`. Classical $N$-bit repetition code comparison. Classical always wins at matched qubit counts (i.i.d.). Honest result documented in §7.6.

## [0.6.0] — 2026-05-16 — General-p Validation (Sprint 2, Tasks 2.1-2.6)
Created `0.10.py` (general-$p$ tree), `0.10_p5_results.json`, `0.10_p7_results.json`, `0.10_p2_exhaustive.json`. Validated $p=5$ ($d=2-4$) and $p=7$ ($d=2-3$). Perfect symmetry confirmed. Barrier formula $\lceil p/2 \rceil^d$ confirmed for all tested primes. $p=2$ regular $p$-ary: $B(b1)=1$ (worse than strict BT).

## [0.5.0] — 2026-05-16 — FINAL CLOSURE (Session 5)
Companion paper finalized. FAQ standalone (`0.9.md`). All 7 mandatory documentation files updated. Project marked closed (later reopened for Sprints 2-7).

## [0.4.0] — 2026-05-15 — Phase 6: Documentation
Outreach whitepaper (`0.7.md`), companion paper v1-v3 (`0.8.md`).

## [0.3.0] — 2026-05-15 — Phase 4: Platform Scoping
Physical platform scoping (`0.6.md`). 5 platforms evaluated. Neutral atoms PRIMARY.

## [0.2.0] — 2026-05-15 — Phase 2-3: Experiments and Barrier
$d=7$ completed. Barrier verified (exhaustive $d=1,2$, constructive through $d=15$).

## [0.1.0] — 2026-05-15 — Phase 1: Project Creation
Ternary tree module (`0.1.py`), $d=2..6$ experiments, 7 mandatory documentation files.
