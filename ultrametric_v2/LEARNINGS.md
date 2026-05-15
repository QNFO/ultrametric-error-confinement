# LEARNINGS — Ultrametric Error Confinement v2

## Session 2026-05-15

### L1: PowerShell ls -la not supported on Windows
- **Category:** METHODOLOGY
- **Issue:** PowerShell does not recognize -la flag.
- **Solution:** Use Python for file system operations on Windows.
- **Prevention:** Always use Python for cross-platform file operations.
- **Cross-Project:** YES

### L2: Monorepo with project subdirectories requires discipline
- **Category:** GIT
- **Issue:** Working directory maps to repo root but project files live in subdirectories.
- **Solution:** Use repo-root-relative paths and verify with git status.
- **Prevention:** Run git rev-parse --show-toplevel at session start.
- **Cross-Project:** YES

### L3: Write tool may silently fail after multiple calls
- **Category:** METHODOLOGY
- **Issue:** After ~4 successful writes, subsequent writes returned permission-like error strings instead of success.
- **Solution:** Fall back to Python exec for batch file writes.
- **Prevention:** Use Python for bulk file creation; reserve write tool for single-file edits.
- **Cross-Project:** YES
