"""
0.12_correlated_noise.py — Correlated Noise Model for Tree & Classical Codes

Implements two-stage correlated bit-flip noise:
  Stage 1: i.i.d. flips with probability p_err_base
  Stage 2: For each flipped leaf/bit, flip k nearest neighbors with prob p_corr

This models physical crosstalk and environmental noise correlations.

Comparison: Tree (hierarchical) vs Classical repetition (flat) under same noise.
Hypothesis: Tree may BENEFIT from correlated noise — clustered errors within
one subtree are contained by hierarchical voting, while classical code sees
concentrated errors across adjacent bits that can flip the majority.

Author: LLM-assisted implementation for ultrametric_v2 project
Date: 2026-05-16
Version: 0.12.0
"""

import random
import math
import json
import sys
import os
from typing import List, Tuple, Optional, Dict, Any, Callable
from dataclasses import dataclass, field


# ============================================================================
# Import tree module
# ============================================================================

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util

spec = importlib.util.spec_from_file_location(
    'tree_0_10', os.path.join(os.path.dirname(os.path.abspath(__file__)), '0.10.py')
)
tree_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tree_mod)


# ============================================================================
# Correlated Noise — General
# ============================================================================

def correlated_flip_stage2(indices: List[int], n_total: int,
                           p_corr: float, k: int,
                           rng: random.Random) -> List[int]:
    """Stage 2: For each flipped index, flip up to k neighbors with prob p_corr.

    indices: list of indices flipped in stage 1 (0-based)
    n_total: total number of leaves/bits
    p_corr: probability of flipping each neighbor
    k: maximum neighbors on each side (total window = 2k)
    rng: random number generator

    Returns: list of NEW indices flipped in stage 2 (not including stage 1)
    """
    stage2_flips = set()
    for idx in indices:
        for offset in range(-k, k + 1):
            if offset == 0:
                continue  # skip self
            neighbor = idx + offset
            if 0 <= neighbor < n_total:
                if neighbor not in indices and neighbor not in stage2_flips:
                    if rng.random() < p_corr:
                        stage2_flips.add(neighbor)
    return list(stage2_flips)


# ============================================================================
# Correlated Noise — Tree
# ============================================================================

def apply_correlated_noise_tree(root: 'tree_mod.Node', p_err_base: float,
                                p_corr: float, k: int = 2,
                                rng: Optional[random.Random] = None
                                ) -> Dict[str, Any]:
    """Apply two-stage correlated noise to tree leaves.

    Stage 1: i.i.d. flips with p_err_base on all leaves
    Stage 2: For each flipped leaf, flip k DFS-nearest neighbors with prob p_corr

    Returns dict with: stage1_errors, stage2_errors, total_errors, error_rate
    """
    if rng is None:
        rng = random.Random()

    leaves = tree_mod.get_leaves(root)

    # Stage 1: i.i.d. flips
    stage1_indices = []
    for i, leaf in enumerate(leaves):
        if rng.random() < p_err_base:
            leaf.value = 1 - leaf.value
            stage1_indices.append(i)

    # Stage 2: correlated neighbor flips
    stage2_indices = correlated_flip_stage2(
        stage1_indices, len(leaves), p_corr, k, rng
    )
    for idx in stage2_indices:
        leaves[idx].value = 1 - leaves[idx].value

    total_errors = len(stage1_indices) + len(stage2_indices)

    return {
        'stage1_errors': len(stage1_indices),
        'stage2_errors': len(stage2_indices),
        'total_errors': total_errors,
        'error_rate': total_errors / len(leaves),
        'stage1_indices': stage1_indices,
        'stage2_indices': stage2_indices
    }


# ============================================================================
# Correlated Noise — Classical Repetition Code
# ============================================================================

def apply_correlated_noise_classical(bits: List[int], p_err_base: float,
                                     p_corr: float, k: int = 2,
                                     rng: Optional[random.Random] = None
                                     ) -> Dict[str, Any]:
    """Apply two-stage correlated noise to classical bit array.

    Stage 1: i.i.d. flips with p_err_base
    Stage 2: For each flipped bit, flip k adjacent neighbors with prob p_corr

    Returns dict with error info.
    """
    if rng is None:
        rng = random.Random()

    n = len(bits)

    # Stage 1: i.i.d. flips
    stage1_indices = []
    for i in range(n):
        if rng.random() < p_err_base:
            bits[i] = 1 - bits[i]
            stage1_indices.append(i)

    # Stage 2: correlated neighbor flips
    stage2_indices = correlated_flip_stage2(
        stage1_indices, n, p_corr, k, rng
    )
    for idx in stage2_indices:
        if idx not in stage1_indices:  # don't double-count
            bits[idx] = 1 - bits[idx]

    total_errors = len(stage1_indices) + len(stage2_indices)

    return {
        'stage1_errors': len(stage1_indices),
        'stage2_errors': len(stage2_indices),
        'total_errors': total_errors,
        'error_rate': total_errors / n
    }


# ============================================================================
# Monte Carlo — Correlated Noise
# ============================================================================

def run_trial_correlated_tree(depth: int, p_err_base: float,
                              p_corr: float, k: int,
                              logical_bit: int, p: int = 3,
                              seed: Optional[int] = None
                              ) -> Tuple[bool, int, int]:
    """Single MC trial with correlated noise on tree.

    Returns: (logical_error, decoded_bit, total_physical_errors)
    """
    rng = random.Random(seed)
    tree = tree_mod.build_tree(depth, p=p)
    tree_mod.encode(tree, logical_bit)
    corr_info = apply_correlated_noise_tree(
        tree, p_err_base, p_corr, k, rng=rng
    )
    decoded = tree_mod.decode(tree)
    error = (decoded != logical_bit)
    return error, decoded, corr_info['total_errors']


def run_trial_correlated_classical(n_bits: int, p_err_base: float,
                                   p_corr: float, k: int,
                                   logical_bit: int,
                                   seed: Optional[int] = None
                                   ) -> Tuple[bool, int, int]:
    """Single MC trial with correlated noise on classical code.

    Returns: (logical_error, decoded_bit, total_physical_errors)
    """
    rng = random.Random(seed)

    # Classical encode: repeat bit
    bits = [logical_bit] * n_bits

    # Apply correlated noise
    corr_info = apply_correlated_noise_classical(
        bits, p_err_base, p_corr, k, rng=rng
    )

    # Classical decode: majority vote
    ones = sum(bits)
    decoded = 1 if ones > n_bits // 2 else 0
    error = (decoded != logical_bit)

    return error, decoded, corr_info['total_errors']


def run_experiment_correlated(
    runner_fn: Callable,
    p_err_base_list: List[float],
    p_corr: float, k: int,
    n_trials: int = 500, seed: int = 42,
    **runner_kwargs
) -> Dict[str, Any]:
    """Run MC experiment with correlated noise.

    runner_fn: function that takes (p_err_base, p_corr, k, ..., seed)
               and returns (error, decoded, phys_errors)
    """
    results = []
    for p_err_base in p_err_base_list:
        errors = 0
        total_phys = 0
        for trial in range(n_trials):
            trial_seed = seed + trial
            logical_error, _, phys_errors = runner_fn(
                p_err_base=p_err_base, p_corr=p_corr, k=k,
                seed=trial_seed, **runner_kwargs
            )
            if logical_error:
                errors += 1
            total_phys += phys_errors
        ler = errors / n_trials
        avg_phys = total_phys / n_trials
        ci_lower, ci_upper = tree_mod.wilson_ci(n_trials - errors, n_trials)
        results.append({
            'p_err_base': p_err_base,
            'p_corr': p_corr,
            'k': k,
            'errors': errors,
            'n_trials': n_trials,
            'ler': ler,
            'avg_physical_errors': avg_phys,
            'ci_lower': ci_lower,
            'ci_upper': ci_upper
        })
    return {
        'p_corr': p_corr,
        'k': k,
        'n_trials': n_trials,
        'results': results
    }


# ============================================================================
# Comparison Runner
# ============================================================================

def compare_correlated(p: int, d: int, p_err_base_list: List[float],
                       p_corr_list: List[float],
                       k: int = 2, n_trials: int = 500, seed: int = 42,
                       verbose: bool = True) -> Dict[str, Any]:
    """Compare tree vs classical under correlated noise at matched N = p^d.

    Returns nested dict of results for each p_corr value.
    """
    N = p ** d
    all_results = {}

    for p_corr in p_corr_list:
        if verbose:
            print(f"\n{'='*60}")
            print(f"p={p} d={d} N={N:,} p_corr={p_corr} k={k}")
            print(f"{'='*60}")

        # Tree experiment
        if verbose:
            print("Tree...", end=" ", flush=True)
        tree_results = run_experiment_correlated(
            runner_fn=run_trial_correlated_tree,
            p_err_base_list=p_err_base_list,
            p_corr=p_corr, k=k, n_trials=n_trials, seed=seed,
            depth=d, logical_bit=0, p=p
        )
        tree_results['N'] = N
        tree_results['barrier'] = tree_mod.barrier_formula(p, d)
        if verbose:
            print("done.")

        # Classical experiment
        if verbose:
            print("Classical...", end=" ", flush=True)
        classical_results = run_experiment_correlated(
            runner_fn=run_trial_correlated_classical,
            p_err_base_list=p_err_base_list,
            p_corr=p_corr, k=k, n_trials=n_trials, seed=seed,
            n_bits=N, logical_bit=0
        )
        classical_results['N'] = N
        classical_results['barrier'] = (N + 1) // 2
        if verbose:
            print("done.")

        all_results[str(p_corr)] = {
            'tree': tree_results,
            'classical': classical_results
        }

        # Print comparison table
        if verbose:
            print(f"\n{'p_err_base':>12} {'Tree LER':>10} {'CL LER':>10} "
                  f"{'Winner':>12}")
            print("-" * 48)
            for i, p_err_base in enumerate(p_err_base_list):
                tree_ler = tree_results['results'][i]['ler']
                cl_ler = classical_results['results'][i]['ler']
                if tree_ler < cl_ler:
                    winner = "TREE"
                elif cl_ler < tree_ler:
                    winner = "CLASSICAL"
                else:
                    winner = "TIE"
                print(f"{p_err_base:>12.2f} {tree_ler:>10.4f} {cl_ler:>10.4f} "
                      f"{winner:>12}")

    return all_results


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    print("=== Correlated Noise Model v0.12 ===")
    print()

    # Quick demo
    print("Quick demo: p=3 d=3 (N=27), p_err_base=0.20, p_corr=0.50, k=2")
    print()

    seed = 42
    rng = random.Random(seed)

    # Tree demo
    tree = tree_mod.build_tree(3, p=3)
    tree_mod.encode(tree, 1)  # logical 1
    corr_info = apply_correlated_noise_tree(tree, 0.20, 0.50, k=2, rng=rng)
    decoded = tree_mod.decode(tree)
    print(f"Tree: stage1={corr_info['stage1_errors']}, "
          f"stage2={corr_info['stage2_errors']}, "
          f"total={corr_info['total_errors']}/27, "
          f"decoded={decoded}, correct={decoded==1}")

    # Classical demo
    rng2 = random.Random(seed)
    bits = [0] * 27  # logical 0 for variety
    corr_info2 = apply_correlated_noise_classical(bits, 0.20, 0.50, k=2, rng=rng2)
    decoded2 = 1 if sum(bits) > 13 else 0
    print(f"Classical: stage1={corr_info2['stage1_errors']}, "
          f"stage2={corr_info2['stage2_errors']}, "
          f"total={corr_info2['total_errors']}/27, "
          f"decoded={decoded2}, correct={decoded2==0}")
    print()

    # Run comparison for p=3 d=3
    print("=== Correlated Noise Comparison ===")
    p_err_base_list = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30]
    p_corr_list = [0.0, 0.25, 0.50, 0.75]

    results = compare_correlated(
        p=3, d=3,
        p_err_base_list=p_err_base_list,
        p_corr_list=p_corr_list,
        k=2, n_trials=200, seed=42
    )

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY: Tree advantage ratio at p_err_base=0.30")
    print("=" * 60)
    print(f"{'p_corr':>8} {'Tree LER':>10} {'CL LER':>10} {'CL/Tree':>10}")
    print("-" * 42)
    for p_corr_str, data in results.items():
        p_corr = float(p_corr_str)
        i = len(p_err_base_list) - 1  # last p_err_base
        tree_ler = data['tree']['results'][i]['ler']
        cl_ler = data['classical']['results'][i]['ler']
        ratio = cl_ler / tree_ler if tree_ler > 0 else float('inf')
        print(f"{p_corr:>8.2f} {tree_ler:>10.4f} {cl_ler:>10.4f} {ratio:>10.2f}x")
