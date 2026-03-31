class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
        
        visited = set()
        def dfs(src: int, prev: int):
            if src in visited:
                return False
            
            visited.add(src)
            # implicit base case. If no neighbors, the tree must be valid
            for nei in adj[src]:
                if nei == prev:
                    continue
                if not dfs(nei, src):
                    return False

            return True
        
        return dfs(0, -1) and len(visited) == n