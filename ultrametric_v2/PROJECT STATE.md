# PROJECT STATE — Ultrametric Error Confinement v2

**Last Updated:** 2026-05-15
**Active Branch:** `feature/ultrametric-v2-ternary-tree`
**Session Focus:** Phase 0 (Setup) + Phase 1 (Symmetric Tree Code)

## Current Status

| Aspect | State |
|:-------|:------|
| Phase 0 (Setup) | IN PROGRESS |
| Phase 1 (Tree Code) | NOT STARTED |
| Phase 2 (Experiments) | NOT STARTED |
| Phase 3 (Energy Barrier) | NOT STARTED |
| Phase 4 (Physical Scoping) | NOT STARTED |
| Phase 5 (Lean Formalization) | NOT STARTED |
| Phase 6 (Documentation) | NOT STARTED |

## Key Decisions Made

1. **Ternary tree (root degree = 3):** Avoids tie-breaking at root. All internal nodes have exactly 3 children.
2. **p = 3:** Odd branching factor eliminates ties in majority vote (majority = 2 of 3).
3. **Symmetric design:** No bias toward logical 0 or 1. Both states tested independently.

## Next Steps (This Session)

1. Complete Phase 0: documentation files + .gitignore
2. Write `ultrametric_tree.py` with `build_tree()`, encode, decode, noise injection
3. Write unit tests with pytest
4. Run initial correctness check on small depths (d=2,3)

## Handoff Notes

- Project directory: `G:\My Drive\projects\ultrametric_v2\`
- Git repo: `G:\My Drive\projects` (monorepo with feature branches)
- No virtual environment yet — using system Python 3.10+
- All code is standard library only (no external deps beyond pytest)
