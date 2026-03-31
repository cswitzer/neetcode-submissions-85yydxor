class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}

        def dfs(r: int, c: int) -> int:
            if (r, c) in dp:
                return dp[(r, c)]
            if r == len(text1) or c == len(text2):
                return 0
            
            if text1[r] == text2[c]:
                dp[(r, c)] = 1 + dfs(r + 1, c + 1)
            else:
                dp[(r, c)] = max(dfs(r + 1, c), dfs(r, c + 1))
            return dp[(r, c)]

        return dfs(0, 0)