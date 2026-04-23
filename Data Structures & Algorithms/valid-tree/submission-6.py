class DSU:
    def __init__(self, n):
        self.components = n
        self.parent = list(range(n))
        self.rank = [0] * (n)
    
    def find(self, node):
        """
        Not only are we finding the parent of the node, but we are also flattening the tree at every step

        Take 3 -> 2 -> 1 -> 0 for example
        0 is the parent of 3, but notice how this is a linear time operation where 3 must go through
        2 and 1 before reaching 0. With the approach before, the parents of 1, 2, and 3 are all set to 0,
        thus flattening the tree:
        3 -> 0
        2 -> 0
        1 -> 0
        0 -> 0
        """
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        # we can't merge if the nodes are already in the same set
        if pu == pv:
            return False
        
        self.components -= 1
        # We only increase rank when merging two trees of equal rank, since that’s the only case where the tree height may increase.
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu
        # Only by joining trees of approx. equal height can we ever increase the height/rank of the tree
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        dsu = DSU(n)
        for u, v in edges:
            # A cycle exists if an edge connects two nodes that already belong to the same connected component (same root).
            if not dsu.union(u, v):
                return False

        # At this point:
        # - If we ever saw a cycle, we already returned False above.
        # - So the structure is a FOREST (collection of trees, no cycles guaranteed).
        #
        # BUT a valid TREE must also be fully connected.
        # That means all nodes must belong to ONE connected component.
        #
        # dsu.components tracks how many separate groups exist:
        #   - starts at n (each node isolated)
        #   - decreases by 1 every successful union
        #   - NEVER increases incorrectly
        #
        # EXAMPLE (5 nodes, 2 edges):
        #
        #   Nodes: 0 1 2 3 4
        #
        #   Edges:
        #     0 - 1
        #     2 - 3
        #
        #   After union(0,1):
        #       {0,1}   {2}   {3}   {4}
        #       components = 4
        #
        #   After union(2,3):
        #       {0,1}   {2,3}   {4}
        #       components = 3
        #
        #   No cycle ever occurred → valid FOREST so far
        #
        #   BUT components != 1 → graph is NOT fully connected
        #
        #   So:
        #     - No cycle ✔
        #     - Not connected ✘
        #
        # Therefore NOT a valid tree
        #
        # Final rule:
        # A valid tree = (no cycles) AND (exactly one connected component)
        return dsu.components == 1