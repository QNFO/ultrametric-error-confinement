# Computational Validation of Ultrametric Error Confinement

> **Thesis:** Bruhat-Tits tree quantum circuits demonstrate passive error confinement. Logical error rate drops to zero at depth 3+ for physical error rates up to 40%.

**Status:** Paper drafted (6 sections, 19 references). Simulations complete. Target: arXiv / Zenodo.

---
## Quick Start
```bash
cd simulations/
python experiment_0a.py  # Error confinement
python experiment_0b.py  # Energy barrier scaling
```

## Key Results
| Experiment | Finding |
|:-----------|:--------|
| **0A** | Tree LER=0 at depth 3+; flat LER=1-15% |
| **0B** | Barrier = 2^d, verified d=2,3 |
| **STI** | 0 violations in 15,000 trials across p=2,3,5 |

*Extracted from QWAV (2026-05-12).*
