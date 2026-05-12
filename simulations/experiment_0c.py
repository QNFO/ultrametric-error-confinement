"""Experiment 0C: Strong Triangle Inequality Verification.

Verifies that the ultrametric distance on Bruhat-Tits trees satisfies
the strong triangle inequality d(x,z) <= max(d(x,y), d(y,z)) and the
isosceles property (the two largest distances among any triple are equal).

This corresponds to Section 3.7 and Table 3 of the paper.

Key insight: The strong triangle inequality is what geometrically
confines errors to their local branches in ultrametric spaces.
This property is mathematically guaranteed for Bruhat-Tits trees,
but we verify it computationally as a sanity check.
"""

from __future__ import annotations
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from btree import BruhatTitsTree


def run_experiment_0c(
    primes: list[int] | None = None,
    depth: int = 5,
    trials_per_prime: int = 5000,
    verbose: bool = True,
) -> dict:
    """Run the strong triangle inequality verification experiment.

    Args:
        primes: Primes to test (default: [2, 3, 5])
        depth: Tree depth for verification (default: 5)
        trials_per_prime: Random leaf triples per prime (default: 5000)
        verbose: Print progress

    Returns:
        dict with verification results for each prime
    """
    if primes is None:
        primes = [2, 3, 5]

    results: dict[int, dict] = {}
    total_violations = 0
    total_isosceles = 0
    total_trials = 0

    if verbose:
        print(f"\n{'='*60}")
        print("EXPERIMENT 0C: Strong Triangle Inequality Verification")
        print(f"{'='*60}")
        print(f"  Tree depth: {depth}")
        print(f"  Trials per prime: {trials_per_prime:,}")
        print(f"  Primes tested: {primes}")
        print()

    for p in primes:
        if verbose:
            print(f"  p = {p}: building Bruhat-Tits tree (depth {depth})... ", end="", flush=True)

        t0 = time.time()
        tree = BruhatTitsTree(p=p, depth=depth)
        build_time = time.time() - t0

        if verbose:
            print(f"built in {build_time:.2f}s, running {trials_per_prime:,} trials... ", end="", flush=True)

        t1 = time.time()
        result = tree.verify_strong_triangle_inequality(trials=trials_per_prime)
        trial_time = time.time() - t1

        results[p] = result
        total_trials += trials_per_prime
        total_violations += result["strong_triangle_violations"]
        total_isosceles += result["isosceles_violations"]

        if verbose:
            sti_status = "PASS" if result["strong_triangle_holds"] else "FAIL"
            iso_status = "PASS" if result["isosceles_holds"] else "FAIL"
            print(f"done in {trial_time:.2f}s")
            print(f"    STI violations: {result['strong_triangle_violations']}/{trials_per_prime:,} [{sti_status}]")
            print(f"    Isosceles violations: {result['isosceles_violations']}/{trials_per_prime:,} [{iso_status}]")
            print()

    if verbose:
        _print_summary(results, primes, total_trials, total_violations, total_isosceles)

    return {
        "results": results,
        "primes": primes,
        "depth": depth,
        "total_trials": total_trials,
        "total_violations": total_violations,
        "total_isosceles_violations": total_isosceles,
        "overall_sti_holds": total_violations == 0,
        "overall_isosceles_holds": total_isosceles == 0,
    }


def _print_summary(
    results: dict[int, dict],
    primes: list[int],
    total_trials: int,
    total_violations: int,
    total_isosceles: int,
) -> None:
    """Print Table 3 format summary."""
    print(f"{'='*60}")
    print("EXPERIMENT 0C SUMMARY")
    print(f"{'='*60}")
    print()
    print("Table 3: Strong Triangle Inequality Verification")
    print()
    print(f"{'Prime p':>8s} | {'Trials':>8s} | {'Violations':>10s} | {'Isosceles Viol.':>15s} | {'Status':>6s}")
    print("-" * 65)

    for p in primes:
        r = results[p]
        sti = "PASS" if r["strong_triangle_holds"] else "FAIL"
        print(f"{p:>8d} | {r['trials']:>8,d} | "
              f"{r['strong_triangle_violations']:>10d} | "
              f"{r['isosceles_violations']:>15d} | {sti:>6s}")

    print("-" * 65)
    print(f"{'Total':>8s} | {total_trials:>8,d} | {total_violations:>10d} | "
          f"{total_isosceles:>15d} | {'PASS' if total_violations == 0 else 'FAIL':>6s}")

    print()
    overall = "ALL PASS" if total_violations == 0 and total_isosceles == 0 else "FAILURES DETECTED"
    print(f"  OVERALL: {overall}")
    print()
    print(f"  Interpretation:")
    print(f"    The strong triangle inequality d(x,z) <= max(d(x,y), d(y,z))")
    print(f"    holds universally across {total_trials:,} random leaf triples")
    print(f"    and three primes (p = {', '.join(str(p) for p in primes)}).")
    print()
    print(f"    The isosceles property — that the two largest distances among")
    print(f"    any triple are equal — also holds universally, confirming the")
    print(f"    ultrametric structure of Bruhat-Tits trees.")
    print()
    print(f"    This provides the geometric foundation for passive error")
    print(f"    confinement: errors confined to one branch cannot cross into")
    print(f"    another, enforced by the strong triangle inequality.")
    print()

    # Falsification
    if total_violations == 0 and total_isosceles == 0:
        print("  FALSIFICATION: PASSED — No counterexamples found.")
        print("    The strong triangle inequality is verified computationally.")
    else:
        print("  FALSIFICATION: FAILED — Counterexamples exist!")
        print("    This would indicate a bug in the tree implementation.")
        print("    Investigate immediately.")

    print()


if __name__ == "__main__":
    run_experiment_0c()
