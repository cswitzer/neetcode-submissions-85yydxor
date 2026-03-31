class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        used to have n - 1 edges
        now, the graph contains n edges and a cycle

        objective: return an edge (not a node) that can be removed
        that allows:

        1. The graph to still be connected
        2. The graph is non-cyclical
        3. If multiple answers are possible, return the last edge that appears in edges
        """
        adj = defaultdict(list)
        
        # find where the cycle happens
        def dfs(node: int, prev: int) -> bool:
            if node in visited:
                return True
            
            visited.add(node)
            for nei in adj[node]:
                # 1 - 2 is not a cycle, but represents an undirected graph
                if nei == prev:
                    continue
                if dfs(nei, node):
                    return True
            return False
        
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
            visited = set()

            if dfs(src, -1):
                return [src, dest]
        return []

