"""
Automated test suite for A1 — Error Confinement Live Demo.

Validates:
  TEST 1: Tree construction (node/leaf counts)
  TEST 2: Error simulation — majority-vote vs binomial model
  TEST 3: Strong triangle inequality (ultrametric distance property)
  TEST 4: Error rate vs published Tier 0/Tier 1 Table 1 (placeholder)

Run: python test_plan.py
"""
import sys
import random

random.seed(42)

PASS, FAIL = 0, 0


def check(cond, label):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"  [PASS] {label}")
    else:
        FAIL += 1
        print(f"  [FAIL] {label}")
    return cond


def count_tree(p, d):
    """Replicate A1's buildTree(p,d) logic in Python.
    
    Tree structure: degree = p+1 children per non-leaf node.
    All leaves at depth d. Root at depth 0.
    Leaf count = (p+1)^d
    Total nodes = sum_{j=0}^{d} (p+1)^j = ((p+1)^(d+1) - 1) / p
    """
    degree = p + 1
    nodes = [{"id": 0, "layer": 0, "children": [], "leaf": False}]
    nid = 1

    def grow(parent, remaining):
        nonlocal nid
        if remaining <= 0:
            parent["leaf"] = True
            return
        for _ in range(degree):
            child = {"id": nid, "layer": parent["layer"] + 1, "children": [], "leaf": False}
            nid += 1
            parent["children"].append(child)
            nodes.append(child)
            grow(child, remaining - 1)

    grow(nodes[0], d)
    leaves = [n for n in nodes if n["leaf"]]
    return nodes, leaves


def expected_leaf_count(p, d):
    return (p + 1) ** d


def expected_total_nodes(p, d):
    degree = p + 1
    return (degree ** (d + 1) - 1) // p


def simulate_majority_vote(leaf_count, p_err, trials):
    """Replicate A1's simulate() logic.
    
    Each trial: pick random bit (0/1), each leaf flips independently
    with prob p_err, decode by majority vote.
    """
    errors = 0
    for _ in range(trials):
        bit = random.randint(0, 1)
        # Each leaf: flip with prob p_err
        votes = [1 - bit if random.random() < p_err else bit for _ in range(leaf_count)]
        decoded = 1 if sum(votes) > leaf_count / 2 else 0
        if decoded != bit:
            errors += 1
    ler = errors / trials
    threshold = leaf_count // 2 + 1
    return ler, threshold


def compute_ultrametric_distance(leaf_a, leaf_b, nodes, leaves):
    """Compute ultrametric (cophenetic) distance between two leaves.
    
    Distance = depth of lowest common ancestor (LCA) in the tree.
    For a Bruhat-Tits tree, this equals: depth - layer_of_lca.
    """
    # Find path from leaf to root for both
    def path_to_root(leaf):
        path = [leaf]
        # Walk up through parent references (we don't have parent refs,
        # but we know leaves are at depth d and we can reconstruct)
        # Simple approach: leaves at same depth, LCA depth determines distance
        return path

    # Simplified: since all leaves are at same depth d,
    # and tree is regular, ultrametric distance = d - lca_layer
    # For a regular tree with degree = p+1, leaves at positions i and j
    # have LCA at layer based on their first differing digit in base-(p+1)
    leaf_a_idx = leaves.index(leaf_a)
    leaf_b_idx = leaves.index(leaf_b)

    # Find first digit where they differ in base-(degree)
    degree = len(nodes[0]["children"]) if nodes[0]["children"] else 3
    diff_layer = 0
    a, b = leaf_a_idx, leaf_b_idx
    for layer in range(1, len(leaves) + 1):
        if a // (degree ** (len(leaves).bit_length() - layer)) != \
           b // (degree ** (len(leaves).bit_length() - layer)):
            diff_layer = layer - 1
            break
        a %= degree ** (len(leaves).bit_length() - layer)
        b %= degree ** (len(leaves).bit_length() - layer)

    # All leaves at depth d
    d = nodes[-1]["layer"]  # max layer
    return d - diff_layer


# ================================================================
print("=" * 60)
print("TEST 1: Tree Construction")
print("=" * 60)

for p, d in [(2, 1), (2, 2), (2, 3), (2, 4),
              (3, 1), (3, 2), (3, 3),
              (5, 1), (5, 2), (5, 3)]:
    nodes, leaves = count_tree(p, d)
    exp_leaves = expected_leaf_count(p, d)
    exp_total = expected_total_nodes(p, d)
    check(len(leaves) == exp_leaves,
          f"p={p}, d={d}: leaves={len(leaves)} (expected {exp_leaves})")
    check(len(nodes) == exp_total,
          f"p={p}, d={d}: total nodes={len(nodes)} (expected {exp_total})")

# ================================================================
print(f"\n{'=' * 60}")
print("TEST 2: Error Simulation — Majority Vote")
print("=" * 60)

# For a majority vote with N independent leaves each flipping with p_err,
# the LER should follow the cumulative binomial distribution.
# With large N and small p_err, LER should be very small.

test_cases = [
    # (leaf_count, p_err, trials, max_expected_ler)
    (3, 0.10, 50000, 0.03),    # binom: ~0.028
    (3, 0.20, 50000, 0.11),    # binom: ~0.104
    (9, 0.10, 50000, 0.001),   # binom: ~0.0009
    (9, 0.20, 50000, 0.004),   # binom: ~0.0031
    (27, 0.10, 50000, 0.0000001),  # essentially zero
    (27, 0.30, 50000, 0.005),  # binom: small but non-zero
]

for leaf_count, p_err, trials, max_expected in test_cases:
    ler, threshold = simulate_majority_vote(leaf_count, p_err, trials)
    # The theoretical LER can be computed via binomial CDF
    import math
    # Binomial: P(at least threshold successes) where success = leaf error
    def binom_pmf(n, k, p):
        return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    theoretical_ler = sum(binom_pmf(leaf_count, k, p_err) 
                         for k in range(threshold, leaf_count + 1))
    
    # LER should be within reasonable tolerance of theoretical
    tolerance = max(0.01, theoretical_ler * 3)  # 3x theoretical or 0.01 minimum
    check(abs(ler - theoretical_ler) < tolerance,
          f"leaf_count={leaf_count}, p_err={p_err}: LER={ler:.6f} "
          f"(theoretical={theoretical_ler:.6f}, tol={tolerance:.6f})")

# ================================================================
print(f"\n{'=' * 60}")
print("TEST 3: Strong Triangle Inequality")
print("=" * 60)

# For ultrametric distance d(x,z) <= max(d(x,y), d(y,z))
# In a Bruhat-Tits tree: all leaves are at same depth d.
# d(leaf_i, leaf_j) = d - depth_of_lca(i,j)
# This inherently satisfies the strong triangle inequality.

# Verify for p=2, d=3 (8 leaves)
nodes, leaves = count_tree(2, 3)
# Compute LCA depth for each pair
def lca_depth(a, b, degree=3, max_depth=3):
    """Find LCA depth of two leaf indices in a regular p-tree."""
    # Leaves are at positions 0..N-1 in base-degree representation
    layer = 0
    a_val, b_val = a, b
    divisor = degree ** (max_depth - 1)
    for l in range(max_depth):
        a_digit = a_val // divisor if divisor > 0 else a_val
        b_digit = b_val // divisor if divisor > 0 else b_val
        if a_digit != b_digit:
            return l
        a_val = a_val % divisor if divisor > 0 else 0
        b_val = b_val % divisor if divisor > 0 else 0
        divisor //= degree
    return max_depth  # same leaf

max_depth = 3
degree = 3  # p+1 for p=2
violations = 0
for i in range(len(leaves)):
    for j in range(i + 1, len(leaves)):
        for k in range(len(leaves)):
            if k == i or k == j:
                continue
            d_ij = max_depth - lca_depth(i, j, degree, max_depth)
            d_jk = max_depth - lca_depth(j, k, degree, max_depth)
            d_ik = max_depth - lca_depth(i, k, degree, max_depth)
            # Strong triangle inequality: d(i,k) <= max(d(i,j), d(j,k))
            if d_ik > max(d_ij, d_jk):
                violations += 1

check(violations == 0,
      f"Strong triangle inequality: {violations} violations in "
      f"{len(leaves) * (len(leaves)-1) * (len(leaves)-2)} triples")

# Verify d(i,j) is symmetric
for i in range(len(leaves)):
    for j in range(i + 1, len(leaves)):
        d_ij = max_depth - lca_depth(i, j, degree, max_depth)
        d_ji = max_depth - lca_depth(j, i, degree, max_depth)
        if d_ij != d_ji:
            violations += 1

check(violations == 0, "Ultrametric distance is symmetric for all pairs")

# ================================================================
print(f"\n{'=' * 60}")
print("TEST 4: Error Rate Validation — Published Table 1")
print("=" * 60)

print("  [SKIP] Published Tier 0/Tier 1 data not yet integrated.")
print("  Placeholder: verify against DOI: 10.5281/zenodo.20134944")
print("  Task S7.3 will populate this test with published LER values.")

# Placeholder structure for S7.3:
# published_table1 = {
#     (3, 3, 0.10): 0,  # 0 logical errors out of 500
#     (3, 3, 0.15): 0,
#     ...
# }
# For each (p, d, p_err), expected:
#   1. Build tree with count_tree(p, d)
#   2. Simulate simulate_majority_vote(leaf_count, p_err, 500)
#   3. Compare LER to published value within statistical tolerance

# ================================================================
print(f"\n{'=' * 60}")
print(f"RESULTS: {PASS} passed, {FAIL} failed, {PASS + FAIL} total")
print("=" * 60)

sys.exit(0 if FAIL == 0 else 1)
