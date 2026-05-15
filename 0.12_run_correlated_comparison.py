"""
0.12_run_correlated_comparison.py — Comprehensive Correlated Noise Study

Compares tree vs classical under correlated noise at:
- p=3 d=3,4 (N=27,81)
- p=5 d=3 (N=125)
- p_corr = 0.0, 0.25, 0.50, 0.75
- k=2 neighbors
- 1000 trials per condition
"""
import sys, json, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util

spec = importlib.util.spec_from_file_location(
    'corr', os.path.join(os.path.dirname(os.path.abspath(__file__)), '0.12_correlated_noise.py')
)
corr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(corr)

SEED = 42
N_TRIALS = 1000
P_ERR_BASE_LIST = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35]
P_CORR_LIST = [0.0, 0.25, 0.50, 0.75]
K = 2

all_results = {}

for p, d in [(3, 3), (3, 4), (5, 3)]:
    N = p ** d
    key = f"p{p}_d{d}"
    all_results[key] = {}
    
    for p_corr in P_CORR_LIST:
        print(f"\n{'='*60}")
        print(f"p={p} d={d} N={N:,} p_corr={p_corr}")
        print(f"{'='*60}")
        
        # Tree
        t0 = time.time()
        tree_exp = corr.run_experiment_correlated(
            runner_fn=corr.run_trial_correlated_tree,
            p_err_base_list=P_ERR_BASE_LIST,
            p_corr=p_corr, k=K, n_trials=N_TRIALS, seed=SEED,
            depth=d, logical_bit=0, p=p
        )
        tree_elapsed = time.time() - t0
        
        # Classical
        t0 = time.time()
        cl_exp = corr.run_experiment_correlated(
            runner_fn=corr.run_trial_correlated_classical,
            p_err_base_list=P_ERR_BASE_LIST,
            p_corr=p_corr, k=K, n_trials=N_TRIALS, seed=SEED,
            n_bits=N, logical_bit=0
        )
        cl_elapsed = time.time() - t0
        
        all_results[key][str(p_corr)] = {
            'tree': tree_exp,
            'classical': cl_exp
        }
        
        # Print results
        print(f"\n{'p_err':>8} {'Tree LER':>10} {'Tree phys':>10} "
              f"{'CL LER':>10} {'CL phys':>10} {'Winner':>10}")
        print("-" * 62)
        for i, p_err_base in enumerate(P_ERR_BASE_LIST):
            tr = tree_exp['results'][i]
            cl = cl_exp['results'][i]
            tree_ler = tr['ler']
            cl_ler = cl['ler']
            if tree_ler < cl_ler:
                winner = "TREE"
            elif cl_ler < tree_ler:
                winner = "CL"
            else:
                winner = "TIE"
            print(f"{p_err_base:>8.2f} {tree_ler:>10.4f} {tr['avg_physical_errors']:>10.1f} "
                  f"{cl_ler:>10.4f} {cl['avg_physical_errors']:>10.1f} {winner:>10}")
        print(f"  Time: tree={tree_elapsed:.1f}s, cl={cl_elapsed:.1f}s")

# Save results
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '0.12_correlated_results.json')
with open(out_path, 'w') as f:
    json.dump(all_results, f, indent=2)
print(f"\nResults saved to {out_path}")
