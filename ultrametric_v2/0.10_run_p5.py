"""
0.10_run_p5.py — p=5 Monte Carlo experiments
Runs d=2,3,4 for both logical bits (b0, b1).
Barrier: B(d) = ceil(5/2)^d = 3^d
"""
import sys, json, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util
spec = importlib.util.spec_from_file_location('tree', os.path.join(os.path.dirname(os.path.abspath(__file__)), '0.10.py'))
tree = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tree)

SEED = 42
P_ERR_LIST = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]

configs = [
    (2, 500),   # d=2: 25 leaves, B=9, 500 trials
    (3, 500),   # d=3: 125 leaves, B=27, 500 trials
    (4, 500),   # d=4: 625 leaves, B=81, 500 trials
]

all_results = {}

for d, n_trials in configs:
    for bit in [0, 1]:
        key = f"p5_d{d}_bit{bit}"
        print(f"\n{'='*60}")
        print(f"p=5 d={d} bit={bit} ({n_trials} trials, barrier={tree.barrier_formula(5,d)})")
        print(f"{'='*60}")
        t0 = time.time()
        result = tree.run_experiment(d, P_ERR_LIST, n_trials=n_trials,
                                     seed=SEED, logical_bit=bit, p=5)
        elapsed = time.time() - t0
        all_results[key] = result

        # Print summary
        for r in result['results']:
            ler = r['ler']
            ci_lo = r['ci_lower']
            ci_hi = r['ci_upper']
            err_lo = 1.0 - ci_hi  # error rate CI lower
            err_hi = 1.0 - ci_lo  # error rate CI upper
            print(f"  p_err={r['p_err']:.2f}: errors={r['errors']}/{r['n_trials']} "
                  f"LER={ler:.4f} CI_err=[{err_lo:.4f}, {err_hi:.4f}]")
        print(f"  Time: {elapsed:.1f}s")

# Save results
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '0.10_p5_results.json')
with open(output_path, 'w') as f:
    json.dump(all_results, f, indent=2)
print(f"\nResults saved to {output_path}")
print(f"Total experiments: {len(all_results)}")
