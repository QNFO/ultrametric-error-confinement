# DECISIONS -- Ultrametric Error Confinement v2

## D1: Ternary Tree (Root Degree = 3) Instead of Strict Bruhat-Tits (p+1)
- **Date:** 2026-05-15
- **Decision:** Regular p-ary tree (all nodes have p children), not strict BT (root p+1).
- **Rationale:** The p+1 rule ALWAYS creates asymmetry (Theorem 1 in 0.8.md §2.3). For p=2: ties at internal level. For p>=3: ties at root. Regular p-ary eliminates ties for all odd p.
- **Status:** FINAL — justified in 0.8.md §3.1.

## D2: p=3 Only (Not Parameterized)
- **Date:** 2026-05-15
- **Decision:** Primary architecture uses p=3 specifically.
- **Rationale:** Smallest odd prime — minimal qubit overhead, identical barrier exponent (2^d) as p=2(b0). All odd p work symmetrically; p=3 is the minimal choice.
- **Status:** FINAL — rationale in 0.8.md §3.2, trade-off in §3.3.

## D3: No Virtual Environment
- **Date:** 2026-05-15
- **Decision:** System Python 3.10+, no venv. Only standard library + pytest.
- **Status:** FINAL.

## D4: Companion Paper Positioning
- **Date:** 2026-05-16
- **Decision:** 0.8.md is a companion to Quni-Gudzinas (2026, DOI: 10.5281/zenodo.20134944), NOT a replacement.
- **Rationale:** Original identified the mechanism. Companion fixes asymmetry, adds bidirectional validation, extends depths, adds physical scoping.
- **Status:** FINAL.

## D5: FAQ as Standalone File
- **Date:** 2026-05-16
- **Decision:** FAQ saved as both appendix to 0.8.md AND standalone 0.9.md.
- **Rationale:** Standalone file allows quick sharing without sending the full paper.
- **Status:** FINAL.

## D6: Higher p (5, 7, 11...) Deferred
- **Date:** 2026-05-16
- **Decision:** No simulations for p=5,7 beyond d=1 exhaustive. Trade-off documented in 0.8.md §3.3.
- **Rationale:** p=5 at d=7 needs 78K leaves vs 2K for p=3. Worth revisiting if qubit scaling improves.
- **Status:** DEFERRED.
