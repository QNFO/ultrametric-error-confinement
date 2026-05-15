"""cophenetic - Tree Distance Cophenetic Python Package.

Provides Tree class for cophenetic distance computation, ultrametric
inequality verification, and triadic rigidity testing.

Example:
    from cophenetic import Tree
    tree = Tree.demo_dendrogram()
    print(tree.distance_matrix())
"""

import itertools

class Tree:
    """Rooted tree with monotone height function for cophenetic distance."""

    def __init__(self, n_leaves, height_function, parent):
        self.n = n_leaves
        self.height = height_function
        self.parent = parent

    def lca(self, x, y):
        """Lowest common ancestor of leaves x and y."""
        path_x = self._path_to_root(x)
        path_y = self._path_to_root(y)
        for node in path_x:
            if node in path_y:
                return node
        return 0

    def _path_to_root(self, leaf):
        """List of nodes from leaf up to root (inclusive). Root is self-parent."""
        path = []
        node = leaf
        while True:
            path.append(node)
            if self.parent[node] == node:  # root: self-parent
                break
            node = self.parent[node]
        return path

    def cophenetic_distance(self, x, y):
        """d(x, y) = h(lca(x, y))."""
        if x == y:
            return 0.0
        return self.height[self.lca(x, y)]

    def distance_matrix(self):
        """Full pairwise cophenetic distance matrix."""
        D = [[0.0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(i + 1, self.n):
                d = self.cophenetic_distance(i, j)
                D[i][j] = d
                D[j][i] = d
        return D

    def check_ultrametric(self):
        """Verify ultrametric inequality for all triples."""
        for i, j, k in itertools.combinations(range(self.n), 3):
            dij = self.cophenetic_distance(i, j)
            dik = self.cophenetic_distance(i, k)
            djk = self.cophenetic_distance(j, k)
            if dik > max(dij, djk):
                return False
            if dij > max(dik, djk):
                return False
            if djk > max(dij, dik):
                return False
        return True

    def triadic_rigidity(self, epsilon=1e-10):
        """Fraction of triples where two largest distances are equal."""
        total = 0
        rigid = 0
        for i, j, k in itertools.combinations(range(self.n), 3):
            d = sorted([
                self.cophenetic_distance(i, j),
                self.cophenetic_distance(i, k),
                self.cophenetic_distance(j, k)
            ], reverse=True)
            total += 1
            if abs(d[0] - d[1]) < epsilon:
                rigid += 1
        return rigid / total if total > 0 else 0.0

    @staticmethod
    def demo_dendrogram():
        """4-item: A(Red/Large)=0, B(Red/Small)=1, C(Blue/Large)=2, D(Blue/Small)=3.

        Internal nodes: root(10, h=5), red(11, h=3), blue(12, h=3).
        Leaves at height 0, with parents linking to internal nodes.
        """
        n = 4
        ROOT, RED, BLUE = 10, 11, 12
        height = {
            ROOT: 5.0,
            RED: 3.0,
            BLUE: 3.0,
        }
        parent = {
            ROOT: ROOT,  # root self-parent
            RED: ROOT,
            BLUE: ROOT,
            0: RED,     # A -> Red
            1: RED,     # B -> Red
            2: BLUE,    # C -> Blue
            3: BLUE,    # D -> Blue
        }
        return Tree(n, height, parent)

    @staticmethod
    def euclidean_counterexample():
        """NYC, Philly, Boston: Euclidean violates triadic rigidity."""
        import math
        def euclidean(p, q):
            return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)
        cities = {'NYC': (0, 0), 'PHL': (1.5, 0), 'BOS': (2.5, 0.5)}
        names = list(cities.keys())
        d = []
        for i in range(3):
            for j in range(i+1, 3):
                d.append(euclidean(cities[names[i]], cities[names[j]]))
        d.sort(reverse=True)
        return abs(d[0] - d[1]) > 1e-10

    def __repr__(self):
        return f"Tree(n_leaves={self.n}, heights={len(self.height)} nodes)"
