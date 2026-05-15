"""
0.14_run_qary_comparison.py -- Comprehensive q-ary LER Comparison

Runs p=3 d=2..4 at q=2,3,5,10 with 500 trials each.
"""
import sys, json, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util

spec = importlib.util.spec_from_file_location(
    'qary', os.path.join(os.path.dirname(os.path.abspath(__file__)), '0.14_qary.py')
)
qary_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qary_mod)

SEED = 42
N_TRIALS = 500
P_ERR_LIST = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
Q_VALUES = [2, 3, 5, 10]
DEPTHS = [2, 3, 4]
P = 3

all_results = {}

for d in DEPTHS:
    all_results[f'd{d}'] = {}
    for q in Q_VALUES:
        key = f'q{q}'
        print(f"\n{'='*60}")
        print(f"d={d} q={q}: p=3, {3**d} leaves, B_adv={qary_mod.qary_barrier_adversarial(3,d)}")
        print(f"{'='*60}")
        t0 = time.time()
        exp = qary_mod.qary_run_experiment(
            d, P_ERR_LIST, q, p=P, n_trials=N_TRIALS, seed=SEED
        )
        elapsed = time.time() - t0
        all_results[f'd{d}'][key] = exp
        for r in exp['results']:
            print(f"  p_err={r['p_err']:.2f}: LER={r['ler']:.4f} "
                  f"({r['errors']}/{r['n_trials']})")
        print(f"  Time: {elapsed:.1f}s")

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '0.14_qary_results.json')
with open(out_path, 'w') as f:
    json.dump(all_results, f, indent=2)
print(f"\nResults saved to {out_path}")

# Summary table
print("\n" + "=" * 80)
print("SUMMARY: LER at p_err=0.40")
print("=" * 80)
print(f"{'d':>4} {'Leaves':>8} {'q=2':>10} {'q=3':>10} {'q=5':>10} {'q=10':>10}")
print("-" * 56)
for d in DEPTHS:
    leaves = 3**d
    row = [f"{d:>4}", f"{leaves:>8}"]
    for q in Q_VALUES:
        exp = all_results[f'd{d}'][f'q{q}']
        ler = exp['results'][-1]['ler']  # last p_err = 0.40
        row.append(f"{ler:>10.4f}")
    print("".join(row))
