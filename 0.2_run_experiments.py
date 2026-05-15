"""
0.2_run_experiments.py -- Phase 2: Monte Carlo error confinement experiments.
Runs for depths 2..5, p_err 0.01..0.40, 500 trials, both logical bits.
Saves results to 0.2_results.json
"""
import sys
import os
import json
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import importlib.util
spec = importlib.util.spec_from_file_location('ultrametric',
    os.path.join(os.path.dirname(__file__), '0.1.py'))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

p_err_list = [0.01, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
depths = [2, 3, 4, 5]
n_trials = 500
base_seed = 42

all_results = {}

for depth in depths:
    for bit in [0, 1]:
        key = f"d{depth}_bit{bit}"
        print(f"Running: depth={depth}, bit={bit} ... ", end="", flush=True)
        t0 = time.time()
        result = mod.run_experiment(depth, p_err_list,
                                    n_trials=n_trials,
                                    seed=base_seed,
                                    logical_bit=bit)
        elapsed = time.time() - t0
        print(f"done in {elapsed:.1f}s")

        # Add Wilson CIs
        for r in result["results"]:
            lo, hi = mod.wilson_ci(r["errors"], r["n_trials"])
            r["ci_lower"] = lo
            r["ci_upper"] = hi

        all_results[key] = result

# Save results
outpath = os.path.join(os.path.dirname(__file__), "0.2_results.json")
with open(outpath, "w") as f:
    json.dump(all_results, f, indent=2)

print()
print("=== SUMMARY ===")
for depth in depths:
    for bit in [0, 1]:
        key = f"d{depth}_bit{bit}"
        res = all_results[key]
        max_ler = max(r["ler"] for r in res["results"])
        max_at = max(res["results"], key=lambda r: r["ler"])
        print(f"d={depth}, bit={bit}: max LER={max_ler:.4f} "
              f"at p_err={max_at['p_err']:.2f} "
              f"({max_at['errors']}/{max_at['n_trials']} errors)")

print()
print(f"Results saved to {outpath}")
