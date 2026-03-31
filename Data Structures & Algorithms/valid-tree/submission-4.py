class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for src, dest in edges:
            """
            both directions since this is an undirected graph
            **Without bidirectional edges** (`adj[src].append(dest)` only):

            adj[1] = [0, 2]
            adj[0] = []  # ← Problem!
            adj[2] = []

            Then, when we start from 0 in the code, this fails since 0 'has no neighbors',
            which is false since 0 does have a neighbor '1'
            """
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