class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}

        def dfs(r: int, c: int, prev: int) -> int:
            if (
                r < 0 or 
                c < 0 or 
                r == len(matrix) or 
                c == len(matrix[0]) or
                matrix[r][c] <= prev
                ):
                return 0
            
            if (r, c, prev) in dp:
                return dp[(r, c, prev)]
            
            longest = 0
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                longest = max(longest, 1 + dfs(r + dr, c + dc, prev=matrix[r][c]))
            dp[(r, c, prev)] = longest
            return dp[(r, c, prev)]

        result = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                result = max(result, dfs(r, c, float("-infinity")))
        return result