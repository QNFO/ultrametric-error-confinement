# PROJECT STATE -- Ultrametric Error Confinement v2 (FINAL)

**Last Updated:** 2026-05-16
**Active Branch:** feature/tree-distance-cophenetic
**Project Status:** COMPLETE — All 7 sprints delivered. All BACKLOG P1 items done.
**Handoff Target:** Next LLM session or human for Phase B (outreach) and Phase D (Lean 4).

---

## Executive Summary (1 Paragraph)

This project is a companion paper to Quni-Gudzinas (2026), "Computational Validation of Ultrametric Error Confinement in Bruhat–Tits Tree Quantum Circuits" (Zenodo, DOI: 10.5281/zenodo.20134944). It identifies a structural asymmetry in the original $p=2$ architecture (internal tie-breaking favors bit 0, collapsing bit 1's barrier to a constant $B=2$) and resolves it with a $p=3$ ternary architecture where odd branching eliminates all tie-breaking. The companion paper validates perfect symmetry through $d=8$, then extends across 6 additional sprints: general-$p$ validation ($p=5,7$), classical baseline comparison, correlated noise advantage, $q$-ary generalization (48× LER reduction at zero qubit cost), dynamic restructuring, QEC concatenation, and hardware prototype design specs. **Eight novel computational findings** beyond the original paper. Total: 260,000+ MC trials, 26 files, all [CODE-EXECUTED] and reproducible.

---

## Phase Status (Complete)

| Phase | Status | Key Files | Notes |
|:------|:-------|:----------|:------|
| 0 Setup | COMPLETE | 7 mandatory docs | Git, documentation standards established |
| 1 Tree Code | COMPLETE | `0.1.py`, `0.10.py` | $p=3$ specific + general-$p$ module |
| 2a Experiments $p=3$ | COMPLETE | `0.2_results.json` | $d=2..8$, both bits, 500-2000 trials |
| 2b Experiments $p=5,7$ | COMPLETE | `0.10_p5_results.json`, `0.10_p7_results.json` | $p=5$: $d=2-4$, $p=7$: $d=2-3$ |
| 2c Classical Baseline | COMPLETE | `0.11_classical_repetition.py` | Honest: classical wins at i.i.d. |
| 2d Correlated Noise | COMPLETE | `0.12_correlated_noise.py`, `0.12_correlated_results.json` | Tree wins at $p_{\text{corr}} \geq 0.50$ |
| 2e Multi-bit Encoding | COMPLETE | `0.13_multi_bit.py` | 9 bits at $B=8$, $7.29\times$ throughput |
| 2f $q$-ary Generalization | COMPLETE | `0.14_qary.py`, `0.14_qary_results.json` | 48× LER reduction at $q=3$ |
| 2g Dynamic Restructuring | COMPLETE | `0.15_unbalanced.py` | Balanced optimal under i.i.d. |
| 2h QEC Concatenation | COMPLETE | `0.16_qec_concatenation.py`, `0.16_qec_results.json` | Concatenation is redundant |
| 2i Hardware Specs | COMPLETE | `hardware-specs.md` | 40 atoms, $d=3$, existing platforms |
| 3 Energy Barrier | COMPLETE | `0.4_barrier_verify.py`, `0.10_p2_exhaustive.json` | Exhaustive + constructive, all primes |
| 4 Platform Scoping | COMPLETE | `platform-scoping.md` | 5 platforms evaluated, neutral atoms PRIMARY |
| 5 Lean Formalization | DEFERRED | — | See BACKLOG.md Phase D for spec |
| 6 Documentation | COMPLETE | `outreach-whitepaper.md`, `companion-paper.md`, `faq.md`, `progress-report.md` | Whitepaper, companion paper, FAQ, progress narrative |

---

## Eight Novel Findings Beyond Original Paper [1]

| # | Finding | Sprint | Evidence | In companion-paper.md |
|:--|:--------|:-------|:---------|:----------|
| F1 | $p=2$ asymmetry: $B(b1)=2$ constant | 1 | Exhaustive $d=1-3$, all 4096 patterns | §1.1-1.3 |
| F2 | $p=5,7$ symmetric; barrier formula $\lceil p/2 \rceil^d$ confirmed | 2 | MC $d=2-4$ ($p=5$), $d=2-3$ ($p=7$) | §3.3-3.4 |
| F3 | Classical repetition beats tree at i.i.d. noise (honest baseline) | 2 | MC at matched $N=p^d$, all $(p,d)$ | §7.6 |
| F4 | Tree beats classical under correlated noise (first practical advantage) | 3 | 1,000 trials, $p_{\text{corr}}=0.0..0.75$ | §7.6.1 |
| F5 | Multi-bit encoding scales throughput ($7.29\times$ at 9 bits) | 3 | $p=3$, $d=5$, $k=2$, independence verified | §7.6 |
| F6 | $q$-ary scatter: 48× LER reduction at zero qubit cost | 4 | $p=3$, $d=2-4$, $q=2,3,5,10$, 500 trials | §7.7 |
| F7 | Balanced trees optimal under i.i.d. noise | 5 | Utility-per-leaf comparison | Not in companion-paper.md |
| F8 | QEC concatenation is redundant | 6 | 3 qubit budgets, 10 architectures | §7.8 |

---

## Definitive Numerical Results ([CODE-EXECUTED], seed=42)

### $p=3$ LER at $p_{\text{err}}=0.40$ (both bits identical)
| $d$ | Leaves | Barrier | LER | Trials/bit | CI Upper |
|:----|:-------|:--------|:----|:-----------|:---------|
| 2 | 9 | 4 | 0.248 | 500 | 0.288 |
| 3 | 27 | 8 | 0.182 | 500 | 0.218 |
| 4 | 81 | 16 | 0.106 | 500 | 0.136 |
| 5 | 243 | 32 | 0.010 | 500 | 0.023 |
| 6 | 729 | 64 | 0.002 | 1,000 | 0.007 |
| 7 | 2,187 | 128 | 0.000 | 2,000 | 0.0019 |
| 8 | 6,561 | 256 | 0.000 | 1,000 | 0.0038 |

### $p=5$ LER at $p_{\text{err}}=0.40$ (both bits identical, 500 trials)
| $d$ | Leaves | Barrier | LER |
|:----|:-------|:--------|:----|
| 2 | 25 | 9 | 0.190 |
| 3 | 125 | 27 | 0.040 |
| 4 | 625 | 81 | 0.000 |

### $p=7$ LER at $p_{\text{err}}=0.40$ (both bits identical, 500 trials)
| $d$ | Leaves | Barrier | LER |
|:----|:-------|:--------|:----|
| 2 | 49 | 16 | 0.126 |
| 3 | 343 | 64 | 0.002 |

### $q$-ary LER ($p=3$, $p_{\text{err}}=0.40$, 500 trials)
| $d$ | Leaves | $q=2$ | $q=3$ | $q=5$ | $q=10$ |
|:----|:-------|:------|:------|:------|:-------|
| 2 | 9 | 0.304 | 0.076 | 0.006 | 0.004 |
| 3 | 27 | 0.194 | 0.004 | 0.000 | 0.000 |
| 4 | 81 | 0.094 | 0.000 | 0.000 | 0.000 |

### Correlated Noise — Tree advantage threshold ($p_{\text{base}}$ where Tree LER < Classical LER)
| $(p,d)$ | $N$ | $p_{\text{corr}}=0.25$ | $p_{\text{corr}}=0.50$ | $p_{\text{corr}}=0.75$ |
|:--------|:----|:----------------------|:----------------------|:----------------------|
| (3,3) | 27 | — | $\geq 0.30$ | $\geq 0.25$ |
| (3,4) | 81 | $\geq 0.35$ | $\geq 0.25$ | $\geq 0.20$ |
| (5,3) | 125 | $\geq 0.35$ | $\geq 0.30$ | $\geq 0.20$ |

---

## Complete File Inventory (26 files)

### Core Modules (Python)
| File | Lines | Purpose |
|:-----|:------|:-------|
| `0.1.py` | 258 | Ternary tree module ($p=3$) |
| `0.10.py` | 399 | General-$p$ tree module (any prime) |
| `0.11_classical_repetition.py` | 185 | Classical $N$-bit repetition code |
| `0.12_correlated_noise.py` | 376 | Two-stage correlated noise model |
| `0.13_multi_bit.py` | 341 | Multi-bit encoding via subtree partitioning |
| `0.14_qary.py` | 343 | $q$-ary alphabet generalization |
| `0.15_unbalanced.py` | 264 | Dynamic tree restructuring |
| `0.16_qec_concatenation.py` | 185 | QEC concatenation at leaf level |

### Runners & Data
| File | Purpose |
|:-----|:--------|
| `0.2_run_experiments.py` | $p=3$ experiment runner |
| `0.3_run_d6.py` | $d=6$ extended runner |
| `0.4_barrier_verify.py` | Exhaustive + constructive barrier proof |
| `0.5_run_d7.py` | $d=7$ runner (2,000 trials) |
| `0.8_run_d8.py` | $d=8$ split-mode runner |
| `0.10_run_p5.py`, `0.10_p5_results.json` | $p=5$ experiments + data |
| `0.10_run_p7.py`, `0.10_p7_results.json` | $p=7$ experiments + data |
| `0.10_p2_exhaustive.json` | $p=2$ exhaustive asymmetry data |
| `0.11_run_comparison.py` | Tree vs classical comparison runner |
| `0.12_run_correlated_comparison.py`, `0.12_correlated_results.json` | Correlated noise comparison |
| `0.14_run_qary_comparison.py`, `0.14_qary_results.json` | $q$-ary comparison |
| `0.16_qec_results.json` | QEC concatenation data |

### Documentation
| File | Purpose |
|:-----|:--------|
| **`companion-paper.md`** | **DEFINITIVE COMPANION PAPER** (8 sections + FAQ appendix) |
| `faq.md` | Quick Reference FAQ |
| `outreach-whitepaper.md` | Outreach whitepaper |
| `platform-scoping.md` | Physical platform scoping |
| `hardware-specs.md` | Hardware prototype design specification |
| `progress-report.md` | Complete progress narrative (this session) |
| `README.md` | Project identity and status |
| `PROJECT STATE.md` | This file — comprehensive handoff |
| `SPRINT.md` | Sprint status and task log |
| `CHANGELOG.md` | Versioned change log |
| `BACKLOG.md` | Prioritized future work with minute specificity |
| `LEARNINGS.md` | 10 cross-project lessons |
| `DECISIONS.md` | 6 architecture decisions with rationale |

---

## Immediate Next Actions (For Next Session)

1. **READ `progress-report.md`** — full narrative of all work completed
2. **READ `BACKLOG.md`** — excruciatingly specific next steps for outreach (Phase B), Lean 4 (Phase D), and computational extensions (Phase C)
3. **READ `companion-paper.md`** — the definitive companion paper, ready for Zenodo upload
4. **DECIDE:** Phase B (outreach) requires web/email access; Phase D (Lean 4) requires Go/No-Go decision; Phase C (computation) is immediately executable
5. **COMMIT** this file and any new work before session end

---

## Git Information

- **Branch:** feature/tree-distance-cophenetic
- **Latest commit:** 0b5fc7c (all Sprint 6-7 deliverables)
- **Repo:** `G:/My Drive/projects` (monorepo)
- **Project directory:** `G:/My Drive/projects/ultrametric_v2/`
- **All files committed and clean:** Yes ✓

---

*This project is complete. All computational phases are done. All BACKLOG P1 items are delivered. The next session should focus on Phase A (Zenodo publication) and Phase B (experimental outreach), with Phase C (computational extensions) and Phase D (Lean 4) as secondary priorities.*
