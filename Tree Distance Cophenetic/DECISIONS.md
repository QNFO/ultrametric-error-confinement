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
