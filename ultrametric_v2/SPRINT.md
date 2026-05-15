# SPRINT — Ultrametric Error Confinement v2

**Sprint:** 1 — Ternary Tree Implementation & Validation
**Start:** 2026-05-15
**Target:** 2-3 days

## Tasks

| # | Task | Status | Priority |
|:--|:-----|:-------|:---------|
| 0.1 | Create project directory | ✅ DONE | P0 |
| 0.2 | Git setup & feature branch | ✅ DONE | P0 |
| 0.3 | Mandatory documentation files | 🔄 IN PROGRESS | P0 |
| 0.5 | .gitignore for Python | ⬜ TODO | P1 |
| 1.1 | `build_tree(depth, p=3)` — ternary tree construction | ⬜ TODO | P0 |
| 1.2 | Encode logical bit → all leaves | ⬜ TODO | P0 |
| 1.3 | Decode: bottom-up majority vote | ⬜ TODO | P0 |
| 1.4 | Noise injection (i.i.d. bit-flip) | ⬜ TODO | P1 |
| 1.5 | Monte Carlo trial framework | ⬜ TODO | P1 |
| 1.6 | Unit tests (tree structure, majority, encode/decode roundtrip) | ⬜ TODO | P1 |
| 2.1 | Run experiments: d=2..5, p_err=0.01..0.40 | ⬜ TODO | P0 |
| 2.2 | Compute LER and Wilson CIs | ⬜ TODO | P1 |
| 2.3 | Plots: LER vs p_err, suppression vs depth | ⬜ TODO | P1 |
| 3.1 | Analytic barrier formula: $B(d) = 2^d$ | ⬜ TODO | P1 |
| 3.2 | Exhaustive verification for d≤4 | ⬜ TODO | P2 |

## Blockers

None.

## Notes

- Root degree = 3 (not p+1=4) to avoid tie-breaking — this is a deliberate deviation from strict Bruhat-Tits tree definition.
- All internal nodes have exactly 3 children.
- Majority = 2 of 3 — no ties possible except at root with 4 children, which we've eliminated.
