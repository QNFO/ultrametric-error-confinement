# LEARNINGS -- Ultrametric Error Confinement v2

## Session 2026-05-15

### L1: PowerShell ls -la not supported on Windows
- Category: METHODOLOGY
- Issue: PowerShell does not recognize -la flag.
- Solution: Use Python for file system operations on Windows.
- Prevention: Always use Python for cross-platform file operations.
- Cross-Project: YES

### L2: Monorepo with project subdirectories requires discipline
- Category: GIT
- Issue: Working directory maps to repo root, project files in subdirectories.
- Solution: Use repo-root-relative paths in git commands.
- Prevention: Run git rev-parse --show-toplevel at session start.
- Cross-Project: YES

### L3: Write tool may silently fail after multiple calls
- Category: METHODOLOGY
- Issue: After ~4 successful writes, subsequent writes returned permission-like errors.
- Solution: Fall back to Python exec for batch file writes.
- Prevention: Use Python for bulk file creation; reserve write tool for single-file edits.
- Cross-Project: YES

### L4: Constructive barrier pattern requires recursive design
- Category: METHODOLOGY
- Issue: Naive barrier pattern (flipping consecutive leaves) does not flip the root because leaf order does not align with subtree boundaries.
- Solution: Use recursive pattern: at each level, flip 2 of 3 subtrees; recurse.
- Prevention: Always verify constructive proofs against actual tree decode.
- Cross-Project: YES

### L5: Python stdout buffering in background exec on Windows
- Category: METHODOLOGY
- Issue: Background exec processes do not flush stdout, appearing stuck.
- Solution: Use flush=True or write to log file; use process tool poll/log.
- Prevention: For long tasks, write intermediate results to a file.
- Cross-Project: YES
