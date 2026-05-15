# PROJECT STATE -- Ultrametric Error Confinement v2

**Last Updated:** 2026-05-15
**Active Branch:** `feature/ultrametric-v2-ternary-tree`
**Session Focus:** Phase 0-2 complete, moving to Phase 3

## Current Status

| Aspect | State |
|:-------|:------|
| Phase 0 (Setup) | ✅ COMPLETE |
| Phase 1 (Tree Code) | ✅ COMPLETE |
| Phase 2 (Experiments) | ✅ COMPLETE |
| Phase 3 (Energy Barrier) | 🔄 NEXT |
| Phase 4 (Physical Scoping) | ⬜ NOT STARTED |
| Phase 5 (Lean Formalization) | ⬜ NOT STARTED |
| Phase 6 (Documentation) | ⬜ NOT STARTED |

## Phase 2 Results Summary

**Perfect symmetry confirmed:** Logical 0 and 1 produce identical LER at all (depth, p_err) combinations.

### Key Metrics at p_err = 0.40

| Depth | Leaves | Barrier | LER | Suppression |
|:------|:-------|:--------|:----|:------------|
| 2 | 9 | 4 | 0.248 | 1.6x |
| 3 | 27 | 8 | 0.182 | 2.2x |
| 4 | 81 | 16 | 0.106 | 3.8x |
| 5 | 243 | 32 | 0.010 | 40x |
| 6 | 729 | 64 | 0.002 | 200x |

### Zero-Error Thresholds (500 trials d<=5, 1000 trials d=6)

- d=2: Zero errors up to p_err = 0.05
- d=3: Zero errors up to p_err = 0.15
- d=4: Zero errors up to p_err = 0.30
- d=5: Zero errors up to p_err = 0.30
- d=6: Zero errors up to p_err = 0.35

### Success Criterion Assessment

Original target: LER < 1e-3 at p_err=0.40, d>=3.
- At d=3: LER=0.182 (far above target)
- At d=5: LER=0.010 (above target)
- At d=6: LER=0.002 (close, CI upper bound 0.0073)
- At d>=7: projected below 1e-3 (barrier=128)

## Next Steps

1. Phase 3: Exhaustive energy barrier verification for d<=4
2. Consider running d=7 to cross the 1e-3 threshold
3. Begin Phase 4 scoping

## Handoff Notes

- Core module: `0.1.py` (ternary tree, encode/decode, noise, MC framework)
- Experiment runner: `0.2_run_experiments.py`
- Results: `0.2_results.json` (all depths, both bits, Wilson CIs)
- D6 runner: `0.3_run_d6.py`
