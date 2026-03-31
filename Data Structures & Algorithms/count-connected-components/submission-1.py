class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # add edges between the nodes
        adj = defaultdict(list)
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
        
        """
        adj = {
        0: [1], 
        1: [0, 2], 
        2: [1],
        3: [4],
        4: [3],
        }

        1 - 2 - 3
        |       |
        ---------
        """
        self.num_components = 0

        visited = set()
        def dfs(curr: int):
            if curr not in visited:
                visited.add(curr)

            # this must be a new component
            for nei in adj[curr]:
                if nei in visited:
                    continue
                visited.add(nei)
                dfs(nei)
        
        for num in range(n):
            if num not in visited:
                self.num_components += 1
                dfs(num)
        
        return self.num_components
                
