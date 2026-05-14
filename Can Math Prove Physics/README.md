# Can Math Prove Physics?

> **Project thesis:** Exploring whether mathematics — including formal proof systems like Lean — can validate physical theories, using ultrametric error confinement as the test case.

## Identity

This project examines the epistemological boundary between mathematical proof and physical reality. The central question: **Can a formal mathematical proof (e.g., in Lean) "prove" that a physical system will behave in a certain way?**

The investigation is grounded in a concrete case study: an ultrametric error confinement architecture on Bruhat–Tits trees. Richard (a mathematician with expertise in formal verification via HeytingLean) raised four technical objections to the paper. The ensuing exchange exposes deeper philosophical tensions about what formal proof can and cannot do for physics.

## Key Questions

1. **Does formal proof guarantee physical behavior?** No — it guarantees logical consistency under stated assumptions. The gap between assumptions and reality is always unbridgeable by math alone.

2. **What value does formal verification add?** It catches logical errors, clarifies assumptions, and proves that *if* the assumptions hold, the conclusion follows. This is useful but not equivalent to experimental validation.

3. **Is ultrametric error confinement provable?** Under idealized assumptions (symmetric decoder, $p \geq 3$, i.i.d. noise, tree geometry), the threshold theorem is provable. Whether those assumptions hold in physical hardware is a separate question.

## Constraints

- All quantitative work must be code-executed
- All citations must be traceable to source files
- Math formatting: LaTeX/MathJax only (no bare Unicode)
- Git: feature branches only, never commit to main

## Outputs

| File | Description |
|:-----|:------------|
| `0.1.md` | Iterative email draft responding to Richard's critique |
| `0.1.1.md` | Philosophical essay: "Can math prove physics?" |
