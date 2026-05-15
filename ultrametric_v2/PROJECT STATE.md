# PROJECT STATE -- Ultrametric Error Confinement v2 (ACTIVE)

**Last Updated:** 2026-05-16
**Active Branch:** feature/tree-distance-cophenetic
**Project Status:** ACTIVE — Sprint 3 complete, all BACKLOG P1 items done

## Phase Status

| Phase | Status | Key File |
|:------|:-------|:---------|
| 0 Setup | COMPLETE | 7 mandatory docs |
| 1 Tree Code | COMPLETE | 0.1.py (p=3), 0.10.py (general-p) |
| 2 Experiments d=2..8 (p=3) | COMPLETE | 0.2_results.json |
| 2b Experiments p=5,7 | COMPLETE | 0.10_p5_results.json, 0.10_p7_results.json |
| 2c Classical Baseline | COMPLETE | 0.11_classical_repetition.py |
| 2d Correlated Noise | COMPLETE | 0.12_correlated_noise.py |
| 2e Multi-bit Encoding | COMPLETE | 0.13_multi_bit.py |
| 3 Energy Barrier | COMPLETE | 0.4_barrier_verify.py, 0.10_p2_exhaustive.json |
| 4 Platform Scoping | COMPLETE | 0.6.md |
| 5 Lean Formalization | DEFERRED (optional) | -- |
| 6 Documentation/Outreach | COMPLETE | 0.7.md, 0.8.md, 0.9.md |

## Key Findings Beyond Original Paper

1. **p=5 and p=7 symmetric** (computationally validated, Sprint 2)
2. **Classical repetition outperforms tree at i.i.d. noise** (honest baseline, Task 2.7)
3. **Tree outperforms classical under correlated noise** (Sprint 3 — first practical advantage)
4. **Multi-bit encoding increases throughput** (9 bits at B=8 achieve 7.29x single-bit throughput)

## Next Actions (Ranked)
- P1: Publish companion to Zenodo (0.8.md ready, needs DOI)
- P2: Contact experimental groups (see 0.7.md)
- P3: q-ary alphabet generalization (BACKLOG P1)
- P4: Run p=5 d=5 (3,125 leaves, B=243)
- P5: Lean 4 formalization

## Definitive Results (All CODE-EXECUTED, seed=42)

### p=3 LER at p_err=0.40 (both bits, identical)
| Depth | Leaves | Barrier | LER | CI Upper |
|:------|:-------|:--------|:----|:---------|
| 2 | 9 | 4 | 0.248 | 0.288 |
| 3 | 27 | 8 | 0.182 | 0.218 |
| 4 | 81 | 16 | 0.106 | 0.136 |
| 5 | 243 | 32 | 0.010 | 0.023 |
| 6 | 729 | 64 | 0.002 | 0.007 |
| 7 | 2,187 | 128 | 0.000 | 0.0019 |
| 8 | 6,561 | 256 | 0.000 | 0.0038 |

### p=5 LER at p_err=0.40 (both bits, identical, 500 trials)
| Depth | Leaves | Barrier | LER | CI Upper |
|:------|:-------|:--------|:----|:---------|
| 2 | 25 | 9 | 0.190 | 0.227 |
| 3 | 125 | 27 | 0.040 | 0.061 |
| 4 | 625 | 81 | 0.000 | 0.0076 |

### p=7 LER at p_err=0.40 (both bits, identical, 500 trials)
| Depth | Leaves | Barrier | LER | CI Upper |
|:------|:-------|:--------|:----|:---------|
| 2 | 49 | 16 | 0.126 | 0.158 |
| 3 | 343 | 64 | 0.002 | 0.011 |

### p=2 Asymmetry (Regular p-ary, Exhaustively Verified d=1-3)
- p=2 b=0: B(d) = 2^d (exponential)
- p=2 b=1: B(d) = 1 (CONSTANT at all depths — single error propagates)

### Cross-p Comparison at d=3, p_err=0.40
| p | Leaves | Barrier | LER | Overhead vs p=3 |
|:--|:-------|:--------|:----|:----------------|
| 3 | 27 | 8 | 0.182 | 1.0x (baseline) |
| 5 | 125 | 27 | 0.040 | 4.6x |
| 7 | 343 | 64 | 0.002 | 12.7x |

## Complete File Inventory
0.1.py — Ternary tree module (p=3)
0.10.py — General-p tree module (any prime p)
0.2_results.json — p=3 experiment data (d=2..8, both bits, CIs)
0.2_run_experiments.py — p=3 experiment runner
0.3_run_d6.py — p=3 d=6 extended runner
0.4_barrier_verify.py — Barrier proof (exhaustive + constructive)
0.5_run_d7.py — p=3 d=7 runner
0.6.md — Physical platform scoping
0.7.md — Outreach whitepaper
0.8.md — DEFINITIVE COMPANION PAPER (updated with p=5,7 data)
0.8_run_d8.py — p=3 d=8 runner
0.9.md — Quick Reference FAQ
0.10_run_p5.py — p=5 experiment runner
0.10_p5_results.json — p=5 experiment data
0.10_run_p7.py — p=7 experiment runner
0.10_p7_results.json — p=7 experiment data
0.10_p2_exhaustive.json — p=2 exhaustive asymmetry data
0.11_classical_repetition.py — Classical repetition code module
0.11_run_comparison.py — Tree vs classical comparison runner

## Next Actions (Ranked)
- P1: Classical repetition code baseline comparison (Task 2.7)
- P2: Publish companion to Zenodo
- P3: Contact experimental groups (see 0.7.md)
- P4: Run p=5 d=5 (3125 leaves, B=243)
- P5: Lean 4 formalization
