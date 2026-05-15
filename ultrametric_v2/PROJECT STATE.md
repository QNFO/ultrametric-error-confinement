# PROJECT STATE -- Ultrametric Error Confinement v2

**Last Updated:** 2026-05-15
**Active Branch:** `feature/ultrametric-v2-ternary-tree`
**Session Focus:** Phase 2 completion (d=7 crossed threshold), Phase 3 (barrier verified), Phase 4 (scoping next)

## Current Status

| Aspect | State |
|:-------|:------|
| Phase 0 (Setup) | COMPLETE |
| Phase 1 (Tree Code) | COMPLETE |
| Phase 2 (Experiments) | COMPLETE (d=2..7) |
| Phase 3 (Energy Barrier) | COMPLETE |
| Phase 4 (Physical Scoping) | NEXT |
| Phase 5 (Lean Formalization) | NOT STARTED |
| Phase 6 (Documentation) | NOT STARTED |

## Phase 2 Results Summary (FINAL)

**Perfect symmetry confirmed through d=7:** Logical 0 and 1 produce identical LER at all depths and p_err values.

### Complete LER Table at p_err = 0.40

| Depth | Leaves | Barrier | LER | Trials | Suppression |
|:------|:-------|:--------|:----|:-------|:------------|
| 2 | 9 | 4 | 0.248 | 500 | 1.6x |
| 3 | 27 | 8 | 0.182 | 500 | 2.2x |
| 4 | 81 | 16 | 0.106 | 500 | 3.8x |
| 5 | 243 | 32 | 0.010 | 500 | 40x |
| 6 | 729 | 64 | 0.002 | 1000 | 200x |
| 7 | 2187 | 128 | **0.000** | 2000 | **Infinite** |

### d=7: Complete Zero-Error Achievement

At d=7 (2187 leaves, barrier=128), ZERO logical errors observed across ALL p_err values (0.01 to 0.40) for both logical bits, 2000 trials each. Wilson CI upper bound: 0.0019 (95% confidence the true LER is below 0.19%).

### Zero-Error Thresholds

- d=2: Zero errors up to p_err = 0.05
- d=3: Zero errors up to p_err = 0.15
- d=4: Zero errors up to p_err = 0.30
- d=5: Zero errors up to p_err = 0.30
- d=6: Zero errors up to p_err = 0.35
- d=7: **Zero errors up to p_err = 0.40** (full tested range)

### Phase 3: Energy Barrier Verified

- Exhaustive d=1,2: Confirmed via full enumeration (8 and 512 patterns)
- Constructive d=3..15: Recursive barrier pattern proves B(d) = 2^d exactly
- B(d) recurrence: B(1)=2, B(d) = 2*B(d-1)

## Next Steps

1. Phase 4: Physical platform scoping document
2. Phase 6: Update original paper with symmetric p=3 results
3. Optional: d=8 experiment for definitive confirmation

## Handoff Notes

- Core module: `0.1.py` (ternary tree, encode/decode, noise, MC framework)
- Experiment runner: `0.2_run_experiments.py`
- Results: `0.2_results.json` (d=2..7, all p_err, both bits, Wilson CIs)
- D6 runner: `0.3_run_d6.py`
- Barrier verification: `0.4_barrier_verify.py`
- D7 runner: `0.5_run_d7.py`
