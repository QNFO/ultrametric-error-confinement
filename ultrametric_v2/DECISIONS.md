# DECISIONS — Ultrametric Error Confinement v2

## D1: Ternary Tree (Root Degree = 3) Instead of Strict Bruhat-Tits (p+1)
- **Date:** 2026-05-15
- **Decision:** Regular ternary tree (root degree=3), not strict Bruhat-Tits.
- **Rationale:** Root with 4 children creates 2-vs-2 tie in majority voting requiring tie-breaker, breaking symmetry.
- **Trade-off:** Not a strict Bruhat-Tits tree but ultrametric properties preserved.
- **Impact:** Document as ternary ultrametric tree, not Bruhat-Tits tree.

## D2: p=3 Only (Not Parameterized)
- **Date:** 2026-05-15
- **Decision:** Initial implementation targets p=3 specifically.
- **Rationale:** Simplest odd branching factor eliminating ties. Core phenomena independent of p.

## D3: No Virtual Environment
- **Date:** 2026-05-15
- **Decision:** Skip venv; use system Python 3.10+.
- **Rationale:** Only standard library + pytest. No dependency conflicts.
