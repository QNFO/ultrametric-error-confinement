# PROJECT CHARTER — Error Confinement Live Demo

## 1. PROJECT IDENTITY

| Field | Value |
|:------|:------|
| **Project Name** | `ultrametric-error-confinement-demo` |
| **Title** | Error Confinement Live Demo |
| **Type** | QWAV Spinoff — Interactive Artifact (D13) |
| **QWAV Strategy Reference** | `strategy/3.0.md` — Build Gravity, Tier 1 Artifact A1 |
| **Created** | 2026-05-22 |
| **Repository** | `QNFO/ultrametric-error-confinement` |
| **Live Target** | `https://qnfo.github.io/ultrametric-error-confinement/` |
| **Parent Program** | QWAV — Ultrametric Quantum Computing & AI |

## 2. RAISON D'ÊTRE — QWAV STRATEGY NEXUS

**This project exists because QWAV's core thesis — that ultrametric geometry suppresses quantum errors without active QEC — is a mathematical claim that needs a visual, interactive proof.**

QWAV Strategy 3.0 ("Build Gravity") defines Tier 1 as "Interactive Artifacts." These are the gravitational center of the entire program: something people explore, interact with, and share because it's interesting in itself. A1 is the single most important artifact in the portfolio — it demonstrates the core thesis without requiring anyone to read a 30-page paper.

**Strategic contribution:**
- Converts the Tier 0/Tier 1 publication claims (48× error reduction, zero logical errors at depth 7) into a 30-second interactive experience
- Serves as the primary "gravity well" for cold outreach to neutral atom labs
- Is the first link shared in any application, email, or social media post about QWAV
- Validates (or falsifies) the core thesis through interactive exploration

**Without this project, QWAV has no way to demonstrate its thesis to non-specialists.** Papers are inert. A working interactive demo is gravity.

## 3. SCOPE

### In Scope
- Interactive Bruhat-Tits tree visualization on HTML5 Canvas
- Adjustable parameters: prime $p$, error rate $p_{\text{err}}$, tree depth $d$, sample count
- Real-time error rate computation matching the published Tier 0/Tier 1 validation data
- Visual demonstration of the strong triangle inequality preventing error propagation
- Error path highlighting — show the geometric mechanism, not just the numbers
- Responsive design (works on mobile and desktop)
- Single-file deployment (no build step, no dependencies except CDN fonts)

### Out of Scope
- Real quantum hardware simulation (classical approximation only)
- Multi-qubit gate modeling beyond the ternary tree structure
- Active QEC comparison visualization (that's A3's domain)
- Backend computation — everything runs in-browser

## 4. DELIVERABLES

| # | Deliverable | Acceptance Criteria | Status |
|:--|:------------|:--------------------|:------|
| D1 | Interactive tree canvas | Tree renders correctly at all $(p,d)$ combinations | PROTOTYPE |
| D2 | Parameter sliders | Slider movement triggers instant canvas redraw | PROTOTYPE |
| D3 | Error rate computation | LER values match published Table 1 within statistical tolerance | UNTESTED |
| D4 | Error path visualization | User can see which branches carry errors and why they don't propagate | NOT BUILT |
| D5 | Explanation overlay | Tooltips or info panel explaining what the user is seeing | NOT BUILT |
| D6 | Test suite | Automated verification of tree construction, error rates, and rendering | NOT BUILT |
| D7 | Deployment | Live on GitHub Pages, verified loading | DONE |

## 5. CONSTRAINTS

| Constraint | Rationale |
|:-----------|:----------|
| **Single HTML file, vanilla JS** | D13 compliance: no framework dependencies, no build tooling |
| **All computation in-browser** | No server costs, no backend maintenance, infinite scalability |
| **Must match published data** | Error rates must reproduce Tier 0/Tier 1 Table 1 within statistical tolerance |
| **Under 250KB total** | Must load instantly on mobile connections |
| **No external data files** | Self-contained — tree is generated algorithmically |

## 6. SUCCESS CRITERIA

1. **Mathematical correctness:** Error rates match published validation data to within $\pm 2\sigma$ statistical tolerance
2. **Interactivity:** Every parameter change produces visible, correct output within 100ms
3. **Educational clarity:** A visitor with no quantum computing background understands "the tree geometry prevents errors from spreading" within 30 seconds
4. **Gravity generation:** The demo is compelling enough that visitors share the link without being asked

## 7. STAKEHOLDERS

| Stakeholder | Interest |
|:------------|:---------|
| **Founder (Rowan)** | Primary outreach tool — linked in every application and email |
| **Neutral atom labs** | See if the geometry is physically realizable |
| **Grant reviewers** | 30-second thesis validation |
| **General public** | Understand why ultrametric geometry matters |

## 8. CURRENT STATUS (2026-05-23)

**Phase:** PROTOTYPE — Functional but untested

**What exists:** A single `index.html` (10 KB, 116 lines JS) with tree rendering, parameter sliders, and error injection. The tree draws. Sliders work. Basic interaction is functional.

**What's missing:**
- **No test suite.** Zero automated verification that error rates match published data.
- **No error path visualization.** User sees error counts but not WHERE errors occur or WHY the tree confines them. Missing the core educational value.
- **No explanation overlay.** There's no text explaining what the visitor is looking at.
- **No statistical validation.** The JS computes error values but no one has verified they match the Tier 0/Tier 1 paper data.
- **Hardcoded parameters.** Dataset selection is fixed — no way to explore different regimes.

**Next milestone:** D3 (Error rate computation verified against published data) + D4 (Error path visualization).

---

*Updated: 2026-05-23 | QWAV Strategy: Build Gravity v3.0 | Artifact: Tier 1 — A1*
