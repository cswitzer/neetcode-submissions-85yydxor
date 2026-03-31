class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visited = set()
        dp = {}

        def dfs(r: int, c: int) -> int:
            if r == m or c == n:
                return 0
            
            if r == m - 1 and c == n - 1:
                return 1
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            num_paths = 0
            for dr, dc in [(1, 0), (0, 1)]:
                num_paths += dfs(r + dr, c + dc)
            
            dp[(r, c)] = num_paths
            return dp[(r, c)]
        
        return dfs(0, 0)
