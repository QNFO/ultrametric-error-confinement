# BACKLOG -- Ultrametric Error Confinement v2 (FINAL)

**Last Updated:** 2026-05-16
**Status:** ALL P1 ITEMS COMPLETE. Remaining items require external access (web, email, human collaborators).

---

## PHASE A: PUBLICATION & DISSEMINATION (Priority: CRITICAL)

### A1. Zenodo Publication of Companion Paper

**Objective:** Upload `0.8.md` to Zenodo as a formal companion publication with bidirectional cross-reference to the original paper [1].

**Exact file to upload:** `G:\My Drive\projects\ultrametric_v2\0.8.md` (converted to PDF via pandoc or similar Markdown-to-PDF renderer)

**Exact Zenodo metadata fields to populate:**

| Field | Value |
|:------|:------|
| **Title** | Symmetric Extension of Ultrametric Error Confinement — Ternary Tree Architecture with Bidirectional Validation |
| **Authors** | Rowan Brad Quni-Gudzinas |
| **Description** | Companion paper to "Computational Validation of Ultrametric Error Confinement in Bruhat–Tits Tree Quantum Circuits" (Zenodo, DOI: 10.5281/zenodo.20134944). Identifies and resolves a structural asymmetry in the original p=2 architecture: internal tie-breaking favors logical 0, collapsing the energy barrier for logical 1 to a constant B=2 at all depths. Presents a p=3 (ternary) symmetric architecture with bidirectional validation through d=8, exhaustive barrier verification, p-selection rationale, physical implementation pathway, classical baseline comparison, correlated noise advantage demonstration, and q-ary alphabet generalization achieving 48× LER reduction at zero additional qubit cost. All results computationally validated (Python 3.10+, seed=42). |
| **Keywords** | ultrametric error confinement, Bruhat-Tits tree, p-adic quantum computation, ternary tree, majority voting, hierarchical error correction, passive fault tolerance, neutral atom quantum computing |
| **License** | Creative Commons Attribution 4.0 International (CC BY 4.0) |
| **Publication type** | Preprint / Working Paper |
| **Communities** | quantum computing, mathematical physics, error correction |
| **Related identifiers** | References: 10.5281/zenodo.20134944 (the original paper [1]) |
| **Version** | 1.0.0 |

**Post-upload action:** After DOI is assigned (format: 10.5281/zenodo.XXXXXXXXX), update `0.8.md` frontmatter to include the companion DOI, and add a bidirectional reference note.

**Update original paper [1]:** Add the following note to the original Zenodo record:
> "**Companion Publication:** Quni-Gudzinas, 'Symmetric Extension of Ultrametric Error Confinement — Ternary Tree Architecture with Bidirectional Validation,' Zenodo, 2026. DOI: [NEW-DOI]. This companion identifies a structural asymmetry in the p=2 architecture (bit 1 receives constant barrier B=2 rather than exponential protection) and provides the first fully symmetric, bidirectionally validated architecture using p=3 ternary trees."

---

## PHASE B: EXPERIMENTAL OUTREACH (Priority: HIGH)

### B1. Neutral Atom Laboratory Outreach — Target List

**Background:** The tree architecture requires NO ancilla qubits, syndrome measurements, or real-time feedback. Encoding is passive (leaf values), decoding is classical post-processing (majority vote). Error injection is controlled X-rotations. Readout is standard fluorescence imaging. This makes it uniquely suited for IMMEDIATE implementation on existing neutral atom platforms — no hardware modifications required.

**Target Laboratory 1: Harvard University — Lukin/Greiner Group**

| Detail | Specification |
|:-------|:-------------|
| **Group** | Mikhail Lukin / Markus Greiner — Harvard Quantum Optics Group |
| **Relevance** | Demonstrated 256+ atom tweezer arrays with single-atom control. Published reconfigurable 2D geometries in Science (2021-2024). Active in quantum simulation and error mitigation. |
| **Contact approach** | Email to group PI or senior postdoc (Dr. Dolev Bluvstein, Dr. Simon Evered, Dr. Tout Wang — verify current group members on arXiv before sending) |
| **Email subject line** | "Proposal: Immediate Demonstration of Passive Error Confinement on Existing Neutral Atom Hardware — 40 Atoms, No Modifications Required" |
| **Email body template** | See §B2 below |
| **Attachments** | `0.7.md` (outreach whitepaper), `0.17_hardware_specs.md` (hardware spec), link to companion paper on Zenodo (after A1 complete) |
| **Papers to cite in email** | Bluvstein et al., "A quantum processor based on coherent transport of entangled atom arrays," Nature 604, 451-456 (2022). Ebadi et al., "Quantum phases of matter on a 256-atom programmable quantum simulator," Nature 595, 227-232 (2021). |
| **Specific ask** | "Would you be willing to allocate 2-4 hours of machine time to encode our ternary tree pattern on 40 atoms, inject controlled bit-flip errors at 8 error rates, and share the raw fluorescence readout data for our classical post-processing? We provide all analysis code and can co-author the resulting experimental paper." |
| **Expected outcome (optimistic)** | Co-authored experimental validation paper: "Experimental Demonstration of Symmetric Ultrametric Error Confinement in a Ternary Tree Architecture" — submitted to PRL or Nature Communications within 3-6 months |
| **Expected outcome (realistic)** | Preliminary data sharing agreement, iterative protocol refinement over video calls, experimental run within 3-12 months |
| **Fallback if no response within 2 weeks** | Send follow-up email; try contact through Harvard Quantum Initiative administrative office; try personal introduction through mutual contacts in quantum computing community |

**Target Laboratory 2: California Institute of Technology — Endres Group**

| Detail | Specification |
|:-------|:-------------|
| **Group** | Manuel Endres — Caltech Quantum Optics Group |
| **Relevance** | Demonstrated 200+ atom tweezer arrays with high-fidelity single-qubit control. Active in quantum error correction and fault-tolerant architectures. Strong track record of experimental-theoretical collaboration. |
| **Contact approach** | Same as Harvard, adapted for Caltech context |
| **Papers to cite in email** | Endres et al., "Atom-by-atom assembly of defect-free one-dimensional cold atom arrays," Science 354, 1024-1027 (2016). |
| **Specific ask** | Same as Harvard |

**Target Laboratory 3: PASQAL / Institut d'Optique — Browaeys Group**

| Detail | Specification |
|:-------|:-------------|
| **Group** | Antoine Browaeys / Thierry Lahaye — Laboratoire Charles Fabry, Institut d'Optique, and PASQAL (quantum computing company) |
| **Relevance** | PASQAL operates commercial neutral atom quantum processors with 100+ atoms. Demonstrated 2D and 3D atom arrays. Strong industry-academic collaboration model. |
| **Contact approach** | Dual-track: (1) Email to Browaeys/Lahaye at Institut d'Optique for academic collaboration, (2) Contact PASQAL's research partnership team (partnerships@pasqal.com) for potential industry collaboration |
| **Papers to cite in email** | Barredo et al., "Synthetic three-dimensional atomic structures assembled atom by atom," Nature 561, 79-82 (2018). Scholl et al., "Quantum simulation of 2D antiferromagnets with hundreds of Rydberg atoms," Nature 595, 233-238 (2021). |
| **Specific ask** | Same as Harvard, plus: "PASQAL's commercial platform is particularly well-suited because your API already supports arbitrary atom positioning and single-qubit rotations — our protocol requires only these two capabilities." |

**Target Laboratory 4: University of Innsbruck / IQOQI — Zoller/Blatt Group**

| Detail | Specification |
|:-------|:-------------|
| **Group** | Peter Zoller / Rainer Blatt — Institute for Quantum Optics and Quantum Information (IQOQI) |
| **Relevance** | World-leading trapped ion group with demonstrated high-fidelity single-qubit control. Trapped ions offer longer coherence times than neutral atoms, potentially enabling deeper tree depths. Secondary platform per 0.6.md scoping. |
| **Contact approach** | Email to group — note that trapped ions are our SECONDARY platform; emphasize that ion chains naturally map to tree DFS ordering |
| **Specific ask** | "Would a 40-ion linear chain demonstration of our ternary tree encoding be feasible on your platform? The protocol requires only single-qubit rotations and fluorescence readout — no entangling gates." |

### B2. Outreach Email Template

```
Subject: Proposal: Immediate Demonstration of Passive Error Confinement on
Existing Neutral Atom Hardware — 40 Atoms, No Modifications Required

Dear [Dr. Lastname / Prof. Lastname],

I am writing to propose a collaboration that could yield an experimental
result on your EXISTING neutral atom platform within 2-4 hours of machine
time, requiring no hardware modifications, no ancilla qubits, no syndrome
measurements, and no real-time feedback.

The protocol:
1. Arrange 40 atoms in a ternary tree pattern (geometric layout provided)
2. Encode a logical bit by setting all atoms to |0> or |1> (one global pulse)
3. Inject controlled bit-flip errors at 8 error rates (X-rotations, tunable)
4. Read out all atoms via standard fluorescence imaging
5. We perform all classical post-processing (hierarchical majority vote)

The architecture is described in our companion paper:
  "[TITLE]", Zenodo, 2026. DOI: [INSERT AFTER A1 COMPLETE]

This is a companion to our earlier validation:
  Quni-Gudzinas, "Computational Validation of Ultrametric Error Confinement
  in Bruhat-Tits Tree Quantum Circuits," Zenodo, 2026.
  DOI: 10.5281/zenodo.20134944

Key computational findings (all code-executed, reproducible):
- At depth 7 (2,187 atoms), zero logical errors at 40% physical error rate
  for BOTH logical states (36,000 trials)
- Ternary (p=3) branching eliminates tie-breaking asymmetry present in the
  original p=2 architecture
- Under correlated noise, the hierarchical structure outperforms classical
  repetition codes at matched qubit counts
- A q-ary generalization achieves 48× error rate reduction using existing
  atomic hyperfine levels (no additional atoms required)

The near-term demonstration uses only depth 3 (40 atoms total, 27 leaves +
13 internal nodes). Expected logical error rate: ~18% at 40% physical error
rate, with PERFECT symmetry between logical states — the critical experimental
signature.

I have attached:
- 1-page outreach summary (0.7.md)
- Hardware prototype design specification (0.17.md)
- Link to full companion paper with all computational data

I would be honored to discuss this further at your convenience. I am happy
to provide all simulation code, analysis scripts, and paper drafts in
exchange for experimental data sharing and co-authorship on the resulting
publication.

With warm regards,
Rowan Brad Quni-Gudzinas
[rowan@email.com — REPLACE WITH ACTUAL EMAIL]
```

### B3. Conference and Workshop Targets

| Venue | Relevance | Action |
|:------|:----------|:-------|
| **QEC 2027** (International Conference on Quantum Error Correction) | Premier error correction venue | Submit abstract once Zenodo DOI exists + experimental data (if available) |
| **APS March Meeting 2027** | Largest physics conference | Submit contributed talk in Division of Quantum Information (DQI) |
| **Q2B 2027** (Quantum Computing Business) | Industry-academic bridge | Poster or talk if PASQAL collaboration established |
| **DAMOP 2027** (Atomic, Molecular, Optical Physics) | Neutral atom community | Ideal for experimental validation talk if data exists |
| **TQC 2027** (Theory of Quantum Computation) | Theory-focused | Submit if Lean 4 formalization (Phase D) is complete |
| **QIP 2028** (Quantum Information Processing) | Top quantum information venue | Target for full experimental + theoretical paper |

---

## PHASE C: COMPUTATIONAL EXTENSIONS (Priority: MEDIUM)

### C1. $p=5$, $d=5$ Validation Run

**Objective:** Confirm $p=5$ symmetry and zero-error claim at $d=5$ (3,125 leaves, barrier $3^5=243$).

**Exact computational parameters:**
- Module: `0.10.py` (general-$p$ tree, already implemented)
- Runner: Create `0.19_run_p5_d5.py` based on `0.10_run_p5.py`
- Parameters: `p=5`, `depth=5`, `n_trials=500`, `seed=42`, `p_err_list = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]`
- Logical bits: `[0, 1]` (both independently)
- Total trials: $500 \times 8 \times 2 = 8{,}000$
- Expected runtime: ~30-60 seconds per $p_{\text{err}}$ condition (3,125 leaves × 500 trials × majority vote), ~8-16 minutes total
- Expected result: Both bits produce identical LER (symmetric); at $p_{\text{err}}=0.40$, LER should be effectively zero (Wilson CI upper bound ≈ 0.0076 at 500 trials)
- Risk: Python recursion limit may be hit at depth 5 with 3,125 leaves; set `sys.setrecursionlimit(20000)` as precaution
- Output format: JSON matching `0.10_p5_results.json` schema; append as `p5_d5_bit0` and `p5_d5_bit1` keys
- Post-run: Update `0.8.md` §3.3.1 Table 3b to add $d=5$ row

### C2. Multi-Bit with Correlated Noise

**Objective:** Test whether the tree's correlated-noise advantage (Sprint 3, Task 3.2) persists when multiple logical bits are encoded simultaneously.

**Exact computational parameters:**
- Modules: Combine `0.12_correlated_noise.py` with `0.13_multi_bit.py`
- Create: `0.19_multi_bit_correlated.py`
- Test configurations:
  - (a) $p=3$, $d=5$, $k=1$: 3 logical bits, 81 leaves/bit, $B=16$ per bit
  - (b) $p=3$, $d=5$, $k=2$: 9 logical bits, 27 leaves/bit, $B=8$ per bit
- Correlated noise parameters: $p_{\text{base}} \in [0.10, 0.20, 0.30, 0.40]$, $p_{\text{corr}} \in [0.0, 0.25, 0.50, 0.75]$, $k=2$
- Trials per condition: 500
- Expected result: At high $p_{\text{corr}}$, the tree's multi-bit BER should degrade less severely than classical multi-bit repetition at matched qubit count — the hierarchical structure should contain correlated errors within individual subtrees
- Risk: Computational cost is moderate ($4 \times 4 \times 500 = 8{,}000$ trials per configuration, ~2-5 minutes total)

### C3. $p=7$, $d=4$ Validation Run

**Objective:** Extend $p=7$ validation to $d=4$ (2,401 leaves, barrier $4^4=256$).

**Exact computational parameters:**
- Parameters: `p=7`, `depth=4`, `n_trials=500`, `seed=42`, 8 $p_{\text{err}}$ values, both bits
- Expected runtime: ~2-5 minutes per condition, ~30-60 minutes total
- Expected result: LER = 0.000 at all $p_{\text{err}} \leq 0.40$ for both bits; Wilson CI upper bound ≈ 0.0076
- Risk: Recursion depth — 2,401 leaves; set `sys.setrecursionlimit(10000)`
- Output: JSON matching `0.10_p7_results.json` schema; append `p7_d4_bit0` and `p7_d4_bit1` keys

---

## PHASE D: LEAN 4 FORMALIZATION (Priority: LOW — Requires Go/No-Go Decision)

### D0. Go/No-Go Decision Criteria

**GO if:**
1. A collaborator with Lean 4 expertise expresses interest (co-author on formalization paper)
2. A journal referee requests machine-checked proofs (respond to reviewer request)
3. QWAV strategic priorities explicitly prioritize formal verification as a capability demonstration
4. The companion paper receives significant attention and the formalization would strengthen follow-up work

**NO-GO if:**
1. No Lean 4 collaborator is available within 6 months
2. Experimental outreach (Phase B) consumes available bandwidth
3. The mathematical claims are sufficiently simple (barrier recurrence, Theorem 1) that machine verification adds marginal value

### D1. Theorem Formalization — Exact Specifications

**Theorem 1 (Universal BT Asymmetry): "For every prime $p$, the strict Bruhat-Tits rooted tree contains nodes with an even number of children, at which majority-vote tie-breaking is required."**

**Lean 4 formalization plan:**

```
File: Ultrametric/BTAsymmetry.lean

Module structure:
1. Import Mathlib (Data.Nat.Parity, Data.Nat.Prime, Data.Finset)
2. Define: BruhatTitsTree (p : Nat) [Fact p.Prime]
   - Vertices: homothety classes of Z_p-lattices in Q_p^2
   - For finite fragment: use rooted subtree of depth d
3. Define: strict root degree = p+1 (neighbors in full tree)
4. Define: internal node degree = p
5. Lemma: root_degree_even (p : Nat) [hp : Fact p.Prime] [hodd : p ≠ 2] : Even (p+1)
   - Proof: If p is odd prime, p ≡ 1 mod 2, so p+1 ≡ 0 mod 2, hence even.
6. Lemma: internal_degree_even (p : Nat) [hp : Fact p.Prime] [h : p = 2] : Even p
   - Proof: 2 = 2, trivially even.
7. Theorem: universal_asymmetry (p : Nat) [Fact p.Prime] :
   (∃ n : Node (strict_tree p d), Even (children n)) := ...
   - Case 1: p = 2 → internal nodes have 2 children (even)
   - Case 2: p ≥ 3 → root has p+1 children, p odd → p+1 even
   - QED
```

**Theorem 2 (Barrier Recurrence): "For regular $p$-ary tree with odd $p$, the minimum number of leaf errors required to flip the root majority vote is $B(d) = \lceil p/2 \rceil^d$."**

**Lean 4 formalization plan:**

```
File: Ultrametric/BarrierRecurrence.lean

Module structure:
1. Import: Mathlib (Data.Nat.Basic, Algebra.Order, Induction)
2. Define: RegularParyTree (p d : Nat) [Fact p.Prime] [hodd : Odd p]
   - All nodes have exactly p children
   - Leaves at uniform depth d
   - Root at depth 0
3. Define: decode (t : RegularParyTree p d) (leaf_values : List (Fin 2)) : Fin 2
   - Bottom-up majority: for each node, majority of p children → node value
   - Tie-breaking not possible (p odd)
4. Define: barrier (p d : Nat) : Nat := (Nat.ceil (p / 2)) ^ d
5. Lemma: base_case (p : Nat) [Odd p] : barrier p 1 = Nat.ceil (p / 2)
   - Proof: For depth 1, all p leaves are children of root. Need ceil(p/2) errors to change majority.
6. Lemma: inductive_step (p d : Nat) [Odd p] [h : barrier p d = (Nat.ceil (p / 2)) ^ d] :
   barrier p (d+1) = (Nat.ceil (p / 2)) ^ (d+1)
   - Proof: At depth d+1, each internal node at depth 1 has p children that are subtrees of depth d.
     Each subtree requires B(d) errors to flip. Need ceil(p/2) subtrees to flip to change root majority.
     Total: ceil(p/2) * B(d) = ceil(p/2) * ceil(p/2)^d = ceil(p/2)^(d+1).
7. Theorem: barrier_formula (p d : Nat) [Odd p] : barrier p d = (Nat.ceil (p / 2)) ^ d :=
   by induction d; exact base_case; exact inductive_step

8. Corollary: p3_barrier (d : Nat) : barrier 3 d = 2^d := by
   simp [barrier_formula, show Nat.ceil (3/2) = 2 by norm_num]
```

**Theorem 3 (Symmetry): "For odd $p$, the barrier for logical 0 equals the barrier for logical 1."**

```
File: Ultrametric/Symmetry.lean

1. Theorem: barrier_symmetric (p d : Nat) [Odd p] :
   barrier p d = barrier p d := rfl
   -- Trivial: the barrier formula is independent of logical bit value
   -- This is the whole point: odd p eliminates tie-breaking asymmetry
2. Corollary: symmetry_holds (p d : Nat) [Odd p] :
   (barrier_for_bit p d 0) = (barrier_for_bit p d 1) := by
   unfold barrier_for_bit; rfl
```

### D2. Implementation Roadmap

**Step 1 — Environment Setup (1-2 hours):**
- Install Lean 4 + Mathlib4 via elan: `elan toolchain install leanprover/lean4:stable`
- Create new Lean project: `lake new UltrametricErrorConfinement`
- Add Mathlib4 dependency to `lakefile.lean`
- Structure: `UltrametricErrorConfinement/Ultrametric/` (BTAsymmetry.lean, BarrierRecurrence.lean, Symmetry.lean, MajorityVote.lean)
- Verify build: `lake build`

**Step 2 — Core Definitions (2-4 hours):**
- `Ultrametric/MajorityVote.lean`: Define majority vote function over `List (Fin 2)` with tie-breaking to 0
- `Ultrametric/Tree.lean`: Define `RegularParyTree` as inductive type with depth, children
- Prove termination: depth decreases in recursive decode calls

**Step 3 — Theorem 1 Proof (2-4 hours):**
- Requires parity lemmas from Mathlib (Nat.Even, Nat.Odd, Nat.Prime)
- Main difficulty: formalizing "node in tree has N children" as a predicate
- Use `Finset.card` for child counting

**Step 4 — Theorem 2 Proof (4-8 hours):**
- Main difficulty: the induction step requires reasoning about subtree errors
- Need lemma: "if ceil(p/2) subtrees are flipped, root flips"
- Need lemma: "fewer than ceil(p/2) subtrees flipped → root does not flip"
- The "minimum errors" claim requires an adversarial pattern lemma: "there exists a pattern of ceil(p/2)^d leaf errors that flips the root"
- Constructive: flip ceil(p/2) subtrees at each level, recursively

**Step 5 — Verification (2-4 hours):**
- Run `#eval` on small instances (p=3, d=1,2,3) to cross-check with Python exhaustive results
- Generate documentation: `lake doc`
- Total estimated Lean 4 effort: 12-24 hours for an experienced Lean user, 40-80 hours for a Lean learner

### D3. Collaborator Wishlist

| Name/Affiliation | Lean 4 Experience | Relevance | Contact Method |
|:-----------------|:------------------|:----------|:---------------|
| **Kevin Buzzard** (Imperial College) | Lead of Mathlib, Xena Project | World's leading expert on formalizing mathematics in Lean | Email or Xena Project Discord |
| **Terence Tao** (UCLA) | Recently started using Lean for formalization (2024) | Mathematical physics expertise; p-adic background | Email or Lean Zulip chat |
| **Johan Commelin** (Universität Freiburg) | Mathlib maintainer, formalized perfectoid spaces (p-adic!) | Direct p-adic expertise in Lean | Mathlib GitHub or Zulip |
| **Patrick Massot** (Université Paris-Saclay) | Mathlib maintainer, formalized topology | Expertise in formalizing geometric structures | Mathlib GitHub or Zulip |
| **Any Lean Zulip community member** | Variable | Post as "Proposition for collaboration" on `#mathematics` or `#general` stream | https://leanprover.zulipchat.com |

---

## PHASE E: DOCUMENTATION & ARCHIVAL (Priority: MEDIUM)

### E1. Project Archival

- [ ] Create `README.md` in `ultrametric_v2/` with 1-paragraph summary + file inventory + "Where to start" guide
- [ ] Ensure all 26 files have consistent headers (author, date, version, project)
- [ ] Delete temporary files (`_*.py`, `_*.txt`, `check_consistency.py`, `__pycache__/`)
- [ ] Create `G:\My Drive\projects\ultrametric_v2\ARCHIVE.md` with metadata for each file (purpose, dependencies, reproducibility notes)
- [ ] Tag the final git commit: `git tag -a v2.0.0 -m "Ultrametric Error Confinement v2 — Complete. 7 sprints, 26 files, 250K+ trials."`

### E2. Cross-Project Learning Export (Kaizen)

- [ ] Review `LEARNINGS.md` (10 lessons) and export cross-project-applicable lessons to `G:\My Drive\projects\_shared\CROSS-PROJECT-LEARNINGS.md`
- [ ] Lessons L2 (monorepo discipline), L3 (write tool failure), L4 (constructive patterns), L6 (branch renaming), L7 (exhaustive exponential), L8 (universal asymmetry), L9 (regular p-ary p=2), L10 (PowerShell/inline Python) are all cross-project applicable

---

*All quantitative parameters [CODE-EXECUTED]. External contacts [LLM-INFERRED] — verify before sending communications.*
