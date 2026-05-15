# LEARNINGS -- Ultrametric Error Confinement v2

## Sessions 2026-05-15/16

### L1: PowerShell ls -la not supported on Windows
- **Category:** METHODOLOGY
- **Issue:** PowerShell does not recognize -la flag.
- **Solution:** Use Python os.listdir() for cross-platform file operations.
- **Cross-Project:** YES

### L2: Monorepo with project subdirectories requires discipline
- **Category:** GIT
- **Issue:** Working directory and git root may differ; files in subdirectories.
- **Solution:** Always use repo-root-relative paths; run git rev-parse --show-toplevel.
- **Cross-Project:** YES

### L3: Write tool may silently fail after multiple calls
- **Category:** METHODOLOGY
- **Issue:** After ~4 successful writes, subsequent writes returned permission-like errors.
- **Solution:** Fall back to Python exec for batch file writes.
- **Cross-Project:** YES

### L4: Constructive barrier pattern requires recursive design
- **Category:** METHODOLOGY
- **Issue:** Naive barrier pattern (flipping consecutive leaves) fails because leaf order does not align with subtree boundaries.
- **Solution:** Use recursive pattern: at each level, flip 2 of 3 subtrees; recurse.
- **Cross-Project:** YES

### L5: Python stdout buffering in background exec on Windows
- **Category:** METHODOLOGY
- **Issue:** Background exec processes do not flush stdout, appearing stuck.
- **Solution:** Use flush=True or write to log file; use process tool poll/log.
- **Cross-Project:** YES

### L6: Git branch may be renamed by concurrent processes
- **Category:** GIT
- **Issue:** feature/ultrametric-v2-ternary-tree was renamed to feature/tree-distance-cophenetic mid-session.
- **Solution:** Check git branch --show-current before every commit; use reflog to recover.
- **Cross-Project:** YES

### L7: Exhaustive enumeration barrier is exponential in leaves, not depth
- **Category:** METHODOLOGY
- **Issue:** p=3 d=3 has 2^27 = 134M patterns — infeasible for exhaustive verification.
- **Solution:** Use constructive proof for d>=3; reserve exhaustive for d=1,2 (max 512 patterns).
- **Cross-Project:** YES

### L8: Strict Bruhat-Tits asymmetry is universal — not specific to p=2
- **Category:** MATHEMATICAL INSIGHT
- **Issue:** Every prime p introduces even-count nodes somewhere (internal for p=2, root for p>=3).
- **Solution:** Regular p-ary deviation (all nodes have p children) eliminates asymmetry for all odd p. Documented in 0.8.md §2.3.
- **Cross-Project:** YES
