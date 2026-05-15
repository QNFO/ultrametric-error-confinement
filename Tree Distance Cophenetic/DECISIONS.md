# DECISIONS — Tree Distance Cophenetic

## D1: Project Documentation Standard
- **Date:** 2026-05-14
- **Decision:** Adopt the 7-file documentation standard (`README.md`, `PROJECT STATE.md`, `SPRINT.md`, `CHANGELOG.md`, `BACKLOG.md`, `LEARNINGS.md`, `DECISIONS.md`).
- **Rationale:** Required by agent system prompt for cross-session handoff and kaizen.
- **Alternatives Considered:** None — this is a mandatory standard.

## D2: Git Repo Structure
- **Date:** 2026-05-14
- **Status:** NOTED (not a decision — structural constraint)
- **Observation:** Git repo is at parent `G:/My Drive/projects` level, not project-isolated. This violates the recommended isolation pattern where each project has its own independent repo.
- **Impact:** All git commits affect the parent repo. Sibling project changes appear in the same git history.
- **Resolution:** TBD — user decision needed on whether to init a separate repo within this project directory.

## D3: Next Steps After Subagent Review
- **Date:** 2026-05-14
- **Decision:** Prioritize 4 HIGH-priority additions before any dissemination of the Tree Distance Cophenetic framework:
  1. Define cophenetic distance explicitly (formula + example)
  2. Add at least one concrete worked example
  3. Write the ultrametric inequality explicitly with derivation of triadic rigidity
  4. Add citations (Page & Wootters 1983, Wheeler & DeWitt, Sokal & Rohlf)
- **Rationale:** Reader testing revealed the document is currently inaccessible to anyone not already an expert in 4+ disciplines. The central concept (cophenetic distance) is never defined. The consilience claim is asserted, not demonstrated.
- **Alternatives Considered:** Skip to dissemination — rejected because reader testing showed the document would fail with its target audience.

## D4: Publication Draft (0.8.md) as Definitive Version
- **Date:** 2026-05-15
- **Decision:** `0.8.md` is the definitive publication draft, superseding `0.7.md` and all component documents (`0.3.md`–`0.6.md`). It includes DOI (10.5281/zenodo.20200828), formal abstract, academic structure, and all content from prior versions.
- **Rationale:** 0.8.md was reader-tested (7 issues identified and resolved), has a formal academic format suitable for Zenodo publication, and consolidates all prior work into a single document.
- **Impact:** `0.3.md`–`0.6.md` are retained for provenance but are superseded. `0.7.md` is an intermediate consolidation.

## D5: Branch Rename
- **Date:** 2026-05-15
- **Decision:** Rename active branch from `feature/ultrametric-v2-ternary-tree` to `feature/tree-distance-cophenetic`.
- **Rationale:** The old name referred to a different (sibling) project. The new name accurately reflects this project's identity.
- **Impact:** Documentation files (SPRINT.md, PROJECT STATE.md, CHANGELOG.md) updated with new branch name.
