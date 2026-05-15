# PROJECT STATE — Tree Distance Cophenetic

**Last Updated:** 2026-05-15
**Current Phase:** Mathematical formalization complete — core definitions, proofs, and Python verification written
**Active Branch:** `feature/ultrametric-v2-ternary-tree`

## Current State

### Content Files
| File | Size | Status |
|:-----|:-----|:-------|
| `0.1.md` | 111,442 chars | Original core document — conversation-style exploration |
| `0.1.1.md` | 4,381 chars | Convergent outline — reader tested, gaps identified |
| `0.2.md` | 15,806 chars | Subagent review synthesis — cross-reference, gap analysis, reader testing, next steps |
| **`0.3.md`** | ~12,000 chars | **NEW** — Mathematical formalization: definitions, worked example, proofs, gauge invariance |
| **`0.3.py`** | ~8,500 chars | **NEW** — Python verification script (drafted, not yet executed) |
| `src_0.2_*.md` | 16 files | Imported release documents for cross-reference |

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
   - Reference list (pending verification)
3. Created `0.3.py` — companion verification script

### Key Decisions
- See `DECISIONS.md` for D4 (mathematical formalization approach)
- `0.3.md` uses standard cophenetic distance definition: $d(x, y) = h(\operatorname{lca}(x, y))$ with leaves at height 0, heights increasing toward root
- Triadic rigidity proven as consequence of LCA property (not asserted)

### Blocked Items
- Python execution unavailable — `0.3.py` drafted but theorems not [CODE-EXECUTED] verified
- Git exec requires `-C` flag workaround

### Handoff Notes
- `0.3.md` is the most complete and self-contained mathematical description of the framework
- `0.3.py` should be executed first thing in next session for [CODE-EXECUTED] verification
- Next HIGH priorities: add citations, generative mechanism (Autaxys bridge), methodology section (5I), CGF self-evaluation
- The resolution-dependence bridge (tree as resolution ladder → Illusion of Time's epsilon) is the strongest new convergence found in this session
