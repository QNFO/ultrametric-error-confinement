"""
0.1.py -- Ternary Ultrametric Tree for Symmetric Error Confinement

Implements a regular ternary tree (p=3, root degree=3, all internal nodes
degree=3) for passive error confinement via majority-vote decoding.

Architecture:
- Root has exactly 3 children (deviation from strict Bruhat-Tits p+1 rule)
- Every internal node has exactly 3 children
- Leaves are at depth d
- Bottom-up majority decoding: each node evaluates to the majority of its 3 children
- No ties possible since 3 is odd

Author: LLM-assisted implementation for ultrametric_v2 project
Date: 2026-05-15
"""

import random
import math
import itertools
from typing import List, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class Node:
    """A node in the ternary ultrametric tree."""
    value: int = 0
    depth: int = 0
    children: List['Node'] = field(default_factory=list)
    parent: Optional['Node'] = None

    @property
    def is_leaf(self) -> bool:
        return len(self.children) == 0

    @property
    def is_root(self) -> bool:
        return self.parent is None


def build_tree(depth: int, p: int = 3) -> Node:
    """Build a regular p-ary tree. Root also has p children (not p+1)."""
    if depth < 0:
        raise ValueError(f"depth must be >= 0, got {depth}")
    if p < 2:
        raise ValueError(f"p must be >= 2, got {p}")
    root = Node(depth=0)
    _build_subtree(root, depth, p)
    return root


def _build_subtree(parent: Node, remaining_depth: int, p: int) -> None:
    if remaining_depth == 0:
        return
    for _ in range(p):
        child = Node(depth=parent.depth + 1, parent=parent)
        parent.children.append(child)
        _build_subtree(child, remaining_depth - 1, p)


def copy_tree(node: Node, parent: Optional[Node] = None) -> Node:
    """Deep copy a tree starting from node."""
    copy = Node(value=node.value, depth=node.depth, parent=parent)
    for child in node.children:
        child_copy = copy_tree(child, parent=copy)
        copy.children.append(child_copy)
    return copy


def get_leaves(root: Node) -> List[Node]:
    """Return all leaf nodes in DFS order."""
    leaves = []
    def collect(n):
        if n.is_leaf:
            leaves.append(n)
        else:
            for c in n.children:
                collect(c)
    collect(root)
    return leaves


def leaf_count(depth: int, p: int = 3) -> int:
    """Return number of leaves: p^depth."""
    return p ** depth


def total_nodes(depth: int, p: int = 3) -> int:
    """Return total nodes: (p^(depth+1) - 1) / (p - 1)."""
    return (p ** (depth + 1) - 1) // (p - 1)


def _count_nodes(node: Node) -> int:
    return 1 + sum(_count_nodes(c) for c in node.children)


def encode(root: Node, logical_bit: int) -> None:
    """Encode a logical bit by setting all leaf values."""
    if logical_bit not in (0, 1):
        raise ValueError(f"logical_bit must be 0 or 1, got {logical_bit}")
    for leaf in get_leaves(root):
        leaf.value = logical_bit


def decode(root: Node) -> int:
    """Decode via bottom-up majority vote."""
    def _decode(n):
        if n.is_leaf:
            return n.value
        child_values = [_decode(c) for c in n.children]
        result = _majority(child_values)
        n.value = result
        return result
    return _decode(root)


def _majority(values: List[int]) -> int:
    """Majority: 1 if more 1s than 0s, else 0."""
    ones = sum(values)
    zeros = len(values) - ones
    return 1 if ones > zeros else 0


def apply_noise(root: Node, p_err: float, rng: Optional[random.Random] = None) -> List[bool]:
    """Apply i.i.d. bit-flip noise to all leaf values."""
    if rng is None:
        rng = random.Random()
    leaves = get_leaves(root)
    flipped = []
    for leaf in leaves:
        if rng.random() < p_err:
            leaf.value = 1 - leaf.value
            flipped.append(True)
        else:
            flipped.append(False)
    return flipped


def run_trial(depth: int, p_err: float, logical_bit: int,
              seed: Optional[int] = None) -> Tuple[bool, int]:
    """Run a single Monte Carlo trial. Returns (error_occurred, decoded_bit)."""
    rng = random.Random(seed)
    tree = build_tree(depth, p=3)
    encode(tree, logical_bit)
    apply_noise(tree, p_err, rng=rng)
    decoded = decode(tree)
    error = (decoded != logical_bit)
    return error, decoded


def run_experiment(depth: int, p_err_list: List[float],
                   n_trials: int = 500, seed: int = 42,
                   logical_bit: int = 0) -> dict:
    """Run Monte Carlo experiment across multiple p_err values."""
    results = []
    for p_err in p_err_list:
        errors = 0
        for trial in range(n_trials):
            trial_seed = seed + trial
            error_occurred, _ = run_trial(depth, p_err, logical_bit, seed=trial_seed)
            if error_occurred:
                errors += 1
        ler = errors / n_trials
        results.append({
            "p_err": p_err,
            "errors": errors,
            "n_trials": n_trials,
            "ler": ler
        })
    return {
        "depth": depth,
        "logical_bit": logical_bit,
        "n_trials": n_trials,
        "results": results
    }


def wilson_ci(successes: int, n: int, z: float = 1.96) -> Tuple[float, float]:
    """Wilson score confidence interval for a binomial proportion."""
    if n == 0:
        return (0.0, 1.0)
    p_hat = successes / n
    denominator = 1 + z**2 / n
    center = (p_hat + z**2 / (2 * n)) / denominator
    margin = z * math.sqrt((p_hat * (1 - p_hat) + z**2 / (4 * n)) / n) / denominator
    lower = max(0.0, center - margin)
    upper = min(1.0, center + margin)
    return (lower, upper)


def energy_barrier(depth: int, p: int = 3) -> int:
    """Minimum leaf flips to flip root: ceil(p/2)^d."""
    return int(math.ceil(p / 2) ** depth)


def energy_barrier_table(max_depth: int = 10, p: int = 3) -> List[Tuple[int, int, int]]:
    """Generate energy barrier table for depths 1..max_depth."""
    return [(d, leaf_count(d, p), energy_barrier(d, p)) for d in range(1, max_depth + 1)]


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== Ternary Ultrametric Tree -- Self-Test ===")

    # Test tree construction
    for d in [0, 1, 2, 3]:
        tree = build_tree(d, p=3)
        leaves = get_leaves(tree)
        assert len(leaves) == leaf_count(d)
        assert _count_nodes(tree) == total_nodes(d)
    print("Tree construction: PASS (d=0..3)")

    # Test encode/decode roundtrip
    for d in [1, 2, 3, 4]:
        for bit in [0, 1]:
            tree = build_tree(d, p=3)
            encode(tree, bit)
            assert decode(tree) == bit
    print("Encode/decode roundtrip: PASS (all depths, both bits)")

    # Zero-noise trials
    for d in [1, 2, 3, 4]:
        for bit in [0, 1]:
            error, _ = run_trial(d, 0.0, bit, seed=42)
            assert not error
    print("Zero-noise trials: PASS")

    # Full-noise trials
    for d in [1, 2, 3]:
        for bit in [0, 1]:
            error, _ = run_trial(d, 1.0, bit, seed=42)
            assert error
    print("Full-noise trials: PASS")

    # Copy tree test
    tree = build_tree(2, p=3)
    encode(tree, 1)
    tree_copy = copy_tree(tree)
    assert decode(tree) == decode(tree_copy) == 1
    for leaf in get_leaves(tree_copy):
        leaf.value = 0
    assert decode(tree) == 1
    assert decode(tree_copy) == 0
    print("copy_tree: PASS")

    # Energy barrier table
    print()
    print("=== Energy Barrier Table ===")
    print(f"{'Depth':>6} {'Leaves':>8} {'Barrier':>8} {'Fraction':>10}")
    for d, n_leaves, barrier in energy_barrier_table(8):
        frac = barrier / n_leaves
        print(f"{d:>6} {n_leaves:>8} {barrier:>8} {frac:>10.6f}")

    print()
    print("All self-tests passed!")
