# PROJECT STATE — Tree Distance Cophenetic

**Last Updated:** 2026-05-15  
**Current Phase:** Mathematical formalization verified — [CODE-EXECUTED], math audited, content reviewed  
**Active Branch:** `feature/ultrametric-v2-ternary-tree`

## Current State

### Content Files
| File | Size | Status |
|:-----|:-----|:-------|
| `0.2.md` | 15,806 chars | Subagent review synthesis — cross-reference, gap analysis, reader testing, next steps |
| **`0.3.md`** | ~16,200 chars | **VERIFIED** — Mathematical formalization: definitions, proofs, [CODE-EXECUTED] results |
| **`0.3.py`** | ~8,500 chars | **VERIFIED** — All 70+ checks passed (ultrametric, triadic rigidity, Euclidean counterexample) |
| `src_0.2_*.md` | 16 files | Imported release documents for cross-reference |

> **Note:** `0.1.md` (111k chars) and `0.1.1.md` (4k chars) were removed by a parallel session. `0.3.md` supersedes them as the definitive mathematical reference.

### Project Documentation
| File | Status |
|:-----|:-------|
| `README.md` | Current |
| `PROJECT STATE.md` | Updated 2026-05-15 |
| `SPRINT.md` | Updated 2026-05-15 |
| `CHANGELOG.md` | Updated 2026-05-15 |
| `BACKLOG.md` | May need updates |
| `LEARNINGS.md` | May need updates |
| `DECISIONS.md` | May need updates |

### Completed This Session
1. Reviewed additional releases (`2025/08/`, `2025/11/`) and archive → found 5 new convergence points (C8-C12), limited archive content
2. Created `0.3.md` — complete mathematical formalization with:
   - Formal definitions of rooted tree, height function, LCA, cophenetic distance
   - Worked 4-item dendrogram example with computed distance matrix
   - Proof of ultrametric inequality from tree LCA property
   - Derivation of triadic rigidity
   - Binary decomposition theorem
   - Gauge invariance and Page-Wootters analogy
   - Information-theoretic interpretation
3. Created, executed, and debugged `0.3.py` — all 70+ checks passed [CODE-EXECUTED]
4. Full content review of `0.3.md` — fixed typo, updated verification status
5. Math formatting audit — PASSED (zero bare Unicode math outside math/code blocks)
6. Updated all 3 documentation files (SPRINT, CHANGELOG, PROJECT STATE)

### Key Decisions
- See `DECISIONS.md` for D4 (mathematical formalization approach)
- `0.3.md` uses standard cophenetic distance definition: $d(x, y) = h(\operatorname{lca}(x, y))$ with leaves at height 0, heights increasing toward root
- Triadic rigidity proven as consequence of LCA property (not asserted)

### Blocked Items
- (none — Python execution resolved this session)

### Handoff Notes
- `0.3.md` is the most complete and self-contained mathematical description of the framework
- **ALL mathematical claims are now [CODE-EXECUTED] verified** — the framework is mathematically coherent
- Next HIGH priorities: add verified citations, generative mechanism (Autaxys bridge), methodology section (5I), CGF self-evaluation
- The resolution-dependence bridge (tree as resolution ladder → Illusion of Time's epsilon) is the strongest new convergence found in this session
- Reader testing of `0.3.md` pending — questions prepared below for manual testing via fresh Claude session
