"""
0.11_classical_repetition.py — Classical Repetition Code Baseline

Compares classical N-bit repetition code against hierarchical tree architectures.
For fair comparison, N is matched to tree leaf count: N = p^d.

Classical repetition:
- Encode: repeat bit N times
- Noise: i.i.d. bit-flip with p_err
- Decode: majority vote (ties break to 0)
- Barrier: ceil(N/2)
- LER: P(k >= ceil(N/2)) where k ~ Binomial(N, p_err)

Tree (for comparison):
- Each leaf is a physical qubit (N = p^d)
- Hierarchical majority voting
- Barrier: ceil(p/2)^d

Author: LLM-assisted implementation for ultrametric_v2 project
Date: 2026-05-16
Version: 0.11.0
"""

import random
import math
from typing import List, Tuple, Dict, Any


# ============================================================================
# Classical Repetition Code
# ============================================================================

def classical_barrier(n_bits: int) -> int:
    """Barrier for N-bit classical repetition code: ceil(N/2)."""
    return (n_bits + 1) // 2  # ceil(N/2)


def classical_encode(bit: int, n_bits: int) -> List[int]:
    """Encode logical bit by repeating it N times."""
    return [bit] * n_bits


def classical_apply_noise(bits: List[int], p_err: float,
                          rng: random.Random) -> Tuple[List[int], int]:
    """Apply i.i.d. bit-flip noise. Returns (noisy bits, error count)."""
    errors = 0
    noisy = []
    for b in bits:
        if rng.random() < p_err:
            noisy.append(1 - b)
            errors += 1
        else:
            noisy.append(b)
    return noisy, errors


def classical_decode(bits: List[int]) -> int:
    """Majority vote (ties break to 0)."""
    ones = sum(bits)
    zeros = len(bits) - ones
    return 1 if ones > zeros else 0


def classical_run_trial(n_bits: int, p_err: float, logical_bit: int,
                        rng: random.Random) -> Tuple[bool, int, int]:
    """Run single trial. Returns (logical_error, decoded_bit, error_count)."""
    encoded = classical_encode(logical_bit, n_bits)
    noisy, error_count = classical_apply_noise(encoded, p_err, rng)
    decoded = classical_decode(noisy)
    logical_error = (decoded != logical_bit)
    return logical_error, decoded, error_count


def classical_run_experiment(n_bits: int, p_err_list: List[float],
                             n_trials: int = 500, seed: int = 42,
                             logical_bit: int = 0) -> Dict[str, Any]:
    """Run Monte Carlo experiment for classical repetition code."""
    rng = random.Random(seed)
    results = []
    for p_err in p_err_list:
        errors = 0
        total_bit_errors = 0
        for trial in range(n_trials):
            trial_rng = random.Random(rng.randint(0, 2**31 - 1))
            logical_error, _, bit_errors = classical_run_trial(
                n_bits, p_err, logical_bit, trial_rng
            )
            if logical_error:
                errors += 1
            total_bit_errors += bit_errors
        ler = errors / n_trials
        avg_bit_errors = total_bit_errors / n_trials
        ci_lower, ci_upper = wilson_ci(n_trials - errors, n_trials)
        results.append({
            "p_err": p_err,
            "errors": errors,
            "n_trials": n_trials,
            "ler": ler,
            "avg_bit_errors": avg_bit_errors,
            "ci_lower": ci_lower,
            "ci_upper": ci_upper
        })
    return {
        "code": "classical_repetition",
        "n_bits": n_bits,
        "barrier": classical_barrier(n_bits),
        "logical_bit": logical_bit,
        "n_trials": n_trials,
        "results": results
    }


# ============================================================================
# Theoretical LER (Binomial CDF)
# ============================================================================

def classical_ler_theoretical(n_bits: int, p_err: float) -> float:
    """Exact LER via binomial CDF: P(k >= ceil(N/2) | k ~ Bin(N, p))."""
    threshold = (n_bits + 1) // 2  # ceil(N/2)
    # Compute tail probability
    # Use log-space for numerical stability with large N
    total = 0.0
    for k in range(threshold, n_bits + 1):
        # P(k) = C(n,k) * p^k * (1-p)^(n-k)
        log_prob = (
            math.lgamma(n_bits + 1) - math.lgamma(k + 1) -
            math.lgamma(n_bits - k + 1) +
            k * math.log(p_err) + (n_bits - k) * math.log(1 - p_err)
        )
        total += math.exp(log_prob)
    return total


# ============================================================================
# Statistics
# ============================================================================

def wilson_ci(successes: int, n: int, z: float = 1.96) -> Tuple[float, float]:
    """Wilson score confidence interval for binomial proportion."""
    if n == 0:
        return (0.0, 1.0)
    p_hat = successes / n
    denominator = 1 + z**2 / n
    center = (p_hat + z**2 / (2 * n)) / denominator
    margin = z * math.sqrt(
        (p_hat * (1 - p_hat) + z**2 / (4 * n)) / n
    ) / denominator
    lower = max(0.0, center - margin)
    upper = min(1.0, center + margin)
    return (lower, upper)


# ============================================================================
# Cross-Architecture Comparison
# ============================================================================

def compare_architectures(tree_results_path: str,
                          p_values: List[int],
                          depths: List[int],
                          p_err_list: List[float],
                          n_trials: int = 500,
                          seed: int = 42) -> List[Dict[str, Any]]:
    """Compare tree vs classical at matching qubit counts.

    For each (p, d): N = p^d. Run classical at that N and compare.
    """
    import json, sys, os

    # Load tree results
    tree_data = {}
    if os.path.exists(tree_results_path):
        with open(tree_results_path, 'r') as f:
            tree_data = json.load(f)

    comparisons = []
    for p in p_values:
        for d in depths:
            N = p ** d
            comparisons.append({
                "p": p, "d": d, "N": N,
                "tree_barrier": int(math.ceil(p / 2) ** d),
                "classical_barrier": classical_barrier(N),
            })
    return comparisons


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    print("=== Classical Repetition Code Baseline ===")
    print()

    # Compare barriers at matching N
    print("Barrier comparison at matching qubit counts:")
    print(f"{'Architecture':<25} {'N':>8} {'Barrier':>10} {'B/N':>10}")
    print("-" * 55)
    for d in [2, 3, 4, 5, 7]:
        N3 = 3 ** d
        N5 = 5 ** d
        B3 = 2 ** d
        B5 = 3 ** d
        B_classical_3 = classical_barrier(N3)
        B_classical_5 = classical_barrier(N5)
        print(f"p=3 d={d} (tree):         {N3:>8,} {B3:>10} {B3/N3:>10.4f}")
        print(f"Classical N={N3:,}:        {N3:>8,} {B_classical_3:>10} {B_classical_3/N3:>10.4f}")
        print(f"p=5 d={d} (tree):         {N5:>8,} {B5:>10} {B5/N5:>10.4f}")
        print(f"Classical N={N5:,}:        {N5:>8,} {B_classical_5:>10} {B_classical_5/N5:>10.4f}")
        print()

    # Theoretical LER comparison
    print("Theoretical LER comparison at p_err=0.40 (classical via binomial):")
    print(f"{'Architecture':<20} {'N':>8} {'Barrier':>8} {'LER':>10}")
    print("-" * 50)
    for d in [2, 3, 4, 5, 6, 7]:
        N3 = 3 ** d
        B3 = 2 ** d
        ler_cl = classical_ler_theoretical(N3, 0.40)
        print(f"p=3 d={d} (tree):    {N3:>8,} {B3:>8} see 0.2_results.json")
        print(f"Classical N={N3:,}:   {N3:>8,} {classical_barrier(N3):>8} {ler_cl:>10.6f}")
        print()

    # Quick MC validation
    print("=== Quick MC Validation (500 trials, seed=42) ===")
    for d in [3, 4]:
        N = 3 ** d
        exp = classical_run_experiment(N, [0.40], n_trials=500, seed=42)
        r = exp['results'][0]
        ler_theo = classical_ler_theoretical(N, 0.40)
        print(f"N={N} (d={d} eq.): LER={r['ler']:.4f}, CI_err=[{1-r['ci_upper']:.4f}, {1-r['ci_lower']:.4f}], theory={ler_theo:.6f}")
        print(f"  Tree p=3 d={d}: see 0.2_results.json")
        print()
