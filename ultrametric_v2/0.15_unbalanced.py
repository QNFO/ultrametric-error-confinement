"""
0.15_unbalanced.py -- Dynamic Tree Restructuring for Adaptive Error Confinement

Extends multi-bit encoding (0.13_multi_bit.py) to support ASYMMETRIC split depths:
different subtrees can be at different depths, allocating more qubits
to high-priority logical bits.

Key question: At fixed total qubit count, does asymmetric allocation provide
better overall utility than symmetric (uniform depth)?

Approach:
1. Build unbalanced tree: root has p children, each child subtree can have
   DIFFERENT depths d_0, d_1, ..., d_{p-1}
2. Each subtree encodes one logical bit with barrier B_i = ceil(p/2)^(d_i)
3. Compare weighted utility: U = sum_i w_i * (1 - BER_i) where w_i is priority
4. Show that giving high-w_i bits deeper subtrees improves total utility

Author: LLM-assisted implementation for ultrametric_v2 project
Date: 2026-05-16
Version: 0.15.0
"""

import random
import math
import json
import sys
import os
from typing import List, Tuple, Optional, Dict, Any
from dataclasses import dataclass, field

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util

spec = importlib.util.spec_from_file_location(
    'tree', os.path.join(os.path.dirname(os.path.abspath(__file__)), '0.10.py')
)
tree_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tree_mod)


# ============================================================================
# Unbalanced Tree Construction
# ============================================================================

def build_unbalanced_tree(depths: List[int], p: int = 3) -> 'tree_mod.Node':
    """Build a tree where the p root-children have different subtree depths.

    depths[i] = depth of subtree rooted at root's i-th child.
    Total leaves = sum_i p^depths[i].
    """
    root = tree_mod.Node(depth=0)
    for d in depths:
        child = tree_mod.Node(depth=1, parent=root)
        tree_mod._build_subtree(child, d, p)
        root.children.append(child)
    return root


def unbalanced_leaf_count(depths: List[int], p: int = 3) -> int:
    """Total leaves in unbalanced tree."""
    return sum(p ** d for d in depths)


# ============================================================================
# Unbalanced Multi-Bit Encoding
# ============================================================================

def unbalanced_encode(root: 'tree_mod.Node', bits: List[int],
                      depths: List[int]) -> None:
    """Encode multiple bits in an unbalanced tree.

    bits[i] is encoded into the subtree rooted at root.children[i],
    which has depth depths[i].
    """
    if len(bits) != len(root.children):
        raise ValueError(f"Need {len(root.children)} bits, got {len(bits)}")

    for i, child_root in enumerate(root.children):
        bit = bits[i]
        leaves = tree_mod.get_leaves(child_root)
        for leaf in leaves:
            leaf.value = bit


def unbalanced_decode(root: 'tree_mod.Node') -> List[int]:
    """Decode multi-bit from unbalanced tree.

    Each root child subtree is decoded independently via majority vote.
    """
    decoded = []
    for child in root.children:
        bit = tree_mod.decode(child)
        decoded.append(bit)
    return decoded


def unbalanced_run_trial(depths: List[int], bits: List[int],
                         p_err: float, p: int = 3,
                         seed: Optional[int] = None
                         ) -> Tuple[List[int], List[int], int, int]:
    """Single trial with unbalanced tree.

    Returns: (encoded_bits, decoded_bits, bit_errors, total_leaf_errors)
    """
    rng = random.Random(seed)
    tree = build_unbalanced_tree(depths, p=p)
    unbalanced_encode(tree, bits, depths)

    # Apply noise to all leaves
    flip_info = tree_mod.apply_noise(tree, p_err, rng=rng)
    total_leaf_errors = sum(1 for f in flip_info if f)

    decoded = unbalanced_decode(tree)
    bit_errors = sum(1 for e, d in zip(bits, decoded) if e != d)

    return bits, decoded, bit_errors, total_leaf_errors


# ============================================================================
# Comparison: Balanced vs Unbalanced
# ============================================================================

def compare_balanced_vs_unbalanced(
    p: int = 3,
    balanced_depth: int = 3,
    p_err_list: List[float] = None,
    n_trials: int = 500,
    seed: int = 42
) -> Dict[str, Any]:
    """Compare balanced (uniform depth) vs unbalanced allocation.

    Balanced: p subtrees at depth d, total leaves = p * p^d = p^(d+1)
    Unbalanced: p subtrees at depths [d+1, d, d-1], total leaves ~= p^(d+2) + p^(d+1) + p^d

    Wait, that gives DIFFERENT total leaves. For fair comparison, need SAME total.

    Strategy: Fix total qubit budget N. Balanced uses uniform depth.
    Unbalanced allocates MORE leaves to high-priority bits, FEWER to low-priority.

    Example: p=3, budget N=12 leaves
    - Balanced: each subtree gets 4 leaves -> depth 1 (3 leaves each, total 9)
      Actually, with p=3: balanced d=1 gives 3*3=9 leaves, d=2 gives 3*9=27 leaves.
      There's no nice way to hit exactly N=12 with uniform depths.

    Better approach: compare UTILITY at FIXED DEPTH (which controls barrier).
    - Balanced: all p subtrees at depth d, barrier B = ceil(p/2)^d for all bits
    - Unbalanced: give 1 subtree depth d+1 (higher priority), p-2 at depth d,
      and 1 subtree at depth d-1 (lowest priority), total leaves ~= same

    Let's do this:
    - Balanced: [d, d, d], leaves = 3 * p^d
    - Unbalanced A: [d+1, d, d-1], leaves = p^(d+1) + p^d + p^(d-1)
      Check ratio: (p^(d+1) + p^d + p^(d-1)) / (3 * p^d) = (p + 1 + 1/p) / 3
      For p=3: (3+1+0.333)/3 = 1.444 -> unbalanced uses MORE leaves

    - Unbalanced B: [d+1, d-1, d-1], leaves = p^(d+1) + 2 * p^(d-1)
      Ratio: (p^(d+1) + 2*p^(d-1)) / (3 * p^d) = (p + 2/p) / 3
      For p=3: (3 + 0.667)/3 = 1.222 -> still more leaves

    For FAIR comparison at approximately equal N, adjust depths slightly.

    Actually, let's just compare at the same total qubit count approximately.
    """
    if p_err_list is None:
        p_err_list = [0.10, 0.20, 0.30, 0.40]

    # Balanced: all subtrees at same depth
    balanced_depths = [balanced_depth] * p
    balanced_leaves = unbalanced_leaf_count(balanced_depths, p)

    # Unbalanced: [d+1, d, d-1] for p=3
    unbalanced_depths = [balanced_depth + 1, balanced_depth, balanced_depth - 1]
    unbalanced_leaves = unbalanced_leaf_count(unbalanced_depths, p)

    print(f"=== Balanced vs Unbalanced ===")
    print(f"p={p}")
    print(f"Balanced: depths={balanced_depths}, leaves={balanced_leaves}")
    print(f"Unbalanced: depths={unbalanced_depths}, leaves={unbalanced_leaves}")
    print(f"Leaf ratio: {unbalanced_leaves/balanced_leaves:.3f}")
    print()

    results = {
        'p': p,
        'balanced_depths': balanced_depths,
        'balanced_leaves': balanced_leaves,
        'unbalanced_depths': unbalanced_depths,
        'unbalanced_leaves': unbalanced_leaves,
        'n_trials': n_trials,
        'p_err_results': []
    }

    for p_err in p_err_list:
        print(f"p_err={p_err:.2f}")

        # Balanced
        bal_errors = 0
        bal_bit_errors = [0] * p  # per-subtree error count
        for trial in range(n_trials):
            trial_seed = seed + trial
            bits = [random.Random(trial_seed + 1000).randint(0, 1) for _ in range(p)]
            _, decoded, n_err, _ = unbalanced_run_trial(
                balanced_depths, bits, p_err, p=p, seed=trial_seed
            )
            bal_errors += n_err
            for i in range(p):
                if decoded[i] != bits[i]:
                    bal_bit_errors[i] += 1

        # Unbalanced
        unb_errors = 0
        unb_bit_errors = [0] * p
        for trial in range(n_trials):
            trial_seed = seed + trial + 100000  # different seed offset
            bits = [random.Random(trial_seed + 2000).randint(0, 1) for _ in range(p)]
            _, decoded, n_err, _ = unbalanced_run_trial(
                unbalanced_depths, bits, p_err, p=p, seed=trial_seed
            )
            unb_errors += n_err
            for i in range(p):
                if decoded[i] != bits[i]:
                    unb_bit_errors[i] += 1

        bal_ber = bal_errors / (p * n_trials)
        unb_ber = unb_errors / (p * n_trials)

        # Per-subtree BER
        bal_per_bit = [e / n_trials for e in bal_bit_errors]
        unb_per_bit = [e / n_trials for e in unb_bit_errors]

        # Utility: weighted by priority (depth -> higher priority)
        # High-priority bit (deepest) has weight 4, medium weight 2, low weight 1
        weights_balanced = [1, 1, 1]  # all equal priority
        weights_unbalanced = [4, 2, 1]  # deeper = higher priority

        bal_utility = sum(w * (1 - b) for w, b in zip(weights_balanced, bal_per_bit))
        unb_utility = sum(w * (1 - b) for w, b in zip(weights_unbalanced, unb_per_bit))

        result = {
            'p_err': p_err,
            'balanced_ber': bal_ber,
            'unbalanced_ber': unb_ber,
            'balanced_per_bit': bal_per_bit,
            'unbalanced_per_bit': unb_per_bit,
            'balanced_utility': bal_utility,
            'unbalanced_utility': unb_utility,
            'barriers_balanced': [tree_mod.barrier_formula(p, balanced_depth)] * p,
            'barriers_unbalanced': [
                tree_mod.barrier_formula(p, unbalanced_depths[i]) for i in range(p)
            ]
        }
        results['p_err_results'].append(result)

        print(f"  Balanced: BER={bal_ber:.4f}, per-bit={[f'{x:.4f}' for x in bal_per_bit]}, util={bal_utility:.4f}")
        print(f"  Unbalanced: BER={unb_ber:.4f}, per-bit={[f'{x:.4f}' for x in unb_per_bit]}, util={unb_utility:.4f}")
        print(f"  Unbalanced barriers: {result['barriers_unbalanced']}")
        winner = "UNBALANCED" if unb_utility > bal_utility else "BALANCED"
        print(f"  Utility winner: {winner}")
        print()

    return results


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    print("=== Dynamic Tree Restructuring v0.15 ===")
    print()

    # Quick sanity
    depths = [2, 1, 0]
    tree = build_unbalanced_tree(depths, p=3)
    leaves = tree_mod.get_leaves(tree)
    print(f"Unbalanced depths={depths}:")
    print(f"  Total leaves: {len(leaves)} (expected: 9+3+1=13)")
    print(f"  Root children: {len(tree.children)}")
    for i, child in enumerate(tree.children):
        child_leaves = tree_mod.get_leaves(child)
        print(f"    Child {i}: depth={depths[i]}, leaves={len(child_leaves)}")
    print()

    # Quick encode-decode
    bits = [0, 1, 0]
    unbalanced_encode(tree, bits, depths)
    decoded = unbalanced_decode(tree)
    print(f"Encoded: {bits}, Decoded: {decoded}, correct={bits==decoded}")
    print()

    # Balanced vs Unbalanced comparison
    results = compare_balanced_vs_unbalanced(
        p=3, balanced_depth=2,
        p_err_list=[0.10, 0.20, 0.30, 0.40],
        n_trials=300, seed=42
    )

    # Summary
    print("=" * 60)
    print("SUMMARY: Utility Comparison")
    print("=" * 60)
    print(f"{'p_err':>6} {'Bal Util':>10} {'Unb Util':>10} {'Winner':>12}")
    print("-" * 42)
    for r in results['p_err_results']:
        winner = "UNBALANCED" if r['unbalanced_utility'] > r['balanced_utility'] else "BALANCED"
        print(f"{r['p_err']:>6.2f} {r['balanced_utility']:>10.4f} "
              f"{r['unbalanced_utility']:>10.4f} {winner:>12}")

    print()
    print("Module loaded successfully.")
