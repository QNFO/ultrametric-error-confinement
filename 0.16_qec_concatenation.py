"""
0.16_qec_concatenation.py -- Tree + QEC Concatenation at Leaf Level

Concatenates the tree architecture with an inner repetition code at each leaf.
Each tree leaf is itself M physical qubits encoded as a repetition code.

Architecture:
- Outer code: Tree of depth d, p children per node (barrier = ceil(p/2)^d)
- Inner code: Each leaf encoded as M-bit repetition (barrier = ceil(M/2))
- Total physical qubits: p^d * M
- Effective barrier: depends on error propagation through both layers

Comparison at matched total qubit count:
- Concatenated: tree(d1) * inner(M), total = p^d1 * M
- Pure tree d2: total = p^d2
- Pure repetition: total = N

Author: LLM-assisted implementation for ultrametric_v2 project
Date: 2026-05-16
Version: 0.16.0
"""
import random, math, json, sys, os, itertools
from typing import List, Tuple, Optional, Dict, Any
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util
spec = importlib.util.spec_from_file_location('tree', os.path.join(os.path.dirname(os.path.abspath(__file__)), '0.10.py'))
tree_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tree_mod)

# ============================================================================
# Concatenated Encoding / Decoding
# ============================================================================
def concatenated_encode(root, logical_bit, m):
    """Encode logical bit: set all tree leaves, then each leaf = m copies."""
    tree_mod.encode(root, logical_bit)
    # Store m per leaf as attribute (simulated -- just note the multiplicity)
    root._inner_reps = m

def concatenated_decode(root, m):
    """Decode: first decode each leaf (majority over m bits), then tree majority."""
    def _decode_leaf(leaf_val, m_bits_error_count):
        """Simulate inner majority: if >= ceil(m/2) errors, leaf flips."""
        threshold = (m + 1) // 2
        return 1 - leaf_val if m_bits_error_count >= threshold else leaf_val

    def _decode(node):
        if node.is_leaf:
            # Simulate inner code: get errors from leaf's m physical qubits
            # leaf_errs = how many of m bits flipped (determined during noise)
            leaf_val = node.value
            leaf_errs = getattr(node, '_inner_errors', 0)
            return _decode_leaf(leaf_val, leaf_errs)
        child_values = [_decode(c) for c in node.children]
        result = tree_mod._majority(child_values)
        node.value = result
        return result
    return _decode(root)

# ============================================================================
# Concatenated Noise Model
# ============================================================================
def concatenated_apply_noise(root, p_err, m, rng=None):
    """Apply noise: each physical qubit (m per leaf) flips independently with p_err.
    Then count per-leaf errors for inner decoding.
    Returns total physical bit flips.
    """
    if rng is None:
        rng = random.Random()
    leaves = tree_mod.get_leaves(root)
    total_flips = 0
    for leaf in leaves:
        leaf_errs = 0
        for _ in range(m):
            if rng.random() < p_err:
                leaf_errs += 1
                total_flips += 1
        leaf._inner_errors = leaf_errs
    return total_flips

def concatenated_run_trial(depth, p_err, logical_bit, m, p=3, seed=None):
    """Single concatenated trial."""
    rng = random.Random(seed)
    tree = tree_mod.build_tree(depth, p=p)
    concatenated_encode(tree, logical_bit, m)
    flips = concatenated_apply_noise(tree, p_err, m, rng=rng)
    decoded = concatenated_decode(tree, m)
    error = (decoded != logical_bit)
    return error, decoded, flips

# ============================================================================
# Monte Carlo
# ============================================================================
def concatenated_run_experiment(depth, p_err_list, m, p=3, n_trials=500, seed=42):
    results = []
    for p_err in p_err_list:
        errors = 0; total_flips = 0
        for t in range(n_trials):
            err, _, flips = concatenated_run_trial(depth, p_err, 0, m, p=p, seed=seed+t)
            if err: errors += 1
            total_flips += flips
        ler = errors / n_trials
        results.append({'p_err':p_err, 'errors':errors, 'n_trials':n_trials,
                        'ler':ler, 'avg_flips':total_flips/n_trials})
    return {'depth':depth, 'p':p, 'm':m, 'total_qubits':(p**depth)*m,
            'results':results}

# ============================================================================
# Comparison: Concatenated vs Pure Tree vs Pure Rep at matched qubits
# ============================================================================
def run_matched_comparison():
    """Compare three architectures at approximately matched total physical qubits."""
    p = 3; n_trials = 500; seed = 42
    p_err_list = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]

    configs = [
        # (label, type, params, total_qubits)
        ('Tree d=3 (pure)', 'tree', {'depth':3, 'p':3}, 27),
        ('Tree d=4 (pure)', 'tree', {'depth':4, 'p':3}, 81),
        ('Tree d=5 (pure)', 'tree', {'depth':5, 'p':3}, 243),
        ('Tree+Rep d=2 m=3', 'concat', {'depth':2, 'm':3, 'p':3}, 27),
        ('Tree+Rep d=2 m=9', 'concat', {'depth':2, 'm':9, 'p':3}, 81),
        ('Tree+Rep d=3 m=3', 'concat', {'depth':3, 'm':3, 'p':3}, 81),
        ('Tree+Rep d=3 m=9', 'concat', {'depth':3, 'm':9, 'p':3}, 243),
        ('Rep N=27', 'rep', {'n_bits':27}, 27),
        ('Rep N=81', 'rep', {'n_bits':81}, 81),
        ('Rep N=243', 'rep', {'n_bits':243}, 243),
    ]

    all_results = {}
    for label, typ, params, qubits in configs:
        print(f"\n{'='*60}")
        print(f"{label}: {qubits} total qubits")
        print(f"{'='*60}")

        if typ == 'tree':
            from importlib import reload
            exp = tree_mod.run_experiment(params['depth'], p_err_list,
                                          n_trials=n_trials, seed=seed,
                                          logical_bit=0, p=params['p'])
            exp['total_qubits'] = qubits
            exp['label'] = label
            all_results[label] = exp
            for r in exp['results']:
                print(f"  p_err={r['p_err']:.2f}: LER={r['ler']:.4f}")

        elif typ == 'concat':
            exp = concatenated_run_experiment(params['depth'], p_err_list,
                                              params['m'], p=params['p'],
                                              n_trials=n_trials, seed=seed)
            exp['label'] = label
            all_results[label] = exp
            for r in exp['results']:
                print(f"  p_err={r['p_err']:.2f}: LER={r['ler']:.4f}")

        elif typ == 'rep':
            from importlib.util import spec_from_file_location
            spec2 = spec_from_file_location('cl', os.path.join(os.path.dirname(os.path.abspath(__file__)), '0.11_classical_repetition.py'))
            cl = importlib.util.module_from_spec(spec2)
            spec2.loader.exec_module(cl)
            exp = cl.classical_run_experiment(params['n_bits'], p_err_list,
                                              n_trials=n_trials, seed=seed)
            exp['total_qubits'] = qubits
            exp['label'] = label
            all_results[label] = exp
            for r in exp['results']:
                ler = r['ler']
                print(f"  p_err={r['p_err']:.2f}: LER={ler:.4f}")

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY: LER at p_err=0.40")
    print("=" * 80)
    print(f"{'Architecture':<25} {'Qubits':>8} {'LER':>10} {'Winner per Q':>14}")
    print("-" * 62)
    # Group by qubit count
    for q in [27, 81, 243]:
        group = {k: v for k, v in all_results.items() if v.get('total_qubits', 0) == q}
        if not group:
            continue
        best_ler = min(v['results'][-1]['ler'] for v in group.values())
        for label, exp in group.items():
            ler = exp['results'][-1]['ler']
            marker = " <-- BEST" if abs(ler - best_ler) < 1e-6 else ""
            print(f"{label:<25} {q:>8} {ler:>10.4f}{marker}")
        print()

    return all_results

if __name__ == "__main__":
    print("=== QEC Concatenation v0.16 ===")
    import time
    t0 = time.time()
    results = run_matched_comparison()
    elapsed = time.time() - t0
    print(f"Total time: {elapsed:.1f}s")

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '0.16_qec_results.json')
    # Simplify for JSON serialization
    simple = {}
    for k, v in results.items():
        simple[k] = {
            'label': v.get('label', k),
            'total_qubits': v.get('total_qubits', 0),
            'results': v['results']
        }
    with open(out, 'w') as f:
        json.dump(simple, f, indent=2)
    print(f"Results saved to {out}")
