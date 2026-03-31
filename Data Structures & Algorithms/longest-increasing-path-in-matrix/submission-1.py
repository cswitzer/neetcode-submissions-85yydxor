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
            
            # we do not need prev in dp since when we reach here, we already know
            # that matrix[r][c] is greater than prev
            if (r, c) in dp:
                return dp[(r, c)]
            
            longest = 0
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                longest = max(longest, 1 + dfs(r + dr, c + dc, prev=matrix[r][c]))
            dp[(r, c)] = longest
            return dp[(r, c)]

        result = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                result = max(result, dfs(r, c, float("-infinity")))
        return result