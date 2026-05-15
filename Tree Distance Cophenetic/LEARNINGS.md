# LEARNINGS — Tree Distance Cophenetic

## Lessons

### L1: Shared parent repo causes cross-project contamination
- **Category:** GIT
- **Issue:** The git repo at `G:/My Drive/projects` (parent level) mixes commits from sibling projects (`Can Math Prove Physics`, `Fractal Harmonic Trees`, `Tree Distance Cophenetic`). Branch names and commit history are shared across unrelated work.
- **Solution:** Noted but not resolved — this is a structural decision by the user. Each project should ideally have its own independent git repo.
- **Prevention:** Per-project `git init`. See CROSS-PROJECT-LEARNINGS.md L1.
- **Cross-Project:** YES

### L2: Backlog drift when files are deleted by parallel sessions
- **Category:** METHODOLOGY
- **Issue:** `0.1.md` and `0.1.1.md` were removed by a parallel session. BACKLOG.md still referenced them as active files, making it stale. PROJECT STATE.md documented the deletion but BACKLOG.md was not updated.
- **Solution:** Full-file audit at session start catches stale references. Rewrote BACKLOG.md to reference only current files.
- **Prevention:** When files are deleted, immediately update all 7 documentation files that reference them. Use Python `os.path.exists()` to verify all referenced files exist.
- **Cross-Project:** YES

### L3: Versioned file naming enables quick project state assessment
- **Category:** METHODOLOGY
- **Issue:** Without versioned names, it would be difficult to trace the evolution from 0.2.md (subagent review) → 0.3.md (math formalization) → 0.4.md–0.6.md (bridges) → 0.7.md (consolidation) → 0.8.md (publication draft).
- **Solution:** The 0.N.md naming convention encodes the chronological order and makes the project's evolution trivially visible from a directory listing.
- **Prevention:** Always use versioned filenames for content/output files. See Rule 7 (Section 10).
- **Cross-Project:** YES

### L4: Subagent unavailability should be detected early
- **Category:** TOOL-USE
- **Issue:** Attempted to use `subagent_orchestrator` for reader testing but the tool is not available in this environment. Time was spent planning subagent-based testing that couldn't execute.
- **Solution:** Check tool availability before designing workflows that depend on specific tools. Fall back to manual testing protocol.
- **Prevention:** At session start, verify which tools are actually available (not just listed in documentation). Design workflows around available tools.
- **Cross-Project:** YES

### L5: Publication draft (0.8.md) was created in sibling project directory context
- **Category:** OTHER
- **Issue:** `0.8.md` was committed under the path `ultrametric_v2/0.8.md` (git history) but physically exists in `Tree Distance Cophenetic/0.8.md`. This discrepancy arose because the branch `feature/ultrametric-v2-ternary-tree` was originally created for the ultrametric_v2 project, then reused for Tree Distance Cophenetic work.
- **Solution:** The file content is correct and complete. The git path discrepancy is cosmetic but noted for future reference.
- **Prevention:** Create project-specific branches from the start. Never reuse branches across projects.
- **Cross-Project:** YES
