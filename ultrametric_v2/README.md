# README -- Ultrametric Error Confinement v2 (CLOSED)

**Symmetric, computationally validated ultrametric error confinement architecture using ternary Bruhat-Tits trees (p=3), with exponential error suppression and physical implementation pathway.**

## Project Status: COMPLETE (2026-05-16)

All phases complete. Companion paper (0.8.md) finalized. FAQ (0.9.md) for quick reference.

## Key Result

At depth 7 (2,187 leaves, barrier 128): **ZERO logical errors** across 36,000 total trials at all physical error rates up to 40%. Both logical states protected identically. Perfect symmetry confirmed at all 63 data points.

## Definitive Deliverables

| File | Content |
|:-----|:--------|
| 0.1.py | Ternary tree module |
| 0.2_results.json | Complete experiment data (d=2..8) |
| 0.4_barrier_verify.py | Exhaustive + constructive barrier proof |
| 0.6.md | Physical platform scoping |
| 0.7.md | Outreach whitepaper |
| **0.8.md** | **Definitive companion paper (8 sections + FAQ appendix)** |
| **0.9.md** | **Quick Reference FAQ** |

## Companion Paper

This project is a companion to: Quni-Gudzinas, "Computational Validation of Ultrametric Error Confinement in Bruhat-Tits Tree Quantum Circuits," Zenodo, 2026. DOI: 10.5281/zenodo.20134944.

- **Fixes:** p=2 asymmetry — B(b=1)=2 constant at all depths (only bit 0 was protected)
- **Adds:** p=3 symmetric architecture, bidirectional validation (d=2..8), physical pathway (neutral atoms, d=3, 40 atoms)
- **Explains:** Why primes, why p=3, why not p=5/7 (exhaustive verification + trade-off tables)

## Constraints

- No active error correction (passive encoding)
- Python standard library only (no external deps)
- Symmetric by design (both logical states tested independently)
- Simulation-first (computational evidence before formal proof)
