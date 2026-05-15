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

### L4: Subagent output truncation at ~32K tokens — parent must complete long content

- **Category:** METHODOLOGY
- **Issue:** Subagent tasked with writing a ~3,000-word essay produced excellent content but the session terminated ("error" status) at ~32K tokens, cutting off mid-sentence in the penultimate section. The essay was structurally complete through Section 5.2 and required parent to finish Sections 5.2–6.
- **Solution:** For long-form content generation via subagents, either (a) split into smaller sequential sections, or (b) expect the parent to complete truncated output. Subagents reliably produce ~2,000–2,500 words before hitting token limits.
- **Prevention:** For content >2,000 words, use chain mode with smaller section-level tasks rather than a single large essay task.
- **Cross-Project:** YES — applies to any subagent-based long-form writing.

### L5: Avoid role-labeling collaborators — "formal verification specialist" reads as reductive

- **Category:** METHODOLOGY
- **Issue:** Subagent essay characterized Richard as a "formal verification specialist" and framed the exchange as "physicist vs. formal verification specialist." This is reductive, creates an us-vs-them dynamic, and would be inflammatory if read by the person so labeled.
- **Solution:** Refer to people neutrally by name or not at all. Frame exchanges around the ideas, not the identities of participants. "The proposal received detailed technical feedback" is better than "a formal verification specialist reviewed it."
- **Prevention:** When writing about collaborative exchanges where participants may read the output, audit all characterizations of people. If a label could rankle, remove it.
- **Cross-Project:** YES — applies to all writing that references specific people, especially potential collaborators.

### L3: PowerShell `&&` does not work — use `;` or separate commands

- **Category:** PYTHON
- **Issue:** Attempted `cd "path" && git status` on Windows PowerShell; parser error.
- **Solution:** Use `Set-Location "path"; git status` or run commands separately.
- **Prevention:** Always use PowerShell-compatible syntax on Windows.
- **Cross-Project:** YES (also documented in CROSS-PROJECT-LEARNINGS.md as L5)
