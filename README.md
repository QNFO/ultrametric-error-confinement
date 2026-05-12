# Computational Validation of Ultrametric Error Confinement

> **Thesis:** Bruhat-Tits tree quantum circuits demonstrate passive error confinement. Logical error rate drops to zero at depth 3+ for physical error rates up to 40%.

**Status:** Published on Zenodo (DOI: 10.5281/zenodo.20134944). Simulations complete (3 experiments). GitHub: github.com/QNFO/ultrametric-error-confinement.

---
## Quick Start
```bash
cd simulations/
python experiment_0a.py  # Error confinement
python experiment_0b.py  # Energy barrier scaling
python experiment_0c.py  # Strong triangle inequality verification
```

## Key Results
| Experiment | Finding |
|:-----------|:--------|
| **0A** | Tree LER=0 at depth 3+; flat LER=1-15% |
| **0B** | Barrier = 2^d, verified d=2,3; analytic to d=10 |
| **0C** | 0 violations in 15,000 trials across p=2,3,5 |

*All experiments reproducible with Python 3.8+ and zero external dependencies.*
