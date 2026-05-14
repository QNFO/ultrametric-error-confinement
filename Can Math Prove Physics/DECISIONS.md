# DECISIONS — Can Math Prove Physics?

> Architecture/design decisions with rationale. Add entries when key decisions are made.

---

### D1: Project scope — email drafting as research method

- **Date:** Prior to 2026-05-14
- **Decision:** Use the email exchange with Richard as the primary vehicle for exploring "Can math prove physics?" rather than writing a standalone paper first.
- **Rationale:** The concrete objections from a domain expert force the philosophical questions into sharp relief. The email format allows iterative refinement of both technical and epistemological positions.
- **Alternatives considered:** Writing a standalone essay without the dialogue format; writing a formal paper.
- **Impact:** The project's primary artifact (`0.1.md`) is an iterative draft, not a polished document.

### D2: Tone rules for email drafting

- **Date:** During `0.1.md` iterations
- **Decision:** Enforce specific tone rules: no apologies, no false humility, direct answers, no math formulas in email body, acknowledge uncertainty honestly.
- **Rationale:** Early drafts were verbose, apologetic, and math-heavy — the opposite of what the user wanted. Explicit rules reduced iteration count.
- **Alternatives considered:** Freeform drafting with post-hoc tone correction.
- **Impact:** Converged email draft after ~12 iterations, with final versions achieving target tone in 2-3 rounds.

### D3: Philosophical position — math proves consistency, not reality

- **Date:** Captured in `0.1.1.md` and final email draft
- **Decision:** Adopt the position that formal proofs (including Lean) prove logical consistency under stated assumptions, not physical truth. The "assumptions gap" between model and reality is fundamental and unbridgeable by math alone.
- **Rationale:** This position aligns with standard philosophy of science (the Duhem-Quine thesis, model-dependent realism) and provides a framework for responding to Richard's objections.
- **Alternatives considered:** Stronger claim that math CAN prove physics (rejected as indefensible); stronger skepticism that formal proof has no value for physics (rejected as too extreme).
- **Impact:** Shapes all subsequent writing and the framing of Richard's objections.

### D4: Git monorepo — accepted for now, to be resolved

- **Date:** 2026-05-14 (documented)
- **Decision:** Proceed with the current monorepo setup (`G:/My Drive/projects` as git root) for this session, flagging the [REPO-MISALIGNED] issue. Resolution deferred to a future session.
- **Rationale:** Restructuring git repos requires user approval and significant effort. The documentation work doesn't depend on repo structure.
- **Alternatives considered:** `git init` in project directory immediately (requires user sign-off).
- **Impact:** Cross-project git contamination risk persists. See CROSS-PROJECT-LEARNINGS.md L1.
