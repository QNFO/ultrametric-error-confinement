# platform-scoping.md — Physical Platform Scoping for Ultrametric Error Confinement

**Phase 4:** Physical Implementation Pathway Analysis
**Date:** 2026-05-15
**Source Classification:** `[LLM-INFERRED]` — platform analysis based on training knowledge of quantum computing architectures. No external web search performed. All claims are reasoning-based and should be verified against current literature before contacting experimental groups.

---

## 1. Architecture Requirements

The ternary ultrametric tree architecture imposes specific physical requirements:

1. **Tree topology connectivity:** A rooted ternary tree of depth $d$ with $3^d$ leaf qubits and $(3^{d+1}-1)/2$ total qubits. Edges must connect each parent to exactly 3 children.
2. **Hierarchical coupling:** Parent-child couplings must be substantially stronger than non-tree couplings (cross-talk suppression). The error confinement mechanism assumes errors propagate only along tree edges.
3. **Majority-vote decoding:** Readout must measure all qubits and compute a bottom-up majority vote — this is classical post-processing, not a quantum operation.
4. **Encoding:** Initial state preparation sets all leaf qubits to $\lvert 0\rangle$ or $\lvert 1\rangle$ identically — a trivial product state.
5. **Noise model:** The architecture is validated against i.i.d. bit-flip noise. Physical platforms should have noise dominated by independent single-qubit errors rather than correlated multi-qubit errors.
6. **Scalability target:** $d = 7$ (2187 leaves, 3280 total qubits) achieves zero observed logical errors at 40% physical error rate. This is the demonstration target.

---

## 2. Candidate Platform Evaluation

### 2.1 Trapped Ions

**Description:** Ions confined in segmented RF Paul traps, with qubits encoded in hyperfine or optical transitions. Coupling via shared motional modes (Molmer-Sorensen gates) or through photonic interconnects.

**Tree Mapping:**
- **Layout:** Ions in a linear chain or 2D segmented trap. A tree topology requires non-local couplings. Segmented traps (e.g., QCCD architecture) can physically shuttle ions between zones to realize arbitrary connectivity. A depth-3 tree (27 leaves, 40 ions) is within current capabilities.
- **Coupling hierarchy:** Entangling gates between specific ion pairs can be engineered via focused laser beams. Parent-child couplings can be made strong (gate fidelity $>99.9\%$ reported). Non-tree couplings are naturally suppressed by physical separation and laser addressing.
- **Scalability:** Linear chains scale poorly beyond ~50 ions due to spectral crowding. Segmented traps (Honeywell, IonQ) are more scalable but introduce shuttling overhead. For $d=7$ (3280 ions), this is far beyond current demonstrations but not fundamentally impossible with photonic interconnects.

**Noise Model:**
- Dominant errors: motional heating, laser intensity fluctuations, magnetic field noise.
- Errors are predominantly independent single-qubit errors — a good match for the i.i.d. bit-flip model.
- $T_2$ coherence times: seconds for hyperfine qubits — ample for encoding and readout.

**Feasibility Assessment:**
- **Tree layout:** Moderate. Segmented traps can realize tree connectivity via shuttling.
- **Coupling engineering:** Good. Laser-addressed gates between specific pairs.
- **Noise match:** Excellent. Dominantly independent errors.
- **Scalability to $d=7$:** Poor with current technology. Better suited for proof-of-principle at $d=3$ (40 ions).
- **Overall:** **PROMISING for near-term demonstration.** Best platform for $d \leq 4$.

---

### 2.2 Superconducting Qubits

**Description:** Josephson junction-based qubits (transmons, fluxoniums) coupled via microwave resonators or direct capacitive coupling. Most widely deployed platform (IBM, Google, Rigetti).

**Tree Mapping:**
- **Layout:** Superconducting qubits are fabricated on a 2D chip. A ternary tree is a planar graph (it can be drawn without edge crossings). A depth-3 tree (40 qubits) can be laid out on current chips. Larger trees require 3D integration or long-range couplers.
- **Coupling hierarchy:** Neighboring qubits are coupled via bus resonators or direct capacitance. Tree edges must be designed as intentional couplers; non-tree edges must be suppressed by physical distance or frequency detuning (the "always-on" ZZ coupling problem). Frequency crowding becomes severe for dense graphs.
- **Scalability:** IBM has demonstrated 433-qubit (Osprey) and 1121-qubit (Condor) chips with 2D heavy-hex lattice — not a tree. Mapping a ternary tree to a 2D grid requires significant overhead but is possible for $d \leq 5$ (243 leaves).

**Noise Model:**
- Dominant errors: $T_1$ relaxation, $T_2$ dephasing, gate errors (cross-talk, leakage to non-computational states).
- Cross-talk is a significant issue for dense layouts — this directly violates the tree-edge-only assumption.
- Error rates: single-qubit gate fidelity $>99.9\%$; two-qubit gate fidelity $\sim99.5\%$; measurement fidelity $\sim99\%$.

**Feasibility Assessment:**
- **Tree layout:** Good for small depths. Planar embedding of ternary tree requires careful routing.
- **Coupling engineering:** Challenging. Cross-talk suppression in dense arrays is an active research problem.
- **Noise match:** Moderate. Cross-talk and frequency crowding introduce correlated errors.
- **Scalability to $d=7$:** Poor for a pure tree. The planar embedding overhead and cross-talk management are prohibitive.
- **Overall:** **POSSIBLE for proof-of-principle ($d \leq 4$).** Cross-talk is the primary concern.

---

### 2.3 Photonic Cluster States

**Description:** Qubits encoded in photon polarization or time-bin degrees of freedom, entangled via spontaneous parametric down-conversion (SPDC) or quantum dot sources. Cluster states are the natural resource for measurement-based quantum computing.

**Tree Mapping:**
- **Layout:** Photonic cluster states can be generated in arbitrary graph topologies by programming the entanglement source. Tree graphs are particularly natural — the beam-splitter network or time-delay loop can be configured to produce specific graph states. A depth-3 tree (40 photons) has been demonstrated in principle.
- **Coupling hierarchy:** Graph edges are created by entanglement generation; non-edges are naturally uncoupled. This is the cleanest mapping to the tree model — only intended edges exist.
- **Scalability:** Photonic cluster states scale with source brightness and detector efficiency. Current demonstrations reach ~10-20 photon cluster states. Scaling to thousands of photons requires multiplexed sources and improved detectors.

**Noise Model:**
- Dominant errors: Photon loss (the primary error), detector inefficiency, source impurity.
- Photon loss is NOT a bit-flip error — it's an erasure error (the qubit is lost, not flipped). This is a fundamentally different error model from what the tree architecture assumes.
- Bit-flip errors in photonic qubits are relatively rare compared to loss.

**Feasibility Assessment:**
- **Tree layout:** Excellent. Graph states can be programmed to any topology.
- **Coupling engineering:** Excellent. Only intended edges exist.
- **Noise match:** Poor. Dominant error is photon loss (erasure), not bit-flip. The architecture would need adaptation to handle erasure errors.
- **Scalability to $d=7$:** Poor for near-term. Photon numbers are limited.
- **Overall:** **THEORETICALLY ELEGANT but PRACTICALLY MISMATCHED.** The clean tree mapping is offset by the erasure-dominant noise model. Worth revisiting if the error model is extended to handle erasures.

---

### 2.4 Neutral Atoms

**Description:** Ultracold atoms trapped in optical tweezer arrays, with qubits encoded in hyperfine ground states. Interactions via Rydberg blockade for entangling gates. Highly reconfigurable 2D/3D geometries.

**Tree Mapping:**
- **Layout:** Optical tweezers can position atoms in arbitrary 2D (and increasingly 3D) configurations. A ternary tree can be laid out in 2D with atoms at tree positions. Reconfiguration during computation is possible (moving atoms between zones). 2D arrays of 200+ atoms are routine (Harvard, Caltech, Pasqal); 3D is emerging.
- **Coupling hierarchy:** Rydberg blockade provides strong, localized interactions between neighboring atoms. The interaction range can be tuned via laser parameters. Non-tree couplings can be suppressed by physical separation beyond the blockade radius or by spectral addressing.
- **Scalability:** 2D arrays of 1000+ atoms demonstrated. 3D arrays are being developed. For $d=5$ (243 leaves, 3280 atoms total — wait, 3280 is for d=7), let me recalculate: for d=5, total nodes = (3^6 - 1)/2 = (729-1)/2 = 364. For d=6: 1093 atoms. For d=7: 3280 atoms. Current demonstrations are at the scale of d=5..6.

**Noise Model:**
- Dominant errors: Atom loss (from vacuum), laser intensity/phase noise during gates, finite $T_2$ (seconds for hyperfine qubits).
- Atom loss is an erasure error (detectable — you know when an atom is lost). Entangling gate errors can produce bit-flip or phase-flip errors.
- The noise model is mixed: some erasure (detectable), some independent bit-flip.

**Feasibility Assessment:**
- **Tree layout:** Excellent. Arbitrary 2D/3D atom positioning.
- **Coupling engineering:** Very good. Rydberg blockade provides strong, tunable, localized interactions.
- **Noise match:** Good. Loss is detectable (erasure); remaining errors are largely independent.
- **Scalability to $d=7$:** Moderate-Good. At the edge of current capabilities but plausible with near-term scaling.
- **Overall:** **MOST PROMISING PLATFORM.** Combines arbitrary geometry, demonstrated scalability, and favorable noise characteristics. The reconfigurability allows iterative refinement of the tree layout.

---

### 2.5 NV Centers in Diamond

**Description:** Nitrogen-vacancy centers in diamond, with electronic spin qubits coupled to nearby nuclear spin registers. Dipole-dipole coupling between proximal NV centers. Long coherence times at room temperature.

**Tree Mapping:**
- **Layout:** NV centers are fixed by the diamond lattice. Creating a precise tree topology requires deterministic placement (ion implantation or lithography), which has limited precision. Current arrays are small ($<20$ NV centers).
- **Coupling hierarchy:** Dipole-dipole coupling strength falls as $1/r^3$. Tree edges require proximal placement; non-tree edges are suppressed by distance. Engineering precise, uniform coupling strengths across a tree is extremely challenging.
- **Scalability:** Poor. Deterministic placement of hundreds of NV centers with controlled coupling is far from demonstrated.

**Noise Model:**
- Dominant errors: Spin bath interactions ($^{13}$C nuclei), magnetic field inhomogeneity, optical readout infidelity.
- Errors are largely independent but with significant inhomogeneity across centers.

**Feasibility Assessment:**
- **Tree layout:** Poor. Fabrication precision limits deterministic placement.
- **Coupling engineering:** Poor. Dipole coupling strength hard to control precisely.
- **Noise match:** Moderate. Largely independent but inhomogeneous.
- **Scalability:** Very Poor.
- **Overall:** **NOT VIABLE for near-term.** Scaling and fabrication challenges are too severe.

---

## 3. Down-Select Summary

| Platform | Tree Geometry | Coupling Control | Noise Match | Scalability | Overall |
|:---------|:-------------:|:----------------:|:-----------:|:-----------:|:-------:|
| Trapped Ions | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | **PROMISING** |
| Superconducting | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ | Possible |
| Photonic | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐ | ⭐ | Mismatched |
| Neutral Atoms | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | **BEST** |
| NV Centers | ⭐ | ⭐ | ⭐⭐⭐ | ⭐ | Not viable |

### Primary Recommendation: Neutral Atoms

Neutral atom tweezer arrays are the most promising platform for physical implementation of the ultrametric tree architecture. The combination of:
1. Arbitrary 2D/3D atom positioning (exact tree layout)
2. Rydberg-mediated interactions with tunable range (coupling hierarchy)
3. Demonstrated scaling to 1000+ atoms
4. Detector-detectable atom loss (erasure errors can be identified and potentially corrected)
5. Active academic and commercial development (multiple groups worldwide)

makes this platform uniquely suited.

### Secondary Recommendation: Trapped Ions (for small-scale demonstration)

Trapped ions offer the cleanest noise model (dominantly independent errors) and the highest gate fidelities. A proof-of-principle experiment at $d=3$ (27 leaves, 40 ions) would demonstrate the core mechanism — exponential error suppression via tree topology — with a platform where the physics is well understood and controlled.

### Next-Generation Candidate: Photonic Cluster States (requires error model extension)

If the error model is extended to handle erasure errors (which are dominant in photonics), the photonic cluster state approach becomes the theoretically cleanest implementation. The ability to program arbitrary graph topologies means the ternary tree can be realized exactly, with zero cross-talk (only intended edges exist). This is a strong candidate for future work.

---

## 4. Implementation Pathway (Neutral Atoms)

### 4.1 Near-Term Demonstration ($d=3$, 40 atoms)

- **Atoms:** 40 Rubidium atoms in optical tweezers.
- **Layout:** 2D ternary tree of depth 3 (27 leaves, 13 internal nodes, 40 total). The tree can be drawn as a planar graph.
- **Encoding:** Initialize all atoms to $\lvert 0\rangle$ via optical pumping.
- **Noise application:** Apply random single-qubit rotations (simulating $p_{\text{err}}$) using focused laser pulses — this is a deliberate error injection to test the architecture, not natural noise.
- **Readout:** Fluorescence imaging of all atoms simultaneously.
- **Decoding:** Classical post-processing: majority vote on the acquired images.
- **Expected result:** At $p_{\text{err}} = 0.20$, the simulation predicts zero logical errors in 500 trials. The experiment would test this prediction.
- **Advantage:** Well within current capabilities. Can be performed on existing neutral atom platforms (e.g., Harvard, Caltech, Pasqal).

### 4.2 Medium-Term ($d=5$, 364 atoms)

- Requires a 2D array of ~400 atoms, which is within demonstrated capabilities.
- Adds Rydberg entangling gates between tree-coupled neighbors for a more realistic "propagation" noise model.
- Simulation predicts: at $d=5$, $p_{\text{err}} = 0.40$: LER $= 0.010$. Experimentally distinguishable from baseline.

### 4.3 Long-Term ($d=7$, 3280 atoms)

- Requires scaling to 3000+ atoms, which is at the frontier but plausible with 3D tweezer arrays and improved vacuum/laser systems.
- Simulation predicts: zero observed logical errors at all tested $p_{\text{err}} \leq 0.40$.
- Would constitute a definitive experimental demonstration of passive ultrametric error confinement.

---

## 5. Experimental Design Considerations

### 5.1 What to Measure

1. **Logical error rate vs. physical error rate:** The central claim — exponential suppression with depth. Measure LER for $d=3,4,5$ at controlled $p_{\text{err}}$.
2. **Symmetry verification:** Confirm LER is identical for logical $\lvert 0\rangle$ and $\lvert 1\rangle$.
3. **Energy barrier:** Verify that the minimum number of flipped leaves to change the logical state follows $B(d) = 2^d$ (requires targeted flipping of specific qubits, not random noise).

### 5.2 Error Injection Protocol

The simulation uses i.i.d. bit-flip noise. To replicate this experimentally:
- After encoding all qubits to $\lvert 0\rangle$, apply independent $X$-rotation gates with rotation angle $\theta$ where $\sin^2(\theta/2) = p_{\text{err}}$.
- Alternatively, use a spatial light modulator to apply a different random phase to each atom, mapping to bit-flip probability.
- This is a controlled error injection, not natural noise — the experiment tests the architecture, not the platform's intrinsic noise.

### 5.3 Cross-Talk Mitigation

- **Neutral atoms:** Maintain atom spacing larger than the Rydberg blockade radius for non-tree pairs. Tree edges can be within the blockade radius for entanglement if desired, or can be outside it if only independent operations are needed.
- **Trapped ions:** Use segmented traps with physical separation between tree branches. Shuttling can be used to bring ions together for gates.
- **Superconducting:** Use frequency detuning (different qubit frequencies for different tree levels) and physical separation to suppress cross-talk.

### 5.4 Readout

- **All platforms:** Readout is a classical measurement — measure each qubit's state and apply the majority-vote algorithm in post-processing. No quantum error correction cycle is involved.
- **Neutral atoms:** Fluorescence imaging with high-fidelity state detection ($>99\%$).
- **Trapped ions:** Electron shelving with state-dependent fluorescence.

---

## 6. Identified Experimental Groups (for Outreach)

These groups have the demonstrated capability and research interests most aligned with the ultrametric tree architecture. `[LLM-INFERRED]` — verify current status before contacting.

### Neutral Atoms

| Group | Institution | Capability | Fit |
|:------|:-----------|:-----------|:----|
| Lukin Group / Greiner Group | Harvard | 2D tweezer arrays, 200+ atoms, Rydberg gates | Excellent |
| Endres Group | Caltech | 2D/3D tweezers, reconfigurable geometries | Excellent |
| Browaeys Group | Institut d'Optique (Pasqal) | Large-scale neutral atom arrays, commercial platform | Very Good |
| Kaufman Group | JILA / U. Colorado | Alkaline-earth atoms, high-fidelity gates | Good |

### Trapped Ions

| Group | Institution | Capability | Fit |
|:------|:-----------|:-----------|:----|
| Monroe Group | U. Maryland / IonQ | Segmented traps, QCCD architecture, commercial platform | Excellent |
| Home Group | ETH Zurich | High-fidelity gates, small-scale precision | Good |
| Lucas Group | Oxford | Segmented traps, shuttling | Good |

### Photonic Cluster States

| Group | Institution | Capability | Fit |
|:------|:-----------|:-----------|:----|
| Walther Group | U. Vienna | Programmable photonic cluster states | Very Good (if error model extended) |
| Furusawa Group | U. Tokyo | Large-scale time-domain multiplexed cluster states | Good |

---

## 7. Next Steps

1. **Write outreach email/abstract** summarizing the architecture and simulation results (outreach-whitepaper.md).
2. **Identify one specific group** for initial contact (recommendation: Endres Group at Caltech — reconfigurable 2D/3D geometries with demonstrated scalability).
3. **Prepare a 2-page whitepaper** (companion-paper.md) with key figures: LER vs $p_{\text{err}}$ table, barrier scaling, tree diagram.
4. **Optional: Adapt error model for photonic platform** (handle erasure errors) to broaden applicability.

---

*All platform assessments are `[LLM-INFERRED]` based on training knowledge. Capabilities and group affiliations should be verified against current literature before outreach.*
