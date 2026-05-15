# CHANGELOG -- Ultrametric Error Confinement v2

## [0.1.0] -- 2026-05-15

### What Changed
- **Created project:** `ultrametric_v2/` under `G:\My Drive\projects\`
- **Git:** Created `feature/ultrametric-v2-ternary-tree` branch
- **Documentation:** Created all 7 mandatory project files
- **Phase 1:** Implemented ternary tree module (`0.1.py`) with:
  - `build_tree(depth, p=3)`: Regular ternary tree (root degree=3)
  - `encode(root, bit)`: Set all leaf values
  - `decode(root)`: Bottom-up majority vote (no ties)
  - `apply_noise(root, p_err)`: i.i.d. bit-flip noise
  - `run_trial()` / `run_experiment()`: Monte Carlo framework
  - `wilson_ci()`: Wilson confidence intervals
  - `energy_barrier()`: B(d) = 2^d calculation
  - Self-tests pass (tree construction, roundtrip, noise, copy)
- **Phase 2:** Monte Carlo experiments completed:
  - Depths: d = 2, 3, 4, 5 (500 trials), d = 6 (1000 trials)
  - p_err: 0.01 to 0.40 in 9 steps
  - Both logical bits (0 and 1)
  - **Perfect symmetry confirmed:** Identical LER for both bits
  - **Key result at p_err=0.40:** LER = 0.248 (d=2) -> 0.010 (d=5) -> 0.002 (d=6)
  - **Zero errors up to p_err=0.35 at d=6** (1000 trials)

### Files Changed
- `ultrametric_v2/README.md` -- CREATE
- `ultrametric_v2/PROJECT STATE.md` -- CREATE
- `ultrametric_v2/SPRINT.md` -- CREATE
- `ultrametric_v2/CHANGELOG.md` -- CREATE
- `ultrametric_v2/BACKLOG.md` -- CREATE
- `ultrametric_v2/LEARNINGS.md` -- CREATE
- `ultrametric_v2/DECISIONS.md` -- CREATE
- `ultrametric_v2/.gitignore` -- CREATE
- `ultrametric_v2/0.1.py` -- CREATE (ternary tree module, 258 lines)
- `ultrametric_v2/0.2_run_experiments.py` -- CREATE (experiment runner)
- `ultrametric_v2/0.2_results.json` -- CREATE (all experiment data)
- `ultrametric_v2/0.3_run_d6.py` -- CREATE (d=6 extended runner)

### Git
- Branch: `feature/ultrametric-v2-ternary-tree`
- Commits:
  - `124539f` -- Project documentation setup
  - `7242115` -- 0.1.py ternary tree module
  - `d13efb6` -- Phase 2 experiment results
