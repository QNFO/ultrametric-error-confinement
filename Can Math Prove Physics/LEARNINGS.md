# LEARNINGS — Can Math Prove Physics?

> Project-specific lessons (kaizen engine). Machine-readable format.

---

### L1: Iterative drafting converges faster with clear feedback rules

- **Category:** METHODOLOGY
- **Issue:** In `0.1.md`, the draft went through ~12 iterations before converging. Early iterations were verbose and apologetic; the user had to repeatedly correct tone.
- **Solution:** The user established clear rules: (1) no apologizing, (2) direct style, (3) no math formulas in email, (4) acknowledge uncertainty without false humility. Once these were explicit, iterations converged in 2–3 rounds.
- **Prevention:** Ask for tone/style preferences BEFORE starting the first draft. Use a "tone sample" from the user.
- **Cross-Project:** YES — applicable to all email/direct-response drafting tasks.

### L2: The "assumptions gap" is the central epistemological issue

- **Category:** METHODOLOGY
- **Issue:** Both Richard's objections and the philosophical essay converge on the same point: formal proofs prove logical consistency under assumptions, not physical reality. The gap between assumptions (symmetric decoder, i.i.d. noise, tree geometry) and hardware realizability is the core unresolved question.
- **Solution:** Explicitly map which assumptions are mathematically convenient vs. physically plausible. Treat the assumption set as a hypothesis to be tested, not a given.
- **Prevention:** Every formal proof project should include an "assumption audit" section.
- **Cross-Project:** YES — applies to any formal verification of physical systems.

### L3: PowerShell `&&` does not work — use `;` or separate commands

- **Category:** PYTHON
- **Issue:** Attempted `cd "path" && git status` on Windows PowerShell; parser error.
- **Solution:** Use `Set-Location "path"; git status` or run commands separately.
- **Prevention:** Always use PowerShell-compatible syntax on Windows.
- **Cross-Project:** YES (also documented in CROSS-PROJECT-LEARNINGS.md as L5)
