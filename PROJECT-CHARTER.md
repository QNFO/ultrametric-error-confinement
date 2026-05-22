# PROJECT CHARTER — Error Confinement Live Demo

## Project Identity

| Field | Value |
|:------|:------|
| **Project Name** | ultrametric-error-confinement-demo |
| **Title** | Error Confinement Live Demo |
| **Type** | QWAV Spinoff — Interactive Artifact (D13) |
| **Created** | 2026-05-22 |
| **Deployed** | 2026-05-23 |
| **Live URL** | https://qnfo.github.io/ultrametric-error-confinement/ |
| **Repository** | QNFO/ultrametric-error-confinement |
| **Parent Program** | QWAV — Ultrametric Quantum Computing & AI |

## Purpose & Thesis

Interactive Bruhat-Tits tree simulation demonstrating ultrametric error suppression. Users adjust error rates and tree depth with sliders to see the strong triangle inequality geometrically prevent error accumulation.

## Technical Approach

Single HTML file, vanilla JavaScript, Canvas API. No dependencies.

## User Interaction

3 sliders (physical error rate, tree depth, samples). Canvas redraws in real time.

## Evidence Contribution

Zero logical errors at depth 7. 48x error reduction at q=128. Validated at physical error rates up to 40%.

## Success Criteria

1. Interactive elements respond to user input (verified by automated canvas check)
2. Deployed and loading at https://qnfo.github.io/ultrametric-error-confinement/
3. JavaScript executes without console errors
4. Cross-linked from QWAV Technical Site Hub
5. Demonstrates a specific, published QWAV result

## Constraints

- Zero external dependencies (no CDN, no npm)
- Single HTML file (inline CSS/JS)
- GitHub Pages deployment (no server)
- MIT licensed or equivalent open-source

## Relationship to QWAV Program

This project is one of 5 interactive artifacts (D13) that make QWAV's computational evidence tangible. Each demo demonstrates one key result:
- Error Confinement → strong triangle inequality visualization
- Q-PNA Playground → glass-box AI decision trees
- Convergence Explorer → ultrametric vs Euclidean comparison
- Tree Distance Sandbox → cophenetic distance computation
- Hardware Visualizer → neutral atom hardware mapping

Together, these 5 demos + the Technical Site Hub + the Virtual Qubit Showdown form the complete QWAV Gravity Portfolio.

---

*Project charter established 2026-05-22. Project completed 2026-05-23.*
