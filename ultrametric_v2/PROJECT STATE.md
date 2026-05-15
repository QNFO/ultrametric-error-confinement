# PROJECT STATE -- Ultrametric Error Confinement v2

**Last Updated:** 2026-05-15
**Active Branch:** feature/ultrametric-v2-ternary-tree

## Phase Status

| Phase | Status | Key File |
|:------|:-------|:---------|
| 0 Setup | COMPLETE | 7 mandatory docs |
| 1 Tree Code | COMPLETE | 0.1.py |
| 2 Experiments | COMPLETE d=2..7, d=8 RUNNING | 0.2_results.json |
| 3 Energy Barrier | COMPLETE | 0.4_barrier_verify.py |
| 4 Platform Scoping | COMPLETE | 0.6.md |
| 5 Lean Formalization | OPTIONAL | -- |
| 6.1 Paper | COMPLETE | 0.8.md |
| 6.2 Whitepaper | COMPLETE | 0.7.md |

## d=8 Status: RUNNING (background)
- 6561 leaves, 9841 nodes, barrier B=256
- 2000 trials x 9 p_err x 2 bits = 36000 trials
- Expected time: ~10-12 minutes

## Full Content Files
0.1.py - Ternary tree module
0.2_results.json - All experiment data (d=2..7, merging d=8)
0.2_run_experiments.py - Experiment runner
0.3_run_d6.py - d=6 extended runner
0.4_barrier_verify.py - Barrier verification
0.5_run_d7.py - d=7 runner
0.6.md - Physical platform scoping
0.7.md - Outreach whitepaper
0.8.md - REVISED PAPER (symmetric p=3, AGP/Heydeman/Boettcher citations)
0.8_run_d8.py - d=8 runner
