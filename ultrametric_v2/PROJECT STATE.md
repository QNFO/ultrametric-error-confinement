'# PROJECT STATE -- Ultrametric Error Confinement v2 (CLOSED)

**Last Updated:** 2026-05-16
**Active Branch:** feature/tree-distance-cophenetic (renamed from feature/ultrametric-v2-ternary-tree)
**Project Status:** CLOSED — all phases complete, companion paper finalized

## Phase Status

| Phase | Status | Key File |
|:------|:-------|:---------|
| 0 Setup | COMPLETE | 7 mandatory docs |
| 1 Tree Code | COMPLETE | 0.1.py |
| 2 Experiments d=2..8 | COMPLETE | 0.2_results.json |
| 3 Energy Barrier | COMPLETE | 0.4_barrier_verify.py |
| 4 Platform Scoping | COMPLETE | 0.6.md |
| 5 Lean Formalization | DEFERRED (optional) | -- |
| 6 Documentation/Outreach | COMPLETE | 0.7.md, 0.8.md, 0.9.md |

## Definitive Results

### LER at p_err=0.40 (both bits, identical)
| Depth | Leaves | Barrier | LER | CI Upper |
|:------|:-------|:--------|:----|:---------|
| 2 | 9 | 4 | 0.248 | 0.288 |
| 3 | 27 | 8 | 0.182 | 0.218 |
| 4 | 81 | 16 | 0.106 | 0.136 |
| 5 | 243 | 32 | 0.010 | 0.023 |
| 6 | 729 | 64 | 0.002 | 0.007 |
| 7 | 2,187 | 128 | 0.000 | 0.0019 |
| 8 | 6,561 | 256 | 0.000 | 0.0038 |

### p=2 Asymmetry (Exhaustively Verified)
- p=2 b=0: B(d) = 2^d (exponential)
- p=2 b=1: B(d) = 2 (CONSTANT — internal tie-breaking collapses barrier)
- p=3 both bits: B(d) = 2^d (symmetric, exponential)

### p-Selection Rationale (in 0.8.md and 0.9.md)
- p must be prime (Bruhat-Tits tree over Q_p requires Z_p DVR)
- Strict BT always asymmetric (Theorem 1, §2.3)
- p=3: minimal symmetric (smallest odd prime, identical barrier exponent)
- p=5/7: stronger barriers, exponentially more qubits (trade-off in §3.3)

## Complete File Inventory
0.1.py — Ternary tree module (258 lines)
0.2_results.json — Complete experiment data (d=2..8, both bits, CIs)
0.2_run_experiments.py — Experiment runner
0.3_run_d6.py — d=6 extended runner
0.4_barrier_verify.py — Barrier proof (exhaustive + constructive)
0.5_run_d7.py — d=7 runner (2000 trials)
0.6.md — Physical platform scoping (5 platforms, neutral atoms primary)
0.7.md — Outreach whitepaper (2-page summary for experimentalists)
0.8.md — DEFINITIVE COMPANION PAPER (8 sections, 11 refs, FAQ appendix)
0.8_run_d8.py — d=8 runner (split-mode)
0.9.md — Quick Reference FAQ (one-liner for every question)

## Handoff Notes (For Next LLM Session)
- This project is CLOSED. All deliverables complete.
- Companion paper (0.8.md) is the definitive publication draft.
- FAQ (0.9.md) answers all p=2 vs p=3 vs p=5 questions.
- Original paper: ''Computational Validation of Ultrametric Error Confinement in Bruhat-Tits Tree Quantum Circuits'' (Zenodo, DOI: 10.5281/zenodo.20134944).
- Next logical steps for a new session: publish companion to Zenodo, contact experimental groups (see 0.7.md), or initiate Phase 5 (Lean 4 formalization).
