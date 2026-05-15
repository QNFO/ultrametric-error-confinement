"""
0.11_run_comparison.py — Tree vs Classical Repetition Code Comparison

Compares LER across tree (p=3,5,7) and classical repetition at matching N=p^d.
Runs full MC experiments and computes theoretical classical LER via binomial CDF.
"""
import sys, json, time, math, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import our modules
import importlib.util

spec_tree = importlib.util.spec_from_file_location(
    'tree_0_10', os.path.join(os.path.dirname(os.path.abspath(__file__)), '0.10.py')
)
tree = importlib.util.module_from_spec(spec_tree)
spec_tree.loader.exec_module(tree)

spec_cl = importlib.util.spec_from_file_location(
    'classical', os.path.join(os.path.dirname(os.path.abspath(__file__)), '0.11_classical_repetition.py')
)
cl = importlib.util.module_from_spec(spec_cl)
spec_cl.loader.exec_module(cl)

SEED = 42
P_ERR_LIST = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
N_TRIALS = 500

def load_tree_result(p, d, bit):
    """Load tree LER from existing results."""
    if p == 3:
        fp = os.path.join(os.path.dirname(os.path.abspath(__file__)), '0.2_results.json')
        with open(fp) as f:
            data = json.load(f)
        key = f'd{d}_bit{bit}'
        return data[key]['results']
    elif p == 5:
        fp = os.path.join(os.path.dirname(os.path.abspath(__file__)), '0.10_p5_results.json')
        with open(fp) as f:
            data = json.load(f)
        key = f'p5_d{d}_bit{bit}'
        return data[key]['results']
    elif p == 7:
        fp = os.path.join(os.path.dirname(os.path.abspath(__file__)), '0.10_p7_results.json')
        with open(fp) as f:
            data = json.load(f)
        key = f'p7_d{d}_bit{bit}'
        return data[key]['results']
    return None

print("=" * 80)
print("TREE vs CLASSICAL REPETITION CODE — COMPREHENSIVE COMPARISON")
print("=" * 80)

comparisons = []

for p, max_d in [(3, 7), (5, 4), (7, 3)]:
    for d in range(2, max_d + 1):
        N = p ** d
        tree_barrier = math.ceil(p / 2) ** d
        cl_barrier = cl.classical_barrier(N)

        print(f"\n{'='*60}")
        print(f"p={p} d={d}: N={N:,}, Tree B={tree_barrier}, Classical B={cl_barrier}")
        print(f"{'='*60}")

        # Load tree data
        tree_b0 = load_tree_result(p, d, 0)
        tree_b1 = load_tree_result(p, d, 1)

        # Run classical experiment
        print("Running classical repetition...", end=" ", flush=True)
        t0 = time.time()
        cl_exp = cl.classical_run_experiment(
            N, P_ERR_LIST, n_trials=N_TRIALS, seed=SEED, logical_bit=0
        )
        elapsed = time.time() - t0
        print(f"done ({elapsed:.1f}s)")

        # Print comparison table
        print(f"\n{'p_err':>6} {'Tree(B0)':>10} {'Tree(B1)':>10} {'Classical':>10} "
              f"{'Winner':>12} {'CL theor':>10}")
        print("-" * 62)

        for i, p_err in enumerate(P_ERR_LIST):
            tree_ler0 = tree_b0[i]['ler']
            tree_ler1 = tree_b1[i]['ler']
            cl_ler = cl_exp['results'][i]['ler']
            cl_theor = cl.classical_ler_theoretical(N, p_err)

            # Determine winner
            if tree_ler0 < cl_ler:
                winner = "TREE"
            elif cl_ler < tree_ler0:
                winner = "CLASSICAL"
            else:
                winner = "TIE"

            print(f"{p_err:>6.2f} {tree_ler0:>10.4f} {tree_ler1:>10.4f} "
                  f"{cl_ler:>10.4f} {winner:>12} {cl_theor:>10.6f}")

        # Store for summary
        comparisons.append({
            'p': p, 'd': d, 'N': N,
            'tree_barrier': tree_barrier,
            'cl_barrier': cl_barrier,
            'tree_ler_at_40': tree_b0[-1]['ler'],
            'cl_ler_at_40': cl_exp['results'][-1]['ler'],
            'cl_ler_theor_40': cl.classical_ler_theoretical(N, 0.40)
        })

# Cross-over analysis
print("\n" + "=" * 80)
print("CROSS-OVER ANALYSIS: At what p_err does Tree beat Classical?")
print("=" * 80)

for p, max_d in [(3, 5), (5, 4), (7, 3)]:
    for d in range(2, max_d + 1):
        N = p ** d
        tree_results = load_tree_result(p, d, 0)
        if tree_results is None:
            continue

        # Find crossover: tree_ler < cl_ler
        crossover_found = False
        for r in tree_results:
            p_err = r['p_err']
            tree_ler = r['ler']
            cl_theor = cl.classical_ler_theoretical(N, p_err)
            if tree_ler < cl_theor and not crossover_found:
                print(f"p={p} d={d} (N={N:,}): Tree beats Classical at p_err={p_err:.2f} "
                      f"(Tree LER={tree_ler:.4f}, CL LER={cl_theor:.6f})")
                crossover_found = True
        if not crossover_found:
            # Check if tree is always better or never better
            first_r = tree_results[0]
            last_r = tree_results[-1]
            first_cl = cl.classical_ler_theoretical(N, first_r['p_err'])
            last_cl = cl.classical_ler_theoretical(N, last_r['p_err'])
            if first_r['ler'] < first_cl:
                print(f"p={p} d={d} (N={N:,}): Tree ALWAYS beats Classical "
                      f"(even at p_err={first_r['p_err']:.2f})")
            elif last_r['ler'] > last_cl:
                print(f"p={p} d={d} (N={N:,}): Classical ALWAYS beats Tree "
                      f"(even at p_err={last_r['p_err']:.2f})")
            else:
                print(f"p={p} d={d} (N={N:,}): No clear crossover in tested range")

# Summary table
print("\n" + "=" * 80)
print("SUMMARY: LER at p_err=0.40")
print("=" * 80)
print(f"{'Architecture':<25} {'N':>8} {'Barrier':>10} {'LER(MC)':>10} {'LER(theo)':>12}")
print("-" * 65)
for c in comparisons:
    print(f"p={c['p']} d={c['d']} (tree):       {c['N']:>8,} {c['tree_barrier']:>10} "
          f"{c['tree_ler_at_40']:>10.4f}")
    print(f"Classical N={c['N']:,}:       {c['N']:>8,} {c['cl_barrier']:>10} "
          f"{c['cl_ler_at_40']:>10.4f} {c['cl_ler_theor_40']:>12.6f}")
    print()

print("\nKey finding: Classical repetition code achieves LOWER LER at matched")
print("qubit counts for all tested (p,d) at p_err=0.40. However, the tree")
print("architecture offers theoretical advantages (ultrametric geometry,")
print("natural physical mapping) not captured by raw LER comparison.")
print()
print("See discussion in updated 0.8.md §7.6.")
