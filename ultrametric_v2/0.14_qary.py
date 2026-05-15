"""
0.14_qary.py -- q-ary Alphabet Generalization for Ultrametric Trees

Extends the binary {0,1} encoding to q-ary {0,1,...,q-1} logical symbols.

Key changes:
- encode: all leaves set to the logical symbol s (0 <= s < q)
- decode: PLURALITY vote (most common child symbol wins; ties break to smallest)
- noise: each leaf flips to a random WRONG symbol with probability p_err
  (uniformly distributed among q-1 wrong symbols)

Barrier analysis:
- Adversarial barrier B_adv: ceil(p/2) errors, ALL targeting the same wrong symbol
- Random-scatter effect: errors distribute across q-1 wrong symbols, making
  it HARDER for any one wrong symbol to achieve plurality
- Effective barrier B_eff >= B_adv, growing with q
- For large q relative to p, errors scatter so broadly that plurality is
  essentially unflippable -- the tree becomes "thermodynamically stable"

Author: LLM-assisted implementation for ultrametric_v2 project
Date: 2026-05-16
Version: 0.14.0
"""

import random
import math
import json
import sys
import os
from typing import List, Tuple, Optional, Dict, Any
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util

spec = importlib.util.spec_from_file_location(
    'tree', os.path.join(os.path.dirname(os.path.abspath(__file__)), '0.10.py')
)
tree_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tree_mod)


# ============================================================================
# q-ary Voting
# ============================================================================

def plurality(values: List[int], q: int) -> int:
    """Return the most common value in `values` (ties break to smallest)."""
    counts = Counter(values)
    max_count = max(counts.values())
    # Find smallest symbol with max count
    for s in range(q):
        if counts.get(s, 0) == max_count:
            return s
    return 0  # fallback


def majority_threshold(p: int) -> int:
    """Minimum votes needed for strict majority: ceil(p/2)."""
    return (p + 1) // 2  # ceil(p/2) for integer p


# ============================================================================
# q-ary Tree Encoding/Decoding
# ============================================================================

def qary_encode(root: 'tree_mod.Node', symbol: int, q: int) -> None:
    """Encode a q-ary logical symbol by setting all leaf values."""
    if not (0 <= symbol < q):
        raise ValueError(f"symbol must be in [0, {q-1}], got {symbol}")
    for leaf in tree_mod.get_leaves(root):
        leaf.value = symbol


def qary_decode(root: 'tree_mod.Node', q: int) -> int:
    """Decode via bottom-up plurality vote (q-ary)."""
    def _decode(node):
        if node.is_leaf:
            return node.value
        child_values = [_decode(c) for c in node.children]
        result = plurality(child_values, q)
        node.value = result
        return result
    return _decode(root)


# ============================================================================
# q-ary Noise Model
# ============================================================================

def qary_apply_noise(root: 'tree_mod.Node', p_err: float, q: int,
                     rng: Optional[random.Random] = None) -> int:
    """Apply q-ary noise: each leaf flips to random wrong symbol with prob p_err.

    Returns total number of leaf flips.
    """
    if rng is None:
        rng = random.Random()

    leaves = tree_mod.get_leaves(root)
    flips = 0

    for leaf in leaves:
        if rng.random() < p_err:
            # Flip to a random WRONG symbol
            wrong_symbols = [s for s in range(q) if s != leaf.value]
            leaf.value = rng.choice(wrong_symbols)
            flips += 1

    return flips


# ============================================================================
# Monte Carlo
# ============================================================================

def qary_run_trial(depth: int, p_err: float, symbol: int, q: int, p: int = 3,
                   seed: Optional[int] = None) -> Tuple[bool, int, int]:
    """Single q-ary MC trial.

    Returns: (error_occurred, decoded_symbol, total_leaf_flips)
    """
    rng = random.Random(seed)
    tree = tree_mod.build_tree(depth, p=p)
    qary_encode(tree, symbol, q)
    flips = qary_apply_noise(tree, p_err, q, rng=rng)
    decoded = qary_decode(tree, q)
    error = (decoded != symbol)
    return error, decoded, flips


def qary_run_experiment(depth: int, p_err_list: List[float], q: int,
                        p: int = 3, n_trials: int = 500, seed: int = 42
                        ) -> Dict[str, Any]:
    """Run q-ary MC experiment across p_err values.

    Tests ONE symbol (since symmetry means all symbols are equivalent).
    """
    results = []
    for p_err in p_err_list:
        errors = 0
        total_flips = 0
        for trial in range(n_trials):
            trial_seed = seed + trial
            error_occurred, _, flips = qary_run_trial(
                depth, p_err, symbol=0, q=q, p=p, seed=trial_seed
            )
            if error_occurred:
                errors += 1
            total_flips += flips
        ler = errors / n_trials
        avg_flips = total_flips / n_trials
        results.append({
            'p_err': p_err,
            'errors': errors,
            'n_trials': n_trials,
            'ler': ler,
            'avg_flips': avg_flips
        })
    return {
        'p': p, 'q': q,
        'depth': depth,
        'leaves': p ** depth,
        'barrier_adversarial': majority_threshold(p) ** depth,
        'n_trials': n_trials,
        'results': results
    }


# ============================================================================
# Barrier Analysis
# ============================================================================

def qary_barrier_adversarial(p: int, d: int) -> int:
    """Adversarial barrier: ceil(p/2)^d errors all targeting same wrong symbol."""
    return majority_threshold(p) ** d


def qary_barrier_random_expected(p: int, d: int, q: int) -> float:
    """Expected minimum errors with random scatter.

    Under random scattering across q-1 wrong symbols, the effective number
    of errors needed to flip a node is approximately:
      B_eff = ceil(p/2) * (q-1)

    This is because only ~1/(q-1) of errors target any specific wrong symbol.
    At depth d: B_eff(d) = (ceil(p/2) * (q-1))^d

    This is a heuristic, not rigorous.
    """
    return (majority_threshold(p) * (q - 1)) ** d


def qary_barrier_analysis(p: int, q: int, max_d: int) -> List[Dict]:
    """Analyze barriers for q-ary encoding.

    Returns list of dicts with adversarial and random-scatter barriers per depth.
    """
    results = []
    for d in range(1, max_d + 1):
        B_adv = qary_barrier_adversarial(p, d)
        B_rand = qary_barrier_random_expected(p, d, q)
        leaves = p ** d
        results.append({
            'depth': d,
            'leaves': leaves,
            'B_adversarial': B_adv,
            'B_random_scatter': B_rand,
            'scatter_factor': B_rand / B_adv if B_adv > 0 else float('inf')
        })
    return results


# ============================================================================
# Cross-q Comparison
# ============================================================================

def compare_q_values(p: int, d: int, q_values: List[int],
                     p_err_list: List[float],
                     n_trials: int = 500, seed: int = 42) -> Dict[str, Any]:
    """Compare LER across different q values at same (p,d)."""
    comparison = {'p': p, 'd': d, 'leaves': p**d, 'n_trials': n_trials}
    comparison['results'] = {}

    for q in q_values:
        print(f"\n{'='*60}")
        print(f"q={q}: p={p} d={d} ({p**d} leaves, B_adv={qary_barrier_adversarial(p,d)})")
        print(f"{'='*60}")

        exp = qary_run_experiment(
            d, p_err_list, q, p=p, n_trials=n_trials, seed=seed
        )
        comparison['results'][str(q)] = exp

        for r in exp['results']:
            print(f"  p_err={r['p_err']:.2f}: LER={r['ler']:.4f} "
                  f"({r['errors']}/{r['n_trials']}), avg_flips={r['avg_flips']:.1f}")

    return comparison


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    print("=== q-ary Alphabet Generalization v0.14 ===")
    print()

    # Quick sanity
    p, d, q = 3, 3, 3
    rng = random.Random(42)
    tree = tree_mod.build_tree(d, p=p)
    qary_encode(tree, 1, q)
    flips = qary_apply_noise(tree, 0.20, q, rng=rng)
    decoded = qary_decode(tree, q)
    print(f"Sanity: p={p} d={d} q={q}, symbol=1, p_err=0.20")
    print(f"  Leaf flips: {flips}/{p**d}, decoded={decoded}, correct={decoded==1}")
    print()

    # Barrier analysis
    print("=== Barrier Analysis: Adversarial vs Random Scatter ===")
    print(f"{'depth':>6} {'B_adv':>8} {'B_rand(q=3)':>14} {'B_rand(q=5)':>14} {'B_rand(q=10)':>15}")
    print("-" * 63)
    for d in range(1, 7):
        B_adv = qary_barrier_adversarial(p, d)
        B_rand_3 = qary_barrier_random_expected(p, d, 3)
        B_rand_5 = qary_barrier_random_expected(p, d, 5)
        B_rand_10 = qary_barrier_random_expected(p, d, 10)
        print(f"{d:>6} {B_adv:>8} {B_rand_3:>14.0f} {B_rand_5:>14.0f} {B_rand_10:>15.0f}")
    print()

    # Cross-q comparison
    print("=== Cross-q LER Comparison ===")
    print("(p=3 d=3, 27 leaves, 300 trials)")
    compare_q_values(
        p=3, d=3,
        q_values=[2, 3, 5, 10],
        p_err_list=[0.10, 0.20, 0.30, 0.40],
        n_trials=300, seed=42
    )

    print()
    print("Module loaded successfully.")
