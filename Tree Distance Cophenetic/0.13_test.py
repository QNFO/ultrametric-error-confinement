\"\"\"0.13_test.py — Verify cophenetic package works.\"\"\"

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cophenetic import Tree

# Test 1: Import and basic operations
tree = Tree.demo_dendrogram()
assert tree.n == 4, f\"Expected 4 leaves, got {tree.n}\"

# Test 2: Distance matrix
D = tree.distance_matrix()
assert len(D) == 4
assert D[0][1] == 3.0, f\"d(A,B) should be 3, got {D[0][1]}\"
assert D[0][2] == 5.0, f\"d(A,C) should be 5, got {D[0][2]}\"

# Test 3: Ultrametric inequality
assert tree.check_ultrametric(), \"Ultrametric inequality must hold\"

# Test 4: Triadic rigidity
tri = tree.triadic_rigidity()
assert tri == 1.0, f\"Triadic rigidity should be 1.0, got {tri}\"

# Test 5: Euclidean counterexample
assert Tree.euclidean_counterexample(), \"Euclidean must violate triadic rigidity\"

# Test 6: Cophenetic distance
assert tree.cophenetic_distance(0, 0) == 0.0
assert tree.cophenetic_distance(0, 1) == 3.0

print(\"=\" * 60)
print(\"ALL TESTS PASSED\")
print(f\"  Tree: {tree}\")
print(f\"  Distance matrix: {D}\")
print(f\"  Ultrametric: {tree.check_ultrametric()}\")
print(f\"  Triadic rigidity: {tri:.3f}\")
print(f\"  Euclidean counterexample: {Tree.euclidean_counterexample()}\")
print(\"=\" * 60)
print(\"[CODE-EXECUTED] Package verified\")
