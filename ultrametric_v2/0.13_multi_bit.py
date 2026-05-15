"""
0.13_multi_bit.py — Multi-Bit Logical Encoding on General-p Trees

Encodes multiple logical bits by partitioning tree at split depth k.
Each of the p^k subtrees at depth k independently encodes one logical bit.

Trade-off:
- Total logical bits: p^k
- Leaves per subtree (per logical bit): p^(d-k)
- Barrier per bit: ceil(p/2)^(d-k)
- Total physical qubits: p^d

Example: p=3, d=5, k=2
- 9 logical bits, each using 3^3=27 leaves, each with barrier 2^3=8
- Total physical qubits: 243 (unchanged from single-bit d=5)

Author: LLM-assisted implementation for ultrametric_v2 project
Date: 2026-05-16
Version: 0.13.0
"""

import random
import math
import json
import sys
import os
from typing import List, Tuple, Optional, Dict, Any, Set

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util

spec = importlib.util.spec_from_file_location(
    'tree', os.path.join(os.path.dirname(os.path.abspath(__file__)), '0.10.py')
)
tree_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tree_mod)


# ============================================================================
# Multi-Bit Encoding
# ============================================================================

def get_nodes_at_depth(root: 'tree_mod.Node', target_depth: int
                       ) -> List['tree_mod.Node']:
    """Return all nodes at a specific depth in the tree."""
    nodes = []
    def _collect(node):
        if node.depth == target_depth:
            nodes.append(node)
        elif node.depth < target_depth:
            for child in node.children:
                _collect(child)
    _collect(root)
    return nodes


def multi_bit_encode(root: 'tree_mod.Node', logical_bits: List[int],
                     split_depth: int) -> None:
    """Encode multiple logical bits by partitioning at split_depth.

    Each subtree rooted at a node at depth split_depth encodes one logical bit.
    logical_bits[i] is encoded into subtree i (ordered by DFS at split_depth).

    All leaves outside the subtrees (above split_depth) are set to 0
    (they don't participate in majority votes for any logical bit since
    subtrees are rooted at split_depth).

    Actually: we encode all leaves in each subtree. The subtrees at
    split_depth are independent — their roots are at depth split_depth,
    and decoding starts from those roots.
    """
    subtree_roots = get_nodes_at_depth(root, split_depth)

    if len(logical_bits) != len(subtree_roots):
        raise ValueError(
            f"Need {len(subtree_roots)} logical bits (one per subtree), "
            f"got {len(logical_bits)}"
        )

    for i, subtree_root in enumerate(subtree_roots):
        bit = logical_bits[i]
        leaves = tree_mod.get_leaves(subtree_root)
        for leaf in leaves:
            leaf.value = bit


def multi_bit_decode(root: 'tree_mod.Node', split_depth: int
                     ) -> List[int]:
    """Decode multiple logical bits from subtree partitions.

    Decodes each subtree independently from its root at split_depth.
    Returns list of decoded bits in DFS order of subtree roots.
    """
    subtree_roots = get_nodes_at_depth(root, split_depth)

    # Decode each subtree independently
    # We need to decode from the subtree root, not the global root
    decoded = []
    for subtree_root in subtree_roots:
        bit = tree_mod.decode(subtree_root)
        decoded.append(bit)

    return decoded


def multi_bit_trial(depth: int, split_depth: int, n_bits: int,
                    p_err: float, p: int = 3,
                    seed: Optional[int] = None
                    ) -> Tuple[List[int], List[int], int, int]:
    """Run a single multi-bit MC trial.

    Returns:
    - encoded: list of encoded logical bits
    - decoded: list of decoded logical bits
    - bit_errors: number of logical bit errors
    - total_leaf_errors: total leaf flips applied
    """
    if n_bits != p ** split_depth:
        raise ValueError(f"n_bits={n_bits} must equal p^split_depth={p**split_depth}")

    rng = random.Random(seed)

    # Build tree
    tree = tree_mod.build_tree(depth, p=p)

    # Generate random logical bits
    encoded = [rng.randint(0, 1) for _ in range(n_bits)]

    # Encode
    multi_bit_encode(tree, encoded, split_depth)

    # Apply noise to all leaves
    flip_info = tree_mod.apply_noise(tree, p_err, rng=rng)
    total_leaf_errors = sum(1 for f in flip_info if f)

    # Decode each subtree independently
    decoded = multi_bit_decode(tree, split_depth)

    # Count bit errors
    bit_errors = sum(1 for e, d in zip(encoded, decoded) if e != d)

    return encoded, decoded, bit_errors, total_leaf_errors


def multi_bit_experiment(depth: int, split_depth: int, p_err_list: List[float],
                         n_trials: int = 500, seed: int = 42, p: int = 3
                         ) -> Dict[str, Any]:
    """Run multi-bit MC experiment.

    Returns dict with per-p_err results and summary statistics.
    """
    n_bits = p ** split_depth
    leaves_per_bit = p ** (depth - split_depth)
    barrier_per_bit = tree_mod.barrier_formula(p, depth - split_depth)

    results = []
    for p_err in p_err_list:
        bit_errors_total = 0
        trials_with_errors = 0
        total_leaf_flips = 0

        for trial in range(n_trials):
            trial_seed = seed + trial
            _, _, bit_errors, leaf_flips = multi_bit_trial(
                depth, split_depth, n_bits, p_err, p=p, seed=trial_seed
            )
            bit_errors_total += bit_errors
            if bit_errors > 0:
                trials_with_errors += 1
            total_leaf_flips += leaf_flips

        # BER (bit error rate) = bit errors / (n_bits * n_trials)
        ber = bit_errors_total / (n_bits * n_trials)

        # Fraction of trials with at least one bit error
        trial_error_rate = trials_with_errors / n_trials

        # Average leaf flips per trial
        avg_leaf_flips = total_leaf_flips / n_trials

        results.append({
            'p_err': p_err,
            'n_trials': n_trials,
            'bit_errors': bit_errors_total,
            'total_bits_tested': n_bits * n_trials,
            'ber': ber,
            'trial_error_rate': trial_error_rate,
            'avg_leaf_flips': avg_leaf_flips,
            'trials_with_errors': trials_with_errors
        })

    return {
        'p': p,
        'depth': depth,
        'split_depth': split_depth,
        'n_logical_bits': n_bits,
        'leaves_per_bit': leaves_per_bit,
        'barrier_per_bit': barrier_per_bit,
        'total_leaves': p ** depth,
        'n_trials': n_trials,
        'results': results
    }


# ============================================================================
# Independence Test
# ============================================================================

def test_independence(depth: int, split_depth: int, p_err: float,
                      p: int = 3, n_trials: int = 1000,
                      seed: int = 42) -> Dict[str, Any]:
    """Test that logical bits in different subtrees are independent.

    Encodes bit 0 in one subtree and bit 1 in another, verifies no cross-correlation.
    """
    n_bits = p ** split_depth
    rng = random.Random(seed)

    # Track correlation: for each pair of subtrees (i,j), count when
    # bit i was correct and bit j was also correct (independence implies
    # P(i_correct and j_correct) = P(i_correct) * P(j_correct))
    subtree_correct = [0] * n_bits
    subtree_pair_correct = [[0] * n_bits for _ in range(n_bits)]
    subtree_total = [0] * n_bits

    for trial in range(n_trials):
        trial_seed = seed + trial
        encoded, decoded, _, _ = multi_bit_trial(
            depth, split_depth, n_bits, p_err, p=p, seed=trial_seed
        )

        # Identify correct subtrees
        correct = [e == d for e, d in zip(encoded, decoded)]

        for i in range(n_bits):
            subtree_total[i] += 1
            if correct[i]:
                subtree_correct[i] += 1
            for j in range(n_bits):
                if correct[i] and correct[j]:
                    subtree_pair_correct[i][j] += 1

    # Compute correlation metrics
    results = {}
    for i in range(n_bits):
        p_i = subtree_correct[i] / subtree_total[i]
        for j in range(i + 1, n_bits):
            p_j = subtree_correct[j] / subtree_total[j]
            p_ij = subtree_pair_correct[i][j] / n_trials
            # Under independence: p_ij = p_i * p_j
            expected_p_ij = p_i * p_j
            deviation = abs(p_ij - expected_p_ij)
            results[f'pair_{i}_{j}'] = {
                'p_i': p_i, 'p_j': p_j,
                'p_ij': p_ij,
                'expected_p_ij': expected_p_ij,
                'deviation': deviation
            }

    # Summary: average deviation and max deviation
    deviations = [r['deviation'] for r in results.values()]
    avg_dev = sum(deviations) / len(deviations) if deviations else 0
    max_dev = max(deviations) if deviations else 0

    return {
        'n_bits': n_bits,
        'per_bit_accuracy': [subtree_correct[i] / subtree_total[i] for i in range(n_bits)],
        'avg_pair_deviation': avg_dev,
        'max_pair_deviation': max_dev,
        'pair_results': results
    }


# ============================================================================
# Comparison: Single-bit vs Multi-bit
# ============================================================================

def compare_single_vs_multi(p: int, d: int, split_depths: List[int],
                            p_err_list: List[float],
                            n_trials: int = 500, seed: int = 42
                            ) -> Dict[str, Any]:
    """Compare single-bit encoding vs multi-bit at various split depths.

    Same total physical qubits, different logical bit capacities.
    """
    comparison = {
        'p': p, 'd': d, 'total_leaves': p ** d,
        'n_trials': n_trials,
        'configs': {}
    }

    # Single-bit (split_depth = 0: one subtree = whole tree)
    print(f"\n{'='*60}")
    print(f"Single-bit: p={p} d={d} (1 logical bit, {p**d} leaves, "
          f"B={tree_mod.barrier_formula(p,d)})")
    print(f"{'='*60}")

    single_exp = multi_bit_experiment(
        d, 0, p_err_list, n_trials=n_trials, seed=seed, p=p
    )
    comparison['configs']['single'] = single_exp

    for r in single_exp['results']:
        print(f"  p_err={r['p_err']:.2f}: BER={r['ber']:.6f} "
              f"({r['bit_errors']}/{r['total_bits_tested']})")

    # Multi-bit at each split depth
    for k in split_depths:
        n_bits = p ** k
        leaves_per = p ** (d - k)
        barrier_per = tree_mod.barrier_formula(p, d - k)

        print(f"\n{'='*60}")
        print(f"Multi-bit k={k}: p={p} d={d} ({n_bits} logical bits, "
              f"{leaves_per} leaves/bit, B={barrier_per})")
        print(f"{'='*60}")

        exp = multi_bit_experiment(
            d, k, p_err_list, n_trials=n_trials, seed=seed, p=p
        )
        comparison['configs'][f'multi_k{k}'] = exp

        for r in exp['results']:
            print(f"  p_err={r['p_err']:.2f}: BER={r['ber']:.6f} "
                  f"({r['bit_errors']}/{r['total_bits_tested']})")

    return comparison


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    print("=== Multi-Bit Logical Encoding v0.13 ===")
    print()

    # Quick sanity
    p, d, k = 3, 4, 1
    n_bits = p ** k
    print(f"Sanity: p={p} d={d} k={k} -> {n_bits} logical bits")
    print(f"  Each bit: {p**(d-k)} leaves, B={tree_mod.barrier_formula(p, d-k)}")
    print()

    # Run single trial
    seed = 42
    encoded, decoded, bit_errors, leaf_errors = multi_bit_trial(
        d, k, n_bits, 0.20, p=p, seed=seed
    )
    print(f"Single trial (p_err=0.20):")
    print(f"  Encoded: {encoded}")
    print(f"  Decoded: {decoded}")
    print(f"  Bit errors: {bit_errors}/{n_bits}")
    print(f"  Leaf errors: {leaf_errors}/{p**d}")
    print()

    # Independence test
    print("=== Independence Test ===")
    print("(Verifying logical bits in different subtrees are independent)")
    ind_result = test_independence(d, k, 0.20, p=p, n_trials=500, seed=seed)
    print(f"  Per-bit accuracy: {[f'{x:.3f}' for x in ind_result['per_bit_accuracy']]}")
    print(f"  Avg pair deviation from independence: {ind_result['avg_pair_deviation']:.6f}")
    print(f"  Max pair deviation: {ind_result['max_pair_deviation']:.6f}")
    print(f"  Interpretation: deviations < 0.05 suggest independence")
    print()

    # Compare single vs multi-bit
    print("=== Single vs Multi-Bit Comparison ===")
    print("(p=3 d=5, 243 total leaves)")
    compare_single_vs_multi(
        p=3, d=5,
        split_depths=[1, 2],  # k=1: 3 bits, k=2: 9 bits
        p_err_list=[0.10, 0.20, 0.30, 0.40],
        n_trials=200, seed=42
    )

    print()
    print("Module loaded successfully.")
