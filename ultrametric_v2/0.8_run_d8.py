"""
d=8 runner — split mode: runs one logical bit, saves results immediately.
Merges with existing results file if present.
Usage: python 0.8_run_d8.py [0|1]   (default: runs both sequentially)
"""
import sys, os, json, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util
spec = importlib.util.spec_from_file_location("ultrametric",
    os.path.join(os.path.dirname(__file__), "0.1.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

p_err_list = [0.01, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
depth = 8
n_trials = 2000
base_seed = 42
outpath = os.path.join(os.path.dirname(__file__), "0.2_results.json")

bit = int(sys.argv[1]) if len(sys.argv) > 1 else 0

key = f"d{depth}_bit{bit}"
print(f"Running: depth={depth}, bit={bit} ... ", end="", flush=True)
t0 = time.time()
result = mod.run_experiment(depth, p_err_list, n_trials=n_trials,
                            seed=base_seed, logical_bit=bit)
elapsed = time.time() - t0
print(f"done in {elapsed:.1f}s", flush=True)

for r in result["results"]:
    lo, hi = mod.wilson_ci(r["errors"], r["n_trials"])
    r["ci_lower"] = lo
    r["ci_upper"] = hi

# Load existing, merge, save
try:
    with open(outpath) as f:
        existing = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    existing = {}
existing[key] = result

with open(outpath, "w") as f:
    json.dump(existing, f, indent=2)

total_errs = sum(r["errors"] for r in result["results"])
print(f"d={depth}, bit={bit}: {total_errs} total errors in {n_trials*9} trials")
for r in result["results"]:
    print(f"  p_err={r['p_err']:.2f}: {r['errors']}/{n_trials} errors, "
          f"LER={r['ler']:.4f}, CI=[{r['ci_lower']:.4f}, {r['ci_upper']:.4f}]")

print(f"\nResults saved to {outpath}")
